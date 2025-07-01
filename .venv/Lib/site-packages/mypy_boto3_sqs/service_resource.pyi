"""
Type annotations for sqs service ServiceResource

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_sqs.service_resource import SQSServiceResource
    import mypy_boto3_sqs.service_resource as sqs_resources

    session = Session()
    resource: SQSServiceResource = session.resource("sqs")

    my_message: sqs_resources.Message = resource.Message(...)
    my_queue: sqs_resources.Queue = resource.Queue(...)
```
"""

import sys
from typing import Dict, Iterator, List, Mapping, Sequence

from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import SQSClient
from .literals import (
    MessageSystemAttributeNameType,
    QueueAttributeFilterType,
    QueueAttributeNameType,
)
from .type_defs import (
    ChangeMessageVisibilityBatchRequestEntryTypeDef,
    ChangeMessageVisibilityBatchResultTypeDef,
    DeleteMessageBatchRequestEntryTypeDef,
    DeleteMessageBatchResultTypeDef,
    MessageAttributeValueQueueTypeDef,
    MessageAttributeValueTypeDef,
    MessageSystemAttributeValueTypeDef,
    SendMessageBatchRequestEntryQueueTypeDef,
    SendMessageBatchResultTypeDef,
    SendMessageResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "SQSServiceResource",
    "Message",
    "Queue",
    "ServiceResourceQueuesCollection",
    "QueueDeadLetterSourceQueuesCollection",
)

class ServiceResourceQueuesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.queues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#serviceresourcequeuescollection)
    """

    def all(self) -> "ServiceResourceQueuesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#serviceresourcequeuescollection)
        """

    def filter(  # type: ignore
        self, *, QueueNamePrefix: str = ..., NextToken: str = ..., MaxResults: int = ...
    ) -> "ServiceResourceQueuesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#serviceresourcequeuescollection)
        """

    def limit(self, count: int) -> "ServiceResourceQueuesCollection":
        """
        Return at most this many Queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#serviceresourcequeuescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceQueuesCollection":
        """
        Fetch at most this many Queues per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#serviceresourcequeuescollection)
        """

    def pages(self) -> Iterator[List["Queue"]]:
        """
        A generator which yields pages of Queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#serviceresourcequeuescollection)
        """

    def __iter__(self) -> Iterator["Queue"]:
        """
        A generator which yields Queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#serviceresourcequeuescollection)
        """

class QueueDeadLetterSourceQueuesCollection(ResourceCollection):
    def all(self) -> "QueueDeadLetterSourceQueuesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> "QueueDeadLetterSourceQueuesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "QueueDeadLetterSourceQueuesCollection":
        """
        Return at most this many Queues.
        """

    def page_size(self, count: int) -> "QueueDeadLetterSourceQueuesCollection":
        """
        Fetch at most this many Queues per service request.
        """

    def pages(self) -> Iterator[List["Queue"]]:
        """
        A generator which yields pages of Queues.
        """

    def __iter__(self) -> Iterator["Queue"]:
        """
        A generator which yields Queues.
        """

class Message(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.Message)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#message)
    """

    message_id: str
    md5_of_body: str
    body: str
    attributes: Dict[MessageSystemAttributeNameType, str]
    md5_of_message_attributes: str
    message_attributes: Dict[str, MessageAttributeValueTypeDef]
    queue_url: str
    receipt_handle: str

    def Queue(self) -> "_Queue":
        """
        Creates a Queue resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Message.Queue)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#messagequeue-method)
        """

    def change_visibility(self, *, VisibilityTimeout: int) -> None:
        """
        Changes the visibility timeout of a specified message in a queue to a new value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Message.change_visibility)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#messagechange_visibility-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified message from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Message.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#messagedelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Message.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#messageget_available_subresources-method)
        """

_Message = Message

class Queue(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.Queue)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queue)
    """

    attributes: Dict[QueueAttributeNameType, str]
    url: str
    dead_letter_source_queues: QueueDeadLetterSourceQueuesCollection

    def Message(self, receipt_handle: str) -> _Message:
        """
        Creates a Message resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.Message)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queuemessage-method)
        """

    def add_permission(
        self, *, Label: str, AWSAccountIds: Sequence[str], Actions: Sequence[str]
    ) -> None:
        """
        Adds a permission to a queue for a specific
        [principal](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.add_permission)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queueadd_permission-method)
        """

    def change_message_visibility_batch(
        self, *, Entries: Sequence[ChangeMessageVisibilityBatchRequestEntryTypeDef]
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        Changes the visibility timeout of multiple messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.change_message_visibility_batch)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queuechange_message_visibility_batch-method)
        """

    def delete(self) -> None:
        """
        Deletes the queue specified by the `QueueUrl`, regardless of the queue's
        contents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queuedelete-method)
        """

    def delete_messages(
        self, *, Entries: Sequence[DeleteMessageBatchRequestEntryTypeDef]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        Deletes up to ten messages from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.delete_messages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queuedelete_messages-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queueget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`SQS.Client.get_queue_attributes` to update the attributes of
        the Queue
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queueload-method)
        """

    def purge(self) -> None:
        """
        Deletes available messages in a queue (including in-flight messages) specified
        by the `QueueURL`
        parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.purge)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queuepurge-method)
        """

    def receive_messages(
        self,
        *,
        AttributeNames: Sequence[QueueAttributeFilterType] = ...,
        MessageAttributeNames: Sequence[str] = ...,
        MaxNumberOfMessages: int = ...,
        VisibilityTimeout: int = ...,
        WaitTimeSeconds: int = ...,
        ReceiveRequestAttemptId: str = ...
    ) -> List[_Message]:
        """
        Retrieves one or more messages (up to 10), from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.receive_messages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queuereceive_messages-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`SQS.Client.get_queue_attributes` to update the attributes of
        the Queue
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queuereload-method)
        """

    def remove_permission(self, *, Label: str) -> None:
        """
        Revokes any permissions in the queue policy that matches the specified `Label`
        parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.remove_permission)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queueremove_permission-method)
        """

    def send_message(
        self,
        *,
        MessageBody: str,
        DelaySeconds: int = ...,
        MessageAttributes: Mapping[str, MessageAttributeValueQueueTypeDef] = ...,
        MessageSystemAttributes: Mapping[
            Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef
        ] = ...,
        MessageDeduplicationId: str = ...,
        MessageGroupId: str = ...
    ) -> SendMessageResultTypeDef:
        """
        Delivers a message to the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.send_message)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queuesend_message-method)
        """

    def send_messages(
        self, *, Entries: Sequence[SendMessageBatchRequestEntryQueueTypeDef]
    ) -> SendMessageBatchResultTypeDef:
        """
        You can use `SendMessageBatch` to send up to 10 messages to the specified queue
        by assigning either identical or different values to each message (or by not
        assigning values at
        all).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.send_messages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queuesend_messages-method)
        """

    def set_attributes(self, *, Attributes: Mapping[QueueAttributeNameType, str]) -> None:
        """
        Sets the value of one or more queue attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.set_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#queueset_attributes-method)
        """

_Queue = Queue

class SQSResourceMeta(ResourceMeta):
    client: SQSClient

class SQSServiceResource(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/)
    """

    meta: "SQSResourceMeta"
    queues: ServiceResourceQueuesCollection

    def Message(self, queue_url: str, receipt_handle: str) -> _Message:
        """
        Creates a Message resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.Message)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#sqsserviceresourcemessage-method)
        """

    def Queue(self, url: str) -> _Queue:
        """
        Creates a Queue resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.Queue)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#sqsserviceresourcequeue-method)
        """

    def create_queue(
        self,
        *,
        QueueName: str,
        Attributes: Mapping[QueueAttributeNameType, str] = ...,
        tags: Mapping[str, str] = ...
    ) -> _Queue:
        """
        Creates a new standard or FIFO queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.create_queue)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#sqsserviceresourcecreate_queue-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#sqsserviceresourceget_available_subresources-method)
        """

    def get_queue_by_name(self, *, QueueName: str, QueueOwnerAWSAccountId: str = ...) -> _Queue:
        """
        Returns the URL of an existing Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.ServiceResource.get_queue_by_name)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource/#sqsserviceresourceget_queue_by_name-method)
        """
