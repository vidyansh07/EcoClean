import datetime
from dateutil import parser
import boto3
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource, Table
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from logging import Logger as logger

# try:
#     car_bon_connection = boto3.Session(profile_name="AdministratorAccess-956047403479", region_name="us-east-1")
# except:
car_bon_connection = boto3


class dynamo:
    def __init__(self, table_name) -> None:
        self.dynamodb: DynamoDBServiceResource = car_bon_connection.resource("dynamodb")
        self.table: Table = self.dynamodb.Table(table_name)

    def get_tables(self):
        response = self.dynamodb.tables.all()
        all_tables = []
        for table in response:
            all_tables.append(table.name)
        return all_tables

    def get_dynamo_data(self, device_id, timestamp):
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

    def get_last_Updated_value(self, device_id):
        response = self.table.query(
            KeyConditionExpression=Key("device_id").eq(device_id),
            ScanIndexForward=False,
            Limit=1,
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
    ):
        # try:
        #     from_timestamp = str(datetime.datetime.fromtimestamp(int(from_timestamp) / 1e3).timestamp())
        #     to_timestamp = str(datetime.datetime.fromtimestamp(int(to_timestamp) / 1e3).timestamp())
        # except Exception as e:
        #     print(e)
        try:
            from_timestamp = str(parser.parse(from_timestamp).timestamp())
            to_timestamp = str(parser.parse(to_timestamp).timestamp())
            print(f"From Timestamp : {from_timestamp}, To Timestamp : {to_timestamp}")
        except Exception as e:
            print(f"Failed to parse due to following exception:\n{e}")
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
        results = [
            {
                "device_id": item["device_id"],
                "timestamp": int(item["timestamp"]),
                "sensor_values": {"CO": item["CO"], "temperature": 0, "humidity": 0 , "CO_PPM": self.Calculate_ppm(float(item["CO"]))},
            }
            for item in response["Items"]
        ]
        filtered_results = [
            item for item in results if item["sensor_values"]["CO"] != 0
        ]
        return {"Results": filtered_results, "Metadata": {"count": len(results)}}

    def update_table(self, device_id, Temp, Hum, CO) -> None:
        """
        Adds an item to the table.

        :param Temp: Temp value
        :param Hum: Hum value
        :param CO: CO value
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
    
    def Calculate_ppm(self, value):
        ppm_value = ((((5-(value/(1024*100))*5.0)/5)/26)*1000)
        return ppm_value