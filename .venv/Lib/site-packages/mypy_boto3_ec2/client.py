"""
Type annotations for ec2 service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ec2.client import EC2Client

    session = Session()
    client: EC2Client = session.client("ec2")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AccountAttributeNameType,
    AddressFamilyType,
    AffinityType,
    ArchitectureTypeType,
    ArchitectureValuesType,
    AutoPlacementType,
    BootModeValuesType,
    CapacityReservationInstancePlatformType,
    CapacityReservationTenancyType,
    ConnectivityTypeType,
    DeviceTrustProviderTypeType,
    DiskImageFormatType,
    DomainTypeType,
    EndDateTypeType,
    EventTypeType,
    ExcessCapacityTerminationPolicyType,
    ExportEnvironmentType,
    FleetEventTypeType,
    FleetExcessCapacityTerminationPolicyType,
    FleetTypeType,
    FlowLogsResourceTypeType,
    FpgaImageAttributeNameType,
    HostMaintenanceType,
    HostnameTypeType,
    HostRecoveryType,
    HostTenancyType,
    HttpTokensStateType,
    ImageAttributeNameType,
    InstanceAttributeNameType,
    InstanceAutoRecoveryStateType,
    InstanceInterruptionBehaviorType,
    InstanceMatchCriteriaType,
    InstanceMetadataEndpointStateType,
    InstanceMetadataProtocolStateType,
    InstanceMetadataTagsStateType,
    InstanceTypeType,
    InterfacePermissionTypeType,
    IpAddressTypeType,
    IpamPoolPublicIpSourceType,
    IpamResourceTypeType,
    IpamTierType,
    KeyFormatType,
    KeyTypeType,
    LocalGatewayRouteTableModeType,
    LocationTypeType,
    LockModeType,
    LogDestinationTypeType,
    ModifyAvailabilityZoneOptInStatusType,
    NetworkInterfaceAttributeType,
    NetworkInterfaceCreationTypeType,
    OfferingClassTypeType,
    OfferingTypeValuesType,
    OperationTypeType,
    PlacementStrategyType,
    ProtocolType,
    ReportInstanceReasonCodesType,
    ReportStatusTypeType,
    RIProductDescriptionType,
    RuleActionType,
    SelfServicePortalType,
    ShutdownBehaviorType,
    SnapshotAttributeNameType,
    SnapshotBlockPublicAccessStateType,
    SpotInstanceTypeType,
    SpreadLevelType,
    SubnetCidrReservationTypeType,
    TargetCapacityUnitTypeType,
    TenancyType,
    TrafficDirectionType,
    TrafficMirrorFilterRuleFieldType,
    TrafficMirrorRuleActionType,
    TrafficMirrorSessionFieldType,
    TrafficTypeType,
    TransportProtocolType,
    TrustProviderTypeType,
    UnlimitedSupportedInstanceFamilyType,
    UserTrustProviderTypeType,
    VerifiedAccessEndpointTypeType,
    VirtualizationTypeType,
    VolumeAttributeNameType,
    VolumeTypeType,
    VpcAttributeNameType,
    VpcEndpointTypeType,
)
from .paginator import (
    DescribeAddressesAttributePaginator,
    DescribeAddressTransfersPaginator,
    DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator,
    DescribeByoipCidrsPaginator,
    DescribeCapacityBlockOfferingsPaginator,
    DescribeCapacityReservationFleetsPaginator,
    DescribeCapacityReservationsPaginator,
    DescribeCarrierGatewaysPaginator,
    DescribeClassicLinkInstancesPaginator,
    DescribeClientVpnAuthorizationRulesPaginator,
    DescribeClientVpnConnectionsPaginator,
    DescribeClientVpnEndpointsPaginator,
    DescribeClientVpnRoutesPaginator,
    DescribeClientVpnTargetNetworksPaginator,
    DescribeCoipPoolsPaginator,
    DescribeDhcpOptionsPaginator,
    DescribeEgressOnlyInternetGatewaysPaginator,
    DescribeExportImageTasksPaginator,
    DescribeFastLaunchImagesPaginator,
    DescribeFastSnapshotRestoresPaginator,
    DescribeFleetsPaginator,
    DescribeFlowLogsPaginator,
    DescribeFpgaImagesPaginator,
    DescribeHostReservationOfferingsPaginator,
    DescribeHostReservationsPaginator,
    DescribeHostsPaginator,
    DescribeIamInstanceProfileAssociationsPaginator,
    DescribeImagesPaginator,
    DescribeImportImageTasksPaginator,
    DescribeImportSnapshotTasksPaginator,
    DescribeInstanceConnectEndpointsPaginator,
    DescribeInstanceCreditSpecificationsPaginator,
    DescribeInstanceEventWindowsPaginator,
    DescribeInstancesPaginator,
    DescribeInstanceStatusPaginator,
    DescribeInstanceTopologyPaginator,
    DescribeInstanceTypeOfferingsPaginator,
    DescribeInstanceTypesPaginator,
    DescribeInternetGatewaysPaginator,
    DescribeIpamPoolsPaginator,
    DescribeIpamResourceDiscoveriesPaginator,
    DescribeIpamResourceDiscoveryAssociationsPaginator,
    DescribeIpamScopesPaginator,
    DescribeIpamsPaginator,
    DescribeIpv6PoolsPaginator,
    DescribeLaunchTemplatesPaginator,
    DescribeLaunchTemplateVersionsPaginator,
    DescribeLocalGatewayRouteTablesPaginator,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
    DescribeLocalGatewayRouteTableVpcAssociationsPaginator,
    DescribeLocalGatewaysPaginator,
    DescribeLocalGatewayVirtualInterfaceGroupsPaginator,
    DescribeLocalGatewayVirtualInterfacesPaginator,
    DescribeManagedPrefixListsPaginator,
    DescribeMovingAddressesPaginator,
    DescribeNatGatewaysPaginator,
    DescribeNetworkAclsPaginator,
    DescribeNetworkInsightsAccessScopeAnalysesPaginator,
    DescribeNetworkInsightsAccessScopesPaginator,
    DescribeNetworkInsightsAnalysesPaginator,
    DescribeNetworkInsightsPathsPaginator,
    DescribeNetworkInterfacePermissionsPaginator,
    DescribeNetworkInterfacesPaginator,
    DescribePrefixListsPaginator,
    DescribePrincipalIdFormatPaginator,
    DescribePublicIpv4PoolsPaginator,
    DescribeReplaceRootVolumeTasksPaginator,
    DescribeReservedInstancesModificationsPaginator,
    DescribeReservedInstancesOfferingsPaginator,
    DescribeRouteTablesPaginator,
    DescribeScheduledInstanceAvailabilityPaginator,
    DescribeScheduledInstancesPaginator,
    DescribeSecurityGroupRulesPaginator,
    DescribeSecurityGroupsPaginator,
    DescribeSnapshotsPaginator,
    DescribeSnapshotTierStatusPaginator,
    DescribeSpotFleetInstancesPaginator,
    DescribeSpotFleetRequestsPaginator,
    DescribeSpotInstanceRequestsPaginator,
    DescribeSpotPriceHistoryPaginator,
    DescribeStaleSecurityGroupsPaginator,
    DescribeStoreImageTasksPaginator,
    DescribeSubnetsPaginator,
    DescribeTagsPaginator,
    DescribeTrafficMirrorFiltersPaginator,
    DescribeTrafficMirrorSessionsPaginator,
    DescribeTrafficMirrorTargetsPaginator,
    DescribeTransitGatewayAttachmentsPaginator,
    DescribeTransitGatewayConnectPeersPaginator,
    DescribeTransitGatewayConnectsPaginator,
    DescribeTransitGatewayMulticastDomainsPaginator,
    DescribeTransitGatewayPeeringAttachmentsPaginator,
    DescribeTransitGatewayPolicyTablesPaginator,
    DescribeTransitGatewayRouteTableAnnouncementsPaginator,
    DescribeTransitGatewayRouteTablesPaginator,
    DescribeTransitGatewaysPaginator,
    DescribeTransitGatewayVpcAttachmentsPaginator,
    DescribeTrunkInterfaceAssociationsPaginator,
    DescribeVerifiedAccessEndpointsPaginator,
    DescribeVerifiedAccessGroupsPaginator,
    DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator,
    DescribeVerifiedAccessInstancesPaginator,
    DescribeVerifiedAccessTrustProvidersPaginator,
    DescribeVolumesModificationsPaginator,
    DescribeVolumesPaginator,
    DescribeVolumeStatusPaginator,
    DescribeVpcClassicLinkDnsSupportPaginator,
    DescribeVpcEndpointConnectionNotificationsPaginator,
    DescribeVpcEndpointConnectionsPaginator,
    DescribeVpcEndpointServiceConfigurationsPaginator,
    DescribeVpcEndpointServicePermissionsPaginator,
    DescribeVpcEndpointServicesPaginator,
    DescribeVpcEndpointsPaginator,
    DescribeVpcPeeringConnectionsPaginator,
    DescribeVpcsPaginator,
    GetAssociatedIpv6PoolCidrsPaginator,
    GetAwsNetworkPerformanceDataPaginator,
    GetGroupsForCapacityReservationPaginator,
    GetInstanceTypesFromInstanceRequirementsPaginator,
    GetIpamAddressHistoryPaginator,
    GetIpamDiscoveredAccountsPaginator,
    GetIpamDiscoveredResourceCidrsPaginator,
    GetIpamPoolAllocationsPaginator,
    GetIpamPoolCidrsPaginator,
    GetIpamResourceCidrsPaginator,
    GetManagedPrefixListAssociationsPaginator,
    GetManagedPrefixListEntriesPaginator,
    GetNetworkInsightsAccessScopeAnalysisFindingsPaginator,
    GetSecurityGroupsForVpcPaginator,
    GetSpotPlacementScoresPaginator,
    GetTransitGatewayAttachmentPropagationsPaginator,
    GetTransitGatewayMulticastDomainAssociationsPaginator,
    GetTransitGatewayPolicyTableAssociationsPaginator,
    GetTransitGatewayPrefixListReferencesPaginator,
    GetTransitGatewayRouteTableAssociationsPaginator,
    GetTransitGatewayRouteTablePropagationsPaginator,
    GetVpnConnectionDeviceTypesPaginator,
    ListImagesInRecycleBinPaginator,
    ListSnapshotsInRecycleBinPaginator,
    SearchLocalGatewayRoutesPaginator,
    SearchTransitGatewayMulticastGroupsPaginator,
)
from .type_defs import (
    AcceptAddressTransferResultTypeDef,
    AcceptReservedInstancesExchangeQuoteResultTypeDef,
    AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef,
    AcceptTransitGatewayPeeringAttachmentResultTypeDef,
    AcceptTransitGatewayVpcAttachmentResultTypeDef,
    AcceptVpcEndpointConnectionsResultTypeDef,
    AcceptVpcPeeringConnectionResultTypeDef,
    AccessScopePathRequestTypeDef,
    AddIpamOperatingRegionTypeDef,
    AddPrefixListEntryTypeDef,
    AdvertiseByoipCidrResultTypeDef,
    AllocateAddressResultTypeDef,
    AllocateHostsResultTypeDef,
    AllocateIpamPoolCidrResultTypeDef,
    ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef,
    AsnAuthorizationContextTypeDef,
    AssignIpv6AddressesResultTypeDef,
    AssignPrivateIpAddressesResultTypeDef,
    AssignPrivateNatGatewayAddressResultTypeDef,
    AssociateAddressResultTypeDef,
    AssociateClientVpnTargetNetworkResultTypeDef,
    AssociateEnclaveCertificateIamRoleResultTypeDef,
    AssociateIamInstanceProfileResultTypeDef,
    AssociateInstanceEventWindowResultTypeDef,
    AssociateIpamByoasnResultTypeDef,
    AssociateIpamResourceDiscoveryResultTypeDef,
    AssociateNatGatewayAddressResultTypeDef,
    AssociateRouteTableResultTypeDef,
    AssociateSubnetCidrBlockResultTypeDef,
    AssociateTransitGatewayMulticastDomainResultTypeDef,
    AssociateTransitGatewayPolicyTableResultTypeDef,
    AssociateTransitGatewayRouteTableResultTypeDef,
    AssociateTrunkInterfaceResultTypeDef,
    AssociateVpcCidrBlockResultTypeDef,
    AttachClassicLinkVpcResultTypeDef,
    AttachNetworkInterfaceResultTypeDef,
    AttachVerifiedAccessTrustProviderResultTypeDef,
    AttachVpnGatewayResultTypeDef,
    AttributeBooleanValueTypeDef,
    AttributeValueTypeDef,
    AuthorizeClientVpnIngressResultTypeDef,
    AuthorizeSecurityGroupEgressResultTypeDef,
    AuthorizeSecurityGroupIngressResultTypeDef,
    BlobAttributeValueTypeDef,
    BlobTypeDef,
    BlockDeviceMappingTypeDef,
    BundleInstanceResultTypeDef,
    CancelBundleTaskResultTypeDef,
    CancelCapacityReservationFleetsResultTypeDef,
    CancelCapacityReservationResultTypeDef,
    CancelImageLaunchPermissionResultTypeDef,
    CancelImportTaskResultTypeDef,
    CancelReservedInstancesListingResultTypeDef,
    CancelSpotFleetRequestsResponseTypeDef,
    CancelSpotInstanceRequestsResultTypeDef,
    CapacityReservationSpecificationTypeDef,
    CidrAuthorizationContextTypeDef,
    ClientConnectOptionsTypeDef,
    ClientDataTypeDef,
    ClientLoginBannerOptionsTypeDef,
    ClientVpnAuthenticationRequestTypeDef,
    ConfirmProductInstanceResultTypeDef,
    ConnectionLogOptionsTypeDef,
    ConnectionTrackingSpecificationRequestTypeDef,
    CopyFpgaImageResultTypeDef,
    CopyImageResultTypeDef,
    CopySnapshotResultTypeDef,
    CpuOptionsRequestTypeDef,
    CreateCapacityReservationFleetResultTypeDef,
    CreateCapacityReservationResultTypeDef,
    CreateCarrierGatewayResultTypeDef,
    CreateClientVpnEndpointResultTypeDef,
    CreateClientVpnRouteResultTypeDef,
    CreateCoipCidrResultTypeDef,
    CreateCoipPoolResultTypeDef,
    CreateCustomerGatewayResultTypeDef,
    CreateDefaultSubnetResultTypeDef,
    CreateDefaultVpcResultTypeDef,
    CreateDhcpOptionsResultTypeDef,
    CreateEgressOnlyInternetGatewayResultTypeDef,
    CreateFleetResultTypeDef,
    CreateFlowLogsResultTypeDef,
    CreateFpgaImageResultTypeDef,
    CreateImageResultTypeDef,
    CreateInstanceConnectEndpointResultTypeDef,
    CreateInstanceEventWindowResultTypeDef,
    CreateInstanceExportTaskResultTypeDef,
    CreateInternetGatewayResultTypeDef,
    CreateIpamPoolResultTypeDef,
    CreateIpamResourceDiscoveryResultTypeDef,
    CreateIpamResultTypeDef,
    CreateIpamScopeResultTypeDef,
    CreateLaunchTemplateResultTypeDef,
    CreateLaunchTemplateVersionResultTypeDef,
    CreateLocalGatewayRouteResultTypeDef,
    CreateLocalGatewayRouteTableResultTypeDef,
    CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef,
    CreateLocalGatewayRouteTableVpcAssociationResultTypeDef,
    CreateManagedPrefixListResultTypeDef,
    CreateNatGatewayResultTypeDef,
    CreateNetworkAclResultTypeDef,
    CreateNetworkInsightsAccessScopeResultTypeDef,
    CreateNetworkInsightsPathResultTypeDef,
    CreateNetworkInterfacePermissionResultTypeDef,
    CreateNetworkInterfaceResultTypeDef,
    CreatePlacementGroupResultTypeDef,
    CreatePublicIpv4PoolResultTypeDef,
    CreateReplaceRootVolumeTaskResultTypeDef,
    CreateReservedInstancesListingResultTypeDef,
    CreateRestoreImageTaskResultTypeDef,
    CreateRouteResultTypeDef,
    CreateRouteTableResultTypeDef,
    CreateSecurityGroupResultTypeDef,
    CreateSnapshotsResultTypeDef,
    CreateSpotDatafeedSubscriptionResultTypeDef,
    CreateStoreImageTaskResultTypeDef,
    CreateSubnetCidrReservationResultTypeDef,
    CreateSubnetResultTypeDef,
    CreateTrafficMirrorFilterResultTypeDef,
    CreateTrafficMirrorFilterRuleResultTypeDef,
    CreateTrafficMirrorSessionResultTypeDef,
    CreateTrafficMirrorTargetResultTypeDef,
    CreateTransitGatewayConnectPeerResultTypeDef,
    CreateTransitGatewayConnectRequestOptionsTypeDef,
    CreateTransitGatewayConnectResultTypeDef,
    CreateTransitGatewayMulticastDomainRequestOptionsTypeDef,
    CreateTransitGatewayMulticastDomainResultTypeDef,
    CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef,
    CreateTransitGatewayPeeringAttachmentResultTypeDef,
    CreateTransitGatewayPolicyTableResultTypeDef,
    CreateTransitGatewayPrefixListReferenceResultTypeDef,
    CreateTransitGatewayResultTypeDef,
    CreateTransitGatewayRouteResultTypeDef,
    CreateTransitGatewayRouteTableAnnouncementResultTypeDef,
    CreateTransitGatewayRouteTableResultTypeDef,
    CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef,
    CreateTransitGatewayVpcAttachmentResultTypeDef,
    CreateVerifiedAccessEndpointEniOptionsTypeDef,
    CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef,
    CreateVerifiedAccessEndpointResultTypeDef,
    CreateVerifiedAccessGroupResultTypeDef,
    CreateVerifiedAccessInstanceResultTypeDef,
    CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef,
    CreateVerifiedAccessTrustProviderOidcOptionsTypeDef,
    CreateVerifiedAccessTrustProviderResultTypeDef,
    CreateVolumePermissionModificationsTypeDef,
    CreateVpcEndpointConnectionNotificationResultTypeDef,
    CreateVpcEndpointResultTypeDef,
    CreateVpcEndpointServiceConfigurationResultTypeDef,
    CreateVpcPeeringConnectionResultTypeDef,
    CreateVpcResultTypeDef,
    CreateVpnConnectionResultTypeDef,
    CreateVpnGatewayResultTypeDef,
    CreditSpecificationRequestTypeDef,
    DataQueryTypeDef,
    DeleteCarrierGatewayResultTypeDef,
    DeleteClientVpnEndpointResultTypeDef,
    DeleteClientVpnRouteResultTypeDef,
    DeleteCoipCidrResultTypeDef,
    DeleteCoipPoolResultTypeDef,
    DeleteEgressOnlyInternetGatewayResultTypeDef,
    DeleteFleetsResultTypeDef,
    DeleteFlowLogsResultTypeDef,
    DeleteFpgaImageResultTypeDef,
    DeleteInstanceConnectEndpointResultTypeDef,
    DeleteInstanceEventWindowResultTypeDef,
    DeleteIpamPoolResultTypeDef,
    DeleteIpamResourceDiscoveryResultTypeDef,
    DeleteIpamResultTypeDef,
    DeleteIpamScopeResultTypeDef,
    DeleteKeyPairResultTypeDef,
    DeleteLaunchTemplateResultTypeDef,
    DeleteLaunchTemplateVersionsResultTypeDef,
    DeleteLocalGatewayRouteResultTypeDef,
    DeleteLocalGatewayRouteTableResultTypeDef,
    DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef,
    DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef,
    DeleteManagedPrefixListResultTypeDef,
    DeleteNatGatewayResultTypeDef,
    DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef,
    DeleteNetworkInsightsAccessScopeResultTypeDef,
    DeleteNetworkInsightsAnalysisResultTypeDef,
    DeleteNetworkInsightsPathResultTypeDef,
    DeleteNetworkInterfacePermissionResultTypeDef,
    DeletePublicIpv4PoolResultTypeDef,
    DeleteQueuedReservedInstancesResultTypeDef,
    DeleteSubnetCidrReservationResultTypeDef,
    DeleteTrafficMirrorFilterResultTypeDef,
    DeleteTrafficMirrorFilterRuleResultTypeDef,
    DeleteTrafficMirrorSessionResultTypeDef,
    DeleteTrafficMirrorTargetResultTypeDef,
    DeleteTransitGatewayConnectPeerResultTypeDef,
    DeleteTransitGatewayConnectResultTypeDef,
    DeleteTransitGatewayMulticastDomainResultTypeDef,
    DeleteTransitGatewayPeeringAttachmentResultTypeDef,
    DeleteTransitGatewayPolicyTableResultTypeDef,
    DeleteTransitGatewayPrefixListReferenceResultTypeDef,
    DeleteTransitGatewayResultTypeDef,
    DeleteTransitGatewayRouteResultTypeDef,
    DeleteTransitGatewayRouteTableAnnouncementResultTypeDef,
    DeleteTransitGatewayRouteTableResultTypeDef,
    DeleteTransitGatewayVpcAttachmentResultTypeDef,
    DeleteVerifiedAccessEndpointResultTypeDef,
    DeleteVerifiedAccessGroupResultTypeDef,
    DeleteVerifiedAccessInstanceResultTypeDef,
    DeleteVerifiedAccessTrustProviderResultTypeDef,
    DeleteVpcEndpointConnectionNotificationsResultTypeDef,
    DeleteVpcEndpointServiceConfigurationsResultTypeDef,
    DeleteVpcEndpointsResultTypeDef,
    DeleteVpcPeeringConnectionResultTypeDef,
    DeprovisionByoipCidrResultTypeDef,
    DeprovisionIpamByoasnResultTypeDef,
    DeprovisionIpamPoolCidrResultTypeDef,
    DeprovisionPublicIpv4PoolCidrResultTypeDef,
    DeregisterInstanceEventNotificationAttributesResultTypeDef,
    DeregisterInstanceTagAttributeRequestTypeDef,
    DeregisterTransitGatewayMulticastGroupMembersResultTypeDef,
    DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeAddressesAttributeResultTypeDef,
    DescribeAddressesResultTypeDef,
    DescribeAddressTransfersResultTypeDef,
    DescribeAggregateIdFormatResultTypeDef,
    DescribeAvailabilityZonesResultTypeDef,
    DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef,
    DescribeBundleTasksResultTypeDef,
    DescribeByoipCidrsResultTypeDef,
    DescribeCapacityBlockOfferingsResultTypeDef,
    DescribeCapacityReservationFleetsResultTypeDef,
    DescribeCapacityReservationsResultTypeDef,
    DescribeCarrierGatewaysResultTypeDef,
    DescribeClassicLinkInstancesResultTypeDef,
    DescribeClientVpnAuthorizationRulesResultTypeDef,
    DescribeClientVpnConnectionsResultTypeDef,
    DescribeClientVpnEndpointsResultTypeDef,
    DescribeClientVpnRoutesResultTypeDef,
    DescribeClientVpnTargetNetworksResultTypeDef,
    DescribeCoipPoolsResultTypeDef,
    DescribeConversionTasksResultTypeDef,
    DescribeCustomerGatewaysResultTypeDef,
    DescribeDhcpOptionsResultTypeDef,
    DescribeEgressOnlyInternetGatewaysResultTypeDef,
    DescribeElasticGpusResultTypeDef,
    DescribeExportImageTasksResultTypeDef,
    DescribeExportTasksResultTypeDef,
    DescribeFastLaunchImagesResultTypeDef,
    DescribeFastSnapshotRestoresResultTypeDef,
    DescribeFleetHistoryResultTypeDef,
    DescribeFleetInstancesResultTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeFlowLogsResultTypeDef,
    DescribeFpgaImageAttributeResultTypeDef,
    DescribeFpgaImagesResultTypeDef,
    DescribeHostReservationOfferingsResultTypeDef,
    DescribeHostReservationsResultTypeDef,
    DescribeHostsResultTypeDef,
    DescribeIamInstanceProfileAssociationsResultTypeDef,
    DescribeIdentityIdFormatResultTypeDef,
    DescribeIdFormatResultTypeDef,
    DescribeImagesResultTypeDef,
    DescribeImportImageTasksResultTypeDef,
    DescribeImportSnapshotTasksResultTypeDef,
    DescribeInstanceConnectEndpointsResultTypeDef,
    DescribeInstanceCreditSpecificationsResultTypeDef,
    DescribeInstanceEventNotificationAttributesResultTypeDef,
    DescribeInstanceEventWindowsResultTypeDef,
    DescribeInstancesResultTypeDef,
    DescribeInstanceStatusResultTypeDef,
    DescribeInstanceTopologyResultTypeDef,
    DescribeInstanceTypeOfferingsResultTypeDef,
    DescribeInstanceTypesResultTypeDef,
    DescribeInternetGatewaysResultTypeDef,
    DescribeIpamByoasnResultTypeDef,
    DescribeIpamPoolsResultTypeDef,
    DescribeIpamResourceDiscoveriesResultTypeDef,
    DescribeIpamResourceDiscoveryAssociationsResultTypeDef,
    DescribeIpamScopesResultTypeDef,
    DescribeIpamsResultTypeDef,
    DescribeIpv6PoolsResultTypeDef,
    DescribeKeyPairsResultTypeDef,
    DescribeLaunchTemplatesResultTypeDef,
    DescribeLaunchTemplateVersionsResultTypeDef,
    DescribeLocalGatewayRouteTablesResultTypeDef,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef,
    DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef,
    DescribeLocalGatewaysResultTypeDef,
    DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef,
    DescribeLocalGatewayVirtualInterfacesResultTypeDef,
    DescribeLockedSnapshotsResultTypeDef,
    DescribeManagedPrefixListsResultTypeDef,
    DescribeMovingAddressesResultTypeDef,
    DescribeNatGatewaysResultTypeDef,
    DescribeNetworkAclsResultTypeDef,
    DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef,
    DescribeNetworkInsightsAccessScopesResultTypeDef,
    DescribeNetworkInsightsAnalysesResultTypeDef,
    DescribeNetworkInsightsPathsResultTypeDef,
    DescribeNetworkInterfaceAttributeResultTypeDef,
    DescribeNetworkInterfacePermissionsResultTypeDef,
    DescribeNetworkInterfacesResultTypeDef,
    DescribePlacementGroupsResultTypeDef,
    DescribePrefixListsResultTypeDef,
    DescribePrincipalIdFormatResultTypeDef,
    DescribePublicIpv4PoolsResultTypeDef,
    DescribeRegionsResultTypeDef,
    DescribeReplaceRootVolumeTasksResultTypeDef,
    DescribeReservedInstancesListingsResultTypeDef,
    DescribeReservedInstancesModificationsResultTypeDef,
    DescribeReservedInstancesOfferingsResultTypeDef,
    DescribeReservedInstancesResultTypeDef,
    DescribeRouteTablesResultTypeDef,
    DescribeScheduledInstanceAvailabilityResultTypeDef,
    DescribeScheduledInstancesResultTypeDef,
    DescribeSecurityGroupReferencesResultTypeDef,
    DescribeSecurityGroupRulesResultTypeDef,
    DescribeSecurityGroupsResultTypeDef,
    DescribeSnapshotAttributeResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeSnapshotTierStatusResultTypeDef,
    DescribeSpotDatafeedSubscriptionResultTypeDef,
    DescribeSpotFleetInstancesResponseTypeDef,
    DescribeSpotFleetRequestHistoryResponseTypeDef,
    DescribeSpotFleetRequestsResponseTypeDef,
    DescribeSpotInstanceRequestsResultTypeDef,
    DescribeSpotPriceHistoryResultTypeDef,
    DescribeStaleSecurityGroupsResultTypeDef,
    DescribeStoreImageTasksResultTypeDef,
    DescribeSubnetsResultTypeDef,
    DescribeTagsResultTypeDef,
    DescribeTrafficMirrorFiltersResultTypeDef,
    DescribeTrafficMirrorSessionsResultTypeDef,
    DescribeTrafficMirrorTargetsResultTypeDef,
    DescribeTransitGatewayAttachmentsResultTypeDef,
    DescribeTransitGatewayConnectPeersResultTypeDef,
    DescribeTransitGatewayConnectsResultTypeDef,
    DescribeTransitGatewayMulticastDomainsResultTypeDef,
    DescribeTransitGatewayPeeringAttachmentsResultTypeDef,
    DescribeTransitGatewayPolicyTablesResultTypeDef,
    DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef,
    DescribeTransitGatewayRouteTablesResultTypeDef,
    DescribeTransitGatewaysResultTypeDef,
    DescribeTransitGatewayVpcAttachmentsResultTypeDef,
    DescribeTrunkInterfaceAssociationsResultTypeDef,
    DescribeVerifiedAccessEndpointsResultTypeDef,
    DescribeVerifiedAccessGroupsResultTypeDef,
    DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef,
    DescribeVerifiedAccessInstancesResultTypeDef,
    DescribeVerifiedAccessTrustProvidersResultTypeDef,
    DescribeVolumeAttributeResultTypeDef,
    DescribeVolumesModificationsResultTypeDef,
    DescribeVolumesResultTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcAttributeResultTypeDef,
    DescribeVpcClassicLinkDnsSupportResultTypeDef,
    DescribeVpcClassicLinkResultTypeDef,
    DescribeVpcEndpointConnectionNotificationsResultTypeDef,
    DescribeVpcEndpointConnectionsResultTypeDef,
    DescribeVpcEndpointServiceConfigurationsResultTypeDef,
    DescribeVpcEndpointServicePermissionsResultTypeDef,
    DescribeVpcEndpointServicesResultTypeDef,
    DescribeVpcEndpointsResultTypeDef,
    DescribeVpcPeeringConnectionsResultTypeDef,
    DescribeVpcsResultTypeDef,
    DescribeVpnConnectionsResultTypeDef,
    DescribeVpnGatewaysResultTypeDef,
    DestinationOptionsRequestTypeDef,
    DetachClassicLinkVpcResultTypeDef,
    DetachVerifiedAccessTrustProviderResultTypeDef,
    DisableAddressTransferResultTypeDef,
    DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef,
    DisableEbsEncryptionByDefaultResultTypeDef,
    DisableFastLaunchResultTypeDef,
    DisableFastSnapshotRestoresResultTypeDef,
    DisableImageBlockPublicAccessResultTypeDef,
    DisableImageDeprecationResultTypeDef,
    DisableImageResultTypeDef,
    DisableIpamOrganizationAdminAccountResultTypeDef,
    DisableSerialConsoleAccessResultTypeDef,
    DisableSnapshotBlockPublicAccessResultTypeDef,
    DisableTransitGatewayRouteTablePropagationResultTypeDef,
    DisableVpcClassicLinkDnsSupportResultTypeDef,
    DisableVpcClassicLinkResultTypeDef,
    DisassociateClientVpnTargetNetworkResultTypeDef,
    DisassociateEnclaveCertificateIamRoleResultTypeDef,
    DisassociateIamInstanceProfileResultTypeDef,
    DisassociateInstanceEventWindowResultTypeDef,
    DisassociateIpamByoasnResultTypeDef,
    DisassociateIpamResourceDiscoveryResultTypeDef,
    DisassociateNatGatewayAddressResultTypeDef,
    DisassociateSubnetCidrBlockResultTypeDef,
    DisassociateTransitGatewayMulticastDomainResultTypeDef,
    DisassociateTransitGatewayPolicyTableResultTypeDef,
    DisassociateTransitGatewayRouteTableResultTypeDef,
    DisassociateTrunkInterfaceResultTypeDef,
    DisassociateVpcCidrBlockResultTypeDef,
    DiskImageDetailTypeDef,
    DiskImageTypeDef,
    DnsOptionsSpecificationTypeDef,
    DnsServersOptionsModifyStructureTypeDef,
    ElasticGpuSpecificationTypeDef,
    ElasticInferenceAcceleratorTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableAddressTransferResultTypeDef,
    EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef,
    EnableEbsEncryptionByDefaultResultTypeDef,
    EnableFastLaunchResultTypeDef,
    EnableFastSnapshotRestoresResultTypeDef,
    EnableImageBlockPublicAccessResultTypeDef,
    EnableImageDeprecationResultTypeDef,
    EnableImageResultTypeDef,
    EnableIpamOrganizationAdminAccountResultTypeDef,
    EnableReachabilityAnalyzerOrganizationSharingResultTypeDef,
    EnableSerialConsoleAccessResultTypeDef,
    EnableSnapshotBlockPublicAccessResultTypeDef,
    EnableTransitGatewayRouteTablePropagationResultTypeDef,
    EnableVpcClassicLinkDnsSupportResultTypeDef,
    EnableVpcClassicLinkResultTypeDef,
    EnaSrdSpecificationTypeDef,
    EnclaveOptionsRequestTypeDef,
    ExportClientVpnClientCertificateRevocationListResultTypeDef,
    ExportClientVpnClientConfigurationResultTypeDef,
    ExportImageResultTypeDef,
    ExportTaskS3LocationRequestTypeDef,
    ExportToS3TaskSpecificationTypeDef,
    ExportTransitGatewayRoutesResultTypeDef,
    FastLaunchLaunchTemplateSpecificationRequestTypeDef,
    FastLaunchSnapshotConfigurationRequestTypeDef,
    FilterTypeDef,
    FleetLaunchTemplateConfigRequestTypeDef,
    GetAssociatedEnclaveCertificateIamRolesResultTypeDef,
    GetAssociatedIpv6PoolCidrsResultTypeDef,
    GetAwsNetworkPerformanceDataResultTypeDef,
    GetCapacityReservationUsageResultTypeDef,
    GetCoipPoolUsageResultTypeDef,
    GetConsoleOutputResultTypeDef,
    GetConsoleScreenshotResultTypeDef,
    GetDefaultCreditSpecificationResultTypeDef,
    GetEbsDefaultKmsKeyIdResultTypeDef,
    GetEbsEncryptionByDefaultResultTypeDef,
    GetFlowLogsIntegrationTemplateResultTypeDef,
    GetGroupsForCapacityReservationResultTypeDef,
    GetHostReservationPurchasePreviewResultTypeDef,
    GetImageBlockPublicAccessStateResultTypeDef,
    GetInstanceTypesFromInstanceRequirementsResultTypeDef,
    GetInstanceUefiDataResultTypeDef,
    GetIpamAddressHistoryResultTypeDef,
    GetIpamDiscoveredAccountsResultTypeDef,
    GetIpamDiscoveredPublicAddressesResultTypeDef,
    GetIpamDiscoveredResourceCidrsResultTypeDef,
    GetIpamPoolAllocationsResultTypeDef,
    GetIpamPoolCidrsResultTypeDef,
    GetIpamResourceCidrsResultTypeDef,
    GetLaunchTemplateDataResultTypeDef,
    GetManagedPrefixListAssociationsResultTypeDef,
    GetManagedPrefixListEntriesResultTypeDef,
    GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef,
    GetNetworkInsightsAccessScopeContentResultTypeDef,
    GetPasswordDataResultTypeDef,
    GetReservedInstancesExchangeQuoteResultTypeDef,
    GetSecurityGroupsForVpcResultTypeDef,
    GetSerialConsoleAccessStatusResultTypeDef,
    GetSnapshotBlockPublicAccessStateResultTypeDef,
    GetSpotPlacementScoresResultTypeDef,
    GetSubnetCidrReservationsResultTypeDef,
    GetTransitGatewayAttachmentPropagationsResultTypeDef,
    GetTransitGatewayMulticastDomainAssociationsResultTypeDef,
    GetTransitGatewayPolicyTableAssociationsResultTypeDef,
    GetTransitGatewayPolicyTableEntriesResultTypeDef,
    GetTransitGatewayPrefixListReferencesResultTypeDef,
    GetTransitGatewayRouteTableAssociationsResultTypeDef,
    GetTransitGatewayRouteTablePropagationsResultTypeDef,
    GetVerifiedAccessEndpointPolicyResultTypeDef,
    GetVerifiedAccessGroupPolicyResultTypeDef,
    GetVpnConnectionDeviceSampleConfigurationResultTypeDef,
    GetVpnConnectionDeviceTypesResultTypeDef,
    GetVpnTunnelReplacementStatusResultTypeDef,
    HibernationOptionsRequestTypeDef,
    IamInstanceProfileSpecificationTypeDef,
    IcmpTypeCodeTypeDef,
    ImageAttributeTypeDef,
    ImageDiskContainerTypeDef,
    ImportClientVpnClientCertificateRevocationListResultTypeDef,
    ImportImageLicenseConfigurationRequestTypeDef,
    ImportImageResultTypeDef,
    ImportInstanceLaunchSpecificationTypeDef,
    ImportInstanceResultTypeDef,
    ImportKeyPairResultTypeDef,
    ImportSnapshotResultTypeDef,
    ImportVolumeResultTypeDef,
    InstanceAttributeTypeDef,
    InstanceBlockDeviceMappingSpecificationTypeDef,
    InstanceCreditSpecificationRequestTypeDef,
    InstanceEventWindowAssociationRequestTypeDef,
    InstanceEventWindowDisassociationRequestTypeDef,
    InstanceEventWindowTimeRangeRequestTypeDef,
    InstanceIpv6AddressTypeDef,
    InstanceMaintenanceOptionsRequestTypeDef,
    InstanceMarketOptionsRequestTypeDef,
    InstanceMetadataOptionsRequestTypeDef,
    InstanceNetworkInterfaceSpecificationTypeDef,
    InstanceRequirementsRequestTypeDef,
    InstanceRequirementsWithMetadataRequestTypeDef,
    InstanceSpecificationTypeDef,
    IntegrateServicesTypeDef,
    IpamCidrAuthorizationContextTypeDef,
    IpamPoolSourceResourceRequestTypeDef,
    IpPermissionTypeDef,
    Ipv4PrefixSpecificationRequestTypeDef,
    Ipv6PrefixSpecificationRequestTypeDef,
    KeyPairTypeDef,
    LaunchPermissionModificationsTypeDef,
    LaunchTemplateConfigTypeDef,
    LaunchTemplateSpecificationTypeDef,
    LicenseConfigurationRequestTypeDef,
    ListImagesInRecycleBinResultTypeDef,
    ListSnapshotsInRecycleBinResultTypeDef,
    LoadPermissionModificationsTypeDef,
    LockSnapshotResultTypeDef,
    ModifyAddressAttributeResultTypeDef,
    ModifyAvailabilityZoneGroupResultTypeDef,
    ModifyCapacityReservationFleetResultTypeDef,
    ModifyCapacityReservationResultTypeDef,
    ModifyClientVpnEndpointResultTypeDef,
    ModifyDefaultCreditSpecificationResultTypeDef,
    ModifyEbsDefaultKmsKeyIdResultTypeDef,
    ModifyFleetResultTypeDef,
    ModifyFpgaImageAttributeResultTypeDef,
    ModifyHostsResultTypeDef,
    ModifyInstanceCapacityReservationAttributesResultTypeDef,
    ModifyInstanceCreditSpecificationResultTypeDef,
    ModifyInstanceEventStartTimeResultTypeDef,
    ModifyInstanceEventWindowResultTypeDef,
    ModifyInstanceMaintenanceOptionsResultTypeDef,
    ModifyInstanceMetadataOptionsResultTypeDef,
    ModifyInstancePlacementResultTypeDef,
    ModifyIpamPoolResultTypeDef,
    ModifyIpamResourceCidrResultTypeDef,
    ModifyIpamResourceDiscoveryResultTypeDef,
    ModifyIpamResultTypeDef,
    ModifyIpamScopeResultTypeDef,
    ModifyLaunchTemplateResultTypeDef,
    ModifyLocalGatewayRouteResultTypeDef,
    ModifyManagedPrefixListResultTypeDef,
    ModifyPrivateDnsNameOptionsResultTypeDef,
    ModifyReservedInstancesResultTypeDef,
    ModifySecurityGroupRulesResultTypeDef,
    ModifySnapshotTierResultTypeDef,
    ModifySpotFleetRequestResponseTypeDef,
    ModifyTrafficMirrorFilterNetworkServicesResultTypeDef,
    ModifyTrafficMirrorFilterRuleResultTypeDef,
    ModifyTrafficMirrorSessionResultTypeDef,
    ModifyTransitGatewayOptionsTypeDef,
    ModifyTransitGatewayPrefixListReferenceResultTypeDef,
    ModifyTransitGatewayResultTypeDef,
    ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef,
    ModifyTransitGatewayVpcAttachmentResultTypeDef,
    ModifyVerifiedAccessEndpointEniOptionsTypeDef,
    ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef,
    ModifyVerifiedAccessEndpointPolicyResultTypeDef,
    ModifyVerifiedAccessEndpointResultTypeDef,
    ModifyVerifiedAccessGroupPolicyResultTypeDef,
    ModifyVerifiedAccessGroupResultTypeDef,
    ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef,
    ModifyVerifiedAccessInstanceResultTypeDef,
    ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef,
    ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef,
    ModifyVerifiedAccessTrustProviderResultTypeDef,
    ModifyVolumeResultTypeDef,
    ModifyVpcEndpointConnectionNotificationResultTypeDef,
    ModifyVpcEndpointResultTypeDef,
    ModifyVpcEndpointServiceConfigurationResultTypeDef,
    ModifyVpcEndpointServicePayerResponsibilityResultTypeDef,
    ModifyVpcEndpointServicePermissionsResultTypeDef,
    ModifyVpcPeeringConnectionOptionsResultTypeDef,
    ModifyVpcTenancyResultTypeDef,
    ModifyVpnConnectionOptionsResultTypeDef,
    ModifyVpnConnectionResultTypeDef,
    ModifyVpnTunnelCertificateResultTypeDef,
    ModifyVpnTunnelOptionsResultTypeDef,
    ModifyVpnTunnelOptionsSpecificationTypeDef,
    MonitorInstancesResultTypeDef,
    MoveAddressToVpcResultTypeDef,
    MoveByoipCidrToIpamResultTypeDef,
    NetworkInterfaceAttachmentChangesTypeDef,
    NewDhcpConfigurationTypeDef,
    OnDemandOptionsRequestTypeDef,
    PathRequestFilterTypeDef,
    PeeringConnectionOptionsRequestTypeDef,
    PlacementTypeDef,
    PortRangeTypeDef,
    PriceScheduleSpecificationTypeDef,
    PrivateDnsNameOptionsRequestTypeDef,
    PrivateIpAddressSpecificationTypeDef,
    ProvisionByoipCidrResultTypeDef,
    ProvisionIpamByoasnResultTypeDef,
    ProvisionIpamPoolCidrResultTypeDef,
    ProvisionPublicIpv4PoolCidrResultTypeDef,
    PurchaseCapacityBlockResultTypeDef,
    PurchaseHostReservationResultTypeDef,
    PurchaseRequestTypeDef,
    PurchaseReservedInstancesOfferingResultTypeDef,
    PurchaseScheduledInstancesResultTypeDef,
    RegisterImageResultTypeDef,
    RegisterInstanceEventNotificationAttributesResultTypeDef,
    RegisterInstanceTagAttributeRequestTypeDef,
    RegisterTransitGatewayMulticastGroupMembersResultTypeDef,
    RegisterTransitGatewayMulticastGroupSourcesResultTypeDef,
    RejectTransitGatewayMulticastDomainAssociationsResultTypeDef,
    RejectTransitGatewayPeeringAttachmentResultTypeDef,
    RejectTransitGatewayVpcAttachmentResultTypeDef,
    RejectVpcEndpointConnectionsResultTypeDef,
    RejectVpcPeeringConnectionResultTypeDef,
    ReleaseHostsResultTypeDef,
    ReleaseIpamPoolAllocationResultTypeDef,
    RemoveIpamOperatingRegionTypeDef,
    RemovePrefixListEntryTypeDef,
    ReplaceIamInstanceProfileAssociationResultTypeDef,
    ReplaceNetworkAclAssociationResultTypeDef,
    ReplaceRouteTableAssociationResultTypeDef,
    ReplaceTransitGatewayRouteResultTypeDef,
    ReplaceVpnTunnelResultTypeDef,
    RequestIpamResourceTagTypeDef,
    RequestLaunchTemplateDataTypeDef,
    RequestSpotFleetResponseTypeDef,
    RequestSpotInstancesResultTypeDef,
    RequestSpotLaunchSpecificationTypeDef,
    ReservationFleetInstanceSpecificationTypeDef,
    ReservationResponseTypeDef,
    ReservedInstanceLimitPriceTypeDef,
    ReservedInstancesConfigurationTypeDef,
    ResetAddressAttributeResultTypeDef,
    ResetEbsDefaultKmsKeyIdResultTypeDef,
    ResetFpgaImageAttributeResultTypeDef,
    RestoreAddressToClassicResultTypeDef,
    RestoreImageFromRecycleBinResultTypeDef,
    RestoreManagedPrefixListVersionResultTypeDef,
    RestoreSnapshotFromRecycleBinResultTypeDef,
    RestoreSnapshotTierResultTypeDef,
    RevokeClientVpnIngressResultTypeDef,
    RevokeSecurityGroupEgressResultTypeDef,
    RevokeSecurityGroupIngressResultTypeDef,
    RunInstancesMonitoringEnabledTypeDef,
    RunScheduledInstancesResultTypeDef,
    S3ObjectTagTypeDef,
    ScheduledInstanceRecurrenceRequestTypeDef,
    ScheduledInstancesLaunchSpecificationTypeDef,
    SearchLocalGatewayRoutesResultTypeDef,
    SearchTransitGatewayMulticastGroupsResultTypeDef,
    SearchTransitGatewayRoutesResultTypeDef,
    SecurityGroupRuleDescriptionTypeDef,
    SecurityGroupRuleUpdateTypeDef,
    SlotDateTimeRangeRequestTypeDef,
    SlotStartTimeRangeRequestTypeDef,
    SnapshotDiskContainerTypeDef,
    SnapshotResponseTypeDef,
    SpotFleetRequestConfigDataTypeDef,
    SpotOptionsRequestTypeDef,
    StartInstancesResultTypeDef,
    StartNetworkInsightsAccessScopeAnalysisResultTypeDef,
    StartNetworkInsightsAnalysisResultTypeDef,
    StartVpcEndpointServicePrivateDnsVerificationResultTypeDef,
    StopInstancesResultTypeDef,
    StorageLocationTypeDef,
    StorageTypeDef,
    SubnetConfigurationTypeDef,
    TagSpecificationTypeDef,
    TagTypeDef,
    TargetCapacitySpecificationRequestTypeDef,
    TargetConfigurationRequestTypeDef,
    TerminateClientVpnConnectionsResultTypeDef,
    TerminateInstancesResultTypeDef,
    TimestampTypeDef,
    TrafficMirrorPortRangeRequestTypeDef,
    TransitGatewayConnectRequestBgpOptionsTypeDef,
    TransitGatewayRequestOptionsTypeDef,
    UnassignIpv6AddressesResultTypeDef,
    UnassignPrivateNatGatewayAddressResultTypeDef,
    UnlockSnapshotResultTypeDef,
    UnmonitorInstancesResultTypeDef,
    UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef,
    UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef,
    VerifiedAccessLogOptionsTypeDef,
    VerifiedAccessSseSpecificationRequestTypeDef,
    VolumeAttachmentTypeDef,
    VolumeDetailTypeDef,
    VolumeResponseTypeDef,
    VpnConnectionOptionsSpecificationTypeDef,
    WithdrawByoipCidrResultTypeDef,
)
from .waiter import (
    BundleTaskCompleteWaiter,
    ConversionTaskCancelledWaiter,
    ConversionTaskCompletedWaiter,
    ConversionTaskDeletedWaiter,
    CustomerGatewayAvailableWaiter,
    ExportTaskCancelledWaiter,
    ExportTaskCompletedWaiter,
    ImageAvailableWaiter,
    ImageExistsWaiter,
    InstanceExistsWaiter,
    InstanceRunningWaiter,
    InstanceStatusOkWaiter,
    InstanceStoppedWaiter,
    InstanceTerminatedWaiter,
    InternetGatewayExistsWaiter,
    KeyPairExistsWaiter,
    NatGatewayAvailableWaiter,
    NatGatewayDeletedWaiter,
    NetworkInterfaceAvailableWaiter,
    PasswordDataAvailableWaiter,
    SecurityGroupExistsWaiter,
    SnapshotCompletedWaiter,
    SnapshotImportedWaiter,
    SpotInstanceRequestFulfilledWaiter,
    StoreImageTaskCompleteWaiter,
    SubnetAvailableWaiter,
    SystemStatusOkWaiter,
    VolumeAvailableWaiter,
    VolumeDeletedWaiter,
    VolumeInUseWaiter,
    VpcAvailableWaiter,
    VpcExistsWaiter,
    VpcPeeringConnectionDeletedWaiter,
    VpcPeeringConnectionExistsWaiter,
    VpnConnectionAvailableWaiter,
    VpnConnectionDeletedWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EC2Client",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]


class EC2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EC2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.exceptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#exceptions)
        """

    def accept_address_transfer(
        self,
        *,
        Address: str,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> AcceptAddressTransferResultTypeDef:
        """
        Accepts an Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_address_transfer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_address_transfer)
        """

    def accept_reserved_instances_exchange_quote(
        self,
        *,
        ReservedInstanceIds: Sequence[str],
        DryRun: bool = ...,
        TargetConfigurations: Sequence[TargetConfigurationRequestTypeDef] = ...
    ) -> AcceptReservedInstancesExchangeQuoteResultTypeDef:
        """
        Accepts the Convertible Reserved Instance exchange quote described in the
        GetReservedInstancesExchangeQuote
        call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_reserved_instances_exchange_quote)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_reserved_instances_exchange_quote)
        """

    def accept_transit_gateway_multicast_domain_associations(
        self,
        *,
        TransitGatewayMulticastDomainId: str = ...,
        TransitGatewayAttachmentId: str = ...,
        SubnetIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        Accepts a request to associate subnets with a transit gateway multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_transit_gateway_multicast_domain_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_transit_gateway_multicast_domain_associations)
        """

    def accept_transit_gateway_peering_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = ...
    ) -> AcceptTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Accepts a transit gateway peering attachment request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_transit_gateway_peering_attachment)
        """

    def accept_transit_gateway_vpc_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = ...
    ) -> AcceptTransitGatewayVpcAttachmentResultTypeDef:
        """
        Accepts a request to attach a VPC to a transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_transit_gateway_vpc_attachment)
        """

    def accept_vpc_endpoint_connections(
        self, *, ServiceId: str, VpcEndpointIds: Sequence[str], DryRun: bool = ...
    ) -> AcceptVpcEndpointConnectionsResultTypeDef:
        """
        Accepts connection requests to your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_vpc_endpoint_connections)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_vpc_endpoint_connections)
        """

    def accept_vpc_peering_connection(
        self, *, VpcPeeringConnectionId: str, DryRun: bool = ...
    ) -> AcceptVpcPeeringConnectionResultTypeDef:
        """
        Accept a VPC peering connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.accept_vpc_peering_connection)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_vpc_peering_connection)
        """

    def advertise_byoip_cidr(
        self, *, Cidr: str, Asn: str = ..., DryRun: bool = ..., NetworkBorderGroup: str = ...
    ) -> AdvertiseByoipCidrResultTypeDef:
        """
        Advertises an IPv4 or IPv6 address range that is provisioned for use with your
        Amazon Web Services resources through bring your own IP addresses
        (BYOIP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.advertise_byoip_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#advertise_byoip_cidr)
        """

    def allocate_address(
        self,
        *,
        Domain: DomainTypeType = ...,
        Address: str = ...,
        PublicIpv4Pool: str = ...,
        NetworkBorderGroup: str = ...,
        CustomerOwnedIpv4Pool: str = ...,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> AllocateAddressResultTypeDef:
        """
        Allocates an Elastic IP address to your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.allocate_address)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#allocate_address)
        """

    def allocate_hosts(
        self,
        *,
        AvailabilityZone: str,
        AutoPlacement: AutoPlacementType = ...,
        ClientToken: str = ...,
        InstanceType: str = ...,
        InstanceFamily: str = ...,
        Quantity: int = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        HostRecovery: HostRecoveryType = ...,
        OutpostArn: str = ...,
        HostMaintenance: HostMaintenanceType = ...,
        AssetIds: Sequence[str] = ...
    ) -> AllocateHostsResultTypeDef:
        """
        Allocates a Dedicated Host to your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.allocate_hosts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#allocate_hosts)
        """

    def allocate_ipam_pool_cidr(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = ...,
        Cidr: str = ...,
        NetmaskLength: int = ...,
        ClientToken: str = ...,
        Description: str = ...,
        PreviewNextCidr: bool = ...,
        AllowedCidrs: Sequence[str] = ...,
        DisallowedCidrs: Sequence[str] = ...
    ) -> AllocateIpamPoolCidrResultTypeDef:
        """
        Allocate a CIDR from an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.allocate_ipam_pool_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#allocate_ipam_pool_cidr)
        """

    def apply_security_groups_to_client_vpn_target_network(
        self,
        *,
        ClientVpnEndpointId: str,
        VpcId: str,
        SecurityGroupIds: Sequence[str],
        DryRun: bool = ...
    ) -> ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef:
        """
        Applies a security group to the association between the target network and the
        Client VPN
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.apply_security_groups_to_client_vpn_target_network)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#apply_security_groups_to_client_vpn_target_network)
        """

    def assign_ipv6_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        Ipv6AddressCount: int = ...,
        Ipv6Addresses: Sequence[str] = ...,
        Ipv6PrefixCount: int = ...,
        Ipv6Prefixes: Sequence[str] = ...
    ) -> AssignIpv6AddressesResultTypeDef:
        """
        Assigns one or more IPv6 addresses to the specified network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.assign_ipv6_addresses)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#assign_ipv6_addresses)
        """

    def assign_private_ip_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        AllowReassignment: bool = ...,
        PrivateIpAddresses: Sequence[str] = ...,
        SecondaryPrivateIpAddressCount: int = ...,
        Ipv4Prefixes: Sequence[str] = ...,
        Ipv4PrefixCount: int = ...
    ) -> AssignPrivateIpAddressesResultTypeDef:
        """
        Assigns one or more secondary private IP addresses to the specified network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.assign_private_ip_addresses)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#assign_private_ip_addresses)
        """

    def assign_private_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        PrivateIpAddresses: Sequence[str] = ...,
        PrivateIpAddressCount: int = ...,
        DryRun: bool = ...
    ) -> AssignPrivateNatGatewayAddressResultTypeDef:
        """
        Assigns one or more private IPv4 addresses to a private NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.assign_private_nat_gateway_address)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#assign_private_nat_gateway_address)
        """

    def associate_address(
        self,
        *,
        AllocationId: str = ...,
        InstanceId: str = ...,
        PublicIp: str = ...,
        AllowReassociation: bool = ...,
        DryRun: bool = ...,
        NetworkInterfaceId: str = ...,
        PrivateIpAddress: str = ...
    ) -> AssociateAddressResultTypeDef:
        """
        Associates an Elastic IP address, or carrier IP address (for instances that are
        in subnets in Wavelength Zones) with an instance or a network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_address)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_address)
        """

    def associate_client_vpn_target_network(
        self, *, ClientVpnEndpointId: str, SubnetId: str, ClientToken: str = ..., DryRun: bool = ...
    ) -> AssociateClientVpnTargetNetworkResultTypeDef:
        """
        Associates a target network with a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_client_vpn_target_network)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_client_vpn_target_network)
        """

    def associate_dhcp_options(
        self, *, DhcpOptionsId: str, VpcId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a set of DHCP options (that you've previously created) with the
        specified VPC, or associates no DHCP options with the
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_dhcp_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_dhcp_options)
        """

    def associate_enclave_certificate_iam_role(
        self, *, CertificateArn: str, RoleArn: str, DryRun: bool = ...
    ) -> AssociateEnclaveCertificateIamRoleResultTypeDef:
        """
        Associates an Identity and Access Management (IAM) role with an Certificate
        Manager (ACM)
        certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_enclave_certificate_iam_role)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_enclave_certificate_iam_role)
        """

    def associate_iam_instance_profile(
        self, *, IamInstanceProfile: IamInstanceProfileSpecificationTypeDef, InstanceId: str
    ) -> AssociateIamInstanceProfileResultTypeDef:
        """
        Associates an IAM instance profile with a running or stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_iam_instance_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_iam_instance_profile)
        """

    def associate_instance_event_window(
        self,
        *,
        InstanceEventWindowId: str,
        AssociationTarget: InstanceEventWindowAssociationRequestTypeDef,
        DryRun: bool = ...
    ) -> AssociateInstanceEventWindowResultTypeDef:
        """
        Associates one or more targets with an event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_instance_event_window)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_instance_event_window)
        """

    def associate_ipam_byoasn(
        self, *, Asn: str, Cidr: str, DryRun: bool = ...
    ) -> AssociateIpamByoasnResultTypeDef:
        """
        Associates your Autonomous System Number (ASN) with a BYOIP CIDR that you own
        in the same Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_ipam_byoasn)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_ipam_byoasn)
        """

    def associate_ipam_resource_discovery(
        self,
        *,
        IpamId: str,
        IpamResourceDiscoveryId: str,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...
    ) -> AssociateIpamResourceDiscoveryResultTypeDef:
        """
        Associates an IPAM resource discovery with an Amazon VPC IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_ipam_resource_discovery)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_ipam_resource_discovery)
        """

    def associate_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        AllocationIds: Sequence[str],
        PrivateIpAddresses: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> AssociateNatGatewayAddressResultTypeDef:
        """
        Associates Elastic IP addresses (EIPs) and private IPv4 addresses with a public
        NAT
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_nat_gateway_address)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_nat_gateway_address)
        """

    def associate_route_table(
        self, *, RouteTableId: str, DryRun: bool = ..., SubnetId: str = ..., GatewayId: str = ...
    ) -> AssociateRouteTableResultTypeDef:
        """
        Associates a subnet in your VPC or an internet gateway or virtual private
        gateway attached to your VPC with a route table in your
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_route_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_route_table)
        """

    def associate_subnet_cidr_block(
        self,
        *,
        SubnetId: str,
        Ipv6CidrBlock: str = ...,
        Ipv6IpamPoolId: str = ...,
        Ipv6NetmaskLength: int = ...
    ) -> AssociateSubnetCidrBlockResultTypeDef:
        """
        Associates a CIDR block with your subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_subnet_cidr_block)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_subnet_cidr_block)
        """

    def associate_transit_gateway_multicast_domain(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        TransitGatewayAttachmentId: str,
        SubnetIds: Sequence[str],
        DryRun: bool = ...
    ) -> AssociateTransitGatewayMulticastDomainResultTypeDef:
        """
        Associates the specified subnets and transit gateway attachments with the
        specified transit gateway multicast
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_transit_gateway_multicast_domain)
        """

    def associate_transit_gateway_policy_table(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool = ...
    ) -> AssociateTransitGatewayPolicyTableResultTypeDef:
        """
        Associates the specified transit gateway attachment with a transit gateway
        policy
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_transit_gateway_policy_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_transit_gateway_policy_table)
        """

    def associate_transit_gateway_route_table(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool = ...
    ) -> AssociateTransitGatewayRouteTableResultTypeDef:
        """
        Associates the specified attachment with the specified transit gateway route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_transit_gateway_route_table)
        """

    def associate_trunk_interface(
        self,
        *,
        BranchInterfaceId: str,
        TrunkInterfaceId: str,
        VlanId: int = ...,
        GreKey: int = ...,
        ClientToken: str = ...,
        DryRun: bool = ...
    ) -> AssociateTrunkInterfaceResultTypeDef:
        """
        Associates a branch network interface with a trunk network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_trunk_interface)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_trunk_interface)
        """

    def associate_vpc_cidr_block(
        self,
        *,
        VpcId: str,
        AmazonProvidedIpv6CidrBlock: bool = ...,
        CidrBlock: str = ...,
        Ipv6CidrBlockNetworkBorderGroup: str = ...,
        Ipv6Pool: str = ...,
        Ipv6CidrBlock: str = ...,
        Ipv4IpamPoolId: str = ...,
        Ipv4NetmaskLength: int = ...,
        Ipv6IpamPoolId: str = ...,
        Ipv6NetmaskLength: int = ...
    ) -> AssociateVpcCidrBlockResultTypeDef:
        """
        Associates a CIDR block with your VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.associate_vpc_cidr_block)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_vpc_cidr_block)
        """

    def attach_classic_link_vpc(
        self, *, Groups: Sequence[str], InstanceId: str, VpcId: str, DryRun: bool = ...
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.attach_classic_link_vpc)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_classic_link_vpc)
        """

    def attach_internet_gateway(
        self, *, InternetGatewayId: str, VpcId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches an internet gateway or a virtual private gateway to a VPC, enabling
        connectivity between the internet and the
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.attach_internet_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_internet_gateway)
        """

    def attach_network_interface(
        self,
        *,
        DeviceIndex: int,
        InstanceId: str,
        NetworkInterfaceId: str,
        DryRun: bool = ...,
        NetworkCardIndex: int = ...,
        EnaSrdSpecification: EnaSrdSpecificationTypeDef = ...
    ) -> AttachNetworkInterfaceResultTypeDef:
        """
        Attaches a network interface to an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.attach_network_interface)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_network_interface)
        """

    def attach_verified_access_trust_provider(
        self,
        *,
        VerifiedAccessInstanceId: str,
        VerifiedAccessTrustProviderId: str,
        ClientToken: str = ...,
        DryRun: bool = ...
    ) -> AttachVerifiedAccessTrustProviderResultTypeDef:
        """
        Attaches the specified Amazon Web Services Verified Access trust provider to
        the specified Amazon Web Services Verified Access
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.attach_verified_access_trust_provider)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_verified_access_trust_provider)
        """

    def attach_volume(
        self, *, Device: str, InstanceId: str, VolumeId: str, DryRun: bool = ...
    ) -> VolumeAttachmentTypeDef:
        """
        Attaches an EBS volume to a running or stopped instance and exposes it to the
        instance with the specified device
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.attach_volume)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_volume)
        """

    def attach_vpn_gateway(
        self, *, VpcId: str, VpnGatewayId: str, DryRun: bool = ...
    ) -> AttachVpnGatewayResultTypeDef:
        """
        Attaches a virtual private gateway to a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.attach_vpn_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_vpn_gateway)
        """

    def authorize_client_vpn_ingress(
        self,
        *,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str = ...,
        AuthorizeAllGroups: bool = ...,
        Description: str = ...,
        ClientToken: str = ...,
        DryRun: bool = ...
    ) -> AuthorizeClientVpnIngressResultTypeDef:
        """
        Adds an ingress authorization rule to a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.authorize_client_vpn_ingress)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#authorize_client_vpn_ingress)
        """

    def authorize_security_group_egress(
        self,
        *,
        GroupId: str,
        DryRun: bool = ...,
        IpPermissions: Sequence[IpPermissionTypeDef] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        CidrIp: str = ...,
        FromPort: int = ...,
        IpProtocol: str = ...,
        ToPort: int = ...,
        SourceSecurityGroupName: str = ...,
        SourceSecurityGroupOwnerId: str = ...
    ) -> AuthorizeSecurityGroupEgressResultTypeDef:
        """
        Adds the specified outbound (egress) rules to a security group for use with a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.authorize_security_group_egress)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#authorize_security_group_egress)
        """

    def authorize_security_group_ingress(
        self,
        *,
        CidrIp: str = ...,
        FromPort: int = ...,
        GroupId: str = ...,
        GroupName: str = ...,
        IpPermissions: Sequence[IpPermissionTypeDef] = ...,
        IpProtocol: str = ...,
        SourceSecurityGroupName: str = ...,
        SourceSecurityGroupOwnerId: str = ...,
        ToPort: int = ...,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> AuthorizeSecurityGroupIngressResultTypeDef:
        """
        Adds the specified inbound (ingress) rules to a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.authorize_security_group_ingress)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#authorize_security_group_ingress)
        """

    def bundle_instance(
        self, *, InstanceId: str, Storage: StorageTypeDef, DryRun: bool = ...
    ) -> BundleInstanceResultTypeDef:
        """
        Bundles an Amazon instance store-backed Windows instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.bundle_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#bundle_instance)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.can_paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#can_paginate)
        """

    def cancel_bundle_task(
        self, *, BundleId: str, DryRun: bool = ...
    ) -> CancelBundleTaskResultTypeDef:
        """
        Cancels a bundling operation for an instance store-backed Windows instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_bundle_task)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_bundle_task)
        """

    def cancel_capacity_reservation(
        self, *, CapacityReservationId: str, DryRun: bool = ...
    ) -> CancelCapacityReservationResultTypeDef:
        """
        Cancels the specified Capacity Reservation, releases the reserved capacity, and
        changes the Capacity Reservation's state to
        `cancelled`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_capacity_reservation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_capacity_reservation)
        """

    def cancel_capacity_reservation_fleets(
        self, *, CapacityReservationFleetIds: Sequence[str], DryRun: bool = ...
    ) -> CancelCapacityReservationFleetsResultTypeDef:
        """
        Cancels one or more Capacity Reservation Fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_capacity_reservation_fleets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_capacity_reservation_fleets)
        """

    def cancel_conversion_task(
        self, *, ConversionTaskId: str, DryRun: bool = ..., ReasonMessage: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Cancels an active conversion task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_conversion_task)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_conversion_task)
        """

    def cancel_export_task(self, *, ExportTaskId: str) -> EmptyResponseMetadataTypeDef:
        """
        Cancels an active export task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_export_task)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_export_task)
        """

    def cancel_image_launch_permission(
        self, *, ImageId: str, DryRun: bool = ...
    ) -> CancelImageLaunchPermissionResultTypeDef:
        """
        Removes your Amazon Web Services account from the launch permissions for the
        specified
        AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_image_launch_permission)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_image_launch_permission)
        """

    def cancel_import_task(
        self, *, CancelReason: str = ..., DryRun: bool = ..., ImportTaskId: str = ...
    ) -> CancelImportTaskResultTypeDef:
        """
        Cancels an in-process import virtual machine or import snapshot task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_import_task)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_import_task)
        """

    def cancel_reserved_instances_listing(
        self, *, ReservedInstancesListingId: str
    ) -> CancelReservedInstancesListingResultTypeDef:
        """
        Cancels the specified Reserved Instance listing in the Reserved Instance
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_reserved_instances_listing)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_reserved_instances_listing)
        """

    def cancel_spot_fleet_requests(
        self, *, SpotFleetRequestIds: Sequence[str], TerminateInstances: bool, DryRun: bool = ...
    ) -> CancelSpotFleetRequestsResponseTypeDef:
        """
        Cancels the specified Spot Fleet requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_spot_fleet_requests)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_spot_fleet_requests)
        """

    def cancel_spot_instance_requests(
        self, *, SpotInstanceRequestIds: Sequence[str], DryRun: bool = ...
    ) -> CancelSpotInstanceRequestsResultTypeDef:
        """
        Cancels one or more Spot Instance requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.cancel_spot_instance_requests)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_spot_instance_requests)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.close)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#close)
        """

    def confirm_product_instance(
        self, *, InstanceId: str, ProductCode: str, DryRun: bool = ...
    ) -> ConfirmProductInstanceResultTypeDef:
        """
        Determines whether a product code is associated with an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.confirm_product_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#confirm_product_instance)
        """

    def copy_fpga_image(
        self,
        *,
        SourceFpgaImageId: str,
        SourceRegion: str,
        DryRun: bool = ...,
        Description: str = ...,
        Name: str = ...,
        ClientToken: str = ...
    ) -> CopyFpgaImageResultTypeDef:
        """
        Copies the specified Amazon FPGA Image (AFI) to the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.copy_fpga_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#copy_fpga_image)
        """

    def copy_image(
        self,
        *,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        ClientToken: str = ...,
        Description: str = ...,
        Encrypted: bool = ...,
        KmsKeyId: str = ...,
        DestinationOutpostArn: str = ...,
        DryRun: bool = ...,
        CopyImageTags: bool = ...
    ) -> CopyImageResultTypeDef:
        """
        Initiates the copy of an AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.copy_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#copy_image)
        """

    def copy_snapshot(
        self,
        *,
        SourceRegion: str,
        SourceSnapshotId: str,
        Description: str = ...,
        DestinationOutpostArn: str = ...,
        DestinationRegion: str = ...,
        Encrypted: bool = ...,
        KmsKeyId: str = ...,
        PresignedUrl: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CopySnapshotResultTypeDef:
        """
        Copies a point-in-time snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.copy_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#copy_snapshot)
        """

    def create_capacity_reservation(
        self,
        *,
        InstanceType: str,
        InstancePlatform: CapacityReservationInstancePlatformType,
        InstanceCount: int,
        ClientToken: str = ...,
        AvailabilityZone: str = ...,
        AvailabilityZoneId: str = ...,
        Tenancy: CapacityReservationTenancyType = ...,
        EbsOptimized: bool = ...,
        EphemeralStorage: bool = ...,
        EndDate: TimestampTypeDef = ...,
        EndDateType: EndDateTypeType = ...,
        InstanceMatchCriteria: InstanceMatchCriteriaType = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
        OutpostArn: str = ...,
        PlacementGroupArn: str = ...
    ) -> CreateCapacityReservationResultTypeDef:
        """
        Creates a new Capacity Reservation with the specified attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_capacity_reservation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_capacity_reservation)
        """

    def create_capacity_reservation_fleet(
        self,
        *,
        InstanceTypeSpecifications: Sequence[ReservationFleetInstanceSpecificationTypeDef],
        TotalTargetCapacity: int,
        AllocationStrategy: str = ...,
        ClientToken: str = ...,
        Tenancy: Literal["default"] = ...,
        EndDate: TimestampTypeDef = ...,
        InstanceMatchCriteria: Literal["open"] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateCapacityReservationFleetResultTypeDef:
        """
        Creates a Capacity Reservation Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_capacity_reservation_fleet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_capacity_reservation_fleet)
        """

    def create_carrier_gateway(
        self,
        *,
        VpcId: str,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
        ClientToken: str = ...
    ) -> CreateCarrierGatewayResultTypeDef:
        """
        Creates a carrier gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_carrier_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_carrier_gateway)
        """

    def create_client_vpn_endpoint(
        self,
        *,
        ClientCidrBlock: str,
        ServerCertificateArn: str,
        AuthenticationOptions: Sequence[ClientVpnAuthenticationRequestTypeDef],
        ConnectionLogOptions: ConnectionLogOptionsTypeDef,
        DnsServers: Sequence[str] = ...,
        TransportProtocol: TransportProtocolType = ...,
        VpnPort: int = ...,
        Description: str = ...,
        SplitTunnel: bool = ...,
        DryRun: bool = ...,
        ClientToken: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        SecurityGroupIds: Sequence[str] = ...,
        VpcId: str = ...,
        SelfServicePortal: SelfServicePortalType = ...,
        ClientConnectOptions: ClientConnectOptionsTypeDef = ...,
        SessionTimeoutHours: int = ...,
        ClientLoginBannerOptions: ClientLoginBannerOptionsTypeDef = ...
    ) -> CreateClientVpnEndpointResultTypeDef:
        """
        Creates a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_client_vpn_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_client_vpn_endpoint)
        """

    def create_client_vpn_route(
        self,
        *,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str,
        Description: str = ...,
        ClientToken: str = ...,
        DryRun: bool = ...
    ) -> CreateClientVpnRouteResultTypeDef:
        """
        Adds a route to a network to a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_client_vpn_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_client_vpn_route)
        """

    def create_coip_cidr(
        self, *, Cidr: str, CoipPoolId: str, DryRun: bool = ...
    ) -> CreateCoipCidrResultTypeDef:
        """
        Creates a range of customer-owned IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_coip_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_coip_cidr)
        """

    def create_coip_pool(
        self,
        *,
        LocalGatewayRouteTableId: str,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateCoipPoolResultTypeDef:
        """
        Creates a pool of customer-owned IP (CoIP) addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_coip_pool)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_coip_pool)
        """

    def create_customer_gateway(
        self,
        *,
        Type: Literal["ipsec.1"],
        BgpAsn: int = ...,
        PublicIp: str = ...,
        CertificateArn: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DeviceName: str = ...,
        IpAddress: str = ...,
        DryRun: bool = ...
    ) -> CreateCustomerGatewayResultTypeDef:
        """
        Provides information to Amazon Web Services about your customer gateway device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_customer_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_customer_gateway)
        """

    def create_default_subnet(
        self, *, AvailabilityZone: str, DryRun: bool = ..., Ipv6Native: bool = ...
    ) -> CreateDefaultSubnetResultTypeDef:
        """
        Creates a default subnet with a size `/20` IPv4 CIDR block in the specified
        Availability Zone in your default
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_default_subnet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_default_subnet)
        """

    def create_default_vpc(self, *, DryRun: bool = ...) -> CreateDefaultVpcResultTypeDef:
        """
        Creates a default VPC with a size `/16` IPv4 CIDR block and a default subnet in
        each Availability
        Zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_default_vpc)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_default_vpc)
        """

    def create_dhcp_options(
        self,
        *,
        DhcpConfigurations: Sequence[NewDhcpConfigurationTypeDef],
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateDhcpOptionsResultTypeDef:
        """
        Creates a set of DHCP options for your VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_dhcp_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_dhcp_options)
        """

    def create_egress_only_internet_gateway(
        self,
        *,
        VpcId: str,
        ClientToken: str = ...,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateEgressOnlyInternetGatewayResultTypeDef:
        """
        [IPv6 only] Creates an egress-only internet gateway for your VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_egress_only_internet_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_egress_only_internet_gateway)
        """

    def create_fleet(
        self,
        *,
        LaunchTemplateConfigs: Sequence[FleetLaunchTemplateConfigRequestTypeDef],
        TargetCapacitySpecification: TargetCapacitySpecificationRequestTypeDef,
        DryRun: bool = ...,
        ClientToken: str = ...,
        SpotOptions: SpotOptionsRequestTypeDef = ...,
        OnDemandOptions: OnDemandOptionsRequestTypeDef = ...,
        ExcessCapacityTerminationPolicy: FleetExcessCapacityTerminationPolicyType = ...,
        TerminateInstancesWithExpiration: bool = ...,
        Type: FleetTypeType = ...,
        ValidFrom: TimestampTypeDef = ...,
        ValidUntil: TimestampTypeDef = ...,
        ReplaceUnhealthyInstances: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        Context: str = ...
    ) -> CreateFleetResultTypeDef:
        """
        Creates an EC2 Fleet that contains the configuration information for On-Demand
        Instances and Spot
        Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_fleet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_fleet)
        """

    def create_flow_logs(
        self,
        *,
        ResourceIds: Sequence[str],
        ResourceType: FlowLogsResourceTypeType,
        DryRun: bool = ...,
        ClientToken: str = ...,
        DeliverLogsPermissionArn: str = ...,
        DeliverCrossAccountRole: str = ...,
        LogGroupName: str = ...,
        TrafficType: TrafficTypeType = ...,
        LogDestinationType: LogDestinationTypeType = ...,
        LogDestination: str = ...,
        LogFormat: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        MaxAggregationInterval: int = ...,
        DestinationOptions: DestinationOptionsRequestTypeDef = ...
    ) -> CreateFlowLogsResultTypeDef:
        """
        Creates one or more flow logs to capture information about IP traffic for a
        specific network interface, subnet, or
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_flow_logs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_flow_logs)
        """

    def create_fpga_image(
        self,
        *,
        InputStorageLocation: StorageLocationTypeDef,
        DryRun: bool = ...,
        LogsStorageLocation: StorageLocationTypeDef = ...,
        Description: str = ...,
        Name: str = ...,
        ClientToken: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateFpgaImageResultTypeDef:
        """
        Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_fpga_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_fpga_image)
        """

    def create_image(
        self,
        *,
        InstanceId: str,
        Name: str,
        BlockDeviceMappings: Sequence[BlockDeviceMappingTypeDef] = ...,
        Description: str = ...,
        DryRun: bool = ...,
        NoReboot: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateImageResultTypeDef:
        """
        Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is
        either running or
        stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_image)
        """

    def create_instance_connect_endpoint(
        self,
        *,
        SubnetId: str,
        DryRun: bool = ...,
        SecurityGroupIds: Sequence[str] = ...,
        PreserveClientIp: bool = ...,
        ClientToken: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateInstanceConnectEndpointResultTypeDef:
        """
        Creates an EC2 Instance Connect Endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_instance_connect_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_instance_connect_endpoint)
        """

    def create_instance_event_window(
        self,
        *,
        DryRun: bool = ...,
        Name: str = ...,
        TimeRanges: Sequence[InstanceEventWindowTimeRangeRequestTypeDef] = ...,
        CronExpression: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateInstanceEventWindowResultTypeDef:
        """
        Creates an event window in which scheduled events for the associated Amazon EC2
        instances can
        run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_instance_event_window)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_instance_event_window)
        """

    def create_instance_export_task(
        self,
        *,
        ExportToS3Task: ExportToS3TaskSpecificationTypeDef,
        InstanceId: str,
        TargetEnvironment: ExportEnvironmentType,
        Description: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateInstanceExportTaskResultTypeDef:
        """
        Exports a running or stopped instance to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_instance_export_task)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_instance_export_task)
        """

    def create_internet_gateway(
        self, *, TagSpecifications: Sequence[TagSpecificationTypeDef] = ..., DryRun: bool = ...
    ) -> CreateInternetGatewayResultTypeDef:
        """
        Creates an internet gateway for use with a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_internet_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_internet_gateway)
        """

    def create_ipam(
        self,
        *,
        DryRun: bool = ...,
        Description: str = ...,
        OperatingRegions: Sequence[AddIpamOperatingRegionTypeDef] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
        Tier: IpamTierType = ...
    ) -> CreateIpamResultTypeDef:
        """
        Create an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_ipam)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_ipam)
        """

    def create_ipam_pool(
        self,
        *,
        IpamScopeId: str,
        AddressFamily: AddressFamilyType,
        DryRun: bool = ...,
        Locale: str = ...,
        SourceIpamPoolId: str = ...,
        Description: str = ...,
        AutoImport: bool = ...,
        PubliclyAdvertisable: bool = ...,
        AllocationMinNetmaskLength: int = ...,
        AllocationMaxNetmaskLength: int = ...,
        AllocationDefaultNetmaskLength: int = ...,
        AllocationResourceTags: Sequence[RequestIpamResourceTagTypeDef] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
        AwsService: Literal["ec2"] = ...,
        PublicIpSource: IpamPoolPublicIpSourceType = ...,
        SourceResource: IpamPoolSourceResourceRequestTypeDef = ...
    ) -> CreateIpamPoolResultTypeDef:
        """
        Create an IP address pool for Amazon VPC IP Address Manager (IPAM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_ipam_pool)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_ipam_pool)
        """

    def create_ipam_resource_discovery(
        self,
        *,
        DryRun: bool = ...,
        Description: str = ...,
        OperatingRegions: Sequence[AddIpamOperatingRegionTypeDef] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...
    ) -> CreateIpamResourceDiscoveryResultTypeDef:
        """
        Creates an IPAM resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_ipam_resource_discovery)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_ipam_resource_discovery)
        """

    def create_ipam_scope(
        self,
        *,
        IpamId: str,
        DryRun: bool = ...,
        Description: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...
    ) -> CreateIpamScopeResultTypeDef:
        """
        Create an IPAM scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_ipam_scope)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_ipam_scope)
        """

    def create_key_pair(
        self,
        *,
        KeyName: str,
        DryRun: bool = ...,
        KeyType: KeyTypeType = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        KeyFormat: KeyFormatType = ...
    ) -> KeyPairTypeDef:
        """
        Creates an ED25519 or 2048-bit RSA key pair with the specified name and in the
        specified PEM or PPK
        format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_key_pair)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_key_pair)
        """

    def create_launch_template(
        self,
        *,
        LaunchTemplateName: str,
        LaunchTemplateData: RequestLaunchTemplateDataTypeDef,
        DryRun: bool = ...,
        ClientToken: str = ...,
        VersionDescription: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateLaunchTemplateResultTypeDef:
        """
        Creates a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_launch_template)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_launch_template)
        """

    def create_launch_template_version(
        self,
        *,
        LaunchTemplateData: RequestLaunchTemplateDataTypeDef,
        DryRun: bool = ...,
        ClientToken: str = ...,
        LaunchTemplateId: str = ...,
        LaunchTemplateName: str = ...,
        SourceVersion: str = ...,
        VersionDescription: str = ...,
        ResolveAlias: bool = ...
    ) -> CreateLaunchTemplateVersionResultTypeDef:
        """
        Creates a new version of a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_launch_template_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_launch_template_version)
        """

    def create_local_gateway_route(
        self,
        *,
        LocalGatewayRouteTableId: str,
        DestinationCidrBlock: str = ...,
        LocalGatewayVirtualInterfaceGroupId: str = ...,
        DryRun: bool = ...,
        NetworkInterfaceId: str = ...,
        DestinationPrefixListId: str = ...
    ) -> CreateLocalGatewayRouteResultTypeDef:
        """
        Creates a static route for the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_local_gateway_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_local_gateway_route)
        """

    def create_local_gateway_route_table(
        self,
        *,
        LocalGatewayId: str,
        Mode: LocalGatewayRouteTableModeType = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateLocalGatewayRouteTableResultTypeDef:
        """
        Creates a local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_local_gateway_route_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_local_gateway_route_table)
        """

    def create_local_gateway_route_table_virtual_interface_group_association(
        self,
        *,
        LocalGatewayRouteTableId: str,
        LocalGatewayVirtualInterfaceGroupId: str,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef:
        """
        Creates a local gateway route table virtual interface group association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_local_gateway_route_table_virtual_interface_group_association)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_local_gateway_route_table_virtual_interface_group_association)
        """

    def create_local_gateway_route_table_vpc_association(
        self,
        *,
        LocalGatewayRouteTableId: str,
        VpcId: str,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateLocalGatewayRouteTableVpcAssociationResultTypeDef:
        """
        Associates the specified VPC with the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_local_gateway_route_table_vpc_association)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_local_gateway_route_table_vpc_association)
        """

    def create_managed_prefix_list(
        self,
        *,
        PrefixListName: str,
        MaxEntries: int,
        AddressFamily: str,
        DryRun: bool = ...,
        Entries: Sequence[AddPrefixListEntryTypeDef] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...
    ) -> CreateManagedPrefixListResultTypeDef:
        """
        Creates a managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_managed_prefix_list)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_managed_prefix_list)
        """

    def create_nat_gateway(
        self,
        *,
        SubnetId: str,
        AllocationId: str = ...,
        ClientToken: str = ...,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ConnectivityType: ConnectivityTypeType = ...,
        PrivateIpAddress: str = ...,
        SecondaryAllocationIds: Sequence[str] = ...,
        SecondaryPrivateIpAddresses: Sequence[str] = ...,
        SecondaryPrivateIpAddressCount: int = ...
    ) -> CreateNatGatewayResultTypeDef:
        """
        Creates a NAT gateway in the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_nat_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_nat_gateway)
        """

    def create_network_acl(
        self,
        *,
        VpcId: str,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateNetworkAclResultTypeDef:
        """
        Creates a network ACL in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_network_acl)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_acl)
        """

    def create_network_acl_entry(
        self,
        *,
        Egress: bool,
        NetworkAclId: str,
        Protocol: str,
        RuleAction: RuleActionType,
        RuleNumber: int,
        CidrBlock: str = ...,
        DryRun: bool = ...,
        IcmpTypeCode: IcmpTypeCodeTypeDef = ...,
        Ipv6CidrBlock: str = ...,
        PortRange: PortRangeTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates an entry (a rule) in a network ACL with the specified rule number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_network_acl_entry)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_acl_entry)
        """

    def create_network_insights_access_scope(
        self,
        *,
        ClientToken: str,
        MatchPaths: Sequence[AccessScopePathRequestTypeDef] = ...,
        ExcludePaths: Sequence[AccessScopePathRequestTypeDef] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateNetworkInsightsAccessScopeResultTypeDef:
        """
        Creates a Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_network_insights_access_scope)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_insights_access_scope)
        """

    def create_network_insights_path(
        self,
        *,
        Source: str,
        Protocol: ProtocolType,
        ClientToken: str,
        SourceIp: str = ...,
        DestinationIp: str = ...,
        Destination: str = ...,
        DestinationPort: int = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
        FilterAtSource: PathRequestFilterTypeDef = ...,
        FilterAtDestination: PathRequestFilterTypeDef = ...
    ) -> CreateNetworkInsightsPathResultTypeDef:
        """
        Creates a path to analyze for reachability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_network_insights_path)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_insights_path)
        """

    def create_network_interface(
        self,
        *,
        SubnetId: str,
        Description: str = ...,
        DryRun: bool = ...,
        Groups: Sequence[str] = ...,
        Ipv6AddressCount: int = ...,
        Ipv6Addresses: Sequence[InstanceIpv6AddressTypeDef] = ...,
        PrivateIpAddress: str = ...,
        PrivateIpAddresses: Sequence[PrivateIpAddressSpecificationTypeDef] = ...,
        SecondaryPrivateIpAddressCount: int = ...,
        Ipv4Prefixes: Sequence[Ipv4PrefixSpecificationRequestTypeDef] = ...,
        Ipv4PrefixCount: int = ...,
        Ipv6Prefixes: Sequence[Ipv6PrefixSpecificationRequestTypeDef] = ...,
        Ipv6PrefixCount: int = ...,
        InterfaceType: NetworkInterfaceCreationTypeType = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
        EnablePrimaryIpv6: bool = ...,
        ConnectionTrackingSpecification: ConnectionTrackingSpecificationRequestTypeDef = ...
    ) -> CreateNetworkInterfaceResultTypeDef:
        """
        Creates a network interface in the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_network_interface)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_interface)
        """

    def create_network_interface_permission(
        self,
        *,
        NetworkInterfaceId: str,
        Permission: InterfacePermissionTypeType,
        AwsAccountId: str = ...,
        AwsService: str = ...,
        DryRun: bool = ...
    ) -> CreateNetworkInterfacePermissionResultTypeDef:
        """
        Grants an Amazon Web Services-authorized account permission to attach the
        specified network interface to an instance in their
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_network_interface_permission)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_interface_permission)
        """

    def create_placement_group(
        self,
        *,
        DryRun: bool = ...,
        GroupName: str = ...,
        Strategy: PlacementStrategyType = ...,
        PartitionCount: int = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        SpreadLevel: SpreadLevelType = ...
    ) -> CreatePlacementGroupResultTypeDef:
        """
        Creates a placement group in which to launch instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_placement_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_placement_group)
        """

    def create_public_ipv4_pool(
        self, *, DryRun: bool = ..., TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreatePublicIpv4PoolResultTypeDef:
        """
        Creates a public IPv4 address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_public_ipv4_pool)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_public_ipv4_pool)
        """

    def create_replace_root_volume_task(
        self,
        *,
        InstanceId: str,
        SnapshotId: str = ...,
        ClientToken: str = ...,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ImageId: str = ...,
        DeleteReplacedRootVolume: bool = ...
    ) -> CreateReplaceRootVolumeTaskResultTypeDef:
        """
        Replaces the EBS-backed root volume for a `running` instance with a new volume
        that is restored to the original root volume's launch state, that is restored
        to a specific snapshot taken from the original root volume, or that is restored
        from an AMI that has the same key characteristics as that
        ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_replace_root_volume_task)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_replace_root_volume_task)
        """

    def create_reserved_instances_listing(
        self,
        *,
        ClientToken: str,
        InstanceCount: int,
        PriceSchedules: Sequence[PriceScheduleSpecificationTypeDef],
        ReservedInstancesId: str
    ) -> CreateReservedInstancesListingResultTypeDef:
        """
        Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the
        Reserved Instance
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_reserved_instances_listing)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_reserved_instances_listing)
        """

    def create_restore_image_task(
        self,
        *,
        Bucket: str,
        ObjectKey: str,
        Name: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateRestoreImageTaskResultTypeDef:
        """
        Starts a task that restores an AMI from an Amazon S3 object that was previously
        created by using
        [CreateStoreImageTask](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateStoreImageTask.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_restore_image_task)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_restore_image_task)
        """

    def create_route(
        self,
        *,
        RouteTableId: str,
        DestinationCidrBlock: str = ...,
        DestinationIpv6CidrBlock: str = ...,
        DestinationPrefixListId: str = ...,
        DryRun: bool = ...,
        VpcEndpointId: str = ...,
        EgressOnlyInternetGatewayId: str = ...,
        GatewayId: str = ...,
        InstanceId: str = ...,
        NatGatewayId: str = ...,
        TransitGatewayId: str = ...,
        LocalGatewayId: str = ...,
        CarrierGatewayId: str = ...,
        NetworkInterfaceId: str = ...,
        VpcPeeringConnectionId: str = ...,
        CoreNetworkArn: str = ...
    ) -> CreateRouteResultTypeDef:
        """
        Creates a route in a route table within a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_route)
        """

    def create_route_table(
        self,
        *,
        VpcId: str,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateRouteTableResultTypeDef:
        """
        Creates a route table for the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_route_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_route_table)
        """

    def create_security_group(
        self,
        *,
        Description: str,
        GroupName: str,
        VpcId: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateSecurityGroupResultTypeDef:
        """
        Creates a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_security_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_security_group)
        """

    def create_snapshot(
        self,
        *,
        VolumeId: str,
        Description: str = ...,
        OutpostArn: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> SnapshotResponseTypeDef:
        """
        Creates a snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_snapshot)
        """

    def create_snapshots(
        self,
        *,
        InstanceSpecification: InstanceSpecificationTypeDef,
        Description: str = ...,
        OutpostArn: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
        CopyTagsFromSource: Literal["volume"] = ...
    ) -> CreateSnapshotsResultTypeDef:
        """
        Creates crash-consistent snapshots of multiple EBS volumes and stores the data
        in
        S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_snapshots)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_snapshots)
        """

    def create_spot_datafeed_subscription(
        self, *, Bucket: str, DryRun: bool = ..., Prefix: str = ...
    ) -> CreateSpotDatafeedSubscriptionResultTypeDef:
        """
        Creates a data feed for Spot Instances, enabling you to view Spot Instance
        usage
        logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_spot_datafeed_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_spot_datafeed_subscription)
        """

    def create_store_image_task(
        self,
        *,
        ImageId: str,
        Bucket: str,
        S3ObjectTags: Sequence[S3ObjectTagTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateStoreImageTaskResultTypeDef:
        """
        Stores an AMI as a single object in an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_store_image_task)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_store_image_task)
        """

    def create_subnet(
        self,
        *,
        VpcId: str,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        AvailabilityZone: str = ...,
        AvailabilityZoneId: str = ...,
        CidrBlock: str = ...,
        Ipv6CidrBlock: str = ...,
        OutpostArn: str = ...,
        DryRun: bool = ...,
        Ipv6Native: bool = ...,
        Ipv4IpamPoolId: str = ...,
        Ipv4NetmaskLength: int = ...,
        Ipv6IpamPoolId: str = ...,
        Ipv6NetmaskLength: int = ...
    ) -> CreateSubnetResultTypeDef:
        """
        Creates a subnet in the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_subnet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_subnet)
        """

    def create_subnet_cidr_reservation(
        self,
        *,
        SubnetId: str,
        Cidr: str,
        ReservationType: SubnetCidrReservationTypeType,
        Description: str = ...,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateSubnetCidrReservationResultTypeDef:
        """
        Creates a subnet CIDR reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_subnet_cidr_reservation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_subnet_cidr_reservation)
        """

    def create_tags(
        self, *, Resources: Sequence[str], Tags: Sequence[TagTypeDef], DryRun: bool = ...
    ) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_tags)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_tags)
        """

    def create_traffic_mirror_filter(
        self,
        *,
        Description: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
        ClientToken: str = ...
    ) -> CreateTrafficMirrorFilterResultTypeDef:
        """
        Creates a Traffic Mirror filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_traffic_mirror_filter)
        """

    def create_traffic_mirror_filter_rule(
        self,
        *,
        TrafficMirrorFilterId: str,
        TrafficDirection: TrafficDirectionType,
        RuleNumber: int,
        RuleAction: TrafficMirrorRuleActionType,
        DestinationCidrBlock: str,
        SourceCidrBlock: str,
        DestinationPortRange: TrafficMirrorPortRangeRequestTypeDef = ...,
        SourcePortRange: TrafficMirrorPortRangeRequestTypeDef = ...,
        Protocol: int = ...,
        Description: str = ...,
        DryRun: bool = ...,
        ClientToken: str = ...
    ) -> CreateTrafficMirrorFilterRuleResultTypeDef:
        """
        Creates a Traffic Mirror filter rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter_rule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_traffic_mirror_filter_rule)
        """

    def create_traffic_mirror_session(
        self,
        *,
        NetworkInterfaceId: str,
        TrafficMirrorTargetId: str,
        TrafficMirrorFilterId: str,
        SessionNumber: int,
        PacketLength: int = ...,
        VirtualNetworkId: int = ...,
        Description: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
        ClientToken: str = ...
    ) -> CreateTrafficMirrorSessionResultTypeDef:
        """
        Creates a Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_traffic_mirror_session)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_traffic_mirror_session)
        """

    def create_traffic_mirror_target(
        self,
        *,
        NetworkInterfaceId: str = ...,
        NetworkLoadBalancerArn: str = ...,
        Description: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
        ClientToken: str = ...,
        GatewayLoadBalancerEndpointId: str = ...
    ) -> CreateTrafficMirrorTargetResultTypeDef:
        """
        Creates a target for your Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_traffic_mirror_target)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_traffic_mirror_target)
        """

    def create_transit_gateway(
        self,
        *,
        Description: str = ...,
        Options: TransitGatewayRequestOptionsTypeDef = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateTransitGatewayResultTypeDef:
        """
        Creates a transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway)
        """

    def create_transit_gateway_connect(
        self,
        *,
        TransportTransitGatewayAttachmentId: str,
        Options: CreateTransitGatewayConnectRequestOptionsTypeDef,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateTransitGatewayConnectResultTypeDef:
        """
        Creates a Connect attachment from a specified transit gateway attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_connect)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_connect)
        """

    def create_transit_gateway_connect_peer(
        self,
        *,
        TransitGatewayAttachmentId: str,
        PeerAddress: str,
        InsideCidrBlocks: Sequence[str],
        TransitGatewayAddress: str = ...,
        BgpOptions: TransitGatewayConnectRequestBgpOptionsTypeDef = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateTransitGatewayConnectPeerResultTypeDef:
        """
        Creates a Connect peer for a specified transit gateway Connect attachment
        between a transit gateway and an
        appliance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_connect_peer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_connect_peer)
        """

    def create_transit_gateway_multicast_domain(
        self,
        *,
        TransitGatewayId: str,
        Options: CreateTransitGatewayMulticastDomainRequestOptionsTypeDef = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateTransitGatewayMulticastDomainResultTypeDef:
        """
        Creates a multicast domain using the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_multicast_domain)
        """

    def create_transit_gateway_peering_attachment(
        self,
        *,
        TransitGatewayId: str,
        PeerTransitGatewayId: str,
        PeerAccountId: str,
        PeerRegion: str,
        Options: CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Requests a transit gateway peering attachment between the specified transit
        gateway (requester) and a peer transit gateway
        (accepter).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_peering_attachment)
        """

    def create_transit_gateway_policy_table(
        self,
        *,
        TransitGatewayId: str,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateTransitGatewayPolicyTableResultTypeDef:
        """
        Creates a transit gateway policy table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_policy_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_policy_table)
        """

    def create_transit_gateway_prefix_list_reference(
        self,
        *,
        TransitGatewayRouteTableId: str,
        PrefixListId: str,
        TransitGatewayAttachmentId: str = ...,
        Blackhole: bool = ...,
        DryRun: bool = ...
    ) -> CreateTransitGatewayPrefixListReferenceResultTypeDef:
        """
        Creates a reference (route) to a prefix list in a specified transit gateway
        route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_prefix_list_reference)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_prefix_list_reference)
        """

    def create_transit_gateway_route(
        self,
        *,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = ...,
        Blackhole: bool = ...,
        DryRun: bool = ...
    ) -> CreateTransitGatewayRouteResultTypeDef:
        """
        Creates a static route for the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_route)
        """

    def create_transit_gateway_route_table(
        self,
        *,
        TransitGatewayId: str,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateTransitGatewayRouteTableResultTypeDef:
        """
        Creates a route table for the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_route_table)
        """

    def create_transit_gateway_route_table_announcement(
        self,
        *,
        TransitGatewayRouteTableId: str,
        PeeringAttachmentId: str,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateTransitGatewayRouteTableAnnouncementResultTypeDef:
        """
        Advertises a new transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_route_table_announcement)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_route_table_announcement)
        """

    def create_transit_gateway_vpc_attachment(
        self,
        *,
        TransitGatewayId: str,
        VpcId: str,
        SubnetIds: Sequence[str],
        Options: CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...
    ) -> CreateTransitGatewayVpcAttachmentResultTypeDef:
        """
        Attaches the specified VPC to the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_vpc_attachment)
        """

    def create_verified_access_endpoint(
        self,
        *,
        VerifiedAccessGroupId: str,
        EndpointType: VerifiedAccessEndpointTypeType,
        AttachmentType: Literal["vpc"],
        DomainCertificateArn: str,
        ApplicationDomain: str,
        EndpointDomainPrefix: str,
        SecurityGroupIds: Sequence[str] = ...,
        LoadBalancerOptions: CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef = ...,
        NetworkInterfaceOptions: CreateVerifiedAccessEndpointEniOptionsTypeDef = ...,
        Description: str = ...,
        PolicyDocument: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
        DryRun: bool = ...,
        SseSpecification: VerifiedAccessSseSpecificationRequestTypeDef = ...
    ) -> CreateVerifiedAccessEndpointResultTypeDef:
        """
        An Amazon Web Services Verified Access endpoint is where you define your
        application along with an optional endpoint-level access
        policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_verified_access_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_verified_access_endpoint)
        """

    def create_verified_access_group(
        self,
        *,
        VerifiedAccessInstanceId: str,
        Description: str = ...,
        PolicyDocument: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
        DryRun: bool = ...,
        SseSpecification: VerifiedAccessSseSpecificationRequestTypeDef = ...
    ) -> CreateVerifiedAccessGroupResultTypeDef:
        """
        An Amazon Web Services Verified Access group is a collection of Amazon Web
        Services Verified Access endpoints who's associated applications have similar
        security
        requirements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_verified_access_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_verified_access_group)
        """

    def create_verified_access_instance(
        self,
        *,
        Description: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
        DryRun: bool = ...,
        FIPSEnabled: bool = ...
    ) -> CreateVerifiedAccessInstanceResultTypeDef:
        """
        An Amazon Web Services Verified Access instance is a regional entity that
        evaluates application requests and grants access only when your security
        requirements are
        met.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_verified_access_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_verified_access_instance)
        """

    def create_verified_access_trust_provider(
        self,
        *,
        TrustProviderType: TrustProviderTypeType,
        PolicyReferenceName: str,
        UserTrustProviderType: UserTrustProviderTypeType = ...,
        DeviceTrustProviderType: DeviceTrustProviderTypeType = ...,
        OidcOptions: CreateVerifiedAccessTrustProviderOidcOptionsTypeDef = ...,
        DeviceOptions: CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef = ...,
        Description: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
        DryRun: bool = ...,
        SseSpecification: VerifiedAccessSseSpecificationRequestTypeDef = ...
    ) -> CreateVerifiedAccessTrustProviderResultTypeDef:
        """
        A trust provider is a third-party entity that creates, maintains, and manages
        identity information for users and
        devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_verified_access_trust_provider)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_verified_access_trust_provider)
        """

    def create_volume(
        self,
        *,
        AvailabilityZone: str,
        Encrypted: bool = ...,
        Iops: int = ...,
        KmsKeyId: str = ...,
        OutpostArn: str = ...,
        Size: int = ...,
        SnapshotId: str = ...,
        VolumeType: VolumeTypeType = ...,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        MultiAttachEnabled: bool = ...,
        Throughput: int = ...,
        ClientToken: str = ...
    ) -> VolumeResponseTypeDef:
        """
        Creates an EBS volume that can be attached to an instance in the same
        Availability
        Zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_volume)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_volume)
        """

    def create_vpc(
        self,
        *,
        CidrBlock: str = ...,
        AmazonProvidedIpv6CidrBlock: bool = ...,
        Ipv6Pool: str = ...,
        Ipv6CidrBlock: str = ...,
        Ipv4IpamPoolId: str = ...,
        Ipv4NetmaskLength: int = ...,
        Ipv6IpamPoolId: str = ...,
        Ipv6NetmaskLength: int = ...,
        DryRun: bool = ...,
        InstanceTenancy: TenancyType = ...,
        Ipv6CidrBlockNetworkBorderGroup: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateVpcResultTypeDef:
        """
        Creates a VPC with the specified CIDR blocks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpc)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpc)
        """

    def create_vpc_endpoint(
        self,
        *,
        VpcId: str,
        ServiceName: str,
        DryRun: bool = ...,
        VpcEndpointType: VpcEndpointTypeType = ...,
        PolicyDocument: str = ...,
        RouteTableIds: Sequence[str] = ...,
        SubnetIds: Sequence[str] = ...,
        SecurityGroupIds: Sequence[str] = ...,
        IpAddressType: IpAddressTypeType = ...,
        DnsOptions: DnsOptionsSpecificationTypeDef = ...,
        ClientToken: str = ...,
        PrivateDnsEnabled: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        SubnetConfigurations: Sequence[SubnetConfigurationTypeDef] = ...
    ) -> CreateVpcEndpointResultTypeDef:
        """
        Creates a VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpc_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpc_endpoint)
        """

    def create_vpc_endpoint_connection_notification(
        self,
        *,
        ConnectionNotificationArn: str,
        ConnectionEvents: Sequence[str],
        DryRun: bool = ...,
        ServiceId: str = ...,
        VpcEndpointId: str = ...,
        ClientToken: str = ...
    ) -> CreateVpcEndpointConnectionNotificationResultTypeDef:
        """
        Creates a connection notification for a specified VPC endpoint or VPC endpoint
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_connection_notification)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpc_endpoint_connection_notification)
        """

    def create_vpc_endpoint_service_configuration(
        self,
        *,
        DryRun: bool = ...,
        AcceptanceRequired: bool = ...,
        PrivateDnsName: str = ...,
        NetworkLoadBalancerArns: Sequence[str] = ...,
        GatewayLoadBalancerArns: Sequence[str] = ...,
        SupportedIpAddressTypes: Sequence[str] = ...,
        ClientToken: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateVpcEndpointServiceConfigurationResultTypeDef:
        """
        Creates a VPC endpoint service to which service consumers (Amazon Web Services
        accounts, users, and IAM roles) can
        connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_service_configuration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpc_endpoint_service_configuration)
        """

    def create_vpc_peering_connection(
        self,
        *,
        VpcId: str,
        DryRun: bool = ...,
        PeerOwnerId: str = ...,
        PeerVpcId: str = ...,
        PeerRegion: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateVpcPeeringConnectionResultTypeDef:
        """
        Requests a VPC peering connection between two VPCs: a requester VPC that you
        own and an accepter VPC with which to create the
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpc_peering_connection)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpc_peering_connection)
        """

    def create_vpn_connection(
        self,
        *,
        CustomerGatewayId: str,
        Type: str,
        VpnGatewayId: str = ...,
        TransitGatewayId: str = ...,
        DryRun: bool = ...,
        Options: VpnConnectionOptionsSpecificationTypeDef = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> CreateVpnConnectionResultTypeDef:
        """
        Creates a VPN connection between an existing virtual private gateway or transit
        gateway and a customer
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpn_connection)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpn_connection)
        """

    def create_vpn_connection_route(
        self, *, DestinationCidrBlock: str, VpnConnectionId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a static route associated with a VPN connection between an existing
        virtual private gateway and a VPN customer
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpn_connection_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpn_connection_route)
        """

    def create_vpn_gateway(
        self,
        *,
        Type: Literal["ipsec.1"],
        AvailabilityZone: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        AmazonSideAsn: int = ...,
        DryRun: bool = ...
    ) -> CreateVpnGatewayResultTypeDef:
        """
        Creates a virtual private gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.create_vpn_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpn_gateway)
        """

    def delete_carrier_gateway(
        self, *, CarrierGatewayId: str, DryRun: bool = ...
    ) -> DeleteCarrierGatewayResultTypeDef:
        """
        Deletes a carrier gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_carrier_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_carrier_gateway)
        """

    def delete_client_vpn_endpoint(
        self, *, ClientVpnEndpointId: str, DryRun: bool = ...
    ) -> DeleteClientVpnEndpointResultTypeDef:
        """
        Deletes the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_client_vpn_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_client_vpn_endpoint)
        """

    def delete_client_vpn_route(
        self,
        *,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str = ...,
        DryRun: bool = ...
    ) -> DeleteClientVpnRouteResultTypeDef:
        """
        Deletes a route from a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_client_vpn_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_client_vpn_route)
        """

    def delete_coip_cidr(
        self, *, Cidr: str, CoipPoolId: str, DryRun: bool = ...
    ) -> DeleteCoipCidrResultTypeDef:
        """
        Deletes a range of customer-owned IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_coip_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_coip_cidr)
        """

    def delete_coip_pool(
        self, *, CoipPoolId: str, DryRun: bool = ...
    ) -> DeleteCoipPoolResultTypeDef:
        """
        Deletes a pool of customer-owned IP (CoIP) addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_coip_pool)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_coip_pool)
        """

    def delete_customer_gateway(
        self, *, CustomerGatewayId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified customer gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_customer_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_customer_gateway)
        """

    def delete_dhcp_options(
        self, *, DhcpOptionsId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified set of DHCP options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_dhcp_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_dhcp_options)
        """

    def delete_egress_only_internet_gateway(
        self, *, EgressOnlyInternetGatewayId: str, DryRun: bool = ...
    ) -> DeleteEgressOnlyInternetGatewayResultTypeDef:
        """
        Deletes an egress-only internet gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_egress_only_internet_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_egress_only_internet_gateway)
        """

    def delete_fleets(
        self, *, FleetIds: Sequence[str], TerminateInstances: bool, DryRun: bool = ...
    ) -> DeleteFleetsResultTypeDef:
        """
        Deletes the specified EC2 Fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_fleets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_fleets)
        """

    def delete_flow_logs(
        self, *, FlowLogIds: Sequence[str], DryRun: bool = ...
    ) -> DeleteFlowLogsResultTypeDef:
        """
        Deletes one or more flow logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_flow_logs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_flow_logs)
        """

    def delete_fpga_image(
        self, *, FpgaImageId: str, DryRun: bool = ...
    ) -> DeleteFpgaImageResultTypeDef:
        """
        Deletes the specified Amazon FPGA Image (AFI).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_fpga_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_fpga_image)
        """

    def delete_instance_connect_endpoint(
        self, *, InstanceConnectEndpointId: str, DryRun: bool = ...
    ) -> DeleteInstanceConnectEndpointResultTypeDef:
        """
        Deletes the specified EC2 Instance Connect Endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_instance_connect_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_instance_connect_endpoint)
        """

    def delete_instance_event_window(
        self, *, InstanceEventWindowId: str, DryRun: bool = ..., ForceDelete: bool = ...
    ) -> DeleteInstanceEventWindowResultTypeDef:
        """
        Deletes the specified event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_instance_event_window)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_instance_event_window)
        """

    def delete_internet_gateway(
        self, *, InternetGatewayId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified internet gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_internet_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_internet_gateway)
        """

    def delete_ipam(
        self, *, IpamId: str, DryRun: bool = ..., Cascade: bool = ...
    ) -> DeleteIpamResultTypeDef:
        """
        Delete an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_ipam)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_ipam)
        """

    def delete_ipam_pool(
        self, *, IpamPoolId: str, DryRun: bool = ..., Cascade: bool = ...
    ) -> DeleteIpamPoolResultTypeDef:
        """
        Delete an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_ipam_pool)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_ipam_pool)
        """

    def delete_ipam_resource_discovery(
        self, *, IpamResourceDiscoveryId: str, DryRun: bool = ...
    ) -> DeleteIpamResourceDiscoveryResultTypeDef:
        """
        Deletes an IPAM resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_ipam_resource_discovery)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_ipam_resource_discovery)
        """

    def delete_ipam_scope(
        self, *, IpamScopeId: str, DryRun: bool = ...
    ) -> DeleteIpamScopeResultTypeDef:
        """
        Delete the scope for an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_ipam_scope)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_ipam_scope)
        """

    def delete_key_pair(
        self, *, KeyName: str = ..., KeyPairId: str = ..., DryRun: bool = ...
    ) -> DeleteKeyPairResultTypeDef:
        """
        Deletes the specified key pair, by removing the public key from Amazon EC2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_key_pair)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_key_pair)
        """

    def delete_launch_template(
        self, *, DryRun: bool = ..., LaunchTemplateId: str = ..., LaunchTemplateName: str = ...
    ) -> DeleteLaunchTemplateResultTypeDef:
        """
        Deletes a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_launch_template)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_launch_template)
        """

    def delete_launch_template_versions(
        self,
        *,
        Versions: Sequence[str],
        DryRun: bool = ...,
        LaunchTemplateId: str = ...,
        LaunchTemplateName: str = ...
    ) -> DeleteLaunchTemplateVersionsResultTypeDef:
        """
        Deletes one or more versions of a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_launch_template_versions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_launch_template_versions)
        """

    def delete_local_gateway_route(
        self,
        *,
        LocalGatewayRouteTableId: str,
        DestinationCidrBlock: str = ...,
        DryRun: bool = ...,
        DestinationPrefixListId: str = ...
    ) -> DeleteLocalGatewayRouteResultTypeDef:
        """
        Deletes the specified route from the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_local_gateway_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_local_gateway_route)
        """

    def delete_local_gateway_route_table(
        self, *, LocalGatewayRouteTableId: str, DryRun: bool = ...
    ) -> DeleteLocalGatewayRouteTableResultTypeDef:
        """
        Deletes a local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_local_gateway_route_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_local_gateway_route_table)
        """

    def delete_local_gateway_route_table_virtual_interface_group_association(
        self, *, LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: str, DryRun: bool = ...
    ) -> DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef:
        """
        Deletes a local gateway route table virtual interface group association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_local_gateway_route_table_virtual_interface_group_association)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_local_gateway_route_table_virtual_interface_group_association)
        """

    def delete_local_gateway_route_table_vpc_association(
        self, *, LocalGatewayRouteTableVpcAssociationId: str, DryRun: bool = ...
    ) -> DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef:
        """
        Deletes the specified association between a VPC and local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_local_gateway_route_table_vpc_association)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_local_gateway_route_table_vpc_association)
        """

    def delete_managed_prefix_list(
        self, *, PrefixListId: str, DryRun: bool = ...
    ) -> DeleteManagedPrefixListResultTypeDef:
        """
        Deletes the specified managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_managed_prefix_list)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_managed_prefix_list)
        """

    def delete_nat_gateway(
        self, *, NatGatewayId: str, DryRun: bool = ...
    ) -> DeleteNatGatewayResultTypeDef:
        """
        Deletes the specified NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_nat_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_nat_gateway)
        """

    def delete_network_acl(
        self, *, NetworkAclId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified network ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_acl)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_acl)
        """

    def delete_network_acl_entry(
        self, *, Egress: bool, NetworkAclId: str, RuleNumber: int, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified ingress or egress entry (rule) from the specified network
        ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_acl_entry)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_acl_entry)
        """

    def delete_network_insights_access_scope(
        self, *, NetworkInsightsAccessScopeId: str, DryRun: bool = ...
    ) -> DeleteNetworkInsightsAccessScopeResultTypeDef:
        """
        Deletes the specified Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_insights_access_scope)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_insights_access_scope)
        """

    def delete_network_insights_access_scope_analysis(
        self, *, NetworkInsightsAccessScopeAnalysisId: str, DryRun: bool = ...
    ) -> DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef:
        """
        Deletes the specified Network Access Scope analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_insights_access_scope_analysis)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_insights_access_scope_analysis)
        """

    def delete_network_insights_analysis(
        self, *, NetworkInsightsAnalysisId: str, DryRun: bool = ...
    ) -> DeleteNetworkInsightsAnalysisResultTypeDef:
        """
        Deletes the specified network insights analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_insights_analysis)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_insights_analysis)
        """

    def delete_network_insights_path(
        self, *, NetworkInsightsPathId: str, DryRun: bool = ...
    ) -> DeleteNetworkInsightsPathResultTypeDef:
        """
        Deletes the specified path.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_insights_path)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_insights_path)
        """

    def delete_network_interface(
        self, *, NetworkInterfaceId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_interface)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_interface)
        """

    def delete_network_interface_permission(
        self, *, NetworkInterfacePermissionId: str, Force: bool = ..., DryRun: bool = ...
    ) -> DeleteNetworkInterfacePermissionResultTypeDef:
        """
        Deletes a permission for a network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_network_interface_permission)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_interface_permission)
        """

    def delete_placement_group(
        self, *, GroupName: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified placement group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_placement_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_placement_group)
        """

    def delete_public_ipv4_pool(
        self, *, PoolId: str, DryRun: bool = ...
    ) -> DeletePublicIpv4PoolResultTypeDef:
        """
        Delete a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_public_ipv4_pool)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_public_ipv4_pool)
        """

    def delete_queued_reserved_instances(
        self, *, ReservedInstancesIds: Sequence[str], DryRun: bool = ...
    ) -> DeleteQueuedReservedInstancesResultTypeDef:
        """
        Deletes the queued purchases for the specified Reserved Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_queued_reserved_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_queued_reserved_instances)
        """

    def delete_route(
        self,
        *,
        RouteTableId: str,
        DestinationCidrBlock: str = ...,
        DestinationIpv6CidrBlock: str = ...,
        DestinationPrefixListId: str = ...,
        DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified route from the specified route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_route)
        """

    def delete_route_table(
        self, *, RouteTableId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_route_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_route_table)
        """

    def delete_security_group(
        self, *, GroupId: str = ..., GroupName: str = ..., DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_security_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_security_group)
        """

    def delete_snapshot(
        self, *, SnapshotId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_snapshot)
        """

    def delete_spot_datafeed_subscription(
        self, *, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the data feed for Spot Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_spot_datafeed_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_spot_datafeed_subscription)
        """

    def delete_subnet(self, *, SubnetId: str, DryRun: bool = ...) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_subnet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_subnet)
        """

    def delete_subnet_cidr_reservation(
        self, *, SubnetCidrReservationId: str, DryRun: bool = ...
    ) -> DeleteSubnetCidrReservationResultTypeDef:
        """
        Deletes a subnet CIDR reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_subnet_cidr_reservation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_subnet_cidr_reservation)
        """

    def delete_tags(
        self, *, Resources: Sequence[str], Tags: Sequence[TagTypeDef] = ..., DryRun: bool = ...
    ) -> None:
        """
        Deletes the specified set of tags from the specified set of resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_tags)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_tags)
        """

    def delete_traffic_mirror_filter(
        self, *, TrafficMirrorFilterId: str, DryRun: bool = ...
    ) -> DeleteTrafficMirrorFilterResultTypeDef:
        """
        Deletes the specified Traffic Mirror filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_traffic_mirror_filter)
        """

    def delete_traffic_mirror_filter_rule(
        self, *, TrafficMirrorFilterRuleId: str, DryRun: bool = ...
    ) -> DeleteTrafficMirrorFilterRuleResultTypeDef:
        """
        Deletes the specified Traffic Mirror rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter_rule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_traffic_mirror_filter_rule)
        """

    def delete_traffic_mirror_session(
        self, *, TrafficMirrorSessionId: str, DryRun: bool = ...
    ) -> DeleteTrafficMirrorSessionResultTypeDef:
        """
        Deletes the specified Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_session)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_traffic_mirror_session)
        """

    def delete_traffic_mirror_target(
        self, *, TrafficMirrorTargetId: str, DryRun: bool = ...
    ) -> DeleteTrafficMirrorTargetResultTypeDef:
        """
        Deletes the specified Traffic Mirror target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_target)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_traffic_mirror_target)
        """

    def delete_transit_gateway(
        self, *, TransitGatewayId: str, DryRun: bool = ...
    ) -> DeleteTransitGatewayResultTypeDef:
        """
        Deletes the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway)
        """

    def delete_transit_gateway_connect(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = ...
    ) -> DeleteTransitGatewayConnectResultTypeDef:
        """
        Deletes the specified Connect attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_connect)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_connect)
        """

    def delete_transit_gateway_connect_peer(
        self, *, TransitGatewayConnectPeerId: str, DryRun: bool = ...
    ) -> DeleteTransitGatewayConnectPeerResultTypeDef:
        """
        Deletes the specified Connect peer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_connect_peer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_connect_peer)
        """

    def delete_transit_gateway_multicast_domain(
        self, *, TransitGatewayMulticastDomainId: str, DryRun: bool = ...
    ) -> DeleteTransitGatewayMulticastDomainResultTypeDef:
        """
        Deletes the specified transit gateway multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_multicast_domain)
        """

    def delete_transit_gateway_peering_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = ...
    ) -> DeleteTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Deletes a transit gateway peering attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_peering_attachment)
        """

    def delete_transit_gateway_policy_table(
        self, *, TransitGatewayPolicyTableId: str, DryRun: bool = ...
    ) -> DeleteTransitGatewayPolicyTableResultTypeDef:
        """
        Deletes the specified transit gateway policy table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_policy_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_policy_table)
        """

    def delete_transit_gateway_prefix_list_reference(
        self, *, TransitGatewayRouteTableId: str, PrefixListId: str, DryRun: bool = ...
    ) -> DeleteTransitGatewayPrefixListReferenceResultTypeDef:
        """
        Deletes a reference (route) to a prefix list in a specified transit gateway
        route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_prefix_list_reference)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_prefix_list_reference)
        """

    def delete_transit_gateway_route(
        self, *, TransitGatewayRouteTableId: str, DestinationCidrBlock: str, DryRun: bool = ...
    ) -> DeleteTransitGatewayRouteResultTypeDef:
        """
        Deletes the specified route from the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_route)
        """

    def delete_transit_gateway_route_table(
        self, *, TransitGatewayRouteTableId: str, DryRun: bool = ...
    ) -> DeleteTransitGatewayRouteTableResultTypeDef:
        """
        Deletes the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_route_table)
        """

    def delete_transit_gateway_route_table_announcement(
        self, *, TransitGatewayRouteTableAnnouncementId: str, DryRun: bool = ...
    ) -> DeleteTransitGatewayRouteTableAnnouncementResultTypeDef:
        """
        Advertises to the transit gateway that a transit gateway route table is deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route_table_announcement)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_route_table_announcement)
        """

    def delete_transit_gateway_vpc_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = ...
    ) -> DeleteTransitGatewayVpcAttachmentResultTypeDef:
        """
        Deletes the specified VPC attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_vpc_attachment)
        """

    def delete_verified_access_endpoint(
        self, *, VerifiedAccessEndpointId: str, ClientToken: str = ..., DryRun: bool = ...
    ) -> DeleteVerifiedAccessEndpointResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_verified_access_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_verified_access_endpoint)
        """

    def delete_verified_access_group(
        self, *, VerifiedAccessGroupId: str, ClientToken: str = ..., DryRun: bool = ...
    ) -> DeleteVerifiedAccessGroupResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_verified_access_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_verified_access_group)
        """

    def delete_verified_access_instance(
        self, *, VerifiedAccessInstanceId: str, DryRun: bool = ..., ClientToken: str = ...
    ) -> DeleteVerifiedAccessInstanceResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_verified_access_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_verified_access_instance)
        """

    def delete_verified_access_trust_provider(
        self, *, VerifiedAccessTrustProviderId: str, DryRun: bool = ..., ClientToken: str = ...
    ) -> DeleteVerifiedAccessTrustProviderResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access trust provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_verified_access_trust_provider)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_verified_access_trust_provider)
        """

    def delete_volume(self, *, VolumeId: str, DryRun: bool = ...) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified EBS volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_volume)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_volume)
        """

    def delete_vpc(self, *, VpcId: str, DryRun: bool = ...) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpc)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpc)
        """

    def delete_vpc_endpoint_connection_notifications(
        self, *, ConnectionNotificationIds: Sequence[str], DryRun: bool = ...
    ) -> DeleteVpcEndpointConnectionNotificationsResultTypeDef:
        """
        Deletes the specified VPC endpoint connection notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_connection_notifications)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpc_endpoint_connection_notifications)
        """

    def delete_vpc_endpoint_service_configurations(
        self, *, ServiceIds: Sequence[str], DryRun: bool = ...
    ) -> DeleteVpcEndpointServiceConfigurationsResultTypeDef:
        """
        Deletes the specified VPC endpoint service configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_service_configurations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpc_endpoint_service_configurations)
        """

    def delete_vpc_endpoints(
        self, *, VpcEndpointIds: Sequence[str], DryRun: bool = ...
    ) -> DeleteVpcEndpointsResultTypeDef:
        """
        Deletes the specified VPC endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpc_endpoints)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpc_endpoints)
        """

    def delete_vpc_peering_connection(
        self, *, VpcPeeringConnectionId: str, DryRun: bool = ...
    ) -> DeleteVpcPeeringConnectionResultTypeDef:
        """
        Deletes a VPC peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpc_peering_connection)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpc_peering_connection)
        """

    def delete_vpn_connection(
        self, *, VpnConnectionId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified VPN connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpn_connection)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpn_connection)
        """

    def delete_vpn_connection_route(
        self, *, DestinationCidrBlock: str, VpnConnectionId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified static route associated with a VPN connection between an
        existing virtual private gateway and a VPN customer
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpn_connection_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpn_connection_route)
        """

    def delete_vpn_gateway(
        self, *, VpnGatewayId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified virtual private gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.delete_vpn_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpn_gateway)
        """

    def deprovision_byoip_cidr(
        self, *, Cidr: str, DryRun: bool = ...
    ) -> DeprovisionByoipCidrResultTypeDef:
        """
        Releases the specified address range that you provisioned for use with your
        Amazon Web Services resources through bring your own IP addresses (BYOIP) and
        deletes the corresponding address
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deprovision_byoip_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deprovision_byoip_cidr)
        """

    def deprovision_ipam_byoasn(
        self, *, IpamId: str, Asn: str, DryRun: bool = ...
    ) -> DeprovisionIpamByoasnResultTypeDef:
        """
        Deprovisions your Autonomous System Number (ASN) from your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deprovision_ipam_byoasn)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deprovision_ipam_byoasn)
        """

    def deprovision_ipam_pool_cidr(
        self, *, IpamPoolId: str, DryRun: bool = ..., Cidr: str = ...
    ) -> DeprovisionIpamPoolCidrResultTypeDef:
        """
        Deprovision a CIDR provisioned from an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deprovision_ipam_pool_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deprovision_ipam_pool_cidr)
        """

    def deprovision_public_ipv4_pool_cidr(
        self, *, PoolId: str, Cidr: str, DryRun: bool = ...
    ) -> DeprovisionPublicIpv4PoolCidrResultTypeDef:
        """
        Deprovision a CIDR from a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deprovision_public_ipv4_pool_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deprovision_public_ipv4_pool_cidr)
        """

    def deregister_image(self, *, ImageId: str, DryRun: bool = ...) -> EmptyResponseMetadataTypeDef:
        """
        Deregisters the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deregister_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deregister_image)
        """

    def deregister_instance_event_notification_attributes(
        self,
        *,
        InstanceTagAttribute: DeregisterInstanceTagAttributeRequestTypeDef,
        DryRun: bool = ...
    ) -> DeregisterInstanceEventNotificationAttributesResultTypeDef:
        """
        Deregisters tag keys to prevent tags that have the specified tag keys from
        being included in scheduled event notifications for resources in the
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deregister_instance_event_notification_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deregister_instance_event_notification_attributes)
        """

    def deregister_transit_gateway_multicast_group_members(
        self,
        *,
        TransitGatewayMulticastDomainId: str = ...,
        GroupIpAddress: str = ...,
        NetworkInterfaceIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> DeregisterTransitGatewayMulticastGroupMembersResultTypeDef:
        """
        Deregisters the specified members (network interfaces) from the transit gateway
        multicast
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_members)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deregister_transit_gateway_multicast_group_members)
        """

    def deregister_transit_gateway_multicast_group_sources(
        self,
        *,
        TransitGatewayMulticastDomainId: str = ...,
        GroupIpAddress: str = ...,
        NetworkInterfaceIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef:
        """
        Deregisters the specified sources (network interfaces) from the transit gateway
        multicast
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_sources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deregister_transit_gateway_multicast_group_sources)
        """

    def describe_account_attributes(
        self, *, AttributeNames: Sequence[AccountAttributeNameType] = ..., DryRun: bool = ...
    ) -> DescribeAccountAttributesResultTypeDef:
        """
        Describes attributes of your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_account_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_account_attributes)
        """

    def describe_address_transfers(
        self,
        *,
        AllocationIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...
    ) -> DescribeAddressTransfersResultTypeDef:
        """
        Describes an Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_address_transfers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_address_transfers)
        """

    def describe_addresses(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PublicIps: Sequence[str] = ...,
        AllocationIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> DescribeAddressesResultTypeDef:
        """
        Describes the specified Elastic IP addresses or all of your Elastic IP
        addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_addresses)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_addresses)
        """

    def describe_addresses_attribute(
        self,
        *,
        AllocationIds: Sequence[str] = ...,
        Attribute: Literal["domain-name"] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...
    ) -> DescribeAddressesAttributeResultTypeDef:
        """
        Describes the attributes of the specified Elastic IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_addresses_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_addresses_attribute)
        """

    def describe_aggregate_id_format(
        self, *, DryRun: bool = ...
    ) -> DescribeAggregateIdFormatResultTypeDef:
        """
        Describes the longer ID format settings for all resource types in a specific
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_aggregate_id_format)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_aggregate_id_format)
        """

    def describe_availability_zones(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        ZoneNames: Sequence[str] = ...,
        ZoneIds: Sequence[str] = ...,
        AllAvailabilityZones: bool = ...,
        DryRun: bool = ...
    ) -> DescribeAvailabilityZonesResultTypeDef:
        """
        Describes the Availability Zones, Local Zones, and Wavelength Zones that are
        available to
        you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_availability_zones)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_availability_zones)
        """

    def describe_aws_network_performance_metric_subscriptions(
        self,
        *,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef:
        """
        Describes the current Infrastructure Performance metric subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_aws_network_performance_metric_subscriptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_aws_network_performance_metric_subscriptions)
        """

    def describe_bundle_tasks(
        self,
        *,
        BundleIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeBundleTasksResultTypeDef:
        """
        Describes the specified bundle tasks or all of your bundle tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_bundle_tasks)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_bundle_tasks)
        """

    def describe_byoip_cidrs(
        self, *, MaxResults: int, DryRun: bool = ..., NextToken: str = ...
    ) -> DescribeByoipCidrsResultTypeDef:
        """
        Describes the IP address ranges that were specified in calls to
        ProvisionByoipCidr.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_byoip_cidrs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_byoip_cidrs)
        """

    def describe_capacity_block_offerings(
        self,
        *,
        InstanceType: str,
        InstanceCount: int,
        CapacityDurationHours: int,
        DryRun: bool = ...,
        StartDateRange: TimestampTypeDef = ...,
        EndDateRange: TimestampTypeDef = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeCapacityBlockOfferingsResultTypeDef:
        """
        Describes Capacity Block offerings available for purchase.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_capacity_block_offerings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_capacity_block_offerings)
        """

    def describe_capacity_reservation_fleets(
        self,
        *,
        CapacityReservationFleetIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeCapacityReservationFleetsResultTypeDef:
        """
        Describes one or more Capacity Reservation Fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_capacity_reservation_fleets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_capacity_reservation_fleets)
        """

    def describe_capacity_reservations(
        self,
        *,
        CapacityReservationIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeCapacityReservationsResultTypeDef:
        """
        Describes one or more of your Capacity Reservations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_capacity_reservations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_capacity_reservations)
        """

    def describe_carrier_gateways(
        self,
        *,
        CarrierGatewayIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeCarrierGatewaysResultTypeDef:
        """
        Describes one or more of your carrier gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_carrier_gateways)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_carrier_gateways)
        """

    def describe_classic_link_instances(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        InstanceIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeClassicLinkInstancesResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_classic_link_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_classic_link_instances)
        """

    def describe_client_vpn_authorization_rules(
        self,
        *,
        ClientVpnEndpointId: str,
        DryRun: bool = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...
    ) -> DescribeClientVpnAuthorizationRulesResultTypeDef:
        """
        Describes the authorization rules for a specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_client_vpn_authorization_rules)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_client_vpn_authorization_rules)
        """

    def describe_client_vpn_connections(
        self,
        *,
        ClientVpnEndpointId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...
    ) -> DescribeClientVpnConnectionsResultTypeDef:
        """
        Describes active client connections and connections that have been terminated
        within the last 60 minutes for the specified Client VPN
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_client_vpn_connections)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_client_vpn_connections)
        """

    def describe_client_vpn_endpoints(
        self,
        *,
        ClientVpnEndpointIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeClientVpnEndpointsResultTypeDef:
        """
        Describes one or more Client VPN endpoints in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_client_vpn_endpoints)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_client_vpn_endpoints)
        """

    def describe_client_vpn_routes(
        self,
        *,
        ClientVpnEndpointId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeClientVpnRoutesResultTypeDef:
        """
        Describes the routes for the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_client_vpn_routes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_client_vpn_routes)
        """

    def describe_client_vpn_target_networks(
        self,
        *,
        ClientVpnEndpointId: str,
        AssociationIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeClientVpnTargetNetworksResultTypeDef:
        """
        Describes the target networks associated with the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_client_vpn_target_networks)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_client_vpn_target_networks)
        """

    def describe_coip_pools(
        self,
        *,
        PoolIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeCoipPoolsResultTypeDef:
        """
        Describes the specified customer-owned address pools or all of your
        customer-owned address
        pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_coip_pools)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_coip_pools)
        """

    def describe_conversion_tasks(
        self, *, ConversionTaskIds: Sequence[str] = ..., DryRun: bool = ...
    ) -> DescribeConversionTasksResultTypeDef:
        """
        Describes the specified conversion tasks or all your conversion tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_conversion_tasks)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_conversion_tasks)
        """

    def describe_customer_gateways(
        self,
        *,
        CustomerGatewayIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeCustomerGatewaysResultTypeDef:
        """
        Describes one or more of your VPN customer gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_customer_gateways)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_customer_gateways)
        """

    def describe_dhcp_options(
        self,
        *,
        DhcpOptionsIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeDhcpOptionsResultTypeDef:
        """
        Describes one or more of your DHCP options sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_dhcp_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_dhcp_options)
        """

    def describe_egress_only_internet_gateways(
        self,
        *,
        DryRun: bool = ...,
        EgressOnlyInternetGatewayIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...
    ) -> DescribeEgressOnlyInternetGatewaysResultTypeDef:
        """
        Describes one or more of your egress-only internet gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_egress_only_internet_gateways)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_egress_only_internet_gateways)
        """

    def describe_elastic_gpus(
        self,
        *,
        ElasticGpuIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeElasticGpusResultTypeDef:
        """
        Describes the Elastic Graphics accelerator associated with your instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_elastic_gpus)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_elastic_gpus)
        """

    def describe_export_image_tasks(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        ExportImageTaskIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeExportImageTasksResultTypeDef:
        """
        Describes the specified export image tasks or all of your export image tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_export_image_tasks)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_export_image_tasks)
        """

    def describe_export_tasks(
        self, *, ExportTaskIds: Sequence[str] = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> DescribeExportTasksResultTypeDef:
        """
        Describes the specified export instance tasks or all of your export instance
        tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_export_tasks)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_export_tasks)
        """

    def describe_fast_launch_images(
        self,
        *,
        ImageIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeFastLaunchImagesResultTypeDef:
        """
        Describe details for Windows AMIs that are configured for Windows fast launch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fast_launch_images)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fast_launch_images)
        """

    def describe_fast_snapshot_restores(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeFastSnapshotRestoresResultTypeDef:
        """
        Describes the state of fast snapshot restores for your snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fast_snapshot_restores)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fast_snapshot_restores)
        """

    def describe_fleet_history(
        self,
        *,
        FleetId: str,
        StartTime: TimestampTypeDef,
        DryRun: bool = ...,
        EventType: FleetEventTypeType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeFleetHistoryResultTypeDef:
        """
        Describes the events for the specified EC2 Fleet during the specified time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fleet_history)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fleet_history)
        """

    def describe_fleet_instances(
        self,
        *,
        FleetId: str,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...
    ) -> DescribeFleetInstancesResultTypeDef:
        """
        Describes the running instances for the specified EC2 Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fleet_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fleet_instances)
        """

    def describe_fleets(
        self,
        *,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        FleetIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...
    ) -> DescribeFleetsResultTypeDef:
        """
        Describes the specified EC2 Fleets or all of your EC2 Fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fleets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fleets)
        """

    def describe_flow_logs(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        FlowLogIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeFlowLogsResultTypeDef:
        """
        Describes one or more flow logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_flow_logs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_flow_logs)
        """

    def describe_fpga_image_attribute(
        self, *, FpgaImageId: str, Attribute: FpgaImageAttributeNameType, DryRun: bool = ...
    ) -> DescribeFpgaImageAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified Amazon FPGA Image (AFI).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fpga_image_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fpga_image_attribute)
        """

    def describe_fpga_images(
        self,
        *,
        DryRun: bool = ...,
        FpgaImageIds: Sequence[str] = ...,
        Owners: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeFpgaImagesResultTypeDef:
        """
        Describes the Amazon FPGA Images (AFIs) available to you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_fpga_images)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fpga_images)
        """

    def describe_host_reservation_offerings(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxDuration: int = ...,
        MaxResults: int = ...,
        MinDuration: int = ...,
        NextToken: str = ...,
        OfferingId: str = ...
    ) -> DescribeHostReservationOfferingsResultTypeDef:
        """
        Describes the Dedicated Host reservations that are available to purchase.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_host_reservation_offerings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_host_reservation_offerings)
        """

    def describe_host_reservations(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        HostReservationIdSet: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeHostReservationsResultTypeDef:
        """
        Describes reservations that are associated with Dedicated Hosts in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_host_reservations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_host_reservations)
        """

    def describe_hosts(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        HostIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeHostsResultTypeDef:
        """
        Describes the specified Dedicated Hosts or all your Dedicated Hosts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_hosts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_hosts)
        """

    def describe_iam_instance_profile_associations(
        self,
        *,
        AssociationIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeIamInstanceProfileAssociationsResultTypeDef:
        """
        Describes your IAM instance profile associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_iam_instance_profile_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_iam_instance_profile_associations)
        """

    def describe_id_format(self, *, Resource: str = ...) -> DescribeIdFormatResultTypeDef:
        """
        Describes the ID format settings for your resources on a per-Region basis, for
        example, to view which resource types are enabled for longer
        IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_id_format)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_id_format)
        """

    def describe_identity_id_format(
        self, *, PrincipalArn: str, Resource: str = ...
    ) -> DescribeIdentityIdFormatResultTypeDef:
        """
        Describes the ID format settings for resources for the specified IAM user, IAM
        role, or root
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_identity_id_format)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_identity_id_format)
        """

    def describe_image_attribute(
        self, *, Attribute: ImageAttributeNameType, ImageId: str, DryRun: bool = ...
    ) -> ImageAttributeTypeDef:
        """
        Describes the specified attribute of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_image_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_image_attribute)
        """

    def describe_images(
        self,
        *,
        ExecutableUsers: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        ImageIds: Sequence[str] = ...,
        Owners: Sequence[str] = ...,
        IncludeDeprecated: bool = ...,
        IncludeDisabled: bool = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeImagesResultTypeDef:
        """
        Describes the specified images (AMIs, AKIs, and ARIs) available to you or all
        of the images available to
        you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_images)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_images)
        """

    def describe_import_image_tasks(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        ImportTaskIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeImportImageTasksResultTypeDef:
        """
        Displays details about an import virtual machine or import snapshot tasks that
        are already
        created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_import_image_tasks)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_import_image_tasks)
        """

    def describe_import_snapshot_tasks(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        ImportTaskIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeImportSnapshotTasksResultTypeDef:
        """
        Describes your import snapshot tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_import_snapshot_tasks)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_import_snapshot_tasks)
        """

    def describe_instance_attribute(
        self, *, Attribute: InstanceAttributeNameType, InstanceId: str, DryRun: bool = ...
    ) -> InstanceAttributeTypeDef:
        """
        Describes the specified attribute of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_attribute)
        """

    def describe_instance_connect_endpoints(
        self,
        *,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        InstanceConnectEndpointIds: Sequence[str] = ...
    ) -> DescribeInstanceConnectEndpointsResultTypeDef:
        """
        Describes the specified EC2 Instance Connect Endpoints or all EC2 Instance
        Connect
        Endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_connect_endpoints)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_connect_endpoints)
        """

    def describe_instance_credit_specifications(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        InstanceIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeInstanceCreditSpecificationsResultTypeDef:
        """
        Describes the credit option for CPU usage of the specified burstable
        performance
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_credit_specifications)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_credit_specifications)
        """

    def describe_instance_event_notification_attributes(
        self, *, DryRun: bool = ...
    ) -> DescribeInstanceEventNotificationAttributesResultTypeDef:
        """
        Describes the tag keys that are registered to appear in scheduled event
        notifications for resources in the current
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_event_notification_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_event_notification_attributes)
        """

    def describe_instance_event_windows(
        self,
        *,
        DryRun: bool = ...,
        InstanceEventWindowIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeInstanceEventWindowsResultTypeDef:
        """
        Describes the specified event windows or all event windows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_event_windows)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_event_windows)
        """

    def describe_instance_status(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        InstanceIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...,
        IncludeAllInstances: bool = ...
    ) -> DescribeInstanceStatusResultTypeDef:
        """
        Describes the status of the specified instances or all of your instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_status)
        """

    def describe_instance_topology(
        self,
        *,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        InstanceIds: Sequence[str] = ...,
        GroupNames: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...
    ) -> DescribeInstanceTopologyResultTypeDef:
        """
        Describes a tree-based hierarchy that represents the physical host placement of
        your EC2 instances within an Availability Zone or Local
        Zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_topology)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_topology)
        """

    def describe_instance_type_offerings(
        self,
        *,
        DryRun: bool = ...,
        LocationType: LocationTypeType = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeInstanceTypeOfferingsResultTypeDef:
        """
        Returns a list of all instance types offered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_type_offerings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_type_offerings)
        """

    def describe_instance_types(
        self,
        *,
        DryRun: bool = ...,
        InstanceTypes: Sequence[InstanceTypeType] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeInstanceTypesResultTypeDef:
        """
        Describes the details of the instance types that are offered in a location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instance_types)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_types)
        """

    def describe_instances(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        InstanceIds: Sequence[str] = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeInstancesResultTypeDef:
        """
        Describes the specified instances or all instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instances)
        """

    def describe_internet_gateways(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        InternetGatewayIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeInternetGatewaysResultTypeDef:
        """
        Describes one or more of your internet gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_internet_gateways)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_internet_gateways)
        """

    def describe_ipam_byoasn(
        self, *, DryRun: bool = ..., MaxResults: int = ..., NextToken: str = ...
    ) -> DescribeIpamByoasnResultTypeDef:
        """
        Describes your Autonomous System Numbers (ASNs), their provisioning statuses,
        and the BYOIP CIDRs with which they are
        associated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_ipam_byoasn)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipam_byoasn)
        """

    def describe_ipam_pools(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        IpamPoolIds: Sequence[str] = ...
    ) -> DescribeIpamPoolsResultTypeDef:
        """
        Get information about your IPAM pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_ipam_pools)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipam_pools)
        """

    def describe_ipam_resource_discoveries(
        self,
        *,
        DryRun: bool = ...,
        IpamResourceDiscoveryIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        Filters: Sequence[FilterTypeDef] = ...
    ) -> DescribeIpamResourceDiscoveriesResultTypeDef:
        """
        Describes IPAM resource discoveries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_ipam_resource_discoveries)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipam_resource_discoveries)
        """

    def describe_ipam_resource_discovery_associations(
        self,
        *,
        DryRun: bool = ...,
        IpamResourceDiscoveryAssociationIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        Filters: Sequence[FilterTypeDef] = ...
    ) -> DescribeIpamResourceDiscoveryAssociationsResultTypeDef:
        """
        Describes resource discovery association with an Amazon VPC IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_ipam_resource_discovery_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipam_resource_discovery_associations)
        """

    def describe_ipam_scopes(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        IpamScopeIds: Sequence[str] = ...
    ) -> DescribeIpamScopesResultTypeDef:
        """
        Get information about your IPAM scopes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_ipam_scopes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipam_scopes)
        """

    def describe_ipams(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        IpamIds: Sequence[str] = ...
    ) -> DescribeIpamsResultTypeDef:
        """
        Get information about your IPAM pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_ipams)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipams)
        """

    def describe_ipv6_pools(
        self,
        *,
        PoolIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...
    ) -> DescribeIpv6PoolsResultTypeDef:
        """
        Describes your IPv6 address pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_ipv6_pools)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipv6_pools)
        """

    def describe_key_pairs(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        KeyNames: Sequence[str] = ...,
        KeyPairIds: Sequence[str] = ...,
        DryRun: bool = ...,
        IncludePublicKey: bool = ...
    ) -> DescribeKeyPairsResultTypeDef:
        """
        Describes the specified key pairs or all of your key pairs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_key_pairs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_key_pairs)
        """

    def describe_launch_template_versions(
        self,
        *,
        DryRun: bool = ...,
        LaunchTemplateId: str = ...,
        LaunchTemplateName: str = ...,
        Versions: Sequence[str] = ...,
        MinVersion: str = ...,
        MaxVersion: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        ResolveAlias: bool = ...
    ) -> DescribeLaunchTemplateVersionsResultTypeDef:
        """
        Describes one or more versions of a specified launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_launch_template_versions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_launch_template_versions)
        """

    def describe_launch_templates(
        self,
        *,
        DryRun: bool = ...,
        LaunchTemplateIds: Sequence[str] = ...,
        LaunchTemplateNames: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeLaunchTemplatesResultTypeDef:
        """
        Describes one or more launch templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_launch_templates)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_launch_templates)
        """

    def describe_local_gateway_route_table_virtual_interface_group_associations(
        self,
        *,
        LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef:
        """
        Describes the associations between virtual interface groups and local gateway
        route
        tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_virtual_interface_group_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateway_route_table_virtual_interface_group_associations)
        """

    def describe_local_gateway_route_table_vpc_associations(
        self,
        *,
        LocalGatewayRouteTableVpcAssociationIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef:
        """
        Describes the specified associations between VPCs and local gateway route
        tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_vpc_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateway_route_table_vpc_associations)
        """

    def describe_local_gateway_route_tables(
        self,
        *,
        LocalGatewayRouteTableIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeLocalGatewayRouteTablesResultTypeDef:
        """
        Describes one or more local gateway route tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_tables)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateway_route_tables)
        """

    def describe_local_gateway_virtual_interface_groups(
        self,
        *,
        LocalGatewayVirtualInterfaceGroupIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef:
        """
        Describes the specified local gateway virtual interface groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interface_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateway_virtual_interface_groups)
        """

    def describe_local_gateway_virtual_interfaces(
        self,
        *,
        LocalGatewayVirtualInterfaceIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeLocalGatewayVirtualInterfacesResultTypeDef:
        """
        Describes the specified local gateway virtual interfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interfaces)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateway_virtual_interfaces)
        """

    def describe_local_gateways(
        self,
        *,
        LocalGatewayIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeLocalGatewaysResultTypeDef:
        """
        Describes one or more local gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_local_gateways)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateways)
        """

    def describe_locked_snapshots(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        SnapshotIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> DescribeLockedSnapshotsResultTypeDef:
        """
        Describes the lock status for a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_locked_snapshots)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_locked_snapshots)
        """

    def describe_managed_prefix_lists(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        PrefixListIds: Sequence[str] = ...
    ) -> DescribeManagedPrefixListsResultTypeDef:
        """
        Describes your managed prefix lists and any Amazon Web Services-managed prefix
        lists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_managed_prefix_lists)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_managed_prefix_lists)
        """

    def describe_moving_addresses(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        PublicIps: Sequence[str] = ...
    ) -> DescribeMovingAddressesResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_moving_addresses)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_moving_addresses)
        """

    def describe_nat_gateways(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NatGatewayIds: Sequence[str] = ...,
        NextToken: str = ...
    ) -> DescribeNatGatewaysResultTypeDef:
        """
        Describes one or more of your NAT gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_nat_gateways)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_nat_gateways)
        """

    def describe_network_acls(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        NetworkAclIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeNetworkAclsResultTypeDef:
        """
        Describes one or more of your network ACLs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_acls)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_acls)
        """

    def describe_network_insights_access_scope_analyses(
        self,
        *,
        NetworkInsightsAccessScopeAnalysisIds: Sequence[str] = ...,
        NetworkInsightsAccessScopeId: str = ...,
        AnalysisStartTimeBegin: TimestampTypeDef = ...,
        AnalysisStartTimeEnd: TimestampTypeDef = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        NextToken: str = ...
    ) -> DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef:
        """
        Describes the specified Network Access Scope analyses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_insights_access_scope_analyses)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_insights_access_scope_analyses)
        """

    def describe_network_insights_access_scopes(
        self,
        *,
        NetworkInsightsAccessScopeIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        NextToken: str = ...
    ) -> DescribeNetworkInsightsAccessScopesResultTypeDef:
        """
        Describes the specified Network Access Scopes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_insights_access_scopes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_insights_access_scopes)
        """

    def describe_network_insights_analyses(
        self,
        *,
        NetworkInsightsAnalysisIds: Sequence[str] = ...,
        NetworkInsightsPathId: str = ...,
        AnalysisStartTime: TimestampTypeDef = ...,
        AnalysisEndTime: TimestampTypeDef = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        NextToken: str = ...
    ) -> DescribeNetworkInsightsAnalysesResultTypeDef:
        """
        Describes one or more of your network insights analyses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_insights_analyses)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_insights_analyses)
        """

    def describe_network_insights_paths(
        self,
        *,
        NetworkInsightsPathIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        NextToken: str = ...
    ) -> DescribeNetworkInsightsPathsResultTypeDef:
        """
        Describes one or more of your paths.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_insights_paths)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_insights_paths)
        """

    def describe_network_interface_attribute(
        self,
        *,
        NetworkInterfaceId: str,
        Attribute: NetworkInterfaceAttributeType = ...,
        DryRun: bool = ...
    ) -> DescribeNetworkInterfaceAttributeResultTypeDef:
        """
        Describes a network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_interface_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_interface_attribute)
        """

    def describe_network_interface_permissions(
        self,
        *,
        NetworkInterfacePermissionIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeNetworkInterfacePermissionsResultTypeDef:
        """
        Describes the permissions for your network interfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_interface_permissions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_interface_permissions)
        """

    def describe_network_interfaces(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        NetworkInterfaceIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeNetworkInterfacesResultTypeDef:
        """
        Describes one or more of your network interfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_network_interfaces)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_interfaces)
        """

    def describe_placement_groups(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        GroupNames: Sequence[str] = ...,
        GroupIds: Sequence[str] = ...
    ) -> DescribePlacementGroupsResultTypeDef:
        """
        Describes the specified placement groups or all of your placement groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_placement_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_placement_groups)
        """

    def describe_prefix_lists(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        PrefixListIds: Sequence[str] = ...
    ) -> DescribePrefixListsResultTypeDef:
        """
        Describes available Amazon Web Services services in a prefix list format, which
        includes the prefix list name and prefix list ID of the service and the IP
        address range for the
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_prefix_lists)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_prefix_lists)
        """

    def describe_principal_id_format(
        self,
        *,
        DryRun: bool = ...,
        Resources: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribePrincipalIdFormatResultTypeDef:
        """
        Describes the ID format settings for the root user and all IAM roles and IAM
        users that have explicitly specified a longer ID (17-character ID)
        preference.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_principal_id_format)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_principal_id_format)
        """

    def describe_public_ipv4_pools(
        self,
        *,
        PoolIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        Filters: Sequence[FilterTypeDef] = ...
    ) -> DescribePublicIpv4PoolsResultTypeDef:
        """
        Describes the specified IPv4 address pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_public_ipv4_pools)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_public_ipv4_pools)
        """

    def describe_regions(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        RegionNames: Sequence[str] = ...,
        DryRun: bool = ...,
        AllRegions: bool = ...
    ) -> DescribeRegionsResultTypeDef:
        """
        Describes the Regions that are enabled for your account, or all Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_regions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_regions)
        """

    def describe_replace_root_volume_tasks(
        self,
        *,
        ReplaceRootVolumeTaskIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeReplaceRootVolumeTasksResultTypeDef:
        """
        Describes a root volume replacement task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_replace_root_volume_tasks)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_replace_root_volume_tasks)
        """

    def describe_reserved_instances(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        OfferingClass: OfferingClassTypeType = ...,
        ReservedInstancesIds: Sequence[str] = ...,
        DryRun: bool = ...,
        OfferingType: OfferingTypeValuesType = ...
    ) -> DescribeReservedInstancesResultTypeDef:
        """
        Describes one or more of the Reserved Instances that you purchased.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_reserved_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_reserved_instances)
        """

    def describe_reserved_instances_listings(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        ReservedInstancesId: str = ...,
        ReservedInstancesListingId: str = ...
    ) -> DescribeReservedInstancesListingsResultTypeDef:
        """
        Describes your account's Reserved Instance listings in the Reserved Instance
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_reserved_instances_listings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_reserved_instances_listings)
        """

    def describe_reserved_instances_modifications(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        ReservedInstancesModificationIds: Sequence[str] = ...,
        NextToken: str = ...
    ) -> DescribeReservedInstancesModificationsResultTypeDef:
        """
        Describes the modifications made to your Reserved Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_reserved_instances_modifications)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_reserved_instances_modifications)
        """

    def describe_reserved_instances_offerings(
        self,
        *,
        AvailabilityZone: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        IncludeMarketplace: bool = ...,
        InstanceType: InstanceTypeType = ...,
        MaxDuration: int = ...,
        MaxInstanceCount: int = ...,
        MinDuration: int = ...,
        OfferingClass: OfferingClassTypeType = ...,
        ProductDescription: RIProductDescriptionType = ...,
        ReservedInstancesOfferingIds: Sequence[str] = ...,
        DryRun: bool = ...,
        InstanceTenancy: TenancyType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        OfferingType: OfferingTypeValuesType = ...
    ) -> DescribeReservedInstancesOfferingsResultTypeDef:
        """
        Describes Reserved Instance offerings that are available for purchase.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_reserved_instances_offerings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_reserved_instances_offerings)
        """

    def describe_route_tables(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        RouteTableIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeRouteTablesResultTypeDef:
        """
        Describes one or more of your route tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_route_tables)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_route_tables)
        """

    def describe_scheduled_instance_availability(
        self,
        *,
        FirstSlotStartTimeRange: SlotDateTimeRangeRequestTypeDef,
        Recurrence: ScheduledInstanceRecurrenceRequestTypeDef,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        MaxSlotDurationInHours: int = ...,
        MinSlotDurationInHours: int = ...,
        NextToken: str = ...
    ) -> DescribeScheduledInstanceAvailabilityResultTypeDef:
        """
        Finds available schedules that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_scheduled_instance_availability)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_scheduled_instance_availability)
        """

    def describe_scheduled_instances(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        ScheduledInstanceIds: Sequence[str] = ...,
        SlotStartTimeRange: SlotStartTimeRangeRequestTypeDef = ...
    ) -> DescribeScheduledInstancesResultTypeDef:
        """
        Describes the specified Scheduled Instances or all your Scheduled Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_scheduled_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_scheduled_instances)
        """

    def describe_security_group_references(
        self, *, GroupId: Sequence[str], DryRun: bool = ...
    ) -> DescribeSecurityGroupReferencesResultTypeDef:
        """
        Describes the VPCs on the other side of a VPC peering connection or the VPCs
        attached to a transit gateway that are referencing the security groups you've
        specified in this
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_security_group_references)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_security_group_references)
        """

    def describe_security_group_rules(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        SecurityGroupRuleIds: Sequence[str] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeSecurityGroupRulesResultTypeDef:
        """
        Describes one or more of your security group rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_security_group_rules)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_security_group_rules)
        """

    def describe_security_groups(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        GroupIds: Sequence[str] = ...,
        GroupNames: Sequence[str] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeSecurityGroupsResultTypeDef:
        """
        Describes the specified security groups or all of your security groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_security_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_security_groups)
        """

    def describe_snapshot_attribute(
        self, *, Attribute: SnapshotAttributeNameType, SnapshotId: str, DryRun: bool = ...
    ) -> DescribeSnapshotAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_snapshot_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_snapshot_attribute)
        """

    def describe_snapshot_tier_status(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeSnapshotTierStatusResultTypeDef:
        """
        Describes the storage tier status of one or more Amazon EBS snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_snapshot_tier_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_snapshot_tier_status)
        """

    def describe_snapshots(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        OwnerIds: Sequence[str] = ...,
        RestorableByUserIds: Sequence[str] = ...,
        SnapshotIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> DescribeSnapshotsResultTypeDef:
        """
        Describes the specified EBS snapshots available to you or all of the EBS
        snapshots available to
        you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_snapshots)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_snapshots)
        """

    def describe_spot_datafeed_subscription(
        self, *, DryRun: bool = ...
    ) -> DescribeSpotDatafeedSubscriptionResultTypeDef:
        """
        Describes the data feed for Spot Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_datafeed_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_datafeed_subscription)
        """

    def describe_spot_fleet_instances(
        self,
        *,
        SpotFleetRequestId: str,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeSpotFleetInstancesResponseTypeDef:
        """
        Describes the running instances for the specified Spot Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_fleet_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_fleet_instances)
        """

    def describe_spot_fleet_request_history(
        self,
        *,
        SpotFleetRequestId: str,
        StartTime: TimestampTypeDef,
        DryRun: bool = ...,
        EventType: EventTypeType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeSpotFleetRequestHistoryResponseTypeDef:
        """
        Describes the events for the specified Spot Fleet request during the specified
        time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_fleet_request_history)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_fleet_request_history)
        """

    def describe_spot_fleet_requests(
        self,
        *,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        SpotFleetRequestIds: Sequence[str] = ...
    ) -> DescribeSpotFleetRequestsResponseTypeDef:
        """
        Describes your Spot Fleet requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_fleet_requests)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_fleet_requests)
        """

    def describe_spot_instance_requests(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        SpotInstanceRequestIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeSpotInstanceRequestsResultTypeDef:
        """
        Describes the specified Spot Instance requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_instance_requests)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_instance_requests)
        """

    def describe_spot_price_history(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        AvailabilityZone: str = ...,
        DryRun: bool = ...,
        EndTime: TimestampTypeDef = ...,
        InstanceTypes: Sequence[InstanceTypeType] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        ProductDescriptions: Sequence[str] = ...,
        StartTime: TimestampTypeDef = ...
    ) -> DescribeSpotPriceHistoryResultTypeDef:
        """
        Describes the Spot price history.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_spot_price_history)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_price_history)
        """

    def describe_stale_security_groups(
        self, *, VpcId: str, DryRun: bool = ..., MaxResults: int = ..., NextToken: str = ...
    ) -> DescribeStaleSecurityGroupsResultTypeDef:
        """
        Describes the stale security group rules for security groups in a specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_stale_security_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_stale_security_groups)
        """

    def describe_store_image_tasks(
        self,
        *,
        ImageIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeStoreImageTasksResultTypeDef:
        """
        Describes the progress of the AMI store tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_store_image_tasks)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_store_image_tasks)
        """

    def describe_subnets(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        SubnetIds: Sequence[str] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeSubnetsResultTypeDef:
        """
        Describes one or more of your subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_subnets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_subnets)
        """

    def describe_tags(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeTagsResultTypeDef:
        """
        Describes the specified tags for your EC2 resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_tags)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_tags)
        """

    def describe_traffic_mirror_filters(
        self,
        *,
        TrafficMirrorFilterIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeTrafficMirrorFiltersResultTypeDef:
        """
        Describes one or more Traffic Mirror filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_filters)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_traffic_mirror_filters)
        """

    def describe_traffic_mirror_sessions(
        self,
        *,
        TrafficMirrorSessionIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeTrafficMirrorSessionsResultTypeDef:
        """
        Describes one or more Traffic Mirror sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_sessions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_traffic_mirror_sessions)
        """

    def describe_traffic_mirror_targets(
        self,
        *,
        TrafficMirrorTargetIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeTrafficMirrorTargetsResultTypeDef:
        """
        Information about one or more Traffic Mirror targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_targets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_traffic_mirror_targets)
        """

    def describe_transit_gateway_attachments(
        self,
        *,
        TransitGatewayAttachmentIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeTransitGatewayAttachmentsResultTypeDef:
        """
        Describes one or more attachments between resources and transit gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_attachments)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_attachments)
        """

    def describe_transit_gateway_connect_peers(
        self,
        *,
        TransitGatewayConnectPeerIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeTransitGatewayConnectPeersResultTypeDef:
        """
        Describes one or more Connect peers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_connect_peers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_connect_peers)
        """

    def describe_transit_gateway_connects(
        self,
        *,
        TransitGatewayAttachmentIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeTransitGatewayConnectsResultTypeDef:
        """
        Describes one or more Connect attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_connects)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_connects)
        """

    def describe_transit_gateway_multicast_domains(
        self,
        *,
        TransitGatewayMulticastDomainIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeTransitGatewayMulticastDomainsResultTypeDef:
        """
        Describes one or more transit gateway multicast domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_multicast_domains)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_multicast_domains)
        """

    def describe_transit_gateway_peering_attachments(
        self,
        *,
        TransitGatewayAttachmentIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeTransitGatewayPeeringAttachmentsResultTypeDef:
        """
        Describes your transit gateway peering attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_peering_attachments)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_peering_attachments)
        """

    def describe_transit_gateway_policy_tables(
        self,
        *,
        TransitGatewayPolicyTableIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeTransitGatewayPolicyTablesResultTypeDef:
        """
        Describes one or more transit gateway route policy tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_policy_tables)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_policy_tables)
        """

    def describe_transit_gateway_route_table_announcements(
        self,
        *,
        TransitGatewayRouteTableAnnouncementIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef:
        """
        Describes one or more transit gateway route table advertisements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_route_table_announcements)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_route_table_announcements)
        """

    def describe_transit_gateway_route_tables(
        self,
        *,
        TransitGatewayRouteTableIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeTransitGatewayRouteTablesResultTypeDef:
        """
        Describes one or more transit gateway route tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_route_tables)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_route_tables)
        """

    def describe_transit_gateway_vpc_attachments(
        self,
        *,
        TransitGatewayAttachmentIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeTransitGatewayVpcAttachmentsResultTypeDef:
        """
        Describes one or more VPC attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateway_vpc_attachments)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_vpc_attachments)
        """

    def describe_transit_gateways(
        self,
        *,
        TransitGatewayIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> DescribeTransitGatewaysResultTypeDef:
        """
        Describes one or more transit gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_transit_gateways)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateways)
        """

    def describe_trunk_interface_associations(
        self,
        *,
        AssociationIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeTrunkInterfaceAssociationsResultTypeDef:
        """
        Describes one or more network interface trunk associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_trunk_interface_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_trunk_interface_associations)
        """

    def describe_verified_access_endpoints(
        self,
        *,
        VerifiedAccessEndpointIds: Sequence[str] = ...,
        VerifiedAccessInstanceId: str = ...,
        VerifiedAccessGroupId: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeVerifiedAccessEndpointsResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_verified_access_endpoints)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_verified_access_endpoints)
        """

    def describe_verified_access_groups(
        self,
        *,
        VerifiedAccessGroupIds: Sequence[str] = ...,
        VerifiedAccessInstanceId: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeVerifiedAccessGroupsResultTypeDef:
        """
        Describes the specified Verified Access groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_verified_access_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_verified_access_groups)
        """

    def describe_verified_access_instance_logging_configurations(
        self,
        *,
        VerifiedAccessInstanceIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_verified_access_instance_logging_configurations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_verified_access_instance_logging_configurations)
        """

    def describe_verified_access_instances(
        self,
        *,
        VerifiedAccessInstanceIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeVerifiedAccessInstancesResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_verified_access_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_verified_access_instances)
        """

    def describe_verified_access_trust_providers(
        self,
        *,
        VerifiedAccessTrustProviderIds: Sequence[str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> DescribeVerifiedAccessTrustProvidersResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access trust providers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_verified_access_trust_providers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_verified_access_trust_providers)
        """

    def describe_volume_attribute(
        self, *, Attribute: VolumeAttributeNameType, VolumeId: str, DryRun: bool = ...
    ) -> DescribeVolumeAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_volume_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_volume_attribute)
        """

    def describe_volume_status(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        VolumeIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> DescribeVolumeStatusResultTypeDef:
        """
        Describes the status of the specified volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_volume_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_volume_status)
        """

    def describe_volumes(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        VolumeIds: Sequence[str] = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeVolumesResultTypeDef:
        """
        Describes the specified EBS volumes or all of your EBS volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_volumes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_volumes)
        """

    def describe_volumes_modifications(
        self,
        *,
        DryRun: bool = ...,
        VolumeIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeVolumesModificationsResultTypeDef:
        """
        Describes the most recent volume modification request for the specified EBS
        volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_volumes_modifications)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_volumes_modifications)
        """

    def describe_vpc_attribute(
        self, *, Attribute: VpcAttributeNameType, VpcId: str, DryRun: bool = ...
    ) -> DescribeVpcAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_attribute)
        """

    def describe_vpc_classic_link(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        VpcIds: Sequence[str] = ...
    ) -> DescribeVpcClassicLinkResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_classic_link)
        """

    def describe_vpc_classic_link_dns_support(
        self, *, MaxResults: int = ..., NextToken: str = ..., VpcIds: Sequence[str] = ...
    ) -> DescribeVpcClassicLinkDnsSupportResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link_dns_support)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_classic_link_dns_support)
        """

    def describe_vpc_endpoint_connection_notifications(
        self,
        *,
        DryRun: bool = ...,
        ConnectionNotificationId: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeVpcEndpointConnectionNotificationsResultTypeDef:
        """
        Describes the connection notifications for VPC endpoints and VPC endpoint
        services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connection_notifications)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoint_connection_notifications)
        """

    def describe_vpc_endpoint_connections(
        self,
        *,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeVpcEndpointConnectionsResultTypeDef:
        """
        Describes the VPC endpoint connections to your VPC endpoint services, including
        any endpoints that are pending your
        acceptance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connections)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoint_connections)
        """

    def describe_vpc_endpoint_service_configurations(
        self,
        *,
        DryRun: bool = ...,
        ServiceIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeVpcEndpointServiceConfigurationsResultTypeDef:
        """
        Describes the VPC endpoint service configurations in your account (your
        services).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_configurations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoint_service_configurations)
        """

    def describe_vpc_endpoint_service_permissions(
        self,
        *,
        ServiceId: str,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeVpcEndpointServicePermissionsResultTypeDef:
        """
        Describes the principals (service consumers) that are permitted to discover
        your VPC endpoint
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_permissions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoint_service_permissions)
        """

    def describe_vpc_endpoint_services(
        self,
        *,
        DryRun: bool = ...,
        ServiceNames: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeVpcEndpointServicesResultTypeDef:
        """
        Describes available services to which you can create a VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_services)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoint_services)
        """

    def describe_vpc_endpoints(
        self,
        *,
        DryRun: bool = ...,
        VpcEndpointIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeVpcEndpointsResultTypeDef:
        """
        Describes your VPC endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_endpoints)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoints)
        """

    def describe_vpc_peering_connections(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        VpcPeeringConnectionIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeVpcPeeringConnectionsResultTypeDef:
        """
        Describes one or more of your VPC peering connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpc_peering_connections)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_peering_connections)
        """

    def describe_vpcs(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        VpcIds: Sequence[str] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeVpcsResultTypeDef:
        """
        Describes one or more of your VPCs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpcs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpcs)
        """

    def describe_vpn_connections(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        VpnConnectionIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> DescribeVpnConnectionsResultTypeDef:
        """
        Describes one or more of your VPN connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpn_connections)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpn_connections)
        """

    def describe_vpn_gateways(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        VpnGatewayIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> DescribeVpnGatewaysResultTypeDef:
        """
        Describes one or more of your virtual private gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpn_gateways)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpn_gateways)
        """

    def detach_classic_link_vpc(
        self, *, InstanceId: str, VpcId: str, DryRun: bool = ...
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.detach_classic_link_vpc)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_classic_link_vpc)
        """

    def detach_internet_gateway(
        self, *, InternetGatewayId: str, VpcId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Detaches an internet gateway from a VPC, disabling connectivity between the
        internet and the
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.detach_internet_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_internet_gateway)
        """

    def detach_network_interface(
        self, *, AttachmentId: str, DryRun: bool = ..., Force: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Detaches a network interface from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.detach_network_interface)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_network_interface)
        """

    def detach_verified_access_trust_provider(
        self,
        *,
        VerifiedAccessInstanceId: str,
        VerifiedAccessTrustProviderId: str,
        ClientToken: str = ...,
        DryRun: bool = ...
    ) -> DetachVerifiedAccessTrustProviderResultTypeDef:
        """
        Detaches the specified Amazon Web Services Verified Access trust provider from
        the specified Amazon Web Services Verified Access
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.detach_verified_access_trust_provider)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_verified_access_trust_provider)
        """

    def detach_volume(
        self,
        *,
        VolumeId: str,
        Device: str = ...,
        Force: bool = ...,
        InstanceId: str = ...,
        DryRun: bool = ...
    ) -> VolumeAttachmentTypeDef:
        """
        Detaches an EBS volume from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.detach_volume)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_volume)
        """

    def detach_vpn_gateway(
        self, *, VpcId: str, VpnGatewayId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Detaches a virtual private gateway from a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.detach_vpn_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_vpn_gateway)
        """

    def disable_address_transfer(
        self, *, AllocationId: str, DryRun: bool = ...
    ) -> DisableAddressTransferResultTypeDef:
        """
        Disables Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_address_transfer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_address_transfer)
        """

    def disable_aws_network_performance_metric_subscription(
        self,
        *,
        Source: str = ...,
        Destination: str = ...,
        Metric: Literal["aggregate-latency"] = ...,
        Statistic: Literal["p50"] = ...,
        DryRun: bool = ...
    ) -> DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef:
        """
        Disables Infrastructure Performance metric subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_aws_network_performance_metric_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_aws_network_performance_metric_subscription)
        """

    def disable_ebs_encryption_by_default(
        self, *, DryRun: bool = ...
    ) -> DisableEbsEncryptionByDefaultResultTypeDef:
        """
        Disables EBS encryption by default for your account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_ebs_encryption_by_default)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_ebs_encryption_by_default)
        """

    def disable_fast_launch(
        self, *, ImageId: str, Force: bool = ..., DryRun: bool = ...
    ) -> DisableFastLaunchResultTypeDef:
        """
        Discontinue Windows fast launch for a Windows AMI, and clean up existing
        pre-provisioned
        snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_fast_launch)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_fast_launch)
        """

    def disable_fast_snapshot_restores(
        self,
        *,
        AvailabilityZones: Sequence[str],
        SourceSnapshotIds: Sequence[str],
        DryRun: bool = ...
    ) -> DisableFastSnapshotRestoresResultTypeDef:
        """
        Disables fast snapshot restores for the specified snapshots in the specified
        Availability
        Zones.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_fast_snapshot_restores)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_fast_snapshot_restores)
        """

    def disable_image(self, *, ImageId: str, DryRun: bool = ...) -> DisableImageResultTypeDef:
        """
        Sets the AMI state to `disabled` and removes all launch permissions from the
        AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_image)
        """

    def disable_image_block_public_access(
        self, *, DryRun: bool = ...
    ) -> DisableImageBlockPublicAccessResultTypeDef:
        """
        Disables *block public access for AMIs* at the account level in the specified
        Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_image_block_public_access)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_image_block_public_access)
        """

    def disable_image_deprecation(
        self, *, ImageId: str, DryRun: bool = ...
    ) -> DisableImageDeprecationResultTypeDef:
        """
        Cancels the deprecation of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_image_deprecation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_image_deprecation)
        """

    def disable_ipam_organization_admin_account(
        self, *, DelegatedAdminAccountId: str, DryRun: bool = ...
    ) -> DisableIpamOrganizationAdminAccountResultTypeDef:
        """
        Disable the IPAM account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_ipam_organization_admin_account)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_ipam_organization_admin_account)
        """

    def disable_serial_console_access(
        self, *, DryRun: bool = ...
    ) -> DisableSerialConsoleAccessResultTypeDef:
        """
        Disables access to the EC2 serial console of all instances for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_serial_console_access)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_serial_console_access)
        """

    def disable_snapshot_block_public_access(
        self, *, DryRun: bool = ...
    ) -> DisableSnapshotBlockPublicAccessResultTypeDef:
        """
        Disables the *block public access for snapshots* setting at the account level
        for the specified Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_snapshot_block_public_access)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_snapshot_block_public_access)
        """

    def disable_transit_gateway_route_table_propagation(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = ...,
        DryRun: bool = ...,
        TransitGatewayRouteTableAnnouncementId: str = ...
    ) -> DisableTransitGatewayRouteTablePropagationResultTypeDef:
        """
        Disables the specified resource attachment from propagating routes to the
        specified propagation route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_transit_gateway_route_table_propagation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_transit_gateway_route_table_propagation)
        """

    def disable_vgw_route_propagation(
        self, *, GatewayId: str, RouteTableId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disables a virtual private gateway (VGW) from propagating routes to a specified
        route table of a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_vgw_route_propagation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_vgw_route_propagation)
        """

    def disable_vpc_classic_link(
        self, *, VpcId: str, DryRun: bool = ...
    ) -> DisableVpcClassicLinkResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_vpc_classic_link)
        """

    def disable_vpc_classic_link_dns_support(
        self, *, VpcId: str = ...
    ) -> DisableVpcClassicLinkDnsSupportResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link_dns_support)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_vpc_classic_link_dns_support)
        """

    def disassociate_address(
        self, *, AssociationId: str = ..., PublicIp: str = ..., DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates an Elastic IP address from the instance or network interface it's
        associated
        with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_address)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_address)
        """

    def disassociate_client_vpn_target_network(
        self, *, ClientVpnEndpointId: str, AssociationId: str, DryRun: bool = ...
    ) -> DisassociateClientVpnTargetNetworkResultTypeDef:
        """
        Disassociates a target network from the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_client_vpn_target_network)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_client_vpn_target_network)
        """

    def disassociate_enclave_certificate_iam_role(
        self, *, CertificateArn: str, RoleArn: str, DryRun: bool = ...
    ) -> DisassociateEnclaveCertificateIamRoleResultTypeDef:
        """
        Disassociates an IAM role from an Certificate Manager (ACM) certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_enclave_certificate_iam_role)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_enclave_certificate_iam_role)
        """

    def disassociate_iam_instance_profile(
        self, *, AssociationId: str
    ) -> DisassociateIamInstanceProfileResultTypeDef:
        """
        Disassociates an IAM instance profile from a running or stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_iam_instance_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_iam_instance_profile)
        """

    def disassociate_instance_event_window(
        self,
        *,
        InstanceEventWindowId: str,
        AssociationTarget: InstanceEventWindowDisassociationRequestTypeDef,
        DryRun: bool = ...
    ) -> DisassociateInstanceEventWindowResultTypeDef:
        """
        Disassociates one or more targets from an event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_instance_event_window)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_instance_event_window)
        """

    def disassociate_ipam_byoasn(
        self, *, Asn: str, Cidr: str, DryRun: bool = ...
    ) -> DisassociateIpamByoasnResultTypeDef:
        """
        Remove the association between your Autonomous System Number (ASN) and your
        BYOIP
        CIDR.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_ipam_byoasn)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_ipam_byoasn)
        """

    def disassociate_ipam_resource_discovery(
        self, *, IpamResourceDiscoveryAssociationId: str, DryRun: bool = ...
    ) -> DisassociateIpamResourceDiscoveryResultTypeDef:
        """
        Disassociates a resource discovery from an Amazon VPC IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_ipam_resource_discovery)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_ipam_resource_discovery)
        """

    def disassociate_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        AssociationIds: Sequence[str],
        MaxDrainDurationSeconds: int = ...,
        DryRun: bool = ...
    ) -> DisassociateNatGatewayAddressResultTypeDef:
        """
        Disassociates secondary Elastic IP addresses (EIPs) from a public NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_nat_gateway_address)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_nat_gateway_address)
        """

    def disassociate_route_table(
        self, *, AssociationId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates a subnet or gateway from a route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_route_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_route_table)
        """

    def disassociate_subnet_cidr_block(
        self, *, AssociationId: str
    ) -> DisassociateSubnetCidrBlockResultTypeDef:
        """
        Disassociates a CIDR block from a subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_subnet_cidr_block)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_subnet_cidr_block)
        """

    def disassociate_transit_gateway_multicast_domain(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        TransitGatewayAttachmentId: str,
        SubnetIds: Sequence[str],
        DryRun: bool = ...
    ) -> DisassociateTransitGatewayMulticastDomainResultTypeDef:
        """
        Disassociates the specified subnets from the transit gateway multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_transit_gateway_multicast_domain)
        """

    def disassociate_transit_gateway_policy_table(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool = ...
    ) -> DisassociateTransitGatewayPolicyTableResultTypeDef:
        """
        Removes the association between an an attachment and a policy table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_policy_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_transit_gateway_policy_table)
        """

    def disassociate_transit_gateway_route_table(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool = ...
    ) -> DisassociateTransitGatewayRouteTableResultTypeDef:
        """
        Disassociates a resource attachment from a transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_transit_gateway_route_table)
        """

    def disassociate_trunk_interface(
        self, *, AssociationId: str, ClientToken: str = ..., DryRun: bool = ...
    ) -> DisassociateTrunkInterfaceResultTypeDef:
        """
        Removes an association between a branch network interface with a trunk network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_trunk_interface)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_trunk_interface)
        """

    def disassociate_vpc_cidr_block(
        self, *, AssociationId: str
    ) -> DisassociateVpcCidrBlockResultTypeDef:
        """
        Disassociates a CIDR block from a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.disassociate_vpc_cidr_block)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_vpc_cidr_block)
        """

    def enable_address_transfer(
        self, *, AllocationId: str, TransferAccountId: str, DryRun: bool = ...
    ) -> EnableAddressTransferResultTypeDef:
        """
        Enables Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_address_transfer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_address_transfer)
        """

    def enable_aws_network_performance_metric_subscription(
        self,
        *,
        Source: str = ...,
        Destination: str = ...,
        Metric: Literal["aggregate-latency"] = ...,
        Statistic: Literal["p50"] = ...,
        DryRun: bool = ...
    ) -> EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef:
        """
        Enables Infrastructure Performance subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_aws_network_performance_metric_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_aws_network_performance_metric_subscription)
        """

    def enable_ebs_encryption_by_default(
        self, *, DryRun: bool = ...
    ) -> EnableEbsEncryptionByDefaultResultTypeDef:
        """
        Enables EBS encryption by default for your account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_ebs_encryption_by_default)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_ebs_encryption_by_default)
        """

    def enable_fast_launch(
        self,
        *,
        ImageId: str,
        ResourceType: str = ...,
        SnapshotConfiguration: FastLaunchSnapshotConfigurationRequestTypeDef = ...,
        LaunchTemplate: FastLaunchLaunchTemplateSpecificationRequestTypeDef = ...,
        MaxParallelLaunches: int = ...,
        DryRun: bool = ...
    ) -> EnableFastLaunchResultTypeDef:
        """
        When you enable Windows fast launch for a Windows AMI, images are
        pre-provisioned, using snapshots to launch instances up to 65%
        faster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_fast_launch)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_fast_launch)
        """

    def enable_fast_snapshot_restores(
        self,
        *,
        AvailabilityZones: Sequence[str],
        SourceSnapshotIds: Sequence[str],
        DryRun: bool = ...
    ) -> EnableFastSnapshotRestoresResultTypeDef:
        """
        Enables fast snapshot restores for the specified snapshots in the specified
        Availability
        Zones.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_fast_snapshot_restores)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_fast_snapshot_restores)
        """

    def enable_image(self, *, ImageId: str, DryRun: bool = ...) -> EnableImageResultTypeDef:
        """
        Re-enables a disabled AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_image)
        """

    def enable_image_block_public_access(
        self, *, ImageBlockPublicAccessState: Literal["block-new-sharing"], DryRun: bool = ...
    ) -> EnableImageBlockPublicAccessResultTypeDef:
        """
        Enables *block public access for AMIs* at the account level in the specified
        Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_image_block_public_access)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_image_block_public_access)
        """

    def enable_image_deprecation(
        self, *, ImageId: str, DeprecateAt: TimestampTypeDef, DryRun: bool = ...
    ) -> EnableImageDeprecationResultTypeDef:
        """
        Enables deprecation of the specified AMI at the specified date and time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_image_deprecation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_image_deprecation)
        """

    def enable_ipam_organization_admin_account(
        self, *, DelegatedAdminAccountId: str, DryRun: bool = ...
    ) -> EnableIpamOrganizationAdminAccountResultTypeDef:
        """
        Enable an Organizations member account as the IPAM admin account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_ipam_organization_admin_account)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_ipam_organization_admin_account)
        """

    def enable_reachability_analyzer_organization_sharing(
        self, *, DryRun: bool = ...
    ) -> EnableReachabilityAnalyzerOrganizationSharingResultTypeDef:
        """
        Establishes a trust relationship between Reachability Analyzer and
        Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_reachability_analyzer_organization_sharing)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_reachability_analyzer_organization_sharing)
        """

    def enable_serial_console_access(
        self, *, DryRun: bool = ...
    ) -> EnableSerialConsoleAccessResultTypeDef:
        """
        Enables access to the EC2 serial console of all instances for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_serial_console_access)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_serial_console_access)
        """

    def enable_snapshot_block_public_access(
        self, *, State: SnapshotBlockPublicAccessStateType, DryRun: bool = ...
    ) -> EnableSnapshotBlockPublicAccessResultTypeDef:
        """
        Enables or modifies the *block public access for snapshots* setting at the
        account level for the specified Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_snapshot_block_public_access)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_snapshot_block_public_access)
        """

    def enable_transit_gateway_route_table_propagation(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = ...,
        DryRun: bool = ...,
        TransitGatewayRouteTableAnnouncementId: str = ...
    ) -> EnableTransitGatewayRouteTablePropagationResultTypeDef:
        """
        Enables the specified attachment to propagate routes to the specified
        propagation route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_transit_gateway_route_table_propagation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_transit_gateway_route_table_propagation)
        """

    def enable_vgw_route_propagation(
        self, *, GatewayId: str, RouteTableId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables a virtual private gateway (VGW) to propagate routes to the specified
        route table of a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_vgw_route_propagation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_vgw_route_propagation)
        """

    def enable_volume_io(
        self, *, VolumeId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables I/O operations for a volume that had I/O operations disabled because
        the data on the volume was potentially
        inconsistent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_volume_io)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_volume_io)
        """

    def enable_vpc_classic_link(
        self, *, VpcId: str, DryRun: bool = ...
    ) -> EnableVpcClassicLinkResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_vpc_classic_link)
        """

    def enable_vpc_classic_link_dns_support(
        self, *, VpcId: str = ...
    ) -> EnableVpcClassicLinkDnsSupportResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link_dns_support)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_vpc_classic_link_dns_support)
        """

    def export_client_vpn_client_certificate_revocation_list(
        self, *, ClientVpnEndpointId: str, DryRun: bool = ...
    ) -> ExportClientVpnClientCertificateRevocationListResultTypeDef:
        """
        Downloads the client certificate revocation list for the specified Client VPN
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.export_client_vpn_client_certificate_revocation_list)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#export_client_vpn_client_certificate_revocation_list)
        """

    def export_client_vpn_client_configuration(
        self, *, ClientVpnEndpointId: str, DryRun: bool = ...
    ) -> ExportClientVpnClientConfigurationResultTypeDef:
        """
        Downloads the contents of the Client VPN endpoint configuration file for the
        specified Client VPN
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.export_client_vpn_client_configuration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#export_client_vpn_client_configuration)
        """

    def export_image(
        self,
        *,
        DiskImageFormat: DiskImageFormatType,
        ImageId: str,
        S3ExportLocation: ExportTaskS3LocationRequestTypeDef,
        ClientToken: str = ...,
        Description: str = ...,
        DryRun: bool = ...,
        RoleName: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> ExportImageResultTypeDef:
        """
        Exports an Amazon Machine Image (AMI) to a VM file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.export_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#export_image)
        """

    def export_transit_gateway_routes(
        self,
        *,
        TransitGatewayRouteTableId: str,
        S3Bucket: str,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> ExportTransitGatewayRoutesResultTypeDef:
        """
        Exports routes from the specified transit gateway route table to the specified
        S3
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.export_transit_gateway_routes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#export_transit_gateway_routes)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#generate_presigned_url)
        """

    def get_associated_enclave_certificate_iam_roles(
        self, *, CertificateArn: str, DryRun: bool = ...
    ) -> GetAssociatedEnclaveCertificateIamRolesResultTypeDef:
        """
        Returns the IAM roles that are associated with the specified ACM (ACM)
        certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_associated_enclave_certificate_iam_roles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_associated_enclave_certificate_iam_roles)
        """

    def get_associated_ipv6_pool_cidrs(
        self, *, PoolId: str, NextToken: str = ..., MaxResults: int = ..., DryRun: bool = ...
    ) -> GetAssociatedIpv6PoolCidrsResultTypeDef:
        """
        Gets information about the IPv6 CIDR block associations for a specified IPv6
        address
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_associated_ipv6_pool_cidrs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_associated_ipv6_pool_cidrs)
        """

    def get_aws_network_performance_data(
        self,
        *,
        DataQueries: Sequence[DataQueryTypeDef] = ...,
        StartTime: TimestampTypeDef = ...,
        EndTime: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> GetAwsNetworkPerformanceDataResultTypeDef:
        """
        Gets network performance data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_aws_network_performance_data)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_aws_network_performance_data)
        """

    def get_capacity_reservation_usage(
        self,
        *,
        CapacityReservationId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...
    ) -> GetCapacityReservationUsageResultTypeDef:
        """
        Gets usage information about a Capacity Reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_capacity_reservation_usage)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_capacity_reservation_usage)
        """

    def get_coip_pool_usage(
        self,
        *,
        PoolId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> GetCoipPoolUsageResultTypeDef:
        """
        Describes the allocations from the specified customer-owned address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_coip_pool_usage)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_coip_pool_usage)
        """

    def get_console_output(
        self, *, InstanceId: str, DryRun: bool = ..., Latest: bool = ...
    ) -> GetConsoleOutputResultTypeDef:
        """
        Gets the console output for the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_console_output)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_console_output)
        """

    def get_console_screenshot(
        self, *, InstanceId: str, DryRun: bool = ..., WakeUp: bool = ...
    ) -> GetConsoleScreenshotResultTypeDef:
        """
        Retrieve a JPG-format screenshot of a running instance to help with
        troubleshooting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_console_screenshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_console_screenshot)
        """

    def get_default_credit_specification(
        self, *, InstanceFamily: UnlimitedSupportedInstanceFamilyType, DryRun: bool = ...
    ) -> GetDefaultCreditSpecificationResultTypeDef:
        """
        Describes the default credit option for CPU usage of a burstable performance
        instance
        family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_default_credit_specification)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_default_credit_specification)
        """

    def get_ebs_default_kms_key_id(
        self, *, DryRun: bool = ...
    ) -> GetEbsDefaultKmsKeyIdResultTypeDef:
        """
        Describes the default KMS key for EBS encryption by default for your account in
        this
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_ebs_default_kms_key_id)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ebs_default_kms_key_id)
        """

    def get_ebs_encryption_by_default(
        self, *, DryRun: bool = ...
    ) -> GetEbsEncryptionByDefaultResultTypeDef:
        """
        Describes whether EBS encryption by default is enabled for your account in the
        current
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_ebs_encryption_by_default)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ebs_encryption_by_default)
        """

    def get_flow_logs_integration_template(
        self,
        *,
        FlowLogId: str,
        ConfigDeliveryS3DestinationArn: str,
        IntegrateServices: IntegrateServicesTypeDef,
        DryRun: bool = ...
    ) -> GetFlowLogsIntegrationTemplateResultTypeDef:
        """
        Generates a CloudFormation template that streamlines and automates the
        integration of VPC flow logs with Amazon
        Athena.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_flow_logs_integration_template)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_flow_logs_integration_template)
        """

    def get_groups_for_capacity_reservation(
        self,
        *,
        CapacityReservationId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...
    ) -> GetGroupsForCapacityReservationResultTypeDef:
        """
        Lists the resource groups to which a Capacity Reservation has been added.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_groups_for_capacity_reservation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_groups_for_capacity_reservation)
        """

    def get_host_reservation_purchase_preview(
        self, *, HostIdSet: Sequence[str], OfferingId: str
    ) -> GetHostReservationPurchasePreviewResultTypeDef:
        """
        Preview a reservation purchase with configurations that match those of your
        Dedicated
        Host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_host_reservation_purchase_preview)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_host_reservation_purchase_preview)
        """

    def get_image_block_public_access_state(
        self, *, DryRun: bool = ...
    ) -> GetImageBlockPublicAccessStateResultTypeDef:
        """
        Gets the current state of *block public access for AMIs* at the account level
        in the specified Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_image_block_public_access_state)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_image_block_public_access_state)
        """

    def get_instance_types_from_instance_requirements(
        self,
        *,
        ArchitectureTypes: Sequence[ArchitectureTypeType],
        VirtualizationTypes: Sequence[VirtualizationTypeType],
        InstanceRequirements: InstanceRequirementsRequestTypeDef,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> GetInstanceTypesFromInstanceRequirementsResultTypeDef:
        """
        Returns a list of instance types with the specified instance attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_instance_types_from_instance_requirements)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_instance_types_from_instance_requirements)
        """

    def get_instance_uefi_data(
        self, *, InstanceId: str, DryRun: bool = ...
    ) -> GetInstanceUefiDataResultTypeDef:
        """
        A binary representation of the UEFI variable store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_instance_uefi_data)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_instance_uefi_data)
        """

    def get_ipam_address_history(
        self,
        *,
        Cidr: str,
        IpamScopeId: str,
        DryRun: bool = ...,
        VpcId: str = ...,
        StartTime: TimestampTypeDef = ...,
        EndTime: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> GetIpamAddressHistoryResultTypeDef:
        """
        Retrieve historical information about a CIDR within an IPAM scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_ipam_address_history)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_address_history)
        """

    def get_ipam_discovered_accounts(
        self,
        *,
        IpamResourceDiscoveryId: str,
        DiscoveryRegion: str,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> GetIpamDiscoveredAccountsResultTypeDef:
        """
        Gets IPAM discovered accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_ipam_discovered_accounts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_discovered_accounts)
        """

    def get_ipam_discovered_public_addresses(
        self,
        *,
        IpamResourceDiscoveryId: str,
        AddressRegion: str,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> GetIpamDiscoveredPublicAddressesResultTypeDef:
        """
        Gets the public IP addresses that have been discovered by IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_ipam_discovered_public_addresses)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_discovered_public_addresses)
        """

    def get_ipam_discovered_resource_cidrs(
        self,
        *,
        IpamResourceDiscoveryId: str,
        ResourceRegion: str,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> GetIpamDiscoveredResourceCidrsResultTypeDef:
        """
        Returns the resource CIDRs that are monitored as part of a resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_ipam_discovered_resource_cidrs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_discovered_resource_cidrs)
        """

    def get_ipam_pool_allocations(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = ...,
        IpamPoolAllocationId: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> GetIpamPoolAllocationsResultTypeDef:
        """
        Get a list of all the CIDR allocations in an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_ipam_pool_allocations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_pool_allocations)
        """

    def get_ipam_pool_cidrs(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> GetIpamPoolCidrsResultTypeDef:
        """
        Get the CIDRs provisioned to an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_ipam_pool_cidrs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_pool_cidrs)
        """

    def get_ipam_resource_cidrs(
        self,
        *,
        IpamScopeId: str,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        IpamPoolId: str = ...,
        ResourceId: str = ...,
        ResourceType: IpamResourceTypeType = ...,
        ResourceTag: RequestIpamResourceTagTypeDef = ...,
        ResourceOwner: str = ...
    ) -> GetIpamResourceCidrsResultTypeDef:
        """
        Returns resource CIDRs managed by IPAM in a given scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_ipam_resource_cidrs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_resource_cidrs)
        """

    def get_launch_template_data(
        self, *, InstanceId: str, DryRun: bool = ...
    ) -> GetLaunchTemplateDataResultTypeDef:
        """
        Retrieves the configuration data of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_launch_template_data)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_launch_template_data)
        """

    def get_managed_prefix_list_associations(
        self, *, PrefixListId: str, DryRun: bool = ..., MaxResults: int = ..., NextToken: str = ...
    ) -> GetManagedPrefixListAssociationsResultTypeDef:
        """
        Gets information about the resources that are associated with the specified
        managed prefix
        list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_managed_prefix_list_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_managed_prefix_list_associations)
        """

    def get_managed_prefix_list_entries(
        self,
        *,
        PrefixListId: str,
        DryRun: bool = ...,
        TargetVersion: int = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> GetManagedPrefixListEntriesResultTypeDef:
        """
        Gets information about the entries for a specified managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_managed_prefix_list_entries)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_managed_prefix_list_entries)
        """

    def get_network_insights_access_scope_analysis_findings(
        self,
        *,
        NetworkInsightsAccessScopeAnalysisId: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef:
        """
        Gets the findings for the specified Network Access Scope analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_network_insights_access_scope_analysis_findings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_network_insights_access_scope_analysis_findings)
        """

    def get_network_insights_access_scope_content(
        self, *, NetworkInsightsAccessScopeId: str, DryRun: bool = ...
    ) -> GetNetworkInsightsAccessScopeContentResultTypeDef:
        """
        Gets the content for the specified Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_network_insights_access_scope_content)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_network_insights_access_scope_content)
        """

    def get_password_data(
        self, *, InstanceId: str, DryRun: bool = ...
    ) -> GetPasswordDataResultTypeDef:
        """
        Retrieves the encrypted administrator password for a running Windows instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_password_data)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_password_data)
        """

    def get_reserved_instances_exchange_quote(
        self,
        *,
        ReservedInstanceIds: Sequence[str],
        DryRun: bool = ...,
        TargetConfigurations: Sequence[TargetConfigurationRequestTypeDef] = ...
    ) -> GetReservedInstancesExchangeQuoteResultTypeDef:
        """
        Returns a quote and exchange information for exchanging one or more specified
        Convertible Reserved Instances for a new Convertible Reserved
        Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_reserved_instances_exchange_quote)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_reserved_instances_exchange_quote)
        """

    def get_security_groups_for_vpc(
        self,
        *,
        VpcId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...
    ) -> GetSecurityGroupsForVpcResultTypeDef:
        """
        Gets security groups that can be associated by the Amazon Web Services account
        making the request with network interfaces in the specified
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_security_groups_for_vpc)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_security_groups_for_vpc)
        """

    def get_serial_console_access_status(
        self, *, DryRun: bool = ...
    ) -> GetSerialConsoleAccessStatusResultTypeDef:
        """
        Retrieves the access status of your account to the EC2 serial console of all
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_serial_console_access_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_serial_console_access_status)
        """

    def get_snapshot_block_public_access_state(
        self, *, DryRun: bool = ...
    ) -> GetSnapshotBlockPublicAccessStateResultTypeDef:
        """
        Gets the current state of *block public access for snapshots* setting for the
        account and
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_snapshot_block_public_access_state)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_snapshot_block_public_access_state)
        """

    def get_spot_placement_scores(
        self,
        *,
        TargetCapacity: int,
        InstanceTypes: Sequence[str] = ...,
        TargetCapacityUnitType: TargetCapacityUnitTypeType = ...,
        SingleAvailabilityZone: bool = ...,
        RegionNames: Sequence[str] = ...,
        InstanceRequirementsWithMetadata: InstanceRequirementsWithMetadataRequestTypeDef = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> GetSpotPlacementScoresResultTypeDef:
        """
        Calculates the Spot placement score for a Region or Availability Zone based on
        the specified target capacity and compute
        requirements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_spot_placement_scores)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_spot_placement_scores)
        """

    def get_subnet_cidr_reservations(
        self,
        *,
        SubnetId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> GetSubnetCidrReservationsResultTypeDef:
        """
        Gets information about the subnet CIDR reservations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_subnet_cidr_reservations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_subnet_cidr_reservations)
        """

    def get_transit_gateway_attachment_propagations(
        self,
        *,
        TransitGatewayAttachmentId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> GetTransitGatewayAttachmentPropagationsResultTypeDef:
        """
        Lists the route tables to which the specified resource attachment propagates
        routes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_attachment_propagations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_attachment_propagations)
        """

    def get_transit_gateway_multicast_domain_associations(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> GetTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        Gets information about the associations for the transit gateway multicast
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_multicast_domain_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_multicast_domain_associations)
        """

    def get_transit_gateway_policy_table_associations(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> GetTransitGatewayPolicyTableAssociationsResultTypeDef:
        """
        Gets a list of the transit gateway policy table associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_policy_table_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_policy_table_associations)
        """

    def get_transit_gateway_policy_table_entries(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> GetTransitGatewayPolicyTableEntriesResultTypeDef:
        """
        Returns a list of transit gateway policy table entries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_policy_table_entries)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_policy_table_entries)
        """

    def get_transit_gateway_prefix_list_references(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> GetTransitGatewayPrefixListReferencesResultTypeDef:
        """
        Gets information about the prefix list references in a specified transit
        gateway route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_prefix_list_references)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_prefix_list_references)
        """

    def get_transit_gateway_route_table_associations(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> GetTransitGatewayRouteTableAssociationsResultTypeDef:
        """
        Gets information about the associations for the specified transit gateway route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_route_table_associations)
        """

    def get_transit_gateway_route_table_propagations(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> GetTransitGatewayRouteTablePropagationsResultTypeDef:
        """
        Gets information about the route table propagations for the specified transit
        gateway route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_propagations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_route_table_propagations)
        """

    def get_verified_access_endpoint_policy(
        self, *, VerifiedAccessEndpointId: str, DryRun: bool = ...
    ) -> GetVerifiedAccessEndpointPolicyResultTypeDef:
        """
        Get the Verified Access policy associated with the endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_verified_access_endpoint_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_verified_access_endpoint_policy)
        """

    def get_verified_access_group_policy(
        self, *, VerifiedAccessGroupId: str, DryRun: bool = ...
    ) -> GetVerifiedAccessGroupPolicyResultTypeDef:
        """
        Shows the contents of the Verified Access policy associated with the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_verified_access_group_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_verified_access_group_policy)
        """

    def get_vpn_connection_device_sample_configuration(
        self,
        *,
        VpnConnectionId: str,
        VpnConnectionDeviceTypeId: str,
        InternetKeyExchangeVersion: str = ...,
        DryRun: bool = ...
    ) -> GetVpnConnectionDeviceSampleConfigurationResultTypeDef:
        """
        Download an Amazon Web Services-provided sample configuration file to be used
        with the customer gateway device specified for your Site-to-Site VPN
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_vpn_connection_device_sample_configuration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_vpn_connection_device_sample_configuration)
        """

    def get_vpn_connection_device_types(
        self, *, MaxResults: int = ..., NextToken: str = ..., DryRun: bool = ...
    ) -> GetVpnConnectionDeviceTypesResultTypeDef:
        """
        Obtain a list of customer gateway devices for which sample configuration files
        can be
        provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_vpn_connection_device_types)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_vpn_connection_device_types)
        """

    def get_vpn_tunnel_replacement_status(
        self, *, VpnConnectionId: str, VpnTunnelOutsideIpAddress: str, DryRun: bool = ...
    ) -> GetVpnTunnelReplacementStatusResultTypeDef:
        """
        Get details of available tunnel endpoint maintenance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_vpn_tunnel_replacement_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_vpn_tunnel_replacement_status)
        """

    def import_client_vpn_client_certificate_revocation_list(
        self, *, ClientVpnEndpointId: str, CertificateRevocationList: str, DryRun: bool = ...
    ) -> ImportClientVpnClientCertificateRevocationListResultTypeDef:
        """
        Uploads a client certificate revocation list to the specified Client VPN
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_client_vpn_client_certificate_revocation_list)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_client_vpn_client_certificate_revocation_list)
        """

    def import_image(
        self,
        *,
        Architecture: str = ...,
        ClientData: ClientDataTypeDef = ...,
        ClientToken: str = ...,
        Description: str = ...,
        DiskContainers: Sequence[ImageDiskContainerTypeDef] = ...,
        DryRun: bool = ...,
        Encrypted: bool = ...,
        Hypervisor: str = ...,
        KmsKeyId: str = ...,
        LicenseType: str = ...,
        Platform: str = ...,
        RoleName: str = ...,
        LicenseSpecifications: Sequence[ImportImageLicenseConfigurationRequestTypeDef] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        UsageOperation: str = ...,
        BootMode: BootModeValuesType = ...
    ) -> ImportImageResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_image)
        """

    def import_instance(
        self,
        *,
        Platform: Literal["Windows"],
        Description: str = ...,
        DiskImages: Sequence[DiskImageTypeDef] = ...,
        DryRun: bool = ...,
        LaunchSpecification: ImportInstanceLaunchSpecificationTypeDef = ...
    ) -> ImportInstanceResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_instance)
        """

    def import_key_pair(
        self,
        *,
        KeyName: str,
        PublicKeyMaterial: BlobTypeDef,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> ImportKeyPairResultTypeDef:
        """
        Imports the public key from an RSA or ED25519 key pair that you created with a
        third-party
        tool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_key_pair)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_key_pair)
        """

    def import_snapshot(
        self,
        *,
        ClientData: ClientDataTypeDef = ...,
        ClientToken: str = ...,
        Description: str = ...,
        DiskContainer: SnapshotDiskContainerTypeDef = ...,
        DryRun: bool = ...,
        Encrypted: bool = ...,
        KmsKeyId: str = ...,
        RoleName: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> ImportSnapshotResultTypeDef:
        """
        Imports a disk into an EBS snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_snapshot)
        """

    def import_volume(
        self,
        *,
        AvailabilityZone: str,
        Image: DiskImageDetailTypeDef,
        Volume: VolumeDetailTypeDef,
        Description: str = ...,
        DryRun: bool = ...
    ) -> ImportVolumeResultTypeDef:
        """
        Creates an import volume task using metadata from the specified disk image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.import_volume)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_volume)
        """

    def list_images_in_recycle_bin(
        self,
        *,
        ImageIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...
    ) -> ListImagesInRecycleBinResultTypeDef:
        """
        Lists one or more AMIs that are currently in the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.list_images_in_recycle_bin)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#list_images_in_recycle_bin)
        """

    def list_snapshots_in_recycle_bin(
        self,
        *,
        MaxResults: int = ...,
        NextToken: str = ...,
        SnapshotIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> ListSnapshotsInRecycleBinResultTypeDef:
        """
        Lists one or more snapshots that are currently in the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.list_snapshots_in_recycle_bin)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#list_snapshots_in_recycle_bin)
        """

    def lock_snapshot(
        self,
        *,
        SnapshotId: str,
        LockMode: LockModeType,
        DryRun: bool = ...,
        CoolOffPeriod: int = ...,
        LockDuration: int = ...,
        ExpirationDate: TimestampTypeDef = ...
    ) -> LockSnapshotResultTypeDef:
        """
        Locks an Amazon EBS snapshot in either *governance* or *compliance* mode to
        protect it against accidental or malicious deletions for a specific
        duration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.lock_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#lock_snapshot)
        """

    def modify_address_attribute(
        self, *, AllocationId: str, DomainName: str = ..., DryRun: bool = ...
    ) -> ModifyAddressAttributeResultTypeDef:
        """
        Modifies an attribute of the specified Elastic IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_address_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_address_attribute)
        """

    def modify_availability_zone_group(
        self,
        *,
        GroupName: str,
        OptInStatus: ModifyAvailabilityZoneOptInStatusType,
        DryRun: bool = ...
    ) -> ModifyAvailabilityZoneGroupResultTypeDef:
        """
        Changes the opt-in status of the Local Zone and Wavelength Zone group for your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_availability_zone_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_availability_zone_group)
        """

    def modify_capacity_reservation(
        self,
        *,
        CapacityReservationId: str,
        InstanceCount: int = ...,
        EndDate: TimestampTypeDef = ...,
        EndDateType: EndDateTypeType = ...,
        Accept: bool = ...,
        DryRun: bool = ...,
        AdditionalInfo: str = ...
    ) -> ModifyCapacityReservationResultTypeDef:
        """
        Modifies a Capacity Reservation's capacity and the conditions under which it is
        to be
        released.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_capacity_reservation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_capacity_reservation)
        """

    def modify_capacity_reservation_fleet(
        self,
        *,
        CapacityReservationFleetId: str,
        TotalTargetCapacity: int = ...,
        EndDate: TimestampTypeDef = ...,
        DryRun: bool = ...,
        RemoveEndDate: bool = ...
    ) -> ModifyCapacityReservationFleetResultTypeDef:
        """
        Modifies a Capacity Reservation Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_capacity_reservation_fleet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_capacity_reservation_fleet)
        """

    def modify_client_vpn_endpoint(
        self,
        *,
        ClientVpnEndpointId: str,
        ServerCertificateArn: str = ...,
        ConnectionLogOptions: ConnectionLogOptionsTypeDef = ...,
        DnsServers: DnsServersOptionsModifyStructureTypeDef = ...,
        VpnPort: int = ...,
        Description: str = ...,
        SplitTunnel: bool = ...,
        DryRun: bool = ...,
        SecurityGroupIds: Sequence[str] = ...,
        VpcId: str = ...,
        SelfServicePortal: SelfServicePortalType = ...,
        ClientConnectOptions: ClientConnectOptionsTypeDef = ...,
        SessionTimeoutHours: int = ...,
        ClientLoginBannerOptions: ClientLoginBannerOptionsTypeDef = ...
    ) -> ModifyClientVpnEndpointResultTypeDef:
        """
        Modifies the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_client_vpn_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_client_vpn_endpoint)
        """

    def modify_default_credit_specification(
        self,
        *,
        InstanceFamily: UnlimitedSupportedInstanceFamilyType,
        CpuCredits: str,
        DryRun: bool = ...
    ) -> ModifyDefaultCreditSpecificationResultTypeDef:
        """
        Modifies the default credit option for CPU usage of burstable performance
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_default_credit_specification)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_default_credit_specification)
        """

    def modify_ebs_default_kms_key_id(
        self, *, KmsKeyId: str, DryRun: bool = ...
    ) -> ModifyEbsDefaultKmsKeyIdResultTypeDef:
        """
        Changes the default KMS key for EBS encryption by default for your account in
        this
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_ebs_default_kms_key_id)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ebs_default_kms_key_id)
        """

    def modify_fleet(
        self,
        *,
        FleetId: str,
        DryRun: bool = ...,
        ExcessCapacityTerminationPolicy: FleetExcessCapacityTerminationPolicyType = ...,
        LaunchTemplateConfigs: Sequence[FleetLaunchTemplateConfigRequestTypeDef] = ...,
        TargetCapacitySpecification: TargetCapacitySpecificationRequestTypeDef = ...,
        Context: str = ...
    ) -> ModifyFleetResultTypeDef:
        """
        Modifies the specified EC2 Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_fleet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_fleet)
        """

    def modify_fpga_image_attribute(
        self,
        *,
        FpgaImageId: str,
        DryRun: bool = ...,
        Attribute: FpgaImageAttributeNameType = ...,
        OperationType: OperationTypeType = ...,
        UserIds: Sequence[str] = ...,
        UserGroups: Sequence[str] = ...,
        ProductCodes: Sequence[str] = ...,
        LoadPermission: LoadPermissionModificationsTypeDef = ...,
        Description: str = ...,
        Name: str = ...
    ) -> ModifyFpgaImageAttributeResultTypeDef:
        """
        Modifies the specified attribute of the specified Amazon FPGA Image (AFI).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_fpga_image_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_fpga_image_attribute)
        """

    def modify_hosts(
        self,
        *,
        HostIds: Sequence[str],
        AutoPlacement: AutoPlacementType = ...,
        HostRecovery: HostRecoveryType = ...,
        InstanceType: str = ...,
        InstanceFamily: str = ...,
        HostMaintenance: HostMaintenanceType = ...
    ) -> ModifyHostsResultTypeDef:
        """
        Modify the auto-placement setting of a Dedicated Host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_hosts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_hosts)
        """

    def modify_id_format(self, *, Resource: str, UseLongIds: bool) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the ID format for the specified resource on a per-Region basis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_id_format)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_id_format)
        """

    def modify_identity_id_format(
        self, *, PrincipalArn: str, Resource: str, UseLongIds: bool
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the ID format of a resource for a specified IAM user, IAM role, or the
        root user for an account; or all IAM users, IAM roles, and the root user for an
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_identity_id_format)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_identity_id_format)
        """

    def modify_image_attribute(
        self,
        *,
        ImageId: str,
        Attribute: str = ...,
        Description: AttributeValueTypeDef = ...,
        LaunchPermission: LaunchPermissionModificationsTypeDef = ...,
        OperationType: OperationTypeType = ...,
        ProductCodes: Sequence[str] = ...,
        UserGroups: Sequence[str] = ...,
        UserIds: Sequence[str] = ...,
        Value: str = ...,
        DryRun: bool = ...,
        OrganizationArns: Sequence[str] = ...,
        OrganizationalUnitArns: Sequence[str] = ...,
        ImdsSupport: AttributeValueTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the specified attribute of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_image_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_image_attribute)
        """

    def modify_instance_attribute(
        self,
        *,
        InstanceId: str,
        SourceDestCheck: AttributeBooleanValueTypeDef = ...,
        Attribute: InstanceAttributeNameType = ...,
        BlockDeviceMappings: Sequence[InstanceBlockDeviceMappingSpecificationTypeDef] = ...,
        DisableApiTermination: AttributeBooleanValueTypeDef = ...,
        DryRun: bool = ...,
        EbsOptimized: AttributeBooleanValueTypeDef = ...,
        EnaSupport: AttributeBooleanValueTypeDef = ...,
        Groups: Sequence[str] = ...,
        InstanceInitiatedShutdownBehavior: AttributeValueTypeDef = ...,
        InstanceType: AttributeValueTypeDef = ...,
        Kernel: AttributeValueTypeDef = ...,
        Ramdisk: AttributeValueTypeDef = ...,
        SriovNetSupport: AttributeValueTypeDef = ...,
        UserData: BlobAttributeValueTypeDef = ...,
        Value: str = ...,
        DisableApiStop: AttributeBooleanValueTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the specified attribute of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_attribute)
        """

    def modify_instance_capacity_reservation_attributes(
        self,
        *,
        InstanceId: str,
        CapacityReservationSpecification: CapacityReservationSpecificationTypeDef,
        DryRun: bool = ...
    ) -> ModifyInstanceCapacityReservationAttributesResultTypeDef:
        """
        Modifies the Capacity Reservation settings for a stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_capacity_reservation_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_capacity_reservation_attributes)
        """

    def modify_instance_credit_specification(
        self,
        *,
        InstanceCreditSpecifications: Sequence[InstanceCreditSpecificationRequestTypeDef],
        DryRun: bool = ...,
        ClientToken: str = ...
    ) -> ModifyInstanceCreditSpecificationResultTypeDef:
        """
        Modifies the credit option for CPU usage on a running or stopped burstable
        performance
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_credit_specification)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_credit_specification)
        """

    def modify_instance_event_start_time(
        self,
        *,
        InstanceId: str,
        InstanceEventId: str,
        NotBefore: TimestampTypeDef,
        DryRun: bool = ...
    ) -> ModifyInstanceEventStartTimeResultTypeDef:
        """
        Modifies the start time for a scheduled Amazon EC2 instance event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_event_start_time)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_event_start_time)
        """

    def modify_instance_event_window(
        self,
        *,
        InstanceEventWindowId: str,
        DryRun: bool = ...,
        Name: str = ...,
        TimeRanges: Sequence[InstanceEventWindowTimeRangeRequestTypeDef] = ...,
        CronExpression: str = ...
    ) -> ModifyInstanceEventWindowResultTypeDef:
        """
        Modifies the specified event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_event_window)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_event_window)
        """

    def modify_instance_maintenance_options(
        self,
        *,
        InstanceId: str,
        AutoRecovery: InstanceAutoRecoveryStateType = ...,
        DryRun: bool = ...
    ) -> ModifyInstanceMaintenanceOptionsResultTypeDef:
        """
        Modifies the recovery behavior of your instance to disable simplified automatic
        recovery or set the recovery behavior to
        default.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_maintenance_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_maintenance_options)
        """

    def modify_instance_metadata_options(
        self,
        *,
        InstanceId: str,
        HttpTokens: HttpTokensStateType = ...,
        HttpPutResponseHopLimit: int = ...,
        HttpEndpoint: InstanceMetadataEndpointStateType = ...,
        DryRun: bool = ...,
        HttpProtocolIpv6: InstanceMetadataProtocolStateType = ...,
        InstanceMetadataTags: InstanceMetadataTagsStateType = ...
    ) -> ModifyInstanceMetadataOptionsResultTypeDef:
        """
        Modify the instance metadata parameters on a running or stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_metadata_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_metadata_options)
        """

    def modify_instance_placement(
        self,
        *,
        InstanceId: str,
        Affinity: AffinityType = ...,
        GroupName: str = ...,
        HostId: str = ...,
        Tenancy: HostTenancyType = ...,
        PartitionNumber: int = ...,
        HostResourceGroupArn: str = ...,
        GroupId: str = ...
    ) -> ModifyInstancePlacementResultTypeDef:
        """
        Modifies the placement attributes for a specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_instance_placement)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_placement)
        """

    def modify_ipam(
        self,
        *,
        IpamId: str,
        DryRun: bool = ...,
        Description: str = ...,
        AddOperatingRegions: Sequence[AddIpamOperatingRegionTypeDef] = ...,
        RemoveOperatingRegions: Sequence[RemoveIpamOperatingRegionTypeDef] = ...,
        Tier: IpamTierType = ...
    ) -> ModifyIpamResultTypeDef:
        """
        Modify the configurations of an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_ipam)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ipam)
        """

    def modify_ipam_pool(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = ...,
        Description: str = ...,
        AutoImport: bool = ...,
        AllocationMinNetmaskLength: int = ...,
        AllocationMaxNetmaskLength: int = ...,
        AllocationDefaultNetmaskLength: int = ...,
        ClearAllocationDefaultNetmaskLength: bool = ...,
        AddAllocationResourceTags: Sequence[RequestIpamResourceTagTypeDef] = ...,
        RemoveAllocationResourceTags: Sequence[RequestIpamResourceTagTypeDef] = ...
    ) -> ModifyIpamPoolResultTypeDef:
        """
        Modify the configurations of an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_ipam_pool)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ipam_pool)
        """

    def modify_ipam_resource_cidr(
        self,
        *,
        ResourceId: str,
        ResourceCidr: str,
        ResourceRegion: str,
        CurrentIpamScopeId: str,
        Monitored: bool,
        DryRun: bool = ...,
        DestinationIpamScopeId: str = ...
    ) -> ModifyIpamResourceCidrResultTypeDef:
        """
        Modify a resource CIDR.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_ipam_resource_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ipam_resource_cidr)
        """

    def modify_ipam_resource_discovery(
        self,
        *,
        IpamResourceDiscoveryId: str,
        DryRun: bool = ...,
        Description: str = ...,
        AddOperatingRegions: Sequence[AddIpamOperatingRegionTypeDef] = ...,
        RemoveOperatingRegions: Sequence[RemoveIpamOperatingRegionTypeDef] = ...
    ) -> ModifyIpamResourceDiscoveryResultTypeDef:
        """
        Modifies a resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_ipam_resource_discovery)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ipam_resource_discovery)
        """

    def modify_ipam_scope(
        self, *, IpamScopeId: str, DryRun: bool = ..., Description: str = ...
    ) -> ModifyIpamScopeResultTypeDef:
        """
        Modify an IPAM scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_ipam_scope)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ipam_scope)
        """

    def modify_launch_template(
        self,
        *,
        DryRun: bool = ...,
        ClientToken: str = ...,
        LaunchTemplateId: str = ...,
        LaunchTemplateName: str = ...,
        DefaultVersion: str = ...
    ) -> ModifyLaunchTemplateResultTypeDef:
        """
        Modifies a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_launch_template)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_launch_template)
        """

    def modify_local_gateway_route(
        self,
        *,
        LocalGatewayRouteTableId: str,
        DestinationCidrBlock: str = ...,
        LocalGatewayVirtualInterfaceGroupId: str = ...,
        NetworkInterfaceId: str = ...,
        DryRun: bool = ...,
        DestinationPrefixListId: str = ...
    ) -> ModifyLocalGatewayRouteResultTypeDef:
        """
        Modifies the specified local gateway route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_local_gateway_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_local_gateway_route)
        """

    def modify_managed_prefix_list(
        self,
        *,
        PrefixListId: str,
        DryRun: bool = ...,
        CurrentVersion: int = ...,
        PrefixListName: str = ...,
        AddEntries: Sequence[AddPrefixListEntryTypeDef] = ...,
        RemoveEntries: Sequence[RemovePrefixListEntryTypeDef] = ...,
        MaxEntries: int = ...
    ) -> ModifyManagedPrefixListResultTypeDef:
        """
        Modifies the specified managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_managed_prefix_list)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_managed_prefix_list)
        """

    def modify_network_interface_attribute(
        self,
        *,
        NetworkInterfaceId: str,
        Attachment: NetworkInterfaceAttachmentChangesTypeDef = ...,
        Description: AttributeValueTypeDef = ...,
        DryRun: bool = ...,
        Groups: Sequence[str] = ...,
        SourceDestCheck: AttributeBooleanValueTypeDef = ...,
        EnaSrdSpecification: EnaSrdSpecificationTypeDef = ...,
        EnablePrimaryIpv6: bool = ...,
        ConnectionTrackingSpecification: ConnectionTrackingSpecificationRequestTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the specified network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_network_interface_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_network_interface_attribute)
        """

    def modify_private_dns_name_options(
        self,
        *,
        InstanceId: str,
        DryRun: bool = ...,
        PrivateDnsHostnameType: HostnameTypeType = ...,
        EnableResourceNameDnsARecord: bool = ...,
        EnableResourceNameDnsAAAARecord: bool = ...
    ) -> ModifyPrivateDnsNameOptionsResultTypeDef:
        """
        Modifies the options for instance hostnames for the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_private_dns_name_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_private_dns_name_options)
        """

    def modify_reserved_instances(
        self,
        *,
        ReservedInstancesIds: Sequence[str],
        TargetConfigurations: Sequence[ReservedInstancesConfigurationTypeDef],
        ClientToken: str = ...
    ) -> ModifyReservedInstancesResultTypeDef:
        """
        Modifies the configuration of your Reserved Instances, such as the Availability
        Zone, instance count, or instance
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_reserved_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_reserved_instances)
        """

    def modify_security_group_rules(
        self,
        *,
        GroupId: str,
        SecurityGroupRules: Sequence[SecurityGroupRuleUpdateTypeDef],
        DryRun: bool = ...
    ) -> ModifySecurityGroupRulesResultTypeDef:
        """
        Modifies the rules of a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_security_group_rules)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_security_group_rules)
        """

    def modify_snapshot_attribute(
        self,
        *,
        SnapshotId: str,
        Attribute: SnapshotAttributeNameType = ...,
        CreateVolumePermission: CreateVolumePermissionModificationsTypeDef = ...,
        GroupNames: Sequence[str] = ...,
        OperationType: OperationTypeType = ...,
        UserIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or removes permission settings for the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_snapshot_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_snapshot_attribute)
        """

    def modify_snapshot_tier(
        self, *, SnapshotId: str, StorageTier: Literal["archive"] = ..., DryRun: bool = ...
    ) -> ModifySnapshotTierResultTypeDef:
        """
        Archives an Amazon EBS snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_snapshot_tier)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_snapshot_tier)
        """

    def modify_spot_fleet_request(
        self,
        *,
        SpotFleetRequestId: str,
        ExcessCapacityTerminationPolicy: ExcessCapacityTerminationPolicyType = ...,
        LaunchTemplateConfigs: Sequence[LaunchTemplateConfigTypeDef] = ...,
        TargetCapacity: int = ...,
        OnDemandTargetCapacity: int = ...,
        Context: str = ...
    ) -> ModifySpotFleetRequestResponseTypeDef:
        """
        Modifies the specified Spot Fleet request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_spot_fleet_request)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_spot_fleet_request)
        """

    def modify_subnet_attribute(
        self,
        *,
        SubnetId: str,
        AssignIpv6AddressOnCreation: AttributeBooleanValueTypeDef = ...,
        MapPublicIpOnLaunch: AttributeBooleanValueTypeDef = ...,
        MapCustomerOwnedIpOnLaunch: AttributeBooleanValueTypeDef = ...,
        CustomerOwnedIpv4Pool: str = ...,
        EnableDns64: AttributeBooleanValueTypeDef = ...,
        PrivateDnsHostnameTypeOnLaunch: HostnameTypeType = ...,
        EnableResourceNameDnsARecordOnLaunch: AttributeBooleanValueTypeDef = ...,
        EnableResourceNameDnsAAAARecordOnLaunch: AttributeBooleanValueTypeDef = ...,
        EnableLniAtDeviceIndex: int = ...,
        DisableLniAtDeviceIndex: AttributeBooleanValueTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies a subnet attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_subnet_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_subnet_attribute)
        """

    def modify_traffic_mirror_filter_network_services(
        self,
        *,
        TrafficMirrorFilterId: str,
        AddNetworkServices: Sequence[Literal["amazon-dns"]] = ...,
        RemoveNetworkServices: Sequence[Literal["amazon-dns"]] = ...,
        DryRun: bool = ...
    ) -> ModifyTrafficMirrorFilterNetworkServicesResultTypeDef:
        """
        Allows or restricts mirroring network services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_network_services)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_traffic_mirror_filter_network_services)
        """

    def modify_traffic_mirror_filter_rule(
        self,
        *,
        TrafficMirrorFilterRuleId: str,
        TrafficDirection: TrafficDirectionType = ...,
        RuleNumber: int = ...,
        RuleAction: TrafficMirrorRuleActionType = ...,
        DestinationPortRange: TrafficMirrorPortRangeRequestTypeDef = ...,
        SourcePortRange: TrafficMirrorPortRangeRequestTypeDef = ...,
        Protocol: int = ...,
        DestinationCidrBlock: str = ...,
        SourceCidrBlock: str = ...,
        Description: str = ...,
        RemoveFields: Sequence[TrafficMirrorFilterRuleFieldType] = ...,
        DryRun: bool = ...
    ) -> ModifyTrafficMirrorFilterRuleResultTypeDef:
        """
        Modifies the specified Traffic Mirror rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_rule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_traffic_mirror_filter_rule)
        """

    def modify_traffic_mirror_session(
        self,
        *,
        TrafficMirrorSessionId: str,
        TrafficMirrorTargetId: str = ...,
        TrafficMirrorFilterId: str = ...,
        PacketLength: int = ...,
        SessionNumber: int = ...,
        VirtualNetworkId: int = ...,
        Description: str = ...,
        RemoveFields: Sequence[TrafficMirrorSessionFieldType] = ...,
        DryRun: bool = ...
    ) -> ModifyTrafficMirrorSessionResultTypeDef:
        """
        Modifies a Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_session)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_traffic_mirror_session)
        """

    def modify_transit_gateway(
        self,
        *,
        TransitGatewayId: str,
        Description: str = ...,
        Options: ModifyTransitGatewayOptionsTypeDef = ...,
        DryRun: bool = ...
    ) -> ModifyTransitGatewayResultTypeDef:
        """
        Modifies the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_transit_gateway)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_transit_gateway)
        """

    def modify_transit_gateway_prefix_list_reference(
        self,
        *,
        TransitGatewayRouteTableId: str,
        PrefixListId: str,
        TransitGatewayAttachmentId: str = ...,
        Blackhole: bool = ...,
        DryRun: bool = ...
    ) -> ModifyTransitGatewayPrefixListReferenceResultTypeDef:
        """
        Modifies a reference (route) to a prefix list in a specified transit gateway
        route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_transit_gateway_prefix_list_reference)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_transit_gateway_prefix_list_reference)
        """

    def modify_transit_gateway_vpc_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        AddSubnetIds: Sequence[str] = ...,
        RemoveSubnetIds: Sequence[str] = ...,
        Options: ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef = ...,
        DryRun: bool = ...
    ) -> ModifyTransitGatewayVpcAttachmentResultTypeDef:
        """
        Modifies the specified VPC attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_transit_gateway_vpc_attachment)
        """

    def modify_verified_access_endpoint(
        self,
        *,
        VerifiedAccessEndpointId: str,
        VerifiedAccessGroupId: str = ...,
        LoadBalancerOptions: ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef = ...,
        NetworkInterfaceOptions: ModifyVerifiedAccessEndpointEniOptionsTypeDef = ...,
        Description: str = ...,
        ClientToken: str = ...,
        DryRun: bool = ...
    ) -> ModifyVerifiedAccessEndpointResultTypeDef:
        """
        Modifies the configuration of the specified Amazon Web Services Verified Access
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_verified_access_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_endpoint)
        """

    def modify_verified_access_endpoint_policy(
        self,
        *,
        VerifiedAccessEndpointId: str,
        PolicyEnabled: bool = ...,
        PolicyDocument: str = ...,
        ClientToken: str = ...,
        DryRun: bool = ...,
        SseSpecification: VerifiedAccessSseSpecificationRequestTypeDef = ...
    ) -> ModifyVerifiedAccessEndpointPolicyResultTypeDef:
        """
        Modifies the specified Amazon Web Services Verified Access endpoint policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_verified_access_endpoint_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_endpoint_policy)
        """

    def modify_verified_access_group(
        self,
        *,
        VerifiedAccessGroupId: str,
        VerifiedAccessInstanceId: str = ...,
        Description: str = ...,
        ClientToken: str = ...,
        DryRun: bool = ...
    ) -> ModifyVerifiedAccessGroupResultTypeDef:
        """
        Modifies the specified Amazon Web Services Verified Access group configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_verified_access_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_group)
        """

    def modify_verified_access_group_policy(
        self,
        *,
        VerifiedAccessGroupId: str,
        PolicyEnabled: bool = ...,
        PolicyDocument: str = ...,
        ClientToken: str = ...,
        DryRun: bool = ...,
        SseSpecification: VerifiedAccessSseSpecificationRequestTypeDef = ...
    ) -> ModifyVerifiedAccessGroupPolicyResultTypeDef:
        """
        Modifies the specified Amazon Web Services Verified Access group policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_verified_access_group_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_group_policy)
        """

    def modify_verified_access_instance(
        self,
        *,
        VerifiedAccessInstanceId: str,
        Description: str = ...,
        DryRun: bool = ...,
        ClientToken: str = ...
    ) -> ModifyVerifiedAccessInstanceResultTypeDef:
        """
        Modifies the configuration of the specified Amazon Web Services Verified Access
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_verified_access_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_instance)
        """

    def modify_verified_access_instance_logging_configuration(
        self,
        *,
        VerifiedAccessInstanceId: str,
        AccessLogs: VerifiedAccessLogOptionsTypeDef,
        DryRun: bool = ...,
        ClientToken: str = ...
    ) -> ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef:
        """
        Modifies the logging configuration for the specified Amazon Web Services
        Verified Access
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_verified_access_instance_logging_configuration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_instance_logging_configuration)
        """

    def modify_verified_access_trust_provider(
        self,
        *,
        VerifiedAccessTrustProviderId: str,
        OidcOptions: ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef = ...,
        DeviceOptions: ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef = ...,
        Description: str = ...,
        DryRun: bool = ...,
        ClientToken: str = ...,
        SseSpecification: VerifiedAccessSseSpecificationRequestTypeDef = ...
    ) -> ModifyVerifiedAccessTrustProviderResultTypeDef:
        """
        Modifies the configuration of the specified Amazon Web Services Verified Access
        trust
        provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_verified_access_trust_provider)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_trust_provider)
        """

    def modify_volume(
        self,
        *,
        VolumeId: str,
        DryRun: bool = ...,
        Size: int = ...,
        VolumeType: VolumeTypeType = ...,
        Iops: int = ...,
        Throughput: int = ...,
        MultiAttachEnabled: bool = ...
    ) -> ModifyVolumeResultTypeDef:
        """
        You can modify several parameters of an existing EBS volume, including volume
        size, volume type, and IOPS
        capacity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_volume)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_volume)
        """

    def modify_volume_attribute(
        self, *, VolumeId: str, AutoEnableIO: AttributeBooleanValueTypeDef = ..., DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies a volume attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_volume_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_volume_attribute)
        """

    def modify_vpc_attribute(
        self,
        *,
        VpcId: str,
        EnableDnsHostnames: AttributeBooleanValueTypeDef = ...,
        EnableDnsSupport: AttributeBooleanValueTypeDef = ...,
        EnableNetworkAddressUsageMetrics: AttributeBooleanValueTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the specified attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_attribute)
        """

    def modify_vpc_endpoint(
        self,
        *,
        VpcEndpointId: str,
        DryRun: bool = ...,
        ResetPolicy: bool = ...,
        PolicyDocument: str = ...,
        AddRouteTableIds: Sequence[str] = ...,
        RemoveRouteTableIds: Sequence[str] = ...,
        AddSubnetIds: Sequence[str] = ...,
        RemoveSubnetIds: Sequence[str] = ...,
        AddSecurityGroupIds: Sequence[str] = ...,
        RemoveSecurityGroupIds: Sequence[str] = ...,
        IpAddressType: IpAddressTypeType = ...,
        DnsOptions: DnsOptionsSpecificationTypeDef = ...,
        PrivateDnsEnabled: bool = ...,
        SubnetConfigurations: Sequence[SubnetConfigurationTypeDef] = ...
    ) -> ModifyVpcEndpointResultTypeDef:
        """
        Modifies attributes of a specified VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_endpoint)
        """

    def modify_vpc_endpoint_connection_notification(
        self,
        *,
        ConnectionNotificationId: str,
        DryRun: bool = ...,
        ConnectionNotificationArn: str = ...,
        ConnectionEvents: Sequence[str] = ...
    ) -> ModifyVpcEndpointConnectionNotificationResultTypeDef:
        """
        Modifies a connection notification for VPC endpoint or VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_connection_notification)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_endpoint_connection_notification)
        """

    def modify_vpc_endpoint_service_configuration(
        self,
        *,
        ServiceId: str,
        DryRun: bool = ...,
        PrivateDnsName: str = ...,
        RemovePrivateDnsName: bool = ...,
        AcceptanceRequired: bool = ...,
        AddNetworkLoadBalancerArns: Sequence[str] = ...,
        RemoveNetworkLoadBalancerArns: Sequence[str] = ...,
        AddGatewayLoadBalancerArns: Sequence[str] = ...,
        RemoveGatewayLoadBalancerArns: Sequence[str] = ...,
        AddSupportedIpAddressTypes: Sequence[str] = ...,
        RemoveSupportedIpAddressTypes: Sequence[str] = ...
    ) -> ModifyVpcEndpointServiceConfigurationResultTypeDef:
        """
        Modifies the attributes of your VPC endpoint service configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_configuration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_endpoint_service_configuration)
        """

    def modify_vpc_endpoint_service_payer_responsibility(
        self, *, ServiceId: str, PayerResponsibility: Literal["ServiceOwner"], DryRun: bool = ...
    ) -> ModifyVpcEndpointServicePayerResponsibilityResultTypeDef:
        """
        Modifies the payer responsibility for your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_payer_responsibility)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_endpoint_service_payer_responsibility)
        """

    def modify_vpc_endpoint_service_permissions(
        self,
        *,
        ServiceId: str,
        DryRun: bool = ...,
        AddAllowedPrincipals: Sequence[str] = ...,
        RemoveAllowedPrincipals: Sequence[str] = ...
    ) -> ModifyVpcEndpointServicePermissionsResultTypeDef:
        """
        Modifies the permissions for your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_permissions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_endpoint_service_permissions)
        """

    def modify_vpc_peering_connection_options(
        self,
        *,
        VpcPeeringConnectionId: str,
        AccepterPeeringConnectionOptions: PeeringConnectionOptionsRequestTypeDef = ...,
        DryRun: bool = ...,
        RequesterPeeringConnectionOptions: PeeringConnectionOptionsRequestTypeDef = ...
    ) -> ModifyVpcPeeringConnectionOptionsResultTypeDef:
        """
        Modifies the VPC peering connection options on one side of a VPC peering
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_peering_connection_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_peering_connection_options)
        """

    def modify_vpc_tenancy(
        self, *, VpcId: str, InstanceTenancy: Literal["default"], DryRun: bool = ...
    ) -> ModifyVpcTenancyResultTypeDef:
        """
        Modifies the instance tenancy attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpc_tenancy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_tenancy)
        """

    def modify_vpn_connection(
        self,
        *,
        VpnConnectionId: str,
        TransitGatewayId: str = ...,
        CustomerGatewayId: str = ...,
        VpnGatewayId: str = ...,
        DryRun: bool = ...
    ) -> ModifyVpnConnectionResultTypeDef:
        """
        Modifies the customer gateway or the target gateway of an Amazon Web Services
        Site-to-Site VPN
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpn_connection)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpn_connection)
        """

    def modify_vpn_connection_options(
        self,
        *,
        VpnConnectionId: str,
        LocalIpv4NetworkCidr: str = ...,
        RemoteIpv4NetworkCidr: str = ...,
        LocalIpv6NetworkCidr: str = ...,
        RemoteIpv6NetworkCidr: str = ...,
        DryRun: bool = ...
    ) -> ModifyVpnConnectionOptionsResultTypeDef:
        """
        Modifies the connection options for your Site-to-Site VPN connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpn_connection_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpn_connection_options)
        """

    def modify_vpn_tunnel_certificate(
        self, *, VpnConnectionId: str, VpnTunnelOutsideIpAddress: str, DryRun: bool = ...
    ) -> ModifyVpnTunnelCertificateResultTypeDef:
        """
        Modifies the VPN tunnel endpoint certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_certificate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpn_tunnel_certificate)
        """

    def modify_vpn_tunnel_options(
        self,
        *,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        TunnelOptions: ModifyVpnTunnelOptionsSpecificationTypeDef,
        DryRun: bool = ...,
        SkipTunnelReplacement: bool = ...
    ) -> ModifyVpnTunnelOptionsResultTypeDef:
        """
        Modifies the options for a VPN tunnel in an Amazon Web Services Site-to-Site
        VPN
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_options)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpn_tunnel_options)
        """

    def monitor_instances(
        self, *, InstanceIds: Sequence[str], DryRun: bool = ...
    ) -> MonitorInstancesResultTypeDef:
        """
        Enables detailed monitoring for a running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.monitor_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#monitor_instances)
        """

    def move_address_to_vpc(
        self, *, PublicIp: str, DryRun: bool = ...
    ) -> MoveAddressToVpcResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.move_address_to_vpc)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#move_address_to_vpc)
        """

    def move_byoip_cidr_to_ipam(
        self, *, Cidr: str, IpamPoolId: str, IpamPoolOwner: str, DryRun: bool = ...
    ) -> MoveByoipCidrToIpamResultTypeDef:
        """
        Move a BYOIPv4 CIDR to IPAM from a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.move_byoip_cidr_to_ipam)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#move_byoip_cidr_to_ipam)
        """

    def provision_byoip_cidr(
        self,
        *,
        Cidr: str,
        CidrAuthorizationContext: CidrAuthorizationContextTypeDef = ...,
        PubliclyAdvertisable: bool = ...,
        Description: str = ...,
        DryRun: bool = ...,
        PoolTagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        MultiRegion: bool = ...,
        NetworkBorderGroup: str = ...
    ) -> ProvisionByoipCidrResultTypeDef:
        """
        Provisions an IPv4 or IPv6 address range for use with your Amazon Web Services
        resources through bring your own IP addresses (BYOIP) and creates a
        corresponding address
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.provision_byoip_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#provision_byoip_cidr)
        """

    def provision_ipam_byoasn(
        self,
        *,
        IpamId: str,
        Asn: str,
        AsnAuthorizationContext: AsnAuthorizationContextTypeDef,
        DryRun: bool = ...
    ) -> ProvisionIpamByoasnResultTypeDef:
        """
        Provisions your Autonomous System Number (ASN) for use in your Amazon Web
        Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.provision_ipam_byoasn)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#provision_ipam_byoasn)
        """

    def provision_ipam_pool_cidr(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = ...,
        Cidr: str = ...,
        CidrAuthorizationContext: IpamCidrAuthorizationContextTypeDef = ...,
        NetmaskLength: int = ...,
        ClientToken: str = ...
    ) -> ProvisionIpamPoolCidrResultTypeDef:
        """
        Provision a CIDR to an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.provision_ipam_pool_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#provision_ipam_pool_cidr)
        """

    def provision_public_ipv4_pool_cidr(
        self, *, IpamPoolId: str, PoolId: str, NetmaskLength: int, DryRun: bool = ...
    ) -> ProvisionPublicIpv4PoolCidrResultTypeDef:
        """
        Provision a CIDR to a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.provision_public_ipv4_pool_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#provision_public_ipv4_pool_cidr)
        """

    def purchase_capacity_block(
        self,
        *,
        CapacityBlockOfferingId: str,
        InstancePlatform: CapacityReservationInstancePlatformType,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> PurchaseCapacityBlockResultTypeDef:
        """
        Purchase the Capacity Block for use with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.purchase_capacity_block)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#purchase_capacity_block)
        """

    def purchase_host_reservation(
        self,
        *,
        HostIdSet: Sequence[str],
        OfferingId: str,
        ClientToken: str = ...,
        CurrencyCode: Literal["USD"] = ...,
        LimitPrice: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> PurchaseHostReservationResultTypeDef:
        """
        Purchase a reservation with configurations that match those of your Dedicated
        Host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.purchase_host_reservation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#purchase_host_reservation)
        """

    def purchase_reserved_instances_offering(
        self,
        *,
        InstanceCount: int,
        ReservedInstancesOfferingId: str,
        DryRun: bool = ...,
        LimitPrice: ReservedInstanceLimitPriceTypeDef = ...,
        PurchaseTime: TimestampTypeDef = ...
    ) -> PurchaseReservedInstancesOfferingResultTypeDef:
        """
        Purchases a Reserved Instance for use with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.purchase_reserved_instances_offering)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#purchase_reserved_instances_offering)
        """

    def purchase_scheduled_instances(
        self,
        *,
        PurchaseRequests: Sequence[PurchaseRequestTypeDef],
        ClientToken: str = ...,
        DryRun: bool = ...
    ) -> PurchaseScheduledInstancesResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.purchase_scheduled_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#purchase_scheduled_instances)
        """

    def reboot_instances(
        self, *, InstanceIds: Sequence[str], DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Requests a reboot of the specified instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reboot_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reboot_instances)
        """

    def register_image(
        self,
        *,
        Name: str,
        ImageLocation: str = ...,
        Architecture: ArchitectureValuesType = ...,
        BlockDeviceMappings: Sequence[BlockDeviceMappingTypeDef] = ...,
        Description: str = ...,
        DryRun: bool = ...,
        EnaSupport: bool = ...,
        KernelId: str = ...,
        BillingProducts: Sequence[str] = ...,
        RamdiskId: str = ...,
        RootDeviceName: str = ...,
        SriovNetSupport: str = ...,
        VirtualizationType: str = ...,
        BootMode: BootModeValuesType = ...,
        TpmSupport: Literal["v2.0"] = ...,
        UefiData: str = ...,
        ImdsSupport: Literal["v2.0"] = ...
    ) -> RegisterImageResultTypeDef:
        """
        Registers an AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.register_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#register_image)
        """

    def register_instance_event_notification_attributes(
        self,
        *,
        InstanceTagAttribute: RegisterInstanceTagAttributeRequestTypeDef,
        DryRun: bool = ...
    ) -> RegisterInstanceEventNotificationAttributesResultTypeDef:
        """
        Registers a set of tag keys to include in scheduled event notifications for
        your
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.register_instance_event_notification_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#register_instance_event_notification_attributes)
        """

    def register_transit_gateway_multicast_group_members(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        NetworkInterfaceIds: Sequence[str],
        GroupIpAddress: str = ...,
        DryRun: bool = ...
    ) -> RegisterTransitGatewayMulticastGroupMembersResultTypeDef:
        """
        Registers members (network interfaces) with the transit gateway multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_members)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#register_transit_gateway_multicast_group_members)
        """

    def register_transit_gateway_multicast_group_sources(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        NetworkInterfaceIds: Sequence[str],
        GroupIpAddress: str = ...,
        DryRun: bool = ...
    ) -> RegisterTransitGatewayMulticastGroupSourcesResultTypeDef:
        """
        Registers sources (network interfaces) with the specified transit gateway
        multicast
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_sources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#register_transit_gateway_multicast_group_sources)
        """

    def reject_transit_gateway_multicast_domain_associations(
        self,
        *,
        TransitGatewayMulticastDomainId: str = ...,
        TransitGatewayAttachmentId: str = ...,
        SubnetIds: Sequence[str] = ...,
        DryRun: bool = ...
    ) -> RejectTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        Rejects a request to associate cross-account subnets with a transit gateway
        multicast
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reject_transit_gateway_multicast_domain_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reject_transit_gateway_multicast_domain_associations)
        """

    def reject_transit_gateway_peering_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = ...
    ) -> RejectTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Rejects a transit gateway peering attachment request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reject_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reject_transit_gateway_peering_attachment)
        """

    def reject_transit_gateway_vpc_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = ...
    ) -> RejectTransitGatewayVpcAttachmentResultTypeDef:
        """
        Rejects a request to attach a VPC to a transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reject_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reject_transit_gateway_vpc_attachment)
        """

    def reject_vpc_endpoint_connections(
        self, *, ServiceId: str, VpcEndpointIds: Sequence[str], DryRun: bool = ...
    ) -> RejectVpcEndpointConnectionsResultTypeDef:
        """
        Rejects VPC endpoint connection requests to your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reject_vpc_endpoint_connections)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reject_vpc_endpoint_connections)
        """

    def reject_vpc_peering_connection(
        self, *, VpcPeeringConnectionId: str, DryRun: bool = ...
    ) -> RejectVpcPeeringConnectionResultTypeDef:
        """
        Rejects a VPC peering connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reject_vpc_peering_connection)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reject_vpc_peering_connection)
        """

    def release_address(
        self,
        *,
        AllocationId: str = ...,
        PublicIp: str = ...,
        NetworkBorderGroup: str = ...,
        DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Releases the specified Elastic IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.release_address)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#release_address)
        """

    def release_hosts(self, *, HostIds: Sequence[str]) -> ReleaseHostsResultTypeDef:
        """
        When you no longer want to use an On-Demand Dedicated Host it can be released.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.release_hosts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#release_hosts)
        """

    def release_ipam_pool_allocation(
        self, *, IpamPoolId: str, Cidr: str, IpamPoolAllocationId: str, DryRun: bool = ...
    ) -> ReleaseIpamPoolAllocationResultTypeDef:
        """
        Release an allocation within an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.release_ipam_pool_allocation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#release_ipam_pool_allocation)
        """

    def replace_iam_instance_profile_association(
        self, *, IamInstanceProfile: IamInstanceProfileSpecificationTypeDef, AssociationId: str
    ) -> ReplaceIamInstanceProfileAssociationResultTypeDef:
        """
        Replaces an IAM instance profile for the specified running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_iam_instance_profile_association)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_iam_instance_profile_association)
        """

    def replace_network_acl_association(
        self, *, AssociationId: str, NetworkAclId: str, DryRun: bool = ...
    ) -> ReplaceNetworkAclAssociationResultTypeDef:
        """
        Changes which network ACL a subnet is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_network_acl_association)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_network_acl_association)
        """

    def replace_network_acl_entry(
        self,
        *,
        Egress: bool,
        NetworkAclId: str,
        Protocol: str,
        RuleAction: RuleActionType,
        RuleNumber: int,
        CidrBlock: str = ...,
        DryRun: bool = ...,
        IcmpTypeCode: IcmpTypeCodeTypeDef = ...,
        Ipv6CidrBlock: str = ...,
        PortRange: PortRangeTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Replaces an entry (rule) in a network ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_network_acl_entry)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_network_acl_entry)
        """

    def replace_route(
        self,
        *,
        RouteTableId: str,
        DestinationCidrBlock: str = ...,
        DestinationIpv6CidrBlock: str = ...,
        DestinationPrefixListId: str = ...,
        DryRun: bool = ...,
        VpcEndpointId: str = ...,
        EgressOnlyInternetGatewayId: str = ...,
        GatewayId: str = ...,
        InstanceId: str = ...,
        LocalTarget: bool = ...,
        NatGatewayId: str = ...,
        TransitGatewayId: str = ...,
        LocalGatewayId: str = ...,
        CarrierGatewayId: str = ...,
        NetworkInterfaceId: str = ...,
        VpcPeeringConnectionId: str = ...,
        CoreNetworkArn: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Replaces an existing route within a route table in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_route)
        """

    def replace_route_table_association(
        self, *, AssociationId: str, RouteTableId: str, DryRun: bool = ...
    ) -> ReplaceRouteTableAssociationResultTypeDef:
        """
        Changes the route table associated with a given subnet, internet gateway, or
        virtual private gateway in a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_route_table_association)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_route_table_association)
        """

    def replace_transit_gateway_route(
        self,
        *,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = ...,
        Blackhole: bool = ...,
        DryRun: bool = ...
    ) -> ReplaceTransitGatewayRouteResultTypeDef:
        """
        Replaces the specified route in the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_transit_gateway_route)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_transit_gateway_route)
        """

    def replace_vpn_tunnel(
        self,
        *,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        ApplyPendingMaintenance: bool = ...,
        DryRun: bool = ...
    ) -> ReplaceVpnTunnelResultTypeDef:
        """
        Trigger replacement of specified VPN tunnel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.replace_vpn_tunnel)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_vpn_tunnel)
        """

    def report_instance_status(
        self,
        *,
        Instances: Sequence[str],
        ReasonCodes: Sequence[ReportInstanceReasonCodesType],
        Status: ReportStatusTypeType,
        Description: str = ...,
        DryRun: bool = ...,
        EndTime: TimestampTypeDef = ...,
        StartTime: TimestampTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Submits feedback about the status of an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.report_instance_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#report_instance_status)
        """

    def request_spot_fleet(
        self, *, SpotFleetRequestConfig: SpotFleetRequestConfigDataTypeDef, DryRun: bool = ...
    ) -> RequestSpotFleetResponseTypeDef:
        """
        Creates a Spot Fleet request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.request_spot_fleet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#request_spot_fleet)
        """

    def request_spot_instances(
        self,
        *,
        AvailabilityZoneGroup: str = ...,
        BlockDurationMinutes: int = ...,
        ClientToken: str = ...,
        DryRun: bool = ...,
        InstanceCount: int = ...,
        LaunchGroup: str = ...,
        LaunchSpecification: RequestSpotLaunchSpecificationTypeDef = ...,
        SpotPrice: str = ...,
        Type: SpotInstanceTypeType = ...,
        ValidFrom: TimestampTypeDef = ...,
        ValidUntil: TimestampTypeDef = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        InstanceInterruptionBehavior: InstanceInterruptionBehaviorType = ...
    ) -> RequestSpotInstancesResultTypeDef:
        """
        Creates a Spot Instance request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.request_spot_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#request_spot_instances)
        """

    def reset_address_attribute(
        self, *, AllocationId: str, Attribute: Literal["domain-name"], DryRun: bool = ...
    ) -> ResetAddressAttributeResultTypeDef:
        """
        Resets the attribute of the specified IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_address_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_address_attribute)
        """

    def reset_ebs_default_kms_key_id(
        self, *, DryRun: bool = ...
    ) -> ResetEbsDefaultKmsKeyIdResultTypeDef:
        """
        Resets the default KMS key for EBS encryption for your account in this Region
        to the Amazon Web Services managed KMS key for
        EBS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_ebs_default_kms_key_id)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_ebs_default_kms_key_id)
        """

    def reset_fpga_image_attribute(
        self, *, FpgaImageId: str, DryRun: bool = ..., Attribute: Literal["loadPermission"] = ...
    ) -> ResetFpgaImageAttributeResultTypeDef:
        """
        Resets the specified attribute of the specified Amazon FPGA Image (AFI) to its
        default
        value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_fpga_image_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_fpga_image_attribute)
        """

    def reset_image_attribute(
        self, *, Attribute: Literal["launchPermission"], ImageId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Resets an attribute of an AMI to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_image_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_image_attribute)
        """

    def reset_instance_attribute(
        self, *, Attribute: InstanceAttributeNameType, InstanceId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Resets an attribute of an instance to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_instance_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_instance_attribute)
        """

    def reset_network_interface_attribute(
        self, *, NetworkInterfaceId: str, DryRun: bool = ..., SourceDestCheck: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Resets a network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_network_interface_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_network_interface_attribute)
        """

    def reset_snapshot_attribute(
        self, *, Attribute: SnapshotAttributeNameType, SnapshotId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Resets permission settings for the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.reset_snapshot_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_snapshot_attribute)
        """

    def restore_address_to_classic(
        self, *, PublicIp: str, DryRun: bool = ...
    ) -> RestoreAddressToClassicResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.restore_address_to_classic)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#restore_address_to_classic)
        """

    def restore_image_from_recycle_bin(
        self, *, ImageId: str, DryRun: bool = ...
    ) -> RestoreImageFromRecycleBinResultTypeDef:
        """
        Restores an AMI from the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.restore_image_from_recycle_bin)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#restore_image_from_recycle_bin)
        """

    def restore_managed_prefix_list_version(
        self, *, PrefixListId: str, PreviousVersion: int, CurrentVersion: int, DryRun: bool = ...
    ) -> RestoreManagedPrefixListVersionResultTypeDef:
        """
        Restores the entries from a previous version of a managed prefix list to a new
        version of the prefix
        list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.restore_managed_prefix_list_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#restore_managed_prefix_list_version)
        """

    def restore_snapshot_from_recycle_bin(
        self, *, SnapshotId: str, DryRun: bool = ...
    ) -> RestoreSnapshotFromRecycleBinResultTypeDef:
        """
        Restores a snapshot from the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.restore_snapshot_from_recycle_bin)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#restore_snapshot_from_recycle_bin)
        """

    def restore_snapshot_tier(
        self,
        *,
        SnapshotId: str,
        TemporaryRestoreDays: int = ...,
        PermanentRestore: bool = ...,
        DryRun: bool = ...
    ) -> RestoreSnapshotTierResultTypeDef:
        """
        Restores an archived Amazon EBS snapshot for use temporarily or permanently, or
        modifies the restore period or restore type for a snapshot that was previously
        temporarily
        restored.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.restore_snapshot_tier)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#restore_snapshot_tier)
        """

    def revoke_client_vpn_ingress(
        self,
        *,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str = ...,
        RevokeAllGroups: bool = ...,
        DryRun: bool = ...
    ) -> RevokeClientVpnIngressResultTypeDef:
        """
        Removes an ingress authorization rule from a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.revoke_client_vpn_ingress)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#revoke_client_vpn_ingress)
        """

    def revoke_security_group_egress(
        self,
        *,
        GroupId: str,
        DryRun: bool = ...,
        IpPermissions: Sequence[IpPermissionTypeDef] = ...,
        SecurityGroupRuleIds: Sequence[str] = ...,
        CidrIp: str = ...,
        FromPort: int = ...,
        IpProtocol: str = ...,
        ToPort: int = ...,
        SourceSecurityGroupName: str = ...,
        SourceSecurityGroupOwnerId: str = ...
    ) -> RevokeSecurityGroupEgressResultTypeDef:
        """
        Removes the specified outbound (egress) rules from the specified security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.revoke_security_group_egress)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#revoke_security_group_egress)
        """

    def revoke_security_group_ingress(
        self,
        *,
        CidrIp: str = ...,
        FromPort: int = ...,
        GroupId: str = ...,
        GroupName: str = ...,
        IpPermissions: Sequence[IpPermissionTypeDef] = ...,
        IpProtocol: str = ...,
        SourceSecurityGroupName: str = ...,
        SourceSecurityGroupOwnerId: str = ...,
        ToPort: int = ...,
        DryRun: bool = ...,
        SecurityGroupRuleIds: Sequence[str] = ...
    ) -> RevokeSecurityGroupIngressResultTypeDef:
        """
        Removes the specified inbound (ingress) rules from a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.revoke_security_group_ingress)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#revoke_security_group_ingress)
        """

    def run_instances(
        self,
        *,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: Sequence[BlockDeviceMappingTypeDef] = ...,
        ImageId: str = ...,
        InstanceType: InstanceTypeType = ...,
        Ipv6AddressCount: int = ...,
        Ipv6Addresses: Sequence[InstanceIpv6AddressTypeDef] = ...,
        KernelId: str = ...,
        KeyName: str = ...,
        Monitoring: RunInstancesMonitoringEnabledTypeDef = ...,
        Placement: PlacementTypeDef = ...,
        RamdiskId: str = ...,
        SecurityGroupIds: Sequence[str] = ...,
        SecurityGroups: Sequence[str] = ...,
        SubnetId: str = ...,
        UserData: str = ...,
        AdditionalInfo: str = ...,
        ClientToken: str = ...,
        DisableApiTermination: bool = ...,
        DryRun: bool = ...,
        EbsOptimized: bool = ...,
        IamInstanceProfile: IamInstanceProfileSpecificationTypeDef = ...,
        InstanceInitiatedShutdownBehavior: ShutdownBehaviorType = ...,
        NetworkInterfaces: Sequence[InstanceNetworkInterfaceSpecificationTypeDef] = ...,
        PrivateIpAddress: str = ...,
        ElasticGpuSpecification: Sequence[ElasticGpuSpecificationTypeDef] = ...,
        ElasticInferenceAccelerators: Sequence[ElasticInferenceAcceleratorTypeDef] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        LaunchTemplate: LaunchTemplateSpecificationTypeDef = ...,
        InstanceMarketOptions: InstanceMarketOptionsRequestTypeDef = ...,
        CreditSpecification: CreditSpecificationRequestTypeDef = ...,
        CpuOptions: CpuOptionsRequestTypeDef = ...,
        CapacityReservationSpecification: CapacityReservationSpecificationTypeDef = ...,
        HibernationOptions: HibernationOptionsRequestTypeDef = ...,
        LicenseSpecifications: Sequence[LicenseConfigurationRequestTypeDef] = ...,
        MetadataOptions: InstanceMetadataOptionsRequestTypeDef = ...,
        EnclaveOptions: EnclaveOptionsRequestTypeDef = ...,
        PrivateDnsNameOptions: PrivateDnsNameOptionsRequestTypeDef = ...,
        MaintenanceOptions: InstanceMaintenanceOptionsRequestTypeDef = ...,
        DisableApiStop: bool = ...,
        EnablePrimaryIpv6: bool = ...
    ) -> ReservationResponseTypeDef:
        """
        Launches the specified number of instances using an AMI for which you have
        permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.run_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#run_instances)
        """

    def run_scheduled_instances(
        self,
        *,
        LaunchSpecification: ScheduledInstancesLaunchSpecificationTypeDef,
        ScheduledInstanceId: str,
        ClientToken: str = ...,
        DryRun: bool = ...,
        InstanceCount: int = ...
    ) -> RunScheduledInstancesResultTypeDef:
        """
        Launches the specified Scheduled Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.run_scheduled_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#run_scheduled_instances)
        """

    def search_local_gateway_routes(
        self,
        *,
        LocalGatewayRouteTableId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> SearchLocalGatewayRoutesResultTypeDef:
        """
        Searches for routes in the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.search_local_gateway_routes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#search_local_gateway_routes)
        """

    def search_transit_gateway_multicast_groups(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...
    ) -> SearchTransitGatewayMulticastGroupsResultTypeDef:
        """
        Searches one or more transit gateway multicast groups and returns the group
        membership
        information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.search_transit_gateway_multicast_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#search_transit_gateway_multicast_groups)
        """

    def search_transit_gateway_routes(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: Sequence[FilterTypeDef],
        MaxResults: int = ...,
        DryRun: bool = ...
    ) -> SearchTransitGatewayRoutesResultTypeDef:
        """
        Searches for routes in the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.search_transit_gateway_routes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#search_transit_gateway_routes)
        """

    def send_diagnostic_interrupt(
        self, *, InstanceId: str, DryRun: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sends a diagnostic interrupt to the specified Amazon EC2 instance to trigger a
        *kernel panic* (on Linux instances), or a *blue screen*/*stop error* (on
        Windows
        instances).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.send_diagnostic_interrupt)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#send_diagnostic_interrupt)
        """

    def start_instances(
        self, *, InstanceIds: Sequence[str], AdditionalInfo: str = ..., DryRun: bool = ...
    ) -> StartInstancesResultTypeDef:
        """
        Starts an Amazon EBS-backed instance that you've previously stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#start_instances)
        """

    def start_network_insights_access_scope_analysis(
        self,
        *,
        NetworkInsightsAccessScopeId: str,
        ClientToken: str,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> StartNetworkInsightsAccessScopeAnalysisResultTypeDef:
        """
        Starts analyzing the specified Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_network_insights_access_scope_analysis)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#start_network_insights_access_scope_analysis)
        """

    def start_network_insights_analysis(
        self,
        *,
        NetworkInsightsPathId: str,
        ClientToken: str,
        AdditionalAccounts: Sequence[str] = ...,
        FilterInArns: Sequence[str] = ...,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...
    ) -> StartNetworkInsightsAnalysisResultTypeDef:
        """
        Starts analyzing the specified path.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_network_insights_analysis)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#start_network_insights_analysis)
        """

    def start_vpc_endpoint_service_private_dns_verification(
        self, *, ServiceId: str, DryRun: bool = ...
    ) -> StartVpcEndpointServicePrivateDnsVerificationResultTypeDef:
        """
        Initiates the verification process to prove that the service provider owns the
        private DNS name domain for the endpoint
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_vpc_endpoint_service_private_dns_verification)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#start_vpc_endpoint_service_private_dns_verification)
        """

    def stop_instances(
        self,
        *,
        InstanceIds: Sequence[str],
        Hibernate: bool = ...,
        DryRun: bool = ...,
        Force: bool = ...
    ) -> StopInstancesResultTypeDef:
        """
        Stops an Amazon EBS-backed instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.stop_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#stop_instances)
        """

    def terminate_client_vpn_connections(
        self,
        *,
        ClientVpnEndpointId: str,
        ConnectionId: str = ...,
        Username: str = ...,
        DryRun: bool = ...
    ) -> TerminateClientVpnConnectionsResultTypeDef:
        """
        Terminates active Client VPN endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.terminate_client_vpn_connections)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#terminate_client_vpn_connections)
        """

    def terminate_instances(
        self, *, InstanceIds: Sequence[str], DryRun: bool = ...
    ) -> TerminateInstancesResultTypeDef:
        """
        Shuts down the specified instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.terminate_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#terminate_instances)
        """

    def unassign_ipv6_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        Ipv6Addresses: Sequence[str] = ...,
        Ipv6Prefixes: Sequence[str] = ...
    ) -> UnassignIpv6AddressesResultTypeDef:
        """
        Unassigns one or more IPv6 addresses IPv4 Prefix Delegation prefixes from a
        network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.unassign_ipv6_addresses)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#unassign_ipv6_addresses)
        """

    def unassign_private_ip_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        PrivateIpAddresses: Sequence[str] = ...,
        Ipv4Prefixes: Sequence[str] = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Unassigns one or more secondary private IP addresses, or IPv4 Prefix Delegation
        prefixes from a network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.unassign_private_ip_addresses)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#unassign_private_ip_addresses)
        """

    def unassign_private_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        PrivateIpAddresses: Sequence[str],
        MaxDrainDurationSeconds: int = ...,
        DryRun: bool = ...
    ) -> UnassignPrivateNatGatewayAddressResultTypeDef:
        """
        Unassigns secondary private IPv4 addresses from a private NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.unassign_private_nat_gateway_address)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#unassign_private_nat_gateway_address)
        """

    def unlock_snapshot(
        self, *, SnapshotId: str, DryRun: bool = ...
    ) -> UnlockSnapshotResultTypeDef:
        """
        Unlocks a snapshot that is locked in governance mode or that is locked in
        compliance mode but still in the cooling-off
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.unlock_snapshot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#unlock_snapshot)
        """

    def unmonitor_instances(
        self, *, InstanceIds: Sequence[str], DryRun: bool = ...
    ) -> UnmonitorInstancesResultTypeDef:
        """
        Disables detailed monitoring for a running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.unmonitor_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#unmonitor_instances)
        """

    def update_security_group_rule_descriptions_egress(
        self,
        *,
        DryRun: bool = ...,
        GroupId: str = ...,
        GroupName: str = ...,
        IpPermissions: Sequence[IpPermissionTypeDef] = ...,
        SecurityGroupRuleDescriptions: Sequence[SecurityGroupRuleDescriptionTypeDef] = ...
    ) -> UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef:
        """
        Updates the description of an egress (outbound) security group rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_egress)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#update_security_group_rule_descriptions_egress)
        """

    def update_security_group_rule_descriptions_ingress(
        self,
        *,
        DryRun: bool = ...,
        GroupId: str = ...,
        GroupName: str = ...,
        IpPermissions: Sequence[IpPermissionTypeDef] = ...,
        SecurityGroupRuleDescriptions: Sequence[SecurityGroupRuleDescriptionTypeDef] = ...
    ) -> UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef:
        """
        Updates the description of an ingress (inbound) security group rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_ingress)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#update_security_group_rule_descriptions_ingress)
        """

    def withdraw_byoip_cidr(
        self, *, Cidr: str, DryRun: bool = ...
    ) -> WithdrawByoipCidrResultTypeDef:
        """
        Stops advertising an address range that is provisioned as an address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.withdraw_byoip_cidr)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#withdraw_byoip_cidr)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_address_transfers"]
    ) -> DescribeAddressTransfersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_addresses_attribute"]
    ) -> DescribeAddressesAttributePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_aws_network_performance_metric_subscriptions"]
    ) -> DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_byoip_cidrs"]
    ) -> DescribeByoipCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_capacity_block_offerings"]
    ) -> DescribeCapacityBlockOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_capacity_reservation_fleets"]
    ) -> DescribeCapacityReservationFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_capacity_reservations"]
    ) -> DescribeCapacityReservationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_carrier_gateways"]
    ) -> DescribeCarrierGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_classic_link_instances"]
    ) -> DescribeClassicLinkInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_authorization_rules"]
    ) -> DescribeClientVpnAuthorizationRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_connections"]
    ) -> DescribeClientVpnConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_endpoints"]
    ) -> DescribeClientVpnEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_routes"]
    ) -> DescribeClientVpnRoutesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_target_networks"]
    ) -> DescribeClientVpnTargetNetworksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_coip_pools"]
    ) -> DescribeCoipPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_dhcp_options"]
    ) -> DescribeDhcpOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_egress_only_internet_gateways"]
    ) -> DescribeEgressOnlyInternetGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_image_tasks"]
    ) -> DescribeExportImageTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fast_launch_images"]
    ) -> DescribeFastLaunchImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fast_snapshot_restores"]
    ) -> DescribeFastSnapshotRestoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_fleets"]) -> DescribeFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_flow_logs"]
    ) -> DescribeFlowLogsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fpga_images"]
    ) -> DescribeFpgaImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_host_reservation_offerings"]
    ) -> DescribeHostReservationOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_host_reservations"]
    ) -> DescribeHostReservationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_hosts"]) -> DescribeHostsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_iam_instance_profile_associations"]
    ) -> DescribeIamInstanceProfileAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_images"]) -> DescribeImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_import_image_tasks"]
    ) -> DescribeImportImageTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_import_snapshot_tasks"]
    ) -> DescribeImportSnapshotTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_connect_endpoints"]
    ) -> DescribeInstanceConnectEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_credit_specifications"]
    ) -> DescribeInstanceCreditSpecificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_event_windows"]
    ) -> DescribeInstanceEventWindowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_status"]
    ) -> DescribeInstanceStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_topology"]
    ) -> DescribeInstanceTopologyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_type_offerings"]
    ) -> DescribeInstanceTypeOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_types"]
    ) -> DescribeInstanceTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instances"]
    ) -> DescribeInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_internet_gateways"]
    ) -> DescribeInternetGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipam_pools"]
    ) -> DescribeIpamPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipam_resource_discoveries"]
    ) -> DescribeIpamResourceDiscoveriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipam_resource_discovery_associations"]
    ) -> DescribeIpamResourceDiscoveryAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipam_scopes"]
    ) -> DescribeIpamScopesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_ipams"]) -> DescribeIpamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipv6_pools"]
    ) -> DescribeIpv6PoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_template_versions"]
    ) -> DescribeLaunchTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_templates"]
    ) -> DescribeLaunchTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self,
        operation_name: Literal[
            "describe_local_gateway_route_table_virtual_interface_group_associations"
        ],
    ) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_route_table_vpc_associations"]
    ) -> DescribeLocalGatewayRouteTableVpcAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_route_tables"]
    ) -> DescribeLocalGatewayRouteTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_virtual_interface_groups"]
    ) -> DescribeLocalGatewayVirtualInterfaceGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_virtual_interfaces"]
    ) -> DescribeLocalGatewayVirtualInterfacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateways"]
    ) -> DescribeLocalGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_managed_prefix_lists"]
    ) -> DescribeManagedPrefixListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_moving_addresses"]
    ) -> DescribeMovingAddressesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_nat_gateways"]
    ) -> DescribeNatGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_acls"]
    ) -> DescribeNetworkAclsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_insights_access_scope_analyses"]
    ) -> DescribeNetworkInsightsAccessScopeAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_insights_access_scopes"]
    ) -> DescribeNetworkInsightsAccessScopesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_insights_analyses"]
    ) -> DescribeNetworkInsightsAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_insights_paths"]
    ) -> DescribeNetworkInsightsPathsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_interface_permissions"]
    ) -> DescribeNetworkInterfacePermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_interfaces"]
    ) -> DescribeNetworkInterfacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_prefix_lists"]
    ) -> DescribePrefixListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_principal_id_format"]
    ) -> DescribePrincipalIdFormatPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_public_ipv4_pools"]
    ) -> DescribePublicIpv4PoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replace_root_volume_tasks"]
    ) -> DescribeReplaceRootVolumeTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_instances_modifications"]
    ) -> DescribeReservedInstancesModificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_instances_offerings"]
    ) -> DescribeReservedInstancesOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_route_tables"]
    ) -> DescribeRouteTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_instance_availability"]
    ) -> DescribeScheduledInstanceAvailabilityPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_instances"]
    ) -> DescribeScheduledInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_security_group_rules"]
    ) -> DescribeSecurityGroupRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_security_groups"]
    ) -> DescribeSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshot_tier_status"]
    ) -> DescribeSnapshotTierStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_fleet_instances"]
    ) -> DescribeSpotFleetInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_fleet_requests"]
    ) -> DescribeSpotFleetRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_instance_requests"]
    ) -> DescribeSpotInstanceRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_price_history"]
    ) -> DescribeSpotPriceHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_stale_security_groups"]
    ) -> DescribeStaleSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_store_image_tasks"]
    ) -> DescribeStoreImageTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subnets"]
    ) -> DescribeSubnetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_filters"]
    ) -> DescribeTrafficMirrorFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_sessions"]
    ) -> DescribeTrafficMirrorSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_targets"]
    ) -> DescribeTrafficMirrorTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_attachments"]
    ) -> DescribeTransitGatewayAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_connect_peers"]
    ) -> DescribeTransitGatewayConnectPeersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_connects"]
    ) -> DescribeTransitGatewayConnectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_multicast_domains"]
    ) -> DescribeTransitGatewayMulticastDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_peering_attachments"]
    ) -> DescribeTransitGatewayPeeringAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_policy_tables"]
    ) -> DescribeTransitGatewayPolicyTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_route_table_announcements"]
    ) -> DescribeTransitGatewayRouteTableAnnouncementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_route_tables"]
    ) -> DescribeTransitGatewayRouteTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_vpc_attachments"]
    ) -> DescribeTransitGatewayVpcAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateways"]
    ) -> DescribeTransitGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_trunk_interface_associations"]
    ) -> DescribeTrunkInterfaceAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_access_endpoints"]
    ) -> DescribeVerifiedAccessEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_access_groups"]
    ) -> DescribeVerifiedAccessGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_access_instance_logging_configurations"]
    ) -> DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_access_instances"]
    ) -> DescribeVerifiedAccessInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_access_trust_providers"]
    ) -> DescribeVerifiedAccessTrustProvidersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volume_status"]
    ) -> DescribeVolumeStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volumes"]
    ) -> DescribeVolumesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volumes_modifications"]
    ) -> DescribeVolumesModificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_classic_link_dns_support"]
    ) -> DescribeVpcClassicLinkDnsSupportPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_connection_notifications"]
    ) -> DescribeVpcEndpointConnectionNotificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_connections"]
    ) -> DescribeVpcEndpointConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_service_configurations"]
    ) -> DescribeVpcEndpointServiceConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_service_permissions"]
    ) -> DescribeVpcEndpointServicePermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_services"]
    ) -> DescribeVpcEndpointServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoints"]
    ) -> DescribeVpcEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_peering_connections"]
    ) -> DescribeVpcPeeringConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_vpcs"]) -> DescribeVpcsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_associated_ipv6_pool_cidrs"]
    ) -> GetAssociatedIpv6PoolCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_aws_network_performance_data"]
    ) -> GetAwsNetworkPerformanceDataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_groups_for_capacity_reservation"]
    ) -> GetGroupsForCapacityReservationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_instance_types_from_instance_requirements"]
    ) -> GetInstanceTypesFromInstanceRequirementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_address_history"]
    ) -> GetIpamAddressHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_discovered_accounts"]
    ) -> GetIpamDiscoveredAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_discovered_resource_cidrs"]
    ) -> GetIpamDiscoveredResourceCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_pool_allocations"]
    ) -> GetIpamPoolAllocationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_pool_cidrs"]
    ) -> GetIpamPoolCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_resource_cidrs"]
    ) -> GetIpamResourceCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_managed_prefix_list_associations"]
    ) -> GetManagedPrefixListAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_managed_prefix_list_entries"]
    ) -> GetManagedPrefixListEntriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_network_insights_access_scope_analysis_findings"]
    ) -> GetNetworkInsightsAccessScopeAnalysisFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_security_groups_for_vpc"]
    ) -> GetSecurityGroupsForVpcPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_spot_placement_scores"]
    ) -> GetSpotPlacementScoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_attachment_propagations"]
    ) -> GetTransitGatewayAttachmentPropagationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_multicast_domain_associations"]
    ) -> GetTransitGatewayMulticastDomainAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_policy_table_associations"]
    ) -> GetTransitGatewayPolicyTableAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_prefix_list_references"]
    ) -> GetTransitGatewayPrefixListReferencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_route_table_associations"]
    ) -> GetTransitGatewayRouteTableAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_route_table_propagations"]
    ) -> GetTransitGatewayRouteTablePropagationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_vpn_connection_device_types"]
    ) -> GetVpnConnectionDeviceTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_images_in_recycle_bin"]
    ) -> ListImagesInRecycleBinPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_snapshots_in_recycle_bin"]
    ) -> ListSnapshotsInRecycleBinPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_local_gateway_routes"]
    ) -> SearchLocalGatewayRoutesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_transit_gateway_multicast_groups"]
    ) -> SearchTransitGatewayMulticastGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bundle_task_complete"]) -> BundleTaskCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_cancelled"]
    ) -> ConversionTaskCancelledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_completed"]
    ) -> ConversionTaskCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_deleted"]
    ) -> ConversionTaskDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["customer_gateway_available"]
    ) -> CustomerGatewayAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["export_task_cancelled"]
    ) -> ExportTaskCancelledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["export_task_completed"]
    ) -> ExportTaskCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_available"]) -> ImageAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_exists"]) -> ImageExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_exists"]) -> InstanceExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_running"]) -> InstanceRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_status_ok"]) -> InstanceStatusOkWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_stopped"]) -> InstanceStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_terminated"]) -> InstanceTerminatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["internet_gateway_exists"]
    ) -> InternetGatewayExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["key_pair_exists"]) -> KeyPairExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["nat_gateway_available"]
    ) -> NatGatewayAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["nat_gateway_deleted"]) -> NatGatewayDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["network_interface_available"]
    ) -> NetworkInterfaceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["password_data_available"]
    ) -> PasswordDataAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["security_group_exists"]
    ) -> SecurityGroupExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["snapshot_completed"]) -> SnapshotCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["snapshot_imported"]) -> SnapshotImportedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["spot_instance_request_fulfilled"]
    ) -> SpotInstanceRequestFulfilledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["store_image_task_complete"]
    ) -> StoreImageTaskCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["subnet_available"]) -> SubnetAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["system_status_ok"]) -> SystemStatusOkWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["volume_available"]) -> VolumeAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["volume_deleted"]) -> VolumeDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["volume_in_use"]) -> VolumeInUseWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vpc_available"]) -> VpcAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vpc_exists"]) -> VpcExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpc_peering_connection_deleted"]
    ) -> VpcPeeringConnectionDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpc_peering_connection_exists"]
    ) -> VpcPeeringConnectionExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpn_connection_available"]
    ) -> VpnConnectionAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpn_connection_deleted"]
    ) -> VpnConnectionDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """
