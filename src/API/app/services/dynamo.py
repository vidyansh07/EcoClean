"""
DynamoDB Service Module

This module provides a service layer for interacting with AWS DynamoDB.
It handles all CRUD operations for sensor data storage and retrieval.

Author: Vidyansh
Date: 2025-11-09
Version: 1.6.8
"""

import datetime
from dateutil import parser
import boto3
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource, Table
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from logging import Logger as logger
from typing import Dict, List, Any

# Initialize AWS connection
# Uses default boto3 session for AWS credentials
car_bon_connection = boto3


class dynamo:
    """
    DynamoDB Service Class
    
    Provides methods for interacting with DynamoDB tables for IoT sensor data.
    Implements the Repository pattern for data access abstraction.
    
    Attributes:
        dynamodb (DynamoDBServiceResource): DynamoDB resource instance
        table (Table): Reference to the specific DynamoDB table
    """
    def __init__(self, table_name: str) -> None:
        """
        Initialize DynamoDB service with specified table.
        
        Args:
            table_name (str): Name of the DynamoDB table to interact with
        """
        self.dynamodb: DynamoDBServiceResource = car_bon_connection.resource("dynamodb")
        self.table: Table = self.dynamodb.Table(table_name)

    def get_tables(self) -> List[str]:
        """
        Retrieve list of all DynamoDB tables in the account.
        
        Returns:
            List[str]: List of table names
        """
        response = self.dynamodb.tables.all()
        all_tables = []
        for table in response:
            all_tables.append(table.name)
        return all_tables

    def get_dynamo_data(self, device_id: str, timestamp: int) -> Dict[str, Any]:
        """
        Retrieve a single sensor reading from DynamoDB.
        
        Args:
            device_id (str): Unique identifier for the IoT device
            timestamp (int): Unix timestamp of the reading
            
        Returns:
            Dict[str, Any]: Formatted sensor data including CO PPM calculation
        """
        response = self.table.get_item(
            Key={"device_id": device_id, "timestamp": timestamp}
        )
        item = response["Item"]
        CO_PPM_value = self.Calculate_ppm(float(item["CO"]))
        result = {
            "device_id": item["device_id"],
            "timestamp": int(item["timestamp"]),
            "sensor_values": {"CO": item["CO"], "temperature": 0, "humidity": 0, "CO_PPM": CO_PPM_value},
        }
        return result

    def get_last_Updated_value(self, device_id: str) -> Dict[str, Any]:
        """
        Get the most recent sensor reading for a specific device.
        
        Uses descending timestamp sort to efficiently retrieve latest record.
        
        Args:
            device_id (str): Unique identifier for the IoT device
            
        Returns:
            Dict[str, Any]: Most recent sensor data with calculated CO PPM
        """
        response = self.table.query(
            KeyConditionExpression=Key("device_id").eq(device_id),
            ScanIndexForward=False,  # Sort descending by timestamp
            Limit=1,  # Only get the most recent record
        )
        response.pop("ResponseMetadata")
        item = response["Items"][0]
        CO_PPM_value = self.Calculate_ppm(float(item["CO"]))
        result = {
            "device_id": item["device_id"],
            "timestamp": int(item["timestamp"]),
            "sensor_values": {"CO": item["CO"], "temperature": 0, "humidity": 0, "CO_PPM": CO_PPM_value},
        }
        return result

    def get_data_between_timestamps(
        self, device_id: str, from_timestamp: str, to_timestamp: str
    ) -> Dict[str, Any]:
        """
        Query sensor readings within a specified time range.
        
        This method supports flexible timestamp formats and filters out zero CO readings.
        
        Args:
            device_id (str): Unique identifier for the IoT device
            from_timestamp (str): Start timestamp (Unix or ISO 8601 format)
            to_timestamp (str): End timestamp (Unix or ISO 8601 format)
            
        Returns:
            Dict[str, Any]: Dictionary containing:
                - Results: List of sensor readings
                - Metadata: Count of total results
                
        Raises:
            ClientError: If DynamoDB query fails
        """
        # Try to parse timestamps if they're in ISO 8601 format
        try:
            from_timestamp = str(parser.parse(from_timestamp).timestamp())
            to_timestamp = str(parser.parse(to_timestamp).timestamp())
            print(f"From Timestamp : {from_timestamp}, To Timestamp : {to_timestamp}")
        except Exception as e:
            print(f"Failed to parse due to following exception:\n{e}")
            # Use timestamps as-is if parsing fails
            from_timestamp = from_timestamp
            to_timestamp = to_timestamp
        
        try:
            response = self.table.query(
                KeyConditionExpression=Key("device_id").eq(device_id)
                & Key("timestamp").between(from_timestamp, to_timestamp)
            )
        except ClientError as err:
            logger.error(
                "Couldn't query dynamo db. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        
        # Transform DynamoDB items to application format
        results = [
            {
                "device_id": item["device_id"],
                "timestamp": int(item["timestamp"]),
                "sensor_values": {"CO": item["CO"], "temperature": 0, "humidity": 0 , "CO_PPM": self.Calculate_ppm(float(item["CO"]))},
            }
            for item in response["Items"]
        ]
        
        # Filter out invalid readings (CO = 0 typically indicates sensor error)
        filtered_results = [
            item for item in results if item["sensor_values"]["CO"] != 0
        ]
        return {"Results": filtered_results, "Metadata": {"count": len(results)}}

    def update_table(self, device_id: str, Temp: str, Hum: str, CO: str) -> Dict[str, Any]:
        """
        Add a new sensor reading to the DynamoDB table.
        
        Automatically generates timestamp for the reading.
        
        Args:
            device_id (str): Unique identifier for the IoT device
            Temp (str): Temperature reading in Celsius
            Hum (str): Humidity reading in percentage
            CO (str): Carbon monoxide sensor raw value
            
        Returns:
            Dict[str, Any]: Contains the item and write status
            
        Raises:
            ClientError: If DynamoDB write operation fails
        """
        try:
            new_item = {
                "device_id": device_id,
                "timestamp": int(datetime.datetime.now().timestamp()),
                "temperature": Temp,
                "humidity": Hum,
                "CO": CO,
            }
            self.table.put_item(Item=new_item)
            return {"Item": new_item, "write_successful": True}
        except ClientError as err:
            logger.error(
                "Couldn't add Device %s data to table %s. Here's why: %s: %s",
                device_id,
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
    
    def Calculate_ppm(self, value: float) -> float:
        """
        Convert raw sensor value to Parts Per Million (PPM).
        
        Uses calibration formula specific to MQ-7 CO sensor:
        PPM = ((((5 - (value/102400)*5.0)/5)/26)*1000)
        
        Args:
            value (float): Raw analog sensor reading (0-1023)
            
        Returns:
            float: Carbon monoxide concentration in PPM
            
        Note:
            This formula assumes:
            - 5V supply voltage
            - 10-bit ADC (1024 levels)
            - MQ-7 sensor characteristics
        """
        ppm_value = ((((5-(value/(1024*100))*5.0)/5)/26)*1000)
        return ppm_value