"""
Type annotations for rds service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/type_defs/)

Usage::

    ```python
    from mypy_boto3_rds.type_defs import AccountQuotaTypeDef

    data: AccountQuotaTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Optional, Sequence, Union

from .literals import (
    ActivityStreamModeType,
    ActivityStreamPolicyStatusType,
    ActivityStreamStatusType,
    ApplyMethodType,
    AuditPolicyStateType,
    AutomationModeType,
    ClientPasswordAuthTypeType,
    CustomEngineVersionStatusType,
    DBProxyEndpointStatusType,
    DBProxyEndpointTargetRoleType,
    DBProxyStatusType,
    EngineFamilyType,
    ExportSourceTypeType,
    FailoverStatusType,
    GlobalClusterMemberSynchronizationStatusType,
    IAMAuthModeType,
    IntegrationStatusType,
    LocalWriteForwardingStatusType,
    ReplicaModeType,
    SourceTypeType,
    TargetHealthReasonType,
    TargetRoleType,
    TargetStateType,
    TargetTypeType,
    WriteForwardingStatusType,
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
    "AccountQuotaTypeDef",
    "ResponseMetadataTypeDef",
    "AddRoleToDBClusterMessageRequestTypeDef",
    "AddRoleToDBInstanceMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    "EventSubscriptionTypeDef",
    "TagTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "AuthorizeDBSecurityGroupIngressMessageRequestTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableProcessorFeatureTypeDef",
    "TimestampTypeDef",
    "BlueGreenDeploymentTaskTypeDef",
    "SwitchoverDetailTypeDef",
    "CancelExportTaskMessageRequestTypeDef",
    "CertificateDetailsTypeDef",
    "CertificateTypeDef",
    "CharacterSetTypeDef",
    "ClientGenerateDbAuthTokenRequestTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "RdsCustomClusterConfigurationTypeDef",
    "ConnectionPoolConfigurationInfoTypeDef",
    "ConnectionPoolConfigurationTypeDef",
    "ContextAttributeTypeDef",
    "DBClusterParameterGroupTypeDef",
    "DBParameterGroupTypeDef",
    "ScalingConfigurationTypeDef",
    "ServerlessV2ScalingConfigurationTypeDef",
    "ProcessorFeatureTypeDef",
    "DBProxyEndpointTypeDef",
    "UserAuthConfigTypeDef",
    "CreateGlobalClusterMessageRequestTypeDef",
    "CustomDBEngineVersionAMITypeDef",
    "RestoreWindowTypeDef",
    "DBClusterBacktrackTypeDef",
    "DBClusterEndpointTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterOptionGroupStatusTypeDef",
    "ParameterTypeDef",
    "DBClusterRoleTypeDef",
    "DBClusterSnapshotAttributeTypeDef",
    "DBClusterStatusInfoTypeDef",
    "DomainMembershipTypeDef",
    "MasterUserSecretTypeDef",
    "ScalingConfigurationInfoTypeDef",
    "ServerlessV2ScalingConfigurationInfoTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "DBInstanceAutomatedBackupsReplicationTypeDef",
    "DBInstanceRoleTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "EndpointTypeDef",
    "OptionGroupMembershipTypeDef",
    "TargetHealthTypeDef",
    "UserAuthConfigInfoTypeDef",
    "DocLinkTypeDef",
    "EC2SecurityGroupTypeDef",
    "IPRangeTypeDef",
    "DBSnapshotAttributeTypeDef",
    "DeleteBlueGreenDeploymentRequestRequestTypeDef",
    "DeleteCustomDBEngineVersionMessageRequestTypeDef",
    "DeleteDBClusterAutomatedBackupMessageRequestTypeDef",
    "DeleteDBClusterEndpointMessageRequestTypeDef",
    "DeleteDBClusterMessageRequestTypeDef",
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    "DeleteDBInstanceAutomatedBackupMessageRequestTypeDef",
    "DeleteDBInstanceMessageRequestTypeDef",
    "DeleteDBParameterGroupMessageRequestTypeDef",
    "DeleteDBProxyEndpointRequestRequestTypeDef",
    "DeleteDBProxyRequestRequestTypeDef",
    "DeleteDBSecurityGroupMessageRequestTypeDef",
    "DeleteDBSnapshotMessageRequestTypeDef",
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteGlobalClusterMessageRequestTypeDef",
    "DeleteIntegrationMessageRequestTypeDef",
    "DeleteOptionGroupMessageRequestTypeDef",
    "DeleteTenantDatabaseMessageRequestTypeDef",
    "DeregisterDBProxyTargetsRequestRequestTypeDef",
    "FilterTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeDBLogFilesDetailsTypeDef",
    "DescribeDBSnapshotAttributesMessageRequestTypeDef",
    "DescribeValidDBInstanceModificationsMessageRequestTypeDef",
    "DisableHttpEndpointRequestRequestTypeDef",
    "DoubleRangeTypeDef",
    "DownloadDBLogFilePortionMessageRequestTypeDef",
    "EnableHttpEndpointRequestRequestTypeDef",
    "EventCategoriesMapTypeDef",
    "EventTypeDef",
    "ExportTaskTypeDef",
    "FailoverDBClusterMessageRequestTypeDef",
    "FailoverGlobalClusterMessageRequestTypeDef",
    "FailoverStateTypeDef",
    "GlobalClusterMemberTypeDef",
    "IntegrationErrorTypeDef",
    "MinimumEngineVersionPerAllowedValueTypeDef",
    "ModifyActivityStreamRequestRequestTypeDef",
    "ModifyCertificatesMessageRequestTypeDef",
    "ModifyCurrentDBClusterCapacityMessageRequestTypeDef",
    "ModifyCustomDBEngineVersionMessageRequestTypeDef",
    "ModifyDBClusterEndpointMessageRequestTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    "ModifyDBProxyEndpointRequestRequestTypeDef",
    "RecommendedActionUpdateTypeDef",
    "ModifyDBSnapshotAttributeMessageRequestTypeDef",
    "ModifyDBSnapshotMessageRequestTypeDef",
    "ModifyDBSubnetGroupMessageRequestTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyGlobalClusterMessageRequestTypeDef",
    "ModifyTenantDatabaseMessageRequestTypeDef",
    "OptionSettingTypeDef",
    "OptionVersionTypeDef",
    "OutpostTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    "PromoteReadReplicaDBClusterMessageRequestTypeDef",
    "PromoteReadReplicaMessageRequestTypeDef",
    "RangeTypeDef",
    "RebootDBClusterMessageRequestTypeDef",
    "RebootDBInstanceMessageRequestTypeDef",
    "RecommendedActionParameterTypeDef",
    "RecurringChargeTypeDef",
    "ScalarReferenceDetailsTypeDef",
    "RegisterDBProxyTargetsRequestRequestTypeDef",
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    "RemoveRoleFromDBClusterMessageRequestTypeDef",
    "RemoveRoleFromDBInstanceMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "RevokeDBSecurityGroupIngressMessageRequestTypeDef",
    "SourceRegionTypeDef",
    "StartActivityStreamRequestRequestTypeDef",
    "StartDBClusterMessageRequestTypeDef",
    "StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    "StartDBInstanceMessageRequestTypeDef",
    "StartExportTaskMessageRequestTypeDef",
    "StopActivityStreamRequestRequestTypeDef",
    "StopDBClusterMessageRequestTypeDef",
    "StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    "StopDBInstanceMessageRequestTypeDef",
    "SwitchoverBlueGreenDeploymentRequestRequestTypeDef",
    "SwitchoverGlobalClusterMessageRequestTypeDef",
    "SwitchoverReadReplicaMessageRequestTypeDef",
    "TenantDatabasePendingModifiedValuesTypeDef",
    "AccountAttributesMessageTypeDef",
    "DBClusterBacktrackResponseTypeDef",
    "DBClusterCapacityInfoTypeDef",
    "DBClusterEndpointResponseTypeDef",
    "DBClusterParameterGroupNameMessageTypeDef",
    "DBParameterGroupNameMessageTypeDef",
    "DisableHttpEndpointResponseTypeDef",
    "DownloadDBLogFilePortionDetailsTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableHttpEndpointResponseTypeDef",
    "ExportTaskResponseTypeDef",
    "ModifyActivityStreamResponseTypeDef",
    "StartActivityStreamResponseTypeDef",
    "StopActivityStreamResponseTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "CopyDBClusterParameterGroupMessageRequestTypeDef",
    "CopyDBClusterSnapshotMessageRequestTypeDef",
    "CopyDBParameterGroupMessageRequestTypeDef",
    "CopyDBSnapshotMessageRequestTypeDef",
    "CopyOptionGroupMessageRequestTypeDef",
    "CreateBlueGreenDeploymentRequestRequestTypeDef",
    "CreateCustomDBEngineVersionMessageRequestTypeDef",
    "CreateDBClusterEndpointMessageRequestTypeDef",
    "CreateDBClusterParameterGroupMessageRequestTypeDef",
    "CreateDBClusterSnapshotMessageRequestTypeDef",
    "CreateDBParameterGroupMessageRequestTypeDef",
    "CreateDBProxyEndpointRequestRequestTypeDef",
    "CreateDBSecurityGroupMessageRequestTypeDef",
    "CreateDBSnapshotMessageRequestTypeDef",
    "CreateDBSubnetGroupMessageRequestTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateIntegrationMessageRequestTypeDef",
    "CreateOptionGroupMessageRequestTypeDef",
    "CreateTenantDatabaseMessageRequestTypeDef",
    "DBClusterSnapshotTypeDef",
    "DBSnapshotTenantDatabaseTypeDef",
    "PurchaseReservedDBInstancesOfferingMessageRequestTypeDef",
    "TagListMessageTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "BacktrackDBClusterMessageRequestTypeDef",
    "BlueGreenDeploymentTypeDef",
    "CertificateMessageTypeDef",
    "ModifyCertificatesResultTypeDef",
    "ClusterPendingModifiedValuesTypeDef",
    "DBProxyTargetGroupTypeDef",
    "ModifyDBProxyTargetGroupRequestRequestTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "DBClusterParameterGroupsMessageTypeDef",
    "CopyDBParameterGroupResultTypeDef",
    "CreateDBParameterGroupResultTypeDef",
    "DBParameterGroupsMessageTypeDef",
    "CreateDBClusterMessageRequestTypeDef",
    "ModifyDBClusterMessageRequestTypeDef",
    "RestoreDBClusterFromS3MessageRequestTypeDef",
    "RestoreDBClusterFromSnapshotMessageRequestTypeDef",
    "RestoreDBClusterToPointInTimeMessageRequestTypeDef",
    "CreateDBInstanceMessageRequestTypeDef",
    "CreateDBInstanceReadReplicaMessageRequestTypeDef",
    "DBSnapshotTypeDef",
    "ModifyDBInstanceMessageRequestTypeDef",
    "PendingModifiedValuesTypeDef",
    "RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef",
    "RestoreDBInstanceFromS3MessageRequestTypeDef",
    "RestoreDBInstanceToPointInTimeMessageRequestTypeDef",
    "CreateDBProxyEndpointResponseTypeDef",
    "DeleteDBProxyEndpointResponseTypeDef",
    "DescribeDBProxyEndpointsResponseTypeDef",
    "ModifyDBProxyEndpointResponseTypeDef",
    "CreateDBProxyRequestRequestTypeDef",
    "ModifyDBProxyRequestRequestTypeDef",
    "DBClusterAutomatedBackupTypeDef",
    "DBClusterBacktrackMessageTypeDef",
    "DBClusterEndpointMessageTypeDef",
    "DBClusterParameterGroupDetailsTypeDef",
    "DBParameterGroupDetailsTypeDef",
    "EngineDefaultsTypeDef",
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    "ModifyDBParameterGroupMessageRequestTypeDef",
    "ResetDBClusterParameterGroupMessageRequestTypeDef",
    "ResetDBParameterGroupMessageRequestTypeDef",
    "DBClusterSnapshotAttributesResultTypeDef",
    "DBEngineVersionResponseTypeDef",
    "DBEngineVersionTypeDef",
    "DBInstanceAutomatedBackupTypeDef",
    "DBProxyTargetTypeDef",
    "DBProxyTypeDef",
    "DBSecurityGroupTypeDef",
    "DBSnapshotAttributesResultTypeDef",
    "DescribeBlueGreenDeploymentsRequestRequestTypeDef",
    "DescribeCertificatesMessageRequestTypeDef",
    "DescribeDBClusterAutomatedBackupsMessageRequestTypeDef",
    "DescribeDBClusterBacktracksMessageRequestTypeDef",
    "DescribeDBClusterEndpointsMessageRequestTypeDef",
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    "DescribeDBClusterParametersMessageRequestTypeDef",
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    "DescribeDBClustersMessageRequestTypeDef",
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    "DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef",
    "DescribeDBInstancesMessageRequestTypeDef",
    "DescribeDBLogFilesMessageRequestTypeDef",
    "DescribeDBParameterGroupsMessageRequestTypeDef",
    "DescribeDBParametersMessageRequestTypeDef",
    "DescribeDBProxiesRequestRequestTypeDef",
    "DescribeDBProxyEndpointsRequestRequestTypeDef",
    "DescribeDBProxyTargetGroupsRequestRequestTypeDef",
    "DescribeDBProxyTargetsRequestRequestTypeDef",
    "DescribeDBRecommendationsMessageRequestTypeDef",
    "DescribeDBSecurityGroupsMessageRequestTypeDef",
    "DescribeDBSnapshotTenantDatabasesMessageRequestTypeDef",
    "DescribeDBSnapshotsMessageRequestTypeDef",
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeExportTasksMessageRequestTypeDef",
    "DescribeGlobalClustersMessageRequestTypeDef",
    "DescribeIntegrationsMessageRequestTypeDef",
    "DescribeOptionGroupOptionsMessageRequestTypeDef",
    "DescribeOptionGroupsMessageRequestTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "DescribeReservedDBInstancesMessageRequestTypeDef",
    "DescribeReservedDBInstancesOfferingsMessageRequestTypeDef",
    "DescribeSourceRegionsMessageRequestTypeDef",
    "DescribeTenantDatabasesMessageRequestTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "DescribeBlueGreenDeploymentsRequestDescribeBlueGreenDeploymentsPaginateTypeDef",
    "DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef",
    "DescribeDBClusterAutomatedBackupsMessageDescribeDBClusterAutomatedBackupsPaginateTypeDef",
    "DescribeDBClusterBacktracksMessageDescribeDBClusterBacktracksPaginateTypeDef",
    "DescribeDBClusterEndpointsMessageDescribeDBClusterEndpointsPaginateTypeDef",
    "DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef",
    "DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateTypeDef",
    "DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef",
    "DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef",
    "DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef",
    "DescribeDBInstanceAutomatedBackupsMessageDescribeDBInstanceAutomatedBackupsPaginateTypeDef",
    "DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef",
    "DescribeDBLogFilesMessageDescribeDBLogFilesPaginateTypeDef",
    "DescribeDBParameterGroupsMessageDescribeDBParameterGroupsPaginateTypeDef",
    "DescribeDBParametersMessageDescribeDBParametersPaginateTypeDef",
    "DescribeDBProxiesRequestDescribeDBProxiesPaginateTypeDef",
    "DescribeDBProxyEndpointsRequestDescribeDBProxyEndpointsPaginateTypeDef",
    "DescribeDBProxyTargetGroupsRequestDescribeDBProxyTargetGroupsPaginateTypeDef",
    "DescribeDBProxyTargetsRequestDescribeDBProxyTargetsPaginateTypeDef",
    "DescribeDBRecommendationsMessageDescribeDBRecommendationsPaginateTypeDef",
    "DescribeDBSecurityGroupsMessageDescribeDBSecurityGroupsPaginateTypeDef",
    "DescribeDBSnapshotTenantDatabasesMessageDescribeDBSnapshotTenantDatabasesPaginateTypeDef",
    "DescribeDBSnapshotsMessageDescribeDBSnapshotsPaginateTypeDef",
    "DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef",
    "DescribeEngineDefaultClusterParametersMessageDescribeEngineDefaultClusterParametersPaginateTypeDef",
    "DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef",
    "DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef",
    "DescribeEventsMessageDescribeEventsPaginateTypeDef",
    "DescribeExportTasksMessageDescribeExportTasksPaginateTypeDef",
    "DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef",
    "DescribeIntegrationsMessageDescribeIntegrationsPaginateTypeDef",
    "DescribeOptionGroupOptionsMessageDescribeOptionGroupOptionsPaginateTypeDef",
    "DescribeOptionGroupsMessageDescribeOptionGroupsPaginateTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateTypeDef",
    "DescribePendingMaintenanceActionsMessageDescribePendingMaintenanceActionsPaginateTypeDef",
    "DescribeReservedDBInstancesMessageDescribeReservedDBInstancesPaginateTypeDef",
    "DescribeReservedDBInstancesOfferingsMessageDescribeReservedDBInstancesOfferingsPaginateTypeDef",
    "DescribeSourceRegionsMessageDescribeSourceRegionsPaginateTypeDef",
    "DescribeTenantDatabasesMessageDescribeTenantDatabasesPaginateTypeDef",
    "DownloadDBLogFilePortionMessageDownloadDBLogFilePortionPaginateTypeDef",
    "DescribeDBClusterSnapshotsMessageDBClusterSnapshotAvailableWaitTypeDef",
    "DescribeDBClusterSnapshotsMessageDBClusterSnapshotDeletedWaitTypeDef",
    "DescribeDBClustersMessageDBClusterAvailableWaitTypeDef",
    "DescribeDBClustersMessageDBClusterDeletedWaitTypeDef",
    "DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef",
    "DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef",
    "DescribeDBSnapshotsMessageDBSnapshotAvailableWaitTypeDef",
    "DescribeDBSnapshotsMessageDBSnapshotCompletedWaitTypeDef",
    "DescribeDBSnapshotsMessageDBSnapshotDeletedWaitTypeDef",
    "DescribeTenantDatabasesMessageTenantDatabaseAvailableWaitTypeDef",
    "DescribeTenantDatabasesMessageTenantDatabaseDeletedWaitTypeDef",
    "DescribeDBLogFilesResponseTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventsMessageTypeDef",
    "ExportTasksMessageTypeDef",
    "GlobalClusterTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "OptionGroupOptionSettingTypeDef",
    "ModifyDBRecommendationMessageRequestTypeDef",
    "OptionConfigurationTypeDef",
    "OptionTypeDef",
    "SubnetTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "PerformanceInsightsMetricQueryTypeDef",
    "ValidStorageOptionsTypeDef",
    "ReservedDBInstanceTypeDef",
    "ReservedDBInstancesOfferingTypeDef",
    "ReferenceDetailsTypeDef",
    "SourceRegionMessageTypeDef",
    "TenantDatabaseTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "DBClusterSnapshotMessageTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DBSnapshotTenantDatabasesMessageTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "CreateBlueGreenDeploymentResponseTypeDef",
    "DeleteBlueGreenDeploymentResponseTypeDef",
    "DescribeBlueGreenDeploymentsResponseTypeDef",
    "SwitchoverBlueGreenDeploymentResponseTypeDef",
    "DBClusterTypeDef",
    "DescribeDBProxyTargetGroupsResponseTypeDef",
    "ModifyDBProxyTargetGroupResponseTypeDef",
    "CopyDBSnapshotResultTypeDef",
    "CreateDBSnapshotResultTypeDef",
    "DBSnapshotMessageTypeDef",
    "DeleteDBSnapshotResultTypeDef",
    "ModifyDBSnapshotResultTypeDef",
    "DBClusterAutomatedBackupMessageTypeDef",
    "DeleteDBClusterAutomatedBackupResultTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "DBEngineVersionMessageTypeDef",
    "DBInstanceAutomatedBackupMessageTypeDef",
    "DeleteDBInstanceAutomatedBackupResultTypeDef",
    "StartDBInstanceAutomatedBackupsReplicationResultTypeDef",
    "StopDBInstanceAutomatedBackupsReplicationResultTypeDef",
    "DescribeDBProxyTargetsResponseTypeDef",
    "RegisterDBProxyTargetsResponseTypeDef",
    "CreateDBProxyResponseTypeDef",
    "DeleteDBProxyResponseTypeDef",
    "DescribeDBProxiesResponseTypeDef",
    "ModifyDBProxyResponseTypeDef",
    "AuthorizeDBSecurityGroupIngressResultTypeDef",
    "CreateDBSecurityGroupResultTypeDef",
    "DBSecurityGroupMessageTypeDef",
    "RevokeDBSecurityGroupIngressResultTypeDef",
    "DescribeDBSnapshotAttributesResultTypeDef",
    "ModifyDBSnapshotAttributeResultTypeDef",
    "CreateGlobalClusterResultTypeDef",
    "DeleteGlobalClusterResultTypeDef",
    "FailoverGlobalClusterResultTypeDef",
    "GlobalClustersMessageTypeDef",
    "ModifyGlobalClusterResultTypeDef",
    "RemoveFromGlobalClusterResultTypeDef",
    "SwitchoverGlobalClusterResultTypeDef",
    "DescribeIntegrationsResponseTypeDef",
    "OptionGroupOptionTypeDef",
    "ModifyOptionGroupMessageRequestTypeDef",
    "OptionGroupTypeDef",
    "DBSubnetGroupTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "MetricQueryTypeDef",
    "ValidDBInstanceModificationsMessageTypeDef",
    "PurchaseReservedDBInstancesOfferingResultTypeDef",
    "ReservedDBInstanceMessageTypeDef",
    "ReservedDBInstancesOfferingMessageTypeDef",
    "MetricReferenceTypeDef",
    "CreateTenantDatabaseResultTypeDef",
    "DeleteTenantDatabaseResultTypeDef",
    "ModifyTenantDatabaseResultTypeDef",
    "TenantDatabasesMessageTypeDef",
    "CreateDBClusterResultTypeDef",
    "DBClusterMessageTypeDef",
    "DeleteDBClusterResultTypeDef",
    "FailoverDBClusterResultTypeDef",
    "ModifyDBClusterResultTypeDef",
    "PromoteReadReplicaDBClusterResultTypeDef",
    "RebootDBClusterResultTypeDef",
    "RestoreDBClusterFromS3ResultTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "StartDBClusterResultTypeDef",
    "StopDBClusterResultTypeDef",
    "OptionGroupOptionsMessageTypeDef",
    "CopyOptionGroupResultTypeDef",
    "CreateOptionGroupResultTypeDef",
    "ModifyOptionGroupResultTypeDef",
    "OptionGroupsTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "DBInstanceTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "DescribeValidDBInstanceModificationsResultTypeDef",
    "MetricTypeDef",
    "CreateDBInstanceReadReplicaResultTypeDef",
    "CreateDBInstanceResultTypeDef",
    "DBInstanceMessageTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "PromoteReadReplicaResultTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RestoreDBInstanceFromDBSnapshotResultTypeDef",
    "RestoreDBInstanceFromS3ResultTypeDef",
    "RestoreDBInstanceToPointInTimeResultTypeDef",
    "StartDBInstanceResultTypeDef",
    "StopDBInstanceResultTypeDef",
    "SwitchoverReadReplicaResultTypeDef",
    "PerformanceIssueDetailsTypeDef",
    "IssueDetailsTypeDef",
    "RecommendedActionTypeDef",
    "DBRecommendationTypeDef",
    "DBRecommendationMessageTypeDef",
    "DBRecommendationsMessageTypeDef",
)

AccountQuotaTypeDef = TypedDict(
    "AccountQuotaTypeDef",
    {
        "AccountQuotaName": NotRequired[str],
        "Used": NotRequired[int],
        "Max": NotRequired[int],
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
AddRoleToDBClusterMessageRequestTypeDef = TypedDict(
    "AddRoleToDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "RoleArn": str,
        "FeatureName": NotRequired[str],
    },
)
AddRoleToDBInstanceMessageRequestTypeDef = TypedDict(
    "AddRoleToDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "RoleArn": str,
        "FeatureName": str,
    },
)
AddSourceIdentifierToSubscriptionMessageRequestTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)
EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": NotRequired[str],
        "CustSubscriptionId": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "Status": NotRequired[str],
        "SubscriptionCreationTime": NotRequired[str],
        "SourceType": NotRequired[str],
        "SourceIdsList": NotRequired[List[str]],
        "EventCategoriesList": NotRequired[List[str]],
        "Enabled": NotRequired[bool],
        "EventSubscriptionArn": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ApplyPendingMaintenanceActionMessageRequestTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ApplyAction": str,
        "OptInType": str,
    },
)
AuthorizeDBSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "AuthorizeDBSecurityGroupIngressMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
        "CIDRIP": NotRequired[str],
        "EC2SecurityGroupName": NotRequired[str],
        "EC2SecurityGroupId": NotRequired[str],
        "EC2SecurityGroupOwnerId": NotRequired[str],
    },
)
AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)
AvailableProcessorFeatureTypeDef = TypedDict(
    "AvailableProcessorFeatureTypeDef",
    {
        "Name": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "AllowedValues": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
BlueGreenDeploymentTaskTypeDef = TypedDict(
    "BlueGreenDeploymentTaskTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
    },
)
SwitchoverDetailTypeDef = TypedDict(
    "SwitchoverDetailTypeDef",
    {
        "SourceMember": NotRequired[str],
        "TargetMember": NotRequired[str],
        "Status": NotRequired[str],
    },
)
CancelExportTaskMessageRequestTypeDef = TypedDict(
    "CancelExportTaskMessageRequestTypeDef",
    {
        "ExportTaskIdentifier": str,
    },
)
CertificateDetailsTypeDef = TypedDict(
    "CertificateDetailsTypeDef",
    {
        "CAIdentifier": NotRequired[str],
        "ValidTill": NotRequired[datetime],
    },
)
CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "CertificateType": NotRequired[str],
        "Thumbprint": NotRequired[str],
        "ValidFrom": NotRequired[datetime],
        "ValidTill": NotRequired[datetime],
        "CertificateArn": NotRequired[str],
        "CustomerOverride": NotRequired[bool],
        "CustomerOverrideValidTill": NotRequired[datetime],
    },
)
CharacterSetTypeDef = TypedDict(
    "CharacterSetTypeDef",
    {
        "CharacterSetName": NotRequired[str],
        "CharacterSetDescription": NotRequired[str],
    },
)
ClientGenerateDbAuthTokenRequestTypeDef = TypedDict(
    "ClientGenerateDbAuthTokenRequestTypeDef",
    {
        "DBHostname": str,
        "Port": int,
        "DBUsername": str,
        "Region": NotRequired[Optional[str]],
    },
)
CloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "CloudwatchLogsExportConfigurationTypeDef",
    {
        "EnableLogTypes": NotRequired[Sequence[str]],
        "DisableLogTypes": NotRequired[Sequence[str]],
    },
)
PendingCloudwatchLogsExportsTypeDef = TypedDict(
    "PendingCloudwatchLogsExportsTypeDef",
    {
        "LogTypesToEnable": NotRequired[List[str]],
        "LogTypesToDisable": NotRequired[List[str]],
    },
)
RdsCustomClusterConfigurationTypeDef = TypedDict(
    "RdsCustomClusterConfigurationTypeDef",
    {
        "InterconnectSubnetId": NotRequired[str],
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "ReplicaMode": NotRequired[ReplicaModeType],
    },
)
ConnectionPoolConfigurationInfoTypeDef = TypedDict(
    "ConnectionPoolConfigurationInfoTypeDef",
    {
        "MaxConnectionsPercent": NotRequired[int],
        "MaxIdleConnectionsPercent": NotRequired[int],
        "ConnectionBorrowTimeout": NotRequired[int],
        "SessionPinningFilters": NotRequired[List[str]],
        "InitQuery": NotRequired[str],
    },
)
ConnectionPoolConfigurationTypeDef = TypedDict(
    "ConnectionPoolConfigurationTypeDef",
    {
        "MaxConnectionsPercent": NotRequired[int],
        "MaxIdleConnectionsPercent": NotRequired[int],
        "ConnectionBorrowTimeout": NotRequired[int],
        "SessionPinningFilters": NotRequired[Sequence[str]],
        "InitQuery": NotRequired[str],
    },
)
ContextAttributeTypeDef = TypedDict(
    "ContextAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
DBClusterParameterGroupTypeDef = TypedDict(
    "DBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "Description": NotRequired[str],
        "DBClusterParameterGroupArn": NotRequired[str],
    },
)
DBParameterGroupTypeDef = TypedDict(
    "DBParameterGroupTypeDef",
    {
        "DBParameterGroupName": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "Description": NotRequired[str],
        "DBParameterGroupArn": NotRequired[str],
    },
)
ScalingConfigurationTypeDef = TypedDict(
    "ScalingConfigurationTypeDef",
    {
        "MinCapacity": NotRequired[int],
        "MaxCapacity": NotRequired[int],
        "AutoPause": NotRequired[bool],
        "SecondsUntilAutoPause": NotRequired[int],
        "TimeoutAction": NotRequired[str],
        "SecondsBeforeTimeout": NotRequired[int],
    },
)
ServerlessV2ScalingConfigurationTypeDef = TypedDict(
    "ServerlessV2ScalingConfigurationTypeDef",
    {
        "MinCapacity": NotRequired[float],
        "MaxCapacity": NotRequired[float],
    },
)
ProcessorFeatureTypeDef = TypedDict(
    "ProcessorFeatureTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
DBProxyEndpointTypeDef = TypedDict(
    "DBProxyEndpointTypeDef",
    {
        "DBProxyEndpointName": NotRequired[str],
        "DBProxyEndpointArn": NotRequired[str],
        "DBProxyName": NotRequired[str],
        "Status": NotRequired[DBProxyEndpointStatusType],
        "VpcId": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[List[str]],
        "VpcSubnetIds": NotRequired[List[str]],
        "Endpoint": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "TargetRole": NotRequired[DBProxyEndpointTargetRoleType],
        "IsDefault": NotRequired[bool],
    },
)
UserAuthConfigTypeDef = TypedDict(
    "UserAuthConfigTypeDef",
    {
        "Description": NotRequired[str],
        "UserName": NotRequired[str],
        "AuthScheme": NotRequired[Literal["SECRETS"]],
        "SecretArn": NotRequired[str],
        "IAMAuth": NotRequired[IAMAuthModeType],
        "ClientPasswordAuthType": NotRequired[ClientPasswordAuthTypeType],
    },
)
CreateGlobalClusterMessageRequestTypeDef = TypedDict(
    "CreateGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "SourceDBClusterIdentifier": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "DatabaseName": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
    },
)
CustomDBEngineVersionAMITypeDef = TypedDict(
    "CustomDBEngineVersionAMITypeDef",
    {
        "ImageId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
RestoreWindowTypeDef = TypedDict(
    "RestoreWindowTypeDef",
    {
        "EarliestTime": NotRequired[datetime],
        "LatestTime": NotRequired[datetime],
    },
)
DBClusterBacktrackTypeDef = TypedDict(
    "DBClusterBacktrackTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "BacktrackIdentifier": NotRequired[str],
        "BacktrackTo": NotRequired[datetime],
        "BacktrackedFrom": NotRequired[datetime],
        "BacktrackRequestCreationTime": NotRequired[datetime],
        "Status": NotRequired[str],
    },
)
DBClusterEndpointTypeDef = TypedDict(
    "DBClusterEndpointTypeDef",
    {
        "DBClusterEndpointIdentifier": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterEndpointResourceIdentifier": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Status": NotRequired[str],
        "EndpointType": NotRequired[str],
        "CustomEndpointType": NotRequired[str],
        "StaticMembers": NotRequired[List[str]],
        "ExcludedMembers": NotRequired[List[str]],
        "DBClusterEndpointArn": NotRequired[str],
    },
)
DBClusterMemberTypeDef = TypedDict(
    "DBClusterMemberTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "IsClusterWriter": NotRequired[bool],
        "DBClusterParameterGroupStatus": NotRequired[str],
        "PromotionTier": NotRequired[int],
    },
)
DBClusterOptionGroupStatusTypeDef = TypedDict(
    "DBClusterOptionGroupStatusTypeDef",
    {
        "DBClusterOptionGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterValue": NotRequired[str],
        "Description": NotRequired[str],
        "Source": NotRequired[str],
        "ApplyType": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[bool],
        "MinimumEngineVersion": NotRequired[str],
        "ApplyMethod": NotRequired[ApplyMethodType],
        "SupportedEngineModes": NotRequired[List[str]],
    },
)
DBClusterRoleTypeDef = TypedDict(
    "DBClusterRoleTypeDef",
    {
        "RoleArn": NotRequired[str],
        "Status": NotRequired[str],
        "FeatureName": NotRequired[str],
    },
)
DBClusterSnapshotAttributeTypeDef = TypedDict(
    "DBClusterSnapshotAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[List[str]],
    },
)
DBClusterStatusInfoTypeDef = TypedDict(
    "DBClusterStatusInfoTypeDef",
    {
        "StatusType": NotRequired[str],
        "Normal": NotRequired[bool],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
    },
)
DomainMembershipTypeDef = TypedDict(
    "DomainMembershipTypeDef",
    {
        "Domain": NotRequired[str],
        "Status": NotRequired[str],
        "FQDN": NotRequired[str],
        "IAMRoleName": NotRequired[str],
        "OU": NotRequired[str],
        "AuthSecretArn": NotRequired[str],
        "DnsIps": NotRequired[List[str]],
    },
)
MasterUserSecretTypeDef = TypedDict(
    "MasterUserSecretTypeDef",
    {
        "SecretArn": NotRequired[str],
        "SecretStatus": NotRequired[str],
        "KmsKeyId": NotRequired[str],
    },
)
ScalingConfigurationInfoTypeDef = TypedDict(
    "ScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": NotRequired[int],
        "MaxCapacity": NotRequired[int],
        "AutoPause": NotRequired[bool],
        "SecondsUntilAutoPause": NotRequired[int],
        "TimeoutAction": NotRequired[str],
        "SecondsBeforeTimeout": NotRequired[int],
    },
)
ServerlessV2ScalingConfigurationInfoTypeDef = TypedDict(
    "ServerlessV2ScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": NotRequired[float],
        "MaxCapacity": NotRequired[float],
    },
)
VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "VpcSecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
TimezoneTypeDef = TypedDict(
    "TimezoneTypeDef",
    {
        "TimezoneName": NotRequired[str],
    },
)
UpgradeTargetTypeDef = TypedDict(
    "UpgradeTargetTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Description": NotRequired[str],
        "AutoUpgrade": NotRequired[bool],
        "IsMajorVersionUpgrade": NotRequired[bool],
        "SupportedEngineModes": NotRequired[List[str]],
        "SupportsParallelQuery": NotRequired[bool],
        "SupportsGlobalDatabases": NotRequired[bool],
        "SupportsBabelfish": NotRequired[bool],
        "SupportsLocalWriteForwarding": NotRequired[bool],
        "SupportsIntegrations": NotRequired[bool],
    },
)
DBInstanceAutomatedBackupsReplicationTypeDef = TypedDict(
    "DBInstanceAutomatedBackupsReplicationTypeDef",
    {
        "DBInstanceAutomatedBackupsArn": NotRequired[str],
    },
)
DBInstanceRoleTypeDef = TypedDict(
    "DBInstanceRoleTypeDef",
    {
        "RoleArn": NotRequired[str],
        "FeatureName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
DBInstanceStatusInfoTypeDef = TypedDict(
    "DBInstanceStatusInfoTypeDef",
    {
        "StatusType": NotRequired[str],
        "Normal": NotRequired[bool],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
    },
)
DBParameterGroupStatusTypeDef = TypedDict(
    "DBParameterGroupStatusTypeDef",
    {
        "DBParameterGroupName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
    },
)
DBSecurityGroupMembershipTypeDef = TypedDict(
    "DBSecurityGroupMembershipTypeDef",
    {
        "DBSecurityGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
        "HostedZoneId": NotRequired[str],
    },
)
OptionGroupMembershipTypeDef = TypedDict(
    "OptionGroupMembershipTypeDef",
    {
        "OptionGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
TargetHealthTypeDef = TypedDict(
    "TargetHealthTypeDef",
    {
        "State": NotRequired[TargetStateType],
        "Reason": NotRequired[TargetHealthReasonType],
        "Description": NotRequired[str],
    },
)
UserAuthConfigInfoTypeDef = TypedDict(
    "UserAuthConfigInfoTypeDef",
    {
        "Description": NotRequired[str],
        "UserName": NotRequired[str],
        "AuthScheme": NotRequired[Literal["SECRETS"]],
        "SecretArn": NotRequired[str],
        "IAMAuth": NotRequired[IAMAuthModeType],
        "ClientPasswordAuthType": NotRequired[ClientPasswordAuthTypeType],
    },
)
DocLinkTypeDef = TypedDict(
    "DocLinkTypeDef",
    {
        "Text": NotRequired[str],
        "Url": NotRequired[str],
    },
)
EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": NotRequired[str],
        "EC2SecurityGroupName": NotRequired[str],
        "EC2SecurityGroupId": NotRequired[str],
        "EC2SecurityGroupOwnerId": NotRequired[str],
    },
)
IPRangeTypeDef = TypedDict(
    "IPRangeTypeDef",
    {
        "Status": NotRequired[str],
        "CIDRIP": NotRequired[str],
    },
)
DBSnapshotAttributeTypeDef = TypedDict(
    "DBSnapshotAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[List[str]],
    },
)
DeleteBlueGreenDeploymentRequestRequestTypeDef = TypedDict(
    "DeleteBlueGreenDeploymentRequestRequestTypeDef",
    {
        "BlueGreenDeploymentIdentifier": str,
        "DeleteTarget": NotRequired[bool],
    },
)
DeleteCustomDBEngineVersionMessageRequestTypeDef = TypedDict(
    "DeleteCustomDBEngineVersionMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
    },
)
DeleteDBClusterAutomatedBackupMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterAutomatedBackupMessageRequestTypeDef",
    {
        "DbClusterResourceId": str,
    },
)
DeleteDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
    },
)
DeleteDBClusterMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "SkipFinalSnapshot": NotRequired[bool],
        "FinalDBSnapshotIdentifier": NotRequired[str],
        "DeleteAutomatedBackups": NotRequired[bool],
    },
)
DeleteDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)
DeleteDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)
DeleteDBInstanceAutomatedBackupMessageRequestTypeDef = TypedDict(
    "DeleteDBInstanceAutomatedBackupMessageRequestTypeDef",
    {
        "DbiResourceId": NotRequired[str],
        "DBInstanceAutomatedBackupsArn": NotRequired[str],
    },
)
DeleteDBInstanceMessageRequestTypeDef = TypedDict(
    "DeleteDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "SkipFinalSnapshot": NotRequired[bool],
        "FinalDBSnapshotIdentifier": NotRequired[str],
        "DeleteAutomatedBackups": NotRequired[bool],
    },
)
DeleteDBParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
    },
)
DeleteDBProxyEndpointRequestRequestTypeDef = TypedDict(
    "DeleteDBProxyEndpointRequestRequestTypeDef",
    {
        "DBProxyEndpointName": str,
    },
)
DeleteDBProxyRequestRequestTypeDef = TypedDict(
    "DeleteDBProxyRequestRequestTypeDef",
    {
        "DBProxyName": str,
    },
)
DeleteDBSecurityGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBSecurityGroupMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
    },
)
DeleteDBSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteDBSnapshotMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
)
DeleteDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
    },
)
DeleteEventSubscriptionMessageRequestTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)
DeleteGlobalClusterMessageRequestTypeDef = TypedDict(
    "DeleteGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
    },
)
DeleteIntegrationMessageRequestTypeDef = TypedDict(
    "DeleteIntegrationMessageRequestTypeDef",
    {
        "IntegrationIdentifier": str,
    },
)
DeleteOptionGroupMessageRequestTypeDef = TypedDict(
    "DeleteOptionGroupMessageRequestTypeDef",
    {
        "OptionGroupName": str,
    },
)
DeleteTenantDatabaseMessageRequestTypeDef = TypedDict(
    "DeleteTenantDatabaseMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "TenantDBName": str,
        "SkipFinalSnapshot": NotRequired[bool],
        "FinalDBSnapshotIdentifier": NotRequired[str],
    },
)
DeregisterDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "DeregisterDBProxyTargetsRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": NotRequired[str],
        "DBInstanceIdentifiers": NotRequired[Sequence[str]],
        "DBClusterIdentifiers": NotRequired[Sequence[str]],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
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
DescribeDBClusterSnapshotAttributesMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeDBLogFilesDetailsTypeDef = TypedDict(
    "DescribeDBLogFilesDetailsTypeDef",
    {
        "LogFileName": NotRequired[str],
        "LastWritten": NotRequired[int],
        "Size": NotRequired[int],
    },
)
DescribeDBSnapshotAttributesMessageRequestTypeDef = TypedDict(
    "DescribeDBSnapshotAttributesMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
)
DescribeValidDBInstanceModificationsMessageRequestTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
DisableHttpEndpointRequestRequestTypeDef = TypedDict(
    "DisableHttpEndpointRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DoubleRangeTypeDef = TypedDict(
    "DoubleRangeTypeDef",
    {
        "From": NotRequired[float],
        "To": NotRequired[float],
    },
)
DownloadDBLogFilePortionMessageRequestTypeDef = TypedDict(
    "DownloadDBLogFilePortionMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "LogFileName": str,
        "Marker": NotRequired[str],
        "NumberOfLines": NotRequired[int],
    },
)
EnableHttpEndpointRequestRequestTypeDef = TypedDict(
    "EnableHttpEndpointRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
EventCategoriesMapTypeDef = TypedDict(
    "EventCategoriesMapTypeDef",
    {
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[List[str]],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "Message": NotRequired[str],
        "EventCategories": NotRequired[List[str]],
        "Date": NotRequired[datetime],
        "SourceArn": NotRequired[str],
    },
)
ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "ExportTaskIdentifier": NotRequired[str],
        "SourceArn": NotRequired[str],
        "ExportOnly": NotRequired[List[str]],
        "SnapshotTime": NotRequired[datetime],
        "TaskStartTime": NotRequired[datetime],
        "TaskEndTime": NotRequired[datetime],
        "S3Bucket": NotRequired[str],
        "S3Prefix": NotRequired[str],
        "IamRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Status": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "TotalExtractedDataInGB": NotRequired[int],
        "FailureCause": NotRequired[str],
        "WarningMessage": NotRequired[str],
        "SourceType": NotRequired[ExportSourceTypeType],
    },
)
FailoverDBClusterMessageRequestTypeDef = TypedDict(
    "FailoverDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "TargetDBInstanceIdentifier": NotRequired[str],
    },
)
FailoverGlobalClusterMessageRequestTypeDef = TypedDict(
    "FailoverGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "TargetDbClusterIdentifier": str,
        "AllowDataLoss": NotRequired[bool],
        "Switchover": NotRequired[bool],
    },
)
FailoverStateTypeDef = TypedDict(
    "FailoverStateTypeDef",
    {
        "Status": NotRequired[FailoverStatusType],
        "FromDbClusterArn": NotRequired[str],
        "ToDbClusterArn": NotRequired[str],
        "IsDataLossAllowed": NotRequired[bool],
    },
)
GlobalClusterMemberTypeDef = TypedDict(
    "GlobalClusterMemberTypeDef",
    {
        "DBClusterArn": NotRequired[str],
        "Readers": NotRequired[List[str]],
        "IsWriter": NotRequired[bool],
        "GlobalWriteForwardingStatus": NotRequired[WriteForwardingStatusType],
        "SynchronizationStatus": NotRequired[GlobalClusterMemberSynchronizationStatusType],
    },
)
IntegrationErrorTypeDef = TypedDict(
    "IntegrationErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": NotRequired[str],
    },
)
MinimumEngineVersionPerAllowedValueTypeDef = TypedDict(
    "MinimumEngineVersionPerAllowedValueTypeDef",
    {
        "AllowedValue": NotRequired[str],
        "MinimumEngineVersion": NotRequired[str],
    },
)
ModifyActivityStreamRequestRequestTypeDef = TypedDict(
    "ModifyActivityStreamRequestRequestTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "AuditPolicyState": NotRequired[AuditPolicyStateType],
    },
)
ModifyCertificatesMessageRequestTypeDef = TypedDict(
    "ModifyCertificatesMessageRequestTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "RemoveCustomerOverride": NotRequired[bool],
    },
)
ModifyCurrentDBClusterCapacityMessageRequestTypeDef = TypedDict(
    "ModifyCurrentDBClusterCapacityMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Capacity": NotRequired[int],
        "SecondsBeforeTimeout": NotRequired[int],
        "TimeoutAction": NotRequired[str],
    },
)
ModifyCustomDBEngineVersionMessageRequestTypeDef = TypedDict(
    "ModifyCustomDBEngineVersionMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": NotRequired[str],
        "Status": NotRequired[CustomEngineVersionStatusType],
    },
)
ModifyDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "EndpointType": NotRequired[str],
        "StaticMembers": NotRequired[Sequence[str]],
        "ExcludedMembers": NotRequired[Sequence[str]],
    },
)
ModifyDBClusterSnapshotAttributeMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "AttributeName": str,
        "ValuesToAdd": NotRequired[Sequence[str]],
        "ValuesToRemove": NotRequired[Sequence[str]],
    },
)
ModifyDBProxyEndpointRequestRequestTypeDef = TypedDict(
    "ModifyDBProxyEndpointRequestRequestTypeDef",
    {
        "DBProxyEndpointName": str,
        "NewDBProxyEndpointName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)
RecommendedActionUpdateTypeDef = TypedDict(
    "RecommendedActionUpdateTypeDef",
    {
        "ActionId": str,
        "Status": str,
    },
)
ModifyDBSnapshotAttributeMessageRequestTypeDef = TypedDict(
    "ModifyDBSnapshotAttributeMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "AttributeName": str,
        "ValuesToAdd": NotRequired[Sequence[str]],
        "ValuesToRemove": NotRequired[Sequence[str]],
    },
)
ModifyDBSnapshotMessageRequestTypeDef = TypedDict(
    "ModifyDBSnapshotMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "EngineVersion": NotRequired[str],
        "OptionGroupName": NotRequired[str],
    },
)
ModifyDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "SubnetIds": Sequence[str],
        "DBSubnetGroupDescription": NotRequired[str],
    },
)
ModifyEventSubscriptionMessageRequestTypeDef = TypedDict(
    "ModifyEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": NotRequired[str],
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
    },
)
ModifyGlobalClusterMessageRequestTypeDef = TypedDict(
    "ModifyGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "NewGlobalClusterIdentifier": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AllowMajorVersionUpgrade": NotRequired[bool],
    },
)
ModifyTenantDatabaseMessageRequestTypeDef = TypedDict(
    "ModifyTenantDatabaseMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "TenantDBName": str,
        "MasterUserPassword": NotRequired[str],
        "NewTenantDBName": NotRequired[str],
    },
)
OptionSettingTypeDef = TypedDict(
    "OptionSettingTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "Description": NotRequired[str],
        "ApplyType": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[bool],
        "IsCollection": NotRequired[bool],
    },
)
OptionVersionTypeDef = TypedDict(
    "OptionVersionTypeDef",
    {
        "Version": NotRequired[str],
        "IsDefault": NotRequired[bool],
    },
)
OutpostTypeDef = TypedDict(
    "OutpostTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "Action": NotRequired[str],
        "AutoAppliedAfterDate": NotRequired[datetime],
        "ForcedApplyDate": NotRequired[datetime],
        "OptInStatus": NotRequired[str],
        "CurrentApplyDate": NotRequired[datetime],
        "Description": NotRequired[str],
    },
)
PerformanceInsightsMetricDimensionGroupTypeDef = TypedDict(
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    {
        "Dimensions": NotRequired[List[str]],
        "Group": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
PromoteReadReplicaDBClusterMessageRequestTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
PromoteReadReplicaMessageRequestTypeDef = TypedDict(
    "PromoteReadReplicaMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "BackupRetentionPeriod": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
    },
)
RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "From": NotRequired[int],
        "To": NotRequired[int],
        "Step": NotRequired[int],
    },
)
RebootDBClusterMessageRequestTypeDef = TypedDict(
    "RebootDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
RebootDBInstanceMessageRequestTypeDef = TypedDict(
    "RebootDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "ForceFailover": NotRequired[bool],
    },
)
RecommendedActionParameterTypeDef = TypedDict(
    "RecommendedActionParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "RecurringChargeAmount": NotRequired[float],
        "RecurringChargeFrequency": NotRequired[str],
    },
)
ScalarReferenceDetailsTypeDef = TypedDict(
    "ScalarReferenceDetailsTypeDef",
    {
        "Value": NotRequired[float],
    },
)
RegisterDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "RegisterDBProxyTargetsRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": NotRequired[str],
        "DBInstanceIdentifiers": NotRequired[Sequence[str]],
        "DBClusterIdentifiers": NotRequired[Sequence[str]],
    },
)
RemoveFromGlobalClusterMessageRequestTypeDef = TypedDict(
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "DbClusterIdentifier": NotRequired[str],
    },
)
RemoveRoleFromDBClusterMessageRequestTypeDef = TypedDict(
    "RemoveRoleFromDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "RoleArn": str,
        "FeatureName": NotRequired[str],
    },
)
RemoveRoleFromDBInstanceMessageRequestTypeDef = TypedDict(
    "RemoveRoleFromDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "RoleArn": str,
        "FeatureName": str,
    },
)
RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)
RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": Sequence[str],
    },
)
RevokeDBSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "RevokeDBSecurityGroupIngressMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
        "CIDRIP": NotRequired[str],
        "EC2SecurityGroupName": NotRequired[str],
        "EC2SecurityGroupId": NotRequired[str],
        "EC2SecurityGroupOwnerId": NotRequired[str],
    },
)
SourceRegionTypeDef = TypedDict(
    "SourceRegionTypeDef",
    {
        "RegionName": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Status": NotRequired[str],
        "SupportsDBInstanceAutomatedBackupsReplication": NotRequired[bool],
    },
)
StartActivityStreamRequestRequestTypeDef = TypedDict(
    "StartActivityStreamRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Mode": ActivityStreamModeType,
        "KmsKeyId": str,
        "ApplyImmediately": NotRequired[bool],
        "EngineNativeAuditFieldsIncluded": NotRequired[bool],
    },
)
StartDBClusterMessageRequestTypeDef = TypedDict(
    "StartDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef = TypedDict(
    "StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    {
        "SourceDBInstanceArn": str,
        "BackupRetentionPeriod": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "SourceRegion": NotRequired[str],
    },
)
StartDBInstanceMessageRequestTypeDef = TypedDict(
    "StartDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
StartExportTaskMessageRequestTypeDef = TypedDict(
    "StartExportTaskMessageRequestTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "S3BucketName": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
        "S3Prefix": NotRequired[str],
        "ExportOnly": NotRequired[Sequence[str]],
    },
)
StopActivityStreamRequestRequestTypeDef = TypedDict(
    "StopActivityStreamRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ApplyImmediately": NotRequired[bool],
    },
)
StopDBClusterMessageRequestTypeDef = TypedDict(
    "StopDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef = TypedDict(
    "StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    {
        "SourceDBInstanceArn": str,
    },
)
StopDBInstanceMessageRequestTypeDef = TypedDict(
    "StopDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBSnapshotIdentifier": NotRequired[str],
    },
)
SwitchoverBlueGreenDeploymentRequestRequestTypeDef = TypedDict(
    "SwitchoverBlueGreenDeploymentRequestRequestTypeDef",
    {
        "BlueGreenDeploymentIdentifier": str,
        "SwitchoverTimeout": NotRequired[int],
    },
)
SwitchoverGlobalClusterMessageRequestTypeDef = TypedDict(
    "SwitchoverGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "TargetDbClusterIdentifier": str,
    },
)
SwitchoverReadReplicaMessageRequestTypeDef = TypedDict(
    "SwitchoverReadReplicaMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
TenantDatabasePendingModifiedValuesTypeDef = TypedDict(
    "TenantDatabasePendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": NotRequired[str],
        "TenantDBName": NotRequired[str],
    },
)
AccountAttributesMessageTypeDef = TypedDict(
    "AccountAttributesMessageTypeDef",
    {
        "AccountQuotas": List[AccountQuotaTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterBacktrackResponseTypeDef = TypedDict(
    "DBClusterBacktrackResponseTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterCapacityInfoTypeDef = TypedDict(
    "DBClusterCapacityInfoTypeDef",
    {
        "DBClusterIdentifier": str,
        "PendingCapacity": int,
        "CurrentCapacity": int,
        "SecondsBeforeTimeout": int,
        "TimeoutAction": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterEndpointResponseTypeDef = TypedDict(
    "DBClusterEndpointResponseTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterParameterGroupNameMessageTypeDef = TypedDict(
    "DBClusterParameterGroupNameMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBParameterGroupNameMessageTypeDef = TypedDict(
    "DBParameterGroupNameMessageTypeDef",
    {
        "DBParameterGroupName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableHttpEndpointResponseTypeDef = TypedDict(
    "DisableHttpEndpointResponseTypeDef",
    {
        "ResourceArn": str,
        "HttpEndpointEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DownloadDBLogFilePortionDetailsTypeDef = TypedDict(
    "DownloadDBLogFilePortionDetailsTypeDef",
    {
        "LogFileData": str,
        "Marker": str,
        "AdditionalDataPending": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableHttpEndpointResponseTypeDef = TypedDict(
    "EnableHttpEndpointResponseTypeDef",
    {
        "ResourceArn": str,
        "HttpEndpointEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportTaskResponseTypeDef = TypedDict(
    "ExportTaskResponseTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "ExportOnly": List[str],
        "SnapshotTime": datetime,
        "TaskStartTime": datetime,
        "TaskEndTime": datetime,
        "S3Bucket": str,
        "S3Prefix": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
        "Status": str,
        "PercentProgress": int,
        "TotalExtractedDataInGB": int,
        "FailureCause": str,
        "WarningMessage": str,
        "SourceType": ExportSourceTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyActivityStreamResponseTypeDef = TypedDict(
    "ModifyActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
        "Mode": ActivityStreamModeType,
        "EngineNativeAuditFieldsIncluded": bool,
        "PolicyStatus": ActivityStreamPolicyStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartActivityStreamResponseTypeDef = TypedDict(
    "StartActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
        "Mode": ActivityStreamModeType,
        "ApplyImmediately": bool,
        "EngineNativeAuditFieldsIncluded": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopActivityStreamResponseTypeDef = TypedDict(
    "StopActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddSourceIdentifierToSubscriptionResultTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEventSubscriptionResultTypeDef = TypedDict(
    "CreateEventSubscriptionResultTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEventSubscriptionResultTypeDef = TypedDict(
    "DeleteEventSubscriptionResultTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventSubscriptionsMessageTypeDef = TypedDict(
    "EventSubscriptionsMessageTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List[EventSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyEventSubscriptionResultTypeDef = TypedDict(
    "ModifyEventSubscriptionResultTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveSourceIdentifierFromSubscriptionResultTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CopyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "CopyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "SourceDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupDescription": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CopyDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "CopyDBClusterSnapshotMessageRequestTypeDef",
    {
        "SourceDBClusterSnapshotIdentifier": str,
        "TargetDBClusterSnapshotIdentifier": str,
        "KmsKeyId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "CopyTags": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SourceRegion": NotRequired[str],
    },
)
CopyDBParameterGroupMessageRequestTypeDef = TypedDict(
    "CopyDBParameterGroupMessageRequestTypeDef",
    {
        "SourceDBParameterGroupIdentifier": str,
        "TargetDBParameterGroupIdentifier": str,
        "TargetDBParameterGroupDescription": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CopyDBSnapshotMessageRequestTypeDef = TypedDict(
    "CopyDBSnapshotMessageRequestTypeDef",
    {
        "SourceDBSnapshotIdentifier": str,
        "TargetDBSnapshotIdentifier": str,
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "CopyTags": NotRequired[bool],
        "PreSignedUrl": NotRequired[str],
        "OptionGroupName": NotRequired[str],
        "TargetCustomAvailabilityZone": NotRequired[str],
        "CopyOptionGroup": NotRequired[bool],
        "SourceRegion": NotRequired[str],
    },
)
CopyOptionGroupMessageRequestTypeDef = TypedDict(
    "CopyOptionGroupMessageRequestTypeDef",
    {
        "SourceOptionGroupIdentifier": str,
        "TargetOptionGroupIdentifier": str,
        "TargetOptionGroupDescription": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateBlueGreenDeploymentRequestRequestTypeDef = TypedDict(
    "CreateBlueGreenDeploymentRequestRequestTypeDef",
    {
        "BlueGreenDeploymentName": str,
        "Source": str,
        "TargetEngineVersion": NotRequired[str],
        "TargetDBParameterGroupName": NotRequired[str],
        "TargetDBClusterParameterGroupName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "TargetDBInstanceClass": NotRequired[str],
        "UpgradeTargetStorageConfig": NotRequired[bool],
    },
)
CreateCustomDBEngineVersionMessageRequestTypeDef = TypedDict(
    "CreateCustomDBEngineVersionMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DatabaseInstallationFilesS3BucketName": NotRequired[str],
        "DatabaseInstallationFilesS3Prefix": NotRequired[str],
        "ImageId": NotRequired[str],
        "KMSKeyId": NotRequired[str],
        "Description": NotRequired[str],
        "Manifest": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SourceCustomDbEngineVersionIdentifier": NotRequired[str],
        "UseAwsProvidedLatestImage": NotRequired[bool],
    },
)
CreateDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "CreateDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "DBClusterEndpointIdentifier": str,
        "EndpointType": str,
        "StaticMembers": NotRequired[Sequence[str]],
        "ExcludedMembers": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "CreateDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "CreateDBClusterSnapshotMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDBParameterGroupMessageRequestTypeDef = TypedDict(
    "CreateDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDBProxyEndpointRequestRequestTypeDef = TypedDict(
    "CreateDBProxyEndpointRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "DBProxyEndpointName": str,
        "VpcSubnetIds": Sequence[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "TargetRole": NotRequired[DBProxyEndpointTargetRoleType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDBSecurityGroupMessageRequestTypeDef = TypedDict(
    "CreateDBSecurityGroupMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDBSnapshotMessageRequestTypeDef = TypedDict(
    "CreateDBSnapshotMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "CreateDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "SubnetIds": Sequence[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateEventSubscriptionMessageRequestTypeDef = TypedDict(
    "CreateEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": str,
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[Sequence[str]],
        "SourceIds": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateIntegrationMessageRequestTypeDef = TypedDict(
    "CreateIntegrationMessageRequestTypeDef",
    {
        "SourceArn": str,
        "TargetArn": str,
        "IntegrationName": str,
        "KMSKeyId": NotRequired[str],
        "AdditionalEncryptionContext": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateOptionGroupMessageRequestTypeDef = TypedDict(
    "CreateOptionGroupMessageRequestTypeDef",
    {
        "OptionGroupName": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "OptionGroupDescription": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateTenantDatabaseMessageRequestTypeDef = TypedDict(
    "CreateTenantDatabaseMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "TenantDBName": str,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "CharacterSetName": NotRequired[str],
        "NcharCharacterSetName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DBClusterSnapshotTypeDef = TypedDict(
    "DBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "SnapshotCreateTime": NotRequired[datetime],
        "Engine": NotRequired[str],
        "EngineMode": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "ClusterCreateTime": NotRequired[datetime],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DBClusterSnapshotArn": NotRequired[str],
        "SourceDBClusterSnapshotArn": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "TagList": NotRequired[List[TagTypeDef]],
        "DBSystemId": NotRequired[str],
        "StorageType": NotRequired[str],
        "DbClusterResourceId": NotRequired[str],
    },
)
DBSnapshotTenantDatabaseTypeDef = TypedDict(
    "DBSnapshotTenantDatabaseTypeDef",
    {
        "DBSnapshotIdentifier": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "DbiResourceId": NotRequired[str],
        "EngineName": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "TenantDatabaseCreateTime": NotRequired[datetime],
        "TenantDBName": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "TenantDatabaseResourceId": NotRequired[str],
        "CharacterSetName": NotRequired[str],
        "DBSnapshotTenantDatabaseARN": NotRequired[str],
        "NcharCharacterSetName": NotRequired[str],
        "TagList": NotRequired[List[TagTypeDef]],
    },
)
PurchaseReservedDBInstancesOfferingMessageRequestTypeDef = TypedDict(
    "PurchaseReservedDBInstancesOfferingMessageRequestTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
        "ReservedDBInstanceId": NotRequired[str],
        "DBInstanceCount": NotRequired[int],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagListMessageTypeDef = TypedDict(
    "TagListMessageTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OrderableDBInstanceOptionTypeDef = TypedDict(
    "OrderableDBInstanceOptionTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "AvailabilityZoneGroup": NotRequired[str],
        "AvailabilityZones": NotRequired[List[AvailabilityZoneTypeDef]],
        "MultiAZCapable": NotRequired[bool],
        "ReadReplicaCapable": NotRequired[bool],
        "Vpc": NotRequired[bool],
        "SupportsStorageEncryption": NotRequired[bool],
        "StorageType": NotRequired[str],
        "SupportsIops": NotRequired[bool],
        "SupportsEnhancedMonitoring": NotRequired[bool],
        "SupportsIAMDatabaseAuthentication": NotRequired[bool],
        "SupportsPerformanceInsights": NotRequired[bool],
        "MinStorageSize": NotRequired[int],
        "MaxStorageSize": NotRequired[int],
        "MinIopsPerDbInstance": NotRequired[int],
        "MaxIopsPerDbInstance": NotRequired[int],
        "MinIopsPerGib": NotRequired[float],
        "MaxIopsPerGib": NotRequired[float],
        "AvailableProcessorFeatures": NotRequired[List[AvailableProcessorFeatureTypeDef]],
        "SupportedEngineModes": NotRequired[List[str]],
        "SupportsStorageAutoscaling": NotRequired[bool],
        "SupportsKerberosAuthentication": NotRequired[bool],
        "OutpostCapable": NotRequired[bool],
        "SupportedActivityStreamModes": NotRequired[List[str]],
        "SupportsGlobalDatabases": NotRequired[bool],
        "SupportsClusters": NotRequired[bool],
        "SupportedNetworkTypes": NotRequired[List[str]],
        "SupportsStorageThroughput": NotRequired[bool],
        "MinStorageThroughputPerDbInstance": NotRequired[int],
        "MaxStorageThroughputPerDbInstance": NotRequired[int],
        "MinStorageThroughputPerIops": NotRequired[float],
        "MaxStorageThroughputPerIops": NotRequired[float],
        "SupportsDedicatedLogVolume": NotRequired[bool],
    },
)
BacktrackDBClusterMessageRequestTypeDef = TypedDict(
    "BacktrackDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackTo": TimestampTypeDef,
        "Force": NotRequired[bool],
        "UseEarliestTimeOnPointInTimeUnavailable": NotRequired[bool],
    },
)
BlueGreenDeploymentTypeDef = TypedDict(
    "BlueGreenDeploymentTypeDef",
    {
        "BlueGreenDeploymentIdentifier": NotRequired[str],
        "BlueGreenDeploymentName": NotRequired[str],
        "Source": NotRequired[str],
        "Target": NotRequired[str],
        "SwitchoverDetails": NotRequired[List[SwitchoverDetailTypeDef]],
        "Tasks": NotRequired[List[BlueGreenDeploymentTaskTypeDef]],
        "Status": NotRequired[str],
        "StatusDetails": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "DeleteTime": NotRequired[datetime],
        "TagList": NotRequired[List[TagTypeDef]],
    },
)
CertificateMessageTypeDef = TypedDict(
    "CertificateMessageTypeDef",
    {
        "DefaultCertificateForNewLaunches": str,
        "Certificates": List[CertificateTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyCertificatesResultTypeDef = TypedDict(
    "ModifyCertificatesResultTypeDef",
    {
        "Certificate": CertificateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClusterPendingModifiedValuesTypeDef",
    {
        "PendingCloudwatchLogsExports": NotRequired[PendingCloudwatchLogsExportsTypeDef],
        "DBClusterIdentifier": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "AllocatedStorage": NotRequired[int],
        "RdsCustomClusterConfiguration": NotRequired[RdsCustomClusterConfigurationTypeDef],
        "Iops": NotRequired[int],
        "StorageType": NotRequired[str],
    },
)
DBProxyTargetGroupTypeDef = TypedDict(
    "DBProxyTargetGroupTypeDef",
    {
        "DBProxyName": NotRequired[str],
        "TargetGroupName": NotRequired[str],
        "TargetGroupArn": NotRequired[str],
        "IsDefault": NotRequired[bool],
        "Status": NotRequired[str],
        "ConnectionPoolConfig": NotRequired[ConnectionPoolConfigurationInfoTypeDef],
        "CreatedDate": NotRequired[datetime],
        "UpdatedDate": NotRequired[datetime],
    },
)
ModifyDBProxyTargetGroupRequestRequestTypeDef = TypedDict(
    "ModifyDBProxyTargetGroupRequestRequestTypeDef",
    {
        "TargetGroupName": str,
        "DBProxyName": str,
        "ConnectionPoolConfig": NotRequired[ConnectionPoolConfigurationTypeDef],
        "NewName": NotRequired[str],
    },
)
CopyDBClusterParameterGroupResultTypeDef = TypedDict(
    "CopyDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": DBClusterParameterGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBClusterParameterGroupResultTypeDef = TypedDict(
    "CreateDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": DBClusterParameterGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterParameterGroupsMessageTypeDef = TypedDict(
    "DBClusterParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "DBClusterParameterGroups": List[DBClusterParameterGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopyDBParameterGroupResultTypeDef = TypedDict(
    "CopyDBParameterGroupResultTypeDef",
    {
        "DBParameterGroup": DBParameterGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBParameterGroupResultTypeDef = TypedDict(
    "CreateDBParameterGroupResultTypeDef",
    {
        "DBParameterGroup": DBParameterGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBParameterGroupsMessageTypeDef = TypedDict(
    "DBParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "DBParameterGroups": List[DBParameterGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBClusterMessageRequestTypeDef = TypedDict(
    "CreateDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Engine": str,
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "CharacterSetName": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "DBClusterParameterGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "DBSubnetGroupName": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "OptionGroupName": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReplicationSourceIdentifier": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "BacktrackWindow": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "EngineMode": NotRequired[str],
        "ScalingConfiguration": NotRequired[ScalingConfigurationTypeDef],
        "RdsCustomClusterConfiguration": NotRequired[RdsCustomClusterConfigurationTypeDef],
        "DeletionProtection": NotRequired[bool],
        "GlobalClusterIdentifier": NotRequired[str],
        "EnableHttpEndpoint": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "EnableGlobalWriteForwarding": NotRequired[bool],
        "DBClusterInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "StorageType": NotRequired[str],
        "Iops": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "ServerlessV2ScalingConfiguration": NotRequired[ServerlessV2ScalingConfigurationTypeDef],
        "NetworkType": NotRequired[str],
        "DBSystemId": NotRequired[str],
        "ManageMasterUserPassword": NotRequired[bool],
        "MasterUserSecretKmsKeyId": NotRequired[str],
        "EnableLocalWriteForwarding": NotRequired[bool],
        "SourceRegion": NotRequired[str],
    },
)
ModifyDBClusterMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "NewDBClusterIdentifier": NotRequired[str],
        "ApplyImmediately": NotRequired[bool],
        "BackupRetentionPeriod": NotRequired[int],
        "DBClusterParameterGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Port": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "OptionGroupName": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "BacktrackWindow": NotRequired[int],
        "CloudwatchLogsExportConfiguration": NotRequired[CloudwatchLogsExportConfigurationTypeDef],
        "EngineVersion": NotRequired[str],
        "AllowMajorVersionUpgrade": NotRequired[bool],
        "DBInstanceParameterGroupName": NotRequired[str],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "ScalingConfiguration": NotRequired[ScalingConfigurationTypeDef],
        "DeletionProtection": NotRequired[bool],
        "EnableHttpEndpoint": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
        "EnableGlobalWriteForwarding": NotRequired[bool],
        "DBClusterInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "StorageType": NotRequired[str],
        "Iops": NotRequired[int],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "ServerlessV2ScalingConfiguration": NotRequired[ServerlessV2ScalingConfigurationTypeDef],
        "NetworkType": NotRequired[str],
        "ManageMasterUserPassword": NotRequired[bool],
        "RotateMasterUserPassword": NotRequired[bool],
        "MasterUserSecretKmsKeyId": NotRequired[str],
        "EngineMode": NotRequired[str],
        "AllowEngineModeChange": NotRequired[bool],
        "EnableLocalWriteForwarding": NotRequired[bool],
        "AwsBackupRecoveryPointArn": NotRequired[str],
    },
)
RestoreDBClusterFromS3MessageRequestTypeDef = TypedDict(
    "RestoreDBClusterFromS3MessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Engine": str,
        "MasterUsername": str,
        "SourceEngine": str,
        "SourceEngineVersion": str,
        "S3BucketName": str,
        "S3IngestionRoleArn": str,
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "CharacterSetName": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "DBClusterParameterGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "DBSubnetGroupName": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "OptionGroupName": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "S3Prefix": NotRequired[str],
        "BacktrackWindow": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DeletionProtection": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "ServerlessV2ScalingConfiguration": NotRequired[ServerlessV2ScalingConfigurationTypeDef],
        "NetworkType": NotRequired[str],
        "ManageMasterUserPassword": NotRequired[bool],
        "MasterUserSecretKmsKeyId": NotRequired[str],
        "StorageType": NotRequired[str],
    },
)
RestoreDBClusterFromSnapshotMessageRequestTypeDef = TypedDict(
    "RestoreDBClusterFromSnapshotMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "Engine": str,
        "AvailabilityZones": NotRequired[Sequence[str]],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "DBSubnetGroupName": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "OptionGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "KmsKeyId": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "BacktrackWindow": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "EngineMode": NotRequired[str],
        "ScalingConfiguration": NotRequired[ScalingConfigurationTypeDef],
        "DBClusterParameterGroupName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "DBClusterInstanceClass": NotRequired[str],
        "StorageType": NotRequired[str],
        "Iops": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
        "ServerlessV2ScalingConfiguration": NotRequired[ServerlessV2ScalingConfigurationTypeDef],
        "NetworkType": NotRequired[str],
        "RdsCustomClusterConfiguration": NotRequired[RdsCustomClusterConfigurationTypeDef],
    },
)
RestoreDBClusterToPointInTimeMessageRequestTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "RestoreType": NotRequired[str],
        "SourceDBClusterIdentifier": NotRequired[str],
        "RestoreToTime": NotRequired[TimestampTypeDef],
        "UseLatestRestorableTime": NotRequired[bool],
        "Port": NotRequired[int],
        "DBSubnetGroupName": NotRequired[str],
        "OptionGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "KmsKeyId": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "BacktrackWindow": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DBClusterParameterGroupName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "ScalingConfiguration": NotRequired[ScalingConfigurationTypeDef],
        "EngineMode": NotRequired[str],
        "DBClusterInstanceClass": NotRequired[str],
        "StorageType": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "Iops": NotRequired[int],
        "ServerlessV2ScalingConfiguration": NotRequired[ServerlessV2ScalingConfigurationTypeDef],
        "NetworkType": NotRequired[str],
        "SourceDbClusterResourceId": NotRequired[str],
        "RdsCustomClusterConfiguration": NotRequired[RdsCustomClusterConfigurationTypeDef],
    },
)
CreateDBInstanceMessageRequestTypeDef = TypedDict(
    "CreateDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBName": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "DBSecurityGroups": NotRequired[Sequence[str]],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "AvailabilityZone": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "DBParameterGroupName": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
        "Port": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "CharacterSetName": NotRequired[str],
        "NcharCharacterSetName": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DBClusterIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "TdeCredentialPassword": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "Domain": NotRequired[str],
        "DomainFqdn": NotRequired[str],
        "DomainOu": NotRequired[str],
        "DomainAuthSecretArn": NotRequired[str],
        "DomainDnsIps": NotRequired[Sequence[str]],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "PromotionTier": NotRequired[int],
        "Timezone": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence[ProcessorFeatureTypeDef]],
        "DeletionProtection": NotRequired[bool],
        "MaxAllocatedStorage": NotRequired[int],
        "EnableCustomerOwnedIp": NotRequired[bool],
        "CustomIamInstanceProfile": NotRequired[str],
        "BackupTarget": NotRequired[str],
        "NetworkType": NotRequired[str],
        "StorageThroughput": NotRequired[int],
        "ManageMasterUserPassword": NotRequired[bool],
        "MasterUserSecretKmsKeyId": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "DBSystemId": NotRequired[str],
        "DedicatedLogVolume": NotRequired[bool],
        "MultiTenant": NotRequired[bool],
    },
)
CreateDBInstanceReadReplicaMessageRequestTypeDef = TypedDict(
    "CreateDBInstanceReadReplicaMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "SourceDBInstanceIdentifier": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "Port": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "DBParameterGroupName": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DBSubnetGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "StorageType": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence[ProcessorFeatureTypeDef]],
        "UseDefaultProcessorFeatures": NotRequired[bool],
        "DeletionProtection": NotRequired[bool],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "DomainFqdn": NotRequired[str],
        "DomainOu": NotRequired[str],
        "DomainAuthSecretArn": NotRequired[str],
        "DomainDnsIps": NotRequired[Sequence[str]],
        "ReplicaMode": NotRequired[ReplicaModeType],
        "MaxAllocatedStorage": NotRequired[int],
        "CustomIamInstanceProfile": NotRequired[str],
        "NetworkType": NotRequired[str],
        "StorageThroughput": NotRequired[int],
        "EnableCustomerOwnedIp": NotRequired[bool],
        "AllocatedStorage": NotRequired[int],
        "SourceDBClusterIdentifier": NotRequired[str],
        "DedicatedLogVolume": NotRequired[bool],
        "UpgradeStorageConfig": NotRequired[bool],
        "SourceRegion": NotRequired[str],
    },
)
DBSnapshotTypeDef = TypedDict(
    "DBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "SnapshotCreateTime": NotRequired[datetime],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "VpcId": NotRequired[str],
        "InstanceCreateTime": NotRequired[datetime],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "SourceRegion": NotRequired[str],
        "SourceDBSnapshotIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DBSnapshotArn": NotRequired[str],
        "Timezone": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "ProcessorFeatures": NotRequired[List[ProcessorFeatureTypeDef]],
        "DbiResourceId": NotRequired[str],
        "TagList": NotRequired[List[TagTypeDef]],
        "OriginalSnapshotCreateTime": NotRequired[datetime],
        "SnapshotDatabaseTime": NotRequired[datetime],
        "SnapshotTarget": NotRequired[str],
        "StorageThroughput": NotRequired[int],
        "DBSystemId": NotRequired[str],
        "DedicatedLogVolume": NotRequired[bool],
        "MultiTenant": NotRequired[bool],
    },
)
ModifyDBInstanceMessageRequestTypeDef = TypedDict(
    "ModifyDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "AllocatedStorage": NotRequired[int],
        "DBInstanceClass": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "DBSecurityGroups": NotRequired[Sequence[str]],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "ApplyImmediately": NotRequired[bool],
        "MasterUserPassword": NotRequired[str],
        "DBParameterGroupName": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AllowMajorVersionUpgrade": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "NewDBInstanceIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "TdeCredentialPassword": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "Domain": NotRequired[str],
        "DomainFqdn": NotRequired[str],
        "DomainOu": NotRequired[str],
        "DomainAuthSecretArn": NotRequired[str],
        "DomainDnsIps": NotRequired[Sequence[str]],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "DBPortNumber": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
        "MonitoringRoleArn": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "DisableDomain": NotRequired[bool],
        "PromotionTier": NotRequired[int],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "CloudwatchLogsExportConfiguration": NotRequired[CloudwatchLogsExportConfigurationTypeDef],
        "ProcessorFeatures": NotRequired[Sequence[ProcessorFeatureTypeDef]],
        "UseDefaultProcessorFeatures": NotRequired[bool],
        "DeletionProtection": NotRequired[bool],
        "MaxAllocatedStorage": NotRequired[int],
        "CertificateRotationRestart": NotRequired[bool],
        "ReplicaMode": NotRequired[ReplicaModeType],
        "EnableCustomerOwnedIp": NotRequired[bool],
        "AwsBackupRecoveryPointArn": NotRequired[str],
        "AutomationMode": NotRequired[AutomationModeType],
        "ResumeFullAutomationModeMinutes": NotRequired[int],
        "NetworkType": NotRequired[str],
        "StorageThroughput": NotRequired[int],
        "ManageMasterUserPassword": NotRequired[bool],
        "RotateMasterUserPassword": NotRequired[bool],
        "MasterUserSecretKmsKeyId": NotRequired[str],
        "Engine": NotRequired[str],
        "DedicatedLogVolume": NotRequired[bool],
        "MultiTenant": NotRequired[bool],
    },
)
PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "Port": NotRequired[int],
        "BackupRetentionPeriod": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "DBInstanceIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "PendingCloudwatchLogsExports": NotRequired[PendingCloudwatchLogsExportsTypeDef],
        "ProcessorFeatures": NotRequired[List[ProcessorFeatureTypeDef]],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "AutomationMode": NotRequired[AutomationModeType],
        "ResumeFullAutomationModeTime": NotRequired[datetime],
        "StorageThroughput": NotRequired[int],
        "Engine": NotRequired[str],
        "DedicatedLogVolume": NotRequired[bool],
        "MultiTenant": NotRequired[bool],
    },
)
RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef = TypedDict(
    "RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBSnapshotIdentifier": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "PubliclyAccessible": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "LicenseModel": NotRequired[str],
        "DBName": NotRequired[str],
        "Engine": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "TdeCredentialPassword": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Domain": NotRequired[str],
        "DomainFqdn": NotRequired[str],
        "DomainOu": NotRequired[str],
        "DomainAuthSecretArn": NotRequired[str],
        "DomainDnsIps": NotRequired[Sequence[str]],
        "CopyTagsToSnapshot": NotRequired[bool],
        "DomainIAMRoleName": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence[ProcessorFeatureTypeDef]],
        "UseDefaultProcessorFeatures": NotRequired[bool],
        "DBParameterGroupName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "EnableCustomerOwnedIp": NotRequired[bool],
        "CustomIamInstanceProfile": NotRequired[str],
        "BackupTarget": NotRequired[str],
        "NetworkType": NotRequired[str],
        "StorageThroughput": NotRequired[int],
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "DedicatedLogVolume": NotRequired[bool],
    },
)
RestoreDBInstanceFromS3MessageRequestTypeDef = TypedDict(
    "RestoreDBInstanceFromS3MessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "SourceEngine": str,
        "SourceEngineVersion": str,
        "S3BucketName": str,
        "S3IngestionRoleArn": str,
        "DBName": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "DBSecurityGroups": NotRequired[Sequence[str]],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "AvailabilityZone": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "DBParameterGroupName": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
        "Port": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "StorageType": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "S3Prefix": NotRequired[str],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence[ProcessorFeatureTypeDef]],
        "UseDefaultProcessorFeatures": NotRequired[bool],
        "DeletionProtection": NotRequired[bool],
        "MaxAllocatedStorage": NotRequired[int],
        "NetworkType": NotRequired[str],
        "StorageThroughput": NotRequired[int],
        "ManageMasterUserPassword": NotRequired[bool],
        "MasterUserSecretKmsKeyId": NotRequired[str],
        "DedicatedLogVolume": NotRequired[bool],
    },
)
RestoreDBInstanceToPointInTimeMessageRequestTypeDef = TypedDict(
    "RestoreDBInstanceToPointInTimeMessageRequestTypeDef",
    {
        "TargetDBInstanceIdentifier": str,
        "SourceDBInstanceIdentifier": NotRequired[str],
        "RestoreTime": NotRequired[TimestampTypeDef],
        "UseLatestRestorableTime": NotRequired[bool],
        "DBInstanceClass": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "PubliclyAccessible": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "LicenseModel": NotRequired[str],
        "DBName": NotRequired[str],
        "Engine": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "TdeCredentialPassword": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "DomainFqdn": NotRequired[str],
        "DomainOu": NotRequired[str],
        "DomainAuthSecretArn": NotRequired[str],
        "DomainDnsIps": NotRequired[Sequence[str]],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence[ProcessorFeatureTypeDef]],
        "UseDefaultProcessorFeatures": NotRequired[bool],
        "DBParameterGroupName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "SourceDbiResourceId": NotRequired[str],
        "MaxAllocatedStorage": NotRequired[int],
        "SourceDBInstanceAutomatedBackupsArn": NotRequired[str],
        "EnableCustomerOwnedIp": NotRequired[bool],
        "CustomIamInstanceProfile": NotRequired[str],
        "BackupTarget": NotRequired[str],
        "NetworkType": NotRequired[str],
        "StorageThroughput": NotRequired[int],
        "AllocatedStorage": NotRequired[int],
        "DedicatedLogVolume": NotRequired[bool],
    },
)
CreateDBProxyEndpointResponseTypeDef = TypedDict(
    "CreateDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": DBProxyEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDBProxyEndpointResponseTypeDef = TypedDict(
    "DeleteDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": DBProxyEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDBProxyEndpointsResponseTypeDef = TypedDict(
    "DescribeDBProxyEndpointsResponseTypeDef",
    {
        "DBProxyEndpoints": List[DBProxyEndpointTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBProxyEndpointResponseTypeDef = TypedDict(
    "ModifyDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": DBProxyEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBProxyRequestRequestTypeDef = TypedDict(
    "CreateDBProxyRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "EngineFamily": EngineFamilyType,
        "Auth": Sequence[UserAuthConfigTypeDef],
        "RoleArn": str,
        "VpcSubnetIds": Sequence[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "RequireTLS": NotRequired[bool],
        "IdleClientTimeout": NotRequired[int],
        "DebugLogging": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ModifyDBProxyRequestRequestTypeDef = TypedDict(
    "ModifyDBProxyRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "NewDBProxyName": NotRequired[str],
        "Auth": NotRequired[Sequence[UserAuthConfigTypeDef]],
        "RequireTLS": NotRequired[bool],
        "IdleClientTimeout": NotRequired[int],
        "DebugLogging": NotRequired[bool],
        "RoleArn": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
    },
)
DBClusterAutomatedBackupTypeDef = TypedDict(
    "DBClusterAutomatedBackupTypeDef",
    {
        "Engine": NotRequired[str],
        "VpcId": NotRequired[str],
        "DBClusterAutomatedBackupsArn": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "RestoreWindow": NotRequired[RestoreWindowTypeDef],
        "MasterUsername": NotRequired[str],
        "DbClusterResourceId": NotRequired[str],
        "Region": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Status": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "ClusterCreateTime": NotRequired[datetime],
        "StorageEncrypted": NotRequired[bool],
        "AllocatedStorage": NotRequired[int],
        "EngineVersion": NotRequired[str],
        "DBClusterArn": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "EngineMode": NotRequired[str],
        "AvailabilityZones": NotRequired[List[str]],
        "Port": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "StorageType": NotRequired[str],
        "Iops": NotRequired[int],
        "AwsBackupRecoveryPointArn": NotRequired[str],
    },
)
DBClusterBacktrackMessageTypeDef = TypedDict(
    "DBClusterBacktrackMessageTypeDef",
    {
        "Marker": str,
        "DBClusterBacktracks": List[DBClusterBacktrackTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterEndpointMessageTypeDef = TypedDict(
    "DBClusterEndpointMessageTypeDef",
    {
        "Marker": str,
        "DBClusterEndpoints": List[DBClusterEndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterParameterGroupDetailsTypeDef = TypedDict(
    "DBClusterParameterGroupDetailsTypeDef",
    {
        "Parameters": List[ParameterTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBParameterGroupDetailsTypeDef = TypedDict(
    "DBParameterGroupDetailsTypeDef",
    {
        "Parameters": List[ParameterTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": NotRequired[str],
        "Marker": NotRequired[str],
        "Parameters": NotRequired[List[ParameterTypeDef]],
    },
)
ModifyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Parameters": Sequence[ParameterTypeDef],
    },
)
ModifyDBParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "Parameters": Sequence[ParameterTypeDef],
    },
)
ResetDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "ResetDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "ResetAllParameters": NotRequired[bool],
        "Parameters": NotRequired[Sequence[ParameterTypeDef]],
    },
)
ResetDBParameterGroupMessageRequestTypeDef = TypedDict(
    "ResetDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "ResetAllParameters": NotRequired[bool],
        "Parameters": NotRequired[Sequence[ParameterTypeDef]],
    },
)
DBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "DBClusterSnapshotAttributes": NotRequired[List[DBClusterSnapshotAttributeTypeDef]],
    },
)
DBEngineVersionResponseTypeDef = TypedDict(
    "DBEngineVersionResponseTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "DefaultCharacterSet": CharacterSetTypeDef,
        "Image": CustomDBEngineVersionAMITypeDef,
        "DBEngineMediaType": str,
        "SupportedCharacterSets": List[CharacterSetTypeDef],
        "SupportedNcharCharacterSets": List[CharacterSetTypeDef],
        "ValidUpgradeTarget": List[UpgradeTargetTypeDef],
        "SupportedTimezones": List[TimezoneTypeDef],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
        "SupportedEngineModes": List[str],
        "SupportedFeatureNames": List[str],
        "Status": str,
        "SupportsParallelQuery": bool,
        "SupportsGlobalDatabases": bool,
        "MajorEngineVersion": str,
        "DatabaseInstallationFilesS3BucketName": str,
        "DatabaseInstallationFilesS3Prefix": str,
        "DBEngineVersionArn": str,
        "KMSKeyId": str,
        "CreateTime": datetime,
        "TagList": List[TagTypeDef],
        "SupportsBabelfish": bool,
        "CustomDBEngineVersionManifest": str,
        "SupportsCertificateRotationWithoutRestart": bool,
        "SupportedCACertificateIdentifiers": List[str],
        "SupportsLocalWriteForwarding": bool,
        "SupportsIntegrations": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBEngineVersionTypeDef = TypedDict(
    "DBEngineVersionTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "DBEngineDescription": NotRequired[str],
        "DBEngineVersionDescription": NotRequired[str],
        "DefaultCharacterSet": NotRequired[CharacterSetTypeDef],
        "Image": NotRequired[CustomDBEngineVersionAMITypeDef],
        "DBEngineMediaType": NotRequired[str],
        "SupportedCharacterSets": NotRequired[List[CharacterSetTypeDef]],
        "SupportedNcharCharacterSets": NotRequired[List[CharacterSetTypeDef]],
        "ValidUpgradeTarget": NotRequired[List[UpgradeTargetTypeDef]],
        "SupportedTimezones": NotRequired[List[TimezoneTypeDef]],
        "ExportableLogTypes": NotRequired[List[str]],
        "SupportsLogExportsToCloudwatchLogs": NotRequired[bool],
        "SupportsReadReplica": NotRequired[bool],
        "SupportedEngineModes": NotRequired[List[str]],
        "SupportedFeatureNames": NotRequired[List[str]],
        "Status": NotRequired[str],
        "SupportsParallelQuery": NotRequired[bool],
        "SupportsGlobalDatabases": NotRequired[bool],
        "MajorEngineVersion": NotRequired[str],
        "DatabaseInstallationFilesS3BucketName": NotRequired[str],
        "DatabaseInstallationFilesS3Prefix": NotRequired[str],
        "DBEngineVersionArn": NotRequired[str],
        "KMSKeyId": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "TagList": NotRequired[List[TagTypeDef]],
        "SupportsBabelfish": NotRequired[bool],
        "CustomDBEngineVersionManifest": NotRequired[str],
        "SupportsCertificateRotationWithoutRestart": NotRequired[bool],
        "SupportedCACertificateIdentifiers": NotRequired[List[str]],
        "SupportsLocalWriteForwarding": NotRequired[bool],
        "SupportsIntegrations": NotRequired[bool],
    },
)
DBInstanceAutomatedBackupTypeDef = TypedDict(
    "DBInstanceAutomatedBackupTypeDef",
    {
        "DBInstanceArn": NotRequired[str],
        "DbiResourceId": NotRequired[str],
        "Region": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "RestoreWindow": NotRequired[RestoreWindowTypeDef],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "VpcId": NotRequired[str],
        "InstanceCreateTime": NotRequired[datetime],
        "MasterUsername": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "StorageType": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Timezone": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "BackupRetentionPeriod": NotRequired[int],
        "DBInstanceAutomatedBackupsArn": NotRequired[str],
        "DBInstanceAutomatedBackupsReplications": NotRequired[
            List[DBInstanceAutomatedBackupsReplicationTypeDef]
        ],
        "BackupTarget": NotRequired[str],
        "StorageThroughput": NotRequired[int],
        "AwsBackupRecoveryPointArn": NotRequired[str],
        "DedicatedLogVolume": NotRequired[bool],
        "MultiTenant": NotRequired[bool],
    },
)
DBProxyTargetTypeDef = TypedDict(
    "DBProxyTargetTypeDef",
    {
        "TargetArn": NotRequired[str],
        "Endpoint": NotRequired[str],
        "TrackedClusterId": NotRequired[str],
        "RdsResourceId": NotRequired[str],
        "Port": NotRequired[int],
        "Type": NotRequired[TargetTypeType],
        "Role": NotRequired[TargetRoleType],
        "TargetHealth": NotRequired[TargetHealthTypeDef],
    },
)
DBProxyTypeDef = TypedDict(
    "DBProxyTypeDef",
    {
        "DBProxyName": NotRequired[str],
        "DBProxyArn": NotRequired[str],
        "Status": NotRequired[DBProxyStatusType],
        "EngineFamily": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[List[str]],
        "VpcSubnetIds": NotRequired[List[str]],
        "Auth": NotRequired[List[UserAuthConfigInfoTypeDef]],
        "RoleArn": NotRequired[str],
        "Endpoint": NotRequired[str],
        "RequireTLS": NotRequired[bool],
        "IdleClientTimeout": NotRequired[int],
        "DebugLogging": NotRequired[bool],
        "CreatedDate": NotRequired[datetime],
        "UpdatedDate": NotRequired[datetime],
    },
)
DBSecurityGroupTypeDef = TypedDict(
    "DBSecurityGroupTypeDef",
    {
        "OwnerId": NotRequired[str],
        "DBSecurityGroupName": NotRequired[str],
        "DBSecurityGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "EC2SecurityGroups": NotRequired[List[EC2SecurityGroupTypeDef]],
        "IPRanges": NotRequired[List[IPRangeTypeDef]],
        "DBSecurityGroupArn": NotRequired[str],
    },
)
DBSnapshotAttributesResultTypeDef = TypedDict(
    "DBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotIdentifier": NotRequired[str],
        "DBSnapshotAttributes": NotRequired[List[DBSnapshotAttributeTypeDef]],
    },
)
DescribeBlueGreenDeploymentsRequestRequestTypeDef = TypedDict(
    "DescribeBlueGreenDeploymentsRequestRequestTypeDef",
    {
        "BlueGreenDeploymentIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeCertificatesMessageRequestTypeDef = TypedDict(
    "DescribeCertificatesMessageRequestTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBClusterAutomatedBackupsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterAutomatedBackupsMessageRequestTypeDef",
    {
        "DbClusterResourceId": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBClusterBacktracksMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterBacktracksMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBClusterEndpointsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterEndpointsMessageRequestTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterEndpointIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBClusterParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBClusterParametersMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterParametersMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Source": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBClusterSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
        "DbClusterResourceId": NotRequired[str],
    },
)
DescribeDBClustersMessageRequestTypeDef = TypedDict(
    "DescribeDBClustersMessageRequestTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
    },
)
DescribeDBEngineVersionsMessageRequestTypeDef = TypedDict(
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "DefaultOnly": NotRequired[bool],
        "ListSupportedCharacterSets": NotRequired[bool],
        "ListSupportedTimezones": NotRequired[bool],
        "IncludeAll": NotRequired[bool],
    },
)
DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef = TypedDict(
    "DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef",
    {
        "DbiResourceId": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "DBInstanceAutomatedBackupsArn": NotRequired[str],
    },
)
DescribeDBInstancesMessageRequestTypeDef = TypedDict(
    "DescribeDBInstancesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBLogFilesMessageRequestTypeDef = TypedDict(
    "DescribeDBLogFilesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "FilenameContains": NotRequired[str],
        "FileLastWritten": NotRequired[int],
        "FileSize": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBParameterGroupsMessageRequestTypeDef",
    {
        "DBParameterGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBParametersMessageRequestTypeDef = TypedDict(
    "DescribeDBParametersMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "Source": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBProxiesRequestRequestTypeDef = TypedDict(
    "DescribeDBProxiesRequestRequestTypeDef",
    {
        "DBProxyName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeDBProxyEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeDBProxyEndpointsRequestRequestTypeDef",
    {
        "DBProxyName": NotRequired[str],
        "DBProxyEndpointName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeDBProxyTargetGroupsRequestRequestTypeDef = TypedDict(
    "DescribeDBProxyTargetGroupsRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "DescribeDBProxyTargetsRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeDBRecommendationsMessageRequestTypeDef = TypedDict(
    "DescribeDBRecommendationsMessageRequestTypeDef",
    {
        "LastUpdatedAfter": NotRequired[TimestampTypeDef],
        "LastUpdatedBefore": NotRequired[TimestampTypeDef],
        "Locale": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBSecurityGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBSecurityGroupsMessageRequestTypeDef",
    {
        "DBSecurityGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBSnapshotTenantDatabasesMessageRequestTypeDef = TypedDict(
    "DescribeDBSnapshotTenantDatabasesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DBSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "DbiResourceId": NotRequired[str],
    },
)
DescribeDBSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeDBSnapshotsMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DBSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
        "DbiResourceId": NotRequired[str],
    },
)
DescribeDBSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    {
        "DBSubnetGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeEngineDefaultClusterParametersMessageRequestTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeEngineDefaultParametersMessageRequestTypeDef = TypedDict(
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeEventCategoriesMessageRequestTypeDef = TypedDict(
    "DescribeEventCategoriesMessageRequestTypeDef",
    {
        "SourceType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeEventSubscriptionsMessageRequestTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    {
        "SubscriptionName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Duration": NotRequired[int],
        "EventCategories": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeExportTasksMessageRequestTypeDef = TypedDict(
    "DescribeExportTasksMessageRequestTypeDef",
    {
        "ExportTaskIdentifier": NotRequired[str],
        "SourceArn": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "SourceType": NotRequired[ExportSourceTypeType],
    },
)
DescribeGlobalClustersMessageRequestTypeDef = TypedDict(
    "DescribeGlobalClustersMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeIntegrationsMessageRequestTypeDef = TypedDict(
    "DescribeIntegrationsMessageRequestTypeDef",
    {
        "IntegrationIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeOptionGroupOptionsMessageRequestTypeDef = TypedDict(
    "DescribeOptionGroupOptionsMessageRequestTypeDef",
    {
        "EngineName": str,
        "MajorEngineVersion": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeOptionGroupsMessageRequestTypeDef = TypedDict(
    "DescribeOptionGroupsMessageRequestTypeDef",
    {
        "OptionGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "EngineName": NotRequired[str],
        "MajorEngineVersion": NotRequired[str],
    },
)
DescribeOrderableDBInstanceOptionsMessageRequestTypeDef = TypedDict(
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "AvailabilityZoneGroup": NotRequired[str],
        "Vpc": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribePendingMaintenanceActionsMessageRequestTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    {
        "ResourceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeReservedDBInstancesMessageRequestTypeDef = TypedDict(
    "DescribeReservedDBInstancesMessageRequestTypeDef",
    {
        "ReservedDBInstanceId": NotRequired[str],
        "ReservedDBInstancesOfferingId": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "LeaseId": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeReservedDBInstancesOfferingsMessageRequestTypeDef = TypedDict(
    "DescribeReservedDBInstancesOfferingsMessageRequestTypeDef",
    {
        "ReservedDBInstancesOfferingId": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeSourceRegionsMessageRequestTypeDef = TypedDict(
    "DescribeSourceRegionsMessageRequestTypeDef",
    {
        "RegionName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeTenantDatabasesMessageRequestTypeDef = TypedDict(
    "DescribeTenantDatabasesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "TenantDBName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeBlueGreenDeploymentsRequestDescribeBlueGreenDeploymentsPaginateTypeDef = TypedDict(
    "DescribeBlueGreenDeploymentsRequestDescribeBlueGreenDeploymentsPaginateTypeDef",
    {
        "BlueGreenDeploymentIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef = TypedDict(
    "DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBClusterAutomatedBackupsMessageDescribeDBClusterAutomatedBackupsPaginateTypeDef = (
    TypedDict(
        "DescribeDBClusterAutomatedBackupsMessageDescribeDBClusterAutomatedBackupsPaginateTypeDef",
        {
            "DbClusterResourceId": NotRequired[str],
            "DBClusterIdentifier": NotRequired[str],
            "Filters": NotRequired[Sequence[FilterTypeDef]],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeDBClusterBacktracksMessageDescribeDBClusterBacktracksPaginateTypeDef = TypedDict(
    "DescribeDBClusterBacktracksMessageDescribeDBClusterBacktracksPaginateTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBClusterEndpointsMessageDescribeDBClusterEndpointsPaginateTypeDef = TypedDict(
    "DescribeDBClusterEndpointsMessageDescribeDBClusterEndpointsPaginateTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterEndpointIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef = TypedDict(
    "DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef",
    {
        "DBClusterParameterGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateTypeDef = TypedDict(
    "DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Source": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef = TypedDict(
    "DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
        "DbClusterResourceId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef = TypedDict(
    "DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "IncludeShared": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef = TypedDict(
    "DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DefaultOnly": NotRequired[bool],
        "ListSupportedCharacterSets": NotRequired[bool],
        "ListSupportedTimezones": NotRequired[bool],
        "IncludeAll": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBInstanceAutomatedBackupsMessageDescribeDBInstanceAutomatedBackupsPaginateTypeDef = TypedDict(
    "DescribeDBInstanceAutomatedBackupsMessageDescribeDBInstanceAutomatedBackupsPaginateTypeDef",
    {
        "DbiResourceId": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DBInstanceAutomatedBackupsArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef = TypedDict(
    "DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBLogFilesMessageDescribeDBLogFilesPaginateTypeDef = TypedDict(
    "DescribeDBLogFilesMessageDescribeDBLogFilesPaginateTypeDef",
    {
        "DBInstanceIdentifier": str,
        "FilenameContains": NotRequired[str],
        "FileLastWritten": NotRequired[int],
        "FileSize": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBParameterGroupsMessageDescribeDBParameterGroupsPaginateTypeDef = TypedDict(
    "DescribeDBParameterGroupsMessageDescribeDBParameterGroupsPaginateTypeDef",
    {
        "DBParameterGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBParametersMessageDescribeDBParametersPaginateTypeDef = TypedDict(
    "DescribeDBParametersMessageDescribeDBParametersPaginateTypeDef",
    {
        "DBParameterGroupName": str,
        "Source": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBProxiesRequestDescribeDBProxiesPaginateTypeDef = TypedDict(
    "DescribeDBProxiesRequestDescribeDBProxiesPaginateTypeDef",
    {
        "DBProxyName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBProxyEndpointsRequestDescribeDBProxyEndpointsPaginateTypeDef = TypedDict(
    "DescribeDBProxyEndpointsRequestDescribeDBProxyEndpointsPaginateTypeDef",
    {
        "DBProxyName": NotRequired[str],
        "DBProxyEndpointName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBProxyTargetGroupsRequestDescribeDBProxyTargetGroupsPaginateTypeDef = TypedDict(
    "DescribeDBProxyTargetGroupsRequestDescribeDBProxyTargetGroupsPaginateTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBProxyTargetsRequestDescribeDBProxyTargetsPaginateTypeDef = TypedDict(
    "DescribeDBProxyTargetsRequestDescribeDBProxyTargetsPaginateTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBRecommendationsMessageDescribeDBRecommendationsPaginateTypeDef = TypedDict(
    "DescribeDBRecommendationsMessageDescribeDBRecommendationsPaginateTypeDef",
    {
        "LastUpdatedAfter": NotRequired[TimestampTypeDef],
        "LastUpdatedBefore": NotRequired[TimestampTypeDef],
        "Locale": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBSecurityGroupsMessageDescribeDBSecurityGroupsPaginateTypeDef = TypedDict(
    "DescribeDBSecurityGroupsMessageDescribeDBSecurityGroupsPaginateTypeDef",
    {
        "DBSecurityGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBSnapshotTenantDatabasesMessageDescribeDBSnapshotTenantDatabasesPaginateTypeDef = (
    TypedDict(
        "DescribeDBSnapshotTenantDatabasesMessageDescribeDBSnapshotTenantDatabasesPaginateTypeDef",
        {
            "DBInstanceIdentifier": NotRequired[str],
            "DBSnapshotIdentifier": NotRequired[str],
            "SnapshotType": NotRequired[str],
            "Filters": NotRequired[Sequence[FilterTypeDef]],
            "DbiResourceId": NotRequired[str],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeDBSnapshotsMessageDescribeDBSnapshotsPaginateTypeDef = TypedDict(
    "DescribeDBSnapshotsMessageDescribeDBSnapshotsPaginateTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DBSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
        "DbiResourceId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef = TypedDict(
    "DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef",
    {
        "DBSubnetGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEngineDefaultClusterParametersMessageDescribeEngineDefaultClusterParametersPaginateTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersMessageDescribeEngineDefaultClusterParametersPaginateTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef = TypedDict(
    "DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef",
    {
        "SubscriptionName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsMessageDescribeEventsPaginateTypeDef = TypedDict(
    "DescribeEventsMessageDescribeEventsPaginateTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Duration": NotRequired[int],
        "EventCategories": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeExportTasksMessageDescribeExportTasksPaginateTypeDef = TypedDict(
    "DescribeExportTasksMessageDescribeExportTasksPaginateTypeDef",
    {
        "ExportTaskIdentifier": NotRequired[str],
        "SourceArn": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "SourceType": NotRequired[ExportSourceTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef = TypedDict(
    "DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeIntegrationsMessageDescribeIntegrationsPaginateTypeDef = TypedDict(
    "DescribeIntegrationsMessageDescribeIntegrationsPaginateTypeDef",
    {
        "IntegrationIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOptionGroupOptionsMessageDescribeOptionGroupOptionsPaginateTypeDef = TypedDict(
    "DescribeOptionGroupOptionsMessageDescribeOptionGroupOptionsPaginateTypeDef",
    {
        "EngineName": str,
        "MajorEngineVersion": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOptionGroupsMessageDescribeOptionGroupsPaginateTypeDef = TypedDict(
    "DescribeOptionGroupsMessageDescribeOptionGroupsPaginateTypeDef",
    {
        "OptionGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "EngineName": NotRequired[str],
        "MajorEngineVersion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateTypeDef = TypedDict(
    "DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateTypeDef",
    {
        "Engine": str,
        "EngineVersion": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "AvailabilityZoneGroup": NotRequired[str],
        "Vpc": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePendingMaintenanceActionsMessageDescribePendingMaintenanceActionsPaginateTypeDef = (
    TypedDict(
        "DescribePendingMaintenanceActionsMessageDescribePendingMaintenanceActionsPaginateTypeDef",
        {
            "ResourceIdentifier": NotRequired[str],
            "Filters": NotRequired[Sequence[FilterTypeDef]],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeReservedDBInstancesMessageDescribeReservedDBInstancesPaginateTypeDef = TypedDict(
    "DescribeReservedDBInstancesMessageDescribeReservedDBInstancesPaginateTypeDef",
    {
        "ReservedDBInstanceId": NotRequired[str],
        "ReservedDBInstancesOfferingId": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "LeaseId": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReservedDBInstancesOfferingsMessageDescribeReservedDBInstancesOfferingsPaginateTypeDef = TypedDict(
    "DescribeReservedDBInstancesOfferingsMessageDescribeReservedDBInstancesOfferingsPaginateTypeDef",
    {
        "ReservedDBInstancesOfferingId": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSourceRegionsMessageDescribeSourceRegionsPaginateTypeDef = TypedDict(
    "DescribeSourceRegionsMessageDescribeSourceRegionsPaginateTypeDef",
    {
        "RegionName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTenantDatabasesMessageDescribeTenantDatabasesPaginateTypeDef = TypedDict(
    "DescribeTenantDatabasesMessageDescribeTenantDatabasesPaginateTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "TenantDBName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DownloadDBLogFilePortionMessageDownloadDBLogFilePortionPaginateTypeDef = TypedDict(
    "DownloadDBLogFilePortionMessageDownloadDBLogFilePortionPaginateTypeDef",
    {
        "DBInstanceIdentifier": str,
        "LogFileName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBClusterSnapshotsMessageDBClusterSnapshotAvailableWaitTypeDef = TypedDict(
    "DescribeDBClusterSnapshotsMessageDBClusterSnapshotAvailableWaitTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
        "DbClusterResourceId": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDBClusterSnapshotsMessageDBClusterSnapshotDeletedWaitTypeDef = TypedDict(
    "DescribeDBClusterSnapshotsMessageDBClusterSnapshotDeletedWaitTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
        "DbClusterResourceId": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDBClustersMessageDBClusterAvailableWaitTypeDef = TypedDict(
    "DescribeDBClustersMessageDBClusterAvailableWaitTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDBClustersMessageDBClusterDeletedWaitTypeDef = TypedDict(
    "DescribeDBClustersMessageDBClusterDeletedWaitTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef = TypedDict(
    "DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef = TypedDict(
    "DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDBSnapshotsMessageDBSnapshotAvailableWaitTypeDef = TypedDict(
    "DescribeDBSnapshotsMessageDBSnapshotAvailableWaitTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DBSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
        "DbiResourceId": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDBSnapshotsMessageDBSnapshotCompletedWaitTypeDef = TypedDict(
    "DescribeDBSnapshotsMessageDBSnapshotCompletedWaitTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DBSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
        "DbiResourceId": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDBSnapshotsMessageDBSnapshotDeletedWaitTypeDef = TypedDict(
    "DescribeDBSnapshotsMessageDBSnapshotDeletedWaitTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DBSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
        "DbiResourceId": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeTenantDatabasesMessageTenantDatabaseAvailableWaitTypeDef = TypedDict(
    "DescribeTenantDatabasesMessageTenantDatabaseAvailableWaitTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "TenantDBName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeTenantDatabasesMessageTenantDatabaseDeletedWaitTypeDef = TypedDict(
    "DescribeTenantDatabasesMessageTenantDatabaseDeletedWaitTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "TenantDBName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDBLogFilesResponseTypeDef = TypedDict(
    "DescribeDBLogFilesResponseTypeDef",
    {
        "DescribeDBLogFiles": List[DescribeDBLogFilesDetailsTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventCategoriesMessageTypeDef = TypedDict(
    "EventCategoriesMessageTypeDef",
    {
        "EventCategoriesMapList": List[EventCategoriesMapTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventsMessageTypeDef = TypedDict(
    "EventsMessageTypeDef",
    {
        "Marker": str,
        "Events": List[EventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportTasksMessageTypeDef = TypedDict(
    "ExportTasksMessageTypeDef",
    {
        "Marker": str,
        "ExportTasks": List[ExportTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GlobalClusterTypeDef = TypedDict(
    "GlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "GlobalClusterResourceId": NotRequired[str],
        "GlobalClusterArn": NotRequired[str],
        "Status": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "DeletionProtection": NotRequired[bool],
        "GlobalClusterMembers": NotRequired[List[GlobalClusterMemberTypeDef]],
        "FailoverState": NotRequired[FailoverStateTypeDef],
    },
)
IntegrationResponseTypeDef = TypedDict(
    "IntegrationResponseTypeDef",
    {
        "SourceArn": str,
        "TargetArn": str,
        "IntegrationName": str,
        "IntegrationArn": str,
        "KMSKeyId": str,
        "AdditionalEncryptionContext": Dict[str, str],
        "Status": IntegrationStatusType,
        "Tags": List[TagTypeDef],
        "CreateTime": datetime,
        "Errors": List[IntegrationErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "SourceArn": NotRequired[str],
        "TargetArn": NotRequired[str],
        "IntegrationName": NotRequired[str],
        "IntegrationArn": NotRequired[str],
        "KMSKeyId": NotRequired[str],
        "AdditionalEncryptionContext": NotRequired[Dict[str, str]],
        "Status": NotRequired[IntegrationStatusType],
        "Tags": NotRequired[List[TagTypeDef]],
        "CreateTime": NotRequired[datetime],
        "Errors": NotRequired[List[IntegrationErrorTypeDef]],
    },
)
OptionGroupOptionSettingTypeDef = TypedDict(
    "OptionGroupOptionSettingTypeDef",
    {
        "SettingName": NotRequired[str],
        "SettingDescription": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "ApplyType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[bool],
        "IsRequired": NotRequired[bool],
        "MinimumEngineVersionPerAllowedValue": NotRequired[
            List[MinimumEngineVersionPerAllowedValueTypeDef]
        ],
    },
)
ModifyDBRecommendationMessageRequestTypeDef = TypedDict(
    "ModifyDBRecommendationMessageRequestTypeDef",
    {
        "RecommendationId": str,
        "Locale": NotRequired[str],
        "Status": NotRequired[str],
        "RecommendedActionUpdates": NotRequired[Sequence[RecommendedActionUpdateTypeDef]],
    },
)
OptionConfigurationTypeDef = TypedDict(
    "OptionConfigurationTypeDef",
    {
        "OptionName": str,
        "Port": NotRequired[int],
        "OptionVersion": NotRequired[str],
        "DBSecurityGroupMemberships": NotRequired[Sequence[str]],
        "VpcSecurityGroupMemberships": NotRequired[Sequence[str]],
        "OptionSettings": NotRequired[Sequence[OptionSettingTypeDef]],
    },
)
OptionTypeDef = TypedDict(
    "OptionTypeDef",
    {
        "OptionName": NotRequired[str],
        "OptionDescription": NotRequired[str],
        "Persistent": NotRequired[bool],
        "Permanent": NotRequired[bool],
        "Port": NotRequired[int],
        "OptionVersion": NotRequired[str],
        "OptionSettings": NotRequired[List[OptionSettingTypeDef]],
        "DBSecurityGroupMemberships": NotRequired[List[DBSecurityGroupMembershipTypeDef]],
        "VpcSecurityGroupMemberships": NotRequired[List[VpcSecurityGroupMembershipTypeDef]],
    },
)
SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[AvailabilityZoneTypeDef],
        "SubnetOutpost": NotRequired[OutpostTypeDef],
        "SubnetStatus": NotRequired[str],
    },
)
ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": NotRequired[str],
        "PendingMaintenanceActionDetails": NotRequired[List[PendingMaintenanceActionTypeDef]],
    },
)
PerformanceInsightsMetricQueryTypeDef = TypedDict(
    "PerformanceInsightsMetricQueryTypeDef",
    {
        "GroupBy": NotRequired[PerformanceInsightsMetricDimensionGroupTypeDef],
        "Metric": NotRequired[str],
    },
)
ValidStorageOptionsTypeDef = TypedDict(
    "ValidStorageOptionsTypeDef",
    {
        "StorageType": NotRequired[str],
        "StorageSize": NotRequired[List[RangeTypeDef]],
        "ProvisionedIops": NotRequired[List[RangeTypeDef]],
        "IopsToStorageRatio": NotRequired[List[DoubleRangeTypeDef]],
        "SupportsStorageAutoscaling": NotRequired[bool],
        "ProvisionedStorageThroughput": NotRequired[List[RangeTypeDef]],
        "StorageThroughputToIopsRatio": NotRequired[List[DoubleRangeTypeDef]],
    },
)
ReservedDBInstanceTypeDef = TypedDict(
    "ReservedDBInstanceTypeDef",
    {
        "ReservedDBInstanceId": NotRequired[str],
        "ReservedDBInstancesOfferingId": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[str],
        "DBInstanceCount": NotRequired[int],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "State": NotRequired[str],
        "RecurringCharges": NotRequired[List[RecurringChargeTypeDef]],
        "ReservedDBInstanceArn": NotRequired[str],
        "LeaseId": NotRequired[str],
    },
)
ReservedDBInstancesOfferingTypeDef = TypedDict(
    "ReservedDBInstancesOfferingTypeDef",
    {
        "ReservedDBInstancesOfferingId": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "RecurringCharges": NotRequired[List[RecurringChargeTypeDef]],
    },
)
ReferenceDetailsTypeDef = TypedDict(
    "ReferenceDetailsTypeDef",
    {
        "ScalarReferenceDetails": NotRequired[ScalarReferenceDetailsTypeDef],
    },
)
SourceRegionMessageTypeDef = TypedDict(
    "SourceRegionMessageTypeDef",
    {
        "Marker": str,
        "SourceRegions": List[SourceRegionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TenantDatabaseTypeDef = TypedDict(
    "TenantDatabaseTypeDef",
    {
        "TenantDatabaseCreateTime": NotRequired[datetime],
        "DBInstanceIdentifier": NotRequired[str],
        "TenantDBName": NotRequired[str],
        "Status": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "DbiResourceId": NotRequired[str],
        "TenantDatabaseResourceId": NotRequired[str],
        "TenantDatabaseARN": NotRequired[str],
        "CharacterSetName": NotRequired[str],
        "NcharCharacterSetName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "PendingModifiedValues": NotRequired[TenantDatabasePendingModifiedValuesTypeDef],
        "TagList": NotRequired[List[TagTypeDef]],
    },
)
CopyDBClusterSnapshotResultTypeDef = TypedDict(
    "CopyDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": DBClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBClusterSnapshotResultTypeDef = TypedDict(
    "CreateDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": DBClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterSnapshotMessageTypeDef = TypedDict(
    "DBClusterSnapshotMessageTypeDef",
    {
        "Marker": str,
        "DBClusterSnapshots": List[DBClusterSnapshotTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDBClusterSnapshotResultTypeDef = TypedDict(
    "DeleteDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": DBClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBSnapshotTenantDatabasesMessageTypeDef = TypedDict(
    "DBSnapshotTenantDatabasesMessageTypeDef",
    {
        "Marker": str,
        "DBSnapshotTenantDatabases": List[DBSnapshotTenantDatabaseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OrderableDBInstanceOptionsMessageTypeDef = TypedDict(
    "OrderableDBInstanceOptionsMessageTypeDef",
    {
        "OrderableDBInstanceOptions": List[OrderableDBInstanceOptionTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBlueGreenDeploymentResponseTypeDef = TypedDict(
    "CreateBlueGreenDeploymentResponseTypeDef",
    {
        "BlueGreenDeployment": BlueGreenDeploymentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBlueGreenDeploymentResponseTypeDef = TypedDict(
    "DeleteBlueGreenDeploymentResponseTypeDef",
    {
        "BlueGreenDeployment": BlueGreenDeploymentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBlueGreenDeploymentsResponseTypeDef = TypedDict(
    "DescribeBlueGreenDeploymentsResponseTypeDef",
    {
        "BlueGreenDeployments": List[BlueGreenDeploymentTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SwitchoverBlueGreenDeploymentResponseTypeDef = TypedDict(
    "SwitchoverBlueGreenDeploymentResponseTypeDef",
    {
        "BlueGreenDeployment": BlueGreenDeploymentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterTypeDef = TypedDict(
    "DBClusterTypeDef",
    {
        "AllocatedStorage": NotRequired[int],
        "AvailabilityZones": NotRequired[List[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "CharacterSetName": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterParameterGroup": NotRequired[str],
        "DBSubnetGroup": NotRequired[str],
        "Status": NotRequired[str],
        "AutomaticRestartTime": NotRequired[datetime],
        "PercentProgress": NotRequired[str],
        "EarliestRestorableTime": NotRequired[datetime],
        "Endpoint": NotRequired[str],
        "ReaderEndpoint": NotRequired[str],
        "CustomEndpoints": NotRequired[List[str]],
        "MultiAZ": NotRequired[bool],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LatestRestorableTime": NotRequired[datetime],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "DBClusterOptionGroupMemberships": NotRequired[List[DBClusterOptionGroupStatusTypeDef]],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReplicationSourceIdentifier": NotRequired[str],
        "ReadReplicaIdentifiers": NotRequired[List[str]],
        "StatusInfos": NotRequired[List[DBClusterStatusInfoTypeDef]],
        "DBClusterMembers": NotRequired[List[DBClusterMemberTypeDef]],
        "VpcSecurityGroups": NotRequired[List[VpcSecurityGroupMembershipTypeDef]],
        "HostedZoneId": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterResourceId": NotRequired[str],
        "DBClusterArn": NotRequired[str],
        "AssociatedRoles": NotRequired[List[DBClusterRoleTypeDef]],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "CloneGroupId": NotRequired[str],
        "ClusterCreateTime": NotRequired[datetime],
        "EarliestBacktrackTime": NotRequired[datetime],
        "BacktrackWindow": NotRequired[int],
        "BacktrackConsumedChangeRecords": NotRequired[int],
        "EnabledCloudwatchLogsExports": NotRequired[List[str]],
        "Capacity": NotRequired[int],
        "EngineMode": NotRequired[str],
        "ScalingConfigurationInfo": NotRequired[ScalingConfigurationInfoTypeDef],
        "RdsCustomClusterConfiguration": NotRequired[RdsCustomClusterConfigurationTypeDef],
        "DeletionProtection": NotRequired[bool],
        "HttpEndpointEnabled": NotRequired[bool],
        "ActivityStreamMode": NotRequired[ActivityStreamModeType],
        "ActivityStreamStatus": NotRequired[ActivityStreamStatusType],
        "ActivityStreamKmsKeyId": NotRequired[str],
        "ActivityStreamKinesisStreamName": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "CrossAccountClone": NotRequired[bool],
        "DomainMemberships": NotRequired[List[DomainMembershipTypeDef]],
        "TagList": NotRequired[List[TagTypeDef]],
        "GlobalWriteForwardingStatus": NotRequired[WriteForwardingStatusType],
        "GlobalWriteForwardingRequested": NotRequired[bool],
        "PendingModifiedValues": NotRequired[ClusterPendingModifiedValuesTypeDef],
        "DBClusterInstanceClass": NotRequired[str],
        "StorageType": NotRequired[str],
        "Iops": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "PerformanceInsightsEnabled": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "ServerlessV2ScalingConfiguration": NotRequired[
            ServerlessV2ScalingConfigurationInfoTypeDef
        ],
        "NetworkType": NotRequired[str],
        "DBSystemId": NotRequired[str],
        "MasterUserSecret": NotRequired[MasterUserSecretTypeDef],
        "IOOptimizedNextAllowedModificationTime": NotRequired[datetime],
        "LocalWriteForwardingStatus": NotRequired[LocalWriteForwardingStatusType],
        "AwsBackupRecoveryPointArn": NotRequired[str],
    },
)
DescribeDBProxyTargetGroupsResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetGroupsResponseTypeDef",
    {
        "TargetGroups": List[DBProxyTargetGroupTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBProxyTargetGroupResponseTypeDef = TypedDict(
    "ModifyDBProxyTargetGroupResponseTypeDef",
    {
        "DBProxyTargetGroup": DBProxyTargetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopyDBSnapshotResultTypeDef = TypedDict(
    "CopyDBSnapshotResultTypeDef",
    {
        "DBSnapshot": DBSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBSnapshotResultTypeDef = TypedDict(
    "CreateDBSnapshotResultTypeDef",
    {
        "DBSnapshot": DBSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBSnapshotMessageTypeDef = TypedDict(
    "DBSnapshotMessageTypeDef",
    {
        "Marker": str,
        "DBSnapshots": List[DBSnapshotTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDBSnapshotResultTypeDef = TypedDict(
    "DeleteDBSnapshotResultTypeDef",
    {
        "DBSnapshot": DBSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBSnapshotResultTypeDef = TypedDict(
    "ModifyDBSnapshotResultTypeDef",
    {
        "DBSnapshot": DBSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterAutomatedBackupMessageTypeDef = TypedDict(
    "DBClusterAutomatedBackupMessageTypeDef",
    {
        "Marker": str,
        "DBClusterAutomatedBackups": List[DBClusterAutomatedBackupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDBClusterAutomatedBackupResultTypeDef = TypedDict(
    "DeleteDBClusterAutomatedBackupResultTypeDef",
    {
        "DBClusterAutomatedBackup": DBClusterAutomatedBackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEngineDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    {
        "EngineDefaults": EngineDefaultsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEngineDefaultParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultTypeDef",
    {
        "EngineDefaults": EngineDefaultsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": DBClusterSnapshotAttributesResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBClusterSnapshotAttributeResultTypeDef = TypedDict(
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": DBClusterSnapshotAttributesResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBEngineVersionMessageTypeDef = TypedDict(
    "DBEngineVersionMessageTypeDef",
    {
        "Marker": str,
        "DBEngineVersions": List[DBEngineVersionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBInstanceAutomatedBackupMessageTypeDef = TypedDict(
    "DBInstanceAutomatedBackupMessageTypeDef",
    {
        "Marker": str,
        "DBInstanceAutomatedBackups": List[DBInstanceAutomatedBackupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDBInstanceAutomatedBackupResultTypeDef = TypedDict(
    "DeleteDBInstanceAutomatedBackupResultTypeDef",
    {
        "DBInstanceAutomatedBackup": DBInstanceAutomatedBackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDBInstanceAutomatedBackupsReplicationResultTypeDef = TypedDict(
    "StartDBInstanceAutomatedBackupsReplicationResultTypeDef",
    {
        "DBInstanceAutomatedBackup": DBInstanceAutomatedBackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDBInstanceAutomatedBackupsReplicationResultTypeDef = TypedDict(
    "StopDBInstanceAutomatedBackupsReplicationResultTypeDef",
    {
        "DBInstanceAutomatedBackup": DBInstanceAutomatedBackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDBProxyTargetsResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetsResponseTypeDef",
    {
        "Targets": List[DBProxyTargetTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterDBProxyTargetsResponseTypeDef = TypedDict(
    "RegisterDBProxyTargetsResponseTypeDef",
    {
        "DBProxyTargets": List[DBProxyTargetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBProxyResponseTypeDef = TypedDict(
    "CreateDBProxyResponseTypeDef",
    {
        "DBProxy": DBProxyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDBProxyResponseTypeDef = TypedDict(
    "DeleteDBProxyResponseTypeDef",
    {
        "DBProxy": DBProxyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDBProxiesResponseTypeDef = TypedDict(
    "DescribeDBProxiesResponseTypeDef",
    {
        "DBProxies": List[DBProxyTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBProxyResponseTypeDef = TypedDict(
    "ModifyDBProxyResponseTypeDef",
    {
        "DBProxy": DBProxyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AuthorizeDBSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeDBSecurityGroupIngressResultTypeDef",
    {
        "DBSecurityGroup": DBSecurityGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBSecurityGroupResultTypeDef = TypedDict(
    "CreateDBSecurityGroupResultTypeDef",
    {
        "DBSecurityGroup": DBSecurityGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBSecurityGroupMessageTypeDef = TypedDict(
    "DBSecurityGroupMessageTypeDef",
    {
        "Marker": str,
        "DBSecurityGroups": List[DBSecurityGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RevokeDBSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeDBSecurityGroupIngressResultTypeDef",
    {
        "DBSecurityGroup": DBSecurityGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDBSnapshotAttributesResultTypeDef = TypedDict(
    "DescribeDBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotAttributesResult": DBSnapshotAttributesResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBSnapshotAttributeResultTypeDef = TypedDict(
    "ModifyDBSnapshotAttributeResultTypeDef",
    {
        "DBSnapshotAttributesResult": DBSnapshotAttributesResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGlobalClusterResultTypeDef = TypedDict(
    "CreateGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGlobalClusterResultTypeDef = TypedDict(
    "DeleteGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FailoverGlobalClusterResultTypeDef = TypedDict(
    "FailoverGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GlobalClustersMessageTypeDef = TypedDict(
    "GlobalClustersMessageTypeDef",
    {
        "Marker": str,
        "GlobalClusters": List[GlobalClusterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyGlobalClusterResultTypeDef = TypedDict(
    "ModifyGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveFromGlobalClusterResultTypeDef = TypedDict(
    "RemoveFromGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SwitchoverGlobalClusterResultTypeDef = TypedDict(
    "SwitchoverGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIntegrationsResponseTypeDef = TypedDict(
    "DescribeIntegrationsResponseTypeDef",
    {
        "Marker": str,
        "Integrations": List[IntegrationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OptionGroupOptionTypeDef = TypedDict(
    "OptionGroupOptionTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "EngineName": NotRequired[str],
        "MajorEngineVersion": NotRequired[str],
        "MinimumRequiredMinorEngineVersion": NotRequired[str],
        "PortRequired": NotRequired[bool],
        "DefaultPort": NotRequired[int],
        "OptionsDependedOn": NotRequired[List[str]],
        "OptionsConflictsWith": NotRequired[List[str]],
        "Persistent": NotRequired[bool],
        "Permanent": NotRequired[bool],
        "RequiresAutoMinorEngineVersionUpgrade": NotRequired[bool],
        "VpcOnly": NotRequired[bool],
        "SupportsOptionVersionDowngrade": NotRequired[bool],
        "OptionGroupOptionSettings": NotRequired[List[OptionGroupOptionSettingTypeDef]],
        "OptionGroupOptionVersions": NotRequired[List[OptionVersionTypeDef]],
        "CopyableCrossAccount": NotRequired[bool],
    },
)
ModifyOptionGroupMessageRequestTypeDef = TypedDict(
    "ModifyOptionGroupMessageRequestTypeDef",
    {
        "OptionGroupName": str,
        "OptionsToInclude": NotRequired[Sequence[OptionConfigurationTypeDef]],
        "OptionsToRemove": NotRequired[Sequence[str]],
        "ApplyImmediately": NotRequired[bool],
    },
)
OptionGroupTypeDef = TypedDict(
    "OptionGroupTypeDef",
    {
        "OptionGroupName": NotRequired[str],
        "OptionGroupDescription": NotRequired[str],
        "EngineName": NotRequired[str],
        "MajorEngineVersion": NotRequired[str],
        "Options": NotRequired[List[OptionTypeDef]],
        "AllowsVpcAndNonVpcInstanceMemberships": NotRequired[bool],
        "VpcId": NotRequired[str],
        "OptionGroupArn": NotRequired[str],
        "SourceOptionGroup": NotRequired[str],
        "SourceAccountId": NotRequired[str],
        "CopyTimestamp": NotRequired[datetime],
    },
)
DBSubnetGroupTypeDef = TypedDict(
    "DBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": NotRequired[str],
        "DBSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetGroupStatus": NotRequired[str],
        "Subnets": NotRequired[List[SubnetTypeDef]],
        "DBSubnetGroupArn": NotRequired[str],
        "SupportedNetworkTypes": NotRequired[List[str]],
    },
)
ApplyPendingMaintenanceActionResultTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResultTypeDef",
    {
        "ResourcePendingMaintenanceActions": ResourcePendingMaintenanceActionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PendingMaintenanceActionsMessageTypeDef = TypedDict(
    "PendingMaintenanceActionsMessageTypeDef",
    {
        "PendingMaintenanceActions": List[ResourcePendingMaintenanceActionsTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricQueryTypeDef = TypedDict(
    "MetricQueryTypeDef",
    {
        "PerformanceInsightsMetricQuery": NotRequired[PerformanceInsightsMetricQueryTypeDef],
    },
)
ValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "ValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": NotRequired[List[ValidStorageOptionsTypeDef]],
        "ValidProcessorFeatures": NotRequired[List[AvailableProcessorFeatureTypeDef]],
        "SupportsDedicatedLogVolume": NotRequired[bool],
    },
)
PurchaseReservedDBInstancesOfferingResultTypeDef = TypedDict(
    "PurchaseReservedDBInstancesOfferingResultTypeDef",
    {
        "ReservedDBInstance": ReservedDBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReservedDBInstanceMessageTypeDef = TypedDict(
    "ReservedDBInstanceMessageTypeDef",
    {
        "Marker": str,
        "ReservedDBInstances": List[ReservedDBInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReservedDBInstancesOfferingMessageTypeDef = TypedDict(
    "ReservedDBInstancesOfferingMessageTypeDef",
    {
        "Marker": str,
        "ReservedDBInstancesOfferings": List[ReservedDBInstancesOfferingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricReferenceTypeDef = TypedDict(
    "MetricReferenceTypeDef",
    {
        "Name": NotRequired[str],
        "ReferenceDetails": NotRequired[ReferenceDetailsTypeDef],
    },
)
CreateTenantDatabaseResultTypeDef = TypedDict(
    "CreateTenantDatabaseResultTypeDef",
    {
        "TenantDatabase": TenantDatabaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTenantDatabaseResultTypeDef = TypedDict(
    "DeleteTenantDatabaseResultTypeDef",
    {
        "TenantDatabase": TenantDatabaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyTenantDatabaseResultTypeDef = TypedDict(
    "ModifyTenantDatabaseResultTypeDef",
    {
        "TenantDatabase": TenantDatabaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TenantDatabasesMessageTypeDef = TypedDict(
    "TenantDatabasesMessageTypeDef",
    {
        "Marker": str,
        "TenantDatabases": List[TenantDatabaseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBClusterResultTypeDef = TypedDict(
    "CreateDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterMessageTypeDef = TypedDict(
    "DBClusterMessageTypeDef",
    {
        "Marker": str,
        "DBClusters": List[DBClusterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDBClusterResultTypeDef = TypedDict(
    "DeleteDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FailoverDBClusterResultTypeDef = TypedDict(
    "FailoverDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBClusterResultTypeDef = TypedDict(
    "ModifyDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PromoteReadReplicaDBClusterResultTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RebootDBClusterResultTypeDef = TypedDict(
    "RebootDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreDBClusterFromS3ResultTypeDef = TypedDict(
    "RestoreDBClusterFromS3ResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreDBClusterFromSnapshotResultTypeDef = TypedDict(
    "RestoreDBClusterFromSnapshotResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreDBClusterToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDBClusterResultTypeDef = TypedDict(
    "StartDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDBClusterResultTypeDef = TypedDict(
    "StopDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OptionGroupOptionsMessageTypeDef = TypedDict(
    "OptionGroupOptionsMessageTypeDef",
    {
        "OptionGroupOptions": List[OptionGroupOptionTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopyOptionGroupResultTypeDef = TypedDict(
    "CopyOptionGroupResultTypeDef",
    {
        "OptionGroup": OptionGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateOptionGroupResultTypeDef = TypedDict(
    "CreateOptionGroupResultTypeDef",
    {
        "OptionGroup": OptionGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyOptionGroupResultTypeDef = TypedDict(
    "ModifyOptionGroupResultTypeDef",
    {
        "OptionGroup": OptionGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OptionGroupsTypeDef = TypedDict(
    "OptionGroupsTypeDef",
    {
        "OptionGroupsList": List[OptionGroupTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBSubnetGroupResultTypeDef = TypedDict(
    "CreateDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": DBSubnetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBInstanceTypeDef = TypedDict(
    "DBInstanceTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Engine": NotRequired[str],
        "DBInstanceStatus": NotRequired[str],
        "AutomaticRestartTime": NotRequired[datetime],
        "MasterUsername": NotRequired[str],
        "DBName": NotRequired[str],
        "Endpoint": NotRequired[EndpointTypeDef],
        "AllocatedStorage": NotRequired[int],
        "InstanceCreateTime": NotRequired[datetime],
        "PreferredBackupWindow": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "DBSecurityGroups": NotRequired[List[DBSecurityGroupMembershipTypeDef]],
        "VpcSecurityGroups": NotRequired[List[VpcSecurityGroupMembershipTypeDef]],
        "DBParameterGroups": NotRequired[List[DBParameterGroupStatusTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "DBSubnetGroup": NotRequired[DBSubnetGroupTypeDef],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired[PendingModifiedValuesTypeDef],
        "LatestRestorableTime": NotRequired[datetime],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "ReadReplicaSourceDBInstanceIdentifier": NotRequired[str],
        "ReadReplicaDBInstanceIdentifiers": NotRequired[List[str]],
        "ReadReplicaDBClusterIdentifiers": NotRequired[List[str]],
        "ReplicaMode": NotRequired[ReplicaModeType],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupMemberships": NotRequired[List[OptionGroupMembershipTypeDef]],
        "CharacterSetName": NotRequired[str],
        "NcharCharacterSetName": NotRequired[str],
        "SecondaryAvailabilityZone": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "StatusInfos": NotRequired[List[DBInstanceStatusInfoTypeDef]],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "DbInstancePort": NotRequired[int],
        "DBClusterIdentifier": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbiResourceId": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "DomainMemberships": NotRequired[List[DomainMembershipTypeDef]],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "EnhancedMonitoringResourceArn": NotRequired[str],
        "MonitoringRoleArn": NotRequired[str],
        "PromotionTier": NotRequired[int],
        "DBInstanceArn": NotRequired[str],
        "Timezone": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "PerformanceInsightsEnabled": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnabledCloudwatchLogsExports": NotRequired[List[str]],
        "ProcessorFeatures": NotRequired[List[ProcessorFeatureTypeDef]],
        "DeletionProtection": NotRequired[bool],
        "AssociatedRoles": NotRequired[List[DBInstanceRoleTypeDef]],
        "ListenerEndpoint": NotRequired[EndpointTypeDef],
        "MaxAllocatedStorage": NotRequired[int],
        "TagList": NotRequired[List[TagTypeDef]],
        "DBInstanceAutomatedBackupsReplications": NotRequired[
            List[DBInstanceAutomatedBackupsReplicationTypeDef]
        ],
        "CustomerOwnedIpEnabled": NotRequired[bool],
        "AwsBackupRecoveryPointArn": NotRequired[str],
        "ActivityStreamStatus": NotRequired[ActivityStreamStatusType],
        "ActivityStreamKmsKeyId": NotRequired[str],
        "ActivityStreamKinesisStreamName": NotRequired[str],
        "ActivityStreamMode": NotRequired[ActivityStreamModeType],
        "ActivityStreamEngineNativeAuditFieldsIncluded": NotRequired[bool],
        "AutomationMode": NotRequired[AutomationModeType],
        "ResumeFullAutomationModeTime": NotRequired[datetime],
        "CustomIamInstanceProfile": NotRequired[str],
        "BackupTarget": NotRequired[str],
        "NetworkType": NotRequired[str],
        "ActivityStreamPolicyStatus": NotRequired[ActivityStreamPolicyStatusType],
        "StorageThroughput": NotRequired[int],
        "DBSystemId": NotRequired[str],
        "MasterUserSecret": NotRequired[MasterUserSecretTypeDef],
        "CertificateDetails": NotRequired[CertificateDetailsTypeDef],
        "ReadReplicaSourceDBClusterIdentifier": NotRequired[str],
        "PercentProgress": NotRequired[str],
        "DedicatedLogVolume": NotRequired[bool],
        "IsStorageConfigUpgradeAvailable": NotRequired[bool],
        "MultiTenant": NotRequired[bool],
    },
)
DBSubnetGroupMessageTypeDef = TypedDict(
    "DBSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "DBSubnetGroups": List[DBSubnetGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBSubnetGroupResultTypeDef = TypedDict(
    "ModifyDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": DBSubnetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeValidDBInstanceModificationsResultTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsResultTypeDef",
    {
        "ValidDBInstanceModificationsMessage": ValidDBInstanceModificationsMessageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "Name": NotRequired[str],
        "References": NotRequired[List[MetricReferenceTypeDef]],
        "StatisticsDetails": NotRequired[str],
        "MetricQuery": NotRequired[MetricQueryTypeDef],
    },
)
CreateDBInstanceReadReplicaResultTypeDef = TypedDict(
    "CreateDBInstanceReadReplicaResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBInstanceResultTypeDef = TypedDict(
    "CreateDBInstanceResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBInstanceMessageTypeDef = TypedDict(
    "DBInstanceMessageTypeDef",
    {
        "Marker": str,
        "DBInstances": List[DBInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDBInstanceResultTypeDef = TypedDict(
    "DeleteDBInstanceResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBInstanceResultTypeDef = TypedDict(
    "ModifyDBInstanceResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PromoteReadReplicaResultTypeDef = TypedDict(
    "PromoteReadReplicaResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RebootDBInstanceResultTypeDef = TypedDict(
    "RebootDBInstanceResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreDBInstanceFromDBSnapshotResultTypeDef = TypedDict(
    "RestoreDBInstanceFromDBSnapshotResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreDBInstanceFromS3ResultTypeDef = TypedDict(
    "RestoreDBInstanceFromS3ResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreDBInstanceToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBInstanceToPointInTimeResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDBInstanceResultTypeDef = TypedDict(
    "StartDBInstanceResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDBInstanceResultTypeDef = TypedDict(
    "StopDBInstanceResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SwitchoverReadReplicaResultTypeDef = TypedDict(
    "SwitchoverReadReplicaResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PerformanceIssueDetailsTypeDef = TypedDict(
    "PerformanceIssueDetailsTypeDef",
    {
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Metrics": NotRequired[List[MetricTypeDef]],
        "Analysis": NotRequired[str],
    },
)
IssueDetailsTypeDef = TypedDict(
    "IssueDetailsTypeDef",
    {
        "PerformanceIssueDetails": NotRequired[PerformanceIssueDetailsTypeDef],
    },
)
RecommendedActionTypeDef = TypedDict(
    "RecommendedActionTypeDef",
    {
        "ActionId": NotRequired[str],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "Operation": NotRequired[str],
        "Parameters": NotRequired[List[RecommendedActionParameterTypeDef]],
        "ApplyModes": NotRequired[List[str]],
        "Status": NotRequired[str],
        "IssueDetails": NotRequired[IssueDetailsTypeDef],
        "ContextAttributes": NotRequired[List[ContextAttributeTypeDef]],
    },
)
DBRecommendationTypeDef = TypedDict(
    "DBRecommendationTypeDef",
    {
        "RecommendationId": NotRequired[str],
        "TypeId": NotRequired[str],
        "Severity": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Status": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "UpdatedTime": NotRequired[datetime],
        "Detection": NotRequired[str],
        "Recommendation": NotRequired[str],
        "Description": NotRequired[str],
        "Reason": NotRequired[str],
        "RecommendedActions": NotRequired[List[RecommendedActionTypeDef]],
        "Category": NotRequired[str],
        "Source": NotRequired[str],
        "TypeDetection": NotRequired[str],
        "TypeRecommendation": NotRequired[str],
        "Impact": NotRequired[str],
        "AdditionalInfo": NotRequired[str],
        "Links": NotRequired[List[DocLinkTypeDef]],
        "IssueDetails": NotRequired[IssueDetailsTypeDef],
    },
)
DBRecommendationMessageTypeDef = TypedDict(
    "DBRecommendationMessageTypeDef",
    {
        "DBRecommendation": DBRecommendationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBRecommendationsMessageTypeDef = TypedDict(
    "DBRecommendationsMessageTypeDef",
    {
        "DBRecommendations": List[DBRecommendationTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
