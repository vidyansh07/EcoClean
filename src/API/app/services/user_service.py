"""
User Service Module

This module handles user management operations including user creation,
retrieval, and contact management for the Car-Bon IoT system.

Author: Vidyansh
Date: 2025-11-09
Version: 1.6.8
"""

from typing import List, Optional
from ulid import ULID
from pydantic import BaseModel
import boto3
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource, Table
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from logging import Logger as logger

# AWS connection instance
CAR_BON_CONNECTION = boto3


class emergency_contacts(BaseModel):
    """
    Emergency contact numbers model.
    
    Contains standard emergency service numbers for India.
    Can be customized based on user's country.
    """
    primary_sos: str = "100"  # Police
    primary_fire: str = "101"  # Fire
    primary_health: str = "102"  # Ambulance
    secondary_health: str = "108"  # Emergency Ambulance
    primary_NHH: str = "1033"  # National Highway Helpline
    primary_DM: str = "1078"  # Disaster Management
    primary_NHAI: str = "1800-11-6062"  # National Highway Authority


class user_class(BaseModel):
    id: str = str(ULID())
    name: str
    registered_device_id: str
    personal_contact: str
    secondary_contacts: Optional[List[str]]
    emergency_contacts: dict = emergency_contacts().model_dump()

    class Config:
        arbitrary_types_allowed = True


class user_service:
    def __init__(self) -> None:
        table_name = "user_table"
        self.dynamodb: DynamoDBServiceResource = CAR_BON_CONNECTION.resource("dynamodb")
        self.table: Table = self.dynamodb.Table(table_name)

    def create_user(
        self, name: str, device_id: str, personal_contact: str, secondary_contacts: List = None
    ) -> user_class:
        """
        Adds an item to the table.

        :param name: User Name
        :param device_id: Device Id
        :param personal_contact: Personal Contact Number
        :param secondary_contacts (Optional) : List of secondary contacts to notify in case personal contact is not reachable.
        """
        try:
            new_user = user_class(
                name=name,
                registered_device_id=device_id,
                personal_contact=personal_contact,
                secondary_contacts=secondary_contacts,
            )
            self.table.put_item(Item=new_user.model_dump())
            return new_user
        except ClientError as err:
            logger.error(
                "Couldn't add User %s's data to table %s. Here's why: %s: %s",
                name,
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def get_user(self, user_id) -> user_class:
        response = self.table.query(
            KeyConditionExpression=Key("id").eq(user_id),
        )
        response.pop("ResponseMetadata")
        item = response["Items"][0]
        result = user_class(**item)
        return result


# user_name = "Gunpreet Singh"
# user_device_id = "test_random_Id_ESP32"
# personal_contact = "9992371909"
# secondary_contacts = None

# user_service_instance = user_service()

# user_instance = user_service_instance.create_user(
#     user_name, user_device_id, personal_contact, secondary_contacts
# )

# # user_instance = user_class(
# #     name = user_name,
# #     registered_device_id = user_device_id,
# #     personal_contact = personal_contact,
# #     secondary_contacts = secondary_contacts,
# # )

# print(user_instance)
# print(user_service_instance.model_dump())
