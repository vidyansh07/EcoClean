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
    """
    User data model with Pydantic validation.
    
    Uses ULID for unique, sortable identifiers.
    
    Attributes:
        id: Universally Unique Lexicographically Sortable Identifier
        name: User's full name
        registered_device_id: IoT device identifier associated with user
        personal_contact: Primary phone number in E.164 format
        secondary_contacts: Optional list of additional contact numbers
        emergency_contacts: Dictionary of emergency service numbers
    """
    id: str = str(ULID())
    name: str
    registered_device_id: str
    personal_contact: str
    secondary_contacts: Optional[List[str]]
    emergency_contacts: dict = emergency_contacts().model_dump()

    class Config:
        arbitrary_types_allowed = True


class user_service:
    """
    User Service for managing user profiles and device registrations.
    
    Implements the Repository pattern for user data access.
    """
    
    def __init__(self) -> None:
        """
        Initialize user service with DynamoDB connection.
        """
        table_name = "user_table"
        self.dynamodb: DynamoDBServiceResource = CAR_BON_CONNECTION.resource("dynamodb")
        self.table: Table = self.dynamodb.Table(table_name)

    def create_user(
        self, name: str, device_id: str, personal_contact: str, secondary_contacts: List = None
    ) -> user_class:
        """
        Create a new user profile in the system.
        
        Generates a unique ULID for the user and stores profile in DynamoDB.
        Automatically includes emergency contact numbers.
        
        Args:
            name: User's full name
            device_id: IoT device identifier to register
            personal_contact: Primary phone number (E.164 format recommended)
            secondary_contacts: Optional list of additional contact numbers
            
        Returns:
            user_class: Created user object with all fields populated
            
        Raises:
            ClientError: If DynamoDB write operation fails
            
        Example:
            >>> user = create_user(
            ...     "John Doe",
            ...     "ESP32_001",
            ...     "+919876543210",
            ...     ["+919876543211"]
            ... )
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

    def get_user(self, user_id: str) -> user_class:
        """
        Retrieve user profile by ID.
        
        Args:
            user_id: ULID of the user
            
        Returns:
            user_class: User object with all profile data
            
        Raises:
            IndexError: If user not found
            ClientError: If DynamoDB query fails
            
        Example:
            >>> user = get_user("01HANV3Y7Z8QZXJW2K3P4M5N6")
        """
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
