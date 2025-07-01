"""
Type annotations for sqs service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/type_defs/)

Usage::

    ```python
    from mypy_boto3_sqs.type_defs import AddPermissionRequestQueueAddPermissionTypeDef

    data: AddPermissionRequestQueueAddPermissionTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    MessageSystemAttributeNameType,
    QueueAttributeFilterType,
    QueueAttributeNameType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddPermissionRequestQueueAddPermissionTypeDef",
    "AddPermissionRequestRequestTypeDef",
    "BatchResultErrorEntryTypeDef",
    "BlobTypeDef",
    "CancelMessageMoveTaskRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ChangeMessageVisibilityBatchRequestEntryTypeDef",
    "ChangeMessageVisibilityBatchResultEntryTypeDef",
    "ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef",
    "ChangeMessageVisibilityRequestRequestTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "CreateQueueRequestServiceResourceCreateQueueTypeDef",
    "DeleteMessageBatchRequestEntryTypeDef",
    "DeleteMessageBatchResultEntryTypeDef",
    "DeleteMessageRequestRequestTypeDef",
    "DeleteQueueRequestRequestTypeDef",
    "GetQueueAttributesRequestRequestTypeDef",
    "GetQueueUrlRequestRequestTypeDef",
    "GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef",
    "PaginatorConfigTypeDef",
    "ListDeadLetterSourceQueuesRequestRequestTypeDef",
    "ListMessageMoveTasksRequestRequestTypeDef",
    "ListMessageMoveTasksResultEntryTypeDef",
    "ListQueueTagsRequestRequestTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "MessageAttributeValueTypeDef",
    "PurgeQueueRequestRequestTypeDef",
    "ReceiveMessageRequestQueueReceiveMessagesTypeDef",
    "ReceiveMessageRequestRequestTypeDef",
    "RemovePermissionRequestQueueRemovePermissionTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "SendMessageBatchResultEntryTypeDef",
    "SetQueueAttributesRequestQueueSetAttributesTypeDef",
    "SetQueueAttributesRequestRequestTypeDef",
    "StartMessageMoveTaskRequestRequestTypeDef",
    "TagQueueRequestRequestTypeDef",
    "UntagQueueRequestRequestTypeDef",
    "MessageAttributeValueQueueTypeDef",
    "MessageSystemAttributeValueTypeDef",
    "CancelMessageMoveTaskResultTypeDef",
    "CreateQueueResultTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetQueueAttributesResultTypeDef",
    "GetQueueUrlResultTypeDef",
    "ListDeadLetterSourceQueuesResultTypeDef",
    "ListQueueTagsResultTypeDef",
    "ListQueuesResultTypeDef",
    "SendMessageResultTypeDef",
    "StartMessageMoveTaskResultTypeDef",
    "ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef",
    "ChangeMessageVisibilityBatchRequestRequestTypeDef",
    "ChangeMessageVisibilityBatchResultTypeDef",
    "DeleteMessageBatchRequestQueueDeleteMessagesTypeDef",
    "DeleteMessageBatchRequestRequestTypeDef",
    "DeleteMessageBatchResultTypeDef",
    "ListDeadLetterSourceQueuesRequestListDeadLetterSourceQueuesPaginateTypeDef",
    "ListQueuesRequestListQueuesPaginateTypeDef",
    "ListMessageMoveTasksResultTypeDef",
    "MessageTypeDef",
    "SendMessageBatchResultTypeDef",
    "SendMessageBatchRequestEntryQueueTypeDef",
    "SendMessageBatchRequestEntryTypeDef",
    "SendMessageRequestQueueSendMessageTypeDef",
    "SendMessageRequestRequestTypeDef",
    "ReceiveMessageResultTypeDef",
    "SendMessageBatchRequestQueueSendMessagesTypeDef",
    "SendMessageBatchRequestRequestTypeDef",
)

AddPermissionRequestQueueAddPermissionTypeDef = TypedDict(
    "AddPermissionRequestQueueAddPermissionTypeDef",
    {
        "Label": str,
        "AWSAccountIds": Sequence[str],
        "Actions": Sequence[str],
    },
)
AddPermissionRequestRequestTypeDef = TypedDict(
    "AddPermissionRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Label": str,
        "AWSAccountIds": Sequence[str],
        "Actions": Sequence[str],
    },
)
BatchResultErrorEntryTypeDef = TypedDict(
    "BatchResultErrorEntryTypeDef",
    {
        "Id": str,
        "SenderFault": bool,
        "Code": str,
        "Message": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CancelMessageMoveTaskRequestRequestTypeDef = TypedDict(
    "CancelMessageMoveTaskRequestRequestTypeDef",
    {
        "TaskHandle": str,
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
ChangeMessageVisibilityBatchRequestEntryTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchRequestEntryTypeDef",
    {
        "Id": str,
        "ReceiptHandle": str,
        "VisibilityTimeout": NotRequired[int],
    },
)
ChangeMessageVisibilityBatchResultEntryTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchResultEntryTypeDef",
    {
        "Id": str,
    },
)
ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef = TypedDict(
    "ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef",
    {
        "VisibilityTimeout": int,
    },
)
ChangeMessageVisibilityRequestRequestTypeDef = TypedDict(
    "ChangeMessageVisibilityRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "ReceiptHandle": str,
        "VisibilityTimeout": int,
    },
)
CreateQueueRequestRequestTypeDef = TypedDict(
    "CreateQueueRequestRequestTypeDef",
    {
        "QueueName": str,
        "Attributes": NotRequired[Mapping[QueueAttributeNameType, str]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateQueueRequestServiceResourceCreateQueueTypeDef = TypedDict(
    "CreateQueueRequestServiceResourceCreateQueueTypeDef",
    {
        "QueueName": str,
        "Attributes": NotRequired[Mapping[QueueAttributeNameType, str]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
DeleteMessageBatchRequestEntryTypeDef = TypedDict(
    "DeleteMessageBatchRequestEntryTypeDef",
    {
        "Id": str,
        "ReceiptHandle": str,
    },
)
DeleteMessageBatchResultEntryTypeDef = TypedDict(
    "DeleteMessageBatchResultEntryTypeDef",
    {
        "Id": str,
    },
)
DeleteMessageRequestRequestTypeDef = TypedDict(
    "DeleteMessageRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "ReceiptHandle": str,
    },
)
DeleteQueueRequestRequestTypeDef = TypedDict(
    "DeleteQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)
GetQueueAttributesRequestRequestTypeDef = TypedDict(
    "GetQueueAttributesRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "AttributeNames": NotRequired[Sequence[QueueAttributeFilterType]],
    },
)
GetQueueUrlRequestRequestTypeDef = TypedDict(
    "GetQueueUrlRequestRequestTypeDef",
    {
        "QueueName": str,
        "QueueOwnerAWSAccountId": NotRequired[str],
    },
)
GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef = TypedDict(
    "GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef",
    {
        "QueueName": str,
        "QueueOwnerAWSAccountId": NotRequired[str],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListDeadLetterSourceQueuesRequestRequestTypeDef = TypedDict(
    "ListDeadLetterSourceQueuesRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListMessageMoveTasksRequestRequestTypeDef = TypedDict(
    "ListMessageMoveTasksRequestRequestTypeDef",
    {
        "SourceArn": str,
        "MaxResults": NotRequired[int],
    },
)
ListMessageMoveTasksResultEntryTypeDef = TypedDict(
    "ListMessageMoveTasksResultEntryTypeDef",
    {
        "TaskHandle": NotRequired[str],
        "Status": NotRequired[str],
        "SourceArn": NotRequired[str],
        "DestinationArn": NotRequired[str],
        "MaxNumberOfMessagesPerSecond": NotRequired[int],
        "ApproximateNumberOfMessagesMoved": NotRequired[int],
        "ApproximateNumberOfMessagesToMove": NotRequired[int],
        "FailureReason": NotRequired[str],
        "StartedTimestamp": NotRequired[int],
    },
)
ListQueueTagsRequestRequestTypeDef = TypedDict(
    "ListQueueTagsRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)
ListQueuesRequestRequestTypeDef = TypedDict(
    "ListQueuesRequestRequestTypeDef",
    {
        "QueueNamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MessageAttributeValueTypeDef = TypedDict(
    "MessageAttributeValueTypeDef",
    {
        "DataType": str,
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[bytes],
        "StringListValues": NotRequired[List[str]],
        "BinaryListValues": NotRequired[List[bytes]],
    },
)
PurgeQueueRequestRequestTypeDef = TypedDict(
    "PurgeQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)
ReceiveMessageRequestQueueReceiveMessagesTypeDef = TypedDict(
    "ReceiveMessageRequestQueueReceiveMessagesTypeDef",
    {
        "AttributeNames": NotRequired[Sequence[QueueAttributeFilterType]],
        "MessageAttributeNames": NotRequired[Sequence[str]],
        "MaxNumberOfMessages": NotRequired[int],
        "VisibilityTimeout": NotRequired[int],
        "WaitTimeSeconds": NotRequired[int],
        "ReceiveRequestAttemptId": NotRequired[str],
    },
)
ReceiveMessageRequestRequestTypeDef = TypedDict(
    "ReceiveMessageRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "AttributeNames": NotRequired[Sequence[QueueAttributeFilterType]],
        "MessageAttributeNames": NotRequired[Sequence[str]],
        "MaxNumberOfMessages": NotRequired[int],
        "VisibilityTimeout": NotRequired[int],
        "WaitTimeSeconds": NotRequired[int],
        "ReceiveRequestAttemptId": NotRequired[str],
    },
)
RemovePermissionRequestQueueRemovePermissionTypeDef = TypedDict(
    "RemovePermissionRequestQueueRemovePermissionTypeDef",
    {
        "Label": str,
    },
)
RemovePermissionRequestRequestTypeDef = TypedDict(
    "RemovePermissionRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Label": str,
    },
)
SendMessageBatchResultEntryTypeDef = TypedDict(
    "SendMessageBatchResultEntryTypeDef",
    {
        "Id": str,
        "MessageId": str,
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": NotRequired[str],
        "MD5OfMessageSystemAttributes": NotRequired[str],
        "SequenceNumber": NotRequired[str],
    },
)
SetQueueAttributesRequestQueueSetAttributesTypeDef = TypedDict(
    "SetQueueAttributesRequestQueueSetAttributesTypeDef",
    {
        "Attributes": Mapping[QueueAttributeNameType, str],
    },
)
SetQueueAttributesRequestRequestTypeDef = TypedDict(
    "SetQueueAttributesRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Attributes": Mapping[QueueAttributeNameType, str],
    },
)
StartMessageMoveTaskRequestRequestTypeDef = TypedDict(
    "StartMessageMoveTaskRequestRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": NotRequired[str],
        "MaxNumberOfMessagesPerSecond": NotRequired[int],
    },
)
TagQueueRequestRequestTypeDef = TypedDict(
    "TagQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Tags": Mapping[str, str],
    },
)
UntagQueueRequestRequestTypeDef = TypedDict(
    "UntagQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "TagKeys": Sequence[str],
    },
)
MessageAttributeValueQueueTypeDef = TypedDict(
    "MessageAttributeValueQueueTypeDef",
    {
        "DataType": str,
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[BlobTypeDef],
        "StringListValues": NotRequired[Sequence[str]],
        "BinaryListValues": NotRequired[Sequence[BlobTypeDef]],
    },
)
MessageSystemAttributeValueTypeDef = TypedDict(
    "MessageSystemAttributeValueTypeDef",
    {
        "DataType": str,
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[BlobTypeDef],
        "StringListValues": NotRequired[Sequence[str]],
        "BinaryListValues": NotRequired[Sequence[BlobTypeDef]],
    },
)
CancelMessageMoveTaskResultTypeDef = TypedDict(
    "CancelMessageMoveTaskResultTypeDef",
    {
        "ApproximateNumberOfMessagesMoved": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateQueueResultTypeDef = TypedDict(
    "CreateQueueResultTypeDef",
    {
        "QueueUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueueAttributesResultTypeDef = TypedDict(
    "GetQueueAttributesResultTypeDef",
    {
        "Attributes": Dict[QueueAttributeNameType, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueueUrlResultTypeDef = TypedDict(
    "GetQueueUrlResultTypeDef",
    {
        "QueueUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeadLetterSourceQueuesResultTypeDef = TypedDict(
    "ListDeadLetterSourceQueuesResultTypeDef",
    {
        "queueUrls": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListQueueTagsResultTypeDef = TypedDict(
    "ListQueueTagsResultTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListQueuesResultTypeDef = TypedDict(
    "ListQueuesResultTypeDef",
    {
        "QueueUrls": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendMessageResultTypeDef = TypedDict(
    "SendMessageResultTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMessageMoveTaskResultTypeDef = TypedDict(
    "StartMessageMoveTaskResultTypeDef",
    {
        "TaskHandle": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef",
    {
        "Entries": Sequence[ChangeMessageVisibilityBatchRequestEntryTypeDef],
    },
)
ChangeMessageVisibilityBatchRequestRequestTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": Sequence[ChangeMessageVisibilityBatchRequestEntryTypeDef],
    },
)
ChangeMessageVisibilityBatchResultTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchResultTypeDef",
    {
        "Successful": List[ChangeMessageVisibilityBatchResultEntryTypeDef],
        "Failed": List[BatchResultErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMessageBatchRequestQueueDeleteMessagesTypeDef = TypedDict(
    "DeleteMessageBatchRequestQueueDeleteMessagesTypeDef",
    {
        "Entries": Sequence[DeleteMessageBatchRequestEntryTypeDef],
    },
)
DeleteMessageBatchRequestRequestTypeDef = TypedDict(
    "DeleteMessageBatchRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": Sequence[DeleteMessageBatchRequestEntryTypeDef],
    },
)
DeleteMessageBatchResultTypeDef = TypedDict(
    "DeleteMessageBatchResultTypeDef",
    {
        "Successful": List[DeleteMessageBatchResultEntryTypeDef],
        "Failed": List[BatchResultErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeadLetterSourceQueuesRequestListDeadLetterSourceQueuesPaginateTypeDef = TypedDict(
    "ListDeadLetterSourceQueuesRequestListDeadLetterSourceQueuesPaginateTypeDef",
    {
        "QueueUrl": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQueuesRequestListQueuesPaginateTypeDef = TypedDict(
    "ListQueuesRequestListQueuesPaginateTypeDef",
    {
        "QueueNamePrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMessageMoveTasksResultTypeDef = TypedDict(
    "ListMessageMoveTasksResultTypeDef",
    {
        "Results": List[ListMessageMoveTasksResultEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "MessageId": NotRequired[str],
        "ReceiptHandle": NotRequired[str],
        "MD5OfBody": NotRequired[str],
        "Body": NotRequired[str],
        "Attributes": NotRequired[Dict[MessageSystemAttributeNameType, str]],
        "MD5OfMessageAttributes": NotRequired[str],
        "MessageAttributes": NotRequired[Dict[str, MessageAttributeValueTypeDef]],
    },
)
SendMessageBatchResultTypeDef = TypedDict(
    "SendMessageBatchResultTypeDef",
    {
        "Successful": List[SendMessageBatchResultEntryTypeDef],
        "Failed": List[BatchResultErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendMessageBatchRequestEntryQueueTypeDef = TypedDict(
    "SendMessageBatchRequestEntryQueueTypeDef",
    {
        "Id": str,
        "MessageBody": str,
        "DelaySeconds": NotRequired[int],
        "MessageAttributes": NotRequired[Mapping[str, MessageAttributeValueQueueTypeDef]],
        "MessageSystemAttributes": NotRequired[
            Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef]
        ],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)
SendMessageBatchRequestEntryTypeDef = TypedDict(
    "SendMessageBatchRequestEntryTypeDef",
    {
        "Id": str,
        "MessageBody": str,
        "DelaySeconds": NotRequired[int],
        "MessageAttributes": NotRequired[Mapping[str, MessageAttributeValueTypeDef]],
        "MessageSystemAttributes": NotRequired[
            Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef]
        ],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)
SendMessageRequestQueueSendMessageTypeDef = TypedDict(
    "SendMessageRequestQueueSendMessageTypeDef",
    {
        "MessageBody": str,
        "DelaySeconds": NotRequired[int],
        "MessageAttributes": NotRequired[Mapping[str, MessageAttributeValueQueueTypeDef]],
        "MessageSystemAttributes": NotRequired[
            Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef]
        ],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)
SendMessageRequestRequestTypeDef = TypedDict(
    "SendMessageRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "MessageBody": str,
        "DelaySeconds": NotRequired[int],
        "MessageAttributes": NotRequired[Mapping[str, MessageAttributeValueTypeDef]],
        "MessageSystemAttributes": NotRequired[
            Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef]
        ],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)
ReceiveMessageResultTypeDef = TypedDict(
    "ReceiveMessageResultTypeDef",
    {
        "Messages": List[MessageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendMessageBatchRequestQueueSendMessagesTypeDef = TypedDict(
    "SendMessageBatchRequestQueueSendMessagesTypeDef",
    {
        "Entries": Sequence[SendMessageBatchRequestEntryQueueTypeDef],
    },
)
SendMessageBatchRequestRequestTypeDef = TypedDict(
    "SendMessageBatchRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": Sequence[SendMessageBatchRequestEntryTypeDef],
    },
)
