import React, { useEffect, useState } from 'react';
import AWS from 'aws-sdk';

const DynamoDbDataFetcher = ({ tableName, device_id }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const client = new AWS.DynamoDB.DocumentClient();

    client.query({
      ExpressionAttributeValues: {
        ":device_id": device_id
      },
      TableName: tableName,
      KeyConditionExpression: "device_id = :device_id",
    }).promise()
      .then(response => {
        // console.info(response.Items)
        setData(response.Items);
      })
      .catch(error => {
        console.error(error);
      });
  }, [tableName, device_id]);

  return (
    <div>
      {data.map(item => JSON.parse`{"timestamp":"${item.timestamp}","CO":"${item.payload.CO}"}`)}
    </div>
  );
};

export default DynamoDbDataFetcher;