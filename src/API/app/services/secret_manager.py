import boto3
from botocore.exceptions import ClientError
from mypy_boto3_secretsmanager.client import SecretsManagerClient
from mypy_boto3_secretsmanager.type_defs import GetSecretValueResponseTypeDef


def get_secret(my_secret_name):
    secret_name = my_secret_name
    region_name = "us-east-1"

    session = boto3.session.Session()
    client: SecretsManagerClient = session.client(
        service_name="secretsmanager",
        region_name=region_name,
    )
    try:
        client.get_secret_value(SecretId=secret_name)
    except Exception as e:
        print(e)
    try:
        get_secret_value_response: GetSecretValueResponseTypeDef = (
            client.get_secret_value(SecretId=secret_name)
        )
        if "SecretString" in get_secret_value_response:
            text_secret_data = get_secret_value_response["SecretString"]
            output_data = text_secret_data
        else:
            binary_secret_data = get_secret_value_response["SecretBinary"]
            output_data = binary_secret_data

        return output_data
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            print("The requested secret " + secret_name + " was not found")
        elif e.response["Error"]["Code"] == "InvalidRequestException":
            print("The request was invalid due to:", e)
        elif e.response["Error"]["Code"] == "InvalidParameterException":
            print("The request had invalid params:", e)
        elif e.response["Error"]["Code"] == "DecryptionFailure":
            print(
                "The requested secret can't be decrypted using the provided KMS key:", e
            )
        elif e.response["Error"]["Code"] == "InternalServiceError":
            print("An error occurred on service side:", e)

        # Your code goes here.