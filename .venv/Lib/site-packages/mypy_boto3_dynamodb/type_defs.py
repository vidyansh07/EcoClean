"""
Type annotations for dynamodb service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/type_defs/)

Usage::

    ```python
    from mypy_boto3_dynamodb.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Mapping, Sequence, Set, Union

from boto3.dynamodb.conditions import ConditionBase

from .literals import (
    AttributeActionType,
    BackupStatusType,
    BackupTypeFilterType,
    BackupTypeType,
    BatchStatementErrorCodeEnumType,
    BillingModeType,
    ComparisonOperatorType,
    ConditionalOperatorType,
    ContinuousBackupsStatusType,
    ContributorInsightsActionType,
    ContributorInsightsStatusType,
    DestinationStatusType,
    ExportFormatType,
    ExportStatusType,
    ExportTypeType,
    ExportViewTypeType,
    GlobalTableStatusType,
    ImportStatusType,
    IndexStatusType,
    InputCompressionTypeType,
    InputFormatType,
    KeyTypeType,
    PointInTimeRecoveryStatusType,
    ProjectionTypeType,
    ReplicaStatusType,
    ReturnConsumedCapacityType,
    ReturnItemCollectionMetricsType,
    ReturnValuesOnConditionCheckFailureType,
    ReturnValueType,
    S3SseAlgorithmType,
    ScalarAttributeTypeType,
    SelectType,
    SSEStatusType,
    SSETypeType,
    StreamViewTypeType,
    TableClassType,
    TableStatusType,
    TimeToLiveStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ResponseMetadataTypeDef",
    "ArchivalSummaryTypeDef",
    "AttributeDefinitionTypeDef",
    "AttributeValueTypeDef",
    "TableAttributeValueTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    "BackupDetailsTypeDef",
    "BackupSummaryTypeDef",
    "BillingModeSummaryTypeDef",
    "CapacityTypeDef",
    "ConditionBaseImportTypeDef",
    "PointInTimeRecoveryDescriptionTypeDef",
    "ContributorInsightsSummaryTypeDef",
    "CreateBackupInputRequestTypeDef",
    "KeySchemaElementTypeDef",
    "ProjectionTableTypeDef",
    "ProvisionedThroughputTypeDef",
    "ProjectionTypeDef",
    "ReplicaTypeDef",
    "CreateReplicaActionTypeDef",
    "ProvisionedThroughputOverrideTypeDef",
    "SSESpecificationTypeDef",
    "StreamSpecificationTypeDef",
    "TagTypeDef",
    "CsvOptionsTypeDef",
    "DeleteBackupInputRequestTypeDef",
    "DeleteGlobalSecondaryIndexActionTypeDef",
    "DeleteReplicaActionTypeDef",
    "DeleteReplicationGroupMemberActionTypeDef",
    "DeleteTableInputRequestTypeDef",
    "DescribeBackupInputRequestTypeDef",
    "DescribeContinuousBackupsInputRequestTypeDef",
    "DescribeContributorInsightsInputRequestTypeDef",
    "FailureExceptionTypeDef",
    "EndpointTypeDef",
    "DescribeExportInputRequestTypeDef",
    "DescribeGlobalTableInputRequestTypeDef",
    "DescribeGlobalTableSettingsInputRequestTypeDef",
    "DescribeImportInputRequestTypeDef",
    "DescribeKinesisStreamingDestinationInputRequestTypeDef",
    "KinesisDataStreamDestinationTypeDef",
    "DescribeTableInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeTableReplicaAutoScalingInputRequestTypeDef",
    "DescribeTimeToLiveInputRequestTypeDef",
    "TimeToLiveDescriptionTypeDef",
    "IncrementalExportSpecificationTypeDef",
    "ExportSummaryTypeDef",
    "TimestampTypeDef",
    "ProvisionedThroughputDescriptionTypeDef",
    "S3BucketSourceTypeDef",
    "KinesisStreamingDestinationInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListContributorInsightsInputRequestTypeDef",
    "ListExportsInputRequestTypeDef",
    "ListGlobalTablesInputRequestTypeDef",
    "ListImportsInputRequestTypeDef",
    "ListTablesInputRequestTypeDef",
    "ListTagsOfResourceInputRequestTypeDef",
    "PointInTimeRecoverySpecificationTypeDef",
    "TableClassSummaryTypeDef",
    "RestoreSummaryTypeDef",
    "SSEDescriptionTypeDef",
    "TableBatchWriterRequestTypeDef",
    "TimeToLiveSpecificationTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateContributorInsightsInputRequestTypeDef",
    "ArchivalSummaryResponseTypeDef",
    "BillingModeSummaryResponseTypeDef",
    "DescribeLimitsOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "KinesisStreamingDestinationOutputTypeDef",
    "ListTablesOutputTypeDef",
    "ProvisionedThroughputDescriptionResponseTypeDef",
    "RestoreSummaryResponseTypeDef",
    "SSEDescriptionResponseTypeDef",
    "StreamSpecificationResponseTypeDef",
    "TableClassSummaryResponseTypeDef",
    "UpdateContributorInsightsOutputTypeDef",
    "BatchStatementErrorTypeDef",
    "ItemCollectionMetricsTypeDef",
    "ItemResponseTypeDef",
    "UniversalAttributeValueTypeDef",
    "AttributeValueUpdateTableTypeDef",
    "ConditionTableTypeDef",
    "DeleteRequestServiceResourceTypeDef",
    "ExpectedAttributeValueTableTypeDef",
    "GetItemInputTableGetItemTypeDef",
    "ItemCollectionMetricsServiceResourceTypeDef",
    "ItemCollectionMetricsTableTypeDef",
    "KeysAndAttributesServiceResourceTypeDef",
    "PutRequestServiceResourceTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyUpdateTypeDef",
    "CreateBackupOutputTypeDef",
    "ListBackupsOutputTypeDef",
    "ConsumedCapacityTypeDef",
    "ContinuousBackupsDescriptionTypeDef",
    "ListContributorInsightsOutputTypeDef",
    "LocalSecondaryIndexDescriptionTableTypeDef",
    "CreateGlobalSecondaryIndexActionTableTypeDef",
    "SourceTableDetailsTypeDef",
    "UpdateGlobalSecondaryIndexActionTypeDef",
    "CreateGlobalSecondaryIndexActionTypeDef",
    "GlobalSecondaryIndexInfoTypeDef",
    "GlobalSecondaryIndexTypeDef",
    "LocalSecondaryIndexDescriptionTypeDef",
    "LocalSecondaryIndexInfoTypeDef",
    "LocalSecondaryIndexTypeDef",
    "CreateGlobalTableInputRequestTypeDef",
    "GlobalTableTypeDef",
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexTypeDef",
    "ListTagsOfResourceOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "InputFormatOptionsTypeDef",
    "ReplicaUpdateTypeDef",
    "DescribeContributorInsightsOutputTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    "DescribeTableInputTableExistsWaitTypeDef",
    "DescribeTableInputTableNotExistsWaitTypeDef",
    "DescribeTimeToLiveOutputTypeDef",
    "ExportDescriptionTypeDef",
    "ListExportsOutputTypeDef",
    "ExportTableToPointInTimeInputRequestTypeDef",
    "ListBackupsInputRequestTypeDef",
    "GlobalSecondaryIndexDescriptionTableTypeDef",
    "GlobalSecondaryIndexDescriptionTypeDef",
    "ImportSummaryTypeDef",
    "ListBackupsInputListBackupsPaginateTypeDef",
    "ListTablesInputListTablesPaginateTypeDef",
    "ListTagsOfResourceInputListTagsOfResourcePaginateTypeDef",
    "UpdateContinuousBackupsInputRequestTypeDef",
    "UpdateTimeToLiveInputRequestTypeDef",
    "UpdateTimeToLiveOutputTypeDef",
    "BatchStatementResponseTypeDef",
    "AttributeValueUpdateTypeDef",
    "BatchStatementRequestTypeDef",
    "ConditionCheckTypeDef",
    "ConditionTypeDef",
    "DeleteRequestTypeDef",
    "DeleteTypeDef",
    "ExecuteStatementInputRequestTypeDef",
    "ExpectedAttributeValueTypeDef",
    "GetItemInputRequestTypeDef",
    "GetTypeDef",
    "KeysAndAttributesTypeDef",
    "ParameterizedStatementTypeDef",
    "PutRequestTypeDef",
    "PutTypeDef",
    "UpdateTypeDef",
    "QueryInputTableQueryTypeDef",
    "ScanInputTableScanTypeDef",
    "DeleteItemInputTableDeleteItemTypeDef",
    "PutItemInputTablePutItemTypeDef",
    "UpdateItemInputTableUpdateItemTypeDef",
    "BatchGetItemInputServiceResourceBatchGetItemTypeDef",
    "WriteRequestServiceResourceTypeDef",
    "AutoScalingSettingsDescriptionTypeDef",
    "AutoScalingSettingsUpdateTypeDef",
    "BatchGetItemOutputServiceResourceTypeDef",
    "DeleteItemOutputTableTypeDef",
    "DeleteItemOutputTypeDef",
    "ExecuteStatementOutputTypeDef",
    "ExecuteTransactionOutputTypeDef",
    "GetItemOutputTableTypeDef",
    "GetItemOutputTypeDef",
    "PutItemOutputTableTypeDef",
    "PutItemOutputTypeDef",
    "QueryOutputTableTypeDef",
    "QueryOutputTypeDef",
    "ScanOutputTableTypeDef",
    "ScanOutputTypeDef",
    "TransactGetItemsOutputTypeDef",
    "TransactWriteItemsOutputTypeDef",
    "UpdateItemOutputTableTypeDef",
    "UpdateItemOutputTypeDef",
    "DescribeContinuousBackupsOutputTypeDef",
    "UpdateContinuousBackupsOutputTypeDef",
    "GlobalSecondaryIndexUpdateTableTypeDef",
    "GlobalSecondaryIndexUpdateTypeDef",
    "TableCreationParametersTypeDef",
    "SourceTableFeatureDetailsTypeDef",
    "CreateTableInputRequestTypeDef",
    "CreateTableInputServiceResourceCreateTableTypeDef",
    "RestoreTableFromBackupInputRequestTypeDef",
    "RestoreTableToPointInTimeInputRequestTypeDef",
    "ListGlobalTablesOutputTypeDef",
    "ReplicaDescriptionTypeDef",
    "CreateReplicationGroupMemberActionTypeDef",
    "UpdateReplicationGroupMemberActionTypeDef",
    "UpdateGlobalTableInputRequestTypeDef",
    "DescribeExportOutputTypeDef",
    "ExportTableToPointInTimeOutputTypeDef",
    "ListImportsOutputTypeDef",
    "BatchExecuteStatementOutputTypeDef",
    "BatchExecuteStatementInputRequestTypeDef",
    "QueryInputQueryPaginateTypeDef",
    "QueryInputRequestTypeDef",
    "ScanInputRequestTypeDef",
    "ScanInputScanPaginateTypeDef",
    "DeleteItemInputRequestTypeDef",
    "PutItemInputRequestTypeDef",
    "UpdateItemInputRequestTypeDef",
    "TransactGetItemTypeDef",
    "BatchGetItemInputRequestTypeDef",
    "BatchGetItemOutputTypeDef",
    "ExecuteTransactionInputRequestTypeDef",
    "WriteRequestTypeDef",
    "TransactWriteItemTypeDef",
    "BatchWriteItemInputServiceResourceBatchWriteItemTypeDef",
    "BatchWriteItemOutputServiceResourceTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    "ImportTableDescriptionTypeDef",
    "ImportTableInputRequestTypeDef",
    "BackupDescriptionTypeDef",
    "GlobalTableDescriptionTypeDef",
    "TableDescriptionTableTypeDef",
    "TableDescriptionTypeDef",
    "ReplicationGroupUpdateTypeDef",
    "TransactGetItemsInputRequestTypeDef",
    "BatchWriteItemInputRequestTypeDef",
    "BatchWriteItemOutputTypeDef",
    "TransactWriteItemsInputRequestTypeDef",
    "ReplicaAutoScalingDescriptionTypeDef",
    "ReplicaSettingsDescriptionTypeDef",
    "ReplicaAutoScalingUpdateTypeDef",
    "ReplicaSettingsUpdateTypeDef",
    "DescribeImportOutputTypeDef",
    "ImportTableOutputTypeDef",
    "DeleteBackupOutputTypeDef",
    "DescribeBackupOutputTypeDef",
    "CreateGlobalTableOutputTypeDef",
    "DescribeGlobalTableOutputTypeDef",
    "UpdateGlobalTableOutputTypeDef",
    "DeleteTableOutputTableTypeDef",
    "CreateTableOutputTypeDef",
    "DeleteTableOutputTypeDef",
    "DescribeTableOutputTypeDef",
    "RestoreTableFromBackupOutputTypeDef",
    "RestoreTableToPointInTimeOutputTypeDef",
    "UpdateTableOutputTypeDef",
    "UpdateTableInputRequestTypeDef",
    "UpdateTableInputTableUpdateTypeDef",
    "TableAutoScalingDescriptionTypeDef",
    "DescribeGlobalTableSettingsOutputTypeDef",
    "UpdateGlobalTableSettingsOutputTypeDef",
    "UpdateTableReplicaAutoScalingInputRequestTypeDef",
    "UpdateGlobalTableSettingsInputRequestTypeDef",
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    "UpdateTableReplicaAutoScalingOutputTypeDef",
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
ArchivalSummaryTypeDef = TypedDict(
    "ArchivalSummaryTypeDef",
    {
        "ArchivalDateTime": NotRequired[datetime],
        "ArchivalReason": NotRequired[str],
        "ArchivalBackupArn": NotRequired[str],
    },
)
AttributeDefinitionTypeDef = TypedDict(
    "AttributeDefinitionTypeDef",
    {
        "AttributeName": str,
        "AttributeType": ScalarAttributeTypeType,
    },
)
AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": NotRequired[str],
        "N": NotRequired[str],
        "B": NotRequired[bytes],
        "SS": NotRequired[Sequence[str]],
        "NS": NotRequired[Sequence[str]],
        "BS": NotRequired[Sequence[bytes]],
        "M": NotRequired[Mapping[str, Any]],
        "L": NotRequired[Sequence[Any]],
        "NULL": NotRequired[bool],
        "BOOL": NotRequired[bool],
    },
)
TableAttributeValueTypeDef = Union[
    bytes,
    bytearray,
    str,
    int,
    Decimal,
    bool,
    Set[int],
    Set[Decimal],
    Set[str],
    Set[bytes],
    Set[bytearray],
    Sequence[Any],
    Mapping[str, Any],
    None,
]
AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {
        "TargetValue": float,
        "DisableScaleIn": NotRequired[bool],
        "ScaleInCooldown": NotRequired[int],
        "ScaleOutCooldown": NotRequired[int],
    },
)
AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {
        "TargetValue": float,
        "DisableScaleIn": NotRequired[bool],
        "ScaleInCooldown": NotRequired[int],
        "ScaleOutCooldown": NotRequired[int],
    },
)
BackupDetailsTypeDef = TypedDict(
    "BackupDetailsTypeDef",
    {
        "BackupArn": str,
        "BackupName": str,
        "BackupStatus": BackupStatusType,
        "BackupType": BackupTypeType,
        "BackupCreationDateTime": datetime,
        "BackupSizeBytes": NotRequired[int],
        "BackupExpiryDateTime": NotRequired[datetime],
    },
)
BackupSummaryTypeDef = TypedDict(
    "BackupSummaryTypeDef",
    {
        "TableName": NotRequired[str],
        "TableId": NotRequired[str],
        "TableArn": NotRequired[str],
        "BackupArn": NotRequired[str],
        "BackupName": NotRequired[str],
        "BackupCreationDateTime": NotRequired[datetime],
        "BackupExpiryDateTime": NotRequired[datetime],
        "BackupStatus": NotRequired[BackupStatusType],
        "BackupType": NotRequired[BackupTypeType],
        "BackupSizeBytes": NotRequired[int],
    },
)
BillingModeSummaryTypeDef = TypedDict(
    "BillingModeSummaryTypeDef",
    {
        "BillingMode": NotRequired[BillingModeType],
        "LastUpdateToPayPerRequestDateTime": NotRequired[datetime],
    },
)
CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "ReadCapacityUnits": NotRequired[float],
        "WriteCapacityUnits": NotRequired[float],
        "CapacityUnits": NotRequired[float],
    },
)
ConditionBaseImportTypeDef = Union[str, ConditionBase]
PointInTimeRecoveryDescriptionTypeDef = TypedDict(
    "PointInTimeRecoveryDescriptionTypeDef",
    {
        "PointInTimeRecoveryStatus": NotRequired[PointInTimeRecoveryStatusType],
        "EarliestRestorableDateTime": NotRequired[datetime],
        "LatestRestorableDateTime": NotRequired[datetime],
    },
)
ContributorInsightsSummaryTypeDef = TypedDict(
    "ContributorInsightsSummaryTypeDef",
    {
        "TableName": NotRequired[str],
        "IndexName": NotRequired[str],
        "ContributorInsightsStatus": NotRequired[ContributorInsightsStatusType],
    },
)
CreateBackupInputRequestTypeDef = TypedDict(
    "CreateBackupInputRequestTypeDef",
    {
        "TableName": str,
        "BackupName": str,
    },
)
KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)
ProjectionTableTypeDef = TypedDict(
    "ProjectionTableTypeDef",
    {
        "ProjectionType": NotRequired[ProjectionTypeType],
        "NonKeyAttributes": NotRequired[List[str]],
    },
)
ProvisionedThroughputTypeDef = TypedDict(
    "ProvisionedThroughputTypeDef",
    {
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
)
ProjectionTypeDef = TypedDict(
    "ProjectionTypeDef",
    {
        "ProjectionType": NotRequired[ProjectionTypeType],
        "NonKeyAttributes": NotRequired[Sequence[str]],
    },
)
ReplicaTypeDef = TypedDict(
    "ReplicaTypeDef",
    {
        "RegionName": NotRequired[str],
    },
)
CreateReplicaActionTypeDef = TypedDict(
    "CreateReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)
ProvisionedThroughputOverrideTypeDef = TypedDict(
    "ProvisionedThroughputOverrideTypeDef",
    {
        "ReadCapacityUnits": NotRequired[int],
    },
)
SSESpecificationTypeDef = TypedDict(
    "SSESpecificationTypeDef",
    {
        "Enabled": NotRequired[bool],
        "SSEType": NotRequired[SSETypeType],
        "KMSMasterKeyId": NotRequired[str],
    },
)
StreamSpecificationTypeDef = TypedDict(
    "StreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": NotRequired[StreamViewTypeType],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CsvOptionsTypeDef = TypedDict(
    "CsvOptionsTypeDef",
    {
        "Delimiter": NotRequired[str],
        "HeaderList": NotRequired[List[str]],
    },
)
DeleteBackupInputRequestTypeDef = TypedDict(
    "DeleteBackupInputRequestTypeDef",
    {
        "BackupArn": str,
    },
)
DeleteGlobalSecondaryIndexActionTypeDef = TypedDict(
    "DeleteGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
    },
)
DeleteReplicaActionTypeDef = TypedDict(
    "DeleteReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)
DeleteReplicationGroupMemberActionTypeDef = TypedDict(
    "DeleteReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)
DeleteTableInputRequestTypeDef = TypedDict(
    "DeleteTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)
DescribeBackupInputRequestTypeDef = TypedDict(
    "DescribeBackupInputRequestTypeDef",
    {
        "BackupArn": str,
    },
)
DescribeContinuousBackupsInputRequestTypeDef = TypedDict(
    "DescribeContinuousBackupsInputRequestTypeDef",
    {
        "TableName": str,
    },
)
DescribeContributorInsightsInputRequestTypeDef = TypedDict(
    "DescribeContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
        "IndexName": NotRequired[str],
    },
)
FailureExceptionTypeDef = TypedDict(
    "FailureExceptionTypeDef",
    {
        "ExceptionName": NotRequired[str],
        "ExceptionDescription": NotRequired[str],
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)
DescribeExportInputRequestTypeDef = TypedDict(
    "DescribeExportInputRequestTypeDef",
    {
        "ExportArn": str,
    },
)
DescribeGlobalTableInputRequestTypeDef = TypedDict(
    "DescribeGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)
DescribeGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "DescribeGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)
DescribeImportInputRequestTypeDef = TypedDict(
    "DescribeImportInputRequestTypeDef",
    {
        "ImportArn": str,
    },
)
DescribeKinesisStreamingDestinationInputRequestTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationInputRequestTypeDef",
    {
        "TableName": str,
    },
)
KinesisDataStreamDestinationTypeDef = TypedDict(
    "KinesisDataStreamDestinationTypeDef",
    {
        "StreamArn": NotRequired[str],
        "DestinationStatus": NotRequired[DestinationStatusType],
        "DestinationStatusDescription": NotRequired[str],
    },
)
DescribeTableInputRequestTypeDef = TypedDict(
    "DescribeTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingInputRequestTypeDef",
    {
        "TableName": str,
    },
)
DescribeTimeToLiveInputRequestTypeDef = TypedDict(
    "DescribeTimeToLiveInputRequestTypeDef",
    {
        "TableName": str,
    },
)
TimeToLiveDescriptionTypeDef = TypedDict(
    "TimeToLiveDescriptionTypeDef",
    {
        "TimeToLiveStatus": NotRequired[TimeToLiveStatusType],
        "AttributeName": NotRequired[str],
    },
)
IncrementalExportSpecificationTypeDef = TypedDict(
    "IncrementalExportSpecificationTypeDef",
    {
        "ExportFromTime": NotRequired[datetime],
        "ExportToTime": NotRequired[datetime],
        "ExportViewType": NotRequired[ExportViewTypeType],
    },
)
ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "ExportArn": NotRequired[str],
        "ExportStatus": NotRequired[ExportStatusType],
        "ExportType": NotRequired[ExportTypeType],
    },
)
TimestampTypeDef = Union[datetime, str]
ProvisionedThroughputDescriptionTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionTypeDef",
    {
        "LastIncreaseDateTime": NotRequired[datetime],
        "LastDecreaseDateTime": NotRequired[datetime],
        "NumberOfDecreasesToday": NotRequired[int],
        "ReadCapacityUnits": NotRequired[int],
        "WriteCapacityUnits": NotRequired[int],
    },
)
S3BucketSourceTypeDef = TypedDict(
    "S3BucketSourceTypeDef",
    {
        "S3Bucket": str,
        "S3BucketOwner": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
    },
)
KinesisStreamingDestinationInputRequestTypeDef = TypedDict(
    "KinesisStreamingDestinationInputRequestTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
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
ListContributorInsightsInputRequestTypeDef = TypedDict(
    "ListContributorInsightsInputRequestTypeDef",
    {
        "TableName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListExportsInputRequestTypeDef = TypedDict(
    "ListExportsInputRequestTypeDef",
    {
        "TableArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListGlobalTablesInputRequestTypeDef = TypedDict(
    "ListGlobalTablesInputRequestTypeDef",
    {
        "ExclusiveStartGlobalTableName": NotRequired[str],
        "Limit": NotRequired[int],
        "RegionName": NotRequired[str],
    },
)
ListImportsInputRequestTypeDef = TypedDict(
    "ListImportsInputRequestTypeDef",
    {
        "TableArn": NotRequired[str],
        "PageSize": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTablesInputRequestTypeDef = TypedDict(
    "ListTablesInputRequestTypeDef",
    {
        "ExclusiveStartTableName": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListTagsOfResourceInputRequestTypeDef = TypedDict(
    "ListTagsOfResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
    },
)
PointInTimeRecoverySpecificationTypeDef = TypedDict(
    "PointInTimeRecoverySpecificationTypeDef",
    {
        "PointInTimeRecoveryEnabled": bool,
    },
)
TableClassSummaryTypeDef = TypedDict(
    "TableClassSummaryTypeDef",
    {
        "TableClass": NotRequired[TableClassType],
        "LastUpdateDateTime": NotRequired[datetime],
    },
)
RestoreSummaryTypeDef = TypedDict(
    "RestoreSummaryTypeDef",
    {
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
        "SourceBackupArn": NotRequired[str],
        "SourceTableArn": NotRequired[str],
    },
)
SSEDescriptionTypeDef = TypedDict(
    "SSEDescriptionTypeDef",
    {
        "Status": NotRequired[SSEStatusType],
        "SSEType": NotRequired[SSETypeType],
        "KMSMasterKeyArn": NotRequired[str],
        "InaccessibleEncryptionDateTime": NotRequired[datetime],
    },
)
TableBatchWriterRequestTypeDef = TypedDict(
    "TableBatchWriterRequestTypeDef",
    {
        "overwrite_by_pkeys": NotRequired[List[str]],
    },
)
TimeToLiveSpecificationTypeDef = TypedDict(
    "TimeToLiveSpecificationTypeDef",
    {
        "Enabled": bool,
        "AttributeName": str,
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateContributorInsightsInputRequestTypeDef = TypedDict(
    "UpdateContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
        "ContributorInsightsAction": ContributorInsightsActionType,
        "IndexName": NotRequired[str],
    },
)
ArchivalSummaryResponseTypeDef = TypedDict(
    "ArchivalSummaryResponseTypeDef",
    {
        "ArchivalDateTime": datetime,
        "ArchivalReason": str,
        "ArchivalBackupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BillingModeSummaryResponseTypeDef = TypedDict(
    "BillingModeSummaryResponseTypeDef",
    {
        "BillingMode": BillingModeType,
        "LastUpdateToPayPerRequestDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLimitsOutputTypeDef = TypedDict(
    "DescribeLimitsOutputTypeDef",
    {
        "AccountMaxReadCapacityUnits": int,
        "AccountMaxWriteCapacityUnits": int,
        "TableMaxReadCapacityUnits": int,
        "TableMaxWriteCapacityUnits": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KinesisStreamingDestinationOutputTypeDef = TypedDict(
    "KinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
        "DestinationStatus": DestinationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTablesOutputTypeDef = TypedDict(
    "ListTablesOutputTypeDef",
    {
        "TableNames": List[str],
        "LastEvaluatedTableName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisionedThroughputDescriptionResponseTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionResponseTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreSummaryResponseTypeDef = TypedDict(
    "RestoreSummaryResponseTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SSEDescriptionResponseTypeDef = TypedDict(
    "SSEDescriptionResponseTypeDef",
    {
        "Status": SSEStatusType,
        "SSEType": SSETypeType,
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StreamSpecificationResponseTypeDef = TypedDict(
    "StreamSpecificationResponseTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": StreamViewTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TableClassSummaryResponseTypeDef = TypedDict(
    "TableClassSummaryResponseTypeDef",
    {
        "TableClass": TableClassType,
        "LastUpdateDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateContributorInsightsOutputTypeDef = TypedDict(
    "UpdateContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchStatementErrorTypeDef = TypedDict(
    "BatchStatementErrorTypeDef",
    {
        "Code": NotRequired[BatchStatementErrorCodeEnumType],
        "Message": NotRequired[str],
        "Item": NotRequired[Dict[str, AttributeValueTypeDef]],
    },
)
ItemCollectionMetricsTypeDef = TypedDict(
    "ItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": NotRequired[Dict[str, AttributeValueTypeDef]],
        "SizeEstimateRangeGB": NotRequired[List[float]],
    },
)
ItemResponseTypeDef = TypedDict(
    "ItemResponseTypeDef",
    {
        "Item": NotRequired[Dict[str, AttributeValueTypeDef]],
    },
)
UniversalAttributeValueTypeDef = Union[
    AttributeValueTypeDef,
    bytes,
    bytearray,
    str,
    int,
    Decimal,
    bool,
    Set[int],
    Set[Decimal],
    Set[str],
    Set[bytes],
    Set[bytearray],
    Sequence[Any],
    Mapping[str, Any],
    None,
]
AttributeValueUpdateTableTypeDef = TypedDict(
    "AttributeValueUpdateTableTypeDef",
    {
        "Value": NotRequired[TableAttributeValueTypeDef],
        "Action": NotRequired[AttributeActionType],
    },
)
ConditionTableTypeDef = TypedDict(
    "ConditionTableTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
        "AttributeValueList": NotRequired[Sequence[TableAttributeValueTypeDef]],
    },
)
DeleteRequestServiceResourceTypeDef = TypedDict(
    "DeleteRequestServiceResourceTypeDef",
    {
        "Key": Mapping[str, TableAttributeValueTypeDef],
    },
)
ExpectedAttributeValueTableTypeDef = TypedDict(
    "ExpectedAttributeValueTableTypeDef",
    {
        "Value": NotRequired[TableAttributeValueTypeDef],
        "Exists": NotRequired[bool],
        "ComparisonOperator": NotRequired[ComparisonOperatorType],
        "AttributeValueList": NotRequired[Sequence[TableAttributeValueTypeDef]],
    },
)
GetItemInputTableGetItemTypeDef = TypedDict(
    "GetItemInputTableGetItemTypeDef",
    {
        "Key": Mapping[str, TableAttributeValueTypeDef],
        "AttributesToGet": NotRequired[Sequence[str]],
        "ConsistentRead": NotRequired[bool],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ProjectionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
    },
)
ItemCollectionMetricsServiceResourceTypeDef = TypedDict(
    "ItemCollectionMetricsServiceResourceTypeDef",
    {
        "ItemCollectionKey": NotRequired[Dict[str, TableAttributeValueTypeDef]],
        "SizeEstimateRangeGB": NotRequired[List[float]],
    },
)
ItemCollectionMetricsTableTypeDef = TypedDict(
    "ItemCollectionMetricsTableTypeDef",
    {
        "ItemCollectionKey": NotRequired[Dict[str, TableAttributeValueTypeDef]],
        "SizeEstimateRangeGB": NotRequired[List[float]],
    },
)
KeysAndAttributesServiceResourceTypeDef = TypedDict(
    "KeysAndAttributesServiceResourceTypeDef",
    {
        "Keys": Sequence[Mapping[str, TableAttributeValueTypeDef]],
        "AttributesToGet": NotRequired[Sequence[str]],
        "ConsistentRead": NotRequired[bool],
        "ProjectionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
    },
)
PutRequestServiceResourceTypeDef = TypedDict(
    "PutRequestServiceResourceTypeDef",
    {
        "Item": Mapping[str, TableAttributeValueTypeDef],
    },
)
AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "PolicyName": NotRequired[str],
        "TargetTrackingScalingPolicyConfiguration": NotRequired[
            AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef
        ],
    },
)
AutoScalingPolicyUpdateTypeDef = TypedDict(
    "AutoScalingPolicyUpdateTypeDef",
    {
        "TargetTrackingScalingPolicyConfiguration": (
            AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef
        ),
        "PolicyName": NotRequired[str],
    },
)
CreateBackupOutputTypeDef = TypedDict(
    "CreateBackupOutputTypeDef",
    {
        "BackupDetails": BackupDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBackupsOutputTypeDef = TypedDict(
    "ListBackupsOutputTypeDef",
    {
        "BackupSummaries": List[BackupSummaryTypeDef],
        "LastEvaluatedBackupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConsumedCapacityTypeDef = TypedDict(
    "ConsumedCapacityTypeDef",
    {
        "TableName": NotRequired[str],
        "CapacityUnits": NotRequired[float],
        "ReadCapacityUnits": NotRequired[float],
        "WriteCapacityUnits": NotRequired[float],
        "Table": NotRequired[CapacityTypeDef],
        "LocalSecondaryIndexes": NotRequired[Dict[str, CapacityTypeDef]],
        "GlobalSecondaryIndexes": NotRequired[Dict[str, CapacityTypeDef]],
    },
)
ContinuousBackupsDescriptionTypeDef = TypedDict(
    "ContinuousBackupsDescriptionTypeDef",
    {
        "ContinuousBackupsStatus": ContinuousBackupsStatusType,
        "PointInTimeRecoveryDescription": NotRequired[PointInTimeRecoveryDescriptionTypeDef],
    },
)
ListContributorInsightsOutputTypeDef = TypedDict(
    "ListContributorInsightsOutputTypeDef",
    {
        "ContributorInsightsSummaries": List[ContributorInsightsSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LocalSecondaryIndexDescriptionTableTypeDef = TypedDict(
    "LocalSecondaryIndexDescriptionTableTypeDef",
    {
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List[KeySchemaElementTypeDef]],
        "Projection": NotRequired[ProjectionTableTypeDef],
        "IndexSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "IndexArn": NotRequired[str],
    },
)
CreateGlobalSecondaryIndexActionTableTypeDef = TypedDict(
    "CreateGlobalSecondaryIndexActionTableTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "Projection": ProjectionTableTypeDef,
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputTypeDef],
    },
)
SourceTableDetailsTypeDef = TypedDict(
    "SourceTableDetailsTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "KeySchema": List[KeySchemaElementTypeDef],
        "TableCreationDateTime": datetime,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "TableArn": NotRequired[str],
        "TableSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "BillingMode": NotRequired[BillingModeType],
    },
)
UpdateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "UpdateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
    },
)
CreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "CreateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "Projection": ProjectionTypeDef,
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputTypeDef],
    },
)
GlobalSecondaryIndexInfoTypeDef = TypedDict(
    "GlobalSecondaryIndexInfoTypeDef",
    {
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List[KeySchemaElementTypeDef]],
        "Projection": NotRequired[ProjectionTypeDef],
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputTypeDef],
    },
)
GlobalSecondaryIndexTypeDef = TypedDict(
    "GlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "Projection": ProjectionTypeDef,
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputTypeDef],
    },
)
LocalSecondaryIndexDescriptionTypeDef = TypedDict(
    "LocalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List[KeySchemaElementTypeDef]],
        "Projection": NotRequired[ProjectionTypeDef],
        "IndexSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "IndexArn": NotRequired[str],
    },
)
LocalSecondaryIndexInfoTypeDef = TypedDict(
    "LocalSecondaryIndexInfoTypeDef",
    {
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List[KeySchemaElementTypeDef]],
        "Projection": NotRequired[ProjectionTypeDef],
    },
)
LocalSecondaryIndexTypeDef = TypedDict(
    "LocalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "Projection": ProjectionTypeDef,
    },
)
CreateGlobalTableInputRequestTypeDef = TypedDict(
    "CreateGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "ReplicationGroup": Sequence[ReplicaTypeDef],
    },
)
GlobalTableTypeDef = TypedDict(
    "GlobalTableTypeDef",
    {
        "GlobalTableName": NotRequired[str],
        "ReplicationGroup": NotRequired[List[ReplicaTypeDef]],
    },
)
ReplicaGlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[ProvisionedThroughputOverrideTypeDef],
    },
)
ReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": NotRequired[ProvisionedThroughputOverrideTypeDef],
    },
)
ListTagsOfResourceOutputTypeDef = TypedDict(
    "ListTagsOfResourceOutputTypeDef",
    {
        "Tags": List[TagTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
InputFormatOptionsTypeDef = TypedDict(
    "InputFormatOptionsTypeDef",
    {
        "Csv": NotRequired[CsvOptionsTypeDef],
    },
)
ReplicaUpdateTypeDef = TypedDict(
    "ReplicaUpdateTypeDef",
    {
        "Create": NotRequired[CreateReplicaActionTypeDef],
        "Delete": NotRequired[DeleteReplicaActionTypeDef],
    },
)
DescribeContributorInsightsOutputTypeDef = TypedDict(
    "DescribeContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsRuleList": List[str],
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "LastUpdateDateTime": datetime,
        "FailureException": FailureExceptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List[EndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeKinesisStreamingDestinationOutputTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "KinesisDataStreamDestinations": List[KinesisDataStreamDestinationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTableInputTableExistsWaitTypeDef = TypedDict(
    "DescribeTableInputTableExistsWaitTypeDef",
    {
        "TableName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeTableInputTableNotExistsWaitTypeDef = TypedDict(
    "DescribeTableInputTableNotExistsWaitTypeDef",
    {
        "TableName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeTimeToLiveOutputTypeDef = TypedDict(
    "DescribeTimeToLiveOutputTypeDef",
    {
        "TimeToLiveDescription": TimeToLiveDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportDescriptionTypeDef = TypedDict(
    "ExportDescriptionTypeDef",
    {
        "ExportArn": NotRequired[str],
        "ExportStatus": NotRequired[ExportStatusType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "ExportManifest": NotRequired[str],
        "TableArn": NotRequired[str],
        "TableId": NotRequired[str],
        "ExportTime": NotRequired[datetime],
        "ClientToken": NotRequired[str],
        "S3Bucket": NotRequired[str],
        "S3BucketOwner": NotRequired[str],
        "S3Prefix": NotRequired[str],
        "S3SseAlgorithm": NotRequired[S3SseAlgorithmType],
        "S3SseKmsKeyId": NotRequired[str],
        "FailureCode": NotRequired[str],
        "FailureMessage": NotRequired[str],
        "ExportFormat": NotRequired[ExportFormatType],
        "BilledSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "ExportType": NotRequired[ExportTypeType],
        "IncrementalExportSpecification": NotRequired[IncrementalExportSpecificationTypeDef],
    },
)
ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef",
    {
        "ExportSummaries": List[ExportSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportTableToPointInTimeInputRequestTypeDef = TypedDict(
    "ExportTableToPointInTimeInputRequestTypeDef",
    {
        "TableArn": str,
        "S3Bucket": str,
        "ExportTime": NotRequired[TimestampTypeDef],
        "ClientToken": NotRequired[str],
        "S3BucketOwner": NotRequired[str],
        "S3Prefix": NotRequired[str],
        "S3SseAlgorithm": NotRequired[S3SseAlgorithmType],
        "S3SseKmsKeyId": NotRequired[str],
        "ExportFormat": NotRequired[ExportFormatType],
        "ExportType": NotRequired[ExportTypeType],
        "IncrementalExportSpecification": NotRequired[IncrementalExportSpecificationTypeDef],
    },
)
ListBackupsInputRequestTypeDef = TypedDict(
    "ListBackupsInputRequestTypeDef",
    {
        "TableName": NotRequired[str],
        "Limit": NotRequired[int],
        "TimeRangeLowerBound": NotRequired[TimestampTypeDef],
        "TimeRangeUpperBound": NotRequired[TimestampTypeDef],
        "ExclusiveStartBackupArn": NotRequired[str],
        "BackupType": NotRequired[BackupTypeFilterType],
    },
)
GlobalSecondaryIndexDescriptionTableTypeDef = TypedDict(
    "GlobalSecondaryIndexDescriptionTableTypeDef",
    {
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List[KeySchemaElementTypeDef]],
        "Projection": NotRequired[ProjectionTableTypeDef],
        "IndexStatus": NotRequired[IndexStatusType],
        "Backfilling": NotRequired[bool],
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputDescriptionTypeDef],
        "IndexSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "IndexArn": NotRequired[str],
    },
)
GlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "GlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List[KeySchemaElementTypeDef]],
        "Projection": NotRequired[ProjectionTypeDef],
        "IndexStatus": NotRequired[IndexStatusType],
        "Backfilling": NotRequired[bool],
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputDescriptionTypeDef],
        "IndexSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "IndexArn": NotRequired[str],
    },
)
ImportSummaryTypeDef = TypedDict(
    "ImportSummaryTypeDef",
    {
        "ImportArn": NotRequired[str],
        "ImportStatus": NotRequired[ImportStatusType],
        "TableArn": NotRequired[str],
        "S3BucketSource": NotRequired[S3BucketSourceTypeDef],
        "CloudWatchLogGroupArn": NotRequired[str],
        "InputFormat": NotRequired[InputFormatType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)
ListBackupsInputListBackupsPaginateTypeDef = TypedDict(
    "ListBackupsInputListBackupsPaginateTypeDef",
    {
        "TableName": NotRequired[str],
        "TimeRangeLowerBound": NotRequired[TimestampTypeDef],
        "TimeRangeUpperBound": NotRequired[TimestampTypeDef],
        "BackupType": NotRequired[BackupTypeFilterType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTablesInputListTablesPaginateTypeDef = TypedDict(
    "ListTablesInputListTablesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsOfResourceInputListTagsOfResourcePaginateTypeDef = TypedDict(
    "ListTagsOfResourceInputListTagsOfResourcePaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
UpdateContinuousBackupsInputRequestTypeDef = TypedDict(
    "UpdateContinuousBackupsInputRequestTypeDef",
    {
        "TableName": str,
        "PointInTimeRecoverySpecification": PointInTimeRecoverySpecificationTypeDef,
    },
)
UpdateTimeToLiveInputRequestTypeDef = TypedDict(
    "UpdateTimeToLiveInputRequestTypeDef",
    {
        "TableName": str,
        "TimeToLiveSpecification": TimeToLiveSpecificationTypeDef,
    },
)
UpdateTimeToLiveOutputTypeDef = TypedDict(
    "UpdateTimeToLiveOutputTypeDef",
    {
        "TimeToLiveSpecification": TimeToLiveSpecificationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchStatementResponseTypeDef = TypedDict(
    "BatchStatementResponseTypeDef",
    {
        "Error": NotRequired[BatchStatementErrorTypeDef],
        "TableName": NotRequired[str],
        "Item": NotRequired[Dict[str, AttributeValueTypeDef]],
    },
)
AttributeValueUpdateTypeDef = TypedDict(
    "AttributeValueUpdateTypeDef",
    {
        "Value": NotRequired[UniversalAttributeValueTypeDef],
        "Action": NotRequired[AttributeActionType],
    },
)
BatchStatementRequestTypeDef = TypedDict(
    "BatchStatementRequestTypeDef",
    {
        "Statement": str,
        "Parameters": NotRequired[Sequence[UniversalAttributeValueTypeDef]],
        "ConsistentRead": NotRequired[bool],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
ConditionCheckTypeDef = TypedDict(
    "ConditionCheckTypeDef",
    {
        "Key": Mapping[str, UniversalAttributeValueTypeDef],
        "TableName": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
        "AttributeValueList": NotRequired[Sequence[UniversalAttributeValueTypeDef]],
    },
)
DeleteRequestTypeDef = TypedDict(
    "DeleteRequestTypeDef",
    {
        "Key": Mapping[str, UniversalAttributeValueTypeDef],
    },
)
DeleteTypeDef = TypedDict(
    "DeleteTypeDef",
    {
        "Key": Mapping[str, UniversalAttributeValueTypeDef],
        "TableName": str,
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
ExecuteStatementInputRequestTypeDef = TypedDict(
    "ExecuteStatementInputRequestTypeDef",
    {
        "Statement": str,
        "Parameters": NotRequired[Sequence[UniversalAttributeValueTypeDef]],
        "ConsistentRead": NotRequired[bool],
        "NextToken": NotRequired[str],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "Limit": NotRequired[int],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
ExpectedAttributeValueTypeDef = TypedDict(
    "ExpectedAttributeValueTypeDef",
    {
        "Value": NotRequired[UniversalAttributeValueTypeDef],
        "Exists": NotRequired[bool],
        "ComparisonOperator": NotRequired[ComparisonOperatorType],
        "AttributeValueList": NotRequired[Sequence[UniversalAttributeValueTypeDef]],
    },
)
GetItemInputRequestTypeDef = TypedDict(
    "GetItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[str, UniversalAttributeValueTypeDef],
        "AttributesToGet": NotRequired[Sequence[str]],
        "ConsistentRead": NotRequired[bool],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ProjectionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
    },
)
GetTypeDef = TypedDict(
    "GetTypeDef",
    {
        "Key": Mapping[str, UniversalAttributeValueTypeDef],
        "TableName": str,
        "ProjectionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
    },
)
KeysAndAttributesTypeDef = TypedDict(
    "KeysAndAttributesTypeDef",
    {
        "Keys": Sequence[Mapping[str, UniversalAttributeValueTypeDef]],
        "AttributesToGet": NotRequired[Sequence[str]],
        "ConsistentRead": NotRequired[bool],
        "ProjectionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
    },
)
ParameterizedStatementTypeDef = TypedDict(
    "ParameterizedStatementTypeDef",
    {
        "Statement": str,
        "Parameters": NotRequired[Sequence[UniversalAttributeValueTypeDef]],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
PutRequestTypeDef = TypedDict(
    "PutRequestTypeDef",
    {
        "Item": Mapping[str, UniversalAttributeValueTypeDef],
    },
)
PutTypeDef = TypedDict(
    "PutTypeDef",
    {
        "Item": Mapping[str, UniversalAttributeValueTypeDef],
        "TableName": str,
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
UpdateTypeDef = TypedDict(
    "UpdateTypeDef",
    {
        "Key": Mapping[str, UniversalAttributeValueTypeDef],
        "UpdateExpression": str,
        "TableName": str,
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
QueryInputTableQueryTypeDef = TypedDict(
    "QueryInputTableQueryTypeDef",
    {
        "IndexName": NotRequired[str],
        "Select": NotRequired[SelectType],
        "AttributesToGet": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "ConsistentRead": NotRequired[bool],
        "KeyConditions": NotRequired[Mapping[str, ConditionTableTypeDef]],
        "QueryFilter": NotRequired[Mapping[str, ConditionTableTypeDef]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ScanIndexForward": NotRequired[bool],
        "ExclusiveStartKey": NotRequired[Mapping[str, TableAttributeValueTypeDef]],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ProjectionExpression": NotRequired[str],
        "FilterExpression": NotRequired[ConditionBaseImportTypeDef],
        "KeyConditionExpression": NotRequired[ConditionBaseImportTypeDef],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, TableAttributeValueTypeDef]],
    },
)
ScanInputTableScanTypeDef = TypedDict(
    "ScanInputTableScanTypeDef",
    {
        "IndexName": NotRequired[str],
        "AttributesToGet": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "Select": NotRequired[SelectType],
        "ScanFilter": NotRequired[Mapping[str, ConditionTableTypeDef]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ExclusiveStartKey": NotRequired[Mapping[str, TableAttributeValueTypeDef]],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "TotalSegments": NotRequired[int],
        "Segment": NotRequired[int],
        "ProjectionExpression": NotRequired[str],
        "FilterExpression": NotRequired[ConditionBaseImportTypeDef],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, TableAttributeValueTypeDef]],
        "ConsistentRead": NotRequired[bool],
    },
)
DeleteItemInputTableDeleteItemTypeDef = TypedDict(
    "DeleteItemInputTableDeleteItemTypeDef",
    {
        "Key": Mapping[str, TableAttributeValueTypeDef],
        "Expected": NotRequired[Mapping[str, ExpectedAttributeValueTableTypeDef]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "ConditionExpression": NotRequired[ConditionBaseImportTypeDef],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, TableAttributeValueTypeDef]],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
PutItemInputTablePutItemTypeDef = TypedDict(
    "PutItemInputTablePutItemTypeDef",
    {
        "Item": Mapping[str, TableAttributeValueTypeDef],
        "Expected": NotRequired[Mapping[str, ExpectedAttributeValueTableTypeDef]],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ConditionExpression": NotRequired[ConditionBaseImportTypeDef],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, TableAttributeValueTypeDef]],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
UpdateItemInputTableUpdateItemTypeDef = TypedDict(
    "UpdateItemInputTableUpdateItemTypeDef",
    {
        "Key": Mapping[str, TableAttributeValueTypeDef],
        "AttributeUpdates": NotRequired[Mapping[str, AttributeValueUpdateTableTypeDef]],
        "Expected": NotRequired[Mapping[str, ExpectedAttributeValueTableTypeDef]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "UpdateExpression": NotRequired[str],
        "ConditionExpression": NotRequired[ConditionBaseImportTypeDef],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, TableAttributeValueTypeDef]],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
BatchGetItemInputServiceResourceBatchGetItemTypeDef = TypedDict(
    "BatchGetItemInputServiceResourceBatchGetItemTypeDef",
    {
        "RequestItems": Mapping[str, KeysAndAttributesServiceResourceTypeDef],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
    },
)
WriteRequestServiceResourceTypeDef = TypedDict(
    "WriteRequestServiceResourceTypeDef",
    {
        "PutRequest": NotRequired[PutRequestServiceResourceTypeDef],
        "DeleteRequest": NotRequired[DeleteRequestServiceResourceTypeDef],
    },
)
AutoScalingSettingsDescriptionTypeDef = TypedDict(
    "AutoScalingSettingsDescriptionTypeDef",
    {
        "MinimumUnits": NotRequired[int],
        "MaximumUnits": NotRequired[int],
        "AutoScalingDisabled": NotRequired[bool],
        "AutoScalingRoleArn": NotRequired[str],
        "ScalingPolicies": NotRequired[List[AutoScalingPolicyDescriptionTypeDef]],
    },
)
AutoScalingSettingsUpdateTypeDef = TypedDict(
    "AutoScalingSettingsUpdateTypeDef",
    {
        "MinimumUnits": NotRequired[int],
        "MaximumUnits": NotRequired[int],
        "AutoScalingDisabled": NotRequired[bool],
        "AutoScalingRoleArn": NotRequired[str],
        "ScalingPolicyUpdate": NotRequired[AutoScalingPolicyUpdateTypeDef],
    },
)
BatchGetItemOutputServiceResourceTypeDef = TypedDict(
    "BatchGetItemOutputServiceResourceTypeDef",
    {
        "Responses": Dict[str, List[Dict[str, TableAttributeValueTypeDef]]],
        "UnprocessedKeys": Dict[str, KeysAndAttributesServiceResourceTypeDef],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteItemOutputTableTypeDef = TypedDict(
    "DeleteItemOutputTableTypeDef",
    {
        "Attributes": Dict[str, TableAttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteItemOutputTypeDef = TypedDict(
    "DeleteItemOutputTypeDef",
    {
        "Attributes": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecuteStatementOutputTypeDef = TypedDict(
    "ExecuteStatementOutputTypeDef",
    {
        "Items": List[Dict[str, AttributeValueTypeDef]],
        "NextToken": str,
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "LastEvaluatedKey": Dict[str, AttributeValueTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecuteTransactionOutputTypeDef = TypedDict(
    "ExecuteTransactionOutputTypeDef",
    {
        "Responses": List[ItemResponseTypeDef],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetItemOutputTableTypeDef = TypedDict(
    "GetItemOutputTableTypeDef",
    {
        "Item": Dict[str, TableAttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetItemOutputTypeDef = TypedDict(
    "GetItemOutputTypeDef",
    {
        "Item": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutItemOutputTableTypeDef = TypedDict(
    "PutItemOutputTableTypeDef",
    {
        "Attributes": Dict[str, TableAttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutItemOutputTypeDef = TypedDict(
    "PutItemOutputTypeDef",
    {
        "Attributes": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
QueryOutputTableTypeDef = TypedDict(
    "QueryOutputTableTypeDef",
    {
        "Items": List[Dict[str, TableAttributeValueTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, TableAttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
QueryOutputTypeDef = TypedDict(
    "QueryOutputTypeDef",
    {
        "Items": List[Dict[str, AttributeValueTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScanOutputTableTypeDef = TypedDict(
    "ScanOutputTableTypeDef",
    {
        "Items": List[Dict[str, TableAttributeValueTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, TableAttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScanOutputTypeDef = TypedDict(
    "ScanOutputTypeDef",
    {
        "Items": List[Dict[str, AttributeValueTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TransactGetItemsOutputTypeDef = TypedDict(
    "TransactGetItemsOutputTypeDef",
    {
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "Responses": List[ItemResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TransactWriteItemsOutputTypeDef = TypedDict(
    "TransactWriteItemsOutputTypeDef",
    {
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ItemCollectionMetrics": Dict[str, List[ItemCollectionMetricsTypeDef]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateItemOutputTableTypeDef = TypedDict(
    "UpdateItemOutputTableTypeDef",
    {
        "Attributes": Dict[str, TableAttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateItemOutputTypeDef = TypedDict(
    "UpdateItemOutputTypeDef",
    {
        "Attributes": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeContinuousBackupsOutputTypeDef = TypedDict(
    "DescribeContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": ContinuousBackupsDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateContinuousBackupsOutputTypeDef = TypedDict(
    "UpdateContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": ContinuousBackupsDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GlobalSecondaryIndexUpdateTableTypeDef = TypedDict(
    "GlobalSecondaryIndexUpdateTableTypeDef",
    {
        "Update": NotRequired[UpdateGlobalSecondaryIndexActionTypeDef],
        "Create": NotRequired[CreateGlobalSecondaryIndexActionTableTypeDef],
        "Delete": NotRequired[DeleteGlobalSecondaryIndexActionTypeDef],
    },
)
GlobalSecondaryIndexUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexUpdateTypeDef",
    {
        "Update": NotRequired[UpdateGlobalSecondaryIndexActionTypeDef],
        "Create": NotRequired[CreateGlobalSecondaryIndexActionTypeDef],
        "Delete": NotRequired[DeleteGlobalSecondaryIndexActionTypeDef],
    },
)
TableCreationParametersTypeDef = TypedDict(
    "TableCreationParametersTypeDef",
    {
        "TableName": str,
        "AttributeDefinitions": List[AttributeDefinitionTypeDef],
        "KeySchema": List[KeySchemaElementTypeDef],
        "BillingMode": NotRequired[BillingModeType],
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputTypeDef],
        "SSESpecification": NotRequired[SSESpecificationTypeDef],
        "GlobalSecondaryIndexes": NotRequired[List[GlobalSecondaryIndexTypeDef]],
    },
)
SourceTableFeatureDetailsTypeDef = TypedDict(
    "SourceTableFeatureDetailsTypeDef",
    {
        "LocalSecondaryIndexes": NotRequired[List[LocalSecondaryIndexInfoTypeDef]],
        "GlobalSecondaryIndexes": NotRequired[List[GlobalSecondaryIndexInfoTypeDef]],
        "StreamDescription": NotRequired[StreamSpecificationTypeDef],
        "TimeToLiveDescription": NotRequired[TimeToLiveDescriptionTypeDef],
        "SSEDescription": NotRequired[SSEDescriptionTypeDef],
    },
)
CreateTableInputRequestTypeDef = TypedDict(
    "CreateTableInputRequestTypeDef",
    {
        "AttributeDefinitions": Sequence[AttributeDefinitionTypeDef],
        "TableName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "LocalSecondaryIndexes": NotRequired[Sequence[LocalSecondaryIndexTypeDef]],
        "GlobalSecondaryIndexes": NotRequired[Sequence[GlobalSecondaryIndexTypeDef]],
        "BillingMode": NotRequired[BillingModeType],
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputTypeDef],
        "StreamSpecification": NotRequired[StreamSpecificationTypeDef],
        "SSESpecification": NotRequired[SSESpecificationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "TableClass": NotRequired[TableClassType],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
CreateTableInputServiceResourceCreateTableTypeDef = TypedDict(
    "CreateTableInputServiceResourceCreateTableTypeDef",
    {
        "AttributeDefinitions": Sequence[AttributeDefinitionTypeDef],
        "TableName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "LocalSecondaryIndexes": NotRequired[Sequence[LocalSecondaryIndexTypeDef]],
        "GlobalSecondaryIndexes": NotRequired[Sequence[GlobalSecondaryIndexTypeDef]],
        "BillingMode": NotRequired[BillingModeType],
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputTypeDef],
        "StreamSpecification": NotRequired[StreamSpecificationTypeDef],
        "SSESpecification": NotRequired[SSESpecificationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "TableClass": NotRequired[TableClassType],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
RestoreTableFromBackupInputRequestTypeDef = TypedDict(
    "RestoreTableFromBackupInputRequestTypeDef",
    {
        "TargetTableName": str,
        "BackupArn": str,
        "BillingModeOverride": NotRequired[BillingModeType],
        "GlobalSecondaryIndexOverride": NotRequired[Sequence[GlobalSecondaryIndexTypeDef]],
        "LocalSecondaryIndexOverride": NotRequired[Sequence[LocalSecondaryIndexTypeDef]],
        "ProvisionedThroughputOverride": NotRequired[ProvisionedThroughputTypeDef],
        "SSESpecificationOverride": NotRequired[SSESpecificationTypeDef],
    },
)
RestoreTableToPointInTimeInputRequestTypeDef = TypedDict(
    "RestoreTableToPointInTimeInputRequestTypeDef",
    {
        "TargetTableName": str,
        "SourceTableArn": NotRequired[str],
        "SourceTableName": NotRequired[str],
        "UseLatestRestorableTime": NotRequired[bool],
        "RestoreDateTime": NotRequired[TimestampTypeDef],
        "BillingModeOverride": NotRequired[BillingModeType],
        "GlobalSecondaryIndexOverride": NotRequired[Sequence[GlobalSecondaryIndexTypeDef]],
        "LocalSecondaryIndexOverride": NotRequired[Sequence[LocalSecondaryIndexTypeDef]],
        "ProvisionedThroughputOverride": NotRequired[ProvisionedThroughputTypeDef],
        "SSESpecificationOverride": NotRequired[SSESpecificationTypeDef],
    },
)
ListGlobalTablesOutputTypeDef = TypedDict(
    "ListGlobalTablesOutputTypeDef",
    {
        "GlobalTables": List[GlobalTableTypeDef],
        "LastEvaluatedGlobalTableName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplicaDescriptionTypeDef = TypedDict(
    "ReplicaDescriptionTypeDef",
    {
        "RegionName": NotRequired[str],
        "ReplicaStatus": NotRequired[ReplicaStatusType],
        "ReplicaStatusDescription": NotRequired[str],
        "ReplicaStatusPercentProgress": NotRequired[str],
        "KMSMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[ProvisionedThroughputOverrideTypeDef],
        "GlobalSecondaryIndexes": NotRequired[List[ReplicaGlobalSecondaryIndexDescriptionTypeDef]],
        "ReplicaInaccessibleDateTime": NotRequired[datetime],
        "ReplicaTableClassSummary": NotRequired[TableClassSummaryTypeDef],
    },
)
CreateReplicationGroupMemberActionTypeDef = TypedDict(
    "CreateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
        "KMSMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[ProvisionedThroughputOverrideTypeDef],
        "GlobalSecondaryIndexes": NotRequired[Sequence[ReplicaGlobalSecondaryIndexTypeDef]],
        "TableClassOverride": NotRequired[TableClassType],
    },
)
UpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "UpdateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
        "KMSMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[ProvisionedThroughputOverrideTypeDef],
        "GlobalSecondaryIndexes": NotRequired[Sequence[ReplicaGlobalSecondaryIndexTypeDef]],
        "TableClassOverride": NotRequired[TableClassType],
    },
)
UpdateGlobalTableInputRequestTypeDef = TypedDict(
    "UpdateGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaUpdates": Sequence[ReplicaUpdateTypeDef],
    },
)
DescribeExportOutputTypeDef = TypedDict(
    "DescribeExportOutputTypeDef",
    {
        "ExportDescription": ExportDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportTableToPointInTimeOutputTypeDef = TypedDict(
    "ExportTableToPointInTimeOutputTypeDef",
    {
        "ExportDescription": ExportDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListImportsOutputTypeDef = TypedDict(
    "ListImportsOutputTypeDef",
    {
        "ImportSummaryList": List[ImportSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchExecuteStatementOutputTypeDef = TypedDict(
    "BatchExecuteStatementOutputTypeDef",
    {
        "Responses": List[BatchStatementResponseTypeDef],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchExecuteStatementInputRequestTypeDef = TypedDict(
    "BatchExecuteStatementInputRequestTypeDef",
    {
        "Statements": Sequence[BatchStatementRequestTypeDef],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
    },
)
QueryInputQueryPaginateTypeDef = TypedDict(
    "QueryInputQueryPaginateTypeDef",
    {
        "TableName": str,
        "IndexName": NotRequired[str],
        "Select": NotRequired[SelectType],
        "AttributesToGet": NotRequired[Sequence[str]],
        "ConsistentRead": NotRequired[bool],
        "KeyConditions": NotRequired[Mapping[str, ConditionTypeDef]],
        "QueryFilter": NotRequired[Mapping[str, ConditionTypeDef]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ScanIndexForward": NotRequired[bool],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ProjectionExpression": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "KeyConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
QueryInputRequestTypeDef = TypedDict(
    "QueryInputRequestTypeDef",
    {
        "TableName": str,
        "IndexName": NotRequired[str],
        "Select": NotRequired[SelectType],
        "AttributesToGet": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "ConsistentRead": NotRequired[bool],
        "KeyConditions": NotRequired[Mapping[str, ConditionTypeDef]],
        "QueryFilter": NotRequired[Mapping[str, ConditionTypeDef]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ScanIndexForward": NotRequired[bool],
        "ExclusiveStartKey": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ProjectionExpression": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "KeyConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
    },
)
ScanInputRequestTypeDef = TypedDict(
    "ScanInputRequestTypeDef",
    {
        "TableName": str,
        "IndexName": NotRequired[str],
        "AttributesToGet": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "Select": NotRequired[SelectType],
        "ScanFilter": NotRequired[Mapping[str, ConditionTypeDef]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ExclusiveStartKey": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "TotalSegments": NotRequired[int],
        "Segment": NotRequired[int],
        "ProjectionExpression": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "ConsistentRead": NotRequired[bool],
    },
)
ScanInputScanPaginateTypeDef = TypedDict(
    "ScanInputScanPaginateTypeDef",
    {
        "TableName": str,
        "IndexName": NotRequired[str],
        "AttributesToGet": NotRequired[Sequence[str]],
        "Select": NotRequired[SelectType],
        "ScanFilter": NotRequired[Mapping[str, ConditionTypeDef]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "TotalSegments": NotRequired[int],
        "Segment": NotRequired[int],
        "ProjectionExpression": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "ConsistentRead": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DeleteItemInputRequestTypeDef = TypedDict(
    "DeleteItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[str, UniversalAttributeValueTypeDef],
        "Expected": NotRequired[Mapping[str, ExpectedAttributeValueTypeDef]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
PutItemInputRequestTypeDef = TypedDict(
    "PutItemInputRequestTypeDef",
    {
        "TableName": str,
        "Item": Mapping[str, UniversalAttributeValueTypeDef],
        "Expected": NotRequired[Mapping[str, ExpectedAttributeValueTypeDef]],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
UpdateItemInputRequestTypeDef = TypedDict(
    "UpdateItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[str, UniversalAttributeValueTypeDef],
        "AttributeUpdates": NotRequired[Mapping[str, AttributeValueUpdateTypeDef]],
        "Expected": NotRequired[Mapping[str, ExpectedAttributeValueTypeDef]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "UpdateExpression": NotRequired[str],
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[Mapping[str, UniversalAttributeValueTypeDef]],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)
TransactGetItemTypeDef = TypedDict(
    "TransactGetItemTypeDef",
    {
        "Get": GetTypeDef,
    },
)
BatchGetItemInputRequestTypeDef = TypedDict(
    "BatchGetItemInputRequestTypeDef",
    {
        "RequestItems": Mapping[str, KeysAndAttributesTypeDef],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
    },
)
BatchGetItemOutputTypeDef = TypedDict(
    "BatchGetItemOutputTypeDef",
    {
        "Responses": Dict[str, List[Dict[str, AttributeValueTypeDef]]],
        "UnprocessedKeys": Dict[str, KeysAndAttributesTypeDef],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecuteTransactionInputRequestTypeDef = TypedDict(
    "ExecuteTransactionInputRequestTypeDef",
    {
        "TransactStatements": Sequence[ParameterizedStatementTypeDef],
        "ClientRequestToken": NotRequired[str],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
    },
)
WriteRequestTypeDef = TypedDict(
    "WriteRequestTypeDef",
    {
        "PutRequest": NotRequired[PutRequestTypeDef],
        "DeleteRequest": NotRequired[DeleteRequestTypeDef],
    },
)
TransactWriteItemTypeDef = TypedDict(
    "TransactWriteItemTypeDef",
    {
        "ConditionCheck": NotRequired[ConditionCheckTypeDef],
        "Put": NotRequired[PutTypeDef],
        "Delete": NotRequired[DeleteTypeDef],
        "Update": NotRequired[UpdateTypeDef],
    },
)
BatchWriteItemInputServiceResourceBatchWriteItemTypeDef = TypedDict(
    "BatchWriteItemInputServiceResourceBatchWriteItemTypeDef",
    {
        "RequestItems": Mapping[str, Sequence[WriteRequestServiceResourceTypeDef]],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
    },
)
BatchWriteItemOutputServiceResourceTypeDef = TypedDict(
    "BatchWriteItemOutputServiceResourceTypeDef",
    {
        "UnprocessedItems": Dict[str, List[WriteRequestServiceResourceTypeDef]],
        "ItemCollectionMetrics": Dict[str, List[ItemCollectionMetricsServiceResourceTypeDef]],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    {
        "IndexName": NotRequired[str],
        "IndexStatus": NotRequired[IndexStatusType],
        "ProvisionedReadCapacityAutoScalingSettings": NotRequired[
            AutoScalingSettingsDescriptionTypeDef
        ],
        "ProvisionedWriteCapacityAutoScalingSettings": NotRequired[
            AutoScalingSettingsDescriptionTypeDef
        ],
    },
)
ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    {
        "IndexName": str,
        "IndexStatus": NotRequired[IndexStatusType],
        "ProvisionedReadCapacityUnits": NotRequired[int],
        "ProvisionedReadCapacityAutoScalingSettings": NotRequired[
            AutoScalingSettingsDescriptionTypeDef
        ],
        "ProvisionedWriteCapacityUnits": NotRequired[int],
        "ProvisionedWriteCapacityAutoScalingSettings": NotRequired[
            AutoScalingSettingsDescriptionTypeDef
        ],
    },
)
GlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": NotRequired[str],
        "ProvisionedWriteCapacityAutoScalingUpdate": NotRequired[AutoScalingSettingsUpdateTypeDef],
    },
)
GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedWriteCapacityUnits": NotRequired[int],
        "ProvisionedWriteCapacityAutoScalingSettingsUpdate": NotRequired[
            AutoScalingSettingsUpdateTypeDef
        ],
    },
)
ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": NotRequired[str],
        "ProvisionedReadCapacityAutoScalingUpdate": NotRequired[AutoScalingSettingsUpdateTypeDef],
    },
)
ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedReadCapacityUnits": NotRequired[int],
        "ProvisionedReadCapacityAutoScalingSettingsUpdate": NotRequired[
            AutoScalingSettingsUpdateTypeDef
        ],
    },
)
ImportTableDescriptionTypeDef = TypedDict(
    "ImportTableDescriptionTypeDef",
    {
        "ImportArn": NotRequired[str],
        "ImportStatus": NotRequired[ImportStatusType],
        "TableArn": NotRequired[str],
        "TableId": NotRequired[str],
        "ClientToken": NotRequired[str],
        "S3BucketSource": NotRequired[S3BucketSourceTypeDef],
        "ErrorCount": NotRequired[int],
        "CloudWatchLogGroupArn": NotRequired[str],
        "InputFormat": NotRequired[InputFormatType],
        "InputFormatOptions": NotRequired[InputFormatOptionsTypeDef],
        "InputCompressionType": NotRequired[InputCompressionTypeType],
        "TableCreationParameters": NotRequired[TableCreationParametersTypeDef],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "ProcessedSizeBytes": NotRequired[int],
        "ProcessedItemCount": NotRequired[int],
        "ImportedItemCount": NotRequired[int],
        "FailureCode": NotRequired[str],
        "FailureMessage": NotRequired[str],
    },
)
ImportTableInputRequestTypeDef = TypedDict(
    "ImportTableInputRequestTypeDef",
    {
        "S3BucketSource": S3BucketSourceTypeDef,
        "InputFormat": InputFormatType,
        "TableCreationParameters": TableCreationParametersTypeDef,
        "ClientToken": NotRequired[str],
        "InputFormatOptions": NotRequired[InputFormatOptionsTypeDef],
        "InputCompressionType": NotRequired[InputCompressionTypeType],
    },
)
BackupDescriptionTypeDef = TypedDict(
    "BackupDescriptionTypeDef",
    {
        "BackupDetails": NotRequired[BackupDetailsTypeDef],
        "SourceTableDetails": NotRequired[SourceTableDetailsTypeDef],
        "SourceTableFeatureDetails": NotRequired[SourceTableFeatureDetailsTypeDef],
    },
)
GlobalTableDescriptionTypeDef = TypedDict(
    "GlobalTableDescriptionTypeDef",
    {
        "ReplicationGroup": NotRequired[List[ReplicaDescriptionTypeDef]],
        "GlobalTableArn": NotRequired[str],
        "CreationDateTime": NotRequired[datetime],
        "GlobalTableStatus": NotRequired[GlobalTableStatusType],
        "GlobalTableName": NotRequired[str],
    },
)
TableDescriptionTableTypeDef = TypedDict(
    "TableDescriptionTableTypeDef",
    {
        "AttributeDefinitions": NotRequired[List[AttributeDefinitionTypeDef]],
        "TableName": NotRequired[str],
        "KeySchema": NotRequired[List[KeySchemaElementTypeDef]],
        "TableStatus": NotRequired[TableStatusType],
        "CreationDateTime": NotRequired[datetime],
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputDescriptionTypeDef],
        "TableSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "TableArn": NotRequired[str],
        "TableId": NotRequired[str],
        "BillingModeSummary": NotRequired[BillingModeSummaryTypeDef],
        "LocalSecondaryIndexes": NotRequired[List[LocalSecondaryIndexDescriptionTableTypeDef]],
        "GlobalSecondaryIndexes": NotRequired[List[GlobalSecondaryIndexDescriptionTableTypeDef]],
        "StreamSpecification": NotRequired[StreamSpecificationTypeDef],
        "LatestStreamLabel": NotRequired[str],
        "LatestStreamArn": NotRequired[str],
        "GlobalTableVersion": NotRequired[str],
        "Replicas": NotRequired[List[ReplicaDescriptionTypeDef]],
        "RestoreSummary": NotRequired[RestoreSummaryTypeDef],
        "SSEDescription": NotRequired[SSEDescriptionTypeDef],
        "ArchivalSummary": NotRequired[ArchivalSummaryTypeDef],
        "TableClassSummary": NotRequired[TableClassSummaryTypeDef],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
TableDescriptionTypeDef = TypedDict(
    "TableDescriptionTypeDef",
    {
        "AttributeDefinitions": NotRequired[List[AttributeDefinitionTypeDef]],
        "TableName": NotRequired[str],
        "KeySchema": NotRequired[List[KeySchemaElementTypeDef]],
        "TableStatus": NotRequired[TableStatusType],
        "CreationDateTime": NotRequired[datetime],
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputDescriptionTypeDef],
        "TableSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "TableArn": NotRequired[str],
        "TableId": NotRequired[str],
        "BillingModeSummary": NotRequired[BillingModeSummaryTypeDef],
        "LocalSecondaryIndexes": NotRequired[List[LocalSecondaryIndexDescriptionTypeDef]],
        "GlobalSecondaryIndexes": NotRequired[List[GlobalSecondaryIndexDescriptionTypeDef]],
        "StreamSpecification": NotRequired[StreamSpecificationTypeDef],
        "LatestStreamLabel": NotRequired[str],
        "LatestStreamArn": NotRequired[str],
        "GlobalTableVersion": NotRequired[str],
        "Replicas": NotRequired[List[ReplicaDescriptionTypeDef]],
        "RestoreSummary": NotRequired[RestoreSummaryTypeDef],
        "SSEDescription": NotRequired[SSEDescriptionTypeDef],
        "ArchivalSummary": NotRequired[ArchivalSummaryTypeDef],
        "TableClassSummary": NotRequired[TableClassSummaryTypeDef],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
ReplicationGroupUpdateTypeDef = TypedDict(
    "ReplicationGroupUpdateTypeDef",
    {
        "Create": NotRequired[CreateReplicationGroupMemberActionTypeDef],
        "Update": NotRequired[UpdateReplicationGroupMemberActionTypeDef],
        "Delete": NotRequired[DeleteReplicationGroupMemberActionTypeDef],
    },
)
TransactGetItemsInputRequestTypeDef = TypedDict(
    "TransactGetItemsInputRequestTypeDef",
    {
        "TransactItems": Sequence[TransactGetItemTypeDef],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
    },
)
BatchWriteItemInputRequestTypeDef = TypedDict(
    "BatchWriteItemInputRequestTypeDef",
    {
        "RequestItems": Mapping[str, Sequence[WriteRequestTypeDef]],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
    },
)
BatchWriteItemOutputTypeDef = TypedDict(
    "BatchWriteItemOutputTypeDef",
    {
        "UnprocessedItems": Dict[str, List[WriteRequestTypeDef]],
        "ItemCollectionMetrics": Dict[str, List[ItemCollectionMetricsTypeDef]],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TransactWriteItemsInputRequestTypeDef = TypedDict(
    "TransactWriteItemsInputRequestTypeDef",
    {
        "TransactItems": Sequence[TransactWriteItemTypeDef],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "ClientRequestToken": NotRequired[str],
    },
)
ReplicaAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaAutoScalingDescriptionTypeDef",
    {
        "RegionName": NotRequired[str],
        "GlobalSecondaryIndexes": NotRequired[
            List[ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef]
        ],
        "ReplicaProvisionedReadCapacityAutoScalingSettings": NotRequired[
            AutoScalingSettingsDescriptionTypeDef
        ],
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": NotRequired[
            AutoScalingSettingsDescriptionTypeDef
        ],
        "ReplicaStatus": NotRequired[ReplicaStatusType],
    },
)
ReplicaSettingsDescriptionTypeDef = TypedDict(
    "ReplicaSettingsDescriptionTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": NotRequired[ReplicaStatusType],
        "ReplicaBillingModeSummary": NotRequired[BillingModeSummaryTypeDef],
        "ReplicaProvisionedReadCapacityUnits": NotRequired[int],
        "ReplicaProvisionedReadCapacityAutoScalingSettings": NotRequired[
            AutoScalingSettingsDescriptionTypeDef
        ],
        "ReplicaProvisionedWriteCapacityUnits": NotRequired[int],
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": NotRequired[
            AutoScalingSettingsDescriptionTypeDef
        ],
        "ReplicaGlobalSecondaryIndexSettings": NotRequired[
            List[ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef]
        ],
        "ReplicaTableClassSummary": NotRequired[TableClassSummaryTypeDef],
    },
)
ReplicaAutoScalingUpdateTypeDef = TypedDict(
    "ReplicaAutoScalingUpdateTypeDef",
    {
        "RegionName": str,
        "ReplicaGlobalSecondaryIndexUpdates": NotRequired[
            Sequence[ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef]
        ],
        "ReplicaProvisionedReadCapacityAutoScalingUpdate": NotRequired[
            AutoScalingSettingsUpdateTypeDef
        ],
    },
)
ReplicaSettingsUpdateTypeDef = TypedDict(
    "ReplicaSettingsUpdateTypeDef",
    {
        "RegionName": str,
        "ReplicaProvisionedReadCapacityUnits": NotRequired[int],
        "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate": NotRequired[
            AutoScalingSettingsUpdateTypeDef
        ],
        "ReplicaGlobalSecondaryIndexSettingsUpdate": NotRequired[
            Sequence[ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef]
        ],
        "ReplicaTableClass": NotRequired[TableClassType],
    },
)
DescribeImportOutputTypeDef = TypedDict(
    "DescribeImportOutputTypeDef",
    {
        "ImportTableDescription": ImportTableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportTableOutputTypeDef = TypedDict(
    "ImportTableOutputTypeDef",
    {
        "ImportTableDescription": ImportTableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBackupOutputTypeDef = TypedDict(
    "DeleteBackupOutputTypeDef",
    {
        "BackupDescription": BackupDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBackupOutputTypeDef = TypedDict(
    "DescribeBackupOutputTypeDef",
    {
        "BackupDescription": BackupDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGlobalTableOutputTypeDef = TypedDict(
    "CreateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": GlobalTableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGlobalTableOutputTypeDef = TypedDict(
    "DescribeGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": GlobalTableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGlobalTableOutputTypeDef = TypedDict(
    "UpdateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": GlobalTableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTableOutputTableTypeDef = TypedDict(
    "DeleteTableOutputTableTypeDef",
    {
        "TableDescription": TableDescriptionTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTableOutputTypeDef = TypedDict(
    "CreateTableOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTableOutputTypeDef = TypedDict(
    "DeleteTableOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTableOutputTypeDef = TypedDict(
    "DescribeTableOutputTypeDef",
    {
        "Table": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreTableFromBackupOutputTypeDef = TypedDict(
    "RestoreTableFromBackupOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreTableToPointInTimeOutputTypeDef = TypedDict(
    "RestoreTableToPointInTimeOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTableOutputTypeDef = TypedDict(
    "UpdateTableOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTableInputRequestTypeDef = TypedDict(
    "UpdateTableInputRequestTypeDef",
    {
        "TableName": str,
        "AttributeDefinitions": NotRequired[Sequence[AttributeDefinitionTypeDef]],
        "BillingMode": NotRequired[BillingModeType],
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputTypeDef],
        "GlobalSecondaryIndexUpdates": NotRequired[Sequence[GlobalSecondaryIndexUpdateTypeDef]],
        "StreamSpecification": NotRequired[StreamSpecificationTypeDef],
        "SSESpecification": NotRequired[SSESpecificationTypeDef],
        "ReplicaUpdates": NotRequired[Sequence[ReplicationGroupUpdateTypeDef]],
        "TableClass": NotRequired[TableClassType],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
UpdateTableInputTableUpdateTypeDef = TypedDict(
    "UpdateTableInputTableUpdateTypeDef",
    {
        "AttributeDefinitions": NotRequired[Sequence[AttributeDefinitionTypeDef]],
        "BillingMode": NotRequired[BillingModeType],
        "ProvisionedThroughput": NotRequired[ProvisionedThroughputTypeDef],
        "GlobalSecondaryIndexUpdates": NotRequired[
            Sequence[GlobalSecondaryIndexUpdateTableTypeDef]
        ],
        "StreamSpecification": NotRequired[StreamSpecificationTypeDef],
        "SSESpecification": NotRequired[SSESpecificationTypeDef],
        "ReplicaUpdates": NotRequired[Sequence[ReplicationGroupUpdateTypeDef]],
        "TableClass": NotRequired[TableClassType],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
TableAutoScalingDescriptionTypeDef = TypedDict(
    "TableAutoScalingDescriptionTypeDef",
    {
        "TableName": NotRequired[str],
        "TableStatus": NotRequired[TableStatusType],
        "Replicas": NotRequired[List[ReplicaAutoScalingDescriptionTypeDef]],
    },
)
DescribeGlobalTableSettingsOutputTypeDef = TypedDict(
    "DescribeGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List[ReplicaSettingsDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGlobalTableSettingsOutputTypeDef = TypedDict(
    "UpdateGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List[ReplicaSettingsDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "UpdateTableReplicaAutoScalingInputRequestTypeDef",
    {
        "TableName": str,
        "GlobalSecondaryIndexUpdates": NotRequired[
            Sequence[GlobalSecondaryIndexAutoScalingUpdateTypeDef]
        ],
        "ProvisionedWriteCapacityAutoScalingUpdate": NotRequired[AutoScalingSettingsUpdateTypeDef],
        "ReplicaUpdates": NotRequired[Sequence[ReplicaAutoScalingUpdateTypeDef]],
    },
)
UpdateGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "UpdateGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "GlobalTableBillingMode": NotRequired[BillingModeType],
        "GlobalTableProvisionedWriteCapacityUnits": NotRequired[int],
        "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate": NotRequired[
            AutoScalingSettingsUpdateTypeDef
        ],
        "GlobalTableGlobalSecondaryIndexSettingsUpdate": NotRequired[
            Sequence[GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef]
        ],
        "ReplicaSettingsUpdate": NotRequired[Sequence[ReplicaSettingsUpdateTypeDef]],
    },
)
DescribeTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": TableAutoScalingDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "UpdateTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": TableAutoScalingDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
