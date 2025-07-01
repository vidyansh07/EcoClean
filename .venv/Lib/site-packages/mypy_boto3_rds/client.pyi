"""
Type annotations for rds service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rds.client import RDSClient

    session = Session()
    client: RDSClient = session.client("rds")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Optional, Sequence, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ActivityStreamModeType,
    AuditPolicyStateType,
    AutomationModeType,
    CustomEngineVersionStatusType,
    DBProxyEndpointTargetRoleType,
    EngineFamilyType,
    ExportSourceTypeType,
    ReplicaModeType,
    SourceTypeType,
)
from .paginator import (
    DescribeBlueGreenDeploymentsPaginator,
    DescribeCertificatesPaginator,
    DescribeDBClusterAutomatedBackupsPaginator,
    DescribeDBClusterBacktracksPaginator,
    DescribeDBClusterEndpointsPaginator,
    DescribeDBClusterParameterGroupsPaginator,
    DescribeDBClusterParametersPaginator,
    DescribeDBClusterSnapshotsPaginator,
    DescribeDBClustersPaginator,
    DescribeDBEngineVersionsPaginator,
    DescribeDBInstanceAutomatedBackupsPaginator,
    DescribeDBInstancesPaginator,
    DescribeDBLogFilesPaginator,
    DescribeDBParameterGroupsPaginator,
    DescribeDBParametersPaginator,
    DescribeDBProxiesPaginator,
    DescribeDBProxyEndpointsPaginator,
    DescribeDBProxyTargetGroupsPaginator,
    DescribeDBProxyTargetsPaginator,
    DescribeDBRecommendationsPaginator,
    DescribeDBSecurityGroupsPaginator,
    DescribeDBSnapshotsPaginator,
    DescribeDBSnapshotTenantDatabasesPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEngineDefaultClusterParametersPaginator,
    DescribeEngineDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeExportTasksPaginator,
    DescribeGlobalClustersPaginator,
    DescribeIntegrationsPaginator,
    DescribeOptionGroupOptionsPaginator,
    DescribeOptionGroupsPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
    DescribePendingMaintenanceActionsPaginator,
    DescribeReservedDBInstancesOfferingsPaginator,
    DescribeReservedDBInstancesPaginator,
    DescribeSourceRegionsPaginator,
    DescribeTenantDatabasesPaginator,
    DownloadDBLogFilePortionPaginator,
)
from .type_defs import (
    AccountAttributesMessageTypeDef,
    AddSourceIdentifierToSubscriptionResultTypeDef,
    ApplyPendingMaintenanceActionResultTypeDef,
    AuthorizeDBSecurityGroupIngressResultTypeDef,
    CertificateMessageTypeDef,
    CloudwatchLogsExportConfigurationTypeDef,
    ConnectionPoolConfigurationTypeDef,
    CopyDBClusterParameterGroupResultTypeDef,
    CopyDBClusterSnapshotResultTypeDef,
    CopyDBParameterGroupResultTypeDef,
    CopyDBSnapshotResultTypeDef,
    CopyOptionGroupResultTypeDef,
    CreateBlueGreenDeploymentResponseTypeDef,
    CreateDBClusterParameterGroupResultTypeDef,
    CreateDBClusterResultTypeDef,
    CreateDBClusterSnapshotResultTypeDef,
    CreateDBInstanceReadReplicaResultTypeDef,
    CreateDBInstanceResultTypeDef,
    CreateDBParameterGroupResultTypeDef,
    CreateDBProxyEndpointResponseTypeDef,
    CreateDBProxyResponseTypeDef,
    CreateDBSecurityGroupResultTypeDef,
    CreateDBSnapshotResultTypeDef,
    CreateDBSubnetGroupResultTypeDef,
    CreateEventSubscriptionResultTypeDef,
    CreateGlobalClusterResultTypeDef,
    CreateOptionGroupResultTypeDef,
    CreateTenantDatabaseResultTypeDef,
    DBClusterAutomatedBackupMessageTypeDef,
    DBClusterBacktrackMessageTypeDef,
    DBClusterBacktrackResponseTypeDef,
    DBClusterCapacityInfoTypeDef,
    DBClusterEndpointMessageTypeDef,
    DBClusterEndpointResponseTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupNameMessageTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBEngineVersionResponseTypeDef,
    DBInstanceAutomatedBackupMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBParameterGroupDetailsTypeDef,
    DBParameterGroupNameMessageTypeDef,
    DBParameterGroupsMessageTypeDef,
    DBRecommendationMessageTypeDef,
    DBRecommendationsMessageTypeDef,
    DBSecurityGroupMessageTypeDef,
    DBSnapshotMessageTypeDef,
    DBSnapshotTenantDatabasesMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DeleteBlueGreenDeploymentResponseTypeDef,
    DeleteDBClusterAutomatedBackupResultTypeDef,
    DeleteDBClusterResultTypeDef,
    DeleteDBClusterSnapshotResultTypeDef,
    DeleteDBInstanceAutomatedBackupResultTypeDef,
    DeleteDBInstanceResultTypeDef,
    DeleteDBProxyEndpointResponseTypeDef,
    DeleteDBProxyResponseTypeDef,
    DeleteDBSnapshotResultTypeDef,
    DeleteEventSubscriptionResultTypeDef,
    DeleteGlobalClusterResultTypeDef,
    DeleteTenantDatabaseResultTypeDef,
    DescribeBlueGreenDeploymentsResponseTypeDef,
    DescribeDBClusterSnapshotAttributesResultTypeDef,
    DescribeDBLogFilesResponseTypeDef,
    DescribeDBProxiesResponseTypeDef,
    DescribeDBProxyEndpointsResponseTypeDef,
    DescribeDBProxyTargetGroupsResponseTypeDef,
    DescribeDBProxyTargetsResponseTypeDef,
    DescribeDBSnapshotAttributesResultTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeIntegrationsResponseTypeDef,
    DescribeValidDBInstanceModificationsResultTypeDef,
    DisableHttpEndpointResponseTypeDef,
    DownloadDBLogFilePortionDetailsTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableHttpEndpointResponseTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    ExportTaskResponseTypeDef,
    ExportTasksMessageTypeDef,
    FailoverDBClusterResultTypeDef,
    FailoverGlobalClusterResultTypeDef,
    FilterTypeDef,
    GlobalClustersMessageTypeDef,
    IntegrationResponseTypeDef,
    ModifyActivityStreamResponseTypeDef,
    ModifyCertificatesResultTypeDef,
    ModifyDBClusterResultTypeDef,
    ModifyDBClusterSnapshotAttributeResultTypeDef,
    ModifyDBInstanceResultTypeDef,
    ModifyDBProxyEndpointResponseTypeDef,
    ModifyDBProxyResponseTypeDef,
    ModifyDBProxyTargetGroupResponseTypeDef,
    ModifyDBSnapshotAttributeResultTypeDef,
    ModifyDBSnapshotResultTypeDef,
    ModifyDBSubnetGroupResultTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    ModifyGlobalClusterResultTypeDef,
    ModifyOptionGroupResultTypeDef,
    ModifyTenantDatabaseResultTypeDef,
    OptionConfigurationTypeDef,
    OptionGroupOptionsMessageTypeDef,
    OptionGroupsTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    ParameterTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    ProcessorFeatureTypeDef,
    PromoteReadReplicaDBClusterResultTypeDef,
    PromoteReadReplicaResultTypeDef,
    PurchaseReservedDBInstancesOfferingResultTypeDef,
    RdsCustomClusterConfigurationTypeDef,
    RebootDBClusterResultTypeDef,
    RebootDBInstanceResultTypeDef,
    RecommendedActionUpdateTypeDef,
    RegisterDBProxyTargetsResponseTypeDef,
    RemoveFromGlobalClusterResultTypeDef,
    RemoveSourceIdentifierFromSubscriptionResultTypeDef,
    ReservedDBInstanceMessageTypeDef,
    ReservedDBInstancesOfferingMessageTypeDef,
    RestoreDBClusterFromS3ResultTypeDef,
    RestoreDBClusterFromSnapshotResultTypeDef,
    RestoreDBClusterToPointInTimeResultTypeDef,
    RestoreDBInstanceFromDBSnapshotResultTypeDef,
    RestoreDBInstanceFromS3ResultTypeDef,
    RestoreDBInstanceToPointInTimeResultTypeDef,
    RevokeDBSecurityGroupIngressResultTypeDef,
    ScalingConfigurationTypeDef,
    ServerlessV2ScalingConfigurationTypeDef,
    SourceRegionMessageTypeDef,
    StartActivityStreamResponseTypeDef,
    StartDBClusterResultTypeDef,
    StartDBInstanceAutomatedBackupsReplicationResultTypeDef,
    StartDBInstanceResultTypeDef,
    StopActivityStreamResponseTypeDef,
    StopDBClusterResultTypeDef,
    StopDBInstanceAutomatedBackupsReplicationResultTypeDef,
    StopDBInstanceResultTypeDef,
    SwitchoverBlueGreenDeploymentResponseTypeDef,
    SwitchoverGlobalClusterResultTypeDef,
    SwitchoverReadReplicaResultTypeDef,
    TagListMessageTypeDef,
    TagTypeDef,
    TenantDatabasesMessageTypeDef,
    TimestampTypeDef,
    UserAuthConfigTypeDef,
)
from .waiter import (
    DBClusterAvailableWaiter,
    DBClusterDeletedWaiter,
    DBClusterSnapshotAvailableWaiter,
    DBClusterSnapshotDeletedWaiter,
    DBInstanceAvailableWaiter,
    DBInstanceDeletedWaiter,
    DBSnapshotAvailableWaiter,
    DBSnapshotCompletedWaiter,
    DBSnapshotDeletedWaiter,
    TenantDatabaseAvailableWaiter,
    TenantDatabaseDeletedWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("RDSClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AuthorizationAlreadyExistsFault: Type[BotocoreClientError]
    AuthorizationNotFoundFault: Type[BotocoreClientError]
    AuthorizationQuotaExceededFault: Type[BotocoreClientError]
    BackupPolicyNotFoundFault: Type[BotocoreClientError]
    BlueGreenDeploymentAlreadyExistsFault: Type[BotocoreClientError]
    BlueGreenDeploymentNotFoundFault: Type[BotocoreClientError]
    CertificateNotFoundFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CreateCustomDBEngineVersionFault: Type[BotocoreClientError]
    CustomAvailabilityZoneNotFoundFault: Type[BotocoreClientError]
    CustomDBEngineVersionAlreadyExistsFault: Type[BotocoreClientError]
    CustomDBEngineVersionNotFoundFault: Type[BotocoreClientError]
    CustomDBEngineVersionQuotaExceededFault: Type[BotocoreClientError]
    DBClusterAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterAutomatedBackupNotFoundFault: Type[BotocoreClientError]
    DBClusterAutomatedBackupQuotaExceededFault: Type[BotocoreClientError]
    DBClusterBacktrackNotFoundFault: Type[BotocoreClientError]
    DBClusterEndpointAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterEndpointNotFoundFault: Type[BotocoreClientError]
    DBClusterEndpointQuotaExceededFault: Type[BotocoreClientError]
    DBClusterNotFoundFault: Type[BotocoreClientError]
    DBClusterParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBClusterQuotaExceededFault: Type[BotocoreClientError]
    DBClusterRoleAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterRoleNotFoundFault: Type[BotocoreClientError]
    DBClusterRoleQuotaExceededFault: Type[BotocoreClientError]
    DBClusterSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterSnapshotNotFoundFault: Type[BotocoreClientError]
    DBInstanceAlreadyExistsFault: Type[BotocoreClientError]
    DBInstanceAutomatedBackupNotFoundFault: Type[BotocoreClientError]
    DBInstanceAutomatedBackupQuotaExceededFault: Type[BotocoreClientError]
    DBInstanceNotFoundFault: Type[BotocoreClientError]
    DBInstanceRoleAlreadyExistsFault: Type[BotocoreClientError]
    DBInstanceRoleNotFoundFault: Type[BotocoreClientError]
    DBInstanceRoleQuotaExceededFault: Type[BotocoreClientError]
    DBLogFileNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    DBProxyAlreadyExistsFault: Type[BotocoreClientError]
    DBProxyEndpointAlreadyExistsFault: Type[BotocoreClientError]
    DBProxyEndpointNotFoundFault: Type[BotocoreClientError]
    DBProxyEndpointQuotaExceededFault: Type[BotocoreClientError]
    DBProxyNotFoundFault: Type[BotocoreClientError]
    DBProxyQuotaExceededFault: Type[BotocoreClientError]
    DBProxyTargetAlreadyRegisteredFault: Type[BotocoreClientError]
    DBProxyTargetGroupNotFoundFault: Type[BotocoreClientError]
    DBProxyTargetNotFoundFault: Type[BotocoreClientError]
    DBSecurityGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBSecurityGroupNotFoundFault: Type[BotocoreClientError]
    DBSecurityGroupNotSupportedFault: Type[BotocoreClientError]
    DBSecurityGroupQuotaExceededFault: Type[BotocoreClientError]
    DBSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBSnapshotNotFoundFault: Type[BotocoreClientError]
    DBSnapshotTenantDatabaseNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBSubnetGroupDoesNotCoverEnoughAZs: Type[BotocoreClientError]
    DBSubnetGroupNotAllowedFault: Type[BotocoreClientError]
    DBSubnetGroupNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    DBSubnetQuotaExceededFault: Type[BotocoreClientError]
    DBUpgradeDependencyFailureFault: Type[BotocoreClientError]
    DomainNotFoundFault: Type[BotocoreClientError]
    Ec2ImagePropertiesNotSupportedFault: Type[BotocoreClientError]
    EventSubscriptionQuotaExceededFault: Type[BotocoreClientError]
    ExportTaskAlreadyExistsFault: Type[BotocoreClientError]
    ExportTaskNotFoundFault: Type[BotocoreClientError]
    GlobalClusterAlreadyExistsFault: Type[BotocoreClientError]
    GlobalClusterNotFoundFault: Type[BotocoreClientError]
    GlobalClusterQuotaExceededFault: Type[BotocoreClientError]
    IamRoleMissingPermissionsFault: Type[BotocoreClientError]
    IamRoleNotFoundFault: Type[BotocoreClientError]
    InstanceQuotaExceededFault: Type[BotocoreClientError]
    InsufficientAvailableIPsInSubnetFault: Type[BotocoreClientError]
    InsufficientDBClusterCapacityFault: Type[BotocoreClientError]
    InsufficientDBInstanceCapacityFault: Type[BotocoreClientError]
    InsufficientStorageClusterCapacityFault: Type[BotocoreClientError]
    IntegrationAlreadyExistsFault: Type[BotocoreClientError]
    IntegrationConflictOperationFault: Type[BotocoreClientError]
    IntegrationNotFoundFault: Type[BotocoreClientError]
    IntegrationQuotaExceededFault: Type[BotocoreClientError]
    InvalidBlueGreenDeploymentStateFault: Type[BotocoreClientError]
    InvalidCustomDBEngineVersionStateFault: Type[BotocoreClientError]
    InvalidDBClusterAutomatedBackupStateFault: Type[BotocoreClientError]
    InvalidDBClusterCapacityFault: Type[BotocoreClientError]
    InvalidDBClusterEndpointStateFault: Type[BotocoreClientError]
    InvalidDBClusterSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBClusterStateFault: Type[BotocoreClientError]
    InvalidDBInstanceAutomatedBackupStateFault: Type[BotocoreClientError]
    InvalidDBInstanceStateFault: Type[BotocoreClientError]
    InvalidDBParameterGroupStateFault: Type[BotocoreClientError]
    InvalidDBProxyEndpointStateFault: Type[BotocoreClientError]
    InvalidDBProxyStateFault: Type[BotocoreClientError]
    InvalidDBSecurityGroupStateFault: Type[BotocoreClientError]
    InvalidDBSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBSubnetGroupFault: Type[BotocoreClientError]
    InvalidDBSubnetGroupStateFault: Type[BotocoreClientError]
    InvalidDBSubnetStateFault: Type[BotocoreClientError]
    InvalidEventSubscriptionStateFault: Type[BotocoreClientError]
    InvalidExportOnlyFault: Type[BotocoreClientError]
    InvalidExportSourceStateFault: Type[BotocoreClientError]
    InvalidExportTaskStateFault: Type[BotocoreClientError]
    InvalidGlobalClusterStateFault: Type[BotocoreClientError]
    InvalidIntegrationStateFault: Type[BotocoreClientError]
    InvalidOptionGroupStateFault: Type[BotocoreClientError]
    InvalidResourceStateFault: Type[BotocoreClientError]
    InvalidRestoreFault: Type[BotocoreClientError]
    InvalidS3BucketFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    KMSKeyNotAccessibleFault: Type[BotocoreClientError]
    NetworkTypeNotSupported: Type[BotocoreClientError]
    OptionGroupAlreadyExistsFault: Type[BotocoreClientError]
    OptionGroupNotFoundFault: Type[BotocoreClientError]
    OptionGroupQuotaExceededFault: Type[BotocoreClientError]
    PointInTimeRestoreNotEnabledFault: Type[BotocoreClientError]
    ProvisionedIopsNotAvailableInAZFault: Type[BotocoreClientError]
    ReservedDBInstanceAlreadyExistsFault: Type[BotocoreClientError]
    ReservedDBInstanceNotFoundFault: Type[BotocoreClientError]
    ReservedDBInstanceQuotaExceededFault: Type[BotocoreClientError]
    ReservedDBInstancesOfferingNotFoundFault: Type[BotocoreClientError]
    ResourceNotFoundFault: Type[BotocoreClientError]
    SNSInvalidTopicFault: Type[BotocoreClientError]
    SNSNoAuthorizationFault: Type[BotocoreClientError]
    SNSTopicArnNotFoundFault: Type[BotocoreClientError]
    SharedSnapshotQuotaExceededFault: Type[BotocoreClientError]
    SnapshotQuotaExceededFault: Type[BotocoreClientError]
    SourceClusterNotSupportedFault: Type[BotocoreClientError]
    SourceDatabaseNotSupportedFault: Type[BotocoreClientError]
    SourceNotFoundFault: Type[BotocoreClientError]
    StorageQuotaExceededFault: Type[BotocoreClientError]
    StorageTypeNotAvailableFault: Type[BotocoreClientError]
    StorageTypeNotSupportedFault: Type[BotocoreClientError]
    SubnetAlreadyInUse: Type[BotocoreClientError]
    SubscriptionAlreadyExistFault: Type[BotocoreClientError]
    SubscriptionCategoryNotFoundFault: Type[BotocoreClientError]
    SubscriptionNotFoundFault: Type[BotocoreClientError]
    TenantDatabaseAlreadyExistsFault: Type[BotocoreClientError]
    TenantDatabaseNotFoundFault: Type[BotocoreClientError]
    TenantDatabaseQuotaExceededFault: Type[BotocoreClientError]

class RDSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RDSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.exceptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#exceptions)
        """

    def add_role_to_db_cluster(
        self, *, DBClusterIdentifier: str, RoleArn: str, FeatureName: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates an Identity and Access Management (IAM) role with a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_role_to_db_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_role_to_db_cluster)
        """

    def add_role_to_db_instance(
        self, *, DBInstanceIdentifier: str, RoleArn: str, FeatureName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates an Amazon Web Services Identity and Access Management (IAM) role
        with a DB
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_role_to_db_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_role_to_db_instance)
        """

    def add_source_identifier_to_subscription(
        self, *, SubscriptionName: str, SourceIdentifier: str
    ) -> AddSourceIdentifierToSubscriptionResultTypeDef:
        """
        Adds a source identifier to an existing RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_source_identifier_to_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_source_identifier_to_subscription)
        """

    def add_tags_to_resource(
        self, *, ResourceName: str, Tags: Sequence[TagTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds metadata tags to an Amazon RDS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_tags_to_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, *, ResourceIdentifier: str, ApplyAction: str, OptInType: str
    ) -> ApplyPendingMaintenanceActionResultTypeDef:
        """
        Applies a pending maintenance action to a resource (for example, to a DB
        instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.apply_pending_maintenance_action)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#apply_pending_maintenance_action)
        """

    def authorize_db_security_group_ingress(
        self,
        *,
        DBSecurityGroupName: str,
        CIDRIP: str = ...,
        EC2SecurityGroupName: str = ...,
        EC2SecurityGroupId: str = ...,
        EC2SecurityGroupOwnerId: str = ...,
    ) -> AuthorizeDBSecurityGroupIngressResultTypeDef:
        """
        Enables ingress to a DBSecurityGroup using one of two forms of authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.authorize_db_security_group_ingress)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#authorize_db_security_group_ingress)
        """

    def backtrack_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        BacktrackTo: TimestampTypeDef,
        Force: bool = ...,
        UseEarliestTimeOnPointInTimeUnavailable: bool = ...,
    ) -> DBClusterBacktrackResponseTypeDef:
        """
        Backtracks a DB cluster to a specific time, without creating a new DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.backtrack_db_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#backtrack_db_cluster)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.can_paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#can_paginate)
        """

    def cancel_export_task(self, *, ExportTaskIdentifier: str) -> ExportTaskResponseTypeDef:
        """
        Cancels an export task in progress that is exporting a snapshot or cluster to
        Amazon
        S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.cancel_export_task)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#cancel_export_task)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.close)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#close)
        """

    def copy_db_cluster_parameter_group(
        self,
        *,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CopyDBClusterParameterGroupResultTypeDef:
        """
        Copies the specified DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_cluster_parameter_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_cluster_parameter_group)
        """

    def copy_db_cluster_snapshot(
        self,
        *,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: str = ...,
        PreSignedUrl: str = ...,
        CopyTags: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        SourceRegion: str = ...,
    ) -> CopyDBClusterSnapshotResultTypeDef:
        """
        Copies a snapshot of a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_cluster_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_cluster_snapshot)
        """

    def copy_db_parameter_group(
        self,
        *,
        SourceDBParameterGroupIdentifier: str,
        TargetDBParameterGroupIdentifier: str,
        TargetDBParameterGroupDescription: str,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CopyDBParameterGroupResultTypeDef:
        """
        Copies the specified DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_parameter_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_parameter_group)
        """

    def copy_db_snapshot(
        self,
        *,
        SourceDBSnapshotIdentifier: str,
        TargetDBSnapshotIdentifier: str,
        KmsKeyId: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        CopyTags: bool = ...,
        PreSignedUrl: str = ...,
        OptionGroupName: str = ...,
        TargetCustomAvailabilityZone: str = ...,
        CopyOptionGroup: bool = ...,
        SourceRegion: str = ...,
    ) -> CopyDBSnapshotResultTypeDef:
        """
        Copies the specified DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_snapshot)
        """

    def copy_option_group(
        self,
        *,
        SourceOptionGroupIdentifier: str,
        TargetOptionGroupIdentifier: str,
        TargetOptionGroupDescription: str,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CopyOptionGroupResultTypeDef:
        """
        Copies the specified option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_option_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_option_group)
        """

    def create_blue_green_deployment(
        self,
        *,
        BlueGreenDeploymentName: str,
        Source: str,
        TargetEngineVersion: str = ...,
        TargetDBParameterGroupName: str = ...,
        TargetDBClusterParameterGroupName: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        TargetDBInstanceClass: str = ...,
        UpgradeTargetStorageConfig: bool = ...,
    ) -> CreateBlueGreenDeploymentResponseTypeDef:
        """
        Creates a blue/green deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_blue_green_deployment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_blue_green_deployment)
        """

    def create_custom_db_engine_version(
        self,
        *,
        Engine: str,
        EngineVersion: str,
        DatabaseInstallationFilesS3BucketName: str = ...,
        DatabaseInstallationFilesS3Prefix: str = ...,
        ImageId: str = ...,
        KMSKeyId: str = ...,
        Description: str = ...,
        Manifest: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        SourceCustomDbEngineVersionIdentifier: str = ...,
        UseAwsProvidedLatestImage: bool = ...,
    ) -> DBEngineVersionResponseTypeDef:
        """
        Creates a custom DB engine version (CEV).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_custom_db_engine_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_custom_db_engine_version)
        """

    def create_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        Engine: str,
        AvailabilityZones: Sequence[str] = ...,
        BackupRetentionPeriod: int = ...,
        CharacterSetName: str = ...,
        DatabaseName: str = ...,
        DBClusterParameterGroupName: str = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        DBSubnetGroupName: str = ...,
        EngineVersion: str = ...,
        Port: int = ...,
        MasterUsername: str = ...,
        MasterUserPassword: str = ...,
        OptionGroupName: str = ...,
        PreferredBackupWindow: str = ...,
        PreferredMaintenanceWindow: str = ...,
        ReplicationSourceIdentifier: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        StorageEncrypted: bool = ...,
        KmsKeyId: str = ...,
        PreSignedUrl: str = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        BacktrackWindow: int = ...,
        EnableCloudwatchLogsExports: Sequence[str] = ...,
        EngineMode: str = ...,
        ScalingConfiguration: ScalingConfigurationTypeDef = ...,
        RdsCustomClusterConfiguration: RdsCustomClusterConfigurationTypeDef = ...,
        DeletionProtection: bool = ...,
        GlobalClusterIdentifier: str = ...,
        EnableHttpEndpoint: bool = ...,
        CopyTagsToSnapshot: bool = ...,
        Domain: str = ...,
        DomainIAMRoleName: str = ...,
        EnableGlobalWriteForwarding: bool = ...,
        DBClusterInstanceClass: str = ...,
        AllocatedStorage: int = ...,
        StorageType: str = ...,
        Iops: int = ...,
        PubliclyAccessible: bool = ...,
        AutoMinorVersionUpgrade: bool = ...,
        MonitoringInterval: int = ...,
        MonitoringRoleArn: str = ...,
        EnablePerformanceInsights: bool = ...,
        PerformanceInsightsKMSKeyId: str = ...,
        PerformanceInsightsRetentionPeriod: int = ...,
        ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfigurationTypeDef = ...,
        NetworkType: str = ...,
        DBSystemId: str = ...,
        ManageMasterUserPassword: bool = ...,
        MasterUserSecretKmsKeyId: str = ...,
        EnableLocalWriteForwarding: bool = ...,
        SourceRegion: str = ...,
    ) -> CreateDBClusterResultTypeDef:
        """
        Creates a new Amazon Aurora DB cluster or Multi-AZ DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster)
        """

    def create_db_cluster_endpoint(
        self,
        *,
        DBClusterIdentifier: str,
        DBClusterEndpointIdentifier: str,
        EndpointType: str,
        StaticMembers: Sequence[str] = ...,
        ExcludedMembers: Sequence[str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> DBClusterEndpointResponseTypeDef:
        """
        Creates a new custom endpoint and associates it with an Amazon Aurora DB
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster_endpoint)
        """

    def create_db_cluster_parameter_group(
        self,
        *,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDBClusterParameterGroupResultTypeDef:
        """
        Creates a new DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster_parameter_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster_parameter_group)
        """

    def create_db_cluster_snapshot(
        self,
        *,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDBClusterSnapshotResultTypeDef:
        """
        Creates a snapshot of a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster_snapshot)
        """

    def create_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBName: str = ...,
        AllocatedStorage: int = ...,
        MasterUsername: str = ...,
        MasterUserPassword: str = ...,
        DBSecurityGroups: Sequence[str] = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        AvailabilityZone: str = ...,
        DBSubnetGroupName: str = ...,
        PreferredMaintenanceWindow: str = ...,
        DBParameterGroupName: str = ...,
        BackupRetentionPeriod: int = ...,
        PreferredBackupWindow: str = ...,
        Port: int = ...,
        MultiAZ: bool = ...,
        EngineVersion: str = ...,
        AutoMinorVersionUpgrade: bool = ...,
        LicenseModel: str = ...,
        Iops: int = ...,
        OptionGroupName: str = ...,
        CharacterSetName: str = ...,
        NcharCharacterSetName: str = ...,
        PubliclyAccessible: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        DBClusterIdentifier: str = ...,
        StorageType: str = ...,
        TdeCredentialArn: str = ...,
        TdeCredentialPassword: str = ...,
        StorageEncrypted: bool = ...,
        KmsKeyId: str = ...,
        Domain: str = ...,
        DomainFqdn: str = ...,
        DomainOu: str = ...,
        DomainAuthSecretArn: str = ...,
        DomainDnsIps: Sequence[str] = ...,
        CopyTagsToSnapshot: bool = ...,
        MonitoringInterval: int = ...,
        MonitoringRoleArn: str = ...,
        DomainIAMRoleName: str = ...,
        PromotionTier: int = ...,
        Timezone: str = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        EnablePerformanceInsights: bool = ...,
        PerformanceInsightsKMSKeyId: str = ...,
        PerformanceInsightsRetentionPeriod: int = ...,
        EnableCloudwatchLogsExports: Sequence[str] = ...,
        ProcessorFeatures: Sequence[ProcessorFeatureTypeDef] = ...,
        DeletionProtection: bool = ...,
        MaxAllocatedStorage: int = ...,
        EnableCustomerOwnedIp: bool = ...,
        CustomIamInstanceProfile: str = ...,
        BackupTarget: str = ...,
        NetworkType: str = ...,
        StorageThroughput: int = ...,
        ManageMasterUserPassword: bool = ...,
        MasterUserSecretKmsKeyId: str = ...,
        CACertificateIdentifier: str = ...,
        DBSystemId: str = ...,
        DedicatedLogVolume: bool = ...,
        MultiTenant: bool = ...,
    ) -> CreateDBInstanceResultTypeDef:
        """
        Creates a new DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_instance)
        """

    def create_db_instance_read_replica(
        self,
        *,
        DBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str = ...,
        DBInstanceClass: str = ...,
        AvailabilityZone: str = ...,
        Port: int = ...,
        MultiAZ: bool = ...,
        AutoMinorVersionUpgrade: bool = ...,
        Iops: int = ...,
        OptionGroupName: str = ...,
        DBParameterGroupName: str = ...,
        PubliclyAccessible: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        DBSubnetGroupName: str = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        StorageType: str = ...,
        CopyTagsToSnapshot: bool = ...,
        MonitoringInterval: int = ...,
        MonitoringRoleArn: str = ...,
        KmsKeyId: str = ...,
        PreSignedUrl: str = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        EnablePerformanceInsights: bool = ...,
        PerformanceInsightsKMSKeyId: str = ...,
        PerformanceInsightsRetentionPeriod: int = ...,
        EnableCloudwatchLogsExports: Sequence[str] = ...,
        ProcessorFeatures: Sequence[ProcessorFeatureTypeDef] = ...,
        UseDefaultProcessorFeatures: bool = ...,
        DeletionProtection: bool = ...,
        Domain: str = ...,
        DomainIAMRoleName: str = ...,
        DomainFqdn: str = ...,
        DomainOu: str = ...,
        DomainAuthSecretArn: str = ...,
        DomainDnsIps: Sequence[str] = ...,
        ReplicaMode: ReplicaModeType = ...,
        MaxAllocatedStorage: int = ...,
        CustomIamInstanceProfile: str = ...,
        NetworkType: str = ...,
        StorageThroughput: int = ...,
        EnableCustomerOwnedIp: bool = ...,
        AllocatedStorage: int = ...,
        SourceDBClusterIdentifier: str = ...,
        DedicatedLogVolume: bool = ...,
        UpgradeStorageConfig: bool = ...,
        SourceRegion: str = ...,
    ) -> CreateDBInstanceReadReplicaResultTypeDef:
        """
        Creates a new DB instance that acts as a read replica for an existing source DB
        instance or Multi-AZ DB
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_instance_read_replica)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_instance_read_replica)
        """

    def create_db_parameter_group(
        self,
        *,
        DBParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDBParameterGroupResultTypeDef:
        """
        Creates a new DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_parameter_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_parameter_group)
        """

    def create_db_proxy(
        self,
        *,
        DBProxyName: str,
        EngineFamily: EngineFamilyType,
        Auth: Sequence[UserAuthConfigTypeDef],
        RoleArn: str,
        VpcSubnetIds: Sequence[str],
        VpcSecurityGroupIds: Sequence[str] = ...,
        RequireTLS: bool = ...,
        IdleClientTimeout: int = ...,
        DebugLogging: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDBProxyResponseTypeDef:
        """
        Creates a new DB proxy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_proxy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_proxy)
        """

    def create_db_proxy_endpoint(
        self,
        *,
        DBProxyName: str,
        DBProxyEndpointName: str,
        VpcSubnetIds: Sequence[str],
        VpcSecurityGroupIds: Sequence[str] = ...,
        TargetRole: DBProxyEndpointTargetRoleType = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDBProxyEndpointResponseTypeDef:
        """
        Creates a `DBProxyEndpoint`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_proxy_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_proxy_endpoint)
        """

    def create_db_security_group(
        self,
        *,
        DBSecurityGroupName: str,
        DBSecurityGroupDescription: str,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDBSecurityGroupResultTypeDef:
        """
        Creates a new DB security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_security_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_security_group)
        """

    def create_db_snapshot(
        self,
        *,
        DBSnapshotIdentifier: str,
        DBInstanceIdentifier: str,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDBSnapshotResultTypeDef:
        """
        Creates a snapshot of a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_snapshot)
        """

    def create_db_subnet_group(
        self,
        *,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: Sequence[str],
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDBSubnetGroupResultTypeDef:
        """
        Creates a new DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_subnet_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_subnet_group)
        """

    def create_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = ...,
        EventCategories: Sequence[str] = ...,
        SourceIds: Sequence[str] = ...,
        Enabled: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        Creates an RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_event_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_event_subscription)
        """

    def create_global_cluster(
        self,
        *,
        GlobalClusterIdentifier: str = ...,
        SourceDBClusterIdentifier: str = ...,
        Engine: str = ...,
        EngineVersion: str = ...,
        DeletionProtection: bool = ...,
        DatabaseName: str = ...,
        StorageEncrypted: bool = ...,
    ) -> CreateGlobalClusterResultTypeDef:
        """
        Creates an Aurora global database spread across multiple Amazon Web Services
        Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_global_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_global_cluster)
        """

    def create_integration(
        self,
        *,
        SourceArn: str,
        TargetArn: str,
        IntegrationName: str,
        KMSKeyId: str = ...,
        AdditionalEncryptionContext: Mapping[str, str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> IntegrationResponseTypeDef:
        """
        Creates a zero-ETL integration with Amazon Redshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_integration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_integration)
        """

    def create_option_group(
        self,
        *,
        OptionGroupName: str,
        EngineName: str,
        MajorEngineVersion: str,
        OptionGroupDescription: str,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateOptionGroupResultTypeDef:
        """
        Creates a new option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_option_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_option_group)
        """

    def create_tenant_database(
        self,
        *,
        DBInstanceIdentifier: str,
        TenantDBName: str,
        MasterUsername: str,
        MasterUserPassword: str,
        CharacterSetName: str = ...,
        NcharCharacterSetName: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateTenantDatabaseResultTypeDef:
        """
        Creates a tenant database in a DB instance that uses the multi-tenant
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_tenant_database)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_tenant_database)
        """

    def delete_blue_green_deployment(
        self, *, BlueGreenDeploymentIdentifier: str, DeleteTarget: bool = ...
    ) -> DeleteBlueGreenDeploymentResponseTypeDef:
        """
        Deletes a blue/green deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_blue_green_deployment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_blue_green_deployment)
        """

    def delete_custom_db_engine_version(
        self, *, Engine: str, EngineVersion: str
    ) -> DBEngineVersionResponseTypeDef:
        """
        Deletes a custom engine version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_custom_db_engine_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_custom_db_engine_version)
        """

    def delete_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = ...,
        FinalDBSnapshotIdentifier: str = ...,
        DeleteAutomatedBackups: bool = ...,
    ) -> DeleteDBClusterResultTypeDef:
        """
        The DeleteDBCluster action deletes a previously provisioned DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster)
        """

    def delete_db_cluster_automated_backup(
        self, *, DbClusterResourceId: str
    ) -> DeleteDBClusterAutomatedBackupResultTypeDef:
        """
        Deletes automated backups using the `DbClusterResourceId` value of the source
        DB cluster or the Amazon Resource Name (ARN) of the automated
        backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster_automated_backup)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_automated_backup)
        """

    def delete_db_cluster_endpoint(
        self, *, DBClusterEndpointIdentifier: str
    ) -> DBClusterEndpointResponseTypeDef:
        """
        Deletes a custom endpoint and removes it from an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_endpoint)
        """

    def delete_db_cluster_parameter_group(
        self, *, DBClusterParameterGroupName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specified DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster_parameter_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_parameter_group)
        """

    def delete_db_cluster_snapshot(
        self, *, DBClusterSnapshotIdentifier: str
    ) -> DeleteDBClusterSnapshotResultTypeDef:
        """
        Deletes a DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_snapshot)
        """

    def delete_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        SkipFinalSnapshot: bool = ...,
        FinalDBSnapshotIdentifier: str = ...,
        DeleteAutomatedBackups: bool = ...,
    ) -> DeleteDBInstanceResultTypeDef:
        """
        Deletes a previously provisioned DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_instance)
        """

    def delete_db_instance_automated_backup(
        self, *, DbiResourceId: str = ..., DBInstanceAutomatedBackupsArn: str = ...
    ) -> DeleteDBInstanceAutomatedBackupResultTypeDef:
        """
        Deletes automated backups using the `DbiResourceId` value of the source DB
        instance or the Amazon Resource Name (ARN) of the automated
        backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_instance_automated_backup)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_instance_automated_backup)
        """

    def delete_db_parameter_group(
        self, *, DBParameterGroupName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specified DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_parameter_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_parameter_group)
        """

    def delete_db_proxy(self, *, DBProxyName: str) -> DeleteDBProxyResponseTypeDef:
        """
        Deletes an existing DB proxy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_proxy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_proxy)
        """

    def delete_db_proxy_endpoint(
        self, *, DBProxyEndpointName: str
    ) -> DeleteDBProxyEndpointResponseTypeDef:
        """
        Deletes a `DBProxyEndpoint`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_proxy_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_proxy_endpoint)
        """

    def delete_db_security_group(self, *, DBSecurityGroupName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a DB security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_security_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_security_group)
        """

    def delete_db_snapshot(self, *, DBSnapshotIdentifier: str) -> DeleteDBSnapshotResultTypeDef:
        """
        Deletes a DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_snapshot)
        """

    def delete_db_subnet_group(self, *, DBSubnetGroupName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_subnet_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_subnet_group)
        """

    def delete_event_subscription(
        self, *, SubscriptionName: str
    ) -> DeleteEventSubscriptionResultTypeDef:
        """
        Deletes an RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_event_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_event_subscription)
        """

    def delete_global_cluster(
        self, *, GlobalClusterIdentifier: str
    ) -> DeleteGlobalClusterResultTypeDef:
        """
        Deletes a global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_global_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_global_cluster)
        """

    def delete_integration(self, *, IntegrationIdentifier: str) -> IntegrationResponseTypeDef:
        """
        Deletes a zero-ETL integration with Amazon Redshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_integration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_integration)
        """

    def delete_option_group(self, *, OptionGroupName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_option_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_option_group)
        """

    def delete_tenant_database(
        self,
        *,
        DBInstanceIdentifier: str,
        TenantDBName: str,
        SkipFinalSnapshot: bool = ...,
        FinalDBSnapshotIdentifier: str = ...,
    ) -> DeleteTenantDatabaseResultTypeDef:
        """
        Deletes a tenant database from your DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_tenant_database)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_tenant_database)
        """

    def deregister_db_proxy_targets(
        self,
        *,
        DBProxyName: str,
        TargetGroupName: str = ...,
        DBInstanceIdentifiers: Sequence[str] = ...,
        DBClusterIdentifiers: Sequence[str] = ...,
    ) -> Dict[str, Any]:
        """
        Remove the association between one or more `DBProxyTarget` data structures and
        a
        `DBProxyTargetGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.deregister_db_proxy_targets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#deregister_db_proxy_targets)
        """

    def describe_account_attributes(self) -> AccountAttributesMessageTypeDef:
        """
        Lists all of the attributes for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_account_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_account_attributes)
        """

    def describe_blue_green_deployments(
        self,
        *,
        BlueGreenDeploymentIdentifier: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribeBlueGreenDeploymentsResponseTypeDef:
        """
        Describes one or more blue/green deployments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_blue_green_deployments)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_blue_green_deployments)
        """

    def describe_certificates(
        self,
        *,
        CertificateIdentifier: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> CertificateMessageTypeDef:
        """
        Lists the set of certificate authority (CA) certificates provided by Amazon RDS
        for this Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_certificates)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_certificates)
        """

    def describe_db_cluster_automated_backups(
        self,
        *,
        DbClusterResourceId: str = ...,
        DBClusterIdentifier: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DBClusterAutomatedBackupMessageTypeDef:
        """
        Displays backups for both current and deleted DB clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_automated_backups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_automated_backups)
        """

    def describe_db_cluster_backtracks(
        self,
        *,
        DBClusterIdentifier: str,
        BacktrackIdentifier: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DBClusterBacktrackMessageTypeDef:
        """
        Returns information about backtracks for a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_backtracks)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_backtracks)
        """

    def describe_db_cluster_endpoints(
        self,
        *,
        DBClusterIdentifier: str = ...,
        DBClusterEndpointIdentifier: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DBClusterEndpointMessageTypeDef:
        """
        Returns information about endpoints for an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_endpoints)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_endpoints)
        """

    def describe_db_cluster_parameter_groups(
        self,
        *,
        DBClusterParameterGroupName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DBClusterParameterGroupsMessageTypeDef:
        """
        Returns a list of `DBClusterParameterGroup` descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_parameter_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_parameter_groups)
        """

    def describe_db_cluster_parameters(
        self,
        *,
        DBClusterParameterGroupName: str,
        Source: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DBClusterParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_parameters)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_parameters)
        """

    def describe_db_cluster_snapshot_attributes(
        self, *, DBClusterSnapshotIdentifier: str
    ) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
        """
        Returns a list of DB cluster snapshot attribute names and values for a manual
        DB cluster
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshot_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_snapshot_attributes)
        """

    def describe_db_cluster_snapshots(
        self,
        *,
        DBClusterIdentifier: str = ...,
        DBClusterSnapshotIdentifier: str = ...,
        SnapshotType: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
        IncludeShared: bool = ...,
        IncludePublic: bool = ...,
        DbClusterResourceId: str = ...,
    ) -> DBClusterSnapshotMessageTypeDef:
        """
        Returns information about DB cluster snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshots)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_snapshots)
        """

    def describe_db_clusters(
        self,
        *,
        DBClusterIdentifier: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
        IncludeShared: bool = ...,
    ) -> DBClusterMessageTypeDef:
        """
        Describes existing Amazon Aurora DB clusters and Multi-AZ DB clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_clusters)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_clusters)
        """

    def describe_db_engine_versions(
        self,
        *,
        Engine: str = ...,
        EngineVersion: str = ...,
        DBParameterGroupFamily: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
        DefaultOnly: bool = ...,
        ListSupportedCharacterSets: bool = ...,
        ListSupportedTimezones: bool = ...,
        IncludeAll: bool = ...,
    ) -> DBEngineVersionMessageTypeDef:
        """
        Describes the properties of specific versions of DB engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_engine_versions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_engine_versions)
        """

    def describe_db_instance_automated_backups(
        self,
        *,
        DbiResourceId: str = ...,
        DBInstanceIdentifier: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
        DBInstanceAutomatedBackupsArn: str = ...,
    ) -> DBInstanceAutomatedBackupMessageTypeDef:
        """
        Displays backups for both current and deleted instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_instance_automated_backups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_instance_automated_backups)
        """

    def describe_db_instances(
        self,
        *,
        DBInstanceIdentifier: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DBInstanceMessageTypeDef:
        """
        Describes provisioned RDS instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_instances)
        """

    def describe_db_log_files(
        self,
        *,
        DBInstanceIdentifier: str,
        FilenameContains: str = ...,
        FileLastWritten: int = ...,
        FileSize: int = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DescribeDBLogFilesResponseTypeDef:
        """
        Returns a list of DB log files for the DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_log_files)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_log_files)
        """

    def describe_db_parameter_groups(
        self,
        *,
        DBParameterGroupName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DBParameterGroupsMessageTypeDef:
        """
        Returns a list of `DBParameterGroup` descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_parameter_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_parameter_groups)
        """

    def describe_db_parameters(
        self,
        *,
        DBParameterGroupName: str,
        Source: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DBParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_parameters)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_parameters)
        """

    def describe_db_proxies(
        self,
        *,
        DBProxyName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribeDBProxiesResponseTypeDef:
        """
        Returns information about DB proxies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxies)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxies)
        """

    def describe_db_proxy_endpoints(
        self,
        *,
        DBProxyName: str = ...,
        DBProxyEndpointName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribeDBProxyEndpointsResponseTypeDef:
        """
        Returns information about DB proxy endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxy_endpoints)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxy_endpoints)
        """

    def describe_db_proxy_target_groups(
        self,
        *,
        DBProxyName: str,
        TargetGroupName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribeDBProxyTargetGroupsResponseTypeDef:
        """
        Returns information about DB proxy target groups, represented by
        `DBProxyTargetGroup` data
        structures.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxy_target_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxy_target_groups)
        """

    def describe_db_proxy_targets(
        self,
        *,
        DBProxyName: str,
        TargetGroupName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribeDBProxyTargetsResponseTypeDef:
        """
        Returns information about `DBProxyTarget` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxy_targets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxy_targets)
        """

    def describe_db_recommendations(
        self,
        *,
        LastUpdatedAfter: TimestampTypeDef = ...,
        LastUpdatedBefore: TimestampTypeDef = ...,
        Locale: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DBRecommendationsMessageTypeDef:
        """
        Describes the recommendations to resolve the issues for your DB instances, DB
        clusters, and DB parameter
        groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_recommendations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_recommendations)
        """

    def describe_db_security_groups(
        self,
        *,
        DBSecurityGroupName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DBSecurityGroupMessageTypeDef:
        """
        Returns a list of `DBSecurityGroup` descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_security_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_security_groups)
        """

    def describe_db_snapshot_attributes(
        self, *, DBSnapshotIdentifier: str
    ) -> DescribeDBSnapshotAttributesResultTypeDef:
        """
        Returns a list of DB snapshot attribute names and values for a manual DB
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_snapshot_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_snapshot_attributes)
        """

    def describe_db_snapshot_tenant_databases(
        self,
        *,
        DBInstanceIdentifier: str = ...,
        DBSnapshotIdentifier: str = ...,
        SnapshotType: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
        DbiResourceId: str = ...,
    ) -> DBSnapshotTenantDatabasesMessageTypeDef:
        """
        Describes the tenant databases that exist in a DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_snapshot_tenant_databases)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_snapshot_tenant_databases)
        """

    def describe_db_snapshots(
        self,
        *,
        DBInstanceIdentifier: str = ...,
        DBSnapshotIdentifier: str = ...,
        SnapshotType: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
        IncludeShared: bool = ...,
        IncludePublic: bool = ...,
        DbiResourceId: str = ...,
    ) -> DBSnapshotMessageTypeDef:
        """
        Returns information about DB snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_snapshots)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_snapshots)
        """

    def describe_db_subnet_groups(
        self,
        *,
        DBSubnetGroupName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DBSubnetGroupMessageTypeDef:
        """
        Returns a list of DBSubnetGroup descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_subnet_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_subnet_groups)
        """

    def describe_engine_default_cluster_parameters(
        self,
        *,
        DBParameterGroupFamily: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DescribeEngineDefaultClusterParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the cluster
        database
        engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_engine_default_cluster_parameters)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_engine_default_cluster_parameters)
        """

    def describe_engine_default_parameters(
        self,
        *,
        DBParameterGroupFamily: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DescribeEngineDefaultParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the specified
        database
        engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_engine_default_parameters)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_engine_default_parameters)
        """

    def describe_event_categories(
        self, *, SourceType: str = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> EventCategoriesMessageTypeDef:
        """
        Displays a list of categories for all event source types, or, if specified, for
        a specified source
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_event_categories)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_event_categories)
        """

    def describe_event_subscriptions(
        self,
        *,
        SubscriptionName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> EventSubscriptionsMessageTypeDef:
        """
        Lists all the subscription descriptions for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_event_subscriptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_event_subscriptions)
        """

    def describe_events(
        self,
        *,
        SourceIdentifier: str = ...,
        SourceType: SourceTypeType = ...,
        StartTime: TimestampTypeDef = ...,
        EndTime: TimestampTypeDef = ...,
        Duration: int = ...,
        EventCategories: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> EventsMessageTypeDef:
        """
        Returns events related to DB instances, DB clusters, DB parameter groups, DB
        security groups, DB snapshots, DB cluster snapshots, and RDS Proxies for the
        past 14
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_events)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_events)
        """

    def describe_export_tasks(
        self,
        *,
        ExportTaskIdentifier: str = ...,
        SourceArn: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
        SourceType: ExportSourceTypeType = ...,
    ) -> ExportTasksMessageTypeDef:
        """
        Returns information about a snapshot or cluster export to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_export_tasks)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_export_tasks)
        """

    def describe_global_clusters(
        self,
        *,
        GlobalClusterIdentifier: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> GlobalClustersMessageTypeDef:
        """
        Returns information about Aurora global database clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_global_clusters)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_global_clusters)
        """

    def describe_integrations(
        self,
        *,
        IntegrationIdentifier: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DescribeIntegrationsResponseTypeDef:
        """
        Describe one or more zero-ETL integrations with Amazon Redshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_integrations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_integrations)
        """

    def describe_option_group_options(
        self,
        *,
        EngineName: str,
        MajorEngineVersion: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> OptionGroupOptionsMessageTypeDef:
        """
        Describes all available options for the specified engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_option_group_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_option_group_options)
        """

    def describe_option_groups(
        self,
        *,
        OptionGroupName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
        EngineName: str = ...,
        MajorEngineVersion: str = ...,
    ) -> OptionGroupsTypeDef:
        """
        Describes the available option groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_option_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_option_groups)
        """

    def describe_orderable_db_instance_options(
        self,
        *,
        Engine: str,
        EngineVersion: str = ...,
        DBInstanceClass: str = ...,
        LicenseModel: str = ...,
        AvailabilityZoneGroup: str = ...,
        Vpc: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> OrderableDBInstanceOptionsMessageTypeDef:
        """
        Describes the orderable DB instance options for a specified DB engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_orderable_db_instance_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_orderable_db_instance_options)
        """

    def describe_pending_maintenance_actions(
        self,
        *,
        ResourceIdentifier: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> PendingMaintenanceActionsMessageTypeDef:
        """
        Returns a list of resources (for example, DB instances) that have at least one
        pending maintenance
        action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_pending_maintenance_actions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_pending_maintenance_actions)
        """

    def describe_reserved_db_instances(
        self,
        *,
        ReservedDBInstanceId: str = ...,
        ReservedDBInstancesOfferingId: str = ...,
        DBInstanceClass: str = ...,
        Duration: str = ...,
        ProductDescription: str = ...,
        OfferingType: str = ...,
        MultiAZ: bool = ...,
        LeaseId: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> ReservedDBInstanceMessageTypeDef:
        """
        Returns information about reserved DB instances for this account, or about a
        specified reserved DB
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_reserved_db_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_reserved_db_instances)
        """

    def describe_reserved_db_instances_offerings(
        self,
        *,
        ReservedDBInstancesOfferingId: str = ...,
        DBInstanceClass: str = ...,
        Duration: str = ...,
        ProductDescription: str = ...,
        OfferingType: str = ...,
        MultiAZ: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> ReservedDBInstancesOfferingMessageTypeDef:
        """
        Lists available reserved DB instance offerings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_reserved_db_instances_offerings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_reserved_db_instances_offerings)
        """

    def describe_source_regions(
        self,
        *,
        RegionName: str = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> SourceRegionMessageTypeDef:
        """
        Returns a list of the source Amazon Web Services Regions where the current
        Amazon Web Services Region can create a read replica, copy a DB snapshot from,
        or replicate automated backups
        from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_source_regions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_source_regions)
        """

    def describe_tenant_databases(
        self,
        *,
        DBInstanceIdentifier: str = ...,
        TenantDBName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> TenantDatabasesMessageTypeDef:
        """
        Describes the tenant databases in a DB instance that uses the multi-tenant
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_tenant_databases)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_tenant_databases)
        """

    def describe_valid_db_instance_modifications(
        self, *, DBInstanceIdentifier: str
    ) -> DescribeValidDBInstanceModificationsResultTypeDef:
        """
        You can call `DescribeValidDBInstanceModifications` to learn what modifications
        you can make to your DB
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_valid_db_instance_modifications)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_valid_db_instance_modifications)
        """

    def disable_http_endpoint(self, *, ResourceArn: str) -> DisableHttpEndpointResponseTypeDef:
        """
        Disables the HTTP endpoint for the specified DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.disable_http_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#disable_http_endpoint)
        """

    def download_db_log_file_portion(
        self,
        *,
        DBInstanceIdentifier: str,
        LogFileName: str,
        Marker: str = ...,
        NumberOfLines: int = ...,
    ) -> DownloadDBLogFilePortionDetailsTypeDef:
        """
        Downloads all or a portion of the specified log file, up to 1 MB in size.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.download_db_log_file_portion)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#download_db_log_file_portion)
        """

    def enable_http_endpoint(self, *, ResourceArn: str) -> EnableHttpEndpointResponseTypeDef:
        """
        Enables the HTTP endpoint for the DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.enable_http_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#enable_http_endpoint)
        """

    def failover_db_cluster(
        self, *, DBClusterIdentifier: str, TargetDBInstanceIdentifier: str = ...
    ) -> FailoverDBClusterResultTypeDef:
        """
        Forces a failover for a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.failover_db_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#failover_db_cluster)
        """

    def failover_global_cluster(
        self,
        *,
        GlobalClusterIdentifier: str,
        TargetDbClusterIdentifier: str,
        AllowDataLoss: bool = ...,
        Switchover: bool = ...,
    ) -> FailoverGlobalClusterResultTypeDef:
        """
        Promotes the specified secondary DB cluster to be the primary DB cluster in the
        global database cluster to fail over or switch over a global
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.failover_global_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#failover_global_cluster)
        """

    def generate_db_auth_token(
        self, DBHostname: str, Port: int, DBUsername: str, Region: Optional[str] = ...
    ) -> str:
        """
        Generates an auth token used to connect to a db with IAM credentials.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.generate_db_auth_token)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#generate_db_auth_token)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#generate_presigned_url)
        """

    def list_tags_for_resource(
        self, *, ResourceName: str, Filters: Sequence[FilterTypeDef] = ...
    ) -> TagListMessageTypeDef:
        """
        Lists all tags on an Amazon RDS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#list_tags_for_resource)
        """

    def modify_activity_stream(
        self, *, ResourceArn: str = ..., AuditPolicyState: AuditPolicyStateType = ...
    ) -> ModifyActivityStreamResponseTypeDef:
        """
        Changes the audit policy state of a database activity stream to either locked
        (default) or
        unlocked.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_activity_stream)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_activity_stream)
        """

    def modify_certificates(
        self, *, CertificateIdentifier: str = ..., RemoveCustomerOverride: bool = ...
    ) -> ModifyCertificatesResultTypeDef:
        """
        Override the system-default Secure Sockets Layer/Transport Layer Security
        (SSL/TLS) certificate for Amazon RDS for new DB instances, or remove the
        override.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_certificates)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_certificates)
        """

    def modify_current_db_cluster_capacity(
        self,
        *,
        DBClusterIdentifier: str,
        Capacity: int = ...,
        SecondsBeforeTimeout: int = ...,
        TimeoutAction: str = ...,
    ) -> DBClusterCapacityInfoTypeDef:
        """
        Set the capacity of an Aurora Serverless v1 DB cluster to a specific value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_current_db_cluster_capacity)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_current_db_cluster_capacity)
        """

    def modify_custom_db_engine_version(
        self,
        *,
        Engine: str,
        EngineVersion: str,
        Description: str = ...,
        Status: CustomEngineVersionStatusType = ...,
    ) -> DBEngineVersionResponseTypeDef:
        """
        Modifies the status of a custom engine version (CEV).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_custom_db_engine_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_custom_db_engine_version)
        """

    def modify_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: str = ...,
        ApplyImmediately: bool = ...,
        BackupRetentionPeriod: int = ...,
        DBClusterParameterGroupName: str = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        Port: int = ...,
        MasterUserPassword: str = ...,
        OptionGroupName: str = ...,
        PreferredBackupWindow: str = ...,
        PreferredMaintenanceWindow: str = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        BacktrackWindow: int = ...,
        CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = ...,
        EngineVersion: str = ...,
        AllowMajorVersionUpgrade: bool = ...,
        DBInstanceParameterGroupName: str = ...,
        Domain: str = ...,
        DomainIAMRoleName: str = ...,
        ScalingConfiguration: ScalingConfigurationTypeDef = ...,
        DeletionProtection: bool = ...,
        EnableHttpEndpoint: bool = ...,
        CopyTagsToSnapshot: bool = ...,
        EnableGlobalWriteForwarding: bool = ...,
        DBClusterInstanceClass: str = ...,
        AllocatedStorage: int = ...,
        StorageType: str = ...,
        Iops: int = ...,
        AutoMinorVersionUpgrade: bool = ...,
        MonitoringInterval: int = ...,
        MonitoringRoleArn: str = ...,
        EnablePerformanceInsights: bool = ...,
        PerformanceInsightsKMSKeyId: str = ...,
        PerformanceInsightsRetentionPeriod: int = ...,
        ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfigurationTypeDef = ...,
        NetworkType: str = ...,
        ManageMasterUserPassword: bool = ...,
        RotateMasterUserPassword: bool = ...,
        MasterUserSecretKmsKeyId: str = ...,
        EngineMode: str = ...,
        AllowEngineModeChange: bool = ...,
        EnableLocalWriteForwarding: bool = ...,
        AwsBackupRecoveryPointArn: str = ...,
    ) -> ModifyDBClusterResultTypeDef:
        """
        Modifies the settings of an Amazon Aurora DB cluster or a Multi-AZ DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster)
        """

    def modify_db_cluster_endpoint(
        self,
        *,
        DBClusterEndpointIdentifier: str,
        EndpointType: str = ...,
        StaticMembers: Sequence[str] = ...,
        ExcludedMembers: Sequence[str] = ...,
    ) -> DBClusterEndpointResponseTypeDef:
        """
        Modifies the properties of an endpoint in an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster_endpoint)
        """

    def modify_db_cluster_parameter_group(
        self, *, DBClusterParameterGroupName: str, Parameters: Sequence[ParameterTypeDef]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster_parameter_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster_parameter_group)
        """

    def modify_db_cluster_snapshot_attribute(
        self,
        *,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: Sequence[str] = ...,
        ValuesToRemove: Sequence[str] = ...,
    ) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
        """
        Adds an attribute and values to, or removes an attribute and values from, a
        manual DB cluster
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster_snapshot_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster_snapshot_attribute)
        """

    def modify_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        AllocatedStorage: int = ...,
        DBInstanceClass: str = ...,
        DBSubnetGroupName: str = ...,
        DBSecurityGroups: Sequence[str] = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        ApplyImmediately: bool = ...,
        MasterUserPassword: str = ...,
        DBParameterGroupName: str = ...,
        BackupRetentionPeriod: int = ...,
        PreferredBackupWindow: str = ...,
        PreferredMaintenanceWindow: str = ...,
        MultiAZ: bool = ...,
        EngineVersion: str = ...,
        AllowMajorVersionUpgrade: bool = ...,
        AutoMinorVersionUpgrade: bool = ...,
        LicenseModel: str = ...,
        Iops: int = ...,
        OptionGroupName: str = ...,
        NewDBInstanceIdentifier: str = ...,
        StorageType: str = ...,
        TdeCredentialArn: str = ...,
        TdeCredentialPassword: str = ...,
        CACertificateIdentifier: str = ...,
        Domain: str = ...,
        DomainFqdn: str = ...,
        DomainOu: str = ...,
        DomainAuthSecretArn: str = ...,
        DomainDnsIps: Sequence[str] = ...,
        CopyTagsToSnapshot: bool = ...,
        MonitoringInterval: int = ...,
        DBPortNumber: int = ...,
        PubliclyAccessible: bool = ...,
        MonitoringRoleArn: str = ...,
        DomainIAMRoleName: str = ...,
        DisableDomain: bool = ...,
        PromotionTier: int = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        EnablePerformanceInsights: bool = ...,
        PerformanceInsightsKMSKeyId: str = ...,
        PerformanceInsightsRetentionPeriod: int = ...,
        CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = ...,
        ProcessorFeatures: Sequence[ProcessorFeatureTypeDef] = ...,
        UseDefaultProcessorFeatures: bool = ...,
        DeletionProtection: bool = ...,
        MaxAllocatedStorage: int = ...,
        CertificateRotationRestart: bool = ...,
        ReplicaMode: ReplicaModeType = ...,
        EnableCustomerOwnedIp: bool = ...,
        AwsBackupRecoveryPointArn: str = ...,
        AutomationMode: AutomationModeType = ...,
        ResumeFullAutomationModeMinutes: int = ...,
        NetworkType: str = ...,
        StorageThroughput: int = ...,
        ManageMasterUserPassword: bool = ...,
        RotateMasterUserPassword: bool = ...,
        MasterUserSecretKmsKeyId: str = ...,
        Engine: str = ...,
        DedicatedLogVolume: bool = ...,
        MultiTenant: bool = ...,
    ) -> ModifyDBInstanceResultTypeDef:
        """
        Modifies settings for a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_instance)
        """

    def modify_db_parameter_group(
        self, *, DBParameterGroupName: str, Parameters: Sequence[ParameterTypeDef]
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_parameter_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_parameter_group)
        """

    def modify_db_proxy(
        self,
        *,
        DBProxyName: str,
        NewDBProxyName: str = ...,
        Auth: Sequence[UserAuthConfigTypeDef] = ...,
        RequireTLS: bool = ...,
        IdleClientTimeout: int = ...,
        DebugLogging: bool = ...,
        RoleArn: str = ...,
        SecurityGroups: Sequence[str] = ...,
    ) -> ModifyDBProxyResponseTypeDef:
        """
        Changes the settings for an existing DB proxy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_proxy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_proxy)
        """

    def modify_db_proxy_endpoint(
        self,
        *,
        DBProxyEndpointName: str,
        NewDBProxyEndpointName: str = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
    ) -> ModifyDBProxyEndpointResponseTypeDef:
        """
        Changes the settings for an existing DB proxy endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_proxy_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_proxy_endpoint)
        """

    def modify_db_proxy_target_group(
        self,
        *,
        TargetGroupName: str,
        DBProxyName: str,
        ConnectionPoolConfig: ConnectionPoolConfigurationTypeDef = ...,
        NewName: str = ...,
    ) -> ModifyDBProxyTargetGroupResponseTypeDef:
        """
        Modifies the properties of a `DBProxyTargetGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_proxy_target_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_proxy_target_group)
        """

    def modify_db_recommendation(
        self,
        *,
        RecommendationId: str,
        Locale: str = ...,
        Status: str = ...,
        RecommendedActionUpdates: Sequence[RecommendedActionUpdateTypeDef] = ...,
    ) -> DBRecommendationMessageTypeDef:
        """
        Updates the recommendation status and recommended action status for the
        specified
        recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_recommendation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_recommendation)
        """

    def modify_db_snapshot(
        self, *, DBSnapshotIdentifier: str, EngineVersion: str = ..., OptionGroupName: str = ...
    ) -> ModifyDBSnapshotResultTypeDef:
        """
        Updates a manual DB snapshot with a new engine version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_snapshot)
        """

    def modify_db_snapshot_attribute(
        self,
        *,
        DBSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: Sequence[str] = ...,
        ValuesToRemove: Sequence[str] = ...,
    ) -> ModifyDBSnapshotAttributeResultTypeDef:
        """
        Adds an attribute and values to, or removes an attribute and values from, a
        manual DB
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_snapshot_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_snapshot_attribute)
        """

    def modify_db_subnet_group(
        self,
        *,
        DBSubnetGroupName: str,
        SubnetIds: Sequence[str],
        DBSubnetGroupDescription: str = ...,
    ) -> ModifyDBSubnetGroupResultTypeDef:
        """
        Modifies an existing DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_subnet_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_subnet_group)
        """

    def modify_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str = ...,
        SourceType: str = ...,
        EventCategories: Sequence[str] = ...,
        Enabled: bool = ...,
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        Modifies an existing RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_event_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_event_subscription)
        """

    def modify_global_cluster(
        self,
        *,
        GlobalClusterIdentifier: str = ...,
        NewGlobalClusterIdentifier: str = ...,
        DeletionProtection: bool = ...,
        EngineVersion: str = ...,
        AllowMajorVersionUpgrade: bool = ...,
    ) -> ModifyGlobalClusterResultTypeDef:
        """
        Modifies a setting for an Amazon Aurora global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_global_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_global_cluster)
        """

    def modify_option_group(
        self,
        *,
        OptionGroupName: str,
        OptionsToInclude: Sequence[OptionConfigurationTypeDef] = ...,
        OptionsToRemove: Sequence[str] = ...,
        ApplyImmediately: bool = ...,
    ) -> ModifyOptionGroupResultTypeDef:
        """
        Modifies an existing option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_option_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_option_group)
        """

    def modify_tenant_database(
        self,
        *,
        DBInstanceIdentifier: str,
        TenantDBName: str,
        MasterUserPassword: str = ...,
        NewTenantDBName: str = ...,
    ) -> ModifyTenantDatabaseResultTypeDef:
        """
        Modifies an existing tenant database in a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_tenant_database)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_tenant_database)
        """

    def promote_read_replica(
        self,
        *,
        DBInstanceIdentifier: str,
        BackupRetentionPeriod: int = ...,
        PreferredBackupWindow: str = ...,
    ) -> PromoteReadReplicaResultTypeDef:
        """
        Promotes a read replica DB instance to a standalone DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.promote_read_replica)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#promote_read_replica)
        """

    def promote_read_replica_db_cluster(
        self, *, DBClusterIdentifier: str
    ) -> PromoteReadReplicaDBClusterResultTypeDef:
        """
        Promotes a read replica DB cluster to a standalone DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.promote_read_replica_db_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#promote_read_replica_db_cluster)
        """

    def purchase_reserved_db_instances_offering(
        self,
        *,
        ReservedDBInstancesOfferingId: str,
        ReservedDBInstanceId: str = ...,
        DBInstanceCount: int = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> PurchaseReservedDBInstancesOfferingResultTypeDef:
        """
        Purchases a reserved DB instance offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.purchase_reserved_db_instances_offering)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#purchase_reserved_db_instances_offering)
        """

    def reboot_db_cluster(self, *, DBClusterIdentifier: str) -> RebootDBClusterResultTypeDef:
        """
        You might need to reboot your DB cluster, usually for maintenance reasons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reboot_db_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reboot_db_cluster)
        """

    def reboot_db_instance(
        self, *, DBInstanceIdentifier: str, ForceFailover: bool = ...
    ) -> RebootDBInstanceResultTypeDef:
        """
        You might need to reboot your DB instance, usually for maintenance reasons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reboot_db_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reboot_db_instance)
        """

    def register_db_proxy_targets(
        self,
        *,
        DBProxyName: str,
        TargetGroupName: str = ...,
        DBInstanceIdentifiers: Sequence[str] = ...,
        DBClusterIdentifiers: Sequence[str] = ...,
    ) -> RegisterDBProxyTargetsResponseTypeDef:
        """
        Associate one or more `DBProxyTarget` data structures with a
        `DBProxyTargetGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.register_db_proxy_targets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#register_db_proxy_targets)
        """

    def remove_from_global_cluster(
        self, *, GlobalClusterIdentifier: str = ..., DbClusterIdentifier: str = ...
    ) -> RemoveFromGlobalClusterResultTypeDef:
        """
        Detaches an Aurora secondary cluster from an Aurora global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_from_global_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_from_global_cluster)
        """

    def remove_role_from_db_cluster(
        self, *, DBClusterIdentifier: str, RoleArn: str, FeatureName: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the asssociation of an Amazon Web Services Identity and Access
        Management (IAM) role from a DB
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_role_from_db_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_role_from_db_cluster)
        """

    def remove_role_from_db_instance(
        self, *, DBInstanceIdentifier: str, RoleArn: str, FeatureName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates an Amazon Web Services Identity and Access Management (IAM) role
        from a DB
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_role_from_db_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_role_from_db_instance)
        """

    def remove_source_identifier_from_subscription(
        self, *, SubscriptionName: str, SourceIdentifier: str
    ) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
        """
        Removes a source identifier from an existing RDS event notification
        subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_source_identifier_from_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_source_identifier_from_subscription)
        """

    def remove_tags_from_resource(
        self, *, ResourceName: str, TagKeys: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes metadata tags from an Amazon RDS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_tags_from_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_tags_from_resource)
        """

    def reset_db_cluster_parameter_group(
        self,
        *,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool = ...,
        Parameters: Sequence[ParameterTypeDef] = ...,
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB cluster parameter group to the default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reset_db_cluster_parameter_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reset_db_cluster_parameter_group)
        """

    def reset_db_parameter_group(
        self,
        *,
        DBParameterGroupName: str,
        ResetAllParameters: bool = ...,
        Parameters: Sequence[ParameterTypeDef] = ...,
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB parameter group to the engine/system default
        value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reset_db_parameter_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reset_db_parameter_group)
        """

    def restore_db_cluster_from_s3(
        self,
        *,
        DBClusterIdentifier: str,
        Engine: str,
        MasterUsername: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
        AvailabilityZones: Sequence[str] = ...,
        BackupRetentionPeriod: int = ...,
        CharacterSetName: str = ...,
        DatabaseName: str = ...,
        DBClusterParameterGroupName: str = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        DBSubnetGroupName: str = ...,
        EngineVersion: str = ...,
        Port: int = ...,
        MasterUserPassword: str = ...,
        OptionGroupName: str = ...,
        PreferredBackupWindow: str = ...,
        PreferredMaintenanceWindow: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        StorageEncrypted: bool = ...,
        KmsKeyId: str = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        S3Prefix: str = ...,
        BacktrackWindow: int = ...,
        EnableCloudwatchLogsExports: Sequence[str] = ...,
        DeletionProtection: bool = ...,
        CopyTagsToSnapshot: bool = ...,
        Domain: str = ...,
        DomainIAMRoleName: str = ...,
        ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfigurationTypeDef = ...,
        NetworkType: str = ...,
        ManageMasterUserPassword: bool = ...,
        MasterUserSecretKmsKeyId: str = ...,
        StorageType: str = ...,
    ) -> RestoreDBClusterFromS3ResultTypeDef:
        """
        Creates an Amazon Aurora DB cluster from MySQL data stored in an Amazon S3
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_cluster_from_s3)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_cluster_from_s3)
        """

    def restore_db_cluster_from_snapshot(
        self,
        *,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: Sequence[str] = ...,
        EngineVersion: str = ...,
        Port: int = ...,
        DBSubnetGroupName: str = ...,
        DatabaseName: str = ...,
        OptionGroupName: str = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
        KmsKeyId: str = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        BacktrackWindow: int = ...,
        EnableCloudwatchLogsExports: Sequence[str] = ...,
        EngineMode: str = ...,
        ScalingConfiguration: ScalingConfigurationTypeDef = ...,
        DBClusterParameterGroupName: str = ...,
        DeletionProtection: bool = ...,
        CopyTagsToSnapshot: bool = ...,
        Domain: str = ...,
        DomainIAMRoleName: str = ...,
        DBClusterInstanceClass: str = ...,
        StorageType: str = ...,
        Iops: int = ...,
        PubliclyAccessible: bool = ...,
        ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfigurationTypeDef = ...,
        NetworkType: str = ...,
        RdsCustomClusterConfiguration: RdsCustomClusterConfigurationTypeDef = ...,
    ) -> RestoreDBClusterFromSnapshotResultTypeDef:
        """
        Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_cluster_from_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_cluster_from_snapshot)
        """

    def restore_db_cluster_to_point_in_time(
        self,
        *,
        DBClusterIdentifier: str,
        RestoreType: str = ...,
        SourceDBClusterIdentifier: str = ...,
        RestoreToTime: TimestampTypeDef = ...,
        UseLatestRestorableTime: bool = ...,
        Port: int = ...,
        DBSubnetGroupName: str = ...,
        OptionGroupName: str = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
        KmsKeyId: str = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        BacktrackWindow: int = ...,
        EnableCloudwatchLogsExports: Sequence[str] = ...,
        DBClusterParameterGroupName: str = ...,
        DeletionProtection: bool = ...,
        CopyTagsToSnapshot: bool = ...,
        Domain: str = ...,
        DomainIAMRoleName: str = ...,
        ScalingConfiguration: ScalingConfigurationTypeDef = ...,
        EngineMode: str = ...,
        DBClusterInstanceClass: str = ...,
        StorageType: str = ...,
        PubliclyAccessible: bool = ...,
        Iops: int = ...,
        ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfigurationTypeDef = ...,
        NetworkType: str = ...,
        SourceDbClusterResourceId: str = ...,
        RdsCustomClusterConfiguration: RdsCustomClusterConfigurationTypeDef = ...,
    ) -> RestoreDBClusterToPointInTimeResultTypeDef:
        """
        Restores a DB cluster to an arbitrary point in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_cluster_to_point_in_time)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_cluster_to_point_in_time)
        """

    def restore_db_instance_from_db_snapshot(
        self,
        *,
        DBInstanceIdentifier: str,
        DBSnapshotIdentifier: str = ...,
        DBInstanceClass: str = ...,
        Port: int = ...,
        AvailabilityZone: str = ...,
        DBSubnetGroupName: str = ...,
        MultiAZ: bool = ...,
        PubliclyAccessible: bool = ...,
        AutoMinorVersionUpgrade: bool = ...,
        LicenseModel: str = ...,
        DBName: str = ...,
        Engine: str = ...,
        Iops: int = ...,
        OptionGroupName: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        StorageType: str = ...,
        TdeCredentialArn: str = ...,
        TdeCredentialPassword: str = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        Domain: str = ...,
        DomainFqdn: str = ...,
        DomainOu: str = ...,
        DomainAuthSecretArn: str = ...,
        DomainDnsIps: Sequence[str] = ...,
        CopyTagsToSnapshot: bool = ...,
        DomainIAMRoleName: str = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        EnableCloudwatchLogsExports: Sequence[str] = ...,
        ProcessorFeatures: Sequence[ProcessorFeatureTypeDef] = ...,
        UseDefaultProcessorFeatures: bool = ...,
        DBParameterGroupName: str = ...,
        DeletionProtection: bool = ...,
        EnableCustomerOwnedIp: bool = ...,
        CustomIamInstanceProfile: str = ...,
        BackupTarget: str = ...,
        NetworkType: str = ...,
        StorageThroughput: int = ...,
        DBClusterSnapshotIdentifier: str = ...,
        AllocatedStorage: int = ...,
        DedicatedLogVolume: bool = ...,
    ) -> RestoreDBInstanceFromDBSnapshotResultTypeDef:
        """
        Creates a new DB instance from a DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_instance_from_db_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_instance_from_db_snapshot)
        """

    def restore_db_instance_from_s3(
        self,
        *,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
        DBName: str = ...,
        AllocatedStorage: int = ...,
        MasterUsername: str = ...,
        MasterUserPassword: str = ...,
        DBSecurityGroups: Sequence[str] = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        AvailabilityZone: str = ...,
        DBSubnetGroupName: str = ...,
        PreferredMaintenanceWindow: str = ...,
        DBParameterGroupName: str = ...,
        BackupRetentionPeriod: int = ...,
        PreferredBackupWindow: str = ...,
        Port: int = ...,
        MultiAZ: bool = ...,
        EngineVersion: str = ...,
        AutoMinorVersionUpgrade: bool = ...,
        LicenseModel: str = ...,
        Iops: int = ...,
        OptionGroupName: str = ...,
        PubliclyAccessible: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        StorageType: str = ...,
        StorageEncrypted: bool = ...,
        KmsKeyId: str = ...,
        CopyTagsToSnapshot: bool = ...,
        MonitoringInterval: int = ...,
        MonitoringRoleArn: str = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        S3Prefix: str = ...,
        EnablePerformanceInsights: bool = ...,
        PerformanceInsightsKMSKeyId: str = ...,
        PerformanceInsightsRetentionPeriod: int = ...,
        EnableCloudwatchLogsExports: Sequence[str] = ...,
        ProcessorFeatures: Sequence[ProcessorFeatureTypeDef] = ...,
        UseDefaultProcessorFeatures: bool = ...,
        DeletionProtection: bool = ...,
        MaxAllocatedStorage: int = ...,
        NetworkType: str = ...,
        StorageThroughput: int = ...,
        ManageMasterUserPassword: bool = ...,
        MasterUserSecretKmsKeyId: str = ...,
        DedicatedLogVolume: bool = ...,
    ) -> RestoreDBInstanceFromS3ResultTypeDef:
        """
        Amazon Relational Database Service (Amazon RDS) supports importing MySQL
        databases by using backup
        files.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_instance_from_s3)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_instance_from_s3)
        """

    def restore_db_instance_to_point_in_time(
        self,
        *,
        TargetDBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str = ...,
        RestoreTime: TimestampTypeDef = ...,
        UseLatestRestorableTime: bool = ...,
        DBInstanceClass: str = ...,
        Port: int = ...,
        AvailabilityZone: str = ...,
        DBSubnetGroupName: str = ...,
        MultiAZ: bool = ...,
        PubliclyAccessible: bool = ...,
        AutoMinorVersionUpgrade: bool = ...,
        LicenseModel: str = ...,
        DBName: str = ...,
        Engine: str = ...,
        Iops: int = ...,
        OptionGroupName: str = ...,
        CopyTagsToSnapshot: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        StorageType: str = ...,
        TdeCredentialArn: str = ...,
        TdeCredentialPassword: str = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        Domain: str = ...,
        DomainIAMRoleName: str = ...,
        DomainFqdn: str = ...,
        DomainOu: str = ...,
        DomainAuthSecretArn: str = ...,
        DomainDnsIps: Sequence[str] = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        EnableCloudwatchLogsExports: Sequence[str] = ...,
        ProcessorFeatures: Sequence[ProcessorFeatureTypeDef] = ...,
        UseDefaultProcessorFeatures: bool = ...,
        DBParameterGroupName: str = ...,
        DeletionProtection: bool = ...,
        SourceDbiResourceId: str = ...,
        MaxAllocatedStorage: int = ...,
        SourceDBInstanceAutomatedBackupsArn: str = ...,
        EnableCustomerOwnedIp: bool = ...,
        CustomIamInstanceProfile: str = ...,
        BackupTarget: str = ...,
        NetworkType: str = ...,
        StorageThroughput: int = ...,
        AllocatedStorage: int = ...,
        DedicatedLogVolume: bool = ...,
    ) -> RestoreDBInstanceToPointInTimeResultTypeDef:
        """
        Restores a DB instance to an arbitrary point in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_instance_to_point_in_time)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_instance_to_point_in_time)
        """

    def revoke_db_security_group_ingress(
        self,
        *,
        DBSecurityGroupName: str,
        CIDRIP: str = ...,
        EC2SecurityGroupName: str = ...,
        EC2SecurityGroupId: str = ...,
        EC2SecurityGroupOwnerId: str = ...,
    ) -> RevokeDBSecurityGroupIngressResultTypeDef:
        """
        Revokes ingress from a DBSecurityGroup for previously authorized IP ranges or
        EC2 or VPC security
        groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.revoke_db_security_group_ingress)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#revoke_db_security_group_ingress)
        """

    def start_activity_stream(
        self,
        *,
        ResourceArn: str,
        Mode: ActivityStreamModeType,
        KmsKeyId: str,
        ApplyImmediately: bool = ...,
        EngineNativeAuditFieldsIncluded: bool = ...,
    ) -> StartActivityStreamResponseTypeDef:
        """
        Starts a database activity stream to monitor activity on the database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_activity_stream)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_activity_stream)
        """

    def start_db_cluster(self, *, DBClusterIdentifier: str) -> StartDBClusterResultTypeDef:
        """
        Starts an Amazon Aurora DB cluster that was stopped using the Amazon Web
        Services console, the stop-db-cluster CLI command, or the `StopDBCluster`
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_db_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_db_cluster)
        """

    def start_db_instance(self, *, DBInstanceIdentifier: str) -> StartDBInstanceResultTypeDef:
        """
        Starts an Amazon RDS DB instance that was stopped using the Amazon Web Services
        console, the stop-db-instance CLI command, or the `StopDBInstance`
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_db_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_db_instance)
        """

    def start_db_instance_automated_backups_replication(
        self,
        *,
        SourceDBInstanceArn: str,
        BackupRetentionPeriod: int = ...,
        KmsKeyId: str = ...,
        PreSignedUrl: str = ...,
        SourceRegion: str = ...,
    ) -> StartDBInstanceAutomatedBackupsReplicationResultTypeDef:
        """
        Enables replication of automated backups to a different Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_db_instance_automated_backups_replication)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_db_instance_automated_backups_replication)
        """

    def start_export_task(
        self,
        *,
        ExportTaskIdentifier: str,
        SourceArn: str,
        S3BucketName: str,
        IamRoleArn: str,
        KmsKeyId: str,
        S3Prefix: str = ...,
        ExportOnly: Sequence[str] = ...,
    ) -> ExportTaskResponseTypeDef:
        """
        Starts an export of DB snapshot or DB cluster data to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_export_task)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_export_task)
        """

    def stop_activity_stream(
        self, *, ResourceArn: str, ApplyImmediately: bool = ...
    ) -> StopActivityStreamResponseTypeDef:
        """
        Stops a database activity stream that was started using the Amazon Web Services
        console, the `start-activity-stream` CLI command, or the `StartActivityStream`
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_activity_stream)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_activity_stream)
        """

    def stop_db_cluster(self, *, DBClusterIdentifier: str) -> StopDBClusterResultTypeDef:
        """
        Stops an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_db_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_db_cluster)
        """

    def stop_db_instance(
        self, *, DBInstanceIdentifier: str, DBSnapshotIdentifier: str = ...
    ) -> StopDBInstanceResultTypeDef:
        """
        Stops an Amazon RDS DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_db_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_db_instance)
        """

    def stop_db_instance_automated_backups_replication(
        self, *, SourceDBInstanceArn: str
    ) -> StopDBInstanceAutomatedBackupsReplicationResultTypeDef:
        """
        Stops automated backup replication for a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_db_instance_automated_backups_replication)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_db_instance_automated_backups_replication)
        """

    def switchover_blue_green_deployment(
        self, *, BlueGreenDeploymentIdentifier: str, SwitchoverTimeout: int = ...
    ) -> SwitchoverBlueGreenDeploymentResponseTypeDef:
        """
        Switches over a blue/green deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.switchover_blue_green_deployment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#switchover_blue_green_deployment)
        """

    def switchover_global_cluster(
        self, *, GlobalClusterIdentifier: str, TargetDbClusterIdentifier: str
    ) -> SwitchoverGlobalClusterResultTypeDef:
        """
        Switches over the specified secondary DB cluster to be the new primary DB
        cluster in the global database
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.switchover_global_cluster)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#switchover_global_cluster)
        """

    def switchover_read_replica(
        self, *, DBInstanceIdentifier: str
    ) -> SwitchoverReadReplicaResultTypeDef:
        """
        Switches over an Oracle standby database in an Oracle Data Guard environment,
        making it the new primary
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.switchover_read_replica)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#switchover_read_replica)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_blue_green_deployments"]
    ) -> DescribeBlueGreenDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> DescribeCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_automated_backups"]
    ) -> DescribeDBClusterAutomatedBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_backtracks"]
    ) -> DescribeDBClusterBacktracksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_endpoints"]
    ) -> DescribeDBClusterEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameter_groups"]
    ) -> DescribeDBClusterParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameters"]
    ) -> DescribeDBClusterParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_snapshots"]
    ) -> DescribeDBClusterSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_clusters"]
    ) -> DescribeDBClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> DescribeDBEngineVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instance_automated_backups"]
    ) -> DescribeDBInstanceAutomatedBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instances"]
    ) -> DescribeDBInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_log_files"]
    ) -> DescribeDBLogFilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameter_groups"]
    ) -> DescribeDBParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameters"]
    ) -> DescribeDBParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxies"]
    ) -> DescribeDBProxiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_endpoints"]
    ) -> DescribeDBProxyEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_target_groups"]
    ) -> DescribeDBProxyTargetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_targets"]
    ) -> DescribeDBProxyTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_recommendations"]
    ) -> DescribeDBRecommendationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_security_groups"]
    ) -> DescribeDBSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_snapshot_tenant_databases"]
    ) -> DescribeDBSnapshotTenantDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_snapshots"]
    ) -> DescribeDBSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> DescribeDBSubnetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_cluster_parameters"]
    ) -> DescribeEngineDefaultClusterParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> DescribeEngineDefaultParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> DescribeExportTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_global_clusters"]
    ) -> DescribeGlobalClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_integrations"]
    ) -> DescribeIntegrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_option_group_options"]
    ) -> DescribeOptionGroupOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_option_groups"]
    ) -> DescribeOptionGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> DescribeOrderableDBInstanceOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pending_maintenance_actions"]
    ) -> DescribePendingMaintenanceActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_db_instances"]
    ) -> DescribeReservedDBInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_db_instances_offerings"]
    ) -> DescribeReservedDBInstancesOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_source_regions"]
    ) -> DescribeSourceRegionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tenant_databases"]
    ) -> DescribeTenantDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["download_db_log_file_portion"]
    ) -> DownloadDBLogFilePortionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["db_cluster_available"]) -> DBClusterAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["db_cluster_deleted"]) -> DBClusterDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_cluster_snapshot_available"]
    ) -> DBClusterSnapshotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_cluster_snapshot_deleted"]
    ) -> DBClusterSnapshotDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_instance_available"]
    ) -> DBInstanceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["db_instance_deleted"]) -> DBInstanceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_available"]
    ) -> DBSnapshotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_completed"]
    ) -> DBSnapshotCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["db_snapshot_deleted"]) -> DBSnapshotDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["tenant_database_available"]
    ) -> TenantDatabaseAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["tenant_database_deleted"]
    ) -> TenantDatabaseDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """
