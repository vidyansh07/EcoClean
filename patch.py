from datetime import datetime
import boto3
from boto3.dynamodb.conditions import Key

db_client = boto3.resource("dynamodb", region_name="us-east-1")
table_res = db_client.Table("Car_Bon_Data")
table_new = db_client.Table("CarBon_Data")


not_finished = True
ret = table_res.scan()
while not_finished:
    for item in ret["Items"]:
        if "timestamp" in item and isinstance(item["timestamp"], str):
            new_item = item
            print(new_item)
            new_item["timestamp"] = int(
                float(
                    datetime.strptime(item["timestamp"], "%d-%m-%Y %H:%M").timestamp()
                )
            )
            print("fixing {} -> {}".format(item["timestamp"], new_item["timestamp"]))

            table_new.put_item(Item=new_item)
    if "LastEvaluatedKey" in ret:
        last_key = ret["LastEvaluatedKey"]
        ret = table_res.scan(ExclusiveStartKey=last_key)
    else:
        not_finished = False
