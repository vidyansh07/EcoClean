"""
Type annotations for ec2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/type_defs/)

Usage::

    ```python
    from mypy_boto3_ec2.type_defs import AcceleratorCountRequestTypeDef

    data: AcceleratorCountRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AcceleratorManufacturerType,
    AcceleratorNameType,
    AcceleratorTypeType,
    AccountAttributeNameType,
    ActivityStatusType,
    AddressFamilyType,
    AddressTransferStatusType,
    AffinityType,
    AllocationStateType,
    AllocationStrategyType,
    AllowsMultipleInstanceTypesType,
    AmdSevSnpSpecificationType,
    AnalysisStatusType,
    ApplianceModeSupportValueType,
    ArchitectureTypeType,
    ArchitectureValuesType,
    AsnAssociationStateType,
    AsnStateType,
    AssociationStatusCodeType,
    AttachmentStatusType,
    AutoAcceptSharedAssociationsValueType,
    AutoAcceptSharedAttachmentsValueType,
    AutoPlacementType,
    AvailabilityZoneOptInStatusType,
    AvailabilityZoneStateType,
    BareMetalType,
    BatchStateType,
    BgpStatusType,
    BootModeTypeType,
    BootModeValuesType,
    BundleTaskStateType,
    BurstablePerformanceType,
    ByoipCidrStateType,
    CancelBatchErrorCodeType,
    CancelSpotInstanceRequestStateType,
    CapacityReservationFleetStateType,
    CapacityReservationInstancePlatformType,
    CapacityReservationPreferenceType,
    CapacityReservationStateType,
    CapacityReservationTenancyType,
    CapacityReservationTypeType,
    CarrierGatewayStateType,
    ClientCertificateRevocationListStatusCodeType,
    ClientVpnAuthenticationTypeType,
    ClientVpnAuthorizationRuleStatusCodeType,
    ClientVpnConnectionStatusCodeType,
    ClientVpnEndpointAttributeStatusCodeType,
    ClientVpnEndpointStatusCodeType,
    ClientVpnRouteStatusCodeType,
    ConnectionNotificationStateType,
    ConnectivityTypeType,
    ConversionTaskStateType,
    CpuManufacturerType,
    DatafeedSubscriptionStateType,
    DefaultRouteTableAssociationValueType,
    DefaultRouteTablePropagationValueType,
    DefaultTargetCapacityTypeType,
    DeleteFleetErrorCodeType,
    DeleteQueuedReservedInstancesErrorCodeType,
    DestinationFileFormatType,
    DeviceTrustProviderTypeType,
    DeviceTypeType,
    DiskImageFormatType,
    DiskTypeType,
    DnsNameStateType,
    DnsRecordIpTypeType,
    DnsSupportValueType,
    DomainTypeType,
    DynamicRoutingValueType,
    EbsEncryptionSupportType,
    EbsNvmeSupportType,
    EbsOptimizedSupportType,
    Ec2InstanceConnectEndpointStateType,
    ElasticGpuStatusType,
    EnaSupportType,
    EndDateTypeType,
    EphemeralNvmeSupportType,
    EventCodeType,
    EventTypeType,
    ExcessCapacityTerminationPolicyType,
    ExportEnvironmentType,
    ExportTaskStateType,
    FastLaunchStateCodeType,
    FastSnapshotRestoreStateCodeType,
    FindingsFoundType,
    FleetActivityStatusType,
    FleetEventTypeType,
    FleetExcessCapacityTerminationPolicyType,
    FleetOnDemandAllocationStrategyType,
    FleetReplacementStrategyType,
    FleetStateCodeType,
    FleetTypeType,
    FlowLogsResourceTypeType,
    FpgaImageAttributeNameType,
    FpgaImageStateCodeType,
    GatewayAssociationStateType,
    HostMaintenanceType,
    HostnameTypeType,
    HostRecoveryType,
    HostTenancyType,
    HttpTokensStateType,
    HypervisorTypeType,
    IamInstanceProfileAssociationStateType,
    Igmpv2SupportValueType,
    ImageAttributeNameType,
    ImageStateType,
    ImageTypeValuesType,
    InstanceAttributeNameType,
    InstanceAutoRecoveryStateType,
    InstanceBootModeValuesType,
    InstanceEventWindowStateType,
    InstanceGenerationType,
    InstanceHealthStatusType,
    InstanceInterruptionBehaviorType,
    InstanceLifecycleType,
    InstanceLifecycleTypeType,
    InstanceMatchCriteriaType,
    InstanceMetadataEndpointStateType,
    InstanceMetadataOptionsStateType,
    InstanceMetadataProtocolStateType,
    InstanceMetadataTagsStateType,
    InstanceStateNameType,
    InstanceStorageEncryptionSupportType,
    InstanceTypeHypervisorType,
    InstanceTypeType,
    InterfacePermissionTypeType,
    InterfaceProtocolTypeType,
    IpAddressTypeType,
    IpamAddressHistoryResourceTypeType,
    IpamAssociatedResourceDiscoveryStatusType,
    IpamComplianceStatusType,
    IpamDiscoveryFailureCodeType,
    IpamManagementStateType,
    IpamOverlapStatusType,
    IpamPoolAllocationResourceTypeType,
    IpamPoolCidrFailureCodeType,
    IpamPoolCidrStateType,
    IpamPoolPublicIpSourceType,
    IpamPoolStateType,
    IpamPublicAddressAssociationStatusType,
    IpamPublicAddressAwsServiceType,
    IpamPublicAddressTypeType,
    IpamResourceDiscoveryAssociationStateType,
    IpamResourceDiscoveryStateType,
    IpamResourceTypeType,
    IpamScopeStateType,
    IpamScopeTypeType,
    IpamStateType,
    IpamTierType,
    Ipv6SupportValueType,
    KeyFormatType,
    KeyTypeType,
    LaunchTemplateAutoRecoveryStateType,
    LaunchTemplateErrorCodeType,
    LaunchTemplateHttpTokensStateType,
    LaunchTemplateInstanceMetadataEndpointStateType,
    LaunchTemplateInstanceMetadataOptionsStateType,
    LaunchTemplateInstanceMetadataProtocolIpv6Type,
    LaunchTemplateInstanceMetadataTagsStateType,
    ListingStateType,
    ListingStatusType,
    LocalGatewayRouteStateType,
    LocalGatewayRouteTableModeType,
    LocalGatewayRouteTypeType,
    LocalStorageType,
    LocalStorageTypeType,
    LocationTypeType,
    LockModeType,
    LockStateType,
    LogDestinationTypeType,
    MarketTypeType,
    MembershipTypeType,
    ModifyAvailabilityZoneOptInStatusType,
    MonitoringStateType,
    MoveStatusType,
    MulticastSupportValueType,
    NatGatewayAddressStatusType,
    NatGatewayStateType,
    NetworkInterfaceAttributeType,
    NetworkInterfaceCreationTypeType,
    NetworkInterfacePermissionStateCodeType,
    NetworkInterfaceStatusType,
    NetworkInterfaceTypeType,
    NitroEnclavesSupportType,
    NitroTpmSupportType,
    OfferingClassTypeType,
    OfferingTypeValuesType,
    OnDemandAllocationStrategyType,
    OperationTypeType,
    PartitionLoadFrequencyType,
    PaymentOptionType,
    PeriodTypeType,
    PlacementGroupStateType,
    PlacementGroupStrategyType,
    PlacementStrategyType,
    PrefixListStateType,
    PrincipalTypeType,
    ProductCodeValuesType,
    ProtocolType,
    ReplacementStrategyType,
    ReplaceRootVolumeTaskStateType,
    ReportInstanceReasonCodesType,
    ReportStatusTypeType,
    ReservationStateType,
    ReservedInstanceStateType,
    ResourceTypeType,
    RIProductDescriptionType,
    RootDeviceTypeType,
    RouteOriginType,
    RouteStateType,
    RouteTableAssociationStateCodeType,
    RuleActionType,
    SecurityGroupReferencingSupportValueType,
    SelfServicePortalType,
    ServiceConnectivityTypeType,
    ServiceStateType,
    ServiceTypeType,
    ShutdownBehaviorType,
    SnapshotAttributeNameType,
    SnapshotBlockPublicAccessStateType,
    SnapshotStateType,
    SpotAllocationStrategyType,
    SpotInstanceInterruptionBehaviorType,
    SpotInstanceStateType,
    SpotInstanceTypeType,
    SpreadLevelType,
    SSETypeType,
    StateType,
    StaticSourcesSupportValueType,
    StatusType,
    StatusTypeType,
    StorageTierType,
    SubnetCidrBlockStateCodeType,
    SubnetCidrReservationTypeType,
    SubnetStateType,
    SummaryStatusType,
    TargetCapacityUnitTypeType,
    TelemetryStatusType,
    TenancyType,
    TieringOperationStatusType,
    TrafficDirectionType,
    TrafficMirrorFilterRuleFieldType,
    TrafficMirrorRuleActionType,
    TrafficMirrorSessionFieldType,
    TrafficMirrorTargetTypeType,
    TrafficTypeType,
    TransitGatewayAssociationStateType,
    TransitGatewayAttachmentResourceTypeType,
    TransitGatewayAttachmentStateType,
    TransitGatewayConnectPeerStateType,
    TransitGatewayMulitcastDomainAssociationStateType,
    TransitGatewayMulticastDomainStateType,
    TransitGatewayPolicyTableStateType,
    TransitGatewayPrefixListReferenceStateType,
    TransitGatewayPropagationStateType,
    TransitGatewayRouteStateType,
    TransitGatewayRouteTableAnnouncementDirectionType,
    TransitGatewayRouteTableAnnouncementStateType,
    TransitGatewayRouteTableStateType,
    TransitGatewayRouteTypeType,
    TransitGatewayStateType,
    TransportProtocolType,
    TrustProviderTypeType,
    TunnelInsideIpVersionType,
    UnlimitedSupportedInstanceFamilyType,
    UnsuccessfulInstanceCreditSpecificationErrorCodeType,
    UsageClassTypeType,
    UserTrustProviderTypeType,
    VerifiedAccessEndpointProtocolType,
    VerifiedAccessEndpointStatusCodeType,
    VerifiedAccessEndpointTypeType,
    VerifiedAccessLogDeliveryStatusCodeType,
    VirtualizationTypeType,
    VolumeAttachmentStateType,
    VolumeAttributeNameType,
    VolumeModificationStateType,
    VolumeStateType,
    VolumeStatusInfoStatusType,
    VolumeStatusNameType,
    VolumeTypeType,
    VpcAttributeNameType,
    VpcCidrBlockStateCodeType,
    VpcEndpointTypeType,
    VpcPeeringConnectionStateReasonCodeType,
    VpcStateType,
    VpnEcmpSupportValueType,
    VpnStateType,
    WeekDayType,
    scopeType,
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
    "AcceleratorCountRequestTypeDef",
    "AcceleratorCountTypeDef",
    "AcceleratorTotalMemoryMiBRequestTypeDef",
    "AcceleratorTotalMemoryMiBTypeDef",
    "AddressTransferTypeDef",
    "ResponseMetadataTypeDef",
    "TargetConfigurationRequestTypeDef",
    "AcceptTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    "AcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "AcceptTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "AcceptVpcEndpointConnectionsRequestRequestTypeDef",
    "AcceptVpcPeeringConnectionRequestRequestTypeDef",
    "AcceptVpcPeeringConnectionRequestVpcPeeringConnectionAcceptTypeDef",
    "AccountAttributeValueTypeDef",
    "ActiveInstanceTypeDef",
    "AddIpamOperatingRegionTypeDef",
    "AddPrefixListEntryTypeDef",
    "AddedPrincipalTypeDef",
    "AnalysisComponentTypeDef",
    "RuleGroupTypePairTypeDef",
    "RuleOptionTypeDef",
    "PtrUpdateStatusTypeDef",
    "TagTypeDef",
    "AdvertiseByoipCidrRequestRequestTypeDef",
    "AllocateIpamPoolCidrRequestRequestTypeDef",
    "IpamPoolAllocationTypeDef",
    "AlternatePathHintTypeDef",
    "PortRangeTypeDef",
    "AnalysisLoadBalancerListenerTypeDef",
    "AnalysisRouteTableRouteTypeDef",
    "ApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef",
    "AsnAssociationTypeDef",
    "AsnAuthorizationContextTypeDef",
    "AssignIpv6AddressesRequestRequestTypeDef",
    "AssignPrivateIpAddressesRequestNetworkInterfaceAssignPrivateIpAddressesTypeDef",
    "AssignPrivateIpAddressesRequestRequestTypeDef",
    "AssignedPrivateIpAddressTypeDef",
    "Ipv4PrefixSpecificationTypeDef",
    "AssignPrivateNatGatewayAddressRequestRequestTypeDef",
    "NatGatewayAddressTypeDef",
    "AssociateAddressRequestClassicAddressAssociateTypeDef",
    "AssociateAddressRequestRequestTypeDef",
    "AssociateAddressRequestVpcAddressAssociateTypeDef",
    "AssociateClientVpnTargetNetworkRequestRequestTypeDef",
    "AssociationStatusTypeDef",
    "AssociateDhcpOptionsRequestDhcpOptionsAssociateWithVpcTypeDef",
    "AssociateDhcpOptionsRequestRequestTypeDef",
    "AssociateDhcpOptionsRequestVpcAssociateDhcpOptionsTypeDef",
    "AssociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    "IamInstanceProfileSpecificationTypeDef",
    "AssociateIpamByoasnRequestRequestTypeDef",
    "AssociateNatGatewayAddressRequestRequestTypeDef",
    "AssociateRouteTableRequestRequestTypeDef",
    "AssociateRouteTableRequestRouteTableAssociateWithSubnetTypeDef",
    "RouteTableAssociationStateTypeDef",
    "AssociateSubnetCidrBlockRequestRequestTypeDef",
    "AssociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    "AssociateTransitGatewayPolicyTableRequestRequestTypeDef",
    "TransitGatewayPolicyTableAssociationTypeDef",
    "AssociateTransitGatewayRouteTableRequestRequestTypeDef",
    "TransitGatewayAssociationTypeDef",
    "AssociateTrunkInterfaceRequestRequestTypeDef",
    "AssociateVpcCidrBlockRequestRequestTypeDef",
    "AssociatedRoleTypeDef",
    "AssociatedTargetNetworkTypeDef",
    "TimestampTypeDef",
    "AttachClassicLinkVpcRequestInstanceAttachClassicLinkVpcTypeDef",
    "AttachClassicLinkVpcRequestRequestTypeDef",
    "AttachClassicLinkVpcRequestVpcAttachClassicLinkInstanceTypeDef",
    "AttachInternetGatewayRequestInternetGatewayAttachToVpcTypeDef",
    "AttachInternetGatewayRequestRequestTypeDef",
    "AttachInternetGatewayRequestVpcAttachInternetGatewayTypeDef",
    "AttachVerifiedAccessTrustProviderRequestRequestTypeDef",
    "AttachVolumeRequestInstanceAttachVolumeTypeDef",
    "AttachVolumeRequestRequestTypeDef",
    "AttachVolumeRequestVolumeAttachToInstanceTypeDef",
    "AttachVpnGatewayRequestRequestTypeDef",
    "VpcAttachmentTypeDef",
    "AttachmentEnaSrdUdpSpecificationTypeDef",
    "AttributeBooleanValueTypeDef",
    "AttributeValueTypeDef",
    "ClientVpnAuthorizationRuleStatusTypeDef",
    "AuthorizeClientVpnIngressRequestRequestTypeDef",
    "AvailabilityZoneMessageTypeDef",
    "InstanceCapacityTypeDef",
    "BaselineEbsBandwidthMbpsRequestTypeDef",
    "BaselineEbsBandwidthMbpsTypeDef",
    "BlobTypeDef",
    "EbsBlockDeviceTypeDef",
    "BundleTaskErrorTypeDef",
    "ByoasnTypeDef",
    "CancelBundleTaskRequestRequestTypeDef",
    "CancelCapacityReservationFleetErrorTypeDef",
    "CancelCapacityReservationFleetsRequestRequestTypeDef",
    "CapacityReservationFleetCancellationStateTypeDef",
    "CancelCapacityReservationRequestRequestTypeDef",
    "CancelConversionRequestRequestTypeDef",
    "CancelExportTaskRequestRequestTypeDef",
    "CancelImageLaunchPermissionRequestRequestTypeDef",
    "CancelImportTaskRequestRequestTypeDef",
    "CancelReservedInstancesListingRequestRequestTypeDef",
    "CancelSpotFleetRequestsErrorTypeDef",
    "CancelSpotFleetRequestsRequestRequestTypeDef",
    "CancelSpotFleetRequestsSuccessItemTypeDef",
    "CancelSpotInstanceRequestsRequestRequestTypeDef",
    "CancelledSpotInstanceRequestTypeDef",
    "CapacityAllocationTypeDef",
    "CapacityBlockOfferingTypeDef",
    "FleetCapacityReservationTypeDef",
    "CapacityReservationGroupTypeDef",
    "CapacityReservationOptionsRequestTypeDef",
    "CapacityReservationOptionsTypeDef",
    "CapacityReservationTargetResponseTypeDef",
    "CapacityReservationTargetTypeDef",
    "CertificateAuthenticationRequestTypeDef",
    "CertificateAuthenticationTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CidrBlockTypeDef",
    "ClassicLinkDnsSupportTypeDef",
    "GroupIdentifierTypeDef",
    "ClassicLoadBalancerTypeDef",
    "ClientCertificateRevocationListStatusTypeDef",
    "ClientConnectOptionsTypeDef",
    "ClientVpnEndpointAttributeStatusTypeDef",
    "ClientLoginBannerOptionsTypeDef",
    "ClientLoginBannerResponseOptionsTypeDef",
    "DirectoryServiceAuthenticationRequestTypeDef",
    "FederatedAuthenticationRequestTypeDef",
    "DirectoryServiceAuthenticationTypeDef",
    "FederatedAuthenticationTypeDef",
    "ClientVpnConnectionStatusTypeDef",
    "ClientVpnEndpointStatusTypeDef",
    "ConnectionLogResponseOptionsTypeDef",
    "ClientVpnRouteStatusTypeDef",
    "CloudWatchLogOptionsSpecificationTypeDef",
    "CloudWatchLogOptionsTypeDef",
    "CoipAddressUsageTypeDef",
    "CoipCidrTypeDef",
    "ConfirmProductInstanceRequestRequestTypeDef",
    "ConnectionLogOptionsTypeDef",
    "ConnectionNotificationTypeDef",
    "ConnectionTrackingConfigurationTypeDef",
    "ConnectionTrackingSpecificationRequestTypeDef",
    "ConnectionTrackingSpecificationResponseTypeDef",
    "ConnectionTrackingSpecificationTypeDef",
    "CopyFpgaImageRequestRequestTypeDef",
    "CopyImageRequestRequestTypeDef",
    "CpuOptionsRequestTypeDef",
    "CpuOptionsTypeDef",
    "ReservationFleetInstanceSpecificationTypeDef",
    "CreateClientVpnRouteRequestRequestTypeDef",
    "CreateCoipCidrRequestRequestTypeDef",
    "CreateDefaultSubnetRequestRequestTypeDef",
    "CreateDefaultVpcRequestRequestTypeDef",
    "NewDhcpConfigurationTypeDef",
    "TargetCapacitySpecificationRequestTypeDef",
    "DestinationOptionsRequestTypeDef",
    "StorageLocationTypeDef",
    "InstanceEventWindowTimeRangeRequestTypeDef",
    "ExportToS3TaskSpecificationTypeDef",
    "IpamPoolSourceResourceRequestTypeDef",
    "RequestIpamResourceTagTypeDef",
    "CreateLocalGatewayRouteRequestRequestTypeDef",
    "LocalGatewayRouteTypeDef",
    "IcmpTypeCodeTypeDef",
    "CreateNetworkInterfacePermissionRequestRequestTypeDef",
    "InstanceIpv6AddressTypeDef",
    "Ipv4PrefixSpecificationRequestTypeDef",
    "Ipv6PrefixSpecificationRequestTypeDef",
    "PrivateIpAddressSpecificationTypeDef",
    "PriceScheduleSpecificationTypeDef",
    "CreateRouteRequestRequestTypeDef",
    "CreateRouteRequestRouteTableCreateRouteTypeDef",
    "InstanceSpecificationTypeDef",
    "CreateSpotDatafeedSubscriptionRequestRequestTypeDef",
    "S3ObjectTagTypeDef",
    "TrafficMirrorPortRangeRequestTypeDef",
    "TransitGatewayConnectRequestBgpOptionsTypeDef",
    "CreateTransitGatewayConnectRequestOptionsTypeDef",
    "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef",
    "CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef",
    "CreateTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    "TransitGatewayRequestOptionsTypeDef",
    "CreateTransitGatewayRouteRequestRequestTypeDef",
    "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "CreateVerifiedAccessEndpointEniOptionsTypeDef",
    "CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    "VerifiedAccessSseSpecificationRequestTypeDef",
    "CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef",
    "CreateVerifiedAccessTrustProviderOidcOptionsTypeDef",
    "CreateVolumePermissionTypeDef",
    "CreateVpcEndpointConnectionNotificationRequestRequestTypeDef",
    "DnsOptionsSpecificationTypeDef",
    "SubnetConfigurationTypeDef",
    "CreateVpnConnectionRouteRequestRequestTypeDef",
    "CreditSpecificationRequestTypeDef",
    "CreditSpecificationTypeDef",
    "DataQueryTypeDef",
    "MetricPointTypeDef",
    "DeleteCarrierGatewayRequestRequestTypeDef",
    "DeleteClientVpnEndpointRequestRequestTypeDef",
    "DeleteClientVpnRouteRequestRequestTypeDef",
    "DeleteCoipCidrRequestRequestTypeDef",
    "DeleteCoipPoolRequestRequestTypeDef",
    "DeleteCustomerGatewayRequestRequestTypeDef",
    "DeleteDhcpOptionsRequestDhcpOptionsDeleteTypeDef",
    "DeleteDhcpOptionsRequestRequestTypeDef",
    "DeleteEgressOnlyInternetGatewayRequestRequestTypeDef",
    "DeleteFleetErrorTypeDef",
    "DeleteFleetSuccessItemTypeDef",
    "DeleteFleetsRequestRequestTypeDef",
    "DeleteFlowLogsRequestRequestTypeDef",
    "DeleteFpgaImageRequestRequestTypeDef",
    "DeleteInstanceConnectEndpointRequestRequestTypeDef",
    "DeleteInstanceEventWindowRequestRequestTypeDef",
    "InstanceEventWindowStateChangeTypeDef",
    "DeleteInternetGatewayRequestInternetGatewayDeleteTypeDef",
    "DeleteInternetGatewayRequestRequestTypeDef",
    "DeleteIpamPoolRequestRequestTypeDef",
    "DeleteIpamRequestRequestTypeDef",
    "DeleteIpamResourceDiscoveryRequestRequestTypeDef",
    "DeleteIpamScopeRequestRequestTypeDef",
    "DeleteKeyPairRequestKeyPairDeleteTypeDef",
    "DeleteKeyPairRequestKeyPairInfoDeleteTypeDef",
    "DeleteKeyPairRequestRequestTypeDef",
    "DeleteLaunchTemplateRequestRequestTypeDef",
    "DeleteLaunchTemplateVersionsRequestRequestTypeDef",
    "ResponseErrorTypeDef",
    "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef",
    "DeleteLocalGatewayRouteRequestRequestTypeDef",
    "DeleteLocalGatewayRouteTableRequestRequestTypeDef",
    "DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef",
    "DeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    "DeleteManagedPrefixListRequestRequestTypeDef",
    "DeleteNatGatewayRequestRequestTypeDef",
    "DeleteNetworkAclEntryRequestNetworkAclDeleteEntryTypeDef",
    "DeleteNetworkAclEntryRequestRequestTypeDef",
    "DeleteNetworkAclRequestNetworkAclDeleteTypeDef",
    "DeleteNetworkAclRequestRequestTypeDef",
    "DeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    "DeleteNetworkInsightsAccessScopeRequestRequestTypeDef",
    "DeleteNetworkInsightsAnalysisRequestRequestTypeDef",
    "DeleteNetworkInsightsPathRequestRequestTypeDef",
    "DeleteNetworkInterfacePermissionRequestRequestTypeDef",
    "DeleteNetworkInterfaceRequestNetworkInterfaceDeleteTypeDef",
    "DeleteNetworkInterfaceRequestRequestTypeDef",
    "DeletePlacementGroupRequestPlacementGroupDeleteTypeDef",
    "DeletePlacementGroupRequestRequestTypeDef",
    "DeletePublicIpv4PoolRequestRequestTypeDef",
    "DeleteQueuedReservedInstancesErrorTypeDef",
    "DeleteQueuedReservedInstancesRequestRequestTypeDef",
    "SuccessfulQueuedPurchaseDeletionTypeDef",
    "DeleteRouteRequestRequestTypeDef",
    "DeleteRouteRequestRouteDeleteTypeDef",
    "DeleteRouteTableRequestRequestTypeDef",
    "DeleteRouteTableRequestRouteTableDeleteTypeDef",
    "DeleteSecurityGroupRequestRequestTypeDef",
    "DeleteSecurityGroupRequestSecurityGroupDeleteTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteSnapshotRequestSnapshotDeleteTypeDef",
    "DeleteSpotDatafeedSubscriptionRequestRequestTypeDef",
    "DeleteSubnetCidrReservationRequestRequestTypeDef",
    "DeleteSubnetRequestRequestTypeDef",
    "DeleteSubnetRequestSubnetDeleteTypeDef",
    "DeleteTagsRequestTagDeleteTypeDef",
    "DeleteTrafficMirrorFilterRequestRequestTypeDef",
    "DeleteTrafficMirrorFilterRuleRequestRequestTypeDef",
    "DeleteTrafficMirrorSessionRequestRequestTypeDef",
    "DeleteTrafficMirrorTargetRequestRequestTypeDef",
    "DeleteTransitGatewayConnectPeerRequestRequestTypeDef",
    "DeleteTransitGatewayConnectRequestRequestTypeDef",
    "DeleteTransitGatewayMulticastDomainRequestRequestTypeDef",
    "DeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "DeleteTransitGatewayPolicyTableRequestRequestTypeDef",
    "DeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    "DeleteTransitGatewayRequestRequestTypeDef",
    "DeleteTransitGatewayRouteRequestRequestTypeDef",
    "DeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef",
    "DeleteTransitGatewayRouteTableRequestRequestTypeDef",
    "DeleteTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "DeleteVerifiedAccessEndpointRequestRequestTypeDef",
    "DeleteVerifiedAccessGroupRequestRequestTypeDef",
    "DeleteVerifiedAccessInstanceRequestRequestTypeDef",
    "DeleteVerifiedAccessTrustProviderRequestRequestTypeDef",
    "DeleteVolumeRequestRequestTypeDef",
    "DeleteVolumeRequestVolumeDeleteTypeDef",
    "DeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    "DeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    "DeleteVpcEndpointsRequestRequestTypeDef",
    "DeleteVpcPeeringConnectionRequestRequestTypeDef",
    "DeleteVpcPeeringConnectionRequestVpcPeeringConnectionDeleteTypeDef",
    "DeleteVpcRequestRequestTypeDef",
    "DeleteVpcRequestVpcDeleteTypeDef",
    "DeleteVpnConnectionRequestRequestTypeDef",
    "DeleteVpnConnectionRouteRequestRequestTypeDef",
    "DeleteVpnGatewayRequestRequestTypeDef",
    "DeprovisionByoipCidrRequestRequestTypeDef",
    "DeprovisionIpamByoasnRequestRequestTypeDef",
    "DeprovisionIpamPoolCidrRequestRequestTypeDef",
    "DeprovisionPublicIpv4PoolCidrRequestRequestTypeDef",
    "DeregisterImageRequestImageDeregisterTypeDef",
    "DeregisterImageRequestRequestTypeDef",
    "DeregisterInstanceTagAttributeRequestTypeDef",
    "InstanceTagNotificationAttributeTypeDef",
    "DeregisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
    "DeregisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
    "DescribeAccountAttributesRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAddressTransfersRequestRequestTypeDef",
    "DescribeAddressesAttributeRequestRequestTypeDef",
    "FilterTypeDef",
    "DescribeAggregateIdFormatRequestRequestTypeDef",
    "IdFormatTypeDef",
    "SubscriptionTypeDef",
    "WaiterConfigTypeDef",
    "DescribeByoipCidrsRequestRequestTypeDef",
    "DescribeConversionTasksRequestRequestTypeDef",
    "FastLaunchLaunchTemplateSpecificationResponseTypeDef",
    "FastLaunchSnapshotConfigurationResponseTypeDef",
    "DescribeFastSnapshotRestoreSuccessItemTypeDef",
    "DescribeFpgaImageAttributeRequestRequestTypeDef",
    "HostOfferingTypeDef",
    "DescribeIdFormatRequestRequestTypeDef",
    "DescribeIdentityIdFormatRequestRequestTypeDef",
    "DescribeImageAttributeRequestImageDescribeAttributeTypeDef",
    "DescribeImageAttributeRequestRequestTypeDef",
    "DescribeInstanceAttributeRequestInstanceDescribeAttributeTypeDef",
    "DescribeInstanceAttributeRequestRequestTypeDef",
    "InstanceCreditSpecificationTypeDef",
    "DescribeInstanceEventNotificationAttributesRequestRequestTypeDef",
    "InstanceTopologyTypeDef",
    "InstanceTypeOfferingTypeDef",
    "DescribeIpamByoasnRequestRequestTypeDef",
    "LockedSnapshotsInfoTypeDef",
    "MovingAddressStatusTypeDef",
    "DescribeNetworkInterfaceAttributeRequestNetworkInterfaceDescribeAttributeTypeDef",
    "DescribeNetworkInterfaceAttributeRequestRequestTypeDef",
    "PrefixListTypeDef",
    "DescribePrincipalIdFormatRequestRequestTypeDef",
    "RegionTypeDef",
    "ScheduledInstanceRecurrenceRequestTypeDef",
    "DescribeSecurityGroupReferencesRequestRequestTypeDef",
    "SecurityGroupReferenceTypeDef",
    "DescribeSnapshotAttributeRequestRequestTypeDef",
    "DescribeSnapshotAttributeRequestSnapshotDescribeAttributeTypeDef",
    "ProductCodeTypeDef",
    "DescribeSpotDatafeedSubscriptionRequestRequestTypeDef",
    "DescribeSpotFleetInstancesRequestRequestTypeDef",
    "DescribeSpotFleetRequestsRequestRequestTypeDef",
    "SpotPriceTypeDef",
    "DescribeStaleSecurityGroupsRequestRequestTypeDef",
    "StoreImageTaskResultTypeDef",
    "TagDescriptionTypeDef",
    "DescribeVolumeAttributeRequestRequestTypeDef",
    "DescribeVolumeAttributeRequestVolumeDescribeAttributeTypeDef",
    "VolumeModificationTypeDef",
    "DescribeVpcAttributeRequestRequestTypeDef",
    "DescribeVpcAttributeRequestVpcDescribeAttributeTypeDef",
    "DescribeVpcClassicLinkDnsSupportRequestRequestTypeDef",
    "DestinationOptionsResponseTypeDef",
    "DetachClassicLinkVpcRequestInstanceDetachClassicLinkVpcTypeDef",
    "DetachClassicLinkVpcRequestRequestTypeDef",
    "DetachClassicLinkVpcRequestVpcDetachClassicLinkInstanceTypeDef",
    "DetachInternetGatewayRequestInternetGatewayDetachFromVpcTypeDef",
    "DetachInternetGatewayRequestRequestTypeDef",
    "DetachInternetGatewayRequestVpcDetachInternetGatewayTypeDef",
    "DetachNetworkInterfaceRequestNetworkInterfaceDetachTypeDef",
    "DetachNetworkInterfaceRequestRequestTypeDef",
    "DetachVerifiedAccessTrustProviderRequestRequestTypeDef",
    "DetachVolumeRequestInstanceDetachVolumeTypeDef",
    "DetachVolumeRequestRequestTypeDef",
    "DetachVolumeRequestVolumeDetachFromInstanceTypeDef",
    "DetachVpnGatewayRequestRequestTypeDef",
    "DeviceOptionsTypeDef",
    "DisableAddressTransferRequestRequestTypeDef",
    "DisableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef",
    "DisableEbsEncryptionByDefaultRequestRequestTypeDef",
    "DisableFastLaunchRequestRequestTypeDef",
    "DisableFastSnapshotRestoreStateErrorTypeDef",
    "DisableFastSnapshotRestoreSuccessItemTypeDef",
    "DisableFastSnapshotRestoresRequestRequestTypeDef",
    "DisableImageBlockPublicAccessRequestRequestTypeDef",
    "DisableImageDeprecationRequestRequestTypeDef",
    "DisableImageRequestRequestTypeDef",
    "DisableIpamOrganizationAdminAccountRequestRequestTypeDef",
    "DisableSerialConsoleAccessRequestRequestTypeDef",
    "DisableSnapshotBlockPublicAccessRequestRequestTypeDef",
    "DisableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    "TransitGatewayPropagationTypeDef",
    "DisableVgwRoutePropagationRequestRequestTypeDef",
    "DisableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    "DisableVpcClassicLinkRequestRequestTypeDef",
    "DisableVpcClassicLinkRequestVpcDisableClassicLinkTypeDef",
    "DisassociateAddressRequestClassicAddressDisassociateTypeDef",
    "DisassociateAddressRequestNetworkInterfaceAssociationDeleteTypeDef",
    "DisassociateAddressRequestRequestTypeDef",
    "DisassociateClientVpnTargetNetworkRequestRequestTypeDef",
    "DisassociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    "DisassociateIamInstanceProfileRequestRequestTypeDef",
    "DisassociateIpamByoasnRequestRequestTypeDef",
    "DisassociateIpamResourceDiscoveryRequestRequestTypeDef",
    "DisassociateNatGatewayAddressRequestRequestTypeDef",
    "DisassociateRouteTableRequestRequestTypeDef",
    "DisassociateRouteTableRequestRouteTableAssociationDeleteTypeDef",
    "DisassociateRouteTableRequestServiceResourceDisassociateRouteTableTypeDef",
    "DisassociateSubnetCidrBlockRequestRequestTypeDef",
    "DisassociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    "DisassociateTransitGatewayPolicyTableRequestRequestTypeDef",
    "DisassociateTransitGatewayRouteTableRequestRequestTypeDef",
    "DisassociateTrunkInterfaceRequestRequestTypeDef",
    "DisassociateVpcCidrBlockRequestRequestTypeDef",
    "DiskImageDescriptionTypeDef",
    "DiskImageDetailTypeDef",
    "VolumeDetailTypeDef",
    "DiskImageVolumeDescriptionTypeDef",
    "DiskInfoTypeDef",
    "DnsEntryTypeDef",
    "DnsOptionsTypeDef",
    "DnsServersOptionsModifyStructureTypeDef",
    "EbsOptimizedInfoTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "EbsInstanceBlockDeviceTypeDef",
    "EfaInfoTypeDef",
    "InternetGatewayAttachmentTypeDef",
    "ElasticGpuAssociationTypeDef",
    "ElasticGpuHealthTypeDef",
    "ElasticGpuSpecificationResponseTypeDef",
    "ElasticGpuSpecificationTypeDef",
    "ElasticInferenceAcceleratorAssociationTypeDef",
    "ElasticInferenceAcceleratorTypeDef",
    "EnaSrdUdpSpecificationRequestTypeDef",
    "EnaSrdUdpSpecificationTypeDef",
    "EnableAddressTransferRequestRequestTypeDef",
    "EnableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef",
    "EnableEbsEncryptionByDefaultRequestRequestTypeDef",
    "FastLaunchLaunchTemplateSpecificationRequestTypeDef",
    "FastLaunchSnapshotConfigurationRequestTypeDef",
    "EnableFastSnapshotRestoreStateErrorTypeDef",
    "EnableFastSnapshotRestoreSuccessItemTypeDef",
    "EnableFastSnapshotRestoresRequestRequestTypeDef",
    "EnableImageBlockPublicAccessRequestRequestTypeDef",
    "EnableImageRequestRequestTypeDef",
    "EnableIpamOrganizationAdminAccountRequestRequestTypeDef",
    "EnableReachabilityAnalyzerOrganizationSharingRequestRequestTypeDef",
    "EnableSerialConsoleAccessRequestRequestTypeDef",
    "EnableSnapshotBlockPublicAccessRequestRequestTypeDef",
    "EnableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    "EnableVgwRoutePropagationRequestRequestTypeDef",
    "EnableVolumeIORequestRequestTypeDef",
    "EnableVolumeIORequestVolumeEnableIoTypeDef",
    "EnableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    "EnableVpcClassicLinkRequestRequestTypeDef",
    "EnableVpcClassicLinkRequestVpcEnableClassicLinkTypeDef",
    "EnclaveOptionsRequestTypeDef",
    "EnclaveOptionsTypeDef",
    "EventInformationTypeDef",
    "TransitGatewayRouteTableRouteTypeDef",
    "ExportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    "ExportClientVpnClientConfigurationRequestRequestTypeDef",
    "ExportTaskS3LocationRequestTypeDef",
    "ExportTaskS3LocationTypeDef",
    "ExportToS3TaskTypeDef",
    "InstanceExportDetailsTypeDef",
    "FilterPortRangeTypeDef",
    "TargetCapacitySpecificationTypeDef",
    "FleetLaunchTemplateSpecificationRequestTypeDef",
    "FleetLaunchTemplateSpecificationTypeDef",
    "PlacementTypeDef",
    "PlacementResponseTypeDef",
    "FleetSpotCapacityRebalanceRequestTypeDef",
    "FleetSpotCapacityRebalanceTypeDef",
    "FpgaDeviceMemoryInfoTypeDef",
    "LoadPermissionTypeDef",
    "FpgaImageStateTypeDef",
    "PciIdTypeDef",
    "GetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef",
    "GetAssociatedIpv6PoolCidrsRequestRequestTypeDef",
    "Ipv6CidrAssociationTypeDef",
    "GetCapacityReservationUsageRequestRequestTypeDef",
    "InstanceUsageTypeDef",
    "GetConsoleOutputRequestInstanceConsoleOutputTypeDef",
    "GetConsoleOutputRequestRequestTypeDef",
    "GetConsoleScreenshotRequestRequestTypeDef",
    "GetDefaultCreditSpecificationRequestRequestTypeDef",
    "InstanceFamilyCreditSpecificationTypeDef",
    "GetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    "GetEbsEncryptionByDefaultRequestRequestTypeDef",
    "GetGroupsForCapacityReservationRequestRequestTypeDef",
    "GetHostReservationPurchasePreviewRequestRequestTypeDef",
    "PurchaseTypeDef",
    "GetImageBlockPublicAccessStateRequestRequestTypeDef",
    "InstanceTypeInfoFromInstanceRequirementsTypeDef",
    "GetInstanceUefiDataRequestRequestTypeDef",
    "IpamAddressHistoryRecordTypeDef",
    "GetLaunchTemplateDataRequestRequestTypeDef",
    "GetManagedPrefixListAssociationsRequestRequestTypeDef",
    "PrefixListAssociationTypeDef",
    "GetManagedPrefixListEntriesRequestRequestTypeDef",
    "PrefixListEntryTypeDef",
    "GetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef",
    "GetNetworkInsightsAccessScopeContentRequestRequestTypeDef",
    "GetPasswordDataRequestInstancePasswordDataTypeDef",
    "GetPasswordDataRequestRequestTypeDef",
    "ReservationValueTypeDef",
    "GetSerialConsoleAccessStatusRequestRequestTypeDef",
    "GetSnapshotBlockPublicAccessStateRequestRequestTypeDef",
    "SpotPlacementScoreTypeDef",
    "TransitGatewayAttachmentPropagationTypeDef",
    "TransitGatewayRouteTableAssociationTypeDef",
    "TransitGatewayRouteTablePropagationTypeDef",
    "GetVerifiedAccessEndpointPolicyRequestRequestTypeDef",
    "GetVerifiedAccessGroupPolicyRequestRequestTypeDef",
    "GetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef",
    "GetVpnConnectionDeviceTypesRequestRequestTypeDef",
    "VpnConnectionDeviceTypeTypeDef",
    "GetVpnTunnelReplacementStatusRequestRequestTypeDef",
    "MaintenanceDetailsTypeDef",
    "GpuDeviceMemoryInfoTypeDef",
    "HibernationOptionsRequestTypeDef",
    "HibernationOptionsTypeDef",
    "HostInstanceTypeDef",
    "HostPropertiesTypeDef",
    "IKEVersionsListValueTypeDef",
    "IKEVersionsRequestListValueTypeDef",
    "IamInstanceProfileTypeDef",
    "LaunchPermissionTypeDef",
    "UserBucketTypeDef",
    "ImageRecycleBinInfoTypeDef",
    "ImportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    "ImportImageLicenseConfigurationRequestTypeDef",
    "ImportImageLicenseConfigurationResponseTypeDef",
    "UserDataTypeDef",
    "InferenceDeviceMemoryInfoTypeDef",
    "InstanceAttachmentEnaSrdUdpSpecificationTypeDef",
    "InstanceCountTypeDef",
    "InstanceCreditSpecificationRequestTypeDef",
    "InstanceEventWindowTimeRangeTypeDef",
    "InstanceIpv4PrefixTypeDef",
    "InstanceIpv6AddressRequestTypeDef",
    "InstanceIpv6PrefixTypeDef",
    "InstanceMaintenanceOptionsRequestTypeDef",
    "InstanceMaintenanceOptionsTypeDef",
    "InstanceMetadataOptionsRequestTypeDef",
    "InstanceMetadataOptionsResponseTypeDef",
    "MonitoringTypeDef",
    "InstanceNetworkInterfaceAssociationTypeDef",
    "MemoryGiBPerVCpuRequestTypeDef",
    "MemoryMiBRequestTypeDef",
    "NetworkBandwidthGbpsRequestTypeDef",
    "NetworkInterfaceCountRequestTypeDef",
    "TotalLocalStorageGBRequestTypeDef",
    "VCpuCountRangeRequestTypeDef",
    "MemoryGiBPerVCpuTypeDef",
    "MemoryMiBTypeDef",
    "NetworkBandwidthGbpsTypeDef",
    "NetworkInterfaceCountTypeDef",
    "TotalLocalStorageGBTypeDef",
    "VCpuCountRangeTypeDef",
    "InstanceStateTypeDef",
    "InstanceStatusDetailsTypeDef",
    "InstanceStatusEventTypeDef",
    "LicenseConfigurationTypeDef",
    "PrivateDnsNameOptionsResponseTypeDef",
    "MemoryInfoTypeDef",
    "NitroTpmInfoTypeDef",
    "PlacementGroupInfoTypeDef",
    "ProcessorInfoTypeDef",
    "VCpuInfoTypeDef",
    "IpRangeTypeDef",
    "Ipv6RangeTypeDef",
    "PrefixListIdTypeDef",
    "UserIdGroupPairTypeDef",
    "IpamCidrAuthorizationContextTypeDef",
    "IpamDiscoveryFailureReasonTypeDef",
    "IpamPublicAddressSecurityGroupTypeDef",
    "IpamResourceTagTypeDef",
    "IpamOperatingRegionTypeDef",
    "IpamPoolCidrFailureReasonTypeDef",
    "IpamPoolSourceResourceTypeDef",
    "IpamPublicAddressTagTypeDef",
    "Ipv4PrefixSpecificationResponseTypeDef",
    "Ipv6CidrBlockTypeDef",
    "PoolCidrBlockTypeDef",
    "Ipv6PrefixSpecificationResponseTypeDef",
    "Ipv6PrefixSpecificationTypeDef",
    "LastErrorTypeDef",
    "RunInstancesMonitoringEnabledTypeDef",
    "SpotPlacementTypeDef",
    "LaunchTemplateEbsBlockDeviceRequestTypeDef",
    "LaunchTemplateEbsBlockDeviceTypeDef",
    "LaunchTemplateCpuOptionsRequestTypeDef",
    "LaunchTemplateCpuOptionsTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorTypeDef",
    "LaunchTemplateEnaSrdUdpSpecificationTypeDef",
    "LaunchTemplateEnclaveOptionsRequestTypeDef",
    "LaunchTemplateEnclaveOptionsTypeDef",
    "LaunchTemplateHibernationOptionsRequestTypeDef",
    "LaunchTemplateHibernationOptionsTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
    "LaunchTemplateInstanceMaintenanceOptionsRequestTypeDef",
    "LaunchTemplateInstanceMaintenanceOptionsTypeDef",
    "LaunchTemplateSpotMarketOptionsTypeDef",
    "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    "LaunchTemplateInstanceMetadataOptionsTypeDef",
    "LaunchTemplateLicenseConfigurationRequestTypeDef",
    "LaunchTemplateLicenseConfigurationTypeDef",
    "LaunchTemplatePlacementRequestTypeDef",
    "LaunchTemplatePlacementTypeDef",
    "LaunchTemplatePrivateDnsNameOptionsRequestTypeDef",
    "LaunchTemplatePrivateDnsNameOptionsTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplatesMonitoringRequestTypeDef",
    "LaunchTemplatesMonitoringTypeDef",
    "LicenseConfigurationRequestTypeDef",
    "ListImagesInRecycleBinRequestRequestTypeDef",
    "ListSnapshotsInRecycleBinRequestRequestTypeDef",
    "SnapshotRecycleBinInfoTypeDef",
    "LoadPermissionRequestTypeDef",
    "ModifyAddressAttributeRequestRequestTypeDef",
    "ModifyAvailabilityZoneGroupRequestRequestTypeDef",
    "ModifyDefaultCreditSpecificationRequestRequestTypeDef",
    "ModifyEbsDefaultKmsKeyIdRequestRequestTypeDef",
    "ModifyHostsRequestRequestTypeDef",
    "ModifyIdFormatRequestRequestTypeDef",
    "ModifyIdentityIdFormatRequestRequestTypeDef",
    "SuccessfulInstanceCreditSpecificationItemTypeDef",
    "ModifyInstanceMaintenanceOptionsRequestRequestTypeDef",
    "ModifyInstanceMetadataOptionsRequestRequestTypeDef",
    "ModifyInstancePlacementRequestRequestTypeDef",
    "RemoveIpamOperatingRegionTypeDef",
    "ModifyIpamResourceCidrRequestRequestTypeDef",
    "ModifyIpamScopeRequestRequestTypeDef",
    "ModifyLaunchTemplateRequestRequestTypeDef",
    "ModifyLocalGatewayRouteRequestRequestTypeDef",
    "RemovePrefixListEntryTypeDef",
    "NetworkInterfaceAttachmentChangesTypeDef",
    "ModifyPrivateDnsNameOptionsRequestRequestTypeDef",
    "ReservedInstancesConfigurationTypeDef",
    "ModifySnapshotTierRequestRequestTypeDef",
    "ModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef",
    "ModifyTrafficMirrorSessionRequestRequestTypeDef",
    "ModifyTransitGatewayOptionsTypeDef",
    "ModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "ModifyVerifiedAccessEndpointEniOptionsTypeDef",
    "ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    "VerifiedAccessSseSpecificationResponseTypeDef",
    "ModifyVerifiedAccessGroupRequestRequestTypeDef",
    "ModifyVerifiedAccessInstanceRequestRequestTypeDef",
    "ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef",
    "ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef",
    "ModifyVolumeRequestRequestTypeDef",
    "ModifyVpcEndpointConnectionNotificationRequestRequestTypeDef",
    "ModifyVpcEndpointServiceConfigurationRequestRequestTypeDef",
    "ModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef",
    "ModifyVpcEndpointServicePermissionsRequestRequestTypeDef",
    "PeeringConnectionOptionsRequestTypeDef",
    "PeeringConnectionOptionsTypeDef",
    "ModifyVpcTenancyRequestRequestTypeDef",
    "ModifyVpnConnectionOptionsRequestRequestTypeDef",
    "ModifyVpnConnectionRequestRequestTypeDef",
    "ModifyVpnTunnelCertificateRequestRequestTypeDef",
    "Phase1DHGroupNumbersRequestListValueTypeDef",
    "Phase1EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase1IntegrityAlgorithmsRequestListValueTypeDef",
    "Phase2DHGroupNumbersRequestListValueTypeDef",
    "Phase2EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase2IntegrityAlgorithmsRequestListValueTypeDef",
    "MonitorInstancesRequestInstanceMonitorTypeDef",
    "MonitorInstancesRequestRequestTypeDef",
    "MoveAddressToVpcRequestRequestTypeDef",
    "MoveByoipCidrToIpamRequestRequestTypeDef",
    "ProvisionedBandwidthTypeDef",
    "NetworkAclAssociationTypeDef",
    "NetworkCardInfoTypeDef",
    "NetworkInterfaceAssociationTypeDef",
    "NetworkInterfaceIpv6AddressTypeDef",
    "NetworkInterfacePermissionStateTypeDef",
    "OidcOptionsTypeDef",
    "PacketHeaderStatementRequestTypeDef",
    "PacketHeaderStatementTypeDef",
    "RequestFilterPortRangeTypeDef",
    "ResourceStatementRequestTypeDef",
    "ResourceStatementTypeDef",
    "PeeringAttachmentStatusTypeDef",
    "PeeringTgwInfoTypeDef",
    "Phase1DHGroupNumbersListValueTypeDef",
    "Phase1EncryptionAlgorithmsListValueTypeDef",
    "Phase1IntegrityAlgorithmsListValueTypeDef",
    "Phase2DHGroupNumbersListValueTypeDef",
    "Phase2EncryptionAlgorithmsListValueTypeDef",
    "Phase2IntegrityAlgorithmsListValueTypeDef",
    "PriceScheduleTypeDef",
    "PricingDetailTypeDef",
    "PrivateDnsDetailsTypeDef",
    "PrivateDnsNameConfigurationTypeDef",
    "PrivateDnsNameOptionsOnLaunchTypeDef",
    "PrivateDnsNameOptionsRequestTypeDef",
    "PropagatingVgwTypeDef",
    "ProvisionPublicIpv4PoolCidrRequestRequestTypeDef",
    "PublicIpv4PoolRangeTypeDef",
    "PurchaseRequestTypeDef",
    "ReservedInstanceLimitPriceTypeDef",
    "RebootInstancesRequestInstanceRebootTypeDef",
    "RebootInstancesRequestRequestTypeDef",
    "RecurringChargeTypeDef",
    "ReferencedSecurityGroupTypeDef",
    "RegisterInstanceTagAttributeRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
    "RegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
    "RejectTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    "RejectTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "RejectTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "RejectVpcEndpointConnectionsRequestRequestTypeDef",
    "RejectVpcPeeringConnectionRequestRequestTypeDef",
    "RejectVpcPeeringConnectionRequestVpcPeeringConnectionRejectTypeDef",
    "ReleaseAddressRequestClassicAddressReleaseTypeDef",
    "ReleaseAddressRequestRequestTypeDef",
    "ReleaseAddressRequestVpcAddressReleaseTypeDef",
    "ReleaseHostsRequestRequestTypeDef",
    "ReleaseIpamPoolAllocationRequestRequestTypeDef",
    "ReplaceNetworkAclAssociationRequestNetworkAclReplaceAssociationTypeDef",
    "ReplaceNetworkAclAssociationRequestRequestTypeDef",
    "ReplaceRouteRequestRequestTypeDef",
    "ReplaceRouteRequestRouteReplaceTypeDef",
    "ReplaceRouteTableAssociationRequestRequestTypeDef",
    "ReplaceRouteTableAssociationRequestRouteTableAssociationReplaceSubnetTypeDef",
    "ReplaceTransitGatewayRouteRequestRequestTypeDef",
    "ReplaceVpnTunnelRequestRequestTypeDef",
    "ReservedInstancesIdTypeDef",
    "ResetAddressAttributeRequestRequestTypeDef",
    "ResetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    "ResetFpgaImageAttributeRequestRequestTypeDef",
    "ResetImageAttributeRequestImageResetAttributeTypeDef",
    "ResetImageAttributeRequestRequestTypeDef",
    "ResetInstanceAttributeRequestInstanceResetAttributeTypeDef",
    "ResetInstanceAttributeRequestInstanceResetKernelTypeDef",
    "ResetInstanceAttributeRequestInstanceResetRamdiskTypeDef",
    "ResetInstanceAttributeRequestInstanceResetSourceDestCheckTypeDef",
    "ResetInstanceAttributeRequestRequestTypeDef",
    "ResetNetworkInterfaceAttributeRequestNetworkInterfaceResetAttributeTypeDef",
    "ResetNetworkInterfaceAttributeRequestRequestTypeDef",
    "ResetSnapshotAttributeRequestRequestTypeDef",
    "ResetSnapshotAttributeRequestSnapshotResetAttributeTypeDef",
    "RestoreAddressToClassicRequestRequestTypeDef",
    "RestoreImageFromRecycleBinRequestRequestTypeDef",
    "RestoreManagedPrefixListVersionRequestRequestTypeDef",
    "RestoreSnapshotFromRecycleBinRequestRequestTypeDef",
    "RestoreSnapshotTierRequestRequestTypeDef",
    "RevokeClientVpnIngressRequestRequestTypeDef",
    "RouteTypeDef",
    "ScheduledInstanceRecurrenceTypeDef",
    "ScheduledInstancesEbsTypeDef",
    "ScheduledInstancesIamInstanceProfileTypeDef",
    "ScheduledInstancesIpv6AddressTypeDef",
    "ScheduledInstancesMonitoringTypeDef",
    "ScheduledInstancesPlacementTypeDef",
    "ScheduledInstancesPrivateIpAddressConfigTypeDef",
    "TransitGatewayMulticastGroupTypeDef",
    "SecurityGroupIdentifierTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "SecurityGroupRuleRequestTypeDef",
    "SendDiagnosticInterruptRequestRequestTypeDef",
    "ServiceTypeDetailTypeDef",
    "UserBucketDetailsTypeDef",
    "SpotCapacityRebalanceTypeDef",
    "SpotInstanceStateFaultTypeDef",
    "SpotFleetMonitoringTypeDef",
    "SpotInstanceStatusTypeDef",
    "StartInstancesRequestInstanceStartTypeDef",
    "StartInstancesRequestRequestTypeDef",
    "StartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef",
    "StopInstancesRequestInstanceStopTypeDef",
    "StopInstancesRequestRequestTypeDef",
    "SubnetAssociationTypeDef",
    "SubnetCidrBlockStateTypeDef",
    "TargetConfigurationTypeDef",
    "TargetGroupTypeDef",
    "TerminateClientVpnConnectionsRequestRequestTypeDef",
    "TerminateInstancesRequestInstanceTerminateTypeDef",
    "TerminateInstancesRequestRequestTypeDef",
    "TrafficMirrorPortRangeTypeDef",
    "TransitGatewayAttachmentAssociationTypeDef",
    "TransitGatewayAttachmentBgpConfigurationTypeDef",
    "TransitGatewayConnectOptionsTypeDef",
    "TransitGatewayMulticastDomainOptionsTypeDef",
    "TransitGatewayOptionsTypeDef",
    "TransitGatewayPeeringAttachmentOptionsTypeDef",
    "TransitGatewayPolicyRuleMetaDataTypeDef",
    "TransitGatewayPrefixListAttachmentTypeDef",
    "TransitGatewayRouteAttachmentTypeDef",
    "TransitGatewayVpcAttachmentOptionsTypeDef",
    "UnassignIpv6AddressesRequestRequestTypeDef",
    "UnassignPrivateIpAddressesRequestNetworkInterfaceUnassignPrivateIpAddressesTypeDef",
    "UnassignPrivateIpAddressesRequestRequestTypeDef",
    "UnassignPrivateNatGatewayAddressRequestRequestTypeDef",
    "UnlockSnapshotRequestRequestTypeDef",
    "UnmonitorInstancesRequestInstanceUnmonitorTypeDef",
    "UnmonitorInstancesRequestRequestTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    "UnsuccessfulItemErrorTypeDef",
    "ValidationErrorTypeDef",
    "VerifiedAccessEndpointEniOptionsTypeDef",
    "VerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    "VerifiedAccessEndpointStatusTypeDef",
    "VerifiedAccessTrustProviderCondensedTypeDef",
    "VerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef",
    "VerifiedAccessLogDeliveryStatusTypeDef",
    "VerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef",
    "VerifiedAccessLogS3DestinationOptionsTypeDef",
    "VgwTelemetryTypeDef",
    "VolumeStatusActionTypeDef",
    "VolumeStatusAttachmentStatusTypeDef",
    "VolumeStatusDetailsTypeDef",
    "VolumeStatusEventTypeDef",
    "VpcCidrBlockStateTypeDef",
    "VpcPeeringConnectionOptionsDescriptionTypeDef",
    "VpcPeeringConnectionStateReasonTypeDef",
    "VpnStaticRouteTypeDef",
    "WithdrawByoipCidrRequestRequestTypeDef",
    "AcceptAddressTransferResultTypeDef",
    "AcceptReservedInstancesExchangeQuoteResultTypeDef",
    "AllocateAddressResultTypeDef",
    "AllocateHostsResultTypeDef",
    "ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef",
    "AssignIpv6AddressesResultTypeDef",
    "AssociateAddressResultTypeDef",
    "AssociateEnclaveCertificateIamRoleResultTypeDef",
    "AttachClassicLinkVpcResultTypeDef",
    "AttachNetworkInterfaceResultTypeDef",
    "CancelCapacityReservationResultTypeDef",
    "CancelImageLaunchPermissionResultTypeDef",
    "CancelImportTaskResultTypeDef",
    "ConfirmProductInstanceResultTypeDef",
    "ConnectionTrackingConfigurationResponseTypeDef",
    "CopyFpgaImageResultTypeDef",
    "CopyImageResultTypeDef",
    "CpuOptionsResponseTypeDef",
    "CreateFpgaImageResultTypeDef",
    "CreateImageResultTypeDef",
    "CreatePublicIpv4PoolResultTypeDef",
    "CreateRestoreImageTaskResultTypeDef",
    "CreateRouteResultTypeDef",
    "CreateStoreImageTaskResultTypeDef",
    "DeleteEgressOnlyInternetGatewayResultTypeDef",
    "DeleteFpgaImageResultTypeDef",
    "DeleteKeyPairResultTypeDef",
    "DeleteNatGatewayResultTypeDef",
    "DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef",
    "DeleteNetworkInsightsAccessScopeResultTypeDef",
    "DeleteNetworkInsightsAnalysisResultTypeDef",
    "DeleteNetworkInsightsPathResultTypeDef",
    "DeleteNetworkInterfacePermissionResultTypeDef",
    "DeletePublicIpv4PoolResultTypeDef",
    "DeleteTrafficMirrorFilterResultTypeDef",
    "DeleteTrafficMirrorFilterRuleResultTypeDef",
    "DeleteTrafficMirrorSessionResultTypeDef",
    "DeleteTrafficMirrorTargetResultTypeDef",
    "DeleteVpcPeeringConnectionResultTypeDef",
    "DeprovisionPublicIpv4PoolCidrResultTypeDef",
    "DescribeAddressTransfersResultTypeDef",
    "DetachClassicLinkVpcResultTypeDef",
    "DisableAddressTransferResultTypeDef",
    "DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef",
    "DisableEbsEncryptionByDefaultResultTypeDef",
    "DisableImageBlockPublicAccessResultTypeDef",
    "DisableImageDeprecationResultTypeDef",
    "DisableImageResultTypeDef",
    "DisableIpamOrganizationAdminAccountResultTypeDef",
    "DisableSerialConsoleAccessResultTypeDef",
    "DisableSnapshotBlockPublicAccessResultTypeDef",
    "DisableVpcClassicLinkDnsSupportResultTypeDef",
    "DisableVpcClassicLinkResultTypeDef",
    "DisassociateEnclaveCertificateIamRoleResultTypeDef",
    "DisassociateTrunkInterfaceResultTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableAddressTransferResultTypeDef",
    "EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef",
    "EnableEbsEncryptionByDefaultResultTypeDef",
    "EnableImageBlockPublicAccessResultTypeDef",
    "EnableImageDeprecationResultTypeDef",
    "EnableImageResultTypeDef",
    "EnableIpamOrganizationAdminAccountResultTypeDef",
    "EnableReachabilityAnalyzerOrganizationSharingResultTypeDef",
    "EnableSerialConsoleAccessResultTypeDef",
    "EnableSnapshotBlockPublicAccessResultTypeDef",
    "EnableVpcClassicLinkDnsSupportResultTypeDef",
    "EnableVpcClassicLinkResultTypeDef",
    "EnclaveOptionsResponseTypeDef",
    "ExportClientVpnClientConfigurationResultTypeDef",
    "ExportTransitGatewayRoutesResultTypeDef",
    "GetConsoleOutputResultTypeDef",
    "GetConsoleScreenshotResultTypeDef",
    "GetEbsDefaultKmsKeyIdResultTypeDef",
    "GetEbsEncryptionByDefaultResultTypeDef",
    "GetFlowLogsIntegrationTemplateResultTypeDef",
    "GetImageBlockPublicAccessStateResultTypeDef",
    "GetInstanceUefiDataResultTypeDef",
    "GetPasswordDataResultTypeDef",
    "GetSerialConsoleAccessStatusResultTypeDef",
    "GetSnapshotBlockPublicAccessStateResultTypeDef",
    "GetVerifiedAccessEndpointPolicyResultTypeDef",
    "GetVerifiedAccessGroupPolicyResultTypeDef",
    "GetVpnConnectionDeviceSampleConfigurationResultTypeDef",
    "HibernationOptionsResponseTypeDef",
    "IamInstanceProfileResponseTypeDef",
    "ImportClientVpnClientCertificateRevocationListResultTypeDef",
    "InstanceMaintenanceOptionsResponseTypeDef",
    "InstanceMetadataOptionsResponseResponseTypeDef",
    "InstanceStateResponseTypeDef",
    "LockSnapshotResultTypeDef",
    "ModifyAvailabilityZoneGroupResultTypeDef",
    "ModifyCapacityReservationFleetResultTypeDef",
    "ModifyCapacityReservationResultTypeDef",
    "ModifyClientVpnEndpointResultTypeDef",
    "ModifyEbsDefaultKmsKeyIdResultTypeDef",
    "ModifyFleetResultTypeDef",
    "ModifyInstanceCapacityReservationAttributesResultTypeDef",
    "ModifyInstanceMaintenanceOptionsResultTypeDef",
    "ModifyInstancePlacementResultTypeDef",
    "ModifyPrivateDnsNameOptionsResultTypeDef",
    "ModifyReservedInstancesResultTypeDef",
    "ModifySecurityGroupRulesResultTypeDef",
    "ModifySnapshotTierResultTypeDef",
    "ModifySpotFleetRequestResponseTypeDef",
    "ModifyVpcEndpointConnectionNotificationResultTypeDef",
    "ModifyVpcEndpointResultTypeDef",
    "ModifyVpcEndpointServiceConfigurationResultTypeDef",
    "ModifyVpcEndpointServicePayerResponsibilityResultTypeDef",
    "ModifyVpcTenancyResultTypeDef",
    "MonitoringResponseTypeDef",
    "MoveAddressToVpcResultTypeDef",
    "NetworkInterfaceAssociationResponseTypeDef",
    "PlacementExtraResponseTypeDef",
    "PrivateDnsNameOptionsOnLaunchResponseTypeDef",
    "PrivateDnsNameOptionsResponseResponseTypeDef",
    "PurchaseReservedInstancesOfferingResultTypeDef",
    "RegisterImageResultTypeDef",
    "RejectVpcPeeringConnectionResultTypeDef",
    "ReleaseIpamPoolAllocationResultTypeDef",
    "ReplaceNetworkAclAssociationResultTypeDef",
    "ReplaceVpnTunnelResultTypeDef",
    "RequestSpotFleetResponseTypeDef",
    "ResetEbsDefaultKmsKeyIdResultTypeDef",
    "ResetFpgaImageAttributeResultTypeDef",
    "RestoreAddressToClassicResultTypeDef",
    "RestoreImageFromRecycleBinResultTypeDef",
    "RestoreSnapshotFromRecycleBinResultTypeDef",
    "RestoreSnapshotTierResultTypeDef",
    "RouteTableAssociationStateResponseTypeDef",
    "RunScheduledInstancesResultTypeDef",
    "StartVpcEndpointServicePrivateDnsVerificationResultTypeDef",
    "StateReasonResponseTypeDef",
    "StateReasonTypeDef",
    "UnassignIpv6AddressesResultTypeDef",
    "UnlockSnapshotResultTypeDef",
    "UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef",
    "UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef",
    "VolumeAttachmentResponseTypeDef",
    "VolumeAttachmentTypeDef",
    "VpcPeeringConnectionStateReasonResponseTypeDef",
    "AcceptReservedInstancesExchangeQuoteRequestRequestTypeDef",
    "GetReservedInstancesExchangeQuoteRequestRequestTypeDef",
    "AccountAttributeTypeDef",
    "DescribeFleetInstancesResultTypeDef",
    "DescribeSpotFleetInstancesResponseTypeDef",
    "ModifyVpcEndpointServicePermissionsResultTypeDef",
    "AnalysisLoadBalancerTargetTypeDef",
    "RuleGroupRuleOptionsPairTypeDef",
    "AddressAttributeTypeDef",
    "AddressTypeDef",
    "AllowedPrincipalTypeDef",
    "CarrierGatewayTypeDef",
    "ClientCreateTagsRequestTypeDef",
    "ClientDeleteTagsRequestTypeDef",
    "CoipPoolTypeDef",
    "CopySnapshotResultTypeDef",
    "CreateSecurityGroupResultTypeDef",
    "CreateTagsRequestServiceResourceCreateTagsTypeDef",
    "CustomerGatewayTypeDef",
    "Ec2InstanceConnectEndpointTypeDef",
    "HostReservationTypeDef",
    "ImportKeyPairResultTypeDef",
    "InstanceCreateTagsRequestTypeDef",
    "InstanceDeleteTagsRequestTypeDef",
    "InstanceEventWindowAssociationRequestTypeDef",
    "InstanceEventWindowAssociationTargetTypeDef",
    "InstanceEventWindowDisassociationRequestTypeDef",
    "IpamResourceDiscoveryAssociationTypeDef",
    "IpamScopeTypeDef",
    "KeyPairInfoTypeDef",
    "KeyPairTypeDef",
    "LaunchTemplateTagSpecificationRequestTypeDef",
    "LaunchTemplateTagSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
    "LocalGatewayRouteTableVpcAssociationTypeDef",
    "LocalGatewayTypeDef",
    "LocalGatewayVirtualInterfaceGroupTypeDef",
    "LocalGatewayVirtualInterfaceTypeDef",
    "ManagedPrefixListTypeDef",
    "NetworkInsightsAccessScopeAnalysisTypeDef",
    "NetworkInsightsAccessScopeTypeDef",
    "PlacementGroupTypeDef",
    "ReplaceRootVolumeTaskTypeDef",
    "SecurityGroupForVpcTypeDef",
    "SnapshotInfoTypeDef",
    "SnapshotResponseTypeDef",
    "SnapshotTierStatusTypeDef",
    "SnapshotTypeDef",
    "SpotFleetTagSpecificationTypeDef",
    "SubnetCidrReservationTypeDef",
    "TagSpecificationPaginatorTypeDef",
    "TagSpecificationTypeDef",
    "TrafficMirrorSessionTypeDef",
    "TrafficMirrorTargetTypeDef",
    "TransitGatewayPolicyTableTypeDef",
    "TransitGatewayRouteTableAnnouncementTypeDef",
    "TransitGatewayRouteTableTypeDef",
    "TrunkInterfaceAssociationTypeDef",
    "VpcClassicLinkTypeDef",
    "VpcCreateTagsRequestTypeDef",
    "AllocateIpamPoolCidrResultTypeDef",
    "GetIpamPoolAllocationsResultTypeDef",
    "AnalysisAclRuleTypeDef",
    "AnalysisPacketHeaderTypeDef",
    "AnalysisSecurityGroupRuleTypeDef",
    "FirewallStatefulRuleTypeDef",
    "FirewallStatelessRuleTypeDef",
    "AssociateIpamByoasnResultTypeDef",
    "ByoipCidrTypeDef",
    "DisassociateIpamByoasnResultTypeDef",
    "ProvisionIpamByoasnRequestRequestTypeDef",
    "AssignPrivateIpAddressesResultTypeDef",
    "AssignPrivateNatGatewayAddressResultTypeDef",
    "AssociateNatGatewayAddressResultTypeDef",
    "DisassociateNatGatewayAddressResultTypeDef",
    "UnassignPrivateNatGatewayAddressResultTypeDef",
    "AssociateClientVpnTargetNetworkResultTypeDef",
    "DisassociateClientVpnTargetNetworkResultTypeDef",
    "TargetNetworkTypeDef",
    "AssociateIamInstanceProfileRequestRequestTypeDef",
    "ReplaceIamInstanceProfileAssociationRequestRequestTypeDef",
    "AssociateRouteTableResultTypeDef",
    "ReplaceRouteTableAssociationResultTypeDef",
    "RouteTableAssociationTypeDef",
    "AssociateTransitGatewayPolicyTableResultTypeDef",
    "DisassociateTransitGatewayPolicyTableResultTypeDef",
    "GetTransitGatewayPolicyTableAssociationsResultTypeDef",
    "AssociateTransitGatewayRouteTableResultTypeDef",
    "DisassociateTransitGatewayRouteTableResultTypeDef",
    "GetAssociatedEnclaveCertificateIamRolesResultTypeDef",
    "AthenaIntegrationTypeDef",
    "ClientDataTypeDef",
    "DescribeCapacityBlockOfferingsRequestRequestTypeDef",
    "DescribeFleetHistoryRequestRequestTypeDef",
    "DescribeSpotFleetRequestHistoryRequestRequestTypeDef",
    "EnableImageDeprecationRequestRequestTypeDef",
    "GetIpamAddressHistoryRequestRequestTypeDef",
    "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    "LockSnapshotRequestRequestTypeDef",
    "ModifyCapacityReservationFleetRequestRequestTypeDef",
    "ModifyCapacityReservationRequestRequestTypeDef",
    "ModifyInstanceEventStartTimeRequestRequestTypeDef",
    "ReportInstanceStatusRequestInstanceReportStatusTypeDef",
    "ReportInstanceStatusRequestRequestTypeDef",
    "SlotDateTimeRangeRequestTypeDef",
    "SlotStartTimeRangeRequestTypeDef",
    "SpotMarketOptionsTypeDef",
    "AttachVpnGatewayResultTypeDef",
    "VpnGatewayTypeDef",
    "AttachmentEnaSrdSpecificationTypeDef",
    "DescribeVpcAttributeResultTypeDef",
    "ModifySubnetAttributeRequestRequestTypeDef",
    "ModifyVolumeAttributeRequestRequestTypeDef",
    "ModifyVolumeAttributeRequestVolumeModifyAttributeTypeDef",
    "ModifyVpcAttributeRequestRequestTypeDef",
    "ModifyVpcAttributeRequestVpcModifyAttributeTypeDef",
    "DhcpConfigurationTypeDef",
    "AuthorizationRuleTypeDef",
    "AuthorizeClientVpnIngressResultTypeDef",
    "RevokeClientVpnIngressResultTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableCapacityTypeDef",
    "BlobAttributeValueTypeDef",
    "S3StorageTypeDef",
    "BlockDeviceMappingTypeDef",
    "DeprovisionIpamByoasnResultTypeDef",
    "DescribeIpamByoasnResultTypeDef",
    "ProvisionIpamByoasnResultTypeDef",
    "FailedCapacityReservationFleetCancellationResultTypeDef",
    "CancelSpotFleetRequestsErrorItemTypeDef",
    "CancelSpotInstanceRequestsResultTypeDef",
    "CapacityReservationTypeDef",
    "DescribeCapacityBlockOfferingsResultTypeDef",
    "CapacityReservationFleetTypeDef",
    "CreateCapacityReservationFleetResultTypeDef",
    "GetGroupsForCapacityReservationResultTypeDef",
    "OnDemandOptionsRequestTypeDef",
    "OnDemandOptionsTypeDef",
    "CapacityReservationSpecificationResponseResponseTypeDef",
    "CapacityReservationSpecificationResponseTypeDef",
    "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
    "CapacityReservationSpecificationTypeDef",
    "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
    "DescribeVpcClassicLinkDnsSupportResultTypeDef",
    "ClassicLinkInstanceTypeDef",
    "ClassicLoadBalancersConfigTypeDef",
    "ExportClientVpnClientCertificateRevocationListResultTypeDef",
    "ClientConnectResponseOptionsTypeDef",
    "ClientVpnAuthenticationRequestTypeDef",
    "ClientVpnAuthenticationTypeDef",
    "ClientVpnConnectionTypeDef",
    "TerminateConnectionStatusTypeDef",
    "CreateClientVpnEndpointResultTypeDef",
    "DeleteClientVpnEndpointResultTypeDef",
    "ClientVpnRouteTypeDef",
    "CreateClientVpnRouteResultTypeDef",
    "DeleteClientVpnRouteResultTypeDef",
    "VpnTunnelLogOptionsSpecificationTypeDef",
    "VpnTunnelLogOptionsTypeDef",
    "GetCoipPoolUsageResultTypeDef",
    "CreateCoipCidrResultTypeDef",
    "DeleteCoipCidrResultTypeDef",
    "CreateVpcEndpointConnectionNotificationResultTypeDef",
    "DescribeVpcEndpointConnectionNotificationsResultTypeDef",
    "ModifyInstanceEventWindowRequestRequestTypeDef",
    "ModifyIpamPoolRequestRequestTypeDef",
    "CreateLocalGatewayRouteResultTypeDef",
    "DeleteLocalGatewayRouteResultTypeDef",
    "ModifyLocalGatewayRouteResultTypeDef",
    "SearchLocalGatewayRoutesResultTypeDef",
    "CreateNetworkAclEntryRequestNetworkAclCreateEntryTypeDef",
    "CreateNetworkAclEntryRequestRequestTypeDef",
    "NetworkAclEntryTypeDef",
    "ReplaceNetworkAclEntryRequestNetworkAclReplaceEntryTypeDef",
    "ReplaceNetworkAclEntryRequestRequestTypeDef",
    "CreateReservedInstancesListingRequestRequestTypeDef",
    "CreateStoreImageTaskRequestRequestTypeDef",
    "CreateTrafficMirrorFilterRuleRequestRequestTypeDef",
    "ModifyTrafficMirrorFilterRuleRequestRequestTypeDef",
    "ModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef",
    "ModifyVerifiedAccessGroupPolicyRequestRequestTypeDef",
    "CreateVolumePermissionModificationsTypeDef",
    "ModifyVpcEndpointRequestRequestTypeDef",
    "GetAwsNetworkPerformanceDataRequestRequestTypeDef",
    "DataResponseTypeDef",
    "DeleteFleetErrorItemTypeDef",
    "DeleteInstanceEventWindowResultTypeDef",
    "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef",
    "FailedQueuedPurchaseDeletionTypeDef",
    "DeregisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    "DeregisterInstanceEventNotificationAttributesResultTypeDef",
    "DescribeInstanceEventNotificationAttributesResultTypeDef",
    "RegisterInstanceEventNotificationAttributesResultTypeDef",
    "DeregisterTransitGatewayMulticastGroupMembersResultTypeDef",
    "DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    "DescribeAddressTransfersRequestDescribeAddressTransfersPaginateTypeDef",
    "DescribeAddressesAttributeRequestDescribeAddressesAttributePaginateTypeDef",
    "DescribeByoipCidrsRequestDescribeByoipCidrsPaginateTypeDef",
    "DescribeCapacityBlockOfferingsRequestDescribeCapacityBlockOfferingsPaginateTypeDef",
    "DescribePrincipalIdFormatRequestDescribePrincipalIdFormatPaginateTypeDef",
    "DescribeSpotFleetInstancesRequestDescribeSpotFleetInstancesPaginateTypeDef",
    "DescribeSpotFleetRequestsRequestDescribeSpotFleetRequestsPaginateTypeDef",
    "DescribeStaleSecurityGroupsRequestDescribeStaleSecurityGroupsPaginateTypeDef",
    "DescribeVpcClassicLinkDnsSupportRequestDescribeVpcClassicLinkDnsSupportPaginateTypeDef",
    "GetAssociatedIpv6PoolCidrsRequestGetAssociatedIpv6PoolCidrsPaginateTypeDef",
    "GetAwsNetworkPerformanceDataRequestGetAwsNetworkPerformanceDataPaginateTypeDef",
    "GetGroupsForCapacityReservationRequestGetGroupsForCapacityReservationPaginateTypeDef",
    "GetIpamAddressHistoryRequestGetIpamAddressHistoryPaginateTypeDef",
    "GetManagedPrefixListAssociationsRequestGetManagedPrefixListAssociationsPaginateTypeDef",
    "GetManagedPrefixListEntriesRequestGetManagedPrefixListEntriesPaginateTypeDef",
    "GetNetworkInsightsAccessScopeAnalysisFindingsRequestGetNetworkInsightsAccessScopeAnalysisFindingsPaginateTypeDef",
    "GetVpnConnectionDeviceTypesRequestGetVpnConnectionDeviceTypesPaginateTypeDef",
    "ListImagesInRecycleBinRequestListImagesInRecycleBinPaginateTypeDef",
    "ListSnapshotsInRecycleBinRequestListSnapshotsInRecycleBinPaginateTypeDef",
    "DescribeAddressesRequestRequestTypeDef",
    "DescribeAvailabilityZonesRequestRequestTypeDef",
    "DescribeAwsNetworkPerformanceMetricSubscriptionsRequestDescribeAwsNetworkPerformanceMetricSubscriptionsPaginateTypeDef",
    "DescribeAwsNetworkPerformanceMetricSubscriptionsRequestRequestTypeDef",
    "DescribeBundleTasksRequestRequestTypeDef",
    "DescribeCapacityReservationFleetsRequestDescribeCapacityReservationFleetsPaginateTypeDef",
    "DescribeCapacityReservationFleetsRequestRequestTypeDef",
    "DescribeCapacityReservationsRequestDescribeCapacityReservationsPaginateTypeDef",
    "DescribeCapacityReservationsRequestRequestTypeDef",
    "DescribeCarrierGatewaysRequestDescribeCarrierGatewaysPaginateTypeDef",
    "DescribeCarrierGatewaysRequestRequestTypeDef",
    "DescribeClassicLinkInstancesRequestDescribeClassicLinkInstancesPaginateTypeDef",
    "DescribeClassicLinkInstancesRequestRequestTypeDef",
    "DescribeClientVpnAuthorizationRulesRequestDescribeClientVpnAuthorizationRulesPaginateTypeDef",
    "DescribeClientVpnAuthorizationRulesRequestRequestTypeDef",
    "DescribeClientVpnConnectionsRequestDescribeClientVpnConnectionsPaginateTypeDef",
    "DescribeClientVpnConnectionsRequestRequestTypeDef",
    "DescribeClientVpnEndpointsRequestDescribeClientVpnEndpointsPaginateTypeDef",
    "DescribeClientVpnEndpointsRequestRequestTypeDef",
    "DescribeClientVpnRoutesRequestDescribeClientVpnRoutesPaginateTypeDef",
    "DescribeClientVpnRoutesRequestRequestTypeDef",
    "DescribeClientVpnTargetNetworksRequestDescribeClientVpnTargetNetworksPaginateTypeDef",
    "DescribeClientVpnTargetNetworksRequestRequestTypeDef",
    "DescribeCoipPoolsRequestDescribeCoipPoolsPaginateTypeDef",
    "DescribeCoipPoolsRequestRequestTypeDef",
    "DescribeCustomerGatewaysRequestRequestTypeDef",
    "DescribeDhcpOptionsRequestDescribeDhcpOptionsPaginateTypeDef",
    "DescribeDhcpOptionsRequestRequestTypeDef",
    "DescribeEgressOnlyInternetGatewaysRequestDescribeEgressOnlyInternetGatewaysPaginateTypeDef",
    "DescribeEgressOnlyInternetGatewaysRequestRequestTypeDef",
    "DescribeElasticGpusRequestRequestTypeDef",
    "DescribeExportImageTasksRequestDescribeExportImageTasksPaginateTypeDef",
    "DescribeExportImageTasksRequestRequestTypeDef",
    "DescribeExportTasksRequestRequestTypeDef",
    "DescribeFastLaunchImagesRequestDescribeFastLaunchImagesPaginateTypeDef",
    "DescribeFastLaunchImagesRequestRequestTypeDef",
    "DescribeFastSnapshotRestoresRequestDescribeFastSnapshotRestoresPaginateTypeDef",
    "DescribeFastSnapshotRestoresRequestRequestTypeDef",
    "DescribeFleetInstancesRequestRequestTypeDef",
    "DescribeFleetsRequestDescribeFleetsPaginateTypeDef",
    "DescribeFleetsRequestRequestTypeDef",
    "DescribeFlowLogsRequestDescribeFlowLogsPaginateTypeDef",
    "DescribeFlowLogsRequestRequestTypeDef",
    "DescribeFpgaImagesRequestDescribeFpgaImagesPaginateTypeDef",
    "DescribeFpgaImagesRequestRequestTypeDef",
    "DescribeHostReservationOfferingsRequestDescribeHostReservationOfferingsPaginateTypeDef",
    "DescribeHostReservationOfferingsRequestRequestTypeDef",
    "DescribeHostReservationsRequestDescribeHostReservationsPaginateTypeDef",
    "DescribeHostReservationsRequestRequestTypeDef",
    "DescribeHostsRequestDescribeHostsPaginateTypeDef",
    "DescribeHostsRequestRequestTypeDef",
    "DescribeIamInstanceProfileAssociationsRequestDescribeIamInstanceProfileAssociationsPaginateTypeDef",
    "DescribeIamInstanceProfileAssociationsRequestRequestTypeDef",
    "DescribeImagesRequestDescribeImagesPaginateTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "DescribeImportImageTasksRequestDescribeImportImageTasksPaginateTypeDef",
    "DescribeImportImageTasksRequestRequestTypeDef",
    "DescribeImportSnapshotTasksRequestDescribeImportSnapshotTasksPaginateTypeDef",
    "DescribeImportSnapshotTasksRequestRequestTypeDef",
    "DescribeInstanceConnectEndpointsRequestDescribeInstanceConnectEndpointsPaginateTypeDef",
    "DescribeInstanceConnectEndpointsRequestRequestTypeDef",
    "DescribeInstanceCreditSpecificationsRequestDescribeInstanceCreditSpecificationsPaginateTypeDef",
    "DescribeInstanceCreditSpecificationsRequestRequestTypeDef",
    "DescribeInstanceEventWindowsRequestDescribeInstanceEventWindowsPaginateTypeDef",
    "DescribeInstanceEventWindowsRequestRequestTypeDef",
    "DescribeInstanceStatusRequestDescribeInstanceStatusPaginateTypeDef",
    "DescribeInstanceStatusRequestRequestTypeDef",
    "DescribeInstanceTopologyRequestDescribeInstanceTopologyPaginateTypeDef",
    "DescribeInstanceTopologyRequestRequestTypeDef",
    "DescribeInstanceTypeOfferingsRequestDescribeInstanceTypeOfferingsPaginateTypeDef",
    "DescribeInstanceTypeOfferingsRequestRequestTypeDef",
    "DescribeInstanceTypesRequestDescribeInstanceTypesPaginateTypeDef",
    "DescribeInstanceTypesRequestRequestTypeDef",
    "DescribeInstancesRequestDescribeInstancesPaginateTypeDef",
    "DescribeInstancesRequestRequestTypeDef",
    "DescribeInternetGatewaysRequestDescribeInternetGatewaysPaginateTypeDef",
    "DescribeInternetGatewaysRequestRequestTypeDef",
    "DescribeIpamPoolsRequestDescribeIpamPoolsPaginateTypeDef",
    "DescribeIpamPoolsRequestRequestTypeDef",
    "DescribeIpamResourceDiscoveriesRequestDescribeIpamResourceDiscoveriesPaginateTypeDef",
    "DescribeIpamResourceDiscoveriesRequestRequestTypeDef",
    "DescribeIpamResourceDiscoveryAssociationsRequestDescribeIpamResourceDiscoveryAssociationsPaginateTypeDef",
    "DescribeIpamResourceDiscoveryAssociationsRequestRequestTypeDef",
    "DescribeIpamScopesRequestDescribeIpamScopesPaginateTypeDef",
    "DescribeIpamScopesRequestRequestTypeDef",
    "DescribeIpamsRequestDescribeIpamsPaginateTypeDef",
    "DescribeIpamsRequestRequestTypeDef",
    "DescribeIpv6PoolsRequestDescribeIpv6PoolsPaginateTypeDef",
    "DescribeIpv6PoolsRequestRequestTypeDef",
    "DescribeKeyPairsRequestRequestTypeDef",
    "DescribeLaunchTemplateVersionsRequestDescribeLaunchTemplateVersionsPaginateTypeDef",
    "DescribeLaunchTemplateVersionsRequestRequestTypeDef",
    "DescribeLaunchTemplatesRequestDescribeLaunchTemplatesPaginateTypeDef",
    "DescribeLaunchTemplatesRequestRequestTypeDef",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestDescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginateTypeDef",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestRequestTypeDef",
    "DescribeLocalGatewayRouteTableVpcAssociationsRequestDescribeLocalGatewayRouteTableVpcAssociationsPaginateTypeDef",
    "DescribeLocalGatewayRouteTableVpcAssociationsRequestRequestTypeDef",
    "DescribeLocalGatewayRouteTablesRequestDescribeLocalGatewayRouteTablesPaginateTypeDef",
    "DescribeLocalGatewayRouteTablesRequestRequestTypeDef",
    "DescribeLocalGatewayVirtualInterfaceGroupsRequestDescribeLocalGatewayVirtualInterfaceGroupsPaginateTypeDef",
    "DescribeLocalGatewayVirtualInterfaceGroupsRequestRequestTypeDef",
    "DescribeLocalGatewayVirtualInterfacesRequestDescribeLocalGatewayVirtualInterfacesPaginateTypeDef",
    "DescribeLocalGatewayVirtualInterfacesRequestRequestTypeDef",
    "DescribeLocalGatewaysRequestDescribeLocalGatewaysPaginateTypeDef",
    "DescribeLocalGatewaysRequestRequestTypeDef",
    "DescribeLockedSnapshotsRequestRequestTypeDef",
    "DescribeManagedPrefixListsRequestDescribeManagedPrefixListsPaginateTypeDef",
    "DescribeManagedPrefixListsRequestRequestTypeDef",
    "DescribeMovingAddressesRequestDescribeMovingAddressesPaginateTypeDef",
    "DescribeMovingAddressesRequestRequestTypeDef",
    "DescribeNatGatewaysRequestDescribeNatGatewaysPaginateTypeDef",
    "DescribeNatGatewaysRequestRequestTypeDef",
    "DescribeNetworkAclsRequestDescribeNetworkAclsPaginateTypeDef",
    "DescribeNetworkAclsRequestRequestTypeDef",
    "DescribeNetworkInsightsAccessScopeAnalysesRequestDescribeNetworkInsightsAccessScopeAnalysesPaginateTypeDef",
    "DescribeNetworkInsightsAccessScopeAnalysesRequestRequestTypeDef",
    "DescribeNetworkInsightsAccessScopesRequestDescribeNetworkInsightsAccessScopesPaginateTypeDef",
    "DescribeNetworkInsightsAccessScopesRequestRequestTypeDef",
    "DescribeNetworkInsightsAnalysesRequestDescribeNetworkInsightsAnalysesPaginateTypeDef",
    "DescribeNetworkInsightsAnalysesRequestRequestTypeDef",
    "DescribeNetworkInsightsPathsRequestDescribeNetworkInsightsPathsPaginateTypeDef",
    "DescribeNetworkInsightsPathsRequestRequestTypeDef",
    "DescribeNetworkInterfacePermissionsRequestDescribeNetworkInterfacePermissionsPaginateTypeDef",
    "DescribeNetworkInterfacePermissionsRequestRequestTypeDef",
    "DescribeNetworkInterfacesRequestDescribeNetworkInterfacesPaginateTypeDef",
    "DescribeNetworkInterfacesRequestRequestTypeDef",
    "DescribePlacementGroupsRequestRequestTypeDef",
    "DescribePrefixListsRequestDescribePrefixListsPaginateTypeDef",
    "DescribePrefixListsRequestRequestTypeDef",
    "DescribePublicIpv4PoolsRequestDescribePublicIpv4PoolsPaginateTypeDef",
    "DescribePublicIpv4PoolsRequestRequestTypeDef",
    "DescribeRegionsRequestRequestTypeDef",
    "DescribeReplaceRootVolumeTasksRequestDescribeReplaceRootVolumeTasksPaginateTypeDef",
    "DescribeReplaceRootVolumeTasksRequestRequestTypeDef",
    "DescribeReservedInstancesListingsRequestRequestTypeDef",
    "DescribeReservedInstancesModificationsRequestDescribeReservedInstancesModificationsPaginateTypeDef",
    "DescribeReservedInstancesModificationsRequestRequestTypeDef",
    "DescribeReservedInstancesOfferingsRequestDescribeReservedInstancesOfferingsPaginateTypeDef",
    "DescribeReservedInstancesOfferingsRequestRequestTypeDef",
    "DescribeReservedInstancesRequestRequestTypeDef",
    "DescribeRouteTablesRequestDescribeRouteTablesPaginateTypeDef",
    "DescribeRouteTablesRequestRequestTypeDef",
    "DescribeSecurityGroupRulesRequestDescribeSecurityGroupRulesPaginateTypeDef",
    "DescribeSecurityGroupRulesRequestRequestTypeDef",
    "DescribeSecurityGroupsRequestDescribeSecurityGroupsPaginateTypeDef",
    "DescribeSecurityGroupsRequestRequestTypeDef",
    "DescribeSnapshotTierStatusRequestDescribeSnapshotTierStatusPaginateTypeDef",
    "DescribeSnapshotTierStatusRequestRequestTypeDef",
    "DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef",
    "DescribeSnapshotsRequestRequestTypeDef",
    "DescribeSpotInstanceRequestsRequestDescribeSpotInstanceRequestsPaginateTypeDef",
    "DescribeSpotInstanceRequestsRequestRequestTypeDef",
    "DescribeSpotPriceHistoryRequestDescribeSpotPriceHistoryPaginateTypeDef",
    "DescribeSpotPriceHistoryRequestRequestTypeDef",
    "DescribeStoreImageTasksRequestDescribeStoreImageTasksPaginateTypeDef",
    "DescribeStoreImageTasksRequestRequestTypeDef",
    "DescribeSubnetsRequestDescribeSubnetsPaginateTypeDef",
    "DescribeSubnetsRequestRequestTypeDef",
    "DescribeTagsRequestDescribeTagsPaginateTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeTrafficMirrorFiltersRequestDescribeTrafficMirrorFiltersPaginateTypeDef",
    "DescribeTrafficMirrorFiltersRequestRequestTypeDef",
    "DescribeTrafficMirrorSessionsRequestDescribeTrafficMirrorSessionsPaginateTypeDef",
    "DescribeTrafficMirrorSessionsRequestRequestTypeDef",
    "DescribeTrafficMirrorTargetsRequestDescribeTrafficMirrorTargetsPaginateTypeDef",
    "DescribeTrafficMirrorTargetsRequestRequestTypeDef",
    "DescribeTransitGatewayAttachmentsRequestDescribeTransitGatewayAttachmentsPaginateTypeDef",
    "DescribeTransitGatewayAttachmentsRequestRequestTypeDef",
    "DescribeTransitGatewayConnectPeersRequestDescribeTransitGatewayConnectPeersPaginateTypeDef",
    "DescribeTransitGatewayConnectPeersRequestRequestTypeDef",
    "DescribeTransitGatewayConnectsRequestDescribeTransitGatewayConnectsPaginateTypeDef",
    "DescribeTransitGatewayConnectsRequestRequestTypeDef",
    "DescribeTransitGatewayMulticastDomainsRequestDescribeTransitGatewayMulticastDomainsPaginateTypeDef",
    "DescribeTransitGatewayMulticastDomainsRequestRequestTypeDef",
    "DescribeTransitGatewayPeeringAttachmentsRequestDescribeTransitGatewayPeeringAttachmentsPaginateTypeDef",
    "DescribeTransitGatewayPeeringAttachmentsRequestRequestTypeDef",
    "DescribeTransitGatewayPolicyTablesRequestDescribeTransitGatewayPolicyTablesPaginateTypeDef",
    "DescribeTransitGatewayPolicyTablesRequestRequestTypeDef",
    "DescribeTransitGatewayRouteTableAnnouncementsRequestDescribeTransitGatewayRouteTableAnnouncementsPaginateTypeDef",
    "DescribeTransitGatewayRouteTableAnnouncementsRequestRequestTypeDef",
    "DescribeTransitGatewayRouteTablesRequestDescribeTransitGatewayRouteTablesPaginateTypeDef",
    "DescribeTransitGatewayRouteTablesRequestRequestTypeDef",
    "DescribeTransitGatewayVpcAttachmentsRequestDescribeTransitGatewayVpcAttachmentsPaginateTypeDef",
    "DescribeTransitGatewayVpcAttachmentsRequestRequestTypeDef",
    "DescribeTransitGatewaysRequestDescribeTransitGatewaysPaginateTypeDef",
    "DescribeTransitGatewaysRequestRequestTypeDef",
    "DescribeTrunkInterfaceAssociationsRequestDescribeTrunkInterfaceAssociationsPaginateTypeDef",
    "DescribeTrunkInterfaceAssociationsRequestRequestTypeDef",
    "DescribeVerifiedAccessEndpointsRequestDescribeVerifiedAccessEndpointsPaginateTypeDef",
    "DescribeVerifiedAccessEndpointsRequestRequestTypeDef",
    "DescribeVerifiedAccessGroupsRequestDescribeVerifiedAccessGroupsPaginateTypeDef",
    "DescribeVerifiedAccessGroupsRequestRequestTypeDef",
    "DescribeVerifiedAccessInstanceLoggingConfigurationsRequestDescribeVerifiedAccessInstanceLoggingConfigurationsPaginateTypeDef",
    "DescribeVerifiedAccessInstanceLoggingConfigurationsRequestRequestTypeDef",
    "DescribeVerifiedAccessInstancesRequestDescribeVerifiedAccessInstancesPaginateTypeDef",
    "DescribeVerifiedAccessInstancesRequestRequestTypeDef",
    "DescribeVerifiedAccessTrustProvidersRequestDescribeVerifiedAccessTrustProvidersPaginateTypeDef",
    "DescribeVerifiedAccessTrustProvidersRequestRequestTypeDef",
    "DescribeVolumeStatusRequestDescribeVolumeStatusPaginateTypeDef",
    "DescribeVolumeStatusRequestRequestTypeDef",
    "DescribeVolumeStatusRequestVolumeDescribeStatusTypeDef",
    "DescribeVolumesModificationsRequestDescribeVolumesModificationsPaginateTypeDef",
    "DescribeVolumesModificationsRequestRequestTypeDef",
    "DescribeVolumesRequestDescribeVolumesPaginateTypeDef",
    "DescribeVolumesRequestRequestTypeDef",
    "DescribeVpcClassicLinkRequestRequestTypeDef",
    "DescribeVpcEndpointConnectionNotificationsRequestDescribeVpcEndpointConnectionNotificationsPaginateTypeDef",
    "DescribeVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    "DescribeVpcEndpointConnectionsRequestDescribeVpcEndpointConnectionsPaginateTypeDef",
    "DescribeVpcEndpointConnectionsRequestRequestTypeDef",
    "DescribeVpcEndpointServiceConfigurationsRequestDescribeVpcEndpointServiceConfigurationsPaginateTypeDef",
    "DescribeVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    "DescribeVpcEndpointServicePermissionsRequestDescribeVpcEndpointServicePermissionsPaginateTypeDef",
    "DescribeVpcEndpointServicePermissionsRequestRequestTypeDef",
    "DescribeVpcEndpointServicesRequestDescribeVpcEndpointServicesPaginateTypeDef",
    "DescribeVpcEndpointServicesRequestRequestTypeDef",
    "DescribeVpcEndpointsRequestDescribeVpcEndpointsPaginateTypeDef",
    "DescribeVpcEndpointsRequestRequestTypeDef",
    "DescribeVpcPeeringConnectionsRequestDescribeVpcPeeringConnectionsPaginateTypeDef",
    "DescribeVpcPeeringConnectionsRequestRequestTypeDef",
    "DescribeVpcsRequestDescribeVpcsPaginateTypeDef",
    "DescribeVpcsRequestRequestTypeDef",
    "DescribeVpnConnectionsRequestRequestTypeDef",
    "DescribeVpnGatewaysRequestRequestTypeDef",
    "ExportTransitGatewayRoutesRequestRequestTypeDef",
    "GetCoipPoolUsageRequestRequestTypeDef",
    "GetIpamDiscoveredAccountsRequestGetIpamDiscoveredAccountsPaginateTypeDef",
    "GetIpamDiscoveredAccountsRequestRequestTypeDef",
    "GetIpamDiscoveredPublicAddressesRequestRequestTypeDef",
    "GetIpamDiscoveredResourceCidrsRequestGetIpamDiscoveredResourceCidrsPaginateTypeDef",
    "GetIpamDiscoveredResourceCidrsRequestRequestTypeDef",
    "GetIpamPoolAllocationsRequestGetIpamPoolAllocationsPaginateTypeDef",
    "GetIpamPoolAllocationsRequestRequestTypeDef",
    "GetIpamPoolCidrsRequestGetIpamPoolCidrsPaginateTypeDef",
    "GetIpamPoolCidrsRequestRequestTypeDef",
    "GetIpamResourceCidrsRequestGetIpamResourceCidrsPaginateTypeDef",
    "GetIpamResourceCidrsRequestRequestTypeDef",
    "GetSecurityGroupsForVpcRequestGetSecurityGroupsForVpcPaginateTypeDef",
    "GetSecurityGroupsForVpcRequestRequestTypeDef",
    "GetSubnetCidrReservationsRequestRequestTypeDef",
    "GetTransitGatewayAttachmentPropagationsRequestGetTransitGatewayAttachmentPropagationsPaginateTypeDef",
    "GetTransitGatewayAttachmentPropagationsRequestRequestTypeDef",
    "GetTransitGatewayMulticastDomainAssociationsRequestGetTransitGatewayMulticastDomainAssociationsPaginateTypeDef",
    "GetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    "GetTransitGatewayPolicyTableAssociationsRequestGetTransitGatewayPolicyTableAssociationsPaginateTypeDef",
    "GetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef",
    "GetTransitGatewayPolicyTableEntriesRequestRequestTypeDef",
    "GetTransitGatewayPrefixListReferencesRequestGetTransitGatewayPrefixListReferencesPaginateTypeDef",
    "GetTransitGatewayPrefixListReferencesRequestRequestTypeDef",
    "GetTransitGatewayRouteTableAssociationsRequestGetTransitGatewayRouteTableAssociationsPaginateTypeDef",
    "GetTransitGatewayRouteTableAssociationsRequestRequestTypeDef",
    "GetTransitGatewayRouteTablePropagationsRequestGetTransitGatewayRouteTablePropagationsPaginateTypeDef",
    "GetTransitGatewayRouteTablePropagationsRequestRequestTypeDef",
    "SearchLocalGatewayRoutesRequestRequestTypeDef",
    "SearchLocalGatewayRoutesRequestSearchLocalGatewayRoutesPaginateTypeDef",
    "SearchTransitGatewayMulticastGroupsRequestRequestTypeDef",
    "SearchTransitGatewayMulticastGroupsRequestSearchTransitGatewayMulticastGroupsPaginateTypeDef",
    "SearchTransitGatewayRoutesRequestRequestTypeDef",
    "DescribeAggregateIdFormatResultTypeDef",
    "DescribeIdFormatResultTypeDef",
    "DescribeIdentityIdFormatResultTypeDef",
    "PrincipalIdFormatTypeDef",
    "DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef",
    "DescribeBundleTasksRequestBundleTaskCompleteWaitTypeDef",
    "DescribeConversionTasksRequestConversionTaskCancelledWaitTypeDef",
    "DescribeConversionTasksRequestConversionTaskCompletedWaitTypeDef",
    "DescribeConversionTasksRequestConversionTaskDeletedWaitTypeDef",
    "DescribeCustomerGatewaysRequestCustomerGatewayAvailableWaitTypeDef",
    "DescribeExportTasksRequestExportTaskCancelledWaitTypeDef",
    "DescribeExportTasksRequestExportTaskCompletedWaitTypeDef",
    "DescribeImagesRequestImageAvailableWaitTypeDef",
    "DescribeImagesRequestImageExistsWaitTypeDef",
    "DescribeImportSnapshotTasksRequestSnapshotImportedWaitTypeDef",
    "DescribeInstanceStatusRequestInstanceStatusOkWaitTypeDef",
    "DescribeInstanceStatusRequestSystemStatusOkWaitTypeDef",
    "DescribeInstancesRequestInstanceExistsWaitTypeDef",
    "DescribeInstancesRequestInstanceRunningWaitTypeDef",
    "DescribeInstancesRequestInstanceStoppedWaitTypeDef",
    "DescribeInstancesRequestInstanceTerminatedWaitTypeDef",
    "DescribeInternetGatewaysRequestInternetGatewayExistsWaitTypeDef",
    "DescribeKeyPairsRequestKeyPairExistsWaitTypeDef",
    "DescribeNatGatewaysRequestNatGatewayAvailableWaitTypeDef",
    "DescribeNatGatewaysRequestNatGatewayDeletedWaitTypeDef",
    "DescribeNetworkInterfacesRequestNetworkInterfaceAvailableWaitTypeDef",
    "DescribeSecurityGroupsRequestSecurityGroupExistsWaitTypeDef",
    "DescribeSnapshotsRequestSnapshotCompletedWaitTypeDef",
    "DescribeSpotInstanceRequestsRequestSpotInstanceRequestFulfilledWaitTypeDef",
    "DescribeStoreImageTasksRequestStoreImageTaskCompleteWaitTypeDef",
    "DescribeSubnetsRequestSubnetAvailableWaitTypeDef",
    "DescribeVolumesRequestVolumeAvailableWaitTypeDef",
    "DescribeVolumesRequestVolumeDeletedWaitTypeDef",
    "DescribeVolumesRequestVolumeInUseWaitTypeDef",
    "DescribeVpcPeeringConnectionsRequestVpcPeeringConnectionDeletedWaitTypeDef",
    "DescribeVpcPeeringConnectionsRequestVpcPeeringConnectionExistsWaitTypeDef",
    "DescribeVpcsRequestVpcAvailableWaitTypeDef",
    "DescribeVpcsRequestVpcExistsWaitTypeDef",
    "DescribeVpnConnectionsRequestVpnConnectionAvailableWaitTypeDef",
    "DescribeVpnConnectionsRequestVpnConnectionDeletedWaitTypeDef",
    "GetPasswordDataRequestPasswordDataAvailableWaitTypeDef",
    "DescribeFastLaunchImagesSuccessItemTypeDef",
    "DisableFastLaunchResultTypeDef",
    "EnableFastLaunchResultTypeDef",
    "DescribeFastSnapshotRestoresResultTypeDef",
    "DescribeHostReservationOfferingsResultTypeDef",
    "DescribeInstanceCreditSpecificationsResultTypeDef",
    "DescribeInstanceTopologyResultTypeDef",
    "DescribeInstanceTypeOfferingsResultTypeDef",
    "DescribeLockedSnapshotsResultTypeDef",
    "DescribeMovingAddressesResultTypeDef",
    "DescribePrefixListsResultTypeDef",
    "DescribeRegionsResultTypeDef",
    "DescribeSecurityGroupReferencesResultTypeDef",
    "DescribeSnapshotAttributeResultTypeDef",
    "DescribeVolumeAttributeResultTypeDef",
    "DescribeSpotPriceHistoryResultTypeDef",
    "DescribeStoreImageTasksResultTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeVolumesModificationsResultTypeDef",
    "ModifyVolumeResultTypeDef",
    "FlowLogTypeDef",
    "DisableFastSnapshotRestoreStateErrorItemTypeDef",
    "DisableTransitGatewayRouteTablePropagationResultTypeDef",
    "EnableTransitGatewayRouteTablePropagationResultTypeDef",
    "DiskImageTypeDef",
    "ImportVolumeRequestRequestTypeDef",
    "ImportInstanceVolumeDetailItemTypeDef",
    "ImportVolumeTaskDetailsTypeDef",
    "InstanceStorageInfoTypeDef",
    "VpcEndpointConnectionTypeDef",
    "ModifyClientVpnEndpointRequestRequestTypeDef",
    "EbsInfoTypeDef",
    "InstanceBlockDeviceMappingSpecificationTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "EgressOnlyInternetGatewayTypeDef",
    "InternetGatewayTypeDef",
    "ElasticGpusTypeDef",
    "EnaSrdSpecificationRequestTypeDef",
    "EnaSrdSpecificationTypeDef",
    "EnableFastLaunchRequestRequestTypeDef",
    "EnableFastSnapshotRestoreStateErrorItemTypeDef",
    "HistoryRecordEntryTypeDef",
    "HistoryRecordTypeDef",
    "ExportImageResultTypeDef",
    "ExportImageTaskTypeDef",
    "ExportTaskTypeDef",
    "PathFilterTypeDef",
    "FleetSpotMaintenanceStrategiesRequestTypeDef",
    "FleetSpotMaintenanceStrategiesTypeDef",
    "FpgaDeviceInfoTypeDef",
    "FpgaImageAttributeTypeDef",
    "FpgaImageTypeDef",
    "GetAssociatedIpv6PoolCidrsResultTypeDef",
    "GetCapacityReservationUsageResultTypeDef",
    "GetDefaultCreditSpecificationResultTypeDef",
    "ModifyDefaultCreditSpecificationResultTypeDef",
    "GetHostReservationPurchasePreviewResultTypeDef",
    "PurchaseHostReservationResultTypeDef",
    "GetInstanceTypesFromInstanceRequirementsResultTypeDef",
    "GetIpamAddressHistoryResultTypeDef",
    "GetManagedPrefixListAssociationsResultTypeDef",
    "GetManagedPrefixListEntriesResultTypeDef",
    "ReservedInstanceReservationValueTypeDef",
    "GetSpotPlacementScoresResultTypeDef",
    "GetTransitGatewayAttachmentPropagationsResultTypeDef",
    "GetTransitGatewayRouteTableAssociationsResultTypeDef",
    "GetTransitGatewayRouteTablePropagationsResultTypeDef",
    "GetVpnConnectionDeviceTypesResultTypeDef",
    "GetVpnTunnelReplacementStatusResultTypeDef",
    "GpuDeviceInfoTypeDef",
    "IamInstanceProfileAssociationTypeDef",
    "LaunchPermissionModificationsTypeDef",
    "ImageDiskContainerTypeDef",
    "SnapshotDiskContainerTypeDef",
    "ListImagesInRecycleBinResultTypeDef",
    "ImportInstanceLaunchSpecificationTypeDef",
    "InferenceDeviceInfoTypeDef",
    "InstanceAttachmentEnaSrdSpecificationTypeDef",
    "ModifyInstanceCreditSpecificationRequestRequestTypeDef",
    "ModifyInstanceMetadataOptionsResultTypeDef",
    "InstanceMonitoringTypeDef",
    "InstancePrivateIpAddressTypeDef",
    "InstanceRequirementsRequestTypeDef",
    "InstanceRequirementsTypeDef",
    "InstanceStateChangeTypeDef",
    "InstanceStatusSummaryTypeDef",
    "ModifyInstanceEventStartTimeResultTypeDef",
    "IpPermissionPaginatorTypeDef",
    "IpPermissionTypeDef",
    "StaleIpPermissionTypeDef",
    "ProvisionIpamPoolCidrRequestRequestTypeDef",
    "IpamDiscoveredAccountTypeDef",
    "IpamDiscoveredResourceCidrTypeDef",
    "IpamResourceCidrTypeDef",
    "IpamResourceDiscoveryTypeDef",
    "IpamTypeDef",
    "IpamPoolCidrTypeDef",
    "IpamPoolTypeDef",
    "IpamPublicAddressTagsTypeDef",
    "Ipv6PoolTypeDef",
    "LaunchTemplateBlockDeviceMappingRequestTypeDef",
    "LaunchTemplateBlockDeviceMappingTypeDef",
    "LaunchTemplateEnaSrdSpecificationTypeDef",
    "LaunchTemplateInstanceMarketOptionsTypeDef",
    "ListSnapshotsInRecycleBinResultTypeDef",
    "LoadPermissionModificationsTypeDef",
    "ModifyIpamRequestRequestTypeDef",
    "ModifyIpamResourceDiscoveryRequestRequestTypeDef",
    "ModifyManagedPrefixListRequestRequestTypeDef",
    "ModifyReservedInstancesRequestRequestTypeDef",
    "ReservedInstancesModificationResultTypeDef",
    "ModifyTransitGatewayRequestRequestTypeDef",
    "ModifyTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "ModifyVerifiedAccessEndpointRequestRequestTypeDef",
    "ModifyVerifiedAccessEndpointPolicyResultTypeDef",
    "ModifyVerifiedAccessGroupPolicyResultTypeDef",
    "VerifiedAccessGroupTypeDef",
    "ModifyVerifiedAccessTrustProviderRequestRequestTypeDef",
    "ModifyVpcPeeringConnectionOptionsRequestRequestTypeDef",
    "ModifyVpcPeeringConnectionOptionsResultTypeDef",
    "NatGatewayTypeDef",
    "NetworkInfoTypeDef",
    "NetworkInterfacePrivateIpAddressTypeDef",
    "NetworkInterfacePermissionTypeDef",
    "VerifiedAccessTrustProviderTypeDef",
    "PathRequestFilterTypeDef",
    "PathStatementRequestTypeDef",
    "ThroughResourcesStatementRequestTypeDef",
    "PathStatementTypeDef",
    "ThroughResourcesStatementTypeDef",
    "ReservedInstancesListingTypeDef",
    "ProvisionPublicIpv4PoolCidrResultTypeDef",
    "PublicIpv4PoolTypeDef",
    "PurchaseScheduledInstancesRequestRequestTypeDef",
    "PurchaseReservedInstancesOfferingRequestRequestTypeDef",
    "ReservedInstancesOfferingTypeDef",
    "ReservedInstancesTypeDef",
    "SecurityGroupRuleTypeDef",
    "RegisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupMembersResultTypeDef",
    "RegisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    "ScheduledInstanceAvailabilityTypeDef",
    "ScheduledInstanceTypeDef",
    "ScheduledInstancesBlockDeviceMappingTypeDef",
    "ScheduledInstancesNetworkInterfaceTypeDef",
    "SearchTransitGatewayMulticastGroupsResultTypeDef",
    "VpcEndpointTypeDef",
    "SecurityGroupRuleUpdateTypeDef",
    "ServiceConfigurationTypeDef",
    "ServiceDetailTypeDef",
    "SnapshotDetailTypeDef",
    "SnapshotTaskDetailTypeDef",
    "SpotMaintenanceStrategiesTypeDef",
    "SpotDatafeedSubscriptionTypeDef",
    "TransitGatewayMulticastDomainAssociationTypeDef",
    "TransitGatewayMulticastDomainAssociationsTypeDef",
    "SubnetIpv6CidrBlockAssociationTypeDef",
    "TargetReservationValueTypeDef",
    "TargetGroupsConfigTypeDef",
    "TrafficMirrorFilterRuleTypeDef",
    "TransitGatewayAttachmentTypeDef",
    "TransitGatewayConnectPeerConfigurationTypeDef",
    "TransitGatewayConnectTypeDef",
    "TransitGatewayMulticastDomainTypeDef",
    "TransitGatewayTypeDef",
    "TransitGatewayPeeringAttachmentTypeDef",
    "TransitGatewayPolicyRuleTypeDef",
    "TransitGatewayPrefixListReferenceTypeDef",
    "TransitGatewayRouteTypeDef",
    "TransitGatewayVpcAttachmentTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemTypeDef",
    "UnsuccessfulItemTypeDef",
    "ValidationWarningTypeDef",
    "VerifiedAccessEndpointTypeDef",
    "VerifiedAccessInstanceTypeDef",
    "VerifiedAccessLogCloudWatchLogsDestinationTypeDef",
    "VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef",
    "VerifiedAccessLogS3DestinationTypeDef",
    "VerifiedAccessLogOptionsTypeDef",
    "VolumeStatusInfoTypeDef",
    "VpcCidrBlockAssociationTypeDef",
    "VpcIpv6CidrBlockAssociationTypeDef",
    "VpcPeeringConnectionVpcInfoResponseTypeDef",
    "VpcPeeringConnectionVpcInfoTypeDef",
    "LocalGatewayRouteTableTypeDef",
    "VolumeResponseTypeDef",
    "VolumeTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "AdditionalDetailTypeDef",
    "DescribeAddressesAttributeResultTypeDef",
    "ModifyAddressAttributeResultTypeDef",
    "ResetAddressAttributeResultTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeVpcEndpointServicePermissionsResultTypeDef",
    "CreateCarrierGatewayResultTypeDef",
    "DeleteCarrierGatewayResultTypeDef",
    "DescribeCarrierGatewaysResultTypeDef",
    "CreateCoipPoolResultTypeDef",
    "DeleteCoipPoolResultTypeDef",
    "DescribeCoipPoolsResultTypeDef",
    "CreateCustomerGatewayResultTypeDef",
    "DescribeCustomerGatewaysResultTypeDef",
    "CreateInstanceConnectEndpointResultTypeDef",
    "DeleteInstanceConnectEndpointResultTypeDef",
    "DescribeInstanceConnectEndpointsResultTypeDef",
    "DescribeHostReservationsResultTypeDef",
    "AssociateInstanceEventWindowRequestRequestTypeDef",
    "InstanceEventWindowTypeDef",
    "DisassociateInstanceEventWindowRequestRequestTypeDef",
    "AssociateIpamResourceDiscoveryResultTypeDef",
    "DescribeIpamResourceDiscoveryAssociationsResultTypeDef",
    "DisassociateIpamResourceDiscoveryResultTypeDef",
    "CreateIpamScopeResultTypeDef",
    "DeleteIpamScopeResultTypeDef",
    "DescribeIpamScopesResultTypeDef",
    "ModifyIpamScopeResultTypeDef",
    "DescribeKeyPairsResultTypeDef",
    "DeleteLaunchTemplateResultTypeDef",
    "DescribeLaunchTemplatesResultTypeDef",
    "ModifyLaunchTemplateResultTypeDef",
    "CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef",
    "DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef",
    "CreateLocalGatewayRouteTableVpcAssociationResultTypeDef",
    "DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef",
    "DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef",
    "DescribeLocalGatewaysResultTypeDef",
    "DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef",
    "DescribeLocalGatewayVirtualInterfacesResultTypeDef",
    "CreateManagedPrefixListResultTypeDef",
    "DeleteManagedPrefixListResultTypeDef",
    "DescribeManagedPrefixListsResultTypeDef",
    "ModifyManagedPrefixListResultTypeDef",
    "RestoreManagedPrefixListVersionResultTypeDef",
    "DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef",
    "StartNetworkInsightsAccessScopeAnalysisResultTypeDef",
    "DescribeNetworkInsightsAccessScopesResultTypeDef",
    "CreatePlacementGroupResultTypeDef",
    "DescribePlacementGroupsResultTypeDef",
    "CreateReplaceRootVolumeTaskResultTypeDef",
    "DescribeReplaceRootVolumeTasksResultTypeDef",
    "GetSecurityGroupsForVpcResultTypeDef",
    "CreateSnapshotsResultTypeDef",
    "DescribeSnapshotTierStatusResultTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "CreateSubnetCidrReservationResultTypeDef",
    "DeleteSubnetCidrReservationResultTypeDef",
    "GetSubnetCidrReservationsResultTypeDef",
    "AcceptAddressTransferRequestRequestTypeDef",
    "AllocateAddressRequestRequestTypeDef",
    "AllocateHostsRequestRequestTypeDef",
    "AssociateIpamResourceDiscoveryRequestRequestTypeDef",
    "CopySnapshotRequestRequestTypeDef",
    "CopySnapshotRequestSnapshotCopyTypeDef",
    "CreateCapacityReservationFleetRequestRequestTypeDef",
    "CreateCapacityReservationRequestRequestTypeDef",
    "CreateCarrierGatewayRequestRequestTypeDef",
    "CreateCoipPoolRequestRequestTypeDef",
    "CreateCustomerGatewayRequestRequestTypeDef",
    "CreateDhcpOptionsRequestRequestTypeDef",
    "CreateDhcpOptionsRequestServiceResourceCreateDhcpOptionsTypeDef",
    "CreateEgressOnlyInternetGatewayRequestRequestTypeDef",
    "CreateFlowLogsRequestRequestTypeDef",
    "CreateFpgaImageRequestRequestTypeDef",
    "CreateInstanceConnectEndpointRequestRequestTypeDef",
    "CreateInstanceEventWindowRequestRequestTypeDef",
    "CreateInstanceExportTaskRequestRequestTypeDef",
    "CreateInternetGatewayRequestRequestTypeDef",
    "CreateInternetGatewayRequestServiceResourceCreateInternetGatewayTypeDef",
    "CreateIpamPoolRequestRequestTypeDef",
    "CreateIpamRequestRequestTypeDef",
    "CreateIpamResourceDiscoveryRequestRequestTypeDef",
    "CreateIpamScopeRequestRequestTypeDef",
    "CreateKeyPairRequestRequestTypeDef",
    "CreateKeyPairRequestServiceResourceCreateKeyPairTypeDef",
    "CreateLocalGatewayRouteTableRequestRequestTypeDef",
    "CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef",
    "CreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    "CreateManagedPrefixListRequestRequestTypeDef",
    "CreateNatGatewayRequestRequestTypeDef",
    "CreateNetworkAclRequestRequestTypeDef",
    "CreateNetworkAclRequestServiceResourceCreateNetworkAclTypeDef",
    "CreateNetworkAclRequestVpcCreateNetworkAclTypeDef",
    "CreateNetworkInterfaceRequestRequestTypeDef",
    "CreateNetworkInterfaceRequestServiceResourceCreateNetworkInterfaceTypeDef",
    "CreateNetworkInterfaceRequestSubnetCreateNetworkInterfaceTypeDef",
    "CreatePlacementGroupRequestRequestTypeDef",
    "CreatePlacementGroupRequestServiceResourceCreatePlacementGroupTypeDef",
    "CreatePublicIpv4PoolRequestRequestTypeDef",
    "CreateReplaceRootVolumeTaskRequestRequestTypeDef",
    "CreateRestoreImageTaskRequestRequestTypeDef",
    "CreateRouteTableRequestRequestTypeDef",
    "CreateRouteTableRequestServiceResourceCreateRouteTableTypeDef",
    "CreateRouteTableRequestVpcCreateRouteTableTypeDef",
    "CreateSecurityGroupRequestRequestTypeDef",
    "CreateSecurityGroupRequestServiceResourceCreateSecurityGroupTypeDef",
    "CreateSecurityGroupRequestVpcCreateSecurityGroupTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotRequestServiceResourceCreateSnapshotTypeDef",
    "CreateSnapshotRequestVolumeCreateSnapshotTypeDef",
    "CreateSnapshotsRequestRequestTypeDef",
    "CreateSubnetCidrReservationRequestRequestTypeDef",
    "CreateSubnetRequestRequestTypeDef",
    "CreateSubnetRequestServiceResourceCreateSubnetTypeDef",
    "CreateSubnetRequestVpcCreateSubnetTypeDef",
    "CreateTrafficMirrorFilterRequestRequestTypeDef",
    "CreateTrafficMirrorSessionRequestRequestTypeDef",
    "CreateTrafficMirrorTargetRequestRequestTypeDef",
    "CreateTransitGatewayConnectPeerRequestRequestTypeDef",
    "CreateTransitGatewayConnectRequestRequestTypeDef",
    "CreateTransitGatewayMulticastDomainRequestRequestTypeDef",
    "CreateTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "CreateTransitGatewayPolicyTableRequestRequestTypeDef",
    "CreateTransitGatewayRequestRequestTypeDef",
    "CreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef",
    "CreateTransitGatewayRouteTableRequestRequestTypeDef",
    "CreateTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "CreateVerifiedAccessEndpointRequestRequestTypeDef",
    "CreateVerifiedAccessGroupRequestRequestTypeDef",
    "CreateVerifiedAccessInstanceRequestRequestTypeDef",
    "CreateVerifiedAccessTrustProviderRequestRequestTypeDef",
    "CreateVolumeRequestRequestTypeDef",
    "CreateVolumeRequestServiceResourceCreateVolumeTypeDef",
    "CreateVpcEndpointRequestRequestTypeDef",
    "CreateVpcEndpointServiceConfigurationRequestRequestTypeDef",
    "CreateVpcPeeringConnectionRequestRequestTypeDef",
    "CreateVpcPeeringConnectionRequestServiceResourceCreateVpcPeeringConnectionTypeDef",
    "CreateVpcPeeringConnectionRequestVpcRequestVpcPeeringConnectionTypeDef",
    "CreateVpcRequestRequestTypeDef",
    "CreateVpcRequestServiceResourceCreateVpcTypeDef",
    "CreateVpnGatewayRequestRequestTypeDef",
    "ExportImageRequestRequestTypeDef",
    "ImportKeyPairRequestRequestTypeDef",
    "ImportKeyPairRequestServiceResourceImportKeyPairTypeDef",
    "ProvisionByoipCidrRequestRequestTypeDef",
    "PurchaseCapacityBlockRequestRequestTypeDef",
    "PurchaseHostReservationRequestRequestTypeDef",
    "StartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    "StartNetworkInsightsAnalysisRequestRequestTypeDef",
    "CreateTrafficMirrorSessionResultTypeDef",
    "DescribeTrafficMirrorSessionsResultTypeDef",
    "ModifyTrafficMirrorSessionResultTypeDef",
    "CreateTrafficMirrorTargetResultTypeDef",
    "DescribeTrafficMirrorTargetsResultTypeDef",
    "CreateTransitGatewayPolicyTableResultTypeDef",
    "DeleteTransitGatewayPolicyTableResultTypeDef",
    "DescribeTransitGatewayPolicyTablesResultTypeDef",
    "CreateTransitGatewayRouteTableAnnouncementResultTypeDef",
    "DeleteTransitGatewayRouteTableAnnouncementResultTypeDef",
    "DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef",
    "CreateTransitGatewayRouteTableResultTypeDef",
    "DeleteTransitGatewayRouteTableResultTypeDef",
    "DescribeTransitGatewayRouteTablesResultTypeDef",
    "AssociateTrunkInterfaceResultTypeDef",
    "DescribeTrunkInterfaceAssociationsResultTypeDef",
    "DescribeVpcClassicLinkResultTypeDef",
    "ExplanationTypeDef",
    "AdvertiseByoipCidrResultTypeDef",
    "DeprovisionByoipCidrResultTypeDef",
    "DescribeByoipCidrsResultTypeDef",
    "MoveByoipCidrToIpamResultTypeDef",
    "ProvisionByoipCidrResultTypeDef",
    "WithdrawByoipCidrResultTypeDef",
    "DescribeClientVpnTargetNetworksResultTypeDef",
    "RouteTableTypeDef",
    "IntegrateServicesTypeDef",
    "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
    "DescribeScheduledInstanceAvailabilityRequestDescribeScheduledInstanceAvailabilityPaginateTypeDef",
    "DescribeScheduledInstanceAvailabilityRequestRequestTypeDef",
    "DescribeScheduledInstancesRequestDescribeScheduledInstancesPaginateTypeDef",
    "DescribeScheduledInstancesRequestRequestTypeDef",
    "InstanceMarketOptionsRequestTypeDef",
    "CreateVpnGatewayResultTypeDef",
    "DescribeVpnGatewaysResultTypeDef",
    "NetworkInterfaceAttachmentResponseTypeDef",
    "NetworkInterfaceAttachmentTypeDef",
    "DhcpOptionsTypeDef",
    "DescribeClientVpnAuthorizationRulesResultTypeDef",
    "DescribeAvailabilityZonesResultTypeDef",
    "HostTypeDef",
    "StorageTypeDef",
    "CreateImageRequestInstanceCreateImageTypeDef",
    "CreateImageRequestRequestTypeDef",
    "ImageAttributeTypeDef",
    "ImageTypeDef",
    "RegisterImageRequestRequestTypeDef",
    "RegisterImageRequestServiceResourceRegisterImageTypeDef",
    "CancelCapacityReservationFleetsResultTypeDef",
    "CancelSpotFleetRequestsResponseTypeDef",
    "CreateCapacityReservationResultTypeDef",
    "DescribeCapacityReservationsResultTypeDef",
    "PurchaseCapacityBlockResultTypeDef",
    "DescribeCapacityReservationFleetsResultTypeDef",
    "ModifyInstanceCapacityReservationAttributesRequestRequestTypeDef",
    "DescribeClassicLinkInstancesResultTypeDef",
    "CreateClientVpnEndpointRequestRequestTypeDef",
    "ClientVpnEndpointTypeDef",
    "DescribeClientVpnConnectionsResultTypeDef",
    "TerminateClientVpnConnectionsResultTypeDef",
    "DescribeClientVpnRoutesResultTypeDef",
    "ModifyVpnTunnelOptionsSpecificationTypeDef",
    "VpnTunnelOptionsSpecificationTypeDef",
    "TunnelOptionTypeDef",
    "NetworkAclTypeDef",
    "ModifySnapshotAttributeRequestRequestTypeDef",
    "ModifySnapshotAttributeRequestSnapshotModifyAttributeTypeDef",
    "GetAwsNetworkPerformanceDataResultTypeDef",
    "DeleteFleetsResultTypeDef",
    "DeleteLaunchTemplateVersionsResultTypeDef",
    "DeleteQueuedReservedInstancesResultTypeDef",
    "DescribePrincipalIdFormatResultTypeDef",
    "DescribeFastLaunchImagesResultTypeDef",
    "DescribeFlowLogsResultTypeDef",
    "DisableFastSnapshotRestoreErrorItemTypeDef",
    "ImportInstanceTaskDetailsTypeDef",
    "DescribeVpcEndpointConnectionsResultTypeDef",
    "ModifyInstanceAttributeRequestInstanceModifyAttributeTypeDef",
    "ModifyInstanceAttributeRequestRequestTypeDef",
    "InstanceAttributeTypeDef",
    "CreateEgressOnlyInternetGatewayResultTypeDef",
    "DescribeEgressOnlyInternetGatewaysResultTypeDef",
    "CreateInternetGatewayResultTypeDef",
    "DescribeInternetGatewaysResultTypeDef",
    "DescribeElasticGpusResultTypeDef",
    "InstanceNetworkInterfaceSpecificationServiceResourceTypeDef",
    "InstanceNetworkInterfaceSpecificationSubnetTypeDef",
    "InstanceNetworkInterfaceSpecificationTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef",
    "AttachNetworkInterfaceRequestNetworkInterfaceAttachTypeDef",
    "AttachNetworkInterfaceRequestRequestTypeDef",
    "ModifyNetworkInterfaceAttributeRequestNetworkInterfaceModifyAttributeTypeDef",
    "ModifyNetworkInterfaceAttributeRequestRequestTypeDef",
    "EnableFastSnapshotRestoreErrorItemTypeDef",
    "DescribeFleetHistoryResultTypeDef",
    "DescribeSpotFleetRequestHistoryResponseTypeDef",
    "DescribeExportImageTasksResultTypeDef",
    "CreateInstanceExportTaskResultTypeDef",
    "DescribeExportTasksResultTypeDef",
    "NetworkInsightsPathTypeDef",
    "SpotOptionsRequestTypeDef",
    "SpotOptionsTypeDef",
    "FpgaInfoTypeDef",
    "DescribeFpgaImageAttributeResultTypeDef",
    "ModifyFpgaImageAttributeResultTypeDef",
    "DescribeFpgaImagesResultTypeDef",
    "GpuInfoTypeDef",
    "AssociateIamInstanceProfileResultTypeDef",
    "DescribeIamInstanceProfileAssociationsResultTypeDef",
    "DisassociateIamInstanceProfileResultTypeDef",
    "ReplaceIamInstanceProfileAssociationResultTypeDef",
    "ModifyImageAttributeRequestImageModifyAttributeTypeDef",
    "ModifyImageAttributeRequestRequestTypeDef",
    "ImportImageRequestRequestTypeDef",
    "ImportSnapshotRequestRequestTypeDef",
    "ImportInstanceRequestRequestTypeDef",
    "InferenceAcceleratorInfoTypeDef",
    "InstanceNetworkInterfaceAttachmentTypeDef",
    "MonitorInstancesResultTypeDef",
    "UnmonitorInstancesResultTypeDef",
    "FleetLaunchTemplateOverridesRequestTypeDef",
    "GetInstanceTypesFromInstanceRequirementsRequestGetInstanceTypesFromInstanceRequirementsPaginateTypeDef",
    "GetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef",
    "InstanceRequirementsWithMetadataRequestTypeDef",
    "FleetLaunchTemplateOverridesTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "StartInstancesResultTypeDef",
    "StopInstancesResultTypeDef",
    "TerminateInstancesResultTypeDef",
    "InstanceStatusTypeDef",
    "SecurityGroupPaginatorTypeDef",
    "AuthorizeSecurityGroupEgressRequestRequestTypeDef",
    "AuthorizeSecurityGroupEgressRequestSecurityGroupAuthorizeEgressTypeDef",
    "AuthorizeSecurityGroupIngressRequestRequestTypeDef",
    "AuthorizeSecurityGroupIngressRequestSecurityGroupAuthorizeIngressTypeDef",
    "RevokeSecurityGroupEgressRequestRequestTypeDef",
    "RevokeSecurityGroupEgressRequestSecurityGroupRevokeEgressTypeDef",
    "RevokeSecurityGroupEgressResultTypeDef",
    "RevokeSecurityGroupIngressRequestRequestTypeDef",
    "RevokeSecurityGroupIngressRequestSecurityGroupRevokeIngressTypeDef",
    "RevokeSecurityGroupIngressResultTypeDef",
    "SecurityGroupTypeDef",
    "UpdateSecurityGroupRuleDescriptionsEgressRequestRequestTypeDef",
    "UpdateSecurityGroupRuleDescriptionsIngressRequestRequestTypeDef",
    "StaleSecurityGroupTypeDef",
    "GetIpamDiscoveredAccountsResultTypeDef",
    "GetIpamDiscoveredResourceCidrsResultTypeDef",
    "GetIpamResourceCidrsResultTypeDef",
    "ModifyIpamResourceCidrResultTypeDef",
    "CreateIpamResourceDiscoveryResultTypeDef",
    "DeleteIpamResourceDiscoveryResultTypeDef",
    "DescribeIpamResourceDiscoveriesResultTypeDef",
    "ModifyIpamResourceDiscoveryResultTypeDef",
    "CreateIpamResultTypeDef",
    "DeleteIpamResultTypeDef",
    "DescribeIpamsResultTypeDef",
    "ModifyIpamResultTypeDef",
    "DeprovisionIpamPoolCidrResultTypeDef",
    "GetIpamPoolCidrsResultTypeDef",
    "ProvisionIpamPoolCidrResultTypeDef",
    "CreateIpamPoolResultTypeDef",
    "DeleteIpamPoolResultTypeDef",
    "DescribeIpamPoolsResultTypeDef",
    "ModifyIpamPoolResultTypeDef",
    "IpamDiscoveredPublicAddressTypeDef",
    "DescribeIpv6PoolsResultTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef",
    "ModifyFpgaImageAttributeRequestRequestTypeDef",
    "ReservedInstancesModificationTypeDef",
    "CreateVerifiedAccessGroupResultTypeDef",
    "DeleteVerifiedAccessGroupResultTypeDef",
    "DescribeVerifiedAccessGroupsResultTypeDef",
    "ModifyVerifiedAccessGroupResultTypeDef",
    "CreateNatGatewayResultTypeDef",
    "DescribeNatGatewaysResultTypeDef",
    "CreateNetworkInterfacePermissionResultTypeDef",
    "DescribeNetworkInterfacePermissionsResultTypeDef",
    "CreateVerifiedAccessTrustProviderResultTypeDef",
    "DeleteVerifiedAccessTrustProviderResultTypeDef",
    "DescribeVerifiedAccessTrustProvidersResultTypeDef",
    "ModifyVerifiedAccessTrustProviderResultTypeDef",
    "CreateNetworkInsightsPathRequestRequestTypeDef",
    "AccessScopePathRequestTypeDef",
    "AccessScopePathTypeDef",
    "CancelReservedInstancesListingResultTypeDef",
    "CreateReservedInstancesListingResultTypeDef",
    "DescribeReservedInstancesListingsResultTypeDef",
    "DescribePublicIpv4PoolsResultTypeDef",
    "DescribeReservedInstancesOfferingsResultTypeDef",
    "DescribeReservedInstancesResultTypeDef",
    "AuthorizeSecurityGroupEgressResultTypeDef",
    "AuthorizeSecurityGroupIngressResultTypeDef",
    "DescribeSecurityGroupRulesResultTypeDef",
    "DescribeScheduledInstanceAvailabilityResultTypeDef",
    "DescribeScheduledInstancesResultTypeDef",
    "PurchaseScheduledInstancesResultTypeDef",
    "ScheduledInstancesLaunchSpecificationTypeDef",
    "CreateVpcEndpointResultTypeDef",
    "DescribeVpcEndpointsResultTypeDef",
    "ModifySecurityGroupRulesRequestRequestTypeDef",
    "CreateVpcEndpointServiceConfigurationResultTypeDef",
    "DescribeVpcEndpointServiceConfigurationsResultTypeDef",
    "DescribeVpcEndpointServicesResultTypeDef",
    "ImportImageResultTypeDef",
    "ImportImageTaskTypeDef",
    "ImportSnapshotResultTypeDef",
    "ImportSnapshotTaskTypeDef",
    "CreateSpotDatafeedSubscriptionResultTypeDef",
    "DescribeSpotDatafeedSubscriptionResultTypeDef",
    "GetTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "AssociateTransitGatewayMulticastDomainResultTypeDef",
    "DisassociateTransitGatewayMulticastDomainResultTypeDef",
    "RejectTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "AssociateSubnetCidrBlockResultTypeDef",
    "DisassociateSubnetCidrBlockResultTypeDef",
    "SubnetTypeDef",
    "GetReservedInstancesExchangeQuoteResultTypeDef",
    "LoadBalancersConfigTypeDef",
    "CreateTrafficMirrorFilterRuleResultTypeDef",
    "ModifyTrafficMirrorFilterRuleResultTypeDef",
    "TrafficMirrorFilterTypeDef",
    "DescribeTransitGatewayAttachmentsResultTypeDef",
    "TransitGatewayConnectPeerTypeDef",
    "CreateTransitGatewayConnectResultTypeDef",
    "DeleteTransitGatewayConnectResultTypeDef",
    "DescribeTransitGatewayConnectsResultTypeDef",
    "CreateTransitGatewayMulticastDomainResultTypeDef",
    "DeleteTransitGatewayMulticastDomainResultTypeDef",
    "DescribeTransitGatewayMulticastDomainsResultTypeDef",
    "CreateTransitGatewayResultTypeDef",
    "DeleteTransitGatewayResultTypeDef",
    "DescribeTransitGatewaysResultTypeDef",
    "ModifyTransitGatewayResultTypeDef",
    "AcceptTransitGatewayPeeringAttachmentResultTypeDef",
    "CreateTransitGatewayPeeringAttachmentResultTypeDef",
    "DeleteTransitGatewayPeeringAttachmentResultTypeDef",
    "DescribeTransitGatewayPeeringAttachmentsResultTypeDef",
    "RejectTransitGatewayPeeringAttachmentResultTypeDef",
    "TransitGatewayPolicyTableEntryTypeDef",
    "CreateTransitGatewayPrefixListReferenceResultTypeDef",
    "DeleteTransitGatewayPrefixListReferenceResultTypeDef",
    "GetTransitGatewayPrefixListReferencesResultTypeDef",
    "ModifyTransitGatewayPrefixListReferenceResultTypeDef",
    "CreateTransitGatewayRouteResultTypeDef",
    "DeleteTransitGatewayRouteResultTypeDef",
    "ReplaceTransitGatewayRouteResultTypeDef",
    "SearchTransitGatewayRoutesResultTypeDef",
    "AcceptTransitGatewayVpcAttachmentResultTypeDef",
    "CreateTransitGatewayVpcAttachmentResultTypeDef",
    "DeleteTransitGatewayVpcAttachmentResultTypeDef",
    "DescribeTransitGatewayVpcAttachmentsResultTypeDef",
    "ModifyTransitGatewayVpcAttachmentResultTypeDef",
    "RejectTransitGatewayVpcAttachmentResultTypeDef",
    "ModifyInstanceCreditSpecificationResultTypeDef",
    "AcceptVpcEndpointConnectionsResultTypeDef",
    "CreateFlowLogsResultTypeDef",
    "DeleteFlowLogsResultTypeDef",
    "DeleteVpcEndpointConnectionNotificationsResultTypeDef",
    "DeleteVpcEndpointServiceConfigurationsResultTypeDef",
    "DeleteVpcEndpointsResultTypeDef",
    "ModifyHostsResultTypeDef",
    "RejectVpcEndpointConnectionsResultTypeDef",
    "ReleaseHostsResultTypeDef",
    "CreateLaunchTemplateResultTypeDef",
    "CreateVerifiedAccessEndpointResultTypeDef",
    "DeleteVerifiedAccessEndpointResultTypeDef",
    "DescribeVerifiedAccessEndpointsResultTypeDef",
    "ModifyVerifiedAccessEndpointResultTypeDef",
    "AttachVerifiedAccessTrustProviderResultTypeDef",
    "CreateVerifiedAccessInstanceResultTypeDef",
    "DeleteVerifiedAccessInstanceResultTypeDef",
    "DescribeVerifiedAccessInstancesResultTypeDef",
    "DetachVerifiedAccessTrustProviderResultTypeDef",
    "ModifyVerifiedAccessInstanceResultTypeDef",
    "VerifiedAccessLogsTypeDef",
    "ModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef",
    "VolumeStatusItemTypeDef",
    "AssociateVpcCidrBlockResultTypeDef",
    "DisassociateVpcCidrBlockResultTypeDef",
    "VpcTypeDef",
    "VpcPeeringConnectionTypeDef",
    "CreateLocalGatewayRouteTableResultTypeDef",
    "DeleteLocalGatewayRouteTableResultTypeDef",
    "DescribeLocalGatewayRouteTablesResultTypeDef",
    "DescribeVolumesResultTypeDef",
    "AssociateInstanceEventWindowResultTypeDef",
    "CreateInstanceEventWindowResultTypeDef",
    "DescribeInstanceEventWindowsResultTypeDef",
    "DisassociateInstanceEventWindowResultTypeDef",
    "ModifyInstanceEventWindowResultTypeDef",
    "PathComponentTypeDef",
    "CreateRouteTableResultTypeDef",
    "DescribeRouteTablesResultTypeDef",
    "GetFlowLogsIntegrationTemplateRequestRequestTypeDef",
    "DescribeNetworkInterfaceAttributeResultTypeDef",
    "NetworkInterfaceTypeDef",
    "CreateDhcpOptionsResultTypeDef",
    "DescribeDhcpOptionsResultTypeDef",
    "DescribeHostsResultTypeDef",
    "BundleInstanceRequestRequestTypeDef",
    "BundleTaskTypeDef",
    "DescribeImagesResultTypeDef",
    "DescribeClientVpnEndpointsResultTypeDef",
    "ModifyVpnTunnelOptionsRequestRequestTypeDef",
    "VpnConnectionOptionsSpecificationTypeDef",
    "VpnConnectionOptionsTypeDef",
    "CreateNetworkAclResultTypeDef",
    "DescribeNetworkAclsResultTypeDef",
    "DisableFastSnapshotRestoresResultTypeDef",
    "ConversionTaskTypeDef",
    "RunInstancesRequestServiceResourceCreateInstancesTypeDef",
    "RunInstancesRequestSubnetCreateInstancesTypeDef",
    "LaunchSpecificationTypeDef",
    "RequestSpotLaunchSpecificationTypeDef",
    "RunInstancesRequestRequestTypeDef",
    "SpotFleetLaunchSpecificationTypeDef",
    "RequestLaunchTemplateDataTypeDef",
    "EnableFastSnapshotRestoresResultTypeDef",
    "CreateNetworkInsightsPathResultTypeDef",
    "DescribeNetworkInsightsPathsResultTypeDef",
    "InstanceTypeInfoTypeDef",
    "InstanceNetworkInterfaceTypeDef",
    "FleetLaunchTemplateConfigRequestTypeDef",
    "GetSpotPlacementScoresRequestGetSpotPlacementScoresPaginateTypeDef",
    "GetSpotPlacementScoresRequestRequestTypeDef",
    "FleetLaunchTemplateConfigTypeDef",
    "LaunchTemplateAndOverridesResponseTypeDef",
    "LaunchTemplateConfigTypeDef",
    "DescribeInstanceStatusResultTypeDef",
    "DescribeSecurityGroupsResultPaginatorTypeDef",
    "DescribeSecurityGroupsResultTypeDef",
    "DescribeStaleSecurityGroupsResultTypeDef",
    "GetIpamDiscoveredPublicAddressesResultTypeDef",
    "ResponseLaunchTemplateDataTypeDef",
    "DescribeReservedInstancesModificationsResultTypeDef",
    "CreateNetworkInsightsAccessScopeRequestRequestTypeDef",
    "NetworkInsightsAccessScopeContentTypeDef",
    "RunScheduledInstancesRequestRequestTypeDef",
    "DescribeImportImageTasksResultTypeDef",
    "DescribeImportSnapshotTasksResultTypeDef",
    "CreateDefaultSubnetResultTypeDef",
    "CreateSubnetResultTypeDef",
    "DescribeSubnetsResultTypeDef",
    "CreateTrafficMirrorFilterResultTypeDef",
    "DescribeTrafficMirrorFiltersResultTypeDef",
    "ModifyTrafficMirrorFilterNetworkServicesResultTypeDef",
    "CreateTransitGatewayConnectPeerResultTypeDef",
    "DeleteTransitGatewayConnectPeerResultTypeDef",
    "DescribeTransitGatewayConnectPeersResultTypeDef",
    "GetTransitGatewayPolicyTableEntriesResultTypeDef",
    "VerifiedAccessInstanceLoggingConfigurationTypeDef",
    "DescribeVolumeStatusResultTypeDef",
    "CreateDefaultVpcResultTypeDef",
    "CreateVpcResultTypeDef",
    "DescribeVpcsResultTypeDef",
    "AcceptVpcPeeringConnectionResultTypeDef",
    "CreateVpcPeeringConnectionResultTypeDef",
    "DescribeVpcPeeringConnectionsResultTypeDef",
    "AccessScopeAnalysisFindingTypeDef",
    "NetworkInsightsAnalysisTypeDef",
    "CreateNetworkInterfaceResultTypeDef",
    "DescribeNetworkInterfacesResultTypeDef",
    "BundleInstanceResultTypeDef",
    "CancelBundleTaskResultTypeDef",
    "DescribeBundleTasksResultTypeDef",
    "CreateVpnConnectionRequestRequestTypeDef",
    "VpnConnectionTypeDef",
    "DescribeConversionTasksResultTypeDef",
    "ImportInstanceResultTypeDef",
    "ImportVolumeResultTypeDef",
    "SpotInstanceRequestTypeDef",
    "RequestSpotInstancesRequestRequestTypeDef",
    "CreateLaunchTemplateRequestRequestTypeDef",
    "CreateLaunchTemplateVersionRequestRequestTypeDef",
    "DescribeInstanceTypesResultTypeDef",
    "InstanceTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "ModifyFleetRequestRequestTypeDef",
    "CreateFleetErrorTypeDef",
    "CreateFleetInstanceTypeDef",
    "DescribeFleetErrorTypeDef",
    "DescribeFleetsInstancesTypeDef",
    "ModifySpotFleetRequestRequestRequestTypeDef",
    "SpotFleetRequestConfigDataPaginatorTypeDef",
    "SpotFleetRequestConfigDataTypeDef",
    "GetLaunchTemplateDataResultTypeDef",
    "LaunchTemplateVersionTypeDef",
    "CreateNetworkInsightsAccessScopeResultTypeDef",
    "GetNetworkInsightsAccessScopeContentResultTypeDef",
    "DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef",
    "ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef",
    "GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef",
    "DescribeNetworkInsightsAnalysesResultTypeDef",
    "StartNetworkInsightsAnalysisResultTypeDef",
    "CreateVpnConnectionResultTypeDef",
    "DescribeVpnConnectionsResultTypeDef",
    "ModifyVpnConnectionOptionsResultTypeDef",
    "ModifyVpnConnectionResultTypeDef",
    "ModifyVpnTunnelCertificateResultTypeDef",
    "ModifyVpnTunnelOptionsResultTypeDef",
    "DescribeSpotInstanceRequestsResultTypeDef",
    "RequestSpotInstancesResultTypeDef",
    "ReservationResponseTypeDef",
    "ReservationTypeDef",
    "CreateFleetResultTypeDef",
    "FleetDataTypeDef",
    "SpotFleetRequestConfigPaginatorTypeDef",
    "RequestSpotFleetRequestRequestTypeDef",
    "SpotFleetRequestConfigTypeDef",
    "CreateLaunchTemplateVersionResultTypeDef",
    "DescribeLaunchTemplateVersionsResultTypeDef",
    "DescribeInstancesResultTypeDef",
    "DescribeFleetsResultTypeDef",
    "DescribeSpotFleetRequestsResponsePaginatorTypeDef",
    "DescribeSpotFleetRequestsResponseTypeDef",
)

AcceleratorCountRequestTypeDef = TypedDict(
    "AcceleratorCountRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
AcceleratorCountTypeDef = TypedDict(
    "AcceleratorCountTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
AcceleratorTotalMemoryMiBRequestTypeDef = TypedDict(
    "AcceleratorTotalMemoryMiBRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
AcceleratorTotalMemoryMiBTypeDef = TypedDict(
    "AcceleratorTotalMemoryMiBTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
AddressTransferTypeDef = TypedDict(
    "AddressTransferTypeDef",
    {
        "PublicIp": NotRequired[str],
        "AllocationId": NotRequired[str],
        "TransferAccountId": NotRequired[str],
        "TransferOfferExpirationTimestamp": NotRequired[datetime],
        "TransferOfferAcceptedTimestamp": NotRequired[datetime],
        "AddressTransferStatus": NotRequired[AddressTransferStatusType],
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
TargetConfigurationRequestTypeDef = TypedDict(
    "TargetConfigurationRequestTypeDef",
    {
        "OfferingId": str,
        "InstanceCount": NotRequired[int],
    },
)
AcceptTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef = TypedDict(
    "AcceptTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
AcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "AcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)
AcceptTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "AcceptTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)
AcceptVpcEndpointConnectionsRequestRequestTypeDef = TypedDict(
    "AcceptVpcEndpointConnectionsRequestRequestTypeDef",
    {
        "ServiceId": str,
        "VpcEndpointIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
AcceptVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionRequestRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
        "DryRun": NotRequired[bool],
    },
)
AcceptVpcPeeringConnectionRequestVpcPeeringConnectionAcceptTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionRequestVpcPeeringConnectionAcceptTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
AccountAttributeValueTypeDef = TypedDict(
    "AccountAttributeValueTypeDef",
    {
        "AttributeValue": NotRequired[str],
    },
)
ActiveInstanceTypeDef = TypedDict(
    "ActiveInstanceTypeDef",
    {
        "InstanceId": NotRequired[str],
        "InstanceType": NotRequired[str],
        "SpotInstanceRequestId": NotRequired[str],
        "InstanceHealth": NotRequired[InstanceHealthStatusType],
    },
)
AddIpamOperatingRegionTypeDef = TypedDict(
    "AddIpamOperatingRegionTypeDef",
    {
        "RegionName": NotRequired[str],
    },
)
AddPrefixListEntryTypeDef = TypedDict(
    "AddPrefixListEntryTypeDef",
    {
        "Cidr": str,
        "Description": NotRequired[str],
    },
)
AddedPrincipalTypeDef = TypedDict(
    "AddedPrincipalTypeDef",
    {
        "PrincipalType": NotRequired[PrincipalTypeType],
        "Principal": NotRequired[str],
        "ServicePermissionId": NotRequired[str],
        "ServiceId": NotRequired[str],
    },
)
AnalysisComponentTypeDef = TypedDict(
    "AnalysisComponentTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
RuleGroupTypePairTypeDef = TypedDict(
    "RuleGroupTypePairTypeDef",
    {
        "RuleGroupArn": NotRequired[str],
        "RuleGroupType": NotRequired[str],
    },
)
RuleOptionTypeDef = TypedDict(
    "RuleOptionTypeDef",
    {
        "Keyword": NotRequired[str],
        "Settings": NotRequired[List[str]],
    },
)
PtrUpdateStatusTypeDef = TypedDict(
    "PtrUpdateStatusTypeDef",
    {
        "Value": NotRequired[str],
        "Status": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AdvertiseByoipCidrRequestRequestTypeDef = TypedDict(
    "AdvertiseByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "Asn": NotRequired[str],
        "DryRun": NotRequired[bool],
        "NetworkBorderGroup": NotRequired[str],
    },
)
AllocateIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "AllocateIpamPoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Cidr": NotRequired[str],
        "NetmaskLength": NotRequired[int],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "PreviewNextCidr": NotRequired[bool],
        "AllowedCidrs": NotRequired[Sequence[str]],
        "DisallowedCidrs": NotRequired[Sequence[str]],
    },
)
IpamPoolAllocationTypeDef = TypedDict(
    "IpamPoolAllocationTypeDef",
    {
        "Cidr": NotRequired[str],
        "IpamPoolAllocationId": NotRequired[str],
        "Description": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[IpamPoolAllocationResourceTypeType],
        "ResourceRegion": NotRequired[str],
        "ResourceOwner": NotRequired[str],
    },
)
AlternatePathHintTypeDef = TypedDict(
    "AlternatePathHintTypeDef",
    {
        "ComponentId": NotRequired[str],
        "ComponentArn": NotRequired[str],
    },
)
PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "From": NotRequired[int],
        "To": NotRequired[int],
    },
)
AnalysisLoadBalancerListenerTypeDef = TypedDict(
    "AnalysisLoadBalancerListenerTypeDef",
    {
        "LoadBalancerPort": NotRequired[int],
        "InstancePort": NotRequired[int],
    },
)
AnalysisRouteTableRouteTypeDef = TypedDict(
    "AnalysisRouteTableRouteTypeDef",
    {
        "DestinationCidr": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "NatGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "Origin": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "State": NotRequired[str],
        "CarrierGatewayId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
    },
)
ApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "ApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "VpcId": str,
        "SecurityGroupIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
AsnAssociationTypeDef = TypedDict(
    "AsnAssociationTypeDef",
    {
        "Asn": NotRequired[str],
        "Cidr": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "State": NotRequired[AsnAssociationStateType],
    },
)
AsnAuthorizationContextTypeDef = TypedDict(
    "AsnAuthorizationContextTypeDef",
    {
        "Message": str,
        "Signature": str,
    },
)
AssignIpv6AddressesRequestRequestTypeDef = TypedDict(
    "AssignIpv6AddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[str]],
        "Ipv6PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence[str]],
    },
)
AssignPrivateIpAddressesRequestNetworkInterfaceAssignPrivateIpAddressesTypeDef = TypedDict(
    "AssignPrivateIpAddressesRequestNetworkInterfaceAssignPrivateIpAddressesTypeDef",
    {
        "AllowReassignment": NotRequired[bool],
        "PrivateIpAddresses": NotRequired[Sequence[str]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence[str]],
        "Ipv4PrefixCount": NotRequired[int],
    },
)
AssignPrivateIpAddressesRequestRequestTypeDef = TypedDict(
    "AssignPrivateIpAddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "AllowReassignment": NotRequired[bool],
        "PrivateIpAddresses": NotRequired[Sequence[str]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence[str]],
        "Ipv4PrefixCount": NotRequired[int],
    },
)
AssignedPrivateIpAddressTypeDef = TypedDict(
    "AssignedPrivateIpAddressTypeDef",
    {
        "PrivateIpAddress": NotRequired[str],
    },
)
Ipv4PrefixSpecificationTypeDef = TypedDict(
    "Ipv4PrefixSpecificationTypeDef",
    {
        "Ipv4Prefix": NotRequired[str],
    },
)
AssignPrivateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "AssignPrivateNatGatewayAddressRequestRequestTypeDef",
    {
        "NatGatewayId": str,
        "PrivateIpAddresses": NotRequired[Sequence[str]],
        "PrivateIpAddressCount": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
NatGatewayAddressTypeDef = TypedDict(
    "NatGatewayAddressTypeDef",
    {
        "AllocationId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIp": NotRequired[str],
        "PublicIp": NotRequired[str],
        "AssociationId": NotRequired[str],
        "IsPrimary": NotRequired[bool],
        "FailureMessage": NotRequired[str],
        "Status": NotRequired[NatGatewayAddressStatusType],
    },
)
AssociateAddressRequestClassicAddressAssociateTypeDef = TypedDict(
    "AssociateAddressRequestClassicAddressAssociateTypeDef",
    {
        "AllocationId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "AllowReassociation": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)
AssociateAddressRequestRequestTypeDef = TypedDict(
    "AssociateAddressRequestRequestTypeDef",
    {
        "AllocationId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "AllowReassociation": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)
AssociateAddressRequestVpcAddressAssociateTypeDef = TypedDict(
    "AssociateAddressRequestVpcAddressAssociateTypeDef",
    {
        "InstanceId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "AllowReassociation": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)
AssociateClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "AssociateClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "SubnetId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
AssociationStatusTypeDef = TypedDict(
    "AssociationStatusTypeDef",
    {
        "Code": NotRequired[AssociationStatusCodeType],
        "Message": NotRequired[str],
    },
)
AssociateDhcpOptionsRequestDhcpOptionsAssociateWithVpcTypeDef = TypedDict(
    "AssociateDhcpOptionsRequestDhcpOptionsAssociateWithVpcTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
AssociateDhcpOptionsRequestRequestTypeDef = TypedDict(
    "AssociateDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpOptionsId": str,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
AssociateDhcpOptionsRequestVpcAssociateDhcpOptionsTypeDef = TypedDict(
    "AssociateDhcpOptionsRequestVpcAssociateDhcpOptionsTypeDef",
    {
        "DhcpOptionsId": str,
        "DryRun": NotRequired[bool],
    },
)
AssociateEnclaveCertificateIamRoleRequestRequestTypeDef = TypedDict(
    "AssociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "RoleArn": str,
        "DryRun": NotRequired[bool],
    },
)
IamInstanceProfileSpecificationTypeDef = TypedDict(
    "IamInstanceProfileSpecificationTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
AssociateIpamByoasnRequestRequestTypeDef = TypedDict(
    "AssociateIpamByoasnRequestRequestTypeDef",
    {
        "Asn": str,
        "Cidr": str,
        "DryRun": NotRequired[bool],
    },
)
AssociateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "AssociateNatGatewayAddressRequestRequestTypeDef",
    {
        "NatGatewayId": str,
        "AllocationIds": Sequence[str],
        "PrivateIpAddresses": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
AssociateRouteTableRequestRequestTypeDef = TypedDict(
    "AssociateRouteTableRequestRequestTypeDef",
    {
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
        "SubnetId": NotRequired[str],
        "GatewayId": NotRequired[str],
    },
)
AssociateRouteTableRequestRouteTableAssociateWithSubnetTypeDef = TypedDict(
    "AssociateRouteTableRequestRouteTableAssociateWithSubnetTypeDef",
    {
        "DryRun": NotRequired[bool],
        "SubnetId": NotRequired[str],
        "GatewayId": NotRequired[str],
    },
)
RouteTableAssociationStateTypeDef = TypedDict(
    "RouteTableAssociationStateTypeDef",
    {
        "State": NotRequired[RouteTableAssociationStateCodeType],
        "StatusMessage": NotRequired[str],
    },
)
AssociateSubnetCidrBlockRequestRequestTypeDef = TypedDict(
    "AssociateSubnetCidrBlockRequestRequestTypeDef",
    {
        "SubnetId": str,
        "Ipv6CidrBlock": NotRequired[str],
        "Ipv6IpamPoolId": NotRequired[str],
        "Ipv6NetmaskLength": NotRequired[int],
    },
)
AssociateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "AssociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "SubnetIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
AssociateTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "AssociateTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)
TransitGatewayPolicyTableAssociationTypeDef = TypedDict(
    "TransitGatewayPolicyTableAssociationTypeDef",
    {
        "TransitGatewayPolicyTableId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "State": NotRequired[TransitGatewayAssociationStateType],
    },
)
AssociateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "AssociateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)
TransitGatewayAssociationTypeDef = TypedDict(
    "TransitGatewayAssociationTypeDef",
    {
        "TransitGatewayRouteTableId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "State": NotRequired[TransitGatewayAssociationStateType],
    },
)
AssociateTrunkInterfaceRequestRequestTypeDef = TypedDict(
    "AssociateTrunkInterfaceRequestRequestTypeDef",
    {
        "BranchInterfaceId": str,
        "TrunkInterfaceId": str,
        "VlanId": NotRequired[int],
        "GreKey": NotRequired[int],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
AssociateVpcCidrBlockRequestRequestTypeDef = TypedDict(
    "AssociateVpcCidrBlockRequestRequestTypeDef",
    {
        "VpcId": str,
        "AmazonProvidedIpv6CidrBlock": NotRequired[bool],
        "CidrBlock": NotRequired[str],
        "Ipv6CidrBlockNetworkBorderGroup": NotRequired[str],
        "Ipv6Pool": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "Ipv4IpamPoolId": NotRequired[str],
        "Ipv4NetmaskLength": NotRequired[int],
        "Ipv6IpamPoolId": NotRequired[str],
        "Ipv6NetmaskLength": NotRequired[int],
    },
)
AssociatedRoleTypeDef = TypedDict(
    "AssociatedRoleTypeDef",
    {
        "AssociatedRoleArn": NotRequired[str],
        "CertificateS3BucketName": NotRequired[str],
        "CertificateS3ObjectKey": NotRequired[str],
        "EncryptionKmsKeyId": NotRequired[str],
    },
)
AssociatedTargetNetworkTypeDef = TypedDict(
    "AssociatedTargetNetworkTypeDef",
    {
        "NetworkId": NotRequired[str],
        "NetworkType": NotRequired[Literal["vpc"]],
    },
)
TimestampTypeDef = Union[datetime, str]
AttachClassicLinkVpcRequestInstanceAttachClassicLinkVpcTypeDef = TypedDict(
    "AttachClassicLinkVpcRequestInstanceAttachClassicLinkVpcTypeDef",
    {
        "Groups": Sequence[str],
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
AttachClassicLinkVpcRequestRequestTypeDef = TypedDict(
    "AttachClassicLinkVpcRequestRequestTypeDef",
    {
        "Groups": Sequence[str],
        "InstanceId": str,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
AttachClassicLinkVpcRequestVpcAttachClassicLinkInstanceTypeDef = TypedDict(
    "AttachClassicLinkVpcRequestVpcAttachClassicLinkInstanceTypeDef",
    {
        "Groups": Sequence[str],
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)
AttachInternetGatewayRequestInternetGatewayAttachToVpcTypeDef = TypedDict(
    "AttachInternetGatewayRequestInternetGatewayAttachToVpcTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
AttachInternetGatewayRequestRequestTypeDef = TypedDict(
    "AttachInternetGatewayRequestRequestTypeDef",
    {
        "InternetGatewayId": str,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
AttachInternetGatewayRequestVpcAttachInternetGatewayTypeDef = TypedDict(
    "AttachInternetGatewayRequestVpcAttachInternetGatewayTypeDef",
    {
        "InternetGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)
AttachVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "AttachVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "VerifiedAccessTrustProviderId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
AttachVolumeRequestInstanceAttachVolumeTypeDef = TypedDict(
    "AttachVolumeRequestInstanceAttachVolumeTypeDef",
    {
        "Device": str,
        "VolumeId": str,
        "DryRun": NotRequired[bool],
    },
)
AttachVolumeRequestRequestTypeDef = TypedDict(
    "AttachVolumeRequestRequestTypeDef",
    {
        "Device": str,
        "InstanceId": str,
        "VolumeId": str,
        "DryRun": NotRequired[bool],
    },
)
AttachVolumeRequestVolumeAttachToInstanceTypeDef = TypedDict(
    "AttachVolumeRequestVolumeAttachToInstanceTypeDef",
    {
        "Device": str,
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)
AttachVpnGatewayRequestRequestTypeDef = TypedDict(
    "AttachVpnGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
        "VpnGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)
VpcAttachmentTypeDef = TypedDict(
    "VpcAttachmentTypeDef",
    {
        "State": NotRequired[AttachmentStatusType],
        "VpcId": NotRequired[str],
    },
)
AttachmentEnaSrdUdpSpecificationTypeDef = TypedDict(
    "AttachmentEnaSrdUdpSpecificationTypeDef",
    {
        "EnaSrdUdpEnabled": NotRequired[bool],
    },
)
AttributeBooleanValueTypeDef = TypedDict(
    "AttributeBooleanValueTypeDef",
    {
        "Value": NotRequired[bool],
    },
)
AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
ClientVpnAuthorizationRuleStatusTypeDef = TypedDict(
    "ClientVpnAuthorizationRuleStatusTypeDef",
    {
        "Code": NotRequired[ClientVpnAuthorizationRuleStatusCodeType],
        "Message": NotRequired[str],
    },
)
AuthorizeClientVpnIngressRequestRequestTypeDef = TypedDict(
    "AuthorizeClientVpnIngressRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "TargetNetworkCidr": str,
        "AccessGroupId": NotRequired[str],
        "AuthorizeAllGroups": NotRequired[bool],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
AvailabilityZoneMessageTypeDef = TypedDict(
    "AvailabilityZoneMessageTypeDef",
    {
        "Message": NotRequired[str],
    },
)
InstanceCapacityTypeDef = TypedDict(
    "InstanceCapacityTypeDef",
    {
        "AvailableCapacity": NotRequired[int],
        "InstanceType": NotRequired[str],
        "TotalCapacity": NotRequired[int],
    },
)
BaselineEbsBandwidthMbpsRequestTypeDef = TypedDict(
    "BaselineEbsBandwidthMbpsRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
BaselineEbsBandwidthMbpsTypeDef = TypedDict(
    "BaselineEbsBandwidthMbpsTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "DeleteOnTermination": NotRequired[bool],
        "Iops": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[VolumeTypeType],
        "KmsKeyId": NotRequired[str],
        "Throughput": NotRequired[int],
        "OutpostArn": NotRequired[str],
        "Encrypted": NotRequired[bool],
    },
)
BundleTaskErrorTypeDef = TypedDict(
    "BundleTaskErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
ByoasnTypeDef = TypedDict(
    "ByoasnTypeDef",
    {
        "Asn": NotRequired[str],
        "IpamId": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "State": NotRequired[AsnStateType],
    },
)
CancelBundleTaskRequestRequestTypeDef = TypedDict(
    "CancelBundleTaskRequestRequestTypeDef",
    {
        "BundleId": str,
        "DryRun": NotRequired[bool],
    },
)
CancelCapacityReservationFleetErrorTypeDef = TypedDict(
    "CancelCapacityReservationFleetErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
CancelCapacityReservationFleetsRequestRequestTypeDef = TypedDict(
    "CancelCapacityReservationFleetsRequestRequestTypeDef",
    {
        "CapacityReservationFleetIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
CapacityReservationFleetCancellationStateTypeDef = TypedDict(
    "CapacityReservationFleetCancellationStateTypeDef",
    {
        "CurrentFleetState": NotRequired[CapacityReservationFleetStateType],
        "PreviousFleetState": NotRequired[CapacityReservationFleetStateType],
        "CapacityReservationFleetId": NotRequired[str],
    },
)
CancelCapacityReservationRequestRequestTypeDef = TypedDict(
    "CancelCapacityReservationRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
        "DryRun": NotRequired[bool],
    },
)
CancelConversionRequestRequestTypeDef = TypedDict(
    "CancelConversionRequestRequestTypeDef",
    {
        "ConversionTaskId": str,
        "DryRun": NotRequired[bool],
        "ReasonMessage": NotRequired[str],
    },
)
CancelExportTaskRequestRequestTypeDef = TypedDict(
    "CancelExportTaskRequestRequestTypeDef",
    {
        "ExportTaskId": str,
    },
)
CancelImageLaunchPermissionRequestRequestTypeDef = TypedDict(
    "CancelImageLaunchPermissionRequestRequestTypeDef",
    {
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)
CancelImportTaskRequestRequestTypeDef = TypedDict(
    "CancelImportTaskRequestRequestTypeDef",
    {
        "CancelReason": NotRequired[str],
        "DryRun": NotRequired[bool],
        "ImportTaskId": NotRequired[str],
    },
)
CancelReservedInstancesListingRequestRequestTypeDef = TypedDict(
    "CancelReservedInstancesListingRequestRequestTypeDef",
    {
        "ReservedInstancesListingId": str,
    },
)
CancelSpotFleetRequestsErrorTypeDef = TypedDict(
    "CancelSpotFleetRequestsErrorTypeDef",
    {
        "Code": NotRequired[CancelBatchErrorCodeType],
        "Message": NotRequired[str],
    },
)
CancelSpotFleetRequestsRequestRequestTypeDef = TypedDict(
    "CancelSpotFleetRequestsRequestRequestTypeDef",
    {
        "SpotFleetRequestIds": Sequence[str],
        "TerminateInstances": bool,
        "DryRun": NotRequired[bool],
    },
)
CancelSpotFleetRequestsSuccessItemTypeDef = TypedDict(
    "CancelSpotFleetRequestsSuccessItemTypeDef",
    {
        "CurrentSpotFleetRequestState": NotRequired[BatchStateType],
        "PreviousSpotFleetRequestState": NotRequired[BatchStateType],
        "SpotFleetRequestId": NotRequired[str],
    },
)
CancelSpotInstanceRequestsRequestRequestTypeDef = TypedDict(
    "CancelSpotInstanceRequestsRequestRequestTypeDef",
    {
        "SpotInstanceRequestIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
CancelledSpotInstanceRequestTypeDef = TypedDict(
    "CancelledSpotInstanceRequestTypeDef",
    {
        "SpotInstanceRequestId": NotRequired[str],
        "State": NotRequired[CancelSpotInstanceRequestStateType],
    },
)
CapacityAllocationTypeDef = TypedDict(
    "CapacityAllocationTypeDef",
    {
        "AllocationType": NotRequired[Literal["used"]],
        "Count": NotRequired[int],
    },
)
CapacityBlockOfferingTypeDef = TypedDict(
    "CapacityBlockOfferingTypeDef",
    {
        "CapacityBlockOfferingId": NotRequired[str],
        "InstanceType": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "StartDate": NotRequired[datetime],
        "EndDate": NotRequired[datetime],
        "CapacityBlockDurationHours": NotRequired[int],
        "UpfrontFee": NotRequired[str],
        "CurrencyCode": NotRequired[str],
        "Tenancy": NotRequired[CapacityReservationTenancyType],
    },
)
FleetCapacityReservationTypeDef = TypedDict(
    "FleetCapacityReservationTypeDef",
    {
        "CapacityReservationId": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "InstancePlatform": NotRequired[CapacityReservationInstancePlatformType],
        "AvailabilityZone": NotRequired[str],
        "TotalInstanceCount": NotRequired[int],
        "FulfilledCapacity": NotRequired[float],
        "EbsOptimized": NotRequired[bool],
        "CreateDate": NotRequired[datetime],
        "Weight": NotRequired[float],
        "Priority": NotRequired[int],
    },
)
CapacityReservationGroupTypeDef = TypedDict(
    "CapacityReservationGroupTypeDef",
    {
        "GroupArn": NotRequired[str],
        "OwnerId": NotRequired[str],
    },
)
CapacityReservationOptionsRequestTypeDef = TypedDict(
    "CapacityReservationOptionsRequestTypeDef",
    {
        "UsageStrategy": NotRequired[Literal["use-capacity-reservations-first"]],
    },
)
CapacityReservationOptionsTypeDef = TypedDict(
    "CapacityReservationOptionsTypeDef",
    {
        "UsageStrategy": NotRequired[Literal["use-capacity-reservations-first"]],
    },
)
CapacityReservationTargetResponseTypeDef = TypedDict(
    "CapacityReservationTargetResponseTypeDef",
    {
        "CapacityReservationId": NotRequired[str],
        "CapacityReservationResourceGroupArn": NotRequired[str],
    },
)
CapacityReservationTargetTypeDef = TypedDict(
    "CapacityReservationTargetTypeDef",
    {
        "CapacityReservationId": NotRequired[str],
        "CapacityReservationResourceGroupArn": NotRequired[str],
    },
)
CertificateAuthenticationRequestTypeDef = TypedDict(
    "CertificateAuthenticationRequestTypeDef",
    {
        "ClientRootCertificateChainArn": NotRequired[str],
    },
)
CertificateAuthenticationTypeDef = TypedDict(
    "CertificateAuthenticationTypeDef",
    {
        "ClientRootCertificateChain": NotRequired[str],
    },
)
CidrAuthorizationContextTypeDef = TypedDict(
    "CidrAuthorizationContextTypeDef",
    {
        "Message": str,
        "Signature": str,
    },
)
CidrBlockTypeDef = TypedDict(
    "CidrBlockTypeDef",
    {
        "CidrBlock": NotRequired[str],
    },
)
ClassicLinkDnsSupportTypeDef = TypedDict(
    "ClassicLinkDnsSupportTypeDef",
    {
        "ClassicLinkDnsSupported": NotRequired[bool],
        "VpcId": NotRequired[str],
    },
)
GroupIdentifierTypeDef = TypedDict(
    "GroupIdentifierTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
    },
)
ClassicLoadBalancerTypeDef = TypedDict(
    "ClassicLoadBalancerTypeDef",
    {
        "Name": NotRequired[str],
    },
)
ClientCertificateRevocationListStatusTypeDef = TypedDict(
    "ClientCertificateRevocationListStatusTypeDef",
    {
        "Code": NotRequired[ClientCertificateRevocationListStatusCodeType],
        "Message": NotRequired[str],
    },
)
ClientConnectOptionsTypeDef = TypedDict(
    "ClientConnectOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "LambdaFunctionArn": NotRequired[str],
    },
)
ClientVpnEndpointAttributeStatusTypeDef = TypedDict(
    "ClientVpnEndpointAttributeStatusTypeDef",
    {
        "Code": NotRequired[ClientVpnEndpointAttributeStatusCodeType],
        "Message": NotRequired[str],
    },
)
ClientLoginBannerOptionsTypeDef = TypedDict(
    "ClientLoginBannerOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "BannerText": NotRequired[str],
    },
)
ClientLoginBannerResponseOptionsTypeDef = TypedDict(
    "ClientLoginBannerResponseOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "BannerText": NotRequired[str],
    },
)
DirectoryServiceAuthenticationRequestTypeDef = TypedDict(
    "DirectoryServiceAuthenticationRequestTypeDef",
    {
        "DirectoryId": NotRequired[str],
    },
)
FederatedAuthenticationRequestTypeDef = TypedDict(
    "FederatedAuthenticationRequestTypeDef",
    {
        "SAMLProviderArn": NotRequired[str],
        "SelfServiceSAMLProviderArn": NotRequired[str],
    },
)
DirectoryServiceAuthenticationTypeDef = TypedDict(
    "DirectoryServiceAuthenticationTypeDef",
    {
        "DirectoryId": NotRequired[str],
    },
)
FederatedAuthenticationTypeDef = TypedDict(
    "FederatedAuthenticationTypeDef",
    {
        "SamlProviderArn": NotRequired[str],
        "SelfServiceSamlProviderArn": NotRequired[str],
    },
)
ClientVpnConnectionStatusTypeDef = TypedDict(
    "ClientVpnConnectionStatusTypeDef",
    {
        "Code": NotRequired[ClientVpnConnectionStatusCodeType],
        "Message": NotRequired[str],
    },
)
ClientVpnEndpointStatusTypeDef = TypedDict(
    "ClientVpnEndpointStatusTypeDef",
    {
        "Code": NotRequired[ClientVpnEndpointStatusCodeType],
        "Message": NotRequired[str],
    },
)
ConnectionLogResponseOptionsTypeDef = TypedDict(
    "ConnectionLogResponseOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "CloudwatchLogGroup": NotRequired[str],
        "CloudwatchLogStream": NotRequired[str],
    },
)
ClientVpnRouteStatusTypeDef = TypedDict(
    "ClientVpnRouteStatusTypeDef",
    {
        "Code": NotRequired[ClientVpnRouteStatusCodeType],
        "Message": NotRequired[str],
    },
)
CloudWatchLogOptionsSpecificationTypeDef = TypedDict(
    "CloudWatchLogOptionsSpecificationTypeDef",
    {
        "LogEnabled": NotRequired[bool],
        "LogGroupArn": NotRequired[str],
        "LogOutputFormat": NotRequired[str],
    },
)
CloudWatchLogOptionsTypeDef = TypedDict(
    "CloudWatchLogOptionsTypeDef",
    {
        "LogEnabled": NotRequired[bool],
        "LogGroupArn": NotRequired[str],
        "LogOutputFormat": NotRequired[str],
    },
)
CoipAddressUsageTypeDef = TypedDict(
    "CoipAddressUsageTypeDef",
    {
        "AllocationId": NotRequired[str],
        "AwsAccountId": NotRequired[str],
        "AwsService": NotRequired[str],
        "CoIp": NotRequired[str],
    },
)
CoipCidrTypeDef = TypedDict(
    "CoipCidrTypeDef",
    {
        "Cidr": NotRequired[str],
        "CoipPoolId": NotRequired[str],
        "LocalGatewayRouteTableId": NotRequired[str],
    },
)
ConfirmProductInstanceRequestRequestTypeDef = TypedDict(
    "ConfirmProductInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ProductCode": str,
        "DryRun": NotRequired[bool],
    },
)
ConnectionLogOptionsTypeDef = TypedDict(
    "ConnectionLogOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "CloudwatchLogGroup": NotRequired[str],
        "CloudwatchLogStream": NotRequired[str],
    },
)
ConnectionNotificationTypeDef = TypedDict(
    "ConnectionNotificationTypeDef",
    {
        "ConnectionNotificationId": NotRequired[str],
        "ServiceId": NotRequired[str],
        "VpcEndpointId": NotRequired[str],
        "ConnectionNotificationType": NotRequired[Literal["Topic"]],
        "ConnectionNotificationArn": NotRequired[str],
        "ConnectionEvents": NotRequired[List[str]],
        "ConnectionNotificationState": NotRequired[ConnectionNotificationStateType],
    },
)
ConnectionTrackingConfigurationTypeDef = TypedDict(
    "ConnectionTrackingConfigurationTypeDef",
    {
        "TcpEstablishedTimeout": NotRequired[int],
        "UdpStreamTimeout": NotRequired[int],
        "UdpTimeout": NotRequired[int],
    },
)
ConnectionTrackingSpecificationRequestTypeDef = TypedDict(
    "ConnectionTrackingSpecificationRequestTypeDef",
    {
        "TcpEstablishedTimeout": NotRequired[int],
        "UdpStreamTimeout": NotRequired[int],
        "UdpTimeout": NotRequired[int],
    },
)
ConnectionTrackingSpecificationResponseTypeDef = TypedDict(
    "ConnectionTrackingSpecificationResponseTypeDef",
    {
        "TcpEstablishedTimeout": NotRequired[int],
        "UdpStreamTimeout": NotRequired[int],
        "UdpTimeout": NotRequired[int],
    },
)
ConnectionTrackingSpecificationTypeDef = TypedDict(
    "ConnectionTrackingSpecificationTypeDef",
    {
        "TcpEstablishedTimeout": NotRequired[int],
        "UdpTimeout": NotRequired[int],
        "UdpStreamTimeout": NotRequired[int],
    },
)
CopyFpgaImageRequestRequestTypeDef = TypedDict(
    "CopyFpgaImageRequestRequestTypeDef",
    {
        "SourceFpgaImageId": str,
        "SourceRegion": str,
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
CopyImageRequestRequestTypeDef = TypedDict(
    "CopyImageRequestRequestTypeDef",
    {
        "Name": str,
        "SourceImageId": str,
        "SourceRegion": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DestinationOutpostArn": NotRequired[str],
        "DryRun": NotRequired[bool],
        "CopyImageTags": NotRequired[bool],
    },
)
CpuOptionsRequestTypeDef = TypedDict(
    "CpuOptionsRequestTypeDef",
    {
        "CoreCount": NotRequired[int],
        "ThreadsPerCore": NotRequired[int],
        "AmdSevSnp": NotRequired[AmdSevSnpSpecificationType],
    },
)
CpuOptionsTypeDef = TypedDict(
    "CpuOptionsTypeDef",
    {
        "CoreCount": NotRequired[int],
        "ThreadsPerCore": NotRequired[int],
        "AmdSevSnp": NotRequired[AmdSevSnpSpecificationType],
    },
)
ReservationFleetInstanceSpecificationTypeDef = TypedDict(
    "ReservationFleetInstanceSpecificationTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "InstancePlatform": NotRequired[CapacityReservationInstancePlatformType],
        "Weight": NotRequired[float],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "Priority": NotRequired[int],
    },
)
CreateClientVpnRouteRequestRequestTypeDef = TypedDict(
    "CreateClientVpnRouteRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidrBlock": str,
        "TargetVpcSubnetId": str,
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
CreateCoipCidrRequestRequestTypeDef = TypedDict(
    "CreateCoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "CoipPoolId": str,
        "DryRun": NotRequired[bool],
    },
)
CreateDefaultSubnetRequestRequestTypeDef = TypedDict(
    "CreateDefaultSubnetRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "DryRun": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
    },
)
CreateDefaultVpcRequestRequestTypeDef = TypedDict(
    "CreateDefaultVpcRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
NewDhcpConfigurationTypeDef = TypedDict(
    "NewDhcpConfigurationTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
TargetCapacitySpecificationRequestTypeDef = TypedDict(
    "TargetCapacitySpecificationRequestTypeDef",
    {
        "TotalTargetCapacity": int,
        "OnDemandTargetCapacity": NotRequired[int],
        "SpotTargetCapacity": NotRequired[int],
        "DefaultTargetCapacityType": NotRequired[DefaultTargetCapacityTypeType],
        "TargetCapacityUnitType": NotRequired[TargetCapacityUnitTypeType],
    },
)
DestinationOptionsRequestTypeDef = TypedDict(
    "DestinationOptionsRequestTypeDef",
    {
        "FileFormat": NotRequired[DestinationFileFormatType],
        "HiveCompatiblePartitions": NotRequired[bool],
        "PerHourPartition": NotRequired[bool],
    },
)
StorageLocationTypeDef = TypedDict(
    "StorageLocationTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
    },
)
InstanceEventWindowTimeRangeRequestTypeDef = TypedDict(
    "InstanceEventWindowTimeRangeRequestTypeDef",
    {
        "StartWeekDay": NotRequired[WeekDayType],
        "StartHour": NotRequired[int],
        "EndWeekDay": NotRequired[WeekDayType],
        "EndHour": NotRequired[int],
    },
)
ExportToS3TaskSpecificationTypeDef = TypedDict(
    "ExportToS3TaskSpecificationTypeDef",
    {
        "ContainerFormat": NotRequired[Literal["ova"]],
        "DiskImageFormat": NotRequired[DiskImageFormatType],
        "S3Bucket": NotRequired[str],
        "S3Prefix": NotRequired[str],
    },
)
IpamPoolSourceResourceRequestTypeDef = TypedDict(
    "IpamPoolSourceResourceRequestTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[Literal["vpc"]],
        "ResourceRegion": NotRequired[str],
        "ResourceOwner": NotRequired[str],
    },
)
RequestIpamResourceTagTypeDef = TypedDict(
    "RequestIpamResourceTagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
CreateLocalGatewayRouteRequestRequestTypeDef = TypedDict(
    "CreateLocalGatewayRouteRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "DestinationCidrBlock": NotRequired[str],
        "LocalGatewayVirtualInterfaceGroupId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "NetworkInterfaceId": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
    },
)
LocalGatewayRouteTypeDef = TypedDict(
    "LocalGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "LocalGatewayVirtualInterfaceGroupId": NotRequired[str],
        "Type": NotRequired[LocalGatewayRouteTypeType],
        "State": NotRequired[LocalGatewayRouteStateType],
        "LocalGatewayRouteTableId": NotRequired[str],
        "LocalGatewayRouteTableArn": NotRequired[str],
        "OwnerId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "CoipPoolId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
    },
)
IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "Code": NotRequired[int],
        "Type": NotRequired[int],
    },
)
CreateNetworkInterfacePermissionRequestRequestTypeDef = TypedDict(
    "CreateNetworkInterfacePermissionRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Permission": InterfacePermissionTypeType,
        "AwsAccountId": NotRequired[str],
        "AwsService": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
InstanceIpv6AddressTypeDef = TypedDict(
    "InstanceIpv6AddressTypeDef",
    {
        "Ipv6Address": NotRequired[str],
        "IsPrimaryIpv6": NotRequired[bool],
    },
)
Ipv4PrefixSpecificationRequestTypeDef = TypedDict(
    "Ipv4PrefixSpecificationRequestTypeDef",
    {
        "Ipv4Prefix": NotRequired[str],
    },
)
Ipv6PrefixSpecificationRequestTypeDef = TypedDict(
    "Ipv6PrefixSpecificationRequestTypeDef",
    {
        "Ipv6Prefix": NotRequired[str],
    },
)
PrivateIpAddressSpecificationTypeDef = TypedDict(
    "PrivateIpAddressSpecificationTypeDef",
    {
        "Primary": NotRequired[bool],
        "PrivateIpAddress": NotRequired[str],
    },
)
PriceScheduleSpecificationTypeDef = TypedDict(
    "PriceScheduleSpecificationTypeDef",
    {
        "CurrencyCode": NotRequired[Literal["USD"]],
        "Price": NotRequired[float],
        "Term": NotRequired[int],
    },
)
CreateRouteRequestRequestTypeDef = TypedDict(
    "CreateRouteRequestRequestTypeDef",
    {
        "RouteTableId": str,
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "VpcEndpointId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "NatGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "CarrierGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
    },
)
CreateRouteRequestRouteTableCreateRouteTypeDef = TypedDict(
    "CreateRouteRequestRouteTableCreateRouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "VpcEndpointId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "NatGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "CarrierGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
    },
)
InstanceSpecificationTypeDef = TypedDict(
    "InstanceSpecificationTypeDef",
    {
        "InstanceId": str,
        "ExcludeBootVolume": NotRequired[bool],
        "ExcludeDataVolumeIds": NotRequired[Sequence[str]],
    },
)
CreateSpotDatafeedSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateSpotDatafeedSubscriptionRequestRequestTypeDef",
    {
        "Bucket": str,
        "DryRun": NotRequired[bool],
        "Prefix": NotRequired[str],
    },
)
S3ObjectTagTypeDef = TypedDict(
    "S3ObjectTagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
TrafficMirrorPortRangeRequestTypeDef = TypedDict(
    "TrafficMirrorPortRangeRequestTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)
TransitGatewayConnectRequestBgpOptionsTypeDef = TypedDict(
    "TransitGatewayConnectRequestBgpOptionsTypeDef",
    {
        "PeerAsn": NotRequired[int],
    },
)
CreateTransitGatewayConnectRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayConnectRequestOptionsTypeDef",
    {
        "Protocol": Literal["gre"],
    },
)
CreateTransitGatewayMulticastDomainRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef",
    {
        "Igmpv2Support": NotRequired[Igmpv2SupportValueType],
        "StaticSourcesSupport": NotRequired[StaticSourcesSupportValueType],
        "AutoAcceptSharedAssociations": NotRequired[AutoAcceptSharedAssociationsValueType],
    },
)
CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef",
    {
        "DynamicRouting": NotRequired[DynamicRoutingValueType],
    },
)
CreateTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
        "TransitGatewayAttachmentId": NotRequired[str],
        "Blackhole": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)
TransitGatewayRequestOptionsTypeDef = TypedDict(
    "TransitGatewayRequestOptionsTypeDef",
    {
        "AmazonSideAsn": NotRequired[int],
        "AutoAcceptSharedAttachments": NotRequired[AutoAcceptSharedAttachmentsValueType],
        "DefaultRouteTableAssociation": NotRequired[DefaultRouteTableAssociationValueType],
        "DefaultRouteTablePropagation": NotRequired[DefaultRouteTablePropagationValueType],
        "VpnEcmpSupport": NotRequired[VpnEcmpSupportValueType],
        "DnsSupport": NotRequired[DnsSupportValueType],
        "SecurityGroupReferencingSupport": NotRequired[SecurityGroupReferencingSupportValueType],
        "MulticastSupport": NotRequired[MulticastSupportValueType],
        "TransitGatewayCidrBlocks": NotRequired[Sequence[str]],
    },
)
CreateTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": NotRequired[str],
        "Blackhole": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)
CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    {
        "DnsSupport": NotRequired[DnsSupportValueType],
        "SecurityGroupReferencingSupport": NotRequired[SecurityGroupReferencingSupportValueType],
        "Ipv6Support": NotRequired[Ipv6SupportValueType],
        "ApplianceModeSupport": NotRequired[ApplianceModeSupportValueType],
    },
)
CreateVerifiedAccessEndpointEniOptionsTypeDef = TypedDict(
    "CreateVerifiedAccessEndpointEniOptionsTypeDef",
    {
        "NetworkInterfaceId": NotRequired[str],
        "Protocol": NotRequired[VerifiedAccessEndpointProtocolType],
        "Port": NotRequired[int],
    },
)
CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef = TypedDict(
    "CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    {
        "Protocol": NotRequired[VerifiedAccessEndpointProtocolType],
        "Port": NotRequired[int],
        "LoadBalancerArn": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
    },
)
VerifiedAccessSseSpecificationRequestTypeDef = TypedDict(
    "VerifiedAccessSseSpecificationRequestTypeDef",
    {
        "CustomerManagedKeyEnabled": NotRequired[bool],
        "KmsKeyArn": NotRequired[str],
    },
)
CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef = TypedDict(
    "CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef",
    {
        "TenantId": NotRequired[str],
        "PublicSigningKeyUrl": NotRequired[str],
    },
)
CreateVerifiedAccessTrustProviderOidcOptionsTypeDef = TypedDict(
    "CreateVerifiedAccessTrustProviderOidcOptionsTypeDef",
    {
        "Issuer": NotRequired[str],
        "AuthorizationEndpoint": NotRequired[str],
        "TokenEndpoint": NotRequired[str],
        "UserInfoEndpoint": NotRequired[str],
        "ClientId": NotRequired[str],
        "ClientSecret": NotRequired[str],
        "Scope": NotRequired[str],
    },
)
CreateVolumePermissionTypeDef = TypedDict(
    "CreateVolumePermissionTypeDef",
    {
        "Group": NotRequired[Literal["all"]],
        "UserId": NotRequired[str],
    },
)
CreateVpcEndpointConnectionNotificationRequestRequestTypeDef = TypedDict(
    "CreateVpcEndpointConnectionNotificationRequestRequestTypeDef",
    {
        "ConnectionNotificationArn": str,
        "ConnectionEvents": Sequence[str],
        "DryRun": NotRequired[bool],
        "ServiceId": NotRequired[str],
        "VpcEndpointId": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
DnsOptionsSpecificationTypeDef = TypedDict(
    "DnsOptionsSpecificationTypeDef",
    {
        "DnsRecordIpType": NotRequired[DnsRecordIpTypeType],
        "PrivateDnsOnlyForInboundResolverEndpoint": NotRequired[bool],
    },
)
SubnetConfigurationTypeDef = TypedDict(
    "SubnetConfigurationTypeDef",
    {
        "SubnetId": NotRequired[str],
        "Ipv4": NotRequired[str],
        "Ipv6": NotRequired[str],
    },
)
CreateVpnConnectionRouteRequestRequestTypeDef = TypedDict(
    "CreateVpnConnectionRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "VpnConnectionId": str,
    },
)
CreditSpecificationRequestTypeDef = TypedDict(
    "CreditSpecificationRequestTypeDef",
    {
        "CpuCredits": str,
    },
)
CreditSpecificationTypeDef = TypedDict(
    "CreditSpecificationTypeDef",
    {
        "CpuCredits": NotRequired[str],
    },
)
DataQueryTypeDef = TypedDict(
    "DataQueryTypeDef",
    {
        "Id": NotRequired[str],
        "Source": NotRequired[str],
        "Destination": NotRequired[str],
        "Metric": NotRequired[Literal["aggregate-latency"]],
        "Statistic": NotRequired[Literal["p50"]],
        "Period": NotRequired[PeriodTypeType],
    },
)
MetricPointTypeDef = TypedDict(
    "MetricPointTypeDef",
    {
        "StartDate": NotRequired[datetime],
        "EndDate": NotRequired[datetime],
        "Value": NotRequired[float],
        "Status": NotRequired[str],
    },
)
DeleteCarrierGatewayRequestRequestTypeDef = TypedDict(
    "DeleteCarrierGatewayRequestRequestTypeDef",
    {
        "CarrierGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "DeleteClientVpnEndpointRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteClientVpnRouteRequestRequestTypeDef = TypedDict(
    "DeleteClientVpnRouteRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidrBlock": str,
        "TargetVpcSubnetId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteCoipCidrRequestRequestTypeDef = TypedDict(
    "DeleteCoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "CoipPoolId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteCoipPoolRequestRequestTypeDef = TypedDict(
    "DeleteCoipPoolRequestRequestTypeDef",
    {
        "CoipPoolId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteCustomerGatewayRequestRequestTypeDef = TypedDict(
    "DeleteCustomerGatewayRequestRequestTypeDef",
    {
        "CustomerGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteDhcpOptionsRequestDhcpOptionsDeleteTypeDef = TypedDict(
    "DeleteDhcpOptionsRequestDhcpOptionsDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteDhcpOptionsRequestRequestTypeDef = TypedDict(
    "DeleteDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpOptionsId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteEgressOnlyInternetGatewayRequestRequestTypeDef = TypedDict(
    "DeleteEgressOnlyInternetGatewayRequestRequestTypeDef",
    {
        "EgressOnlyInternetGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteFleetErrorTypeDef = TypedDict(
    "DeleteFleetErrorTypeDef",
    {
        "Code": NotRequired[DeleteFleetErrorCodeType],
        "Message": NotRequired[str],
    },
)
DeleteFleetSuccessItemTypeDef = TypedDict(
    "DeleteFleetSuccessItemTypeDef",
    {
        "CurrentFleetState": NotRequired[FleetStateCodeType],
        "PreviousFleetState": NotRequired[FleetStateCodeType],
        "FleetId": NotRequired[str],
    },
)
DeleteFleetsRequestRequestTypeDef = TypedDict(
    "DeleteFleetsRequestRequestTypeDef",
    {
        "FleetIds": Sequence[str],
        "TerminateInstances": bool,
        "DryRun": NotRequired[bool],
    },
)
DeleteFlowLogsRequestRequestTypeDef = TypedDict(
    "DeleteFlowLogsRequestRequestTypeDef",
    {
        "FlowLogIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteFpgaImageRequestRequestTypeDef = TypedDict(
    "DeleteFpgaImageRequestRequestTypeDef",
    {
        "FpgaImageId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteInstanceConnectEndpointRequestRequestTypeDef = TypedDict(
    "DeleteInstanceConnectEndpointRequestRequestTypeDef",
    {
        "InstanceConnectEndpointId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "DeleteInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
        "DryRun": NotRequired[bool],
        "ForceDelete": NotRequired[bool],
    },
)
InstanceEventWindowStateChangeTypeDef = TypedDict(
    "InstanceEventWindowStateChangeTypeDef",
    {
        "InstanceEventWindowId": NotRequired[str],
        "State": NotRequired[InstanceEventWindowStateType],
    },
)
DeleteInternetGatewayRequestInternetGatewayDeleteTypeDef = TypedDict(
    "DeleteInternetGatewayRequestInternetGatewayDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteInternetGatewayRequestRequestTypeDef = TypedDict(
    "DeleteInternetGatewayRequestRequestTypeDef",
    {
        "InternetGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteIpamPoolRequestRequestTypeDef = TypedDict(
    "DeleteIpamPoolRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Cascade": NotRequired[bool],
    },
)
DeleteIpamRequestRequestTypeDef = TypedDict(
    "DeleteIpamRequestRequestTypeDef",
    {
        "IpamId": str,
        "DryRun": NotRequired[bool],
        "Cascade": NotRequired[bool],
    },
)
DeleteIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "DeleteIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "IpamResourceDiscoveryId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteIpamScopeRequestRequestTypeDef = TypedDict(
    "DeleteIpamScopeRequestRequestTypeDef",
    {
        "IpamScopeId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteKeyPairRequestKeyPairDeleteTypeDef = TypedDict(
    "DeleteKeyPairRequestKeyPairDeleteTypeDef",
    {
        "KeyPairId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteKeyPairRequestKeyPairInfoDeleteTypeDef = TypedDict(
    "DeleteKeyPairRequestKeyPairInfoDeleteTypeDef",
    {
        "KeyPairId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteKeyPairRequestRequestTypeDef = TypedDict(
    "DeleteKeyPairRequestRequestTypeDef",
    {
        "KeyName": NotRequired[str],
        "KeyPairId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteLaunchTemplateRequestRequestTypeDef = TypedDict(
    "DeleteLaunchTemplateRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
    },
)
DeleteLaunchTemplateVersionsRequestRequestTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsRequestRequestTypeDef",
    {
        "Versions": Sequence[str],
        "DryRun": NotRequired[bool],
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
    },
)
ResponseErrorTypeDef = TypedDict(
    "ResponseErrorTypeDef",
    {
        "Code": NotRequired[LaunchTemplateErrorCodeType],
        "Message": NotRequired[str],
    },
)
DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "VersionNumber": NotRequired[int],
    },
)
DeleteLocalGatewayRouteRequestRequestTypeDef = TypedDict(
    "DeleteLocalGatewayRouteRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "DestinationCidrBlock": NotRequired[str],
        "DryRun": NotRequired[bool],
        "DestinationPrefixListId": NotRequired[str],
    },
)
DeleteLocalGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteManagedPrefixListRequestRequestTypeDef = TypedDict(
    "DeleteManagedPrefixListRequestRequestTypeDef",
    {
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteNatGatewayRequestRequestTypeDef = TypedDict(
    "DeleteNatGatewayRequestRequestTypeDef",
    {
        "NatGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteNetworkAclEntryRequestNetworkAclDeleteEntryTypeDef = TypedDict(
    "DeleteNetworkAclEntryRequestNetworkAclDeleteEntryTypeDef",
    {
        "Egress": bool,
        "RuleNumber": int,
        "DryRun": NotRequired[bool],
    },
)
DeleteNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "DeleteNetworkAclEntryRequestRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "RuleNumber": int,
        "DryRun": NotRequired[bool],
    },
)
DeleteNetworkAclRequestNetworkAclDeleteTypeDef = TypedDict(
    "DeleteNetworkAclRequestNetworkAclDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteNetworkAclRequestRequestTypeDef = TypedDict(
    "DeleteNetworkAclRequestRequestTypeDef",
    {
        "NetworkAclId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteNetworkInsightsAccessScopeRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInsightsAccessScopeRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteNetworkInsightsAnalysisRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInsightsAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsAnalysisId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteNetworkInsightsPathRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInsightsPathRequestRequestTypeDef",
    {
        "NetworkInsightsPathId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteNetworkInterfacePermissionRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInterfacePermissionRequestRequestTypeDef",
    {
        "NetworkInterfacePermissionId": str,
        "Force": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)
DeleteNetworkInterfaceRequestNetworkInterfaceDeleteTypeDef = TypedDict(
    "DeleteNetworkInterfaceRequestNetworkInterfaceDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "DeleteNetworkInterfaceRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "DryRun": NotRequired[bool],
    },
)
DeletePlacementGroupRequestPlacementGroupDeleteTypeDef = TypedDict(
    "DeletePlacementGroupRequestPlacementGroupDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeletePlacementGroupRequestRequestTypeDef = TypedDict(
    "DeletePlacementGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "DryRun": NotRequired[bool],
    },
)
DeletePublicIpv4PoolRequestRequestTypeDef = TypedDict(
    "DeletePublicIpv4PoolRequestRequestTypeDef",
    {
        "PoolId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteQueuedReservedInstancesErrorTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesErrorTypeDef",
    {
        "Code": NotRequired[DeleteQueuedReservedInstancesErrorCodeType],
        "Message": NotRequired[str],
    },
)
DeleteQueuedReservedInstancesRequestRequestTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesRequestRequestTypeDef",
    {
        "ReservedInstancesIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
SuccessfulQueuedPurchaseDeletionTypeDef = TypedDict(
    "SuccessfulQueuedPurchaseDeletionTypeDef",
    {
        "ReservedInstancesId": NotRequired[str],
    },
)
DeleteRouteRequestRequestTypeDef = TypedDict(
    "DeleteRouteRequestRequestTypeDef",
    {
        "RouteTableId": str,
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteRouteRequestRouteDeleteTypeDef = TypedDict(
    "DeleteRouteRequestRouteDeleteTypeDef",
    {
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteRouteTableRequestRequestTypeDef = TypedDict(
    "DeleteRouteTableRequestRequestTypeDef",
    {
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteRouteTableRequestRouteTableDeleteTypeDef = TypedDict(
    "DeleteRouteTableRequestRouteTableDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteSecurityGroupRequestRequestTypeDef = TypedDict(
    "DeleteSecurityGroupRequestRequestTypeDef",
    {
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteSecurityGroupRequestSecurityGroupDeleteTypeDef = TypedDict(
    "DeleteSecurityGroupRequestSecurityGroupDeleteTypeDef",
    {
        "GroupName": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteSnapshotRequestSnapshotDeleteTypeDef = TypedDict(
    "DeleteSnapshotRequestSnapshotDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteSpotDatafeedSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteSpotDatafeedSubscriptionRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteSubnetCidrReservationRequestRequestTypeDef = TypedDict(
    "DeleteSubnetCidrReservationRequestRequestTypeDef",
    {
        "SubnetCidrReservationId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteSubnetRequestRequestTypeDef = TypedDict(
    "DeleteSubnetRequestRequestTypeDef",
    {
        "SubnetId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteSubnetRequestSubnetDeleteTypeDef = TypedDict(
    "DeleteSubnetRequestSubnetDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteTagsRequestTagDeleteTypeDef = TypedDict(
    "DeleteTagsRequestTagDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteTrafficMirrorFilterRequestRequestTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterRequestRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "DeleteTrafficMirrorSessionRequestRequestTypeDef",
    {
        "TrafficMirrorSessionId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTrafficMirrorTargetRequestRequestTypeDef = TypedDict(
    "DeleteTrafficMirrorTargetRequestRequestTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "TransitGatewayConnectPeerId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTransitGatewayConnectRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayConnectRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTransitGatewayRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayRouteRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "DestinationCidrBlock": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableAnnouncementId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "DeleteTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteVerifiedAccessEndpointRequestRequestTypeDef = TypedDict(
    "DeleteVerifiedAccessEndpointRequestRequestTypeDef",
    {
        "VerifiedAccessEndpointId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteVerifiedAccessGroupRequestRequestTypeDef = TypedDict(
    "DeleteVerifiedAccessGroupRequestRequestTypeDef",
    {
        "VerifiedAccessGroupId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteVerifiedAccessInstanceRequestRequestTypeDef = TypedDict(
    "DeleteVerifiedAccessInstanceRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)
DeleteVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "DeleteVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "VerifiedAccessTrustProviderId": str,
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)
DeleteVolumeRequestRequestTypeDef = TypedDict(
    "DeleteVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteVolumeRequestVolumeDeleteTypeDef = TypedDict(
    "DeleteVolumeRequestVolumeDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef = TypedDict(
    "DeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    {
        "ConnectionNotificationIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef = TypedDict(
    "DeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    {
        "ServiceIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteVpcEndpointsRequestRequestTypeDef = TypedDict(
    "DeleteVpcEndpointsRequestRequestTypeDef",
    {
        "VpcEndpointIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
DeleteVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionRequestRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteVpcPeeringConnectionRequestVpcPeeringConnectionDeleteTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionRequestVpcPeeringConnectionDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteVpcRequestRequestTypeDef = TypedDict(
    "DeleteVpcRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteVpcRequestVpcDeleteTypeDef = TypedDict(
    "DeleteVpcRequestVpcDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeleteVpnConnectionRequestRequestTypeDef = TypedDict(
    "DeleteVpnConnectionRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteVpnConnectionRouteRequestRequestTypeDef = TypedDict(
    "DeleteVpnConnectionRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "VpnConnectionId": str,
    },
)
DeleteVpnGatewayRequestRequestTypeDef = TypedDict(
    "DeleteVpnGatewayRequestRequestTypeDef",
    {
        "VpnGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)
DeprovisionByoipCidrRequestRequestTypeDef = TypedDict(
    "DeprovisionByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "DryRun": NotRequired[bool],
    },
)
DeprovisionIpamByoasnRequestRequestTypeDef = TypedDict(
    "DeprovisionIpamByoasnRequestRequestTypeDef",
    {
        "IpamId": str,
        "Asn": str,
        "DryRun": NotRequired[bool],
    },
)
DeprovisionIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "DeprovisionIpamPoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Cidr": NotRequired[str],
    },
)
DeprovisionPublicIpv4PoolCidrRequestRequestTypeDef = TypedDict(
    "DeprovisionPublicIpv4PoolCidrRequestRequestTypeDef",
    {
        "PoolId": str,
        "Cidr": str,
        "DryRun": NotRequired[bool],
    },
)
DeregisterImageRequestImageDeregisterTypeDef = TypedDict(
    "DeregisterImageRequestImageDeregisterTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DeregisterImageRequestRequestTypeDef = TypedDict(
    "DeregisterImageRequestRequestTypeDef",
    {
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)
DeregisterInstanceTagAttributeRequestTypeDef = TypedDict(
    "DeregisterInstanceTagAttributeRequestTypeDef",
    {
        "IncludeAllTagsOfInstance": NotRequired[bool],
        "InstanceTagKeys": NotRequired[Sequence[str]],
    },
)
InstanceTagNotificationAttributeTypeDef = TypedDict(
    "InstanceTagNotificationAttributeTypeDef",
    {
        "InstanceTagKeys": NotRequired[List[str]],
        "IncludeAllTagsOfInstance": NotRequired[bool],
    },
)
DeregisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "GroupIpAddress": NotRequired[str],
        "NetworkInterfaceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
TransitGatewayMulticastDeregisteredGroupMembersTypeDef = TypedDict(
    "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "DeregisteredNetworkInterfaceIds": NotRequired[List[str]],
        "GroupIpAddress": NotRequired[str],
    },
)
DeregisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "GroupIpAddress": NotRequired[str],
        "NetworkInterfaceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
TransitGatewayMulticastDeregisteredGroupSourcesTypeDef = TypedDict(
    "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "DeregisteredNetworkInterfaceIds": NotRequired[List[str]],
        "GroupIpAddress": NotRequired[str],
    },
)
DescribeAccountAttributesRequestRequestTypeDef = TypedDict(
    "DescribeAccountAttributesRequestRequestTypeDef",
    {
        "AttributeNames": NotRequired[Sequence[AccountAttributeNameType]],
        "DryRun": NotRequired[bool],
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
DescribeAddressTransfersRequestRequestTypeDef = TypedDict(
    "DescribeAddressTransfersRequestRequestTypeDef",
    {
        "AllocationIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
DescribeAddressesAttributeRequestRequestTypeDef = TypedDict(
    "DescribeAddressesAttributeRequestRequestTypeDef",
    {
        "AllocationIds": NotRequired[Sequence[str]],
        "Attribute": NotRequired[Literal["domain-name"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
DescribeAggregateIdFormatRequestRequestTypeDef = TypedDict(
    "DescribeAggregateIdFormatRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
IdFormatTypeDef = TypedDict(
    "IdFormatTypeDef",
    {
        "Deadline": NotRequired[datetime],
        "Resource": NotRequired[str],
        "UseLongIds": NotRequired[bool],
    },
)
SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "Source": NotRequired[str],
        "Destination": NotRequired[str],
        "Metric": NotRequired[Literal["aggregate-latency"]],
        "Statistic": NotRequired[Literal["p50"]],
        "Period": NotRequired[PeriodTypeType],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeByoipCidrsRequestRequestTypeDef = TypedDict(
    "DescribeByoipCidrsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)
DescribeConversionTasksRequestRequestTypeDef = TypedDict(
    "DescribeConversionTasksRequestRequestTypeDef",
    {
        "ConversionTaskIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
FastLaunchLaunchTemplateSpecificationResponseTypeDef = TypedDict(
    "FastLaunchLaunchTemplateSpecificationResponseTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)
FastLaunchSnapshotConfigurationResponseTypeDef = TypedDict(
    "FastLaunchSnapshotConfigurationResponseTypeDef",
    {
        "TargetResourceCount": NotRequired[int],
    },
)
DescribeFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "DescribeFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "State": NotRequired[FastSnapshotRestoreStateCodeType],
        "StateTransitionReason": NotRequired[str],
        "OwnerId": NotRequired[str],
        "OwnerAlias": NotRequired[str],
        "EnablingTime": NotRequired[datetime],
        "OptimizingTime": NotRequired[datetime],
        "EnabledTime": NotRequired[datetime],
        "DisablingTime": NotRequired[datetime],
        "DisabledTime": NotRequired[datetime],
    },
)
DescribeFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "DescribeFpgaImageAttributeRequestRequestTypeDef",
    {
        "FpgaImageId": str,
        "Attribute": FpgaImageAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)
HostOfferingTypeDef = TypedDict(
    "HostOfferingTypeDef",
    {
        "CurrencyCode": NotRequired[Literal["USD"]],
        "Duration": NotRequired[int],
        "HourlyPrice": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "OfferingId": NotRequired[str],
        "PaymentOption": NotRequired[PaymentOptionType],
        "UpfrontPrice": NotRequired[str],
    },
)
DescribeIdFormatRequestRequestTypeDef = TypedDict(
    "DescribeIdFormatRequestRequestTypeDef",
    {
        "Resource": NotRequired[str],
    },
)
DescribeIdentityIdFormatRequestRequestTypeDef = TypedDict(
    "DescribeIdentityIdFormatRequestRequestTypeDef",
    {
        "PrincipalArn": str,
        "Resource": NotRequired[str],
    },
)
DescribeImageAttributeRequestImageDescribeAttributeTypeDef = TypedDict(
    "DescribeImageAttributeRequestImageDescribeAttributeTypeDef",
    {
        "Attribute": ImageAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)
DescribeImageAttributeRequestRequestTypeDef = TypedDict(
    "DescribeImageAttributeRequestRequestTypeDef",
    {
        "Attribute": ImageAttributeNameType,
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)
DescribeInstanceAttributeRequestInstanceDescribeAttributeTypeDef = TypedDict(
    "DescribeInstanceAttributeRequestInstanceDescribeAttributeTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)
DescribeInstanceAttributeRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAttributeRequestRequestTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)
InstanceCreditSpecificationTypeDef = TypedDict(
    "InstanceCreditSpecificationTypeDef",
    {
        "InstanceId": NotRequired[str],
        "CpuCredits": NotRequired[str],
    },
)
DescribeInstanceEventNotificationAttributesRequestRequestTypeDef = TypedDict(
    "DescribeInstanceEventNotificationAttributesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
InstanceTopologyTypeDef = TypedDict(
    "InstanceTopologyTypeDef",
    {
        "InstanceId": NotRequired[str],
        "InstanceType": NotRequired[str],
        "GroupName": NotRequired[str],
        "NetworkNodes": NotRequired[List[str]],
        "AvailabilityZone": NotRequired[str],
        "ZoneId": NotRequired[str],
    },
)
InstanceTypeOfferingTypeDef = TypedDict(
    "InstanceTypeOfferingTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "LocationType": NotRequired[LocationTypeType],
        "Location": NotRequired[str],
    },
)
DescribeIpamByoasnRequestRequestTypeDef = TypedDict(
    "DescribeIpamByoasnRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
LockedSnapshotsInfoTypeDef = TypedDict(
    "LockedSnapshotsInfoTypeDef",
    {
        "OwnerId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "LockState": NotRequired[LockStateType],
        "LockDuration": NotRequired[int],
        "CoolOffPeriod": NotRequired[int],
        "CoolOffPeriodExpiresOn": NotRequired[datetime],
        "LockCreatedOn": NotRequired[datetime],
        "LockDurationStartTime": NotRequired[datetime],
        "LockExpiresOn": NotRequired[datetime],
    },
)
MovingAddressStatusTypeDef = TypedDict(
    "MovingAddressStatusTypeDef",
    {
        "MoveStatus": NotRequired[MoveStatusType],
        "PublicIp": NotRequired[str],
    },
)
DescribeNetworkInterfaceAttributeRequestNetworkInterfaceDescribeAttributeTypeDef = TypedDict(
    "DescribeNetworkInterfaceAttributeRequestNetworkInterfaceDescribeAttributeTypeDef",
    {
        "Attribute": NotRequired[NetworkInterfaceAttributeType],
        "DryRun": NotRequired[bool],
    },
)
DescribeNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Attribute": NotRequired[NetworkInterfaceAttributeType],
        "DryRun": NotRequired[bool],
    },
)
PrefixListTypeDef = TypedDict(
    "PrefixListTypeDef",
    {
        "Cidrs": NotRequired[List[str]],
        "PrefixListId": NotRequired[str],
        "PrefixListName": NotRequired[str],
    },
)
DescribePrincipalIdFormatRequestRequestTypeDef = TypedDict(
    "DescribePrincipalIdFormatRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Resources": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "Endpoint": NotRequired[str],
        "RegionName": NotRequired[str],
        "OptInStatus": NotRequired[str],
    },
)
ScheduledInstanceRecurrenceRequestTypeDef = TypedDict(
    "ScheduledInstanceRecurrenceRequestTypeDef",
    {
        "Frequency": NotRequired[str],
        "Interval": NotRequired[int],
        "OccurrenceDays": NotRequired[Sequence[int]],
        "OccurrenceRelativeToEnd": NotRequired[bool],
        "OccurrenceUnit": NotRequired[str],
    },
)
DescribeSecurityGroupReferencesRequestRequestTypeDef = TypedDict(
    "DescribeSecurityGroupReferencesRequestRequestTypeDef",
    {
        "GroupId": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
SecurityGroupReferenceTypeDef = TypedDict(
    "SecurityGroupReferenceTypeDef",
    {
        "GroupId": NotRequired[str],
        "ReferencingVpcId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
    },
)
DescribeSnapshotAttributeRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotAttributeRequestRequestTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "SnapshotId": str,
        "DryRun": NotRequired[bool],
    },
)
DescribeSnapshotAttributeRequestSnapshotDescribeAttributeTypeDef = TypedDict(
    "DescribeSnapshotAttributeRequestSnapshotDescribeAttributeTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)
ProductCodeTypeDef = TypedDict(
    "ProductCodeTypeDef",
    {
        "ProductCodeId": NotRequired[str],
        "ProductCodeType": NotRequired[ProductCodeValuesType],
    },
)
DescribeSpotDatafeedSubscriptionRequestRequestTypeDef = TypedDict(
    "DescribeSpotDatafeedSubscriptionRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DescribeSpotFleetInstancesRequestRequestTypeDef = TypedDict(
    "DescribeSpotFleetInstancesRequestRequestTypeDef",
    {
        "SpotFleetRequestId": str,
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeSpotFleetRequestsRequestRequestTypeDef = TypedDict(
    "DescribeSpotFleetRequestsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SpotFleetRequestIds": NotRequired[Sequence[str]],
    },
)
SpotPriceTypeDef = TypedDict(
    "SpotPriceTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "ProductDescription": NotRequired[RIProductDescriptionType],
        "SpotPrice": NotRequired[str],
        "Timestamp": NotRequired[datetime],
    },
)
DescribeStaleSecurityGroupsRequestRequestTypeDef = TypedDict(
    "DescribeStaleSecurityGroupsRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
StoreImageTaskResultTypeDef = TypedDict(
    "StoreImageTaskResultTypeDef",
    {
        "AmiId": NotRequired[str],
        "TaskStartTime": NotRequired[datetime],
        "Bucket": NotRequired[str],
        "S3objectKey": NotRequired[str],
        "ProgressPercentage": NotRequired[int],
        "StoreTaskState": NotRequired[str],
        "StoreTaskFailureReason": NotRequired[str],
    },
)
TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "Key": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "Value": NotRequired[str],
    },
)
DescribeVolumeAttributeRequestRequestTypeDef = TypedDict(
    "DescribeVolumeAttributeRequestRequestTypeDef",
    {
        "Attribute": VolumeAttributeNameType,
        "VolumeId": str,
        "DryRun": NotRequired[bool],
    },
)
DescribeVolumeAttributeRequestVolumeDescribeAttributeTypeDef = TypedDict(
    "DescribeVolumeAttributeRequestVolumeDescribeAttributeTypeDef",
    {
        "Attribute": VolumeAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)
VolumeModificationTypeDef = TypedDict(
    "VolumeModificationTypeDef",
    {
        "VolumeId": NotRequired[str],
        "ModificationState": NotRequired[VolumeModificationStateType],
        "StatusMessage": NotRequired[str],
        "TargetSize": NotRequired[int],
        "TargetIops": NotRequired[int],
        "TargetVolumeType": NotRequired[VolumeTypeType],
        "TargetThroughput": NotRequired[int],
        "TargetMultiAttachEnabled": NotRequired[bool],
        "OriginalSize": NotRequired[int],
        "OriginalIops": NotRequired[int],
        "OriginalVolumeType": NotRequired[VolumeTypeType],
        "OriginalThroughput": NotRequired[int],
        "OriginalMultiAttachEnabled": NotRequired[bool],
        "Progress": NotRequired[int],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)
DescribeVpcAttributeRequestRequestTypeDef = TypedDict(
    "DescribeVpcAttributeRequestRequestTypeDef",
    {
        "Attribute": VpcAttributeNameType,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
DescribeVpcAttributeRequestVpcDescribeAttributeTypeDef = TypedDict(
    "DescribeVpcAttributeRequestVpcDescribeAttributeTypeDef",
    {
        "Attribute": VpcAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)
DescribeVpcClassicLinkDnsSupportRequestRequestTypeDef = TypedDict(
    "DescribeVpcClassicLinkDnsSupportRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "VpcIds": NotRequired[Sequence[str]],
    },
)
DestinationOptionsResponseTypeDef = TypedDict(
    "DestinationOptionsResponseTypeDef",
    {
        "FileFormat": NotRequired[DestinationFileFormatType],
        "HiveCompatiblePartitions": NotRequired[bool],
        "PerHourPartition": NotRequired[bool],
    },
)
DetachClassicLinkVpcRequestInstanceDetachClassicLinkVpcTypeDef = TypedDict(
    "DetachClassicLinkVpcRequestInstanceDetachClassicLinkVpcTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
DetachClassicLinkVpcRequestRequestTypeDef = TypedDict(
    "DetachClassicLinkVpcRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
DetachClassicLinkVpcRequestVpcDetachClassicLinkInstanceTypeDef = TypedDict(
    "DetachClassicLinkVpcRequestVpcDetachClassicLinkInstanceTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)
DetachInternetGatewayRequestInternetGatewayDetachFromVpcTypeDef = TypedDict(
    "DetachInternetGatewayRequestInternetGatewayDetachFromVpcTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
DetachInternetGatewayRequestRequestTypeDef = TypedDict(
    "DetachInternetGatewayRequestRequestTypeDef",
    {
        "InternetGatewayId": str,
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
DetachInternetGatewayRequestVpcDetachInternetGatewayTypeDef = TypedDict(
    "DetachInternetGatewayRequestVpcDetachInternetGatewayTypeDef",
    {
        "InternetGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)
DetachNetworkInterfaceRequestNetworkInterfaceDetachTypeDef = TypedDict(
    "DetachNetworkInterfaceRequestNetworkInterfaceDetachTypeDef",
    {
        "AttachmentId": str,
        "DryRun": NotRequired[bool],
        "Force": NotRequired[bool],
    },
)
DetachNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "DetachNetworkInterfaceRequestRequestTypeDef",
    {
        "AttachmentId": str,
        "DryRun": NotRequired[bool],
        "Force": NotRequired[bool],
    },
)
DetachVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "DetachVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "VerifiedAccessTrustProviderId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DetachVolumeRequestInstanceDetachVolumeTypeDef = TypedDict(
    "DetachVolumeRequestInstanceDetachVolumeTypeDef",
    {
        "VolumeId": str,
        "Device": NotRequired[str],
        "Force": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)
DetachVolumeRequestRequestTypeDef = TypedDict(
    "DetachVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "Device": NotRequired[str],
        "Force": NotRequired[bool],
        "InstanceId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DetachVolumeRequestVolumeDetachFromInstanceTypeDef = TypedDict(
    "DetachVolumeRequestVolumeDetachFromInstanceTypeDef",
    {
        "Device": NotRequired[str],
        "Force": NotRequired[bool],
        "InstanceId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DetachVpnGatewayRequestRequestTypeDef = TypedDict(
    "DetachVpnGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
        "VpnGatewayId": str,
        "DryRun": NotRequired[bool],
    },
)
DeviceOptionsTypeDef = TypedDict(
    "DeviceOptionsTypeDef",
    {
        "TenantId": NotRequired[str],
        "PublicSigningKeyUrl": NotRequired[str],
    },
)
DisableAddressTransferRequestRequestTypeDef = TypedDict(
    "DisableAddressTransferRequestRequestTypeDef",
    {
        "AllocationId": str,
        "DryRun": NotRequired[bool],
    },
)
DisableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef = TypedDict(
    "DisableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef",
    {
        "Source": NotRequired[str],
        "Destination": NotRequired[str],
        "Metric": NotRequired[Literal["aggregate-latency"]],
        "Statistic": NotRequired[Literal["p50"]],
        "DryRun": NotRequired[bool],
    },
)
DisableEbsEncryptionByDefaultRequestRequestTypeDef = TypedDict(
    "DisableEbsEncryptionByDefaultRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DisableFastLaunchRequestRequestTypeDef = TypedDict(
    "DisableFastLaunchRequestRequestTypeDef",
    {
        "ImageId": str,
        "Force": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)
DisableFastSnapshotRestoreStateErrorTypeDef = TypedDict(
    "DisableFastSnapshotRestoreStateErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
DisableFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "State": NotRequired[FastSnapshotRestoreStateCodeType],
        "StateTransitionReason": NotRequired[str],
        "OwnerId": NotRequired[str],
        "OwnerAlias": NotRequired[str],
        "EnablingTime": NotRequired[datetime],
        "OptimizingTime": NotRequired[datetime],
        "EnabledTime": NotRequired[datetime],
        "DisablingTime": NotRequired[datetime],
        "DisabledTime": NotRequired[datetime],
    },
)
DisableFastSnapshotRestoresRequestRequestTypeDef = TypedDict(
    "DisableFastSnapshotRestoresRequestRequestTypeDef",
    {
        "AvailabilityZones": Sequence[str],
        "SourceSnapshotIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
DisableImageBlockPublicAccessRequestRequestTypeDef = TypedDict(
    "DisableImageBlockPublicAccessRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DisableImageDeprecationRequestRequestTypeDef = TypedDict(
    "DisableImageDeprecationRequestRequestTypeDef",
    {
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)
DisableImageRequestRequestTypeDef = TypedDict(
    "DisableImageRequestRequestTypeDef",
    {
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)
DisableIpamOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableIpamOrganizationAdminAccountRequestRequestTypeDef",
    {
        "DelegatedAdminAccountId": str,
        "DryRun": NotRequired[bool],
    },
)
DisableSerialConsoleAccessRequestRequestTypeDef = TypedDict(
    "DisableSerialConsoleAccessRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DisableSnapshotBlockPublicAccessRequestRequestTypeDef = TypedDict(
    "DisableSnapshotBlockPublicAccessRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DisableTransitGatewayRouteTablePropagationRequestRequestTypeDef = TypedDict(
    "DisableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "TransitGatewayRouteTableAnnouncementId": NotRequired[str],
    },
)
TransitGatewayPropagationTypeDef = TypedDict(
    "TransitGatewayPropagationTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "TransitGatewayRouteTableId": NotRequired[str],
        "State": NotRequired[TransitGatewayPropagationStateType],
        "TransitGatewayRouteTableAnnouncementId": NotRequired[str],
    },
)
DisableVgwRoutePropagationRequestRequestTypeDef = TypedDict(
    "DisableVgwRoutePropagationRequestRequestTypeDef",
    {
        "GatewayId": str,
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)
DisableVpcClassicLinkDnsSupportRequestRequestTypeDef = TypedDict(
    "DisableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    {
        "VpcId": NotRequired[str],
    },
)
DisableVpcClassicLinkRequestRequestTypeDef = TypedDict(
    "DisableVpcClassicLinkRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
DisableVpcClassicLinkRequestVpcDisableClassicLinkTypeDef = TypedDict(
    "DisableVpcClassicLinkRequestVpcDisableClassicLinkTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DisassociateAddressRequestClassicAddressDisassociateTypeDef = TypedDict(
    "DisassociateAddressRequestClassicAddressDisassociateTypeDef",
    {
        "AssociationId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DisassociateAddressRequestNetworkInterfaceAssociationDeleteTypeDef = TypedDict(
    "DisassociateAddressRequestNetworkInterfaceAssociationDeleteTypeDef",
    {
        "PublicIp": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DisassociateAddressRequestRequestTypeDef = TypedDict(
    "DisassociateAddressRequestRequestTypeDef",
    {
        "AssociationId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DisassociateClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "DisassociateClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "AssociationId": str,
        "DryRun": NotRequired[bool],
    },
)
DisassociateEnclaveCertificateIamRoleRequestRequestTypeDef = TypedDict(
    "DisassociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "RoleArn": str,
        "DryRun": NotRequired[bool],
    },
)
DisassociateIamInstanceProfileRequestRequestTypeDef = TypedDict(
    "DisassociateIamInstanceProfileRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)
DisassociateIpamByoasnRequestRequestTypeDef = TypedDict(
    "DisassociateIpamByoasnRequestRequestTypeDef",
    {
        "Asn": str,
        "Cidr": str,
        "DryRun": NotRequired[bool],
    },
)
DisassociateIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "DisassociateIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "IpamResourceDiscoveryAssociationId": str,
        "DryRun": NotRequired[bool],
    },
)
DisassociateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "DisassociateNatGatewayAddressRequestRequestTypeDef",
    {
        "NatGatewayId": str,
        "AssociationIds": Sequence[str],
        "MaxDrainDurationSeconds": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
DisassociateRouteTableRequestRequestTypeDef = TypedDict(
    "DisassociateRouteTableRequestRequestTypeDef",
    {
        "AssociationId": str,
        "DryRun": NotRequired[bool],
    },
)
DisassociateRouteTableRequestRouteTableAssociationDeleteTypeDef = TypedDict(
    "DisassociateRouteTableRequestRouteTableAssociationDeleteTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
DisassociateRouteTableRequestServiceResourceDisassociateRouteTableTypeDef = TypedDict(
    "DisassociateRouteTableRequestServiceResourceDisassociateRouteTableTypeDef",
    {
        "AssociationId": str,
        "DryRun": NotRequired[bool],
    },
)
DisassociateSubnetCidrBlockRequestRequestTypeDef = TypedDict(
    "DisassociateSubnetCidrBlockRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)
DisassociateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "DisassociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "SubnetIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
DisassociateTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "DisassociateTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)
DisassociateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "DisassociateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)
DisassociateTrunkInterfaceRequestRequestTypeDef = TypedDict(
    "DisassociateTrunkInterfaceRequestRequestTypeDef",
    {
        "AssociationId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DisassociateVpcCidrBlockRequestRequestTypeDef = TypedDict(
    "DisassociateVpcCidrBlockRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)
DiskImageDescriptionTypeDef = TypedDict(
    "DiskImageDescriptionTypeDef",
    {
        "Checksum": NotRequired[str],
        "Format": NotRequired[DiskImageFormatType],
        "ImportManifestUrl": NotRequired[str],
        "Size": NotRequired[int],
    },
)
DiskImageDetailTypeDef = TypedDict(
    "DiskImageDetailTypeDef",
    {
        "Bytes": int,
        "Format": DiskImageFormatType,
        "ImportManifestUrl": str,
    },
)
VolumeDetailTypeDef = TypedDict(
    "VolumeDetailTypeDef",
    {
        "Size": int,
    },
)
DiskImageVolumeDescriptionTypeDef = TypedDict(
    "DiskImageVolumeDescriptionTypeDef",
    {
        "Id": NotRequired[str],
        "Size": NotRequired[int],
    },
)
DiskInfoTypeDef = TypedDict(
    "DiskInfoTypeDef",
    {
        "SizeInGB": NotRequired[int],
        "Count": NotRequired[int],
        "Type": NotRequired[DiskTypeType],
    },
)
DnsEntryTypeDef = TypedDict(
    "DnsEntryTypeDef",
    {
        "DnsName": NotRequired[str],
        "HostedZoneId": NotRequired[str],
    },
)
DnsOptionsTypeDef = TypedDict(
    "DnsOptionsTypeDef",
    {
        "DnsRecordIpType": NotRequired[DnsRecordIpTypeType],
        "PrivateDnsOnlyForInboundResolverEndpoint": NotRequired[bool],
    },
)
DnsServersOptionsModifyStructureTypeDef = TypedDict(
    "DnsServersOptionsModifyStructureTypeDef",
    {
        "CustomDnsServers": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
    },
)
EbsOptimizedInfoTypeDef = TypedDict(
    "EbsOptimizedInfoTypeDef",
    {
        "BaselineBandwidthInMbps": NotRequired[int],
        "BaselineThroughputInMBps": NotRequired[float],
        "BaselineIops": NotRequired[int],
        "MaximumBandwidthInMbps": NotRequired[int],
        "MaximumThroughputInMBps": NotRequired[float],
        "MaximumIops": NotRequired[int],
    },
)
EbsInstanceBlockDeviceSpecificationTypeDef = TypedDict(
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    {
        "DeleteOnTermination": NotRequired[bool],
        "VolumeId": NotRequired[str],
    },
)
EbsInstanceBlockDeviceTypeDef = TypedDict(
    "EbsInstanceBlockDeviceTypeDef",
    {
        "AttachTime": NotRequired[datetime],
        "DeleteOnTermination": NotRequired[bool],
        "Status": NotRequired[AttachmentStatusType],
        "VolumeId": NotRequired[str],
    },
)
EfaInfoTypeDef = TypedDict(
    "EfaInfoTypeDef",
    {
        "MaximumEfaInterfaces": NotRequired[int],
    },
)
InternetGatewayAttachmentTypeDef = TypedDict(
    "InternetGatewayAttachmentTypeDef",
    {
        "State": NotRequired[AttachmentStatusType],
        "VpcId": NotRequired[str],
    },
)
ElasticGpuAssociationTypeDef = TypedDict(
    "ElasticGpuAssociationTypeDef",
    {
        "ElasticGpuId": NotRequired[str],
        "ElasticGpuAssociationId": NotRequired[str],
        "ElasticGpuAssociationState": NotRequired[str],
        "ElasticGpuAssociationTime": NotRequired[str],
    },
)
ElasticGpuHealthTypeDef = TypedDict(
    "ElasticGpuHealthTypeDef",
    {
        "Status": NotRequired[ElasticGpuStatusType],
    },
)
ElasticGpuSpecificationResponseTypeDef = TypedDict(
    "ElasticGpuSpecificationResponseTypeDef",
    {
        "Type": NotRequired[str],
    },
)
ElasticGpuSpecificationTypeDef = TypedDict(
    "ElasticGpuSpecificationTypeDef",
    {
        "Type": str,
    },
)
ElasticInferenceAcceleratorAssociationTypeDef = TypedDict(
    "ElasticInferenceAcceleratorAssociationTypeDef",
    {
        "ElasticInferenceAcceleratorArn": NotRequired[str],
        "ElasticInferenceAcceleratorAssociationId": NotRequired[str],
        "ElasticInferenceAcceleratorAssociationState": NotRequired[str],
        "ElasticInferenceAcceleratorAssociationTime": NotRequired[datetime],
    },
)
ElasticInferenceAcceleratorTypeDef = TypedDict(
    "ElasticInferenceAcceleratorTypeDef",
    {
        "Type": str,
        "Count": NotRequired[int],
    },
)
EnaSrdUdpSpecificationRequestTypeDef = TypedDict(
    "EnaSrdUdpSpecificationRequestTypeDef",
    {
        "EnaSrdUdpEnabled": NotRequired[bool],
    },
)
EnaSrdUdpSpecificationTypeDef = TypedDict(
    "EnaSrdUdpSpecificationTypeDef",
    {
        "EnaSrdUdpEnabled": NotRequired[bool],
    },
)
EnableAddressTransferRequestRequestTypeDef = TypedDict(
    "EnableAddressTransferRequestRequestTypeDef",
    {
        "AllocationId": str,
        "TransferAccountId": str,
        "DryRun": NotRequired[bool],
    },
)
EnableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef = TypedDict(
    "EnableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef",
    {
        "Source": NotRequired[str],
        "Destination": NotRequired[str],
        "Metric": NotRequired[Literal["aggregate-latency"]],
        "Statistic": NotRequired[Literal["p50"]],
        "DryRun": NotRequired[bool],
    },
)
EnableEbsEncryptionByDefaultRequestRequestTypeDef = TypedDict(
    "EnableEbsEncryptionByDefaultRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
FastLaunchLaunchTemplateSpecificationRequestTypeDef = TypedDict(
    "FastLaunchLaunchTemplateSpecificationRequestTypeDef",
    {
        "Version": str,
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
    },
)
FastLaunchSnapshotConfigurationRequestTypeDef = TypedDict(
    "FastLaunchSnapshotConfigurationRequestTypeDef",
    {
        "TargetResourceCount": NotRequired[int],
    },
)
EnableFastSnapshotRestoreStateErrorTypeDef = TypedDict(
    "EnableFastSnapshotRestoreStateErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
EnableFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "State": NotRequired[FastSnapshotRestoreStateCodeType],
        "StateTransitionReason": NotRequired[str],
        "OwnerId": NotRequired[str],
        "OwnerAlias": NotRequired[str],
        "EnablingTime": NotRequired[datetime],
        "OptimizingTime": NotRequired[datetime],
        "EnabledTime": NotRequired[datetime],
        "DisablingTime": NotRequired[datetime],
        "DisabledTime": NotRequired[datetime],
    },
)
EnableFastSnapshotRestoresRequestRequestTypeDef = TypedDict(
    "EnableFastSnapshotRestoresRequestRequestTypeDef",
    {
        "AvailabilityZones": Sequence[str],
        "SourceSnapshotIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
EnableImageBlockPublicAccessRequestRequestTypeDef = TypedDict(
    "EnableImageBlockPublicAccessRequestRequestTypeDef",
    {
        "ImageBlockPublicAccessState": Literal["block-new-sharing"],
        "DryRun": NotRequired[bool],
    },
)
EnableImageRequestRequestTypeDef = TypedDict(
    "EnableImageRequestRequestTypeDef",
    {
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)
EnableIpamOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableIpamOrganizationAdminAccountRequestRequestTypeDef",
    {
        "DelegatedAdminAccountId": str,
        "DryRun": NotRequired[bool],
    },
)
EnableReachabilityAnalyzerOrganizationSharingRequestRequestTypeDef = TypedDict(
    "EnableReachabilityAnalyzerOrganizationSharingRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
EnableSerialConsoleAccessRequestRequestTypeDef = TypedDict(
    "EnableSerialConsoleAccessRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
EnableSnapshotBlockPublicAccessRequestRequestTypeDef = TypedDict(
    "EnableSnapshotBlockPublicAccessRequestRequestTypeDef",
    {
        "State": SnapshotBlockPublicAccessStateType,
        "DryRun": NotRequired[bool],
    },
)
EnableTransitGatewayRouteTablePropagationRequestRequestTypeDef = TypedDict(
    "EnableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "TransitGatewayRouteTableAnnouncementId": NotRequired[str],
    },
)
EnableVgwRoutePropagationRequestRequestTypeDef = TypedDict(
    "EnableVgwRoutePropagationRequestRequestTypeDef",
    {
        "GatewayId": str,
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)
EnableVolumeIORequestRequestTypeDef = TypedDict(
    "EnableVolumeIORequestRequestTypeDef",
    {
        "VolumeId": str,
        "DryRun": NotRequired[bool],
    },
)
EnableVolumeIORequestVolumeEnableIoTypeDef = TypedDict(
    "EnableVolumeIORequestVolumeEnableIoTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
EnableVpcClassicLinkDnsSupportRequestRequestTypeDef = TypedDict(
    "EnableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    {
        "VpcId": NotRequired[str],
    },
)
EnableVpcClassicLinkRequestRequestTypeDef = TypedDict(
    "EnableVpcClassicLinkRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
    },
)
EnableVpcClassicLinkRequestVpcEnableClassicLinkTypeDef = TypedDict(
    "EnableVpcClassicLinkRequestVpcEnableClassicLinkTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
EnclaveOptionsRequestTypeDef = TypedDict(
    "EnclaveOptionsRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
EnclaveOptionsTypeDef = TypedDict(
    "EnclaveOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
EventInformationTypeDef = TypedDict(
    "EventInformationTypeDef",
    {
        "EventDescription": NotRequired[str],
        "EventSubType": NotRequired[str],
        "InstanceId": NotRequired[str],
    },
)
TransitGatewayRouteTableRouteTypeDef = TypedDict(
    "TransitGatewayRouteTableRouteTypeDef",
    {
        "DestinationCidr": NotRequired[str],
        "State": NotRequired[str],
        "RouteOrigin": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "AttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
    },
)
ExportClientVpnClientCertificateRevocationListRequestRequestTypeDef = TypedDict(
    "ExportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DryRun": NotRequired[bool],
    },
)
ExportClientVpnClientConfigurationRequestRequestTypeDef = TypedDict(
    "ExportClientVpnClientConfigurationRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DryRun": NotRequired[bool],
    },
)
ExportTaskS3LocationRequestTypeDef = TypedDict(
    "ExportTaskS3LocationRequestTypeDef",
    {
        "S3Bucket": str,
        "S3Prefix": NotRequired[str],
    },
)
ExportTaskS3LocationTypeDef = TypedDict(
    "ExportTaskS3LocationTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Prefix": NotRequired[str],
    },
)
ExportToS3TaskTypeDef = TypedDict(
    "ExportToS3TaskTypeDef",
    {
        "ContainerFormat": NotRequired[Literal["ova"]],
        "DiskImageFormat": NotRequired[DiskImageFormatType],
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
    },
)
InstanceExportDetailsTypeDef = TypedDict(
    "InstanceExportDetailsTypeDef",
    {
        "InstanceId": NotRequired[str],
        "TargetEnvironment": NotRequired[ExportEnvironmentType],
    },
)
FilterPortRangeTypeDef = TypedDict(
    "FilterPortRangeTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)
TargetCapacitySpecificationTypeDef = TypedDict(
    "TargetCapacitySpecificationTypeDef",
    {
        "TotalTargetCapacity": NotRequired[int],
        "OnDemandTargetCapacity": NotRequired[int],
        "SpotTargetCapacity": NotRequired[int],
        "DefaultTargetCapacityType": NotRequired[DefaultTargetCapacityTypeType],
        "TargetCapacityUnitType": NotRequired[TargetCapacityUnitTypeType],
    },
)
FleetLaunchTemplateSpecificationRequestTypeDef = TypedDict(
    "FleetLaunchTemplateSpecificationRequestTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)
FleetLaunchTemplateSpecificationTypeDef = TypedDict(
    "FleetLaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)
PlacementTypeDef = TypedDict(
    "PlacementTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Affinity": NotRequired[str],
        "GroupName": NotRequired[str],
        "PartitionNumber": NotRequired[int],
        "HostId": NotRequired[str],
        "Tenancy": NotRequired[TenancyType],
        "SpreadDomain": NotRequired[str],
        "HostResourceGroupArn": NotRequired[str],
        "GroupId": NotRequired[str],
    },
)
PlacementResponseTypeDef = TypedDict(
    "PlacementResponseTypeDef",
    {
        "GroupName": NotRequired[str],
    },
)
FleetSpotCapacityRebalanceRequestTypeDef = TypedDict(
    "FleetSpotCapacityRebalanceRequestTypeDef",
    {
        "ReplacementStrategy": NotRequired[FleetReplacementStrategyType],
        "TerminationDelay": NotRequired[int],
    },
)
FleetSpotCapacityRebalanceTypeDef = TypedDict(
    "FleetSpotCapacityRebalanceTypeDef",
    {
        "ReplacementStrategy": NotRequired[FleetReplacementStrategyType],
        "TerminationDelay": NotRequired[int],
    },
)
FpgaDeviceMemoryInfoTypeDef = TypedDict(
    "FpgaDeviceMemoryInfoTypeDef",
    {
        "SizeInMiB": NotRequired[int],
    },
)
LoadPermissionTypeDef = TypedDict(
    "LoadPermissionTypeDef",
    {
        "UserId": NotRequired[str],
        "Group": NotRequired[Literal["all"]],
    },
)
FpgaImageStateTypeDef = TypedDict(
    "FpgaImageStateTypeDef",
    {
        "Code": NotRequired[FpgaImageStateCodeType],
        "Message": NotRequired[str],
    },
)
PciIdTypeDef = TypedDict(
    "PciIdTypeDef",
    {
        "DeviceId": NotRequired[str],
        "VendorId": NotRequired[str],
        "SubsystemId": NotRequired[str],
        "SubsystemVendorId": NotRequired[str],
    },
)
GetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef = TypedDict(
    "GetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "DryRun": NotRequired[bool],
    },
)
GetAssociatedIpv6PoolCidrsRequestRequestTypeDef = TypedDict(
    "GetAssociatedIpv6PoolCidrsRequestRequestTypeDef",
    {
        "PoolId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
Ipv6CidrAssociationTypeDef = TypedDict(
    "Ipv6CidrAssociationTypeDef",
    {
        "Ipv6Cidr": NotRequired[str],
        "AssociatedResource": NotRequired[str],
    },
)
GetCapacityReservationUsageRequestRequestTypeDef = TypedDict(
    "GetCapacityReservationUsageRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
InstanceUsageTypeDef = TypedDict(
    "InstanceUsageTypeDef",
    {
        "AccountId": NotRequired[str],
        "UsedInstanceCount": NotRequired[int],
    },
)
GetConsoleOutputRequestInstanceConsoleOutputTypeDef = TypedDict(
    "GetConsoleOutputRequestInstanceConsoleOutputTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Latest": NotRequired[bool],
    },
)
GetConsoleOutputRequestRequestTypeDef = TypedDict(
    "GetConsoleOutputRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
        "Latest": NotRequired[bool],
    },
)
GetConsoleScreenshotRequestRequestTypeDef = TypedDict(
    "GetConsoleScreenshotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
        "WakeUp": NotRequired[bool],
    },
)
GetDefaultCreditSpecificationRequestRequestTypeDef = TypedDict(
    "GetDefaultCreditSpecificationRequestRequestTypeDef",
    {
        "InstanceFamily": UnlimitedSupportedInstanceFamilyType,
        "DryRun": NotRequired[bool],
    },
)
InstanceFamilyCreditSpecificationTypeDef = TypedDict(
    "InstanceFamilyCreditSpecificationTypeDef",
    {
        "InstanceFamily": NotRequired[UnlimitedSupportedInstanceFamilyType],
        "CpuCredits": NotRequired[str],
    },
)
GetEbsDefaultKmsKeyIdRequestRequestTypeDef = TypedDict(
    "GetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
GetEbsEncryptionByDefaultRequestRequestTypeDef = TypedDict(
    "GetEbsEncryptionByDefaultRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
GetGroupsForCapacityReservationRequestRequestTypeDef = TypedDict(
    "GetGroupsForCapacityReservationRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
GetHostReservationPurchasePreviewRequestRequestTypeDef = TypedDict(
    "GetHostReservationPurchasePreviewRequestRequestTypeDef",
    {
        "HostIdSet": Sequence[str],
        "OfferingId": str,
    },
)
PurchaseTypeDef = TypedDict(
    "PurchaseTypeDef",
    {
        "CurrencyCode": NotRequired[Literal["USD"]],
        "Duration": NotRequired[int],
        "HostIdSet": NotRequired[List[str]],
        "HostReservationId": NotRequired[str],
        "HourlyPrice": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "PaymentOption": NotRequired[PaymentOptionType],
        "UpfrontPrice": NotRequired[str],
    },
)
GetImageBlockPublicAccessStateRequestRequestTypeDef = TypedDict(
    "GetImageBlockPublicAccessStateRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
InstanceTypeInfoFromInstanceRequirementsTypeDef = TypedDict(
    "InstanceTypeInfoFromInstanceRequirementsTypeDef",
    {
        "InstanceType": NotRequired[str],
    },
)
GetInstanceUefiDataRequestRequestTypeDef = TypedDict(
    "GetInstanceUefiDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)
IpamAddressHistoryRecordTypeDef = TypedDict(
    "IpamAddressHistoryRecordTypeDef",
    {
        "ResourceOwnerId": NotRequired[str],
        "ResourceRegion": NotRequired[str],
        "ResourceType": NotRequired[IpamAddressHistoryResourceTypeType],
        "ResourceId": NotRequired[str],
        "ResourceCidr": NotRequired[str],
        "ResourceName": NotRequired[str],
        "ResourceComplianceStatus": NotRequired[IpamComplianceStatusType],
        "ResourceOverlapStatus": NotRequired[IpamOverlapStatusType],
        "VpcId": NotRequired[str],
        "SampledStartTime": NotRequired[datetime],
        "SampledEndTime": NotRequired[datetime],
    },
)
GetLaunchTemplateDataRequestRequestTypeDef = TypedDict(
    "GetLaunchTemplateDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)
GetManagedPrefixListAssociationsRequestRequestTypeDef = TypedDict(
    "GetManagedPrefixListAssociationsRequestRequestTypeDef",
    {
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PrefixListAssociationTypeDef = TypedDict(
    "PrefixListAssociationTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ResourceOwner": NotRequired[str],
    },
)
GetManagedPrefixListEntriesRequestRequestTypeDef = TypedDict(
    "GetManagedPrefixListEntriesRequestRequestTypeDef",
    {
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
        "TargetVersion": NotRequired[int],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PrefixListEntryTypeDef = TypedDict(
    "PrefixListEntryTypeDef",
    {
        "Cidr": NotRequired[str],
        "Description": NotRequired[str],
    },
)
GetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef = TypedDict(
    "GetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
GetNetworkInsightsAccessScopeContentRequestRequestTypeDef = TypedDict(
    "GetNetworkInsightsAccessScopeContentRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "DryRun": NotRequired[bool],
    },
)
GetPasswordDataRequestInstancePasswordDataTypeDef = TypedDict(
    "GetPasswordDataRequestInstancePasswordDataTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
GetPasswordDataRequestRequestTypeDef = TypedDict(
    "GetPasswordDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)
ReservationValueTypeDef = TypedDict(
    "ReservationValueTypeDef",
    {
        "HourlyPrice": NotRequired[str],
        "RemainingTotalValue": NotRequired[str],
        "RemainingUpfrontValue": NotRequired[str],
    },
)
GetSerialConsoleAccessStatusRequestRequestTypeDef = TypedDict(
    "GetSerialConsoleAccessStatusRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
GetSnapshotBlockPublicAccessStateRequestRequestTypeDef = TypedDict(
    "GetSnapshotBlockPublicAccessStateRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
SpotPlacementScoreTypeDef = TypedDict(
    "SpotPlacementScoreTypeDef",
    {
        "Region": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "Score": NotRequired[int],
    },
)
TransitGatewayAttachmentPropagationTypeDef = TypedDict(
    "TransitGatewayAttachmentPropagationTypeDef",
    {
        "TransitGatewayRouteTableId": NotRequired[str],
        "State": NotRequired[TransitGatewayPropagationStateType],
    },
)
TransitGatewayRouteTableAssociationTypeDef = TypedDict(
    "TransitGatewayRouteTableAssociationTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "State": NotRequired[TransitGatewayAssociationStateType],
    },
)
TransitGatewayRouteTablePropagationTypeDef = TypedDict(
    "TransitGatewayRouteTablePropagationTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "State": NotRequired[TransitGatewayPropagationStateType],
        "TransitGatewayRouteTableAnnouncementId": NotRequired[str],
    },
)
GetVerifiedAccessEndpointPolicyRequestRequestTypeDef = TypedDict(
    "GetVerifiedAccessEndpointPolicyRequestRequestTypeDef",
    {
        "VerifiedAccessEndpointId": str,
        "DryRun": NotRequired[bool],
    },
)
GetVerifiedAccessGroupPolicyRequestRequestTypeDef = TypedDict(
    "GetVerifiedAccessGroupPolicyRequestRequestTypeDef",
    {
        "VerifiedAccessGroupId": str,
        "DryRun": NotRequired[bool],
    },
)
GetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef = TypedDict(
    "GetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnConnectionDeviceTypeId": str,
        "InternetKeyExchangeVersion": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
GetVpnConnectionDeviceTypesRequestRequestTypeDef = TypedDict(
    "GetVpnConnectionDeviceTypesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
VpnConnectionDeviceTypeTypeDef = TypedDict(
    "VpnConnectionDeviceTypeTypeDef",
    {
        "VpnConnectionDeviceTypeId": NotRequired[str],
        "Vendor": NotRequired[str],
        "Platform": NotRequired[str],
        "Software": NotRequired[str],
    },
)
GetVpnTunnelReplacementStatusRequestRequestTypeDef = TypedDict(
    "GetVpnTunnelReplacementStatusRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
        "DryRun": NotRequired[bool],
    },
)
MaintenanceDetailsTypeDef = TypedDict(
    "MaintenanceDetailsTypeDef",
    {
        "PendingMaintenance": NotRequired[str],
        "MaintenanceAutoAppliedAfter": NotRequired[datetime],
        "LastMaintenanceApplied": NotRequired[datetime],
    },
)
GpuDeviceMemoryInfoTypeDef = TypedDict(
    "GpuDeviceMemoryInfoTypeDef",
    {
        "SizeInMiB": NotRequired[int],
    },
)
HibernationOptionsRequestTypeDef = TypedDict(
    "HibernationOptionsRequestTypeDef",
    {
        "Configured": NotRequired[bool],
    },
)
HibernationOptionsTypeDef = TypedDict(
    "HibernationOptionsTypeDef",
    {
        "Configured": NotRequired[bool],
    },
)
HostInstanceTypeDef = TypedDict(
    "HostInstanceTypeDef",
    {
        "InstanceId": NotRequired[str],
        "InstanceType": NotRequired[str],
        "OwnerId": NotRequired[str],
    },
)
HostPropertiesTypeDef = TypedDict(
    "HostPropertiesTypeDef",
    {
        "Cores": NotRequired[int],
        "InstanceType": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "Sockets": NotRequired[int],
        "TotalVCpus": NotRequired[int],
    },
)
IKEVersionsListValueTypeDef = TypedDict(
    "IKEVersionsListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
IKEVersionsRequestListValueTypeDef = TypedDict(
    "IKEVersionsRequestListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
IamInstanceProfileTypeDef = TypedDict(
    "IamInstanceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
    },
)
LaunchPermissionTypeDef = TypedDict(
    "LaunchPermissionTypeDef",
    {
        "Group": NotRequired[Literal["all"]],
        "UserId": NotRequired[str],
        "OrganizationArn": NotRequired[str],
        "OrganizationalUnitArn": NotRequired[str],
    },
)
UserBucketTypeDef = TypedDict(
    "UserBucketTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
    },
)
ImageRecycleBinInfoTypeDef = TypedDict(
    "ImageRecycleBinInfoTypeDef",
    {
        "ImageId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "RecycleBinEnterTime": NotRequired[datetime],
        "RecycleBinExitTime": NotRequired[datetime],
    },
)
ImportClientVpnClientCertificateRevocationListRequestRequestTypeDef = TypedDict(
    "ImportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "CertificateRevocationList": str,
        "DryRun": NotRequired[bool],
    },
)
ImportImageLicenseConfigurationRequestTypeDef = TypedDict(
    "ImportImageLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)
ImportImageLicenseConfigurationResponseTypeDef = TypedDict(
    "ImportImageLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)
UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "Data": NotRequired[str],
    },
)
InferenceDeviceMemoryInfoTypeDef = TypedDict(
    "InferenceDeviceMemoryInfoTypeDef",
    {
        "SizeInMiB": NotRequired[int],
    },
)
InstanceAttachmentEnaSrdUdpSpecificationTypeDef = TypedDict(
    "InstanceAttachmentEnaSrdUdpSpecificationTypeDef",
    {
        "EnaSrdUdpEnabled": NotRequired[bool],
    },
)
InstanceCountTypeDef = TypedDict(
    "InstanceCountTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "State": NotRequired[ListingStateType],
    },
)
InstanceCreditSpecificationRequestTypeDef = TypedDict(
    "InstanceCreditSpecificationRequestTypeDef",
    {
        "InstanceId": str,
        "CpuCredits": NotRequired[str],
    },
)
InstanceEventWindowTimeRangeTypeDef = TypedDict(
    "InstanceEventWindowTimeRangeTypeDef",
    {
        "StartWeekDay": NotRequired[WeekDayType],
        "StartHour": NotRequired[int],
        "EndWeekDay": NotRequired[WeekDayType],
        "EndHour": NotRequired[int],
    },
)
InstanceIpv4PrefixTypeDef = TypedDict(
    "InstanceIpv4PrefixTypeDef",
    {
        "Ipv4Prefix": NotRequired[str],
    },
)
InstanceIpv6AddressRequestTypeDef = TypedDict(
    "InstanceIpv6AddressRequestTypeDef",
    {
        "Ipv6Address": NotRequired[str],
    },
)
InstanceIpv6PrefixTypeDef = TypedDict(
    "InstanceIpv6PrefixTypeDef",
    {
        "Ipv6Prefix": NotRequired[str],
    },
)
InstanceMaintenanceOptionsRequestTypeDef = TypedDict(
    "InstanceMaintenanceOptionsRequestTypeDef",
    {
        "AutoRecovery": NotRequired[InstanceAutoRecoveryStateType],
    },
)
InstanceMaintenanceOptionsTypeDef = TypedDict(
    "InstanceMaintenanceOptionsTypeDef",
    {
        "AutoRecovery": NotRequired[InstanceAutoRecoveryStateType],
    },
)
InstanceMetadataOptionsRequestTypeDef = TypedDict(
    "InstanceMetadataOptionsRequestTypeDef",
    {
        "HttpTokens": NotRequired[HttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[InstanceMetadataEndpointStateType],
        "HttpProtocolIpv6": NotRequired[InstanceMetadataProtocolStateType],
        "InstanceMetadataTags": NotRequired[InstanceMetadataTagsStateType],
    },
)
InstanceMetadataOptionsResponseTypeDef = TypedDict(
    "InstanceMetadataOptionsResponseTypeDef",
    {
        "State": NotRequired[InstanceMetadataOptionsStateType],
        "HttpTokens": NotRequired[HttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[InstanceMetadataEndpointStateType],
        "HttpProtocolIpv6": NotRequired[InstanceMetadataProtocolStateType],
        "InstanceMetadataTags": NotRequired[InstanceMetadataTagsStateType],
    },
)
MonitoringTypeDef = TypedDict(
    "MonitoringTypeDef",
    {
        "State": NotRequired[MonitoringStateType],
    },
)
InstanceNetworkInterfaceAssociationTypeDef = TypedDict(
    "InstanceNetworkInterfaceAssociationTypeDef",
    {
        "CarrierIp": NotRequired[str],
        "CustomerOwnedIp": NotRequired[str],
        "IpOwnerId": NotRequired[str],
        "PublicDnsName": NotRequired[str],
        "PublicIp": NotRequired[str],
    },
)
MemoryGiBPerVCpuRequestTypeDef = TypedDict(
    "MemoryGiBPerVCpuRequestTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
MemoryMiBRequestTypeDef = TypedDict(
    "MemoryMiBRequestTypeDef",
    {
        "Min": int,
        "Max": NotRequired[int],
    },
)
NetworkBandwidthGbpsRequestTypeDef = TypedDict(
    "NetworkBandwidthGbpsRequestTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
NetworkInterfaceCountRequestTypeDef = TypedDict(
    "NetworkInterfaceCountRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
TotalLocalStorageGBRequestTypeDef = TypedDict(
    "TotalLocalStorageGBRequestTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
VCpuCountRangeRequestTypeDef = TypedDict(
    "VCpuCountRangeRequestTypeDef",
    {
        "Min": int,
        "Max": NotRequired[int],
    },
)
MemoryGiBPerVCpuTypeDef = TypedDict(
    "MemoryGiBPerVCpuTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
MemoryMiBTypeDef = TypedDict(
    "MemoryMiBTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
NetworkBandwidthGbpsTypeDef = TypedDict(
    "NetworkBandwidthGbpsTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
NetworkInterfaceCountTypeDef = TypedDict(
    "NetworkInterfaceCountTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
TotalLocalStorageGBTypeDef = TypedDict(
    "TotalLocalStorageGBTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
VCpuCountRangeTypeDef = TypedDict(
    "VCpuCountRangeTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "Code": NotRequired[int],
        "Name": NotRequired[InstanceStateNameType],
    },
)
InstanceStatusDetailsTypeDef = TypedDict(
    "InstanceStatusDetailsTypeDef",
    {
        "ImpairedSince": NotRequired[datetime],
        "Name": NotRequired[Literal["reachability"]],
        "Status": NotRequired[StatusTypeType],
    },
)
InstanceStatusEventTypeDef = TypedDict(
    "InstanceStatusEventTypeDef",
    {
        "InstanceEventId": NotRequired[str],
        "Code": NotRequired[EventCodeType],
        "Description": NotRequired[str],
        "NotAfter": NotRequired[datetime],
        "NotBefore": NotRequired[datetime],
        "NotBeforeDeadline": NotRequired[datetime],
    },
)
LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)
PrivateDnsNameOptionsResponseTypeDef = TypedDict(
    "PrivateDnsNameOptionsResponseTypeDef",
    {
        "HostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)
MemoryInfoTypeDef = TypedDict(
    "MemoryInfoTypeDef",
    {
        "SizeInMiB": NotRequired[int],
    },
)
NitroTpmInfoTypeDef = TypedDict(
    "NitroTpmInfoTypeDef",
    {
        "SupportedVersions": NotRequired[List[str]],
    },
)
PlacementGroupInfoTypeDef = TypedDict(
    "PlacementGroupInfoTypeDef",
    {
        "SupportedStrategies": NotRequired[List[PlacementGroupStrategyType]],
    },
)
ProcessorInfoTypeDef = TypedDict(
    "ProcessorInfoTypeDef",
    {
        "SupportedArchitectures": NotRequired[List[ArchitectureTypeType]],
        "SustainedClockSpeedInGhz": NotRequired[float],
        "SupportedFeatures": NotRequired[List[Literal["amd-sev-snp"]]],
        "Manufacturer": NotRequired[str],
    },
)
VCpuInfoTypeDef = TypedDict(
    "VCpuInfoTypeDef",
    {
        "DefaultVCpus": NotRequired[int],
        "DefaultCores": NotRequired[int],
        "DefaultThreadsPerCore": NotRequired[int],
        "ValidCores": NotRequired[List[int]],
        "ValidThreadsPerCore": NotRequired[List[int]],
    },
)
IpRangeTypeDef = TypedDict(
    "IpRangeTypeDef",
    {
        "CidrIp": NotRequired[str],
        "Description": NotRequired[str],
    },
)
Ipv6RangeTypeDef = TypedDict(
    "Ipv6RangeTypeDef",
    {
        "CidrIpv6": NotRequired[str],
        "Description": NotRequired[str],
    },
)
PrefixListIdTypeDef = TypedDict(
    "PrefixListIdTypeDef",
    {
        "Description": NotRequired[str],
        "PrefixListId": NotRequired[str],
    },
)
UserIdGroupPairTypeDef = TypedDict(
    "UserIdGroupPairTypeDef",
    {
        "Description": NotRequired[str],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "PeeringStatus": NotRequired[str],
        "UserId": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)
IpamCidrAuthorizationContextTypeDef = TypedDict(
    "IpamCidrAuthorizationContextTypeDef",
    {
        "Message": NotRequired[str],
        "Signature": NotRequired[str],
    },
)
IpamDiscoveryFailureReasonTypeDef = TypedDict(
    "IpamDiscoveryFailureReasonTypeDef",
    {
        "Code": NotRequired[IpamDiscoveryFailureCodeType],
        "Message": NotRequired[str],
    },
)
IpamPublicAddressSecurityGroupTypeDef = TypedDict(
    "IpamPublicAddressSecurityGroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
    },
)
IpamResourceTagTypeDef = TypedDict(
    "IpamResourceTagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
IpamOperatingRegionTypeDef = TypedDict(
    "IpamOperatingRegionTypeDef",
    {
        "RegionName": NotRequired[str],
    },
)
IpamPoolCidrFailureReasonTypeDef = TypedDict(
    "IpamPoolCidrFailureReasonTypeDef",
    {
        "Code": NotRequired[IpamPoolCidrFailureCodeType],
        "Message": NotRequired[str],
    },
)
IpamPoolSourceResourceTypeDef = TypedDict(
    "IpamPoolSourceResourceTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[Literal["vpc"]],
        "ResourceRegion": NotRequired[str],
        "ResourceOwner": NotRequired[str],
    },
)
IpamPublicAddressTagTypeDef = TypedDict(
    "IpamPublicAddressTagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
Ipv4PrefixSpecificationResponseTypeDef = TypedDict(
    "Ipv4PrefixSpecificationResponseTypeDef",
    {
        "Ipv4Prefix": NotRequired[str],
    },
)
Ipv6CidrBlockTypeDef = TypedDict(
    "Ipv6CidrBlockTypeDef",
    {
        "Ipv6CidrBlock": NotRequired[str],
    },
)
PoolCidrBlockTypeDef = TypedDict(
    "PoolCidrBlockTypeDef",
    {
        "Cidr": NotRequired[str],
    },
)
Ipv6PrefixSpecificationResponseTypeDef = TypedDict(
    "Ipv6PrefixSpecificationResponseTypeDef",
    {
        "Ipv6Prefix": NotRequired[str],
    },
)
Ipv6PrefixSpecificationTypeDef = TypedDict(
    "Ipv6PrefixSpecificationTypeDef",
    {
        "Ipv6Prefix": NotRequired[str],
    },
)
LastErrorTypeDef = TypedDict(
    "LastErrorTypeDef",
    {
        "Message": NotRequired[str],
        "Code": NotRequired[str],
    },
)
RunInstancesMonitoringEnabledTypeDef = TypedDict(
    "RunInstancesMonitoringEnabledTypeDef",
    {
        "Enabled": bool,
    },
)
SpotPlacementTypeDef = TypedDict(
    "SpotPlacementTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "GroupName": NotRequired[str],
        "Tenancy": NotRequired[TenancyType],
    },
)
LaunchTemplateEbsBlockDeviceRequestTypeDef = TypedDict(
    "LaunchTemplateEbsBlockDeviceRequestTypeDef",
    {
        "Encrypted": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Iops": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[VolumeTypeType],
        "Throughput": NotRequired[int],
    },
)
LaunchTemplateEbsBlockDeviceTypeDef = TypedDict(
    "LaunchTemplateEbsBlockDeviceTypeDef",
    {
        "Encrypted": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Iops": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[VolumeTypeType],
        "Throughput": NotRequired[int],
    },
)
LaunchTemplateCpuOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateCpuOptionsRequestTypeDef",
    {
        "CoreCount": NotRequired[int],
        "ThreadsPerCore": NotRequired[int],
        "AmdSevSnp": NotRequired[AmdSevSnpSpecificationType],
    },
)
LaunchTemplateCpuOptionsTypeDef = TypedDict(
    "LaunchTemplateCpuOptionsTypeDef",
    {
        "CoreCount": NotRequired[int],
        "ThreadsPerCore": NotRequired[int],
        "AmdSevSnp": NotRequired[AmdSevSnpSpecificationType],
    },
)
LaunchTemplateElasticInferenceAcceleratorResponseTypeDef = TypedDict(
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    {
        "Type": NotRequired[str],
        "Count": NotRequired[int],
    },
)
LaunchTemplateElasticInferenceAcceleratorTypeDef = TypedDict(
    "LaunchTemplateElasticInferenceAcceleratorTypeDef",
    {
        "Type": str,
        "Count": NotRequired[int],
    },
)
LaunchTemplateEnaSrdUdpSpecificationTypeDef = TypedDict(
    "LaunchTemplateEnaSrdUdpSpecificationTypeDef",
    {
        "EnaSrdUdpEnabled": NotRequired[bool],
    },
)
LaunchTemplateEnclaveOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateEnclaveOptionsRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
LaunchTemplateEnclaveOptionsTypeDef = TypedDict(
    "LaunchTemplateEnclaveOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
LaunchTemplateHibernationOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateHibernationOptionsRequestTypeDef",
    {
        "Configured": NotRequired[bool],
    },
)
LaunchTemplateHibernationOptionsTypeDef = TypedDict(
    "LaunchTemplateHibernationOptionsTypeDef",
    {
        "Configured": NotRequired[bool],
    },
)
LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
LaunchTemplateIamInstanceProfileSpecificationTypeDef = TypedDict(
    "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
LaunchTemplateInstanceMaintenanceOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMaintenanceOptionsRequestTypeDef",
    {
        "AutoRecovery": NotRequired[LaunchTemplateAutoRecoveryStateType],
    },
)
LaunchTemplateInstanceMaintenanceOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMaintenanceOptionsTypeDef",
    {
        "AutoRecovery": NotRequired[LaunchTemplateAutoRecoveryStateType],
    },
)
LaunchTemplateSpotMarketOptionsTypeDef = TypedDict(
    "LaunchTemplateSpotMarketOptionsTypeDef",
    {
        "MaxPrice": NotRequired[str],
        "SpotInstanceType": NotRequired[SpotInstanceTypeType],
        "BlockDurationMinutes": NotRequired[int],
        "ValidUntil": NotRequired[datetime],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
    },
)
LaunchTemplateInstanceMetadataOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    {
        "HttpTokens": NotRequired[LaunchTemplateHttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[LaunchTemplateInstanceMetadataEndpointStateType],
        "HttpProtocolIpv6": NotRequired[LaunchTemplateInstanceMetadataProtocolIpv6Type],
        "InstanceMetadataTags": NotRequired[LaunchTemplateInstanceMetadataTagsStateType],
    },
)
LaunchTemplateInstanceMetadataOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMetadataOptionsTypeDef",
    {
        "State": NotRequired[LaunchTemplateInstanceMetadataOptionsStateType],
        "HttpTokens": NotRequired[LaunchTemplateHttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[LaunchTemplateInstanceMetadataEndpointStateType],
        "HttpProtocolIpv6": NotRequired[LaunchTemplateInstanceMetadataProtocolIpv6Type],
        "InstanceMetadataTags": NotRequired[LaunchTemplateInstanceMetadataTagsStateType],
    },
)
LaunchTemplateLicenseConfigurationRequestTypeDef = TypedDict(
    "LaunchTemplateLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)
LaunchTemplateLicenseConfigurationTypeDef = TypedDict(
    "LaunchTemplateLicenseConfigurationTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)
LaunchTemplatePlacementRequestTypeDef = TypedDict(
    "LaunchTemplatePlacementRequestTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Affinity": NotRequired[str],
        "GroupName": NotRequired[str],
        "HostId": NotRequired[str],
        "Tenancy": NotRequired[TenancyType],
        "SpreadDomain": NotRequired[str],
        "HostResourceGroupArn": NotRequired[str],
        "PartitionNumber": NotRequired[int],
        "GroupId": NotRequired[str],
    },
)
LaunchTemplatePlacementTypeDef = TypedDict(
    "LaunchTemplatePlacementTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Affinity": NotRequired[str],
        "GroupName": NotRequired[str],
        "HostId": NotRequired[str],
        "Tenancy": NotRequired[TenancyType],
        "SpreadDomain": NotRequired[str],
        "HostResourceGroupArn": NotRequired[str],
        "PartitionNumber": NotRequired[int],
        "GroupId": NotRequired[str],
    },
)
LaunchTemplatePrivateDnsNameOptionsRequestTypeDef = TypedDict(
    "LaunchTemplatePrivateDnsNameOptionsRequestTypeDef",
    {
        "HostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)
LaunchTemplatePrivateDnsNameOptionsTypeDef = TypedDict(
    "LaunchTemplatePrivateDnsNameOptionsTypeDef",
    {
        "HostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)
LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)
LaunchTemplatesMonitoringRequestTypeDef = TypedDict(
    "LaunchTemplatesMonitoringRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
LaunchTemplatesMonitoringTypeDef = TypedDict(
    "LaunchTemplatesMonitoringTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
LicenseConfigurationRequestTypeDef = TypedDict(
    "LicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)
ListImagesInRecycleBinRequestRequestTypeDef = TypedDict(
    "ListImagesInRecycleBinRequestRequestTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
ListSnapshotsInRecycleBinRequestRequestTypeDef = TypedDict(
    "ListSnapshotsInRecycleBinRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SnapshotIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
SnapshotRecycleBinInfoTypeDef = TypedDict(
    "SnapshotRecycleBinInfoTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "RecycleBinEnterTime": NotRequired[datetime],
        "RecycleBinExitTime": NotRequired[datetime],
        "Description": NotRequired[str],
        "VolumeId": NotRequired[str],
    },
)
LoadPermissionRequestTypeDef = TypedDict(
    "LoadPermissionRequestTypeDef",
    {
        "Group": NotRequired[Literal["all"]],
        "UserId": NotRequired[str],
    },
)
ModifyAddressAttributeRequestRequestTypeDef = TypedDict(
    "ModifyAddressAttributeRequestRequestTypeDef",
    {
        "AllocationId": str,
        "DomainName": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
ModifyAvailabilityZoneGroupRequestRequestTypeDef = TypedDict(
    "ModifyAvailabilityZoneGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "OptInStatus": ModifyAvailabilityZoneOptInStatusType,
        "DryRun": NotRequired[bool],
    },
)
ModifyDefaultCreditSpecificationRequestRequestTypeDef = TypedDict(
    "ModifyDefaultCreditSpecificationRequestRequestTypeDef",
    {
        "InstanceFamily": UnlimitedSupportedInstanceFamilyType,
        "CpuCredits": str,
        "DryRun": NotRequired[bool],
    },
)
ModifyEbsDefaultKmsKeyIdRequestRequestTypeDef = TypedDict(
    "ModifyEbsDefaultKmsKeyIdRequestRequestTypeDef",
    {
        "KmsKeyId": str,
        "DryRun": NotRequired[bool],
    },
)
ModifyHostsRequestRequestTypeDef = TypedDict(
    "ModifyHostsRequestRequestTypeDef",
    {
        "HostIds": Sequence[str],
        "AutoPlacement": NotRequired[AutoPlacementType],
        "HostRecovery": NotRequired[HostRecoveryType],
        "InstanceType": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "HostMaintenance": NotRequired[HostMaintenanceType],
    },
)
ModifyIdFormatRequestRequestTypeDef = TypedDict(
    "ModifyIdFormatRequestRequestTypeDef",
    {
        "Resource": str,
        "UseLongIds": bool,
    },
)
ModifyIdentityIdFormatRequestRequestTypeDef = TypedDict(
    "ModifyIdentityIdFormatRequestRequestTypeDef",
    {
        "PrincipalArn": str,
        "Resource": str,
        "UseLongIds": bool,
    },
)
SuccessfulInstanceCreditSpecificationItemTypeDef = TypedDict(
    "SuccessfulInstanceCreditSpecificationItemTypeDef",
    {
        "InstanceId": NotRequired[str],
    },
)
ModifyInstanceMaintenanceOptionsRequestRequestTypeDef = TypedDict(
    "ModifyInstanceMaintenanceOptionsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AutoRecovery": NotRequired[InstanceAutoRecoveryStateType],
        "DryRun": NotRequired[bool],
    },
)
ModifyInstanceMetadataOptionsRequestRequestTypeDef = TypedDict(
    "ModifyInstanceMetadataOptionsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HttpTokens": NotRequired[HttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[InstanceMetadataEndpointStateType],
        "DryRun": NotRequired[bool],
        "HttpProtocolIpv6": NotRequired[InstanceMetadataProtocolStateType],
        "InstanceMetadataTags": NotRequired[InstanceMetadataTagsStateType],
    },
)
ModifyInstancePlacementRequestRequestTypeDef = TypedDict(
    "ModifyInstancePlacementRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Affinity": NotRequired[AffinityType],
        "GroupName": NotRequired[str],
        "HostId": NotRequired[str],
        "Tenancy": NotRequired[HostTenancyType],
        "PartitionNumber": NotRequired[int],
        "HostResourceGroupArn": NotRequired[str],
        "GroupId": NotRequired[str],
    },
)
RemoveIpamOperatingRegionTypeDef = TypedDict(
    "RemoveIpamOperatingRegionTypeDef",
    {
        "RegionName": NotRequired[str],
    },
)
ModifyIpamResourceCidrRequestRequestTypeDef = TypedDict(
    "ModifyIpamResourceCidrRequestRequestTypeDef",
    {
        "ResourceId": str,
        "ResourceCidr": str,
        "ResourceRegion": str,
        "CurrentIpamScopeId": str,
        "Monitored": bool,
        "DryRun": NotRequired[bool],
        "DestinationIpamScopeId": NotRequired[str],
    },
)
ModifyIpamScopeRequestRequestTypeDef = TypedDict(
    "ModifyIpamScopeRequestRequestTypeDef",
    {
        "IpamScopeId": str,
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
    },
)
ModifyLaunchTemplateRequestRequestTypeDef = TypedDict(
    "ModifyLaunchTemplateRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "DefaultVersion": NotRequired[str],
    },
)
ModifyLocalGatewayRouteRequestRequestTypeDef = TypedDict(
    "ModifyLocalGatewayRouteRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "DestinationCidrBlock": NotRequired[str],
        "LocalGatewayVirtualInterfaceGroupId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "DestinationPrefixListId": NotRequired[str],
    },
)
RemovePrefixListEntryTypeDef = TypedDict(
    "RemovePrefixListEntryTypeDef",
    {
        "Cidr": str,
    },
)
NetworkInterfaceAttachmentChangesTypeDef = TypedDict(
    "NetworkInterfaceAttachmentChangesTypeDef",
    {
        "AttachmentId": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
    },
)
ModifyPrivateDnsNameOptionsRequestRequestTypeDef = TypedDict(
    "ModifyPrivateDnsNameOptionsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
        "PrivateDnsHostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)
ReservedInstancesConfigurationTypeDef = TypedDict(
    "ReservedInstancesConfigurationTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "InstanceType": NotRequired[InstanceTypeType],
        "Platform": NotRequired[str],
        "Scope": NotRequired[scopeType],
    },
)
ModifySnapshotTierRequestRequestTypeDef = TypedDict(
    "ModifySnapshotTierRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "StorageTier": NotRequired[Literal["archive"]],
        "DryRun": NotRequired[bool],
    },
)
ModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "AddNetworkServices": NotRequired[Sequence[Literal["amazon-dns"]]],
        "RemoveNetworkServices": NotRequired[Sequence[Literal["amazon-dns"]]],
        "DryRun": NotRequired[bool],
    },
)
ModifyTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "ModifyTrafficMirrorSessionRequestRequestTypeDef",
    {
        "TrafficMirrorSessionId": str,
        "TrafficMirrorTargetId": NotRequired[str],
        "TrafficMirrorFilterId": NotRequired[str],
        "PacketLength": NotRequired[int],
        "SessionNumber": NotRequired[int],
        "VirtualNetworkId": NotRequired[int],
        "Description": NotRequired[str],
        "RemoveFields": NotRequired[Sequence[TrafficMirrorSessionFieldType]],
        "DryRun": NotRequired[bool],
    },
)
ModifyTransitGatewayOptionsTypeDef = TypedDict(
    "ModifyTransitGatewayOptionsTypeDef",
    {
        "AddTransitGatewayCidrBlocks": NotRequired[Sequence[str]],
        "RemoveTransitGatewayCidrBlocks": NotRequired[Sequence[str]],
        "VpnEcmpSupport": NotRequired[VpnEcmpSupportValueType],
        "DnsSupport": NotRequired[DnsSupportValueType],
        "SecurityGroupReferencingSupport": NotRequired[SecurityGroupReferencingSupportValueType],
        "AutoAcceptSharedAttachments": NotRequired[AutoAcceptSharedAttachmentsValueType],
        "DefaultRouteTableAssociation": NotRequired[DefaultRouteTableAssociationValueType],
        "AssociationDefaultRouteTableId": NotRequired[str],
        "DefaultRouteTablePropagation": NotRequired[DefaultRouteTablePropagationValueType],
        "PropagationDefaultRouteTableId": NotRequired[str],
        "AmazonSideAsn": NotRequired[int],
    },
)
ModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "ModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
        "TransitGatewayAttachmentId": NotRequired[str],
        "Blackhole": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)
ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    {
        "DnsSupport": NotRequired[DnsSupportValueType],
        "SecurityGroupReferencingSupport": NotRequired[SecurityGroupReferencingSupportValueType],
        "Ipv6Support": NotRequired[Ipv6SupportValueType],
        "ApplianceModeSupport": NotRequired[ApplianceModeSupportValueType],
    },
)
ModifyVerifiedAccessEndpointEniOptionsTypeDef = TypedDict(
    "ModifyVerifiedAccessEndpointEniOptionsTypeDef",
    {
        "Protocol": NotRequired[VerifiedAccessEndpointProtocolType],
        "Port": NotRequired[int],
    },
)
ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef = TypedDict(
    "ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    {
        "SubnetIds": NotRequired[Sequence[str]],
        "Protocol": NotRequired[VerifiedAccessEndpointProtocolType],
        "Port": NotRequired[int],
    },
)
VerifiedAccessSseSpecificationResponseTypeDef = TypedDict(
    "VerifiedAccessSseSpecificationResponseTypeDef",
    {
        "CustomerManagedKeyEnabled": NotRequired[bool],
        "KmsKeyArn": NotRequired[str],
    },
)
ModifyVerifiedAccessGroupRequestRequestTypeDef = TypedDict(
    "ModifyVerifiedAccessGroupRequestRequestTypeDef",
    {
        "VerifiedAccessGroupId": str,
        "VerifiedAccessInstanceId": NotRequired[str],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
ModifyVerifiedAccessInstanceRequestRequestTypeDef = TypedDict(
    "ModifyVerifiedAccessInstanceRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)
ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef = TypedDict(
    "ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef",
    {
        "PublicSigningKeyUrl": NotRequired[str],
    },
)
ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef = TypedDict(
    "ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef",
    {
        "Issuer": NotRequired[str],
        "AuthorizationEndpoint": NotRequired[str],
        "TokenEndpoint": NotRequired[str],
        "UserInfoEndpoint": NotRequired[str],
        "ClientId": NotRequired[str],
        "ClientSecret": NotRequired[str],
        "Scope": NotRequired[str],
    },
)
ModifyVolumeRequestRequestTypeDef = TypedDict(
    "ModifyVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "DryRun": NotRequired[bool],
        "Size": NotRequired[int],
        "VolumeType": NotRequired[VolumeTypeType],
        "Iops": NotRequired[int],
        "Throughput": NotRequired[int],
        "MultiAttachEnabled": NotRequired[bool],
    },
)
ModifyVpcEndpointConnectionNotificationRequestRequestTypeDef = TypedDict(
    "ModifyVpcEndpointConnectionNotificationRequestRequestTypeDef",
    {
        "ConnectionNotificationId": str,
        "DryRun": NotRequired[bool],
        "ConnectionNotificationArn": NotRequired[str],
        "ConnectionEvents": NotRequired[Sequence[str]],
    },
)
ModifyVpcEndpointServiceConfigurationRequestRequestTypeDef = TypedDict(
    "ModifyVpcEndpointServiceConfigurationRequestRequestTypeDef",
    {
        "ServiceId": str,
        "DryRun": NotRequired[bool],
        "PrivateDnsName": NotRequired[str],
        "RemovePrivateDnsName": NotRequired[bool],
        "AcceptanceRequired": NotRequired[bool],
        "AddNetworkLoadBalancerArns": NotRequired[Sequence[str]],
        "RemoveNetworkLoadBalancerArns": NotRequired[Sequence[str]],
        "AddGatewayLoadBalancerArns": NotRequired[Sequence[str]],
        "RemoveGatewayLoadBalancerArns": NotRequired[Sequence[str]],
        "AddSupportedIpAddressTypes": NotRequired[Sequence[str]],
        "RemoveSupportedIpAddressTypes": NotRequired[Sequence[str]],
    },
)
ModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef = TypedDict(
    "ModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef",
    {
        "ServiceId": str,
        "PayerResponsibility": Literal["ServiceOwner"],
        "DryRun": NotRequired[bool],
    },
)
ModifyVpcEndpointServicePermissionsRequestRequestTypeDef = TypedDict(
    "ModifyVpcEndpointServicePermissionsRequestRequestTypeDef",
    {
        "ServiceId": str,
        "DryRun": NotRequired[bool],
        "AddAllowedPrincipals": NotRequired[Sequence[str]],
        "RemoveAllowedPrincipals": NotRequired[Sequence[str]],
    },
)
PeeringConnectionOptionsRequestTypeDef = TypedDict(
    "PeeringConnectionOptionsRequestTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalClassicLinkToRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalVpcToRemoteClassicLink": NotRequired[bool],
    },
)
PeeringConnectionOptionsTypeDef = TypedDict(
    "PeeringConnectionOptionsTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalClassicLinkToRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalVpcToRemoteClassicLink": NotRequired[bool],
    },
)
ModifyVpcTenancyRequestRequestTypeDef = TypedDict(
    "ModifyVpcTenancyRequestRequestTypeDef",
    {
        "VpcId": str,
        "InstanceTenancy": Literal["default"],
        "DryRun": NotRequired[bool],
    },
)
ModifyVpnConnectionOptionsRequestRequestTypeDef = TypedDict(
    "ModifyVpnConnectionOptionsRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "LocalIpv4NetworkCidr": NotRequired[str],
        "RemoteIpv4NetworkCidr": NotRequired[str],
        "LocalIpv6NetworkCidr": NotRequired[str],
        "RemoteIpv6NetworkCidr": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
ModifyVpnConnectionRequestRequestTypeDef = TypedDict(
    "ModifyVpnConnectionRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "TransitGatewayId": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "VpnGatewayId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
ModifyVpnTunnelCertificateRequestRequestTypeDef = TypedDict(
    "ModifyVpnTunnelCertificateRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
        "DryRun": NotRequired[bool],
    },
)
Phase1DHGroupNumbersRequestListValueTypeDef = TypedDict(
    "Phase1DHGroupNumbersRequestListValueTypeDef",
    {
        "Value": NotRequired[int],
    },
)
Phase1EncryptionAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase1EncryptionAlgorithmsRequestListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
Phase1IntegrityAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase1IntegrityAlgorithmsRequestListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
Phase2DHGroupNumbersRequestListValueTypeDef = TypedDict(
    "Phase2DHGroupNumbersRequestListValueTypeDef",
    {
        "Value": NotRequired[int],
    },
)
Phase2EncryptionAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase2EncryptionAlgorithmsRequestListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
Phase2IntegrityAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase2IntegrityAlgorithmsRequestListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
MonitorInstancesRequestInstanceMonitorTypeDef = TypedDict(
    "MonitorInstancesRequestInstanceMonitorTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
MonitorInstancesRequestRequestTypeDef = TypedDict(
    "MonitorInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
MoveAddressToVpcRequestRequestTypeDef = TypedDict(
    "MoveAddressToVpcRequestRequestTypeDef",
    {
        "PublicIp": str,
        "DryRun": NotRequired[bool],
    },
)
MoveByoipCidrToIpamRequestRequestTypeDef = TypedDict(
    "MoveByoipCidrToIpamRequestRequestTypeDef",
    {
        "Cidr": str,
        "IpamPoolId": str,
        "IpamPoolOwner": str,
        "DryRun": NotRequired[bool],
    },
)
ProvisionedBandwidthTypeDef = TypedDict(
    "ProvisionedBandwidthTypeDef",
    {
        "ProvisionTime": NotRequired[datetime],
        "Provisioned": NotRequired[str],
        "RequestTime": NotRequired[datetime],
        "Requested": NotRequired[str],
        "Status": NotRequired[str],
    },
)
NetworkAclAssociationTypeDef = TypedDict(
    "NetworkAclAssociationTypeDef",
    {
        "NetworkAclAssociationId": NotRequired[str],
        "NetworkAclId": NotRequired[str],
        "SubnetId": NotRequired[str],
    },
)
NetworkCardInfoTypeDef = TypedDict(
    "NetworkCardInfoTypeDef",
    {
        "NetworkCardIndex": NotRequired[int],
        "NetworkPerformance": NotRequired[str],
        "MaximumNetworkInterfaces": NotRequired[int],
        "BaselineBandwidthInGbps": NotRequired[float],
        "PeakBandwidthInGbps": NotRequired[float],
    },
)
NetworkInterfaceAssociationTypeDef = TypedDict(
    "NetworkInterfaceAssociationTypeDef",
    {
        "AllocationId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "IpOwnerId": NotRequired[str],
        "PublicDnsName": NotRequired[str],
        "PublicIp": NotRequired[str],
        "CustomerOwnedIp": NotRequired[str],
        "CarrierIp": NotRequired[str],
    },
)
NetworkInterfaceIpv6AddressTypeDef = TypedDict(
    "NetworkInterfaceIpv6AddressTypeDef",
    {
        "Ipv6Address": NotRequired[str],
        "IsPrimaryIpv6": NotRequired[bool],
    },
)
NetworkInterfacePermissionStateTypeDef = TypedDict(
    "NetworkInterfacePermissionStateTypeDef",
    {
        "State": NotRequired[NetworkInterfacePermissionStateCodeType],
        "StatusMessage": NotRequired[str],
    },
)
OidcOptionsTypeDef = TypedDict(
    "OidcOptionsTypeDef",
    {
        "Issuer": NotRequired[str],
        "AuthorizationEndpoint": NotRequired[str],
        "TokenEndpoint": NotRequired[str],
        "UserInfoEndpoint": NotRequired[str],
        "ClientId": NotRequired[str],
        "ClientSecret": NotRequired[str],
        "Scope": NotRequired[str],
    },
)
PacketHeaderStatementRequestTypeDef = TypedDict(
    "PacketHeaderStatementRequestTypeDef",
    {
        "SourceAddresses": NotRequired[Sequence[str]],
        "DestinationAddresses": NotRequired[Sequence[str]],
        "SourcePorts": NotRequired[Sequence[str]],
        "DestinationPorts": NotRequired[Sequence[str]],
        "SourcePrefixLists": NotRequired[Sequence[str]],
        "DestinationPrefixLists": NotRequired[Sequence[str]],
        "Protocols": NotRequired[Sequence[ProtocolType]],
    },
)
PacketHeaderStatementTypeDef = TypedDict(
    "PacketHeaderStatementTypeDef",
    {
        "SourceAddresses": NotRequired[List[str]],
        "DestinationAddresses": NotRequired[List[str]],
        "SourcePorts": NotRequired[List[str]],
        "DestinationPorts": NotRequired[List[str]],
        "SourcePrefixLists": NotRequired[List[str]],
        "DestinationPrefixLists": NotRequired[List[str]],
        "Protocols": NotRequired[List[ProtocolType]],
    },
)
RequestFilterPortRangeTypeDef = TypedDict(
    "RequestFilterPortRangeTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)
ResourceStatementRequestTypeDef = TypedDict(
    "ResourceStatementRequestTypeDef",
    {
        "Resources": NotRequired[Sequence[str]],
        "ResourceTypes": NotRequired[Sequence[str]],
    },
)
ResourceStatementTypeDef = TypedDict(
    "ResourceStatementTypeDef",
    {
        "Resources": NotRequired[List[str]],
        "ResourceTypes": NotRequired[List[str]],
    },
)
PeeringAttachmentStatusTypeDef = TypedDict(
    "PeeringAttachmentStatusTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
PeeringTgwInfoTypeDef = TypedDict(
    "PeeringTgwInfoTypeDef",
    {
        "TransitGatewayId": NotRequired[str],
        "CoreNetworkId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Region": NotRequired[str],
    },
)
Phase1DHGroupNumbersListValueTypeDef = TypedDict(
    "Phase1DHGroupNumbersListValueTypeDef",
    {
        "Value": NotRequired[int],
    },
)
Phase1EncryptionAlgorithmsListValueTypeDef = TypedDict(
    "Phase1EncryptionAlgorithmsListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
Phase1IntegrityAlgorithmsListValueTypeDef = TypedDict(
    "Phase1IntegrityAlgorithmsListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
Phase2DHGroupNumbersListValueTypeDef = TypedDict(
    "Phase2DHGroupNumbersListValueTypeDef",
    {
        "Value": NotRequired[int],
    },
)
Phase2EncryptionAlgorithmsListValueTypeDef = TypedDict(
    "Phase2EncryptionAlgorithmsListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
Phase2IntegrityAlgorithmsListValueTypeDef = TypedDict(
    "Phase2IntegrityAlgorithmsListValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
PriceScheduleTypeDef = TypedDict(
    "PriceScheduleTypeDef",
    {
        "Active": NotRequired[bool],
        "CurrencyCode": NotRequired[Literal["USD"]],
        "Price": NotRequired[float],
        "Term": NotRequired[int],
    },
)
PricingDetailTypeDef = TypedDict(
    "PricingDetailTypeDef",
    {
        "Count": NotRequired[int],
        "Price": NotRequired[float],
    },
)
PrivateDnsDetailsTypeDef = TypedDict(
    "PrivateDnsDetailsTypeDef",
    {
        "PrivateDnsName": NotRequired[str],
    },
)
PrivateDnsNameConfigurationTypeDef = TypedDict(
    "PrivateDnsNameConfigurationTypeDef",
    {
        "State": NotRequired[DnsNameStateType],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
        "Name": NotRequired[str],
    },
)
PrivateDnsNameOptionsOnLaunchTypeDef = TypedDict(
    "PrivateDnsNameOptionsOnLaunchTypeDef",
    {
        "HostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)
PrivateDnsNameOptionsRequestTypeDef = TypedDict(
    "PrivateDnsNameOptionsRequestTypeDef",
    {
        "HostnameType": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
    },
)
PropagatingVgwTypeDef = TypedDict(
    "PropagatingVgwTypeDef",
    {
        "GatewayId": NotRequired[str],
    },
)
ProvisionPublicIpv4PoolCidrRequestRequestTypeDef = TypedDict(
    "ProvisionPublicIpv4PoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "PoolId": str,
        "NetmaskLength": int,
        "DryRun": NotRequired[bool],
    },
)
PublicIpv4PoolRangeTypeDef = TypedDict(
    "PublicIpv4PoolRangeTypeDef",
    {
        "FirstAddress": NotRequired[str],
        "LastAddress": NotRequired[str],
        "AddressCount": NotRequired[int],
        "AvailableAddressCount": NotRequired[int],
    },
)
PurchaseRequestTypeDef = TypedDict(
    "PurchaseRequestTypeDef",
    {
        "InstanceCount": int,
        "PurchaseToken": str,
    },
)
ReservedInstanceLimitPriceTypeDef = TypedDict(
    "ReservedInstanceLimitPriceTypeDef",
    {
        "Amount": NotRequired[float],
        "CurrencyCode": NotRequired[Literal["USD"]],
    },
)
RebootInstancesRequestInstanceRebootTypeDef = TypedDict(
    "RebootInstancesRequestInstanceRebootTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
RebootInstancesRequestRequestTypeDef = TypedDict(
    "RebootInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "Amount": NotRequired[float],
        "Frequency": NotRequired[Literal["Hourly"]],
    },
)
ReferencedSecurityGroupTypeDef = TypedDict(
    "ReferencedSecurityGroupTypeDef",
    {
        "GroupId": NotRequired[str],
        "PeeringStatus": NotRequired[str],
        "UserId": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)
RegisterInstanceTagAttributeRequestTypeDef = TypedDict(
    "RegisterInstanceTagAttributeRequestTypeDef",
    {
        "IncludeAllTagsOfInstance": NotRequired[bool],
        "InstanceTagKeys": NotRequired[Sequence[str]],
    },
)
RegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "NetworkInterfaceIds": Sequence[str],
        "GroupIpAddress": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
TransitGatewayMulticastRegisteredGroupMembersTypeDef = TypedDict(
    "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "RegisteredNetworkInterfaceIds": NotRequired[List[str]],
        "GroupIpAddress": NotRequired[str],
    },
)
RegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "NetworkInterfaceIds": Sequence[str],
        "GroupIpAddress": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
TransitGatewayMulticastRegisteredGroupSourcesTypeDef = TypedDict(
    "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "RegisteredNetworkInterfaceIds": NotRequired[List[str]],
        "GroupIpAddress": NotRequired[str],
    },
)
RejectTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef = TypedDict(
    "RejectTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
RejectTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "RejectTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)
RejectTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "RejectTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": NotRequired[bool],
    },
)
RejectVpcEndpointConnectionsRequestRequestTypeDef = TypedDict(
    "RejectVpcEndpointConnectionsRequestRequestTypeDef",
    {
        "ServiceId": str,
        "VpcEndpointIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
RejectVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "RejectVpcPeeringConnectionRequestRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
        "DryRun": NotRequired[bool],
    },
)
RejectVpcPeeringConnectionRequestVpcPeeringConnectionRejectTypeDef = TypedDict(
    "RejectVpcPeeringConnectionRequestVpcPeeringConnectionRejectTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
ReleaseAddressRequestClassicAddressReleaseTypeDef = TypedDict(
    "ReleaseAddressRequestClassicAddressReleaseTypeDef",
    {
        "AllocationId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
ReleaseAddressRequestRequestTypeDef = TypedDict(
    "ReleaseAddressRequestRequestTypeDef",
    {
        "AllocationId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
ReleaseAddressRequestVpcAddressReleaseTypeDef = TypedDict(
    "ReleaseAddressRequestVpcAddressReleaseTypeDef",
    {
        "AllocationId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
ReleaseHostsRequestRequestTypeDef = TypedDict(
    "ReleaseHostsRequestRequestTypeDef",
    {
        "HostIds": Sequence[str],
    },
)
ReleaseIpamPoolAllocationRequestRequestTypeDef = TypedDict(
    "ReleaseIpamPoolAllocationRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "Cidr": str,
        "IpamPoolAllocationId": str,
        "DryRun": NotRequired[bool],
    },
)
ReplaceNetworkAclAssociationRequestNetworkAclReplaceAssociationTypeDef = TypedDict(
    "ReplaceNetworkAclAssociationRequestNetworkAclReplaceAssociationTypeDef",
    {
        "AssociationId": str,
        "DryRun": NotRequired[bool],
    },
)
ReplaceNetworkAclAssociationRequestRequestTypeDef = TypedDict(
    "ReplaceNetworkAclAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
        "NetworkAclId": str,
        "DryRun": NotRequired[bool],
    },
)
ReplaceRouteRequestRequestTypeDef = TypedDict(
    "ReplaceRouteRequestRequestTypeDef",
    {
        "RouteTableId": str,
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "VpcEndpointId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "LocalTarget": NotRequired[bool],
        "NatGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "CarrierGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
    },
)
ReplaceRouteRequestRouteReplaceTypeDef = TypedDict(
    "ReplaceRouteRequestRouteReplaceTypeDef",
    {
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "VpcEndpointId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "LocalTarget": NotRequired[bool],
        "NatGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "CarrierGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
    },
)
ReplaceRouteTableAssociationRequestRequestTypeDef = TypedDict(
    "ReplaceRouteTableAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)
ReplaceRouteTableAssociationRequestRouteTableAssociationReplaceSubnetTypeDef = TypedDict(
    "ReplaceRouteTableAssociationRequestRouteTableAssociationReplaceSubnetTypeDef",
    {
        "RouteTableId": str,
        "DryRun": NotRequired[bool],
    },
)
ReplaceTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "ReplaceTransitGatewayRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": NotRequired[str],
        "Blackhole": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)
ReplaceVpnTunnelRequestRequestTypeDef = TypedDict(
    "ReplaceVpnTunnelRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
        "ApplyPendingMaintenance": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)
ReservedInstancesIdTypeDef = TypedDict(
    "ReservedInstancesIdTypeDef",
    {
        "ReservedInstancesId": NotRequired[str],
    },
)
ResetAddressAttributeRequestRequestTypeDef = TypedDict(
    "ResetAddressAttributeRequestRequestTypeDef",
    {
        "AllocationId": str,
        "Attribute": Literal["domain-name"],
        "DryRun": NotRequired[bool],
    },
)
ResetEbsDefaultKmsKeyIdRequestRequestTypeDef = TypedDict(
    "ResetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
ResetFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "ResetFpgaImageAttributeRequestRequestTypeDef",
    {
        "FpgaImageId": str,
        "DryRun": NotRequired[bool],
        "Attribute": NotRequired[Literal["loadPermission"]],
    },
)
ResetImageAttributeRequestImageResetAttributeTypeDef = TypedDict(
    "ResetImageAttributeRequestImageResetAttributeTypeDef",
    {
        "Attribute": Literal["launchPermission"],
        "DryRun": NotRequired[bool],
    },
)
ResetImageAttributeRequestRequestTypeDef = TypedDict(
    "ResetImageAttributeRequestRequestTypeDef",
    {
        "Attribute": Literal["launchPermission"],
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)
ResetInstanceAttributeRequestInstanceResetAttributeTypeDef = TypedDict(
    "ResetInstanceAttributeRequestInstanceResetAttributeTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)
ResetInstanceAttributeRequestInstanceResetKernelTypeDef = TypedDict(
    "ResetInstanceAttributeRequestInstanceResetKernelTypeDef",
    {
        "Attribute": NotRequired[InstanceAttributeNameType],
        "DryRun": NotRequired[bool],
    },
)
ResetInstanceAttributeRequestInstanceResetRamdiskTypeDef = TypedDict(
    "ResetInstanceAttributeRequestInstanceResetRamdiskTypeDef",
    {
        "Attribute": NotRequired[InstanceAttributeNameType],
        "DryRun": NotRequired[bool],
    },
)
ResetInstanceAttributeRequestInstanceResetSourceDestCheckTypeDef = TypedDict(
    "ResetInstanceAttributeRequestInstanceResetSourceDestCheckTypeDef",
    {
        "Attribute": NotRequired[InstanceAttributeNameType],
        "DryRun": NotRequired[bool],
    },
)
ResetInstanceAttributeRequestRequestTypeDef = TypedDict(
    "ResetInstanceAttributeRequestRequestTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)
ResetNetworkInterfaceAttributeRequestNetworkInterfaceResetAttributeTypeDef = TypedDict(
    "ResetNetworkInterfaceAttributeRequestNetworkInterfaceResetAttributeTypeDef",
    {
        "DryRun": NotRequired[bool],
        "SourceDestCheck": NotRequired[str],
    },
)
ResetNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "ResetNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "DryRun": NotRequired[bool],
        "SourceDestCheck": NotRequired[str],
    },
)
ResetSnapshotAttributeRequestRequestTypeDef = TypedDict(
    "ResetSnapshotAttributeRequestRequestTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "SnapshotId": str,
        "DryRun": NotRequired[bool],
    },
)
ResetSnapshotAttributeRequestSnapshotResetAttributeTypeDef = TypedDict(
    "ResetSnapshotAttributeRequestSnapshotResetAttributeTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "DryRun": NotRequired[bool],
    },
)
RestoreAddressToClassicRequestRequestTypeDef = TypedDict(
    "RestoreAddressToClassicRequestRequestTypeDef",
    {
        "PublicIp": str,
        "DryRun": NotRequired[bool],
    },
)
RestoreImageFromRecycleBinRequestRequestTypeDef = TypedDict(
    "RestoreImageFromRecycleBinRequestRequestTypeDef",
    {
        "ImageId": str,
        "DryRun": NotRequired[bool],
    },
)
RestoreManagedPrefixListVersionRequestRequestTypeDef = TypedDict(
    "RestoreManagedPrefixListVersionRequestRequestTypeDef",
    {
        "PrefixListId": str,
        "PreviousVersion": int,
        "CurrentVersion": int,
        "DryRun": NotRequired[bool],
    },
)
RestoreSnapshotFromRecycleBinRequestRequestTypeDef = TypedDict(
    "RestoreSnapshotFromRecycleBinRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "DryRun": NotRequired[bool],
    },
)
RestoreSnapshotTierRequestRequestTypeDef = TypedDict(
    "RestoreSnapshotTierRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "TemporaryRestoreDays": NotRequired[int],
        "PermanentRestore": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)
RevokeClientVpnIngressRequestRequestTypeDef = TypedDict(
    "RevokeClientVpnIngressRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "TargetNetworkCidr": str,
        "AccessGroupId": NotRequired[str],
        "RevokeAllGroups": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)
RouteTypeDef = TypedDict(
    "RouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceOwnerId": NotRequired[str],
        "NatGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "CarrierGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "Origin": NotRequired[RouteOriginType],
        "State": NotRequired[RouteStateType],
        "VpcPeeringConnectionId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
    },
)
ScheduledInstanceRecurrenceTypeDef = TypedDict(
    "ScheduledInstanceRecurrenceTypeDef",
    {
        "Frequency": NotRequired[str],
        "Interval": NotRequired[int],
        "OccurrenceDaySet": NotRequired[List[int]],
        "OccurrenceRelativeToEnd": NotRequired[bool],
        "OccurrenceUnit": NotRequired[str],
    },
)
ScheduledInstancesEbsTypeDef = TypedDict(
    "ScheduledInstancesEbsTypeDef",
    {
        "DeleteOnTermination": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "Iops": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[str],
    },
)
ScheduledInstancesIamInstanceProfileTypeDef = TypedDict(
    "ScheduledInstancesIamInstanceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ScheduledInstancesIpv6AddressTypeDef = TypedDict(
    "ScheduledInstancesIpv6AddressTypeDef",
    {
        "Ipv6Address": NotRequired[str],
    },
)
ScheduledInstancesMonitoringTypeDef = TypedDict(
    "ScheduledInstancesMonitoringTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
ScheduledInstancesPlacementTypeDef = TypedDict(
    "ScheduledInstancesPlacementTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "GroupName": NotRequired[str],
    },
)
ScheduledInstancesPrivateIpAddressConfigTypeDef = TypedDict(
    "ScheduledInstancesPrivateIpAddressConfigTypeDef",
    {
        "Primary": NotRequired[bool],
        "PrivateIpAddress": NotRequired[str],
    },
)
TransitGatewayMulticastGroupTypeDef = TypedDict(
    "TransitGatewayMulticastGroupTypeDef",
    {
        "GroupIpAddress": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "ResourceOwnerId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "GroupMember": NotRequired[bool],
        "GroupSource": NotRequired[bool],
        "MemberType": NotRequired[MembershipTypeType],
        "SourceType": NotRequired[MembershipTypeType],
    },
)
SecurityGroupIdentifierTypeDef = TypedDict(
    "SecurityGroupIdentifierTypeDef",
    {
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
    },
)
SecurityGroupRuleDescriptionTypeDef = TypedDict(
    "SecurityGroupRuleDescriptionTypeDef",
    {
        "SecurityGroupRuleId": NotRequired[str],
        "Description": NotRequired[str],
    },
)
SecurityGroupRuleRequestTypeDef = TypedDict(
    "SecurityGroupRuleRequestTypeDef",
    {
        "IpProtocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
        "CidrIpv4": NotRequired[str],
        "CidrIpv6": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "ReferencedGroupId": NotRequired[str],
        "Description": NotRequired[str],
    },
)
SendDiagnosticInterruptRequestRequestTypeDef = TypedDict(
    "SendDiagnosticInterruptRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
    },
)
ServiceTypeDetailTypeDef = TypedDict(
    "ServiceTypeDetailTypeDef",
    {
        "ServiceType": NotRequired[ServiceTypeType],
    },
)
UserBucketDetailsTypeDef = TypedDict(
    "UserBucketDetailsTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
    },
)
SpotCapacityRebalanceTypeDef = TypedDict(
    "SpotCapacityRebalanceTypeDef",
    {
        "ReplacementStrategy": NotRequired[ReplacementStrategyType],
        "TerminationDelay": NotRequired[int],
    },
)
SpotInstanceStateFaultTypeDef = TypedDict(
    "SpotInstanceStateFaultTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
SpotFleetMonitoringTypeDef = TypedDict(
    "SpotFleetMonitoringTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
SpotInstanceStatusTypeDef = TypedDict(
    "SpotInstanceStatusTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
        "UpdateTime": NotRequired[datetime],
    },
)
StartInstancesRequestInstanceStartTypeDef = TypedDict(
    "StartInstancesRequestInstanceStartTypeDef",
    {
        "AdditionalInfo": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
StartInstancesRequestRequestTypeDef = TypedDict(
    "StartInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "AdditionalInfo": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
StartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef = TypedDict(
    "StartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef",
    {
        "ServiceId": str,
        "DryRun": NotRequired[bool],
    },
)
StopInstancesRequestInstanceStopTypeDef = TypedDict(
    "StopInstancesRequestInstanceStopTypeDef",
    {
        "Hibernate": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "Force": NotRequired[bool],
    },
)
StopInstancesRequestRequestTypeDef = TypedDict(
    "StopInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "Hibernate": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "Force": NotRequired[bool],
    },
)
SubnetAssociationTypeDef = TypedDict(
    "SubnetAssociationTypeDef",
    {
        "SubnetId": NotRequired[str],
        "State": NotRequired[TransitGatewayMulitcastDomainAssociationStateType],
    },
)
SubnetCidrBlockStateTypeDef = TypedDict(
    "SubnetCidrBlockStateTypeDef",
    {
        "State": NotRequired[SubnetCidrBlockStateCodeType],
        "StatusMessage": NotRequired[str],
    },
)
TargetConfigurationTypeDef = TypedDict(
    "TargetConfigurationTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "OfferingId": NotRequired[str],
    },
)
TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
TerminateClientVpnConnectionsRequestRequestTypeDef = TypedDict(
    "TerminateClientVpnConnectionsRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "ConnectionId": NotRequired[str],
        "Username": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
TerminateInstancesRequestInstanceTerminateTypeDef = TypedDict(
    "TerminateInstancesRequestInstanceTerminateTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
TerminateInstancesRequestRequestTypeDef = TypedDict(
    "TerminateInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
TrafficMirrorPortRangeTypeDef = TypedDict(
    "TrafficMirrorPortRangeTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)
TransitGatewayAttachmentAssociationTypeDef = TypedDict(
    "TransitGatewayAttachmentAssociationTypeDef",
    {
        "TransitGatewayRouteTableId": NotRequired[str],
        "State": NotRequired[TransitGatewayAssociationStateType],
    },
)
TransitGatewayAttachmentBgpConfigurationTypeDef = TypedDict(
    "TransitGatewayAttachmentBgpConfigurationTypeDef",
    {
        "TransitGatewayAsn": NotRequired[int],
        "PeerAsn": NotRequired[int],
        "TransitGatewayAddress": NotRequired[str],
        "PeerAddress": NotRequired[str],
        "BgpStatus": NotRequired[BgpStatusType],
    },
)
TransitGatewayConnectOptionsTypeDef = TypedDict(
    "TransitGatewayConnectOptionsTypeDef",
    {
        "Protocol": NotRequired[Literal["gre"]],
    },
)
TransitGatewayMulticastDomainOptionsTypeDef = TypedDict(
    "TransitGatewayMulticastDomainOptionsTypeDef",
    {
        "Igmpv2Support": NotRequired[Igmpv2SupportValueType],
        "StaticSourcesSupport": NotRequired[StaticSourcesSupportValueType],
        "AutoAcceptSharedAssociations": NotRequired[AutoAcceptSharedAssociationsValueType],
    },
)
TransitGatewayOptionsTypeDef = TypedDict(
    "TransitGatewayOptionsTypeDef",
    {
        "AmazonSideAsn": NotRequired[int],
        "TransitGatewayCidrBlocks": NotRequired[List[str]],
        "AutoAcceptSharedAttachments": NotRequired[AutoAcceptSharedAttachmentsValueType],
        "DefaultRouteTableAssociation": NotRequired[DefaultRouteTableAssociationValueType],
        "AssociationDefaultRouteTableId": NotRequired[str],
        "DefaultRouteTablePropagation": NotRequired[DefaultRouteTablePropagationValueType],
        "PropagationDefaultRouteTableId": NotRequired[str],
        "VpnEcmpSupport": NotRequired[VpnEcmpSupportValueType],
        "DnsSupport": NotRequired[DnsSupportValueType],
        "SecurityGroupReferencingSupport": NotRequired[SecurityGroupReferencingSupportValueType],
        "MulticastSupport": NotRequired[MulticastSupportValueType],
    },
)
TransitGatewayPeeringAttachmentOptionsTypeDef = TypedDict(
    "TransitGatewayPeeringAttachmentOptionsTypeDef",
    {
        "DynamicRouting": NotRequired[DynamicRoutingValueType],
    },
)
TransitGatewayPolicyRuleMetaDataTypeDef = TypedDict(
    "TransitGatewayPolicyRuleMetaDataTypeDef",
    {
        "MetaDataKey": NotRequired[str],
        "MetaDataValue": NotRequired[str],
    },
)
TransitGatewayPrefixListAttachmentTypeDef = TypedDict(
    "TransitGatewayPrefixListAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "ResourceId": NotRequired[str],
    },
)
TransitGatewayRouteAttachmentTypeDef = TypedDict(
    "TransitGatewayRouteAttachmentTypeDef",
    {
        "ResourceId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
    },
)
TransitGatewayVpcAttachmentOptionsTypeDef = TypedDict(
    "TransitGatewayVpcAttachmentOptionsTypeDef",
    {
        "DnsSupport": NotRequired[DnsSupportValueType],
        "SecurityGroupReferencingSupport": NotRequired[SecurityGroupReferencingSupportValueType],
        "Ipv6Support": NotRequired[Ipv6SupportValueType],
        "ApplianceModeSupport": NotRequired[ApplianceModeSupportValueType],
    },
)
UnassignIpv6AddressesRequestRequestTypeDef = TypedDict(
    "UnassignIpv6AddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Ipv6Addresses": NotRequired[Sequence[str]],
        "Ipv6Prefixes": NotRequired[Sequence[str]],
    },
)
UnassignPrivateIpAddressesRequestNetworkInterfaceUnassignPrivateIpAddressesTypeDef = TypedDict(
    "UnassignPrivateIpAddressesRequestNetworkInterfaceUnassignPrivateIpAddressesTypeDef",
    {
        "PrivateIpAddresses": NotRequired[Sequence[str]],
        "Ipv4Prefixes": NotRequired[Sequence[str]],
    },
)
UnassignPrivateIpAddressesRequestRequestTypeDef = TypedDict(
    "UnassignPrivateIpAddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "PrivateIpAddresses": NotRequired[Sequence[str]],
        "Ipv4Prefixes": NotRequired[Sequence[str]],
    },
)
UnassignPrivateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "UnassignPrivateNatGatewayAddressRequestRequestTypeDef",
    {
        "NatGatewayId": str,
        "PrivateIpAddresses": Sequence[str],
        "MaxDrainDurationSeconds": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
UnlockSnapshotRequestRequestTypeDef = TypedDict(
    "UnlockSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "DryRun": NotRequired[bool],
    },
)
UnmonitorInstancesRequestInstanceUnmonitorTypeDef = TypedDict(
    "UnmonitorInstancesRequestInstanceUnmonitorTypeDef",
    {
        "DryRun": NotRequired[bool],
    },
)
UnmonitorInstancesRequestRequestTypeDef = TypedDict(
    "UnmonitorInstancesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
    },
)
UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef = TypedDict(
    "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    {
        "Code": NotRequired[UnsuccessfulInstanceCreditSpecificationErrorCodeType],
        "Message": NotRequired[str],
    },
)
UnsuccessfulItemErrorTypeDef = TypedDict(
    "UnsuccessfulItemErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
VerifiedAccessEndpointEniOptionsTypeDef = TypedDict(
    "VerifiedAccessEndpointEniOptionsTypeDef",
    {
        "NetworkInterfaceId": NotRequired[str],
        "Protocol": NotRequired[VerifiedAccessEndpointProtocolType],
        "Port": NotRequired[int],
    },
)
VerifiedAccessEndpointLoadBalancerOptionsTypeDef = TypedDict(
    "VerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    {
        "Protocol": NotRequired[VerifiedAccessEndpointProtocolType],
        "Port": NotRequired[int],
        "LoadBalancerArn": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
    },
)
VerifiedAccessEndpointStatusTypeDef = TypedDict(
    "VerifiedAccessEndpointStatusTypeDef",
    {
        "Code": NotRequired[VerifiedAccessEndpointStatusCodeType],
        "Message": NotRequired[str],
    },
)
VerifiedAccessTrustProviderCondensedTypeDef = TypedDict(
    "VerifiedAccessTrustProviderCondensedTypeDef",
    {
        "VerifiedAccessTrustProviderId": NotRequired[str],
        "Description": NotRequired[str],
        "TrustProviderType": NotRequired[TrustProviderTypeType],
        "UserTrustProviderType": NotRequired[UserTrustProviderTypeType],
        "DeviceTrustProviderType": NotRequired[DeviceTrustProviderTypeType],
    },
)
VerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef = TypedDict(
    "VerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef",
    {
        "Enabled": bool,
        "LogGroup": NotRequired[str],
    },
)
VerifiedAccessLogDeliveryStatusTypeDef = TypedDict(
    "VerifiedAccessLogDeliveryStatusTypeDef",
    {
        "Code": NotRequired[VerifiedAccessLogDeliveryStatusCodeType],
        "Message": NotRequired[str],
    },
)
VerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef = TypedDict(
    "VerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef",
    {
        "Enabled": bool,
        "DeliveryStream": NotRequired[str],
    },
)
VerifiedAccessLogS3DestinationOptionsTypeDef = TypedDict(
    "VerifiedAccessLogS3DestinationOptionsTypeDef",
    {
        "Enabled": bool,
        "BucketName": NotRequired[str],
        "Prefix": NotRequired[str],
        "BucketOwner": NotRequired[str],
    },
)
VgwTelemetryTypeDef = TypedDict(
    "VgwTelemetryTypeDef",
    {
        "AcceptedRouteCount": NotRequired[int],
        "LastStatusChange": NotRequired[datetime],
        "OutsideIpAddress": NotRequired[str],
        "Status": NotRequired[TelemetryStatusType],
        "StatusMessage": NotRequired[str],
        "CertificateArn": NotRequired[str],
    },
)
VolumeStatusActionTypeDef = TypedDict(
    "VolumeStatusActionTypeDef",
    {
        "Code": NotRequired[str],
        "Description": NotRequired[str],
        "EventId": NotRequired[str],
        "EventType": NotRequired[str],
    },
)
VolumeStatusAttachmentStatusTypeDef = TypedDict(
    "VolumeStatusAttachmentStatusTypeDef",
    {
        "IoPerformance": NotRequired[str],
        "InstanceId": NotRequired[str],
    },
)
VolumeStatusDetailsTypeDef = TypedDict(
    "VolumeStatusDetailsTypeDef",
    {
        "Name": NotRequired[VolumeStatusNameType],
        "Status": NotRequired[str],
    },
)
VolumeStatusEventTypeDef = TypedDict(
    "VolumeStatusEventTypeDef",
    {
        "Description": NotRequired[str],
        "EventId": NotRequired[str],
        "EventType": NotRequired[str],
        "NotAfter": NotRequired[datetime],
        "NotBefore": NotRequired[datetime],
        "InstanceId": NotRequired[str],
    },
)
VpcCidrBlockStateTypeDef = TypedDict(
    "VpcCidrBlockStateTypeDef",
    {
        "State": NotRequired[VpcCidrBlockStateCodeType],
        "StatusMessage": NotRequired[str],
    },
)
VpcPeeringConnectionOptionsDescriptionTypeDef = TypedDict(
    "VpcPeeringConnectionOptionsDescriptionTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalClassicLinkToRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalVpcToRemoteClassicLink": NotRequired[bool],
    },
)
VpcPeeringConnectionStateReasonTypeDef = TypedDict(
    "VpcPeeringConnectionStateReasonTypeDef",
    {
        "Code": NotRequired[VpcPeeringConnectionStateReasonCodeType],
        "Message": NotRequired[str],
    },
)
VpnStaticRouteTypeDef = TypedDict(
    "VpnStaticRouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "Source": NotRequired[Literal["Static"]],
        "State": NotRequired[VpnStateType],
    },
)
WithdrawByoipCidrRequestRequestTypeDef = TypedDict(
    "WithdrawByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "DryRun": NotRequired[bool],
    },
)
AcceptAddressTransferResultTypeDef = TypedDict(
    "AcceptAddressTransferResultTypeDef",
    {
        "AddressTransfer": AddressTransferTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptReservedInstancesExchangeQuoteResultTypeDef = TypedDict(
    "AcceptReservedInstancesExchangeQuoteResultTypeDef",
    {
        "ExchangeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AllocateAddressResultTypeDef = TypedDict(
    "AllocateAddressResultTypeDef",
    {
        "PublicIp": str,
        "AllocationId": str,
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "Domain": DomainTypeType,
        "CustomerOwnedIp": str,
        "CustomerOwnedIpv4Pool": str,
        "CarrierIp": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AllocateHostsResultTypeDef = TypedDict(
    "AllocateHostsResultTypeDef",
    {
        "HostIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef = TypedDict(
    "ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef",
    {
        "SecurityGroupIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssignIpv6AddressesResultTypeDef = TypedDict(
    "AssignIpv6AddressesResultTypeDef",
    {
        "AssignedIpv6Addresses": List[str],
        "AssignedIpv6Prefixes": List[str],
        "NetworkInterfaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateAddressResultTypeDef = TypedDict(
    "AssociateAddressResultTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateEnclaveCertificateIamRoleResultTypeDef = TypedDict(
    "AssociateEnclaveCertificateIamRoleResultTypeDef",
    {
        "CertificateS3BucketName": str,
        "CertificateS3ObjectKey": str,
        "EncryptionKmsKeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachClassicLinkVpcResultTypeDef = TypedDict(
    "AttachClassicLinkVpcResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachNetworkInterfaceResultTypeDef = TypedDict(
    "AttachNetworkInterfaceResultTypeDef",
    {
        "AttachmentId": str,
        "NetworkCardIndex": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelCapacityReservationResultTypeDef = TypedDict(
    "CancelCapacityReservationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelImageLaunchPermissionResultTypeDef = TypedDict(
    "CancelImageLaunchPermissionResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelImportTaskResultTypeDef = TypedDict(
    "CancelImportTaskResultTypeDef",
    {
        "ImportTaskId": str,
        "PreviousState": str,
        "State": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfirmProductInstanceResultTypeDef = TypedDict(
    "ConfirmProductInstanceResultTypeDef",
    {
        "OwnerId": str,
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConnectionTrackingConfigurationResponseTypeDef = TypedDict(
    "ConnectionTrackingConfigurationResponseTypeDef",
    {
        "TcpEstablishedTimeout": int,
        "UdpStreamTimeout": int,
        "UdpTimeout": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopyFpgaImageResultTypeDef = TypedDict(
    "CopyFpgaImageResultTypeDef",
    {
        "FpgaImageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopyImageResultTypeDef = TypedDict(
    "CopyImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CpuOptionsResponseTypeDef = TypedDict(
    "CpuOptionsResponseTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
        "AmdSevSnp": AmdSevSnpSpecificationType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFpgaImageResultTypeDef = TypedDict(
    "CreateFpgaImageResultTypeDef",
    {
        "FpgaImageId": str,
        "FpgaImageGlobalId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateImageResultTypeDef = TypedDict(
    "CreateImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePublicIpv4PoolResultTypeDef = TypedDict(
    "CreatePublicIpv4PoolResultTypeDef",
    {
        "PoolId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRestoreImageTaskResultTypeDef = TypedDict(
    "CreateRestoreImageTaskResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRouteResultTypeDef = TypedDict(
    "CreateRouteResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStoreImageTaskResultTypeDef = TypedDict(
    "CreateStoreImageTaskResultTypeDef",
    {
        "ObjectKey": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEgressOnlyInternetGatewayResultTypeDef = TypedDict(
    "DeleteEgressOnlyInternetGatewayResultTypeDef",
    {
        "ReturnCode": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFpgaImageResultTypeDef = TypedDict(
    "DeleteFpgaImageResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteKeyPairResultTypeDef = TypedDict(
    "DeleteKeyPairResultTypeDef",
    {
        "Return": bool,
        "KeyPairId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNatGatewayResultTypeDef = TypedDict(
    "DeleteNatGatewayResultTypeDef",
    {
        "NatGatewayId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef = TypedDict(
    "DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNetworkInsightsAccessScopeResultTypeDef = TypedDict(
    "DeleteNetworkInsightsAccessScopeResultTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNetworkInsightsAnalysisResultTypeDef = TypedDict(
    "DeleteNetworkInsightsAnalysisResultTypeDef",
    {
        "NetworkInsightsAnalysisId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNetworkInsightsPathResultTypeDef = TypedDict(
    "DeleteNetworkInsightsPathResultTypeDef",
    {
        "NetworkInsightsPathId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNetworkInterfacePermissionResultTypeDef = TypedDict(
    "DeleteNetworkInterfacePermissionResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePublicIpv4PoolResultTypeDef = TypedDict(
    "DeletePublicIpv4PoolResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTrafficMirrorFilterResultTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterResultTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterRuleResultTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTrafficMirrorSessionResultTypeDef = TypedDict(
    "DeleteTrafficMirrorSessionResultTypeDef",
    {
        "TrafficMirrorSessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTrafficMirrorTargetResultTypeDef = TypedDict(
    "DeleteTrafficMirrorTargetResultTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVpcPeeringConnectionResultTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeprovisionPublicIpv4PoolCidrResultTypeDef = TypedDict(
    "DeprovisionPublicIpv4PoolCidrResultTypeDef",
    {
        "PoolId": str,
        "DeprovisionedAddresses": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAddressTransfersResultTypeDef = TypedDict(
    "DescribeAddressTransfersResultTypeDef",
    {
        "AddressTransfers": List[AddressTransferTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachClassicLinkVpcResultTypeDef = TypedDict(
    "DetachClassicLinkVpcResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableAddressTransferResultTypeDef = TypedDict(
    "DisableAddressTransferResultTypeDef",
    {
        "AddressTransfer": AddressTransferTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef = TypedDict(
    "DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef",
    {
        "Output": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "DisableEbsEncryptionByDefaultResultTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableImageBlockPublicAccessResultTypeDef = TypedDict(
    "DisableImageBlockPublicAccessResultTypeDef",
    {
        "ImageBlockPublicAccessState": Literal["unblocked"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableImageDeprecationResultTypeDef = TypedDict(
    "DisableImageDeprecationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableImageResultTypeDef = TypedDict(
    "DisableImageResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableIpamOrganizationAdminAccountResultTypeDef = TypedDict(
    "DisableIpamOrganizationAdminAccountResultTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableSerialConsoleAccessResultTypeDef = TypedDict(
    "DisableSerialConsoleAccessResultTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableSnapshotBlockPublicAccessResultTypeDef = TypedDict(
    "DisableSnapshotBlockPublicAccessResultTypeDef",
    {
        "State": SnapshotBlockPublicAccessStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "DisableVpcClassicLinkDnsSupportResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableVpcClassicLinkResultTypeDef = TypedDict(
    "DisableVpcClassicLinkResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateEnclaveCertificateIamRoleResultTypeDef = TypedDict(
    "DisassociateEnclaveCertificateIamRoleResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateTrunkInterfaceResultTypeDef = TypedDict(
    "DisassociateTrunkInterfaceResultTypeDef",
    {
        "Return": bool,
        "ClientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableAddressTransferResultTypeDef = TypedDict(
    "EnableAddressTransferResultTypeDef",
    {
        "AddressTransfer": AddressTransferTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef = TypedDict(
    "EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef",
    {
        "Output": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "EnableEbsEncryptionByDefaultResultTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableImageBlockPublicAccessResultTypeDef = TypedDict(
    "EnableImageBlockPublicAccessResultTypeDef",
    {
        "ImageBlockPublicAccessState": Literal["block-new-sharing"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableImageDeprecationResultTypeDef = TypedDict(
    "EnableImageDeprecationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableImageResultTypeDef = TypedDict(
    "EnableImageResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableIpamOrganizationAdminAccountResultTypeDef = TypedDict(
    "EnableIpamOrganizationAdminAccountResultTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableReachabilityAnalyzerOrganizationSharingResultTypeDef = TypedDict(
    "EnableReachabilityAnalyzerOrganizationSharingResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableSerialConsoleAccessResultTypeDef = TypedDict(
    "EnableSerialConsoleAccessResultTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableSnapshotBlockPublicAccessResultTypeDef = TypedDict(
    "EnableSnapshotBlockPublicAccessResultTypeDef",
    {
        "State": SnapshotBlockPublicAccessStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "EnableVpcClassicLinkDnsSupportResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableVpcClassicLinkResultTypeDef = TypedDict(
    "EnableVpcClassicLinkResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnclaveOptionsResponseTypeDef = TypedDict(
    "EnclaveOptionsResponseTypeDef",
    {
        "Enabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportClientVpnClientConfigurationResultTypeDef = TypedDict(
    "ExportClientVpnClientConfigurationResultTypeDef",
    {
        "ClientConfiguration": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportTransitGatewayRoutesResultTypeDef = TypedDict(
    "ExportTransitGatewayRoutesResultTypeDef",
    {
        "S3Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConsoleOutputResultTypeDef = TypedDict(
    "GetConsoleOutputResultTypeDef",
    {
        "InstanceId": str,
        "Output": str,
        "Timestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConsoleScreenshotResultTypeDef = TypedDict(
    "GetConsoleScreenshotResultTypeDef",
    {
        "ImageData": str,
        "InstanceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "GetEbsDefaultKmsKeyIdResultTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "GetEbsEncryptionByDefaultResultTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "SseType": SSETypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFlowLogsIntegrationTemplateResultTypeDef = TypedDict(
    "GetFlowLogsIntegrationTemplateResultTypeDef",
    {
        "Result": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImageBlockPublicAccessStateResultTypeDef = TypedDict(
    "GetImageBlockPublicAccessStateResultTypeDef",
    {
        "ImageBlockPublicAccessState": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstanceUefiDataResultTypeDef = TypedDict(
    "GetInstanceUefiDataResultTypeDef",
    {
        "InstanceId": str,
        "UefiData": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPasswordDataResultTypeDef = TypedDict(
    "GetPasswordDataResultTypeDef",
    {
        "InstanceId": str,
        "PasswordData": str,
        "Timestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSerialConsoleAccessStatusResultTypeDef = TypedDict(
    "GetSerialConsoleAccessStatusResultTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSnapshotBlockPublicAccessStateResultTypeDef = TypedDict(
    "GetSnapshotBlockPublicAccessStateResultTypeDef",
    {
        "State": SnapshotBlockPublicAccessStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVerifiedAccessEndpointPolicyResultTypeDef = TypedDict(
    "GetVerifiedAccessEndpointPolicyResultTypeDef",
    {
        "PolicyEnabled": bool,
        "PolicyDocument": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVerifiedAccessGroupPolicyResultTypeDef = TypedDict(
    "GetVerifiedAccessGroupPolicyResultTypeDef",
    {
        "PolicyEnabled": bool,
        "PolicyDocument": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVpnConnectionDeviceSampleConfigurationResultTypeDef = TypedDict(
    "GetVpnConnectionDeviceSampleConfigurationResultTypeDef",
    {
        "VpnConnectionDeviceSampleConfiguration": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HibernationOptionsResponseTypeDef = TypedDict(
    "HibernationOptionsResponseTypeDef",
    {
        "Configured": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IamInstanceProfileResponseTypeDef = TypedDict(
    "IamInstanceProfileResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportClientVpnClientCertificateRevocationListResultTypeDef = TypedDict(
    "ImportClientVpnClientCertificateRevocationListResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceMaintenanceOptionsResponseTypeDef = TypedDict(
    "InstanceMaintenanceOptionsResponseTypeDef",
    {
        "AutoRecovery": InstanceAutoRecoveryStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceMetadataOptionsResponseResponseTypeDef = TypedDict(
    "InstanceMetadataOptionsResponseResponseTypeDef",
    {
        "State": InstanceMetadataOptionsStateType,
        "HttpTokens": HttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": InstanceMetadataEndpointStateType,
        "HttpProtocolIpv6": InstanceMetadataProtocolStateType,
        "InstanceMetadataTags": InstanceMetadataTagsStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceStateResponseTypeDef = TypedDict(
    "InstanceStateResponseTypeDef",
    {
        "Code": int,
        "Name": InstanceStateNameType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LockSnapshotResultTypeDef = TypedDict(
    "LockSnapshotResultTypeDef",
    {
        "SnapshotId": str,
        "LockState": LockStateType,
        "LockDuration": int,
        "CoolOffPeriod": int,
        "CoolOffPeriodExpiresOn": datetime,
        "LockCreatedOn": datetime,
        "LockExpiresOn": datetime,
        "LockDurationStartTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyAvailabilityZoneGroupResultTypeDef = TypedDict(
    "ModifyAvailabilityZoneGroupResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyCapacityReservationFleetResultTypeDef = TypedDict(
    "ModifyCapacityReservationFleetResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyCapacityReservationResultTypeDef = TypedDict(
    "ModifyCapacityReservationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyClientVpnEndpointResultTypeDef = TypedDict(
    "ModifyClientVpnEndpointResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "ModifyEbsDefaultKmsKeyIdResultTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyFleetResultTypeDef = TypedDict(
    "ModifyFleetResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyInstanceCapacityReservationAttributesResultTypeDef = TypedDict(
    "ModifyInstanceCapacityReservationAttributesResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyInstanceMaintenanceOptionsResultTypeDef = TypedDict(
    "ModifyInstanceMaintenanceOptionsResultTypeDef",
    {
        "InstanceId": str,
        "AutoRecovery": InstanceAutoRecoveryStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyInstancePlacementResultTypeDef = TypedDict(
    "ModifyInstancePlacementResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyPrivateDnsNameOptionsResultTypeDef = TypedDict(
    "ModifyPrivateDnsNameOptionsResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyReservedInstancesResultTypeDef = TypedDict(
    "ModifyReservedInstancesResultTypeDef",
    {
        "ReservedInstancesModificationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifySecurityGroupRulesResultTypeDef = TypedDict(
    "ModifySecurityGroupRulesResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifySnapshotTierResultTypeDef = TypedDict(
    "ModifySnapshotTierResultTypeDef",
    {
        "SnapshotId": str,
        "TieringStartTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifySpotFleetRequestResponseTypeDef = TypedDict(
    "ModifySpotFleetRequestResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpcEndpointConnectionNotificationResultTypeDef = TypedDict(
    "ModifyVpcEndpointConnectionNotificationResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpcEndpointResultTypeDef = TypedDict(
    "ModifyVpcEndpointResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpcEndpointServiceConfigurationResultTypeDef = TypedDict(
    "ModifyVpcEndpointServiceConfigurationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpcEndpointServicePayerResponsibilityResultTypeDef = TypedDict(
    "ModifyVpcEndpointServicePayerResponsibilityResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpcTenancyResultTypeDef = TypedDict(
    "ModifyVpcTenancyResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MonitoringResponseTypeDef = TypedDict(
    "MonitoringResponseTypeDef",
    {
        "State": MonitoringStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MoveAddressToVpcResultTypeDef = TypedDict(
    "MoveAddressToVpcResultTypeDef",
    {
        "AllocationId": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkInterfaceAssociationResponseTypeDef = TypedDict(
    "NetworkInterfaceAssociationResponseTypeDef",
    {
        "AllocationId": str,
        "AssociationId": str,
        "IpOwnerId": str,
        "PublicDnsName": str,
        "PublicIp": str,
        "CustomerOwnedIp": str,
        "CarrierIp": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PlacementExtraResponseTypeDef = TypedDict(
    "PlacementExtraResponseTypeDef",
    {
        "AvailabilityZone": str,
        "Affinity": str,
        "GroupName": str,
        "PartitionNumber": int,
        "HostId": str,
        "Tenancy": TenancyType,
        "SpreadDomain": str,
        "HostResourceGroupArn": str,
        "GroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PrivateDnsNameOptionsOnLaunchResponseTypeDef = TypedDict(
    "PrivateDnsNameOptionsOnLaunchResponseTypeDef",
    {
        "HostnameType": HostnameTypeType,
        "EnableResourceNameDnsARecord": bool,
        "EnableResourceNameDnsAAAARecord": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PrivateDnsNameOptionsResponseResponseTypeDef = TypedDict(
    "PrivateDnsNameOptionsResponseResponseTypeDef",
    {
        "HostnameType": HostnameTypeType,
        "EnableResourceNameDnsARecord": bool,
        "EnableResourceNameDnsAAAARecord": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PurchaseReservedInstancesOfferingResultTypeDef = TypedDict(
    "PurchaseReservedInstancesOfferingResultTypeDef",
    {
        "ReservedInstancesId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterImageResultTypeDef = TypedDict(
    "RegisterImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectVpcPeeringConnectionResultTypeDef = TypedDict(
    "RejectVpcPeeringConnectionResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReleaseIpamPoolAllocationResultTypeDef = TypedDict(
    "ReleaseIpamPoolAllocationResultTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplaceNetworkAclAssociationResultTypeDef = TypedDict(
    "ReplaceNetworkAclAssociationResultTypeDef",
    {
        "NewAssociationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplaceVpnTunnelResultTypeDef = TypedDict(
    "ReplaceVpnTunnelResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestSpotFleetResponseTypeDef = TypedDict(
    "RequestSpotFleetResponseTypeDef",
    {
        "SpotFleetRequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "ResetEbsDefaultKmsKeyIdResultTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetFpgaImageAttributeResultTypeDef = TypedDict(
    "ResetFpgaImageAttributeResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreAddressToClassicResultTypeDef = TypedDict(
    "RestoreAddressToClassicResultTypeDef",
    {
        "PublicIp": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreImageFromRecycleBinResultTypeDef = TypedDict(
    "RestoreImageFromRecycleBinResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreSnapshotFromRecycleBinResultTypeDef = TypedDict(
    "RestoreSnapshotFromRecycleBinResultTypeDef",
    {
        "SnapshotId": str,
        "OutpostArn": str,
        "Description": str,
        "Encrypted": bool,
        "OwnerId": str,
        "Progress": str,
        "StartTime": datetime,
        "State": SnapshotStateType,
        "VolumeId": str,
        "VolumeSize": int,
        "SseType": SSETypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreSnapshotTierResultTypeDef = TypedDict(
    "RestoreSnapshotTierResultTypeDef",
    {
        "SnapshotId": str,
        "RestoreStartTime": datetime,
        "RestoreDuration": int,
        "IsPermanentRestore": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RouteTableAssociationStateResponseTypeDef = TypedDict(
    "RouteTableAssociationStateResponseTypeDef",
    {
        "State": RouteTableAssociationStateCodeType,
        "StatusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RunScheduledInstancesResultTypeDef = TypedDict(
    "RunScheduledInstancesResultTypeDef",
    {
        "InstanceIdSet": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartVpcEndpointServicePrivateDnsVerificationResultTypeDef = TypedDict(
    "StartVpcEndpointServicePrivateDnsVerificationResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StateReasonResponseTypeDef = TypedDict(
    "StateReasonResponseTypeDef",
    {
        "Code": str,
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StateReasonTypeDef = TypedDict(
    "StateReasonTypeDef",
    {
        "Code": str,
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UnassignIpv6AddressesResultTypeDef = TypedDict(
    "UnassignIpv6AddressesResultTypeDef",
    {
        "NetworkInterfaceId": str,
        "UnassignedIpv6Addresses": List[str],
        "UnassignedIpv6Prefixes": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UnlockSnapshotResultTypeDef = TypedDict(
    "UnlockSnapshotResultTypeDef",
    {
        "SnapshotId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VolumeAttachmentResponseTypeDef = TypedDict(
    "VolumeAttachmentResponseTypeDef",
    {
        "AttachTime": datetime,
        "Device": str,
        "InstanceId": str,
        "State": VolumeAttachmentStateType,
        "VolumeId": str,
        "DeleteOnTermination": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VolumeAttachmentTypeDef = TypedDict(
    "VolumeAttachmentTypeDef",
    {
        "AttachTime": datetime,
        "Device": str,
        "InstanceId": str,
        "State": VolumeAttachmentStateType,
        "VolumeId": str,
        "DeleteOnTermination": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VpcPeeringConnectionStateReasonResponseTypeDef = TypedDict(
    "VpcPeeringConnectionStateReasonResponseTypeDef",
    {
        "Code": VpcPeeringConnectionStateReasonCodeType,
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptReservedInstancesExchangeQuoteRequestRequestTypeDef = TypedDict(
    "AcceptReservedInstancesExchangeQuoteRequestRequestTypeDef",
    {
        "ReservedInstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
        "TargetConfigurations": NotRequired[Sequence[TargetConfigurationRequestTypeDef]],
    },
)
GetReservedInstancesExchangeQuoteRequestRequestTypeDef = TypedDict(
    "GetReservedInstancesExchangeQuoteRequestRequestTypeDef",
    {
        "ReservedInstanceIds": Sequence[str],
        "DryRun": NotRequired[bool],
        "TargetConfigurations": NotRequired[Sequence[TargetConfigurationRequestTypeDef]],
    },
)
AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[List[AccountAttributeValueTypeDef]],
    },
)
DescribeFleetInstancesResultTypeDef = TypedDict(
    "DescribeFleetInstancesResultTypeDef",
    {
        "ActiveInstances": List[ActiveInstanceTypeDef],
        "NextToken": str,
        "FleetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSpotFleetInstancesResponseTypeDef = TypedDict(
    "DescribeSpotFleetInstancesResponseTypeDef",
    {
        "ActiveInstances": List[ActiveInstanceTypeDef],
        "NextToken": str,
        "SpotFleetRequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpcEndpointServicePermissionsResultTypeDef = TypedDict(
    "ModifyVpcEndpointServicePermissionsResultTypeDef",
    {
        "AddedPrincipals": List[AddedPrincipalTypeDef],
        "ReturnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnalysisLoadBalancerTargetTypeDef = TypedDict(
    "AnalysisLoadBalancerTargetTypeDef",
    {
        "Address": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "Instance": NotRequired[AnalysisComponentTypeDef],
        "Port": NotRequired[int],
    },
)
RuleGroupRuleOptionsPairTypeDef = TypedDict(
    "RuleGroupRuleOptionsPairTypeDef",
    {
        "RuleGroupArn": NotRequired[str],
        "RuleOptions": NotRequired[List[RuleOptionTypeDef]],
    },
)
AddressAttributeTypeDef = TypedDict(
    "AddressAttributeTypeDef",
    {
        "PublicIp": NotRequired[str],
        "AllocationId": NotRequired[str],
        "PtrRecord": NotRequired[str],
        "PtrRecordUpdate": NotRequired[PtrUpdateStatusTypeDef],
    },
)
AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "InstanceId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "AllocationId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "Domain": NotRequired[DomainTypeType],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkInterfaceOwnerId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "PublicIpv4Pool": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "CustomerOwnedIp": NotRequired[str],
        "CustomerOwnedIpv4Pool": NotRequired[str],
        "CarrierIp": NotRequired[str],
    },
)
AllowedPrincipalTypeDef = TypedDict(
    "AllowedPrincipalTypeDef",
    {
        "PrincipalType": NotRequired[PrincipalTypeType],
        "Principal": NotRequired[str],
        "ServicePermissionId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "ServiceId": NotRequired[str],
    },
)
CarrierGatewayTypeDef = TypedDict(
    "CarrierGatewayTypeDef",
    {
        "CarrierGatewayId": NotRequired[str],
        "VpcId": NotRequired[str],
        "State": NotRequired[CarrierGatewayStateType],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ClientCreateTagsRequestTypeDef = TypedDict(
    "ClientCreateTagsRequestTypeDef",
    {
        "Resources": Sequence[str],
        "Tags": Sequence[TagTypeDef],
        "DryRun": NotRequired[bool],
    },
)
ClientDeleteTagsRequestTypeDef = TypedDict(
    "ClientDeleteTagsRequestTypeDef",
    {
        "Resources": Sequence[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CoipPoolTypeDef = TypedDict(
    "CoipPoolTypeDef",
    {
        "PoolId": NotRequired[str],
        "PoolCidrs": NotRequired[List[str]],
        "LocalGatewayRouteTableId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "PoolArn": NotRequired[str],
    },
)
CopySnapshotResultTypeDef = TypedDict(
    "CopySnapshotResultTypeDef",
    {
        "SnapshotId": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSecurityGroupResultTypeDef = TypedDict(
    "CreateSecurityGroupResultTypeDef",
    {
        "GroupId": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTagsRequestServiceResourceCreateTagsTypeDef = TypedDict(
    "CreateTagsRequestServiceResourceCreateTagsTypeDef",
    {
        "Resources": Sequence[str],
        "Tags": Sequence[TagTypeDef],
        "DryRun": NotRequired[bool],
    },
)
CustomerGatewayTypeDef = TypedDict(
    "CustomerGatewayTypeDef",
    {
        "BgpAsn": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "IpAddress": NotRequired[str],
        "CertificateArn": NotRequired[str],
        "State": NotRequired[str],
        "Type": NotRequired[str],
        "DeviceName": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
Ec2InstanceConnectEndpointTypeDef = TypedDict(
    "Ec2InstanceConnectEndpointTypeDef",
    {
        "OwnerId": NotRequired[str],
        "InstanceConnectEndpointId": NotRequired[str],
        "InstanceConnectEndpointArn": NotRequired[str],
        "State": NotRequired[Ec2InstanceConnectEndpointStateType],
        "StateMessage": NotRequired[str],
        "DnsName": NotRequired[str],
        "FipsDnsName": NotRequired[str],
        "NetworkInterfaceIds": NotRequired[List[str]],
        "VpcId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "SubnetId": NotRequired[str],
        "PreserveClientIp": NotRequired[bool],
        "SecurityGroupIds": NotRequired[List[str]],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
HostReservationTypeDef = TypedDict(
    "HostReservationTypeDef",
    {
        "Count": NotRequired[int],
        "CurrencyCode": NotRequired[Literal["USD"]],
        "Duration": NotRequired[int],
        "End": NotRequired[datetime],
        "HostIdSet": NotRequired[List[str]],
        "HostReservationId": NotRequired[str],
        "HourlyPrice": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "OfferingId": NotRequired[str],
        "PaymentOption": NotRequired[PaymentOptionType],
        "Start": NotRequired[datetime],
        "State": NotRequired[ReservationStateType],
        "UpfrontPrice": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ImportKeyPairResultTypeDef = TypedDict(
    "ImportKeyPairResultTypeDef",
    {
        "KeyFingerprint": str,
        "KeyName": str,
        "KeyPairId": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceCreateTagsRequestTypeDef = TypedDict(
    "InstanceCreateTagsRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
        "DryRun": NotRequired[bool],
    },
)
InstanceDeleteTagsRequestTypeDef = TypedDict(
    "InstanceDeleteTagsRequestTypeDef",
    {
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
InstanceEventWindowAssociationRequestTypeDef = TypedDict(
    "InstanceEventWindowAssociationRequestTypeDef",
    {
        "InstanceIds": NotRequired[Sequence[str]],
        "InstanceTags": NotRequired[Sequence[TagTypeDef]],
        "DedicatedHostIds": NotRequired[Sequence[str]],
    },
)
InstanceEventWindowAssociationTargetTypeDef = TypedDict(
    "InstanceEventWindowAssociationTargetTypeDef",
    {
        "InstanceIds": NotRequired[List[str]],
        "Tags": NotRequired[List[TagTypeDef]],
        "DedicatedHostIds": NotRequired[List[str]],
    },
)
InstanceEventWindowDisassociationRequestTypeDef = TypedDict(
    "InstanceEventWindowDisassociationRequestTypeDef",
    {
        "InstanceIds": NotRequired[Sequence[str]],
        "InstanceTags": NotRequired[Sequence[TagTypeDef]],
        "DedicatedHostIds": NotRequired[Sequence[str]],
    },
)
IpamResourceDiscoveryAssociationTypeDef = TypedDict(
    "IpamResourceDiscoveryAssociationTypeDef",
    {
        "OwnerId": NotRequired[str],
        "IpamResourceDiscoveryAssociationId": NotRequired[str],
        "IpamResourceDiscoveryAssociationArn": NotRequired[str],
        "IpamResourceDiscoveryId": NotRequired[str],
        "IpamId": NotRequired[str],
        "IpamArn": NotRequired[str],
        "IpamRegion": NotRequired[str],
        "IsDefault": NotRequired[bool],
        "ResourceDiscoveryStatus": NotRequired[IpamAssociatedResourceDiscoveryStatusType],
        "State": NotRequired[IpamResourceDiscoveryAssociationStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
IpamScopeTypeDef = TypedDict(
    "IpamScopeTypeDef",
    {
        "OwnerId": NotRequired[str],
        "IpamScopeId": NotRequired[str],
        "IpamScopeArn": NotRequired[str],
        "IpamArn": NotRequired[str],
        "IpamRegion": NotRequired[str],
        "IpamScopeType": NotRequired[IpamScopeTypeType],
        "IsDefault": NotRequired[bool],
        "Description": NotRequired[str],
        "PoolCount": NotRequired[int],
        "State": NotRequired[IpamScopeStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
KeyPairInfoTypeDef = TypedDict(
    "KeyPairInfoTypeDef",
    {
        "KeyPairId": NotRequired[str],
        "KeyFingerprint": NotRequired[str],
        "KeyName": NotRequired[str],
        "KeyType": NotRequired[KeyTypeType],
        "Tags": NotRequired[List[TagTypeDef]],
        "PublicKey": NotRequired[str],
        "CreateTime": NotRequired[datetime],
    },
)
KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "KeyFingerprint": str,
        "KeyMaterial": str,
        "KeyName": str,
        "KeyPairId": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LaunchTemplateTagSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateTagSpecificationRequestTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
LaunchTemplateTagSpecificationTypeDef = TypedDict(
    "LaunchTemplateTagSpecificationTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
        "DefaultVersionNumber": NotRequired[int],
        "LatestVersionNumber": NotRequired[int],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef = TypedDict(
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId": NotRequired[str],
        "LocalGatewayVirtualInterfaceGroupId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "LocalGatewayRouteTableId": NotRequired[str],
        "LocalGatewayRouteTableArn": NotRequired[str],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
LocalGatewayRouteTableVpcAssociationTypeDef = TypedDict(
    "LocalGatewayRouteTableVpcAssociationTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationId": NotRequired[str],
        "LocalGatewayRouteTableId": NotRequired[str],
        "LocalGatewayRouteTableArn": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "VpcId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
LocalGatewayTypeDef = TypedDict(
    "LocalGatewayTypeDef",
    {
        "LocalGatewayId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
LocalGatewayVirtualInterfaceGroupTypeDef = TypedDict(
    "LocalGatewayVirtualInterfaceGroupTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroupId": NotRequired[str],
        "LocalGatewayVirtualInterfaceIds": NotRequired[List[str]],
        "LocalGatewayId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
LocalGatewayVirtualInterfaceTypeDef = TypedDict(
    "LocalGatewayVirtualInterfaceTypeDef",
    {
        "LocalGatewayVirtualInterfaceId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "Vlan": NotRequired[int],
        "LocalAddress": NotRequired[str],
        "PeerAddress": NotRequired[str],
        "LocalBgpAsn": NotRequired[int],
        "PeerBgpAsn": NotRequired[int],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ManagedPrefixListTypeDef = TypedDict(
    "ManagedPrefixListTypeDef",
    {
        "PrefixListId": NotRequired[str],
        "AddressFamily": NotRequired[str],
        "State": NotRequired[PrefixListStateType],
        "StateMessage": NotRequired[str],
        "PrefixListArn": NotRequired[str],
        "PrefixListName": NotRequired[str],
        "MaxEntries": NotRequired[int],
        "Version": NotRequired[int],
        "Tags": NotRequired[List[TagTypeDef]],
        "OwnerId": NotRequired[str],
    },
)
NetworkInsightsAccessScopeAnalysisTypeDef = TypedDict(
    "NetworkInsightsAccessScopeAnalysisTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": NotRequired[str],
        "NetworkInsightsAccessScopeAnalysisArn": NotRequired[str],
        "NetworkInsightsAccessScopeId": NotRequired[str],
        "Status": NotRequired[AnalysisStatusType],
        "StatusMessage": NotRequired[str],
        "WarningMessage": NotRequired[str],
        "StartDate": NotRequired[datetime],
        "EndDate": NotRequired[datetime],
        "FindingsFound": NotRequired[FindingsFoundType],
        "AnalyzedEniCount": NotRequired[int],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
NetworkInsightsAccessScopeTypeDef = TypedDict(
    "NetworkInsightsAccessScopeTypeDef",
    {
        "NetworkInsightsAccessScopeId": NotRequired[str],
        "NetworkInsightsAccessScopeArn": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "UpdatedDate": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
PlacementGroupTypeDef = TypedDict(
    "PlacementGroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "State": NotRequired[PlacementGroupStateType],
        "Strategy": NotRequired[PlacementStrategyType],
        "PartitionCount": NotRequired[int],
        "GroupId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "GroupArn": NotRequired[str],
        "SpreadLevel": NotRequired[SpreadLevelType],
    },
)
ReplaceRootVolumeTaskTypeDef = TypedDict(
    "ReplaceRootVolumeTaskTypeDef",
    {
        "ReplaceRootVolumeTaskId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "TaskState": NotRequired[ReplaceRootVolumeTaskStateType],
        "StartTime": NotRequired[str],
        "CompleteTime": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "ImageId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "DeleteReplacedRootVolume": NotRequired[bool],
    },
)
SecurityGroupForVpcTypeDef = TypedDict(
    "SecurityGroupForVpcTypeDef",
    {
        "Description": NotRequired[str],
        "GroupName": NotRequired[str],
        "OwnerId": NotRequired[str],
        "GroupId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "PrimaryVpcId": NotRequired[str],
    },
)
SnapshotInfoTypeDef = TypedDict(
    "SnapshotInfoTypeDef",
    {
        "Description": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "Encrypted": NotRequired[bool],
        "VolumeId": NotRequired[str],
        "State": NotRequired[SnapshotStateType],
        "VolumeSize": NotRequired[int],
        "StartTime": NotRequired[datetime],
        "Progress": NotRequired[str],
        "OwnerId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "SseType": NotRequired[SSETypeType],
    },
)
SnapshotResponseTypeDef = TypedDict(
    "SnapshotResponseTypeDef",
    {
        "DataEncryptionKeyId": str,
        "Description": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OwnerId": str,
        "Progress": str,
        "SnapshotId": str,
        "StartTime": datetime,
        "State": SnapshotStateType,
        "StateMessage": str,
        "VolumeId": str,
        "VolumeSize": int,
        "OwnerAlias": str,
        "OutpostArn": str,
        "Tags": List[TagTypeDef],
        "StorageTier": StorageTierType,
        "RestoreExpiryTime": datetime,
        "SseType": SSETypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SnapshotTierStatusTypeDef = TypedDict(
    "SnapshotTierStatusTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "VolumeId": NotRequired[str],
        "Status": NotRequired[SnapshotStateType],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "StorageTier": NotRequired[StorageTierType],
        "LastTieringStartTime": NotRequired[datetime],
        "LastTieringProgress": NotRequired[int],
        "LastTieringOperationStatus": NotRequired[TieringOperationStatusType],
        "LastTieringOperationStatusDetail": NotRequired[str],
        "ArchivalCompleteTime": NotRequired[datetime],
        "RestoreExpiryTime": NotRequired[datetime],
    },
)
SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "DataEncryptionKeyId": NotRequired[str],
        "Description": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Progress": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "State": NotRequired[SnapshotStateType],
        "StateMessage": NotRequired[str],
        "VolumeId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "OwnerAlias": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "StorageTier": NotRequired[StorageTierType],
        "RestoreExpiryTime": NotRequired[datetime],
        "SseType": NotRequired[SSETypeType],
    },
)
SpotFleetTagSpecificationTypeDef = TypedDict(
    "SpotFleetTagSpecificationTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
SubnetCidrReservationTypeDef = TypedDict(
    "SubnetCidrReservationTypeDef",
    {
        "SubnetCidrReservationId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Cidr": NotRequired[str],
        "ReservationType": NotRequired[SubnetCidrReservationTypeType],
        "OwnerId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TagSpecificationPaginatorTypeDef = TypedDict(
    "TagSpecificationPaginatorTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TagSpecificationTypeDef = TypedDict(
    "TagSpecificationTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TrafficMirrorSessionTypeDef = TypedDict(
    "TrafficMirrorSessionTypeDef",
    {
        "TrafficMirrorSessionId": NotRequired[str],
        "TrafficMirrorTargetId": NotRequired[str],
        "TrafficMirrorFilterId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "PacketLength": NotRequired[int],
        "SessionNumber": NotRequired[int],
        "VirtualNetworkId": NotRequired[int],
        "Description": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TrafficMirrorTargetTypeDef = TypedDict(
    "TrafficMirrorTargetTypeDef",
    {
        "TrafficMirrorTargetId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkLoadBalancerArn": NotRequired[str],
        "Type": NotRequired[TrafficMirrorTargetTypeType],
        "Description": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "GatewayLoadBalancerEndpointId": NotRequired[str],
    },
)
TransitGatewayPolicyTableTypeDef = TypedDict(
    "TransitGatewayPolicyTableTypeDef",
    {
        "TransitGatewayPolicyTableId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "State": NotRequired[TransitGatewayPolicyTableStateType],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TransitGatewayRouteTableAnnouncementTypeDef = TypedDict(
    "TransitGatewayRouteTableAnnouncementTypeDef",
    {
        "TransitGatewayRouteTableAnnouncementId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "CoreNetworkId": NotRequired[str],
        "PeerTransitGatewayId": NotRequired[str],
        "PeerCoreNetworkId": NotRequired[str],
        "PeeringAttachmentId": NotRequired[str],
        "AnnouncementDirection": NotRequired[TransitGatewayRouteTableAnnouncementDirectionType],
        "TransitGatewayRouteTableId": NotRequired[str],
        "State": NotRequired[TransitGatewayRouteTableAnnouncementStateType],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TransitGatewayRouteTableTypeDef = TypedDict(
    "TransitGatewayRouteTableTypeDef",
    {
        "TransitGatewayRouteTableId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "State": NotRequired[TransitGatewayRouteTableStateType],
        "DefaultAssociationRouteTable": NotRequired[bool],
        "DefaultPropagationRouteTable": NotRequired[bool],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TrunkInterfaceAssociationTypeDef = TypedDict(
    "TrunkInterfaceAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "BranchInterfaceId": NotRequired[str],
        "TrunkInterfaceId": NotRequired[str],
        "InterfaceProtocol": NotRequired[InterfaceProtocolTypeType],
        "VlanId": NotRequired[int],
        "GreKey": NotRequired[int],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
VpcClassicLinkTypeDef = TypedDict(
    "VpcClassicLinkTypeDef",
    {
        "ClassicLinkEnabled": NotRequired[bool],
        "Tags": NotRequired[List[TagTypeDef]],
        "VpcId": NotRequired[str],
    },
)
VpcCreateTagsRequestTypeDef = TypedDict(
    "VpcCreateTagsRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
        "DryRun": NotRequired[bool],
    },
)
AllocateIpamPoolCidrResultTypeDef = TypedDict(
    "AllocateIpamPoolCidrResultTypeDef",
    {
        "IpamPoolAllocation": IpamPoolAllocationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIpamPoolAllocationsResultTypeDef = TypedDict(
    "GetIpamPoolAllocationsResultTypeDef",
    {
        "IpamPoolAllocations": List[IpamPoolAllocationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnalysisAclRuleTypeDef = TypedDict(
    "AnalysisAclRuleTypeDef",
    {
        "Cidr": NotRequired[str],
        "Egress": NotRequired[bool],
        "PortRange": NotRequired[PortRangeTypeDef],
        "Protocol": NotRequired[str],
        "RuleAction": NotRequired[str],
        "RuleNumber": NotRequired[int],
    },
)
AnalysisPacketHeaderTypeDef = TypedDict(
    "AnalysisPacketHeaderTypeDef",
    {
        "DestinationAddresses": NotRequired[List[str]],
        "DestinationPortRanges": NotRequired[List[PortRangeTypeDef]],
        "Protocol": NotRequired[str],
        "SourceAddresses": NotRequired[List[str]],
        "SourcePortRanges": NotRequired[List[PortRangeTypeDef]],
    },
)
AnalysisSecurityGroupRuleTypeDef = TypedDict(
    "AnalysisSecurityGroupRuleTypeDef",
    {
        "Cidr": NotRequired[str],
        "Direction": NotRequired[str],
        "SecurityGroupId": NotRequired[str],
        "PortRange": NotRequired[PortRangeTypeDef],
        "PrefixListId": NotRequired[str],
        "Protocol": NotRequired[str],
    },
)
FirewallStatefulRuleTypeDef = TypedDict(
    "FirewallStatefulRuleTypeDef",
    {
        "RuleGroupArn": NotRequired[str],
        "Sources": NotRequired[List[str]],
        "Destinations": NotRequired[List[str]],
        "SourcePorts": NotRequired[List[PortRangeTypeDef]],
        "DestinationPorts": NotRequired[List[PortRangeTypeDef]],
        "Protocol": NotRequired[str],
        "RuleAction": NotRequired[str],
        "Direction": NotRequired[str],
    },
)
FirewallStatelessRuleTypeDef = TypedDict(
    "FirewallStatelessRuleTypeDef",
    {
        "RuleGroupArn": NotRequired[str],
        "Sources": NotRequired[List[str]],
        "Destinations": NotRequired[List[str]],
        "SourcePorts": NotRequired[List[PortRangeTypeDef]],
        "DestinationPorts": NotRequired[List[PortRangeTypeDef]],
        "Protocols": NotRequired[List[int]],
        "RuleAction": NotRequired[str],
        "Priority": NotRequired[int],
    },
)
AssociateIpamByoasnResultTypeDef = TypedDict(
    "AssociateIpamByoasnResultTypeDef",
    {
        "AsnAssociation": AsnAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ByoipCidrTypeDef = TypedDict(
    "ByoipCidrTypeDef",
    {
        "Cidr": NotRequired[str],
        "Description": NotRequired[str],
        "AsnAssociations": NotRequired[List[AsnAssociationTypeDef]],
        "StatusMessage": NotRequired[str],
        "State": NotRequired[ByoipCidrStateType],
        "NetworkBorderGroup": NotRequired[str],
    },
)
DisassociateIpamByoasnResultTypeDef = TypedDict(
    "DisassociateIpamByoasnResultTypeDef",
    {
        "AsnAssociation": AsnAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisionIpamByoasnRequestRequestTypeDef = TypedDict(
    "ProvisionIpamByoasnRequestRequestTypeDef",
    {
        "IpamId": str,
        "Asn": str,
        "AsnAuthorizationContext": AsnAuthorizationContextTypeDef,
        "DryRun": NotRequired[bool],
    },
)
AssignPrivateIpAddressesResultTypeDef = TypedDict(
    "AssignPrivateIpAddressesResultTypeDef",
    {
        "NetworkInterfaceId": str,
        "AssignedPrivateIpAddresses": List[AssignedPrivateIpAddressTypeDef],
        "AssignedIpv4Prefixes": List[Ipv4PrefixSpecificationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssignPrivateNatGatewayAddressResultTypeDef = TypedDict(
    "AssignPrivateNatGatewayAddressResultTypeDef",
    {
        "NatGatewayId": str,
        "NatGatewayAddresses": List[NatGatewayAddressTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateNatGatewayAddressResultTypeDef = TypedDict(
    "AssociateNatGatewayAddressResultTypeDef",
    {
        "NatGatewayId": str,
        "NatGatewayAddresses": List[NatGatewayAddressTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateNatGatewayAddressResultTypeDef = TypedDict(
    "DisassociateNatGatewayAddressResultTypeDef",
    {
        "NatGatewayId": str,
        "NatGatewayAddresses": List[NatGatewayAddressTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UnassignPrivateNatGatewayAddressResultTypeDef = TypedDict(
    "UnassignPrivateNatGatewayAddressResultTypeDef",
    {
        "NatGatewayId": str,
        "NatGatewayAddresses": List[NatGatewayAddressTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateClientVpnTargetNetworkResultTypeDef = TypedDict(
    "AssociateClientVpnTargetNetworkResultTypeDef",
    {
        "AssociationId": str,
        "Status": AssociationStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateClientVpnTargetNetworkResultTypeDef = TypedDict(
    "DisassociateClientVpnTargetNetworkResultTypeDef",
    {
        "AssociationId": str,
        "Status": AssociationStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TargetNetworkTypeDef = TypedDict(
    "TargetNetworkTypeDef",
    {
        "AssociationId": NotRequired[str],
        "VpcId": NotRequired[str],
        "TargetNetworkId": NotRequired[str],
        "ClientVpnEndpointId": NotRequired[str],
        "Status": NotRequired[AssociationStatusTypeDef],
        "SecurityGroups": NotRequired[List[str]],
    },
)
AssociateIamInstanceProfileRequestRequestTypeDef = TypedDict(
    "AssociateIamInstanceProfileRequestRequestTypeDef",
    {
        "IamInstanceProfile": IamInstanceProfileSpecificationTypeDef,
        "InstanceId": str,
    },
)
ReplaceIamInstanceProfileAssociationRequestRequestTypeDef = TypedDict(
    "ReplaceIamInstanceProfileAssociationRequestRequestTypeDef",
    {
        "IamInstanceProfile": IamInstanceProfileSpecificationTypeDef,
        "AssociationId": str,
    },
)
AssociateRouteTableResultTypeDef = TypedDict(
    "AssociateRouteTableResultTypeDef",
    {
        "AssociationId": str,
        "AssociationState": RouteTableAssociationStateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplaceRouteTableAssociationResultTypeDef = TypedDict(
    "ReplaceRouteTableAssociationResultTypeDef",
    {
        "NewAssociationId": str,
        "AssociationState": RouteTableAssociationStateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RouteTableAssociationTypeDef = TypedDict(
    "RouteTableAssociationTypeDef",
    {
        "Main": NotRequired[bool],
        "RouteTableAssociationId": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "AssociationState": NotRequired[RouteTableAssociationStateTypeDef],
    },
)
AssociateTransitGatewayPolicyTableResultTypeDef = TypedDict(
    "AssociateTransitGatewayPolicyTableResultTypeDef",
    {
        "Association": TransitGatewayPolicyTableAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateTransitGatewayPolicyTableResultTypeDef = TypedDict(
    "DisassociateTransitGatewayPolicyTableResultTypeDef",
    {
        "Association": TransitGatewayPolicyTableAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransitGatewayPolicyTableAssociationsResultTypeDef = TypedDict(
    "GetTransitGatewayPolicyTableAssociationsResultTypeDef",
    {
        "Associations": List[TransitGatewayPolicyTableAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "AssociateTransitGatewayRouteTableResultTypeDef",
    {
        "Association": TransitGatewayAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "DisassociateTransitGatewayRouteTableResultTypeDef",
    {
        "Association": TransitGatewayAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssociatedEnclaveCertificateIamRolesResultTypeDef = TypedDict(
    "GetAssociatedEnclaveCertificateIamRolesResultTypeDef",
    {
        "AssociatedRoles": List[AssociatedRoleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AthenaIntegrationTypeDef = TypedDict(
    "AthenaIntegrationTypeDef",
    {
        "IntegrationResultS3DestinationArn": str,
        "PartitionLoadFrequency": PartitionLoadFrequencyType,
        "PartitionStartDate": NotRequired[TimestampTypeDef],
        "PartitionEndDate": NotRequired[TimestampTypeDef],
    },
)
ClientDataTypeDef = TypedDict(
    "ClientDataTypeDef",
    {
        "Comment": NotRequired[str],
        "UploadEnd": NotRequired[TimestampTypeDef],
        "UploadSize": NotRequired[float],
        "UploadStart": NotRequired[TimestampTypeDef],
    },
)
DescribeCapacityBlockOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeCapacityBlockOfferingsRequestRequestTypeDef",
    {
        "InstanceType": str,
        "InstanceCount": int,
        "CapacityDurationHours": int,
        "DryRun": NotRequired[bool],
        "StartDateRange": NotRequired[TimestampTypeDef],
        "EndDateRange": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeFleetHistoryRequestRequestTypeDef = TypedDict(
    "DescribeFleetHistoryRequestRequestTypeDef",
    {
        "FleetId": str,
        "StartTime": TimestampTypeDef,
        "DryRun": NotRequired[bool],
        "EventType": NotRequired[FleetEventTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeSpotFleetRequestHistoryRequestRequestTypeDef = TypedDict(
    "DescribeSpotFleetRequestHistoryRequestRequestTypeDef",
    {
        "SpotFleetRequestId": str,
        "StartTime": TimestampTypeDef,
        "DryRun": NotRequired[bool],
        "EventType": NotRequired[EventTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
EnableImageDeprecationRequestRequestTypeDef = TypedDict(
    "EnableImageDeprecationRequestRequestTypeDef",
    {
        "ImageId": str,
        "DeprecateAt": TimestampTypeDef,
        "DryRun": NotRequired[bool],
    },
)
GetIpamAddressHistoryRequestRequestTypeDef = TypedDict(
    "GetIpamAddressHistoryRequestRequestTypeDef",
    {
        "Cidr": str,
        "IpamScopeId": str,
        "DryRun": NotRequired[bool],
        "VpcId": NotRequired[str],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
LaunchTemplateSpotMarketOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    {
        "MaxPrice": NotRequired[str],
        "SpotInstanceType": NotRequired[SpotInstanceTypeType],
        "BlockDurationMinutes": NotRequired[int],
        "ValidUntil": NotRequired[TimestampTypeDef],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
    },
)
LockSnapshotRequestRequestTypeDef = TypedDict(
    "LockSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "LockMode": LockModeType,
        "DryRun": NotRequired[bool],
        "CoolOffPeriod": NotRequired[int],
        "LockDuration": NotRequired[int],
        "ExpirationDate": NotRequired[TimestampTypeDef],
    },
)
ModifyCapacityReservationFleetRequestRequestTypeDef = TypedDict(
    "ModifyCapacityReservationFleetRequestRequestTypeDef",
    {
        "CapacityReservationFleetId": str,
        "TotalTargetCapacity": NotRequired[int],
        "EndDate": NotRequired[TimestampTypeDef],
        "DryRun": NotRequired[bool],
        "RemoveEndDate": NotRequired[bool],
    },
)
ModifyCapacityReservationRequestRequestTypeDef = TypedDict(
    "ModifyCapacityReservationRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
        "InstanceCount": NotRequired[int],
        "EndDate": NotRequired[TimestampTypeDef],
        "EndDateType": NotRequired[EndDateTypeType],
        "Accept": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "AdditionalInfo": NotRequired[str],
    },
)
ModifyInstanceEventStartTimeRequestRequestTypeDef = TypedDict(
    "ModifyInstanceEventStartTimeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "InstanceEventId": str,
        "NotBefore": TimestampTypeDef,
        "DryRun": NotRequired[bool],
    },
)
ReportInstanceStatusRequestInstanceReportStatusTypeDef = TypedDict(
    "ReportInstanceStatusRequestInstanceReportStatusTypeDef",
    {
        "ReasonCodes": Sequence[ReportInstanceReasonCodesType],
        "Status": ReportStatusTypeType,
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "EndTime": NotRequired[TimestampTypeDef],
        "StartTime": NotRequired[TimestampTypeDef],
    },
)
ReportInstanceStatusRequestRequestTypeDef = TypedDict(
    "ReportInstanceStatusRequestRequestTypeDef",
    {
        "Instances": Sequence[str],
        "ReasonCodes": Sequence[ReportInstanceReasonCodesType],
        "Status": ReportStatusTypeType,
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "EndTime": NotRequired[TimestampTypeDef],
        "StartTime": NotRequired[TimestampTypeDef],
    },
)
SlotDateTimeRangeRequestTypeDef = TypedDict(
    "SlotDateTimeRangeRequestTypeDef",
    {
        "EarliestTime": TimestampTypeDef,
        "LatestTime": TimestampTypeDef,
    },
)
SlotStartTimeRangeRequestTypeDef = TypedDict(
    "SlotStartTimeRangeRequestTypeDef",
    {
        "EarliestTime": NotRequired[TimestampTypeDef],
        "LatestTime": NotRequired[TimestampTypeDef],
    },
)
SpotMarketOptionsTypeDef = TypedDict(
    "SpotMarketOptionsTypeDef",
    {
        "MaxPrice": NotRequired[str],
        "SpotInstanceType": NotRequired[SpotInstanceTypeType],
        "BlockDurationMinutes": NotRequired[int],
        "ValidUntil": NotRequired[TimestampTypeDef],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
    },
)
AttachVpnGatewayResultTypeDef = TypedDict(
    "AttachVpnGatewayResultTypeDef",
    {
        "VpcAttachment": VpcAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VpnGatewayTypeDef = TypedDict(
    "VpnGatewayTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "State": NotRequired[VpnStateType],
        "Type": NotRequired[Literal["ipsec.1"]],
        "VpcAttachments": NotRequired[List[VpcAttachmentTypeDef]],
        "VpnGatewayId": NotRequired[str],
        "AmazonSideAsn": NotRequired[int],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
AttachmentEnaSrdSpecificationTypeDef = TypedDict(
    "AttachmentEnaSrdSpecificationTypeDef",
    {
        "EnaSrdEnabled": NotRequired[bool],
        "EnaSrdUdpSpecification": NotRequired[AttachmentEnaSrdUdpSpecificationTypeDef],
    },
)
DescribeVpcAttributeResultTypeDef = TypedDict(
    "DescribeVpcAttributeResultTypeDef",
    {
        "VpcId": str,
        "EnableDnsHostnames": AttributeBooleanValueTypeDef,
        "EnableDnsSupport": AttributeBooleanValueTypeDef,
        "EnableNetworkAddressUsageMetrics": AttributeBooleanValueTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifySubnetAttributeRequestRequestTypeDef = TypedDict(
    "ModifySubnetAttributeRequestRequestTypeDef",
    {
        "SubnetId": str,
        "AssignIpv6AddressOnCreation": NotRequired[AttributeBooleanValueTypeDef],
        "MapPublicIpOnLaunch": NotRequired[AttributeBooleanValueTypeDef],
        "MapCustomerOwnedIpOnLaunch": NotRequired[AttributeBooleanValueTypeDef],
        "CustomerOwnedIpv4Pool": NotRequired[str],
        "EnableDns64": NotRequired[AttributeBooleanValueTypeDef],
        "PrivateDnsHostnameTypeOnLaunch": NotRequired[HostnameTypeType],
        "EnableResourceNameDnsARecordOnLaunch": NotRequired[AttributeBooleanValueTypeDef],
        "EnableResourceNameDnsAAAARecordOnLaunch": NotRequired[AttributeBooleanValueTypeDef],
        "EnableLniAtDeviceIndex": NotRequired[int],
        "DisableLniAtDeviceIndex": NotRequired[AttributeBooleanValueTypeDef],
    },
)
ModifyVolumeAttributeRequestRequestTypeDef = TypedDict(
    "ModifyVolumeAttributeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "AutoEnableIO": NotRequired[AttributeBooleanValueTypeDef],
        "DryRun": NotRequired[bool],
    },
)
ModifyVolumeAttributeRequestVolumeModifyAttributeTypeDef = TypedDict(
    "ModifyVolumeAttributeRequestVolumeModifyAttributeTypeDef",
    {
        "AutoEnableIO": NotRequired[AttributeBooleanValueTypeDef],
        "DryRun": NotRequired[bool],
    },
)
ModifyVpcAttributeRequestRequestTypeDef = TypedDict(
    "ModifyVpcAttributeRequestRequestTypeDef",
    {
        "VpcId": str,
        "EnableDnsHostnames": NotRequired[AttributeBooleanValueTypeDef],
        "EnableDnsSupport": NotRequired[AttributeBooleanValueTypeDef],
        "EnableNetworkAddressUsageMetrics": NotRequired[AttributeBooleanValueTypeDef],
    },
)
ModifyVpcAttributeRequestVpcModifyAttributeTypeDef = TypedDict(
    "ModifyVpcAttributeRequestVpcModifyAttributeTypeDef",
    {
        "EnableDnsHostnames": NotRequired[AttributeBooleanValueTypeDef],
        "EnableDnsSupport": NotRequired[AttributeBooleanValueTypeDef],
        "EnableNetworkAddressUsageMetrics": NotRequired[AttributeBooleanValueTypeDef],
    },
)
DhcpConfigurationTypeDef = TypedDict(
    "DhcpConfigurationTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[List[AttributeValueTypeDef]],
    },
)
AuthorizationRuleTypeDef = TypedDict(
    "AuthorizationRuleTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "Description": NotRequired[str],
        "GroupId": NotRequired[str],
        "AccessAll": NotRequired[bool],
        "DestinationCidr": NotRequired[str],
        "Status": NotRequired[ClientVpnAuthorizationRuleStatusTypeDef],
    },
)
AuthorizeClientVpnIngressResultTypeDef = TypedDict(
    "AuthorizeClientVpnIngressResultTypeDef",
    {
        "Status": ClientVpnAuthorizationRuleStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RevokeClientVpnIngressResultTypeDef = TypedDict(
    "RevokeClientVpnIngressResultTypeDef",
    {
        "Status": ClientVpnAuthorizationRuleStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "State": NotRequired[AvailabilityZoneStateType],
        "OptInStatus": NotRequired[AvailabilityZoneOptInStatusType],
        "Messages": NotRequired[List[AvailabilityZoneMessageTypeDef]],
        "RegionName": NotRequired[str],
        "ZoneName": NotRequired[str],
        "ZoneId": NotRequired[str],
        "GroupName": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "ZoneType": NotRequired[str],
        "ParentZoneName": NotRequired[str],
        "ParentZoneId": NotRequired[str],
    },
)
AvailableCapacityTypeDef = TypedDict(
    "AvailableCapacityTypeDef",
    {
        "AvailableInstanceCapacity": NotRequired[List[InstanceCapacityTypeDef]],
        "AvailableVCpus": NotRequired[int],
    },
)
BlobAttributeValueTypeDef = TypedDict(
    "BlobAttributeValueTypeDef",
    {
        "Value": NotRequired[BlobTypeDef],
    },
)
S3StorageTypeDef = TypedDict(
    "S3StorageTypeDef",
    {
        "AWSAccessKeyId": NotRequired[str],
        "Bucket": NotRequired[str],
        "Prefix": NotRequired[str],
        "UploadPolicy": NotRequired[BlobTypeDef],
        "UploadPolicySignature": NotRequired[str],
    },
)
BlockDeviceMappingTypeDef = TypedDict(
    "BlockDeviceMappingTypeDef",
    {
        "DeviceName": NotRequired[str],
        "VirtualName": NotRequired[str],
        "Ebs": NotRequired[EbsBlockDeviceTypeDef],
        "NoDevice": NotRequired[str],
    },
)
DeprovisionIpamByoasnResultTypeDef = TypedDict(
    "DeprovisionIpamByoasnResultTypeDef",
    {
        "Byoasn": ByoasnTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIpamByoasnResultTypeDef = TypedDict(
    "DescribeIpamByoasnResultTypeDef",
    {
        "Byoasns": List[ByoasnTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisionIpamByoasnResultTypeDef = TypedDict(
    "ProvisionIpamByoasnResultTypeDef",
    {
        "Byoasn": ByoasnTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FailedCapacityReservationFleetCancellationResultTypeDef = TypedDict(
    "FailedCapacityReservationFleetCancellationResultTypeDef",
    {
        "CapacityReservationFleetId": NotRequired[str],
        "CancelCapacityReservationFleetError": NotRequired[
            CancelCapacityReservationFleetErrorTypeDef
        ],
    },
)
CancelSpotFleetRequestsErrorItemTypeDef = TypedDict(
    "CancelSpotFleetRequestsErrorItemTypeDef",
    {
        "Error": NotRequired[CancelSpotFleetRequestsErrorTypeDef],
        "SpotFleetRequestId": NotRequired[str],
    },
)
CancelSpotInstanceRequestsResultTypeDef = TypedDict(
    "CancelSpotInstanceRequestsResultTypeDef",
    {
        "CancelledSpotInstanceRequests": List[CancelledSpotInstanceRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CapacityReservationTypeDef = TypedDict(
    "CapacityReservationTypeDef",
    {
        "CapacityReservationId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "CapacityReservationArn": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "InstanceType": NotRequired[str],
        "InstancePlatform": NotRequired[CapacityReservationInstancePlatformType],
        "AvailabilityZone": NotRequired[str],
        "Tenancy": NotRequired[CapacityReservationTenancyType],
        "TotalInstanceCount": NotRequired[int],
        "AvailableInstanceCount": NotRequired[int],
        "EbsOptimized": NotRequired[bool],
        "EphemeralStorage": NotRequired[bool],
        "State": NotRequired[CapacityReservationStateType],
        "StartDate": NotRequired[datetime],
        "EndDate": NotRequired[datetime],
        "EndDateType": NotRequired[EndDateTypeType],
        "InstanceMatchCriteria": NotRequired[InstanceMatchCriteriaType],
        "CreateDate": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
        "OutpostArn": NotRequired[str],
        "CapacityReservationFleetId": NotRequired[str],
        "PlacementGroupArn": NotRequired[str],
        "CapacityAllocations": NotRequired[List[CapacityAllocationTypeDef]],
        "ReservationType": NotRequired[CapacityReservationTypeType],
    },
)
DescribeCapacityBlockOfferingsResultTypeDef = TypedDict(
    "DescribeCapacityBlockOfferingsResultTypeDef",
    {
        "CapacityBlockOfferings": List[CapacityBlockOfferingTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CapacityReservationFleetTypeDef = TypedDict(
    "CapacityReservationFleetTypeDef",
    {
        "CapacityReservationFleetId": NotRequired[str],
        "CapacityReservationFleetArn": NotRequired[str],
        "State": NotRequired[CapacityReservationFleetStateType],
        "TotalTargetCapacity": NotRequired[int],
        "TotalFulfilledCapacity": NotRequired[float],
        "Tenancy": NotRequired[Literal["default"]],
        "EndDate": NotRequired[datetime],
        "CreateTime": NotRequired[datetime],
        "InstanceMatchCriteria": NotRequired[Literal["open"]],
        "AllocationStrategy": NotRequired[str],
        "InstanceTypeSpecifications": NotRequired[List[FleetCapacityReservationTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
CreateCapacityReservationFleetResultTypeDef = TypedDict(
    "CreateCapacityReservationFleetResultTypeDef",
    {
        "CapacityReservationFleetId": str,
        "State": CapacityReservationFleetStateType,
        "TotalTargetCapacity": int,
        "TotalFulfilledCapacity": float,
        "InstanceMatchCriteria": Literal["open"],
        "AllocationStrategy": str,
        "CreateTime": datetime,
        "EndDate": datetime,
        "Tenancy": Literal["default"],
        "FleetCapacityReservations": List[FleetCapacityReservationTypeDef],
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupsForCapacityReservationResultTypeDef = TypedDict(
    "GetGroupsForCapacityReservationResultTypeDef",
    {
        "NextToken": str,
        "CapacityReservationGroups": List[CapacityReservationGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OnDemandOptionsRequestTypeDef = TypedDict(
    "OnDemandOptionsRequestTypeDef",
    {
        "AllocationStrategy": NotRequired[FleetOnDemandAllocationStrategyType],
        "CapacityReservationOptions": NotRequired[CapacityReservationOptionsRequestTypeDef],
        "SingleInstanceType": NotRequired[bool],
        "SingleAvailabilityZone": NotRequired[bool],
        "MinTargetCapacity": NotRequired[int],
        "MaxTotalPrice": NotRequired[str],
    },
)
OnDemandOptionsTypeDef = TypedDict(
    "OnDemandOptionsTypeDef",
    {
        "AllocationStrategy": NotRequired[FleetOnDemandAllocationStrategyType],
        "CapacityReservationOptions": NotRequired[CapacityReservationOptionsTypeDef],
        "SingleInstanceType": NotRequired[bool],
        "SingleAvailabilityZone": NotRequired[bool],
        "MinTargetCapacity": NotRequired[int],
        "MaxTotalPrice": NotRequired[str],
    },
)
CapacityReservationSpecificationResponseResponseTypeDef = TypedDict(
    "CapacityReservationSpecificationResponseResponseTypeDef",
    {
        "CapacityReservationPreference": CapacityReservationPreferenceType,
        "CapacityReservationTarget": CapacityReservationTargetResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CapacityReservationSpecificationResponseTypeDef = TypedDict(
    "CapacityReservationSpecificationResponseTypeDef",
    {
        "CapacityReservationPreference": NotRequired[CapacityReservationPreferenceType],
        "CapacityReservationTarget": NotRequired[CapacityReservationTargetResponseTypeDef],
    },
)
LaunchTemplateCapacityReservationSpecificationResponseTypeDef = TypedDict(
    "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
    {
        "CapacityReservationPreference": NotRequired[CapacityReservationPreferenceType],
        "CapacityReservationTarget": NotRequired[CapacityReservationTargetResponseTypeDef],
    },
)
CapacityReservationSpecificationTypeDef = TypedDict(
    "CapacityReservationSpecificationTypeDef",
    {
        "CapacityReservationPreference": NotRequired[CapacityReservationPreferenceType],
        "CapacityReservationTarget": NotRequired[CapacityReservationTargetTypeDef],
    },
)
LaunchTemplateCapacityReservationSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
    {
        "CapacityReservationPreference": NotRequired[CapacityReservationPreferenceType],
        "CapacityReservationTarget": NotRequired[CapacityReservationTargetTypeDef],
    },
)
DescribeVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "DescribeVpcClassicLinkDnsSupportResultTypeDef",
    {
        "NextToken": str,
        "Vpcs": List[ClassicLinkDnsSupportTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ClassicLinkInstanceTypeDef = TypedDict(
    "ClassicLinkInstanceTypeDef",
    {
        "Groups": NotRequired[List[GroupIdentifierTypeDef]],
        "InstanceId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "VpcId": NotRequired[str],
    },
)
ClassicLoadBalancersConfigTypeDef = TypedDict(
    "ClassicLoadBalancersConfigTypeDef",
    {
        "ClassicLoadBalancers": NotRequired[List[ClassicLoadBalancerTypeDef]],
    },
)
ExportClientVpnClientCertificateRevocationListResultTypeDef = TypedDict(
    "ExportClientVpnClientCertificateRevocationListResultTypeDef",
    {
        "CertificateRevocationList": str,
        "Status": ClientCertificateRevocationListStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ClientConnectResponseOptionsTypeDef = TypedDict(
    "ClientConnectResponseOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "LambdaFunctionArn": NotRequired[str],
        "Status": NotRequired[ClientVpnEndpointAttributeStatusTypeDef],
    },
)
ClientVpnAuthenticationRequestTypeDef = TypedDict(
    "ClientVpnAuthenticationRequestTypeDef",
    {
        "Type": NotRequired[ClientVpnAuthenticationTypeType],
        "ActiveDirectory": NotRequired[DirectoryServiceAuthenticationRequestTypeDef],
        "MutualAuthentication": NotRequired[CertificateAuthenticationRequestTypeDef],
        "FederatedAuthentication": NotRequired[FederatedAuthenticationRequestTypeDef],
    },
)
ClientVpnAuthenticationTypeDef = TypedDict(
    "ClientVpnAuthenticationTypeDef",
    {
        "Type": NotRequired[ClientVpnAuthenticationTypeType],
        "ActiveDirectory": NotRequired[DirectoryServiceAuthenticationTypeDef],
        "MutualAuthentication": NotRequired[CertificateAuthenticationTypeDef],
        "FederatedAuthentication": NotRequired[FederatedAuthenticationTypeDef],
    },
)
ClientVpnConnectionTypeDef = TypedDict(
    "ClientVpnConnectionTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "Timestamp": NotRequired[str],
        "ConnectionId": NotRequired[str],
        "Username": NotRequired[str],
        "ConnectionEstablishedTime": NotRequired[str],
        "IngressBytes": NotRequired[str],
        "EgressBytes": NotRequired[str],
        "IngressPackets": NotRequired[str],
        "EgressPackets": NotRequired[str],
        "ClientIp": NotRequired[str],
        "CommonName": NotRequired[str],
        "Status": NotRequired[ClientVpnConnectionStatusTypeDef],
        "ConnectionEndTime": NotRequired[str],
        "PostureComplianceStatuses": NotRequired[List[str]],
    },
)
TerminateConnectionStatusTypeDef = TypedDict(
    "TerminateConnectionStatusTypeDef",
    {
        "ConnectionId": NotRequired[str],
        "PreviousStatus": NotRequired[ClientVpnConnectionStatusTypeDef],
        "CurrentStatus": NotRequired[ClientVpnConnectionStatusTypeDef],
    },
)
CreateClientVpnEndpointResultTypeDef = TypedDict(
    "CreateClientVpnEndpointResultTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Status": ClientVpnEndpointStatusTypeDef,
        "DnsName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteClientVpnEndpointResultTypeDef = TypedDict(
    "DeleteClientVpnEndpointResultTypeDef",
    {
        "Status": ClientVpnEndpointStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ClientVpnRouteTypeDef = TypedDict(
    "ClientVpnRouteTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "DestinationCidr": NotRequired[str],
        "TargetSubnet": NotRequired[str],
        "Type": NotRequired[str],
        "Origin": NotRequired[str],
        "Status": NotRequired[ClientVpnRouteStatusTypeDef],
        "Description": NotRequired[str],
    },
)
CreateClientVpnRouteResultTypeDef = TypedDict(
    "CreateClientVpnRouteResultTypeDef",
    {
        "Status": ClientVpnRouteStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteClientVpnRouteResultTypeDef = TypedDict(
    "DeleteClientVpnRouteResultTypeDef",
    {
        "Status": ClientVpnRouteStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VpnTunnelLogOptionsSpecificationTypeDef = TypedDict(
    "VpnTunnelLogOptionsSpecificationTypeDef",
    {
        "CloudWatchLogOptions": NotRequired[CloudWatchLogOptionsSpecificationTypeDef],
    },
)
VpnTunnelLogOptionsTypeDef = TypedDict(
    "VpnTunnelLogOptionsTypeDef",
    {
        "CloudWatchLogOptions": NotRequired[CloudWatchLogOptionsTypeDef],
    },
)
GetCoipPoolUsageResultTypeDef = TypedDict(
    "GetCoipPoolUsageResultTypeDef",
    {
        "CoipPoolId": str,
        "CoipAddressUsages": List[CoipAddressUsageTypeDef],
        "LocalGatewayRouteTableId": str,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCoipCidrResultTypeDef = TypedDict(
    "CreateCoipCidrResultTypeDef",
    {
        "CoipCidr": CoipCidrTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCoipCidrResultTypeDef = TypedDict(
    "DeleteCoipCidrResultTypeDef",
    {
        "CoipCidr": CoipCidrTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVpcEndpointConnectionNotificationResultTypeDef = TypedDict(
    "CreateVpcEndpointConnectionNotificationResultTypeDef",
    {
        "ConnectionNotification": ConnectionNotificationTypeDef,
        "ClientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcEndpointConnectionNotificationsResultTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionNotificationsResultTypeDef",
    {
        "ConnectionNotificationSet": List[ConnectionNotificationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "ModifyInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
        "DryRun": NotRequired[bool],
        "Name": NotRequired[str],
        "TimeRanges": NotRequired[Sequence[InstanceEventWindowTimeRangeRequestTypeDef]],
        "CronExpression": NotRequired[str],
    },
)
ModifyIpamPoolRequestRequestTypeDef = TypedDict(
    "ModifyIpamPoolRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "AutoImport": NotRequired[bool],
        "AllocationMinNetmaskLength": NotRequired[int],
        "AllocationMaxNetmaskLength": NotRequired[int],
        "AllocationDefaultNetmaskLength": NotRequired[int],
        "ClearAllocationDefaultNetmaskLength": NotRequired[bool],
        "AddAllocationResourceTags": NotRequired[Sequence[RequestIpamResourceTagTypeDef]],
        "RemoveAllocationResourceTags": NotRequired[Sequence[RequestIpamResourceTagTypeDef]],
    },
)
CreateLocalGatewayRouteResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteResultTypeDef",
    {
        "Route": LocalGatewayRouteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLocalGatewayRouteResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteResultTypeDef",
    {
        "Route": LocalGatewayRouteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyLocalGatewayRouteResultTypeDef = TypedDict(
    "ModifyLocalGatewayRouteResultTypeDef",
    {
        "Route": LocalGatewayRouteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchLocalGatewayRoutesResultTypeDef = TypedDict(
    "SearchLocalGatewayRoutesResultTypeDef",
    {
        "Routes": List[LocalGatewayRouteTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkAclEntryRequestNetworkAclCreateEntryTypeDef = TypedDict(
    "CreateNetworkAclEntryRequestNetworkAclCreateEntryTypeDef",
    {
        "Egress": bool,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
        "CidrBlock": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IcmpTypeCode": NotRequired[IcmpTypeCodeTypeDef],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired[PortRangeTypeDef],
    },
)
CreateNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "CreateNetworkAclEntryRequestRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
        "CidrBlock": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IcmpTypeCode": NotRequired[IcmpTypeCodeTypeDef],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired[PortRangeTypeDef],
    },
)
NetworkAclEntryTypeDef = TypedDict(
    "NetworkAclEntryTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "Egress": NotRequired[bool],
        "IcmpTypeCode": NotRequired[IcmpTypeCodeTypeDef],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired[PortRangeTypeDef],
        "Protocol": NotRequired[str],
        "RuleAction": NotRequired[RuleActionType],
        "RuleNumber": NotRequired[int],
    },
)
ReplaceNetworkAclEntryRequestNetworkAclReplaceEntryTypeDef = TypedDict(
    "ReplaceNetworkAclEntryRequestNetworkAclReplaceEntryTypeDef",
    {
        "Egress": bool,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
        "CidrBlock": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IcmpTypeCode": NotRequired[IcmpTypeCodeTypeDef],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired[PortRangeTypeDef],
    },
)
ReplaceNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "ReplaceNetworkAclEntryRequestRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
        "CidrBlock": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IcmpTypeCode": NotRequired[IcmpTypeCodeTypeDef],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired[PortRangeTypeDef],
    },
)
CreateReservedInstancesListingRequestRequestTypeDef = TypedDict(
    "CreateReservedInstancesListingRequestRequestTypeDef",
    {
        "ClientToken": str,
        "InstanceCount": int,
        "PriceSchedules": Sequence[PriceScheduleSpecificationTypeDef],
        "ReservedInstancesId": str,
    },
)
CreateStoreImageTaskRequestRequestTypeDef = TypedDict(
    "CreateStoreImageTaskRequestRequestTypeDef",
    {
        "ImageId": str,
        "Bucket": str,
        "S3ObjectTags": NotRequired[Sequence[S3ObjectTagTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "CreateTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "TrafficDirection": TrafficDirectionType,
        "RuleNumber": int,
        "RuleAction": TrafficMirrorRuleActionType,
        "DestinationCidrBlock": str,
        "SourceCidrBlock": str,
        "DestinationPortRange": NotRequired[TrafficMirrorPortRangeRequestTypeDef],
        "SourcePortRange": NotRequired[TrafficMirrorPortRangeRequestTypeDef],
        "Protocol": NotRequired[int],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)
ModifyTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "TrafficDirection": NotRequired[TrafficDirectionType],
        "RuleNumber": NotRequired[int],
        "RuleAction": NotRequired[TrafficMirrorRuleActionType],
        "DestinationPortRange": NotRequired[TrafficMirrorPortRangeRequestTypeDef],
        "SourcePortRange": NotRequired[TrafficMirrorPortRangeRequestTypeDef],
        "Protocol": NotRequired[int],
        "DestinationCidrBlock": NotRequired[str],
        "SourceCidrBlock": NotRequired[str],
        "Description": NotRequired[str],
        "RemoveFields": NotRequired[Sequence[TrafficMirrorFilterRuleFieldType]],
        "DryRun": NotRequired[bool],
    },
)
ModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef = TypedDict(
    "ModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef",
    {
        "VerifiedAccessEndpointId": str,
        "PolicyEnabled": NotRequired[bool],
        "PolicyDocument": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "SseSpecification": NotRequired[VerifiedAccessSseSpecificationRequestTypeDef],
    },
)
ModifyVerifiedAccessGroupPolicyRequestRequestTypeDef = TypedDict(
    "ModifyVerifiedAccessGroupPolicyRequestRequestTypeDef",
    {
        "VerifiedAccessGroupId": str,
        "PolicyEnabled": NotRequired[bool],
        "PolicyDocument": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "SseSpecification": NotRequired[VerifiedAccessSseSpecificationRequestTypeDef],
    },
)
CreateVolumePermissionModificationsTypeDef = TypedDict(
    "CreateVolumePermissionModificationsTypeDef",
    {
        "Add": NotRequired[Sequence[CreateVolumePermissionTypeDef]],
        "Remove": NotRequired[Sequence[CreateVolumePermissionTypeDef]],
    },
)
ModifyVpcEndpointRequestRequestTypeDef = TypedDict(
    "ModifyVpcEndpointRequestRequestTypeDef",
    {
        "VpcEndpointId": str,
        "DryRun": NotRequired[bool],
        "ResetPolicy": NotRequired[bool],
        "PolicyDocument": NotRequired[str],
        "AddRouteTableIds": NotRequired[Sequence[str]],
        "RemoveRouteTableIds": NotRequired[Sequence[str]],
        "AddSubnetIds": NotRequired[Sequence[str]],
        "RemoveSubnetIds": NotRequired[Sequence[str]],
        "AddSecurityGroupIds": NotRequired[Sequence[str]],
        "RemoveSecurityGroupIds": NotRequired[Sequence[str]],
        "IpAddressType": NotRequired[IpAddressTypeType],
        "DnsOptions": NotRequired[DnsOptionsSpecificationTypeDef],
        "PrivateDnsEnabled": NotRequired[bool],
        "SubnetConfigurations": NotRequired[Sequence[SubnetConfigurationTypeDef]],
    },
)
GetAwsNetworkPerformanceDataRequestRequestTypeDef = TypedDict(
    "GetAwsNetworkPerformanceDataRequestRequestTypeDef",
    {
        "DataQueries": NotRequired[Sequence[DataQueryTypeDef]],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DataResponseTypeDef = TypedDict(
    "DataResponseTypeDef",
    {
        "Id": NotRequired[str],
        "Source": NotRequired[str],
        "Destination": NotRequired[str],
        "Metric": NotRequired[Literal["aggregate-latency"]],
        "Statistic": NotRequired[Literal["p50"]],
        "Period": NotRequired[PeriodTypeType],
        "MetricPoints": NotRequired[List[MetricPointTypeDef]],
    },
)
DeleteFleetErrorItemTypeDef = TypedDict(
    "DeleteFleetErrorItemTypeDef",
    {
        "Error": NotRequired[DeleteFleetErrorTypeDef],
        "FleetId": NotRequired[str],
    },
)
DeleteInstanceEventWindowResultTypeDef = TypedDict(
    "DeleteInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindowState": InstanceEventWindowStateChangeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLaunchTemplateVersionsResponseErrorItemTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "ResponseError": NotRequired[ResponseErrorTypeDef],
    },
)
FailedQueuedPurchaseDeletionTypeDef = TypedDict(
    "FailedQueuedPurchaseDeletionTypeDef",
    {
        "Error": NotRequired[DeleteQueuedReservedInstancesErrorTypeDef],
        "ReservedInstancesId": NotRequired[str],
    },
)
DeregisterInstanceEventNotificationAttributesRequestRequestTypeDef = TypedDict(
    "DeregisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    {
        "InstanceTagAttribute": DeregisterInstanceTagAttributeRequestTypeDef,
        "DryRun": NotRequired[bool],
    },
)
DeregisterInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "DeregisterInstanceEventNotificationAttributesResultTypeDef",
    {
        "InstanceTagAttribute": InstanceTagNotificationAttributeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "DescribeInstanceEventNotificationAttributesResultTypeDef",
    {
        "InstanceTagAttribute": InstanceTagNotificationAttributeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "RegisterInstanceEventNotificationAttributesResultTypeDef",
    {
        "InstanceTagAttribute": InstanceTagNotificationAttributeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeregisterTransitGatewayMulticastGroupMembersResultTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupMembersResultTypeDef",
    {
        "DeregisteredMulticastGroupMembers": TransitGatewayMulticastDeregisteredGroupMembersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    {
        "DeregisteredMulticastGroupSources": TransitGatewayMulticastDeregisteredGroupSourcesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAddressTransfersRequestDescribeAddressTransfersPaginateTypeDef = TypedDict(
    "DescribeAddressTransfersRequestDescribeAddressTransfersPaginateTypeDef",
    {
        "AllocationIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAddressesAttributeRequestDescribeAddressesAttributePaginateTypeDef = TypedDict(
    "DescribeAddressesAttributeRequestDescribeAddressesAttributePaginateTypeDef",
    {
        "AllocationIds": NotRequired[Sequence[str]],
        "Attribute": NotRequired[Literal["domain-name"]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeByoipCidrsRequestDescribeByoipCidrsPaginateTypeDef = TypedDict(
    "DescribeByoipCidrsRequestDescribeByoipCidrsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCapacityBlockOfferingsRequestDescribeCapacityBlockOfferingsPaginateTypeDef = TypedDict(
    "DescribeCapacityBlockOfferingsRequestDescribeCapacityBlockOfferingsPaginateTypeDef",
    {
        "InstanceType": str,
        "InstanceCount": int,
        "CapacityDurationHours": int,
        "DryRun": NotRequired[bool],
        "StartDateRange": NotRequired[TimestampTypeDef],
        "EndDateRange": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePrincipalIdFormatRequestDescribePrincipalIdFormatPaginateTypeDef = TypedDict(
    "DescribePrincipalIdFormatRequestDescribePrincipalIdFormatPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Resources": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSpotFleetInstancesRequestDescribeSpotFleetInstancesPaginateTypeDef = TypedDict(
    "DescribeSpotFleetInstancesRequestDescribeSpotFleetInstancesPaginateTypeDef",
    {
        "SpotFleetRequestId": str,
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSpotFleetRequestsRequestDescribeSpotFleetRequestsPaginateTypeDef = TypedDict(
    "DescribeSpotFleetRequestsRequestDescribeSpotFleetRequestsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "SpotFleetRequestIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeStaleSecurityGroupsRequestDescribeStaleSecurityGroupsPaginateTypeDef = TypedDict(
    "DescribeStaleSecurityGroupsRequestDescribeStaleSecurityGroupsPaginateTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVpcClassicLinkDnsSupportRequestDescribeVpcClassicLinkDnsSupportPaginateTypeDef = TypedDict(
    "DescribeVpcClassicLinkDnsSupportRequestDescribeVpcClassicLinkDnsSupportPaginateTypeDef",
    {
        "VpcIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetAssociatedIpv6PoolCidrsRequestGetAssociatedIpv6PoolCidrsPaginateTypeDef = TypedDict(
    "GetAssociatedIpv6PoolCidrsRequestGetAssociatedIpv6PoolCidrsPaginateTypeDef",
    {
        "PoolId": str,
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetAwsNetworkPerformanceDataRequestGetAwsNetworkPerformanceDataPaginateTypeDef = TypedDict(
    "GetAwsNetworkPerformanceDataRequestGetAwsNetworkPerformanceDataPaginateTypeDef",
    {
        "DataQueries": NotRequired[Sequence[DataQueryTypeDef]],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetGroupsForCapacityReservationRequestGetGroupsForCapacityReservationPaginateTypeDef = TypedDict(
    "GetGroupsForCapacityReservationRequestGetGroupsForCapacityReservationPaginateTypeDef",
    {
        "CapacityReservationId": str,
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIpamAddressHistoryRequestGetIpamAddressHistoryPaginateTypeDef = TypedDict(
    "GetIpamAddressHistoryRequestGetIpamAddressHistoryPaginateTypeDef",
    {
        "Cidr": str,
        "IpamScopeId": str,
        "DryRun": NotRequired[bool],
        "VpcId": NotRequired[str],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetManagedPrefixListAssociationsRequestGetManagedPrefixListAssociationsPaginateTypeDef = TypedDict(
    "GetManagedPrefixListAssociationsRequestGetManagedPrefixListAssociationsPaginateTypeDef",
    {
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetManagedPrefixListEntriesRequestGetManagedPrefixListEntriesPaginateTypeDef = TypedDict(
    "GetManagedPrefixListEntriesRequestGetManagedPrefixListEntriesPaginateTypeDef",
    {
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
        "TargetVersion": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetNetworkInsightsAccessScopeAnalysisFindingsRequestGetNetworkInsightsAccessScopeAnalysisFindingsPaginateTypeDef = TypedDict(
    "GetNetworkInsightsAccessScopeAnalysisFindingsRequestGetNetworkInsightsAccessScopeAnalysisFindingsPaginateTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetVpnConnectionDeviceTypesRequestGetVpnConnectionDeviceTypesPaginateTypeDef = TypedDict(
    "GetVpnConnectionDeviceTypesRequestGetVpnConnectionDeviceTypesPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListImagesInRecycleBinRequestListImagesInRecycleBinPaginateTypeDef = TypedDict(
    "ListImagesInRecycleBinRequestListImagesInRecycleBinPaginateTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSnapshotsInRecycleBinRequestListSnapshotsInRecycleBinPaginateTypeDef = TypedDict(
    "ListSnapshotsInRecycleBinRequestListSnapshotsInRecycleBinPaginateTypeDef",
    {
        "SnapshotIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAddressesRequestRequestTypeDef = TypedDict(
    "DescribeAddressesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PublicIps": NotRequired[Sequence[str]],
        "AllocationIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
DescribeAvailabilityZonesRequestRequestTypeDef = TypedDict(
    "DescribeAvailabilityZonesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ZoneNames": NotRequired[Sequence[str]],
        "ZoneIds": NotRequired[Sequence[str]],
        "AllAvailabilityZones": NotRequired[bool],
        "DryRun": NotRequired[bool],
    },
)
DescribeAwsNetworkPerformanceMetricSubscriptionsRequestDescribeAwsNetworkPerformanceMetricSubscriptionsPaginateTypeDef = TypedDict(
    "DescribeAwsNetworkPerformanceMetricSubscriptionsRequestDescribeAwsNetworkPerformanceMetricSubscriptionsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAwsNetworkPerformanceMetricSubscriptionsRequestRequestTypeDef = TypedDict(
    "DescribeAwsNetworkPerformanceMetricSubscriptionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeBundleTasksRequestRequestTypeDef = TypedDict(
    "DescribeBundleTasksRequestRequestTypeDef",
    {
        "BundleIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeCapacityReservationFleetsRequestDescribeCapacityReservationFleetsPaginateTypeDef = (
    TypedDict(
        "DescribeCapacityReservationFleetsRequestDescribeCapacityReservationFleetsPaginateTypeDef",
        {
            "CapacityReservationFleetIds": NotRequired[Sequence[str]],
            "Filters": NotRequired[Sequence[FilterTypeDef]],
            "DryRun": NotRequired[bool],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeCapacityReservationFleetsRequestRequestTypeDef = TypedDict(
    "DescribeCapacityReservationFleetsRequestRequestTypeDef",
    {
        "CapacityReservationFleetIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeCapacityReservationsRequestDescribeCapacityReservationsPaginateTypeDef = TypedDict(
    "DescribeCapacityReservationsRequestDescribeCapacityReservationsPaginateTypeDef",
    {
        "CapacityReservationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCapacityReservationsRequestRequestTypeDef = TypedDict(
    "DescribeCapacityReservationsRequestRequestTypeDef",
    {
        "CapacityReservationIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeCarrierGatewaysRequestDescribeCarrierGatewaysPaginateTypeDef = TypedDict(
    "DescribeCarrierGatewaysRequestDescribeCarrierGatewaysPaginateTypeDef",
    {
        "CarrierGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCarrierGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeCarrierGatewaysRequestRequestTypeDef",
    {
        "CarrierGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeClassicLinkInstancesRequestDescribeClassicLinkInstancesPaginateTypeDef = TypedDict(
    "DescribeClassicLinkInstancesRequestDescribeClassicLinkInstancesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "InstanceIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeClassicLinkInstancesRequestRequestTypeDef = TypedDict(
    "DescribeClassicLinkInstancesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "InstanceIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeClientVpnAuthorizationRulesRequestDescribeClientVpnAuthorizationRulesPaginateTypeDef = TypedDict(
    "DescribeClientVpnAuthorizationRulesRequestDescribeClientVpnAuthorizationRulesPaginateTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeClientVpnAuthorizationRulesRequestRequestTypeDef = TypedDict(
    "DescribeClientVpnAuthorizationRulesRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
    },
)
DescribeClientVpnConnectionsRequestDescribeClientVpnConnectionsPaginateTypeDef = TypedDict(
    "DescribeClientVpnConnectionsRequestDescribeClientVpnConnectionsPaginateTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeClientVpnConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeClientVpnConnectionsRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
DescribeClientVpnEndpointsRequestDescribeClientVpnEndpointsPaginateTypeDef = TypedDict(
    "DescribeClientVpnEndpointsRequestDescribeClientVpnEndpointsPaginateTypeDef",
    {
        "ClientVpnEndpointIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeClientVpnEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeClientVpnEndpointsRequestRequestTypeDef",
    {
        "ClientVpnEndpointIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeClientVpnRoutesRequestDescribeClientVpnRoutesPaginateTypeDef = TypedDict(
    "DescribeClientVpnRoutesRequestDescribeClientVpnRoutesPaginateTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeClientVpnRoutesRequestRequestTypeDef = TypedDict(
    "DescribeClientVpnRoutesRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeClientVpnTargetNetworksRequestDescribeClientVpnTargetNetworksPaginateTypeDef = TypedDict(
    "DescribeClientVpnTargetNetworksRequestDescribeClientVpnTargetNetworksPaginateTypeDef",
    {
        "ClientVpnEndpointId": str,
        "AssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeClientVpnTargetNetworksRequestRequestTypeDef = TypedDict(
    "DescribeClientVpnTargetNetworksRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "AssociationIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeCoipPoolsRequestDescribeCoipPoolsPaginateTypeDef = TypedDict(
    "DescribeCoipPoolsRequestDescribeCoipPoolsPaginateTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCoipPoolsRequestRequestTypeDef = TypedDict(
    "DescribeCoipPoolsRequestRequestTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeCustomerGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeCustomerGatewaysRequestRequestTypeDef",
    {
        "CustomerGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeDhcpOptionsRequestDescribeDhcpOptionsPaginateTypeDef = TypedDict(
    "DescribeDhcpOptionsRequestDescribeDhcpOptionsPaginateTypeDef",
    {
        "DhcpOptionsIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDhcpOptionsRequestRequestTypeDef = TypedDict(
    "DescribeDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpOptionsIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeEgressOnlyInternetGatewaysRequestDescribeEgressOnlyInternetGatewaysPaginateTypeDef = TypedDict(
    "DescribeEgressOnlyInternetGatewaysRequestDescribeEgressOnlyInternetGatewaysPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "EgressOnlyInternetGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEgressOnlyInternetGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeEgressOnlyInternetGatewaysRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "EgressOnlyInternetGatewayIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeElasticGpusRequestRequestTypeDef = TypedDict(
    "DescribeElasticGpusRequestRequestTypeDef",
    {
        "ElasticGpuIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeExportImageTasksRequestDescribeExportImageTasksPaginateTypeDef = TypedDict(
    "DescribeExportImageTasksRequestDescribeExportImageTasksPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ExportImageTaskIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeExportImageTasksRequestRequestTypeDef = TypedDict(
    "DescribeExportImageTasksRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ExportImageTaskIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeExportTasksRequestRequestTypeDef = TypedDict(
    "DescribeExportTasksRequestRequestTypeDef",
    {
        "ExportTaskIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeFastLaunchImagesRequestDescribeFastLaunchImagesPaginateTypeDef = TypedDict(
    "DescribeFastLaunchImagesRequestDescribeFastLaunchImagesPaginateTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFastLaunchImagesRequestRequestTypeDef = TypedDict(
    "DescribeFastLaunchImagesRequestRequestTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeFastSnapshotRestoresRequestDescribeFastSnapshotRestoresPaginateTypeDef = TypedDict(
    "DescribeFastSnapshotRestoresRequestDescribeFastSnapshotRestoresPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFastSnapshotRestoresRequestRequestTypeDef = TypedDict(
    "DescribeFastSnapshotRestoresRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeFleetInstancesRequestRequestTypeDef = TypedDict(
    "DescribeFleetInstancesRequestRequestTypeDef",
    {
        "FleetId": str,
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeFleetsRequestDescribeFleetsPaginateTypeDef = TypedDict(
    "DescribeFleetsRequestDescribeFleetsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "FleetIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFleetsRequestRequestTypeDef = TypedDict(
    "DescribeFleetsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "FleetIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeFlowLogsRequestDescribeFlowLogsPaginateTypeDef = TypedDict(
    "DescribeFlowLogsRequestDescribeFlowLogsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "FlowLogIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFlowLogsRequestRequestTypeDef = TypedDict(
    "DescribeFlowLogsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "FlowLogIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeFpgaImagesRequestDescribeFpgaImagesPaginateTypeDef = TypedDict(
    "DescribeFpgaImagesRequestDescribeFpgaImagesPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "FpgaImageIds": NotRequired[Sequence[str]],
        "Owners": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFpgaImagesRequestRequestTypeDef = TypedDict(
    "DescribeFpgaImagesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "FpgaImageIds": NotRequired[Sequence[str]],
        "Owners": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeHostReservationOfferingsRequestDescribeHostReservationOfferingsPaginateTypeDef = TypedDict(
    "DescribeHostReservationOfferingsRequestDescribeHostReservationOfferingsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxDuration": NotRequired[int],
        "MinDuration": NotRequired[int],
        "OfferingId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeHostReservationOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeHostReservationOfferingsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxDuration": NotRequired[int],
        "MaxResults": NotRequired[int],
        "MinDuration": NotRequired[int],
        "NextToken": NotRequired[str],
        "OfferingId": NotRequired[str],
    },
)
DescribeHostReservationsRequestDescribeHostReservationsPaginateTypeDef = TypedDict(
    "DescribeHostReservationsRequestDescribeHostReservationsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "HostReservationIdSet": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeHostReservationsRequestRequestTypeDef = TypedDict(
    "DescribeHostReservationsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "HostReservationIdSet": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeHostsRequestDescribeHostsPaginateTypeDef = TypedDict(
    "DescribeHostsRequestDescribeHostsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "HostIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeHostsRequestRequestTypeDef = TypedDict(
    "DescribeHostsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "HostIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeIamInstanceProfileAssociationsRequestDescribeIamInstanceProfileAssociationsPaginateTypeDef = TypedDict(
    "DescribeIamInstanceProfileAssociationsRequestDescribeIamInstanceProfileAssociationsPaginateTypeDef",
    {
        "AssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeIamInstanceProfileAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeIamInstanceProfileAssociationsRequestRequestTypeDef",
    {
        "AssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeImagesRequestDescribeImagesPaginateTypeDef = TypedDict(
    "DescribeImagesRequestDescribeImagesPaginateTypeDef",
    {
        "ExecutableUsers": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ImageIds": NotRequired[Sequence[str]],
        "Owners": NotRequired[Sequence[str]],
        "IncludeDeprecated": NotRequired[bool],
        "IncludeDisabled": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeImagesRequestRequestTypeDef = TypedDict(
    "DescribeImagesRequestRequestTypeDef",
    {
        "ExecutableUsers": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ImageIds": NotRequired[Sequence[str]],
        "Owners": NotRequired[Sequence[str]],
        "IncludeDeprecated": NotRequired[bool],
        "IncludeDisabled": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeImportImageTasksRequestDescribeImportImageTasksPaginateTypeDef = TypedDict(
    "DescribeImportImageTasksRequestDescribeImportImageTasksPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ImportTaskIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeImportImageTasksRequestRequestTypeDef = TypedDict(
    "DescribeImportImageTasksRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ImportTaskIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeImportSnapshotTasksRequestDescribeImportSnapshotTasksPaginateTypeDef = TypedDict(
    "DescribeImportSnapshotTasksRequestDescribeImportSnapshotTasksPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ImportTaskIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeImportSnapshotTasksRequestRequestTypeDef = TypedDict(
    "DescribeImportSnapshotTasksRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ImportTaskIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInstanceConnectEndpointsRequestDescribeInstanceConnectEndpointsPaginateTypeDef = TypedDict(
    "DescribeInstanceConnectEndpointsRequestDescribeInstanceConnectEndpointsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceConnectEndpointIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstanceConnectEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceConnectEndpointsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceConnectEndpointIds": NotRequired[Sequence[str]],
    },
)
DescribeInstanceCreditSpecificationsRequestDescribeInstanceCreditSpecificationsPaginateTypeDef = TypedDict(
    "DescribeInstanceCreditSpecificationsRequestDescribeInstanceCreditSpecificationsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstanceCreditSpecificationsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceCreditSpecificationsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInstanceEventWindowsRequestDescribeInstanceEventWindowsPaginateTypeDef = TypedDict(
    "DescribeInstanceEventWindowsRequestDescribeInstanceEventWindowsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "InstanceEventWindowIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstanceEventWindowsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceEventWindowsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "InstanceEventWindowIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInstanceStatusRequestDescribeInstanceStatusPaginateTypeDef = TypedDict(
    "DescribeInstanceStatusRequestDescribeInstanceStatusPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "IncludeAllInstances": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstanceStatusRequestRequestTypeDef = TypedDict(
    "DescribeInstanceStatusRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IncludeAllInstances": NotRequired[bool],
    },
)
DescribeInstanceTopologyRequestDescribeInstanceTopologyPaginateTypeDef = TypedDict(
    "DescribeInstanceTopologyRequestDescribeInstanceTopologyPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "InstanceIds": NotRequired[Sequence[str]],
        "GroupNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstanceTopologyRequestRequestTypeDef = TypedDict(
    "DescribeInstanceTopologyRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "InstanceIds": NotRequired[Sequence[str]],
        "GroupNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeInstanceTypeOfferingsRequestDescribeInstanceTypeOfferingsPaginateTypeDef = TypedDict(
    "DescribeInstanceTypeOfferingsRequestDescribeInstanceTypeOfferingsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "LocationType": NotRequired[LocationTypeType],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstanceTypeOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceTypeOfferingsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "LocationType": NotRequired[LocationTypeType],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInstanceTypesRequestDescribeInstanceTypesPaginateTypeDef = TypedDict(
    "DescribeInstanceTypesRequestDescribeInstanceTypesPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "InstanceTypes": NotRequired[Sequence[InstanceTypeType]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstanceTypesRequestRequestTypeDef = TypedDict(
    "DescribeInstanceTypesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "InstanceTypes": NotRequired[Sequence[InstanceTypeType]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInstancesRequestDescribeInstancesPaginateTypeDef = TypedDict(
    "DescribeInstancesRequestDescribeInstancesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstancesRequestRequestTypeDef = TypedDict(
    "DescribeInstancesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInternetGatewaysRequestDescribeInternetGatewaysPaginateTypeDef = TypedDict(
    "DescribeInternetGatewaysRequestDescribeInternetGatewaysPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "InternetGatewayIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInternetGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeInternetGatewaysRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "InternetGatewayIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeIpamPoolsRequestDescribeIpamPoolsPaginateTypeDef = TypedDict(
    "DescribeIpamPoolsRequestDescribeIpamPoolsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "IpamPoolIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeIpamPoolsRequestRequestTypeDef = TypedDict(
    "DescribeIpamPoolsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "IpamPoolIds": NotRequired[Sequence[str]],
    },
)
DescribeIpamResourceDiscoveriesRequestDescribeIpamResourceDiscoveriesPaginateTypeDef = TypedDict(
    "DescribeIpamResourceDiscoveriesRequestDescribeIpamResourceDiscoveriesPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "IpamResourceDiscoveryIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeIpamResourceDiscoveriesRequestRequestTypeDef = TypedDict(
    "DescribeIpamResourceDiscoveriesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "IpamResourceDiscoveryIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeIpamResourceDiscoveryAssociationsRequestDescribeIpamResourceDiscoveryAssociationsPaginateTypeDef = TypedDict(
    "DescribeIpamResourceDiscoveryAssociationsRequestDescribeIpamResourceDiscoveryAssociationsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "IpamResourceDiscoveryAssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeIpamResourceDiscoveryAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeIpamResourceDiscoveryAssociationsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "IpamResourceDiscoveryAssociationIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeIpamScopesRequestDescribeIpamScopesPaginateTypeDef = TypedDict(
    "DescribeIpamScopesRequestDescribeIpamScopesPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "IpamScopeIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeIpamScopesRequestRequestTypeDef = TypedDict(
    "DescribeIpamScopesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "IpamScopeIds": NotRequired[Sequence[str]],
    },
)
DescribeIpamsRequestDescribeIpamsPaginateTypeDef = TypedDict(
    "DescribeIpamsRequestDescribeIpamsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "IpamIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeIpamsRequestRequestTypeDef = TypedDict(
    "DescribeIpamsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "IpamIds": NotRequired[Sequence[str]],
    },
)
DescribeIpv6PoolsRequestDescribeIpv6PoolsPaginateTypeDef = TypedDict(
    "DescribeIpv6PoolsRequestDescribeIpv6PoolsPaginateTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeIpv6PoolsRequestRequestTypeDef = TypedDict(
    "DescribeIpv6PoolsRequestRequestTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeKeyPairsRequestRequestTypeDef = TypedDict(
    "DescribeKeyPairsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "KeyNames": NotRequired[Sequence[str]],
        "KeyPairIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "IncludePublicKey": NotRequired[bool],
    },
)
DescribeLaunchTemplateVersionsRequestDescribeLaunchTemplateVersionsPaginateTypeDef = TypedDict(
    "DescribeLaunchTemplateVersionsRequestDescribeLaunchTemplateVersionsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Versions": NotRequired[Sequence[str]],
        "MinVersion": NotRequired[str],
        "MaxVersion": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ResolveAlias": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLaunchTemplateVersionsRequestRequestTypeDef = TypedDict(
    "DescribeLaunchTemplateVersionsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Versions": NotRequired[Sequence[str]],
        "MinVersion": NotRequired[str],
        "MaxVersion": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ResolveAlias": NotRequired[bool],
    },
)
DescribeLaunchTemplatesRequestDescribeLaunchTemplatesPaginateTypeDef = TypedDict(
    "DescribeLaunchTemplatesRequestDescribeLaunchTemplatesPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "LaunchTemplateIds": NotRequired[Sequence[str]],
        "LaunchTemplateNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLaunchTemplatesRequestRequestTypeDef = TypedDict(
    "DescribeLaunchTemplatesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "LaunchTemplateIds": NotRequired[Sequence[str]],
        "LaunchTemplateNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestDescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginateTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestDescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginateTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeLocalGatewayRouteTableVpcAssociationsRequestDescribeLocalGatewayRouteTableVpcAssociationsPaginateTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVpcAssociationsRequestDescribeLocalGatewayRouteTableVpcAssociationsPaginateTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLocalGatewayRouteTableVpcAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVpcAssociationsRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeLocalGatewayRouteTablesRequestDescribeLocalGatewayRouteTablesPaginateTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTablesRequestDescribeLocalGatewayRouteTablesPaginateTypeDef",
    {
        "LocalGatewayRouteTableIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLocalGatewayRouteTablesRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTablesRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeLocalGatewayVirtualInterfaceGroupsRequestDescribeLocalGatewayVirtualInterfaceGroupsPaginateTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfaceGroupsRequestDescribeLocalGatewayVirtualInterfaceGroupsPaginateTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroupIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLocalGatewayVirtualInterfaceGroupsRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfaceGroupsRequestRequestTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroupIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeLocalGatewayVirtualInterfacesRequestDescribeLocalGatewayVirtualInterfacesPaginateTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfacesRequestDescribeLocalGatewayVirtualInterfacesPaginateTypeDef",
    {
        "LocalGatewayVirtualInterfaceIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLocalGatewayVirtualInterfacesRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfacesRequestRequestTypeDef",
    {
        "LocalGatewayVirtualInterfaceIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeLocalGatewaysRequestDescribeLocalGatewaysPaginateTypeDef = TypedDict(
    "DescribeLocalGatewaysRequestDescribeLocalGatewaysPaginateTypeDef",
    {
        "LocalGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLocalGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewaysRequestRequestTypeDef",
    {
        "LocalGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeLockedSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeLockedSnapshotsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SnapshotIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
DescribeManagedPrefixListsRequestDescribeManagedPrefixListsPaginateTypeDef = TypedDict(
    "DescribeManagedPrefixListsRequestDescribeManagedPrefixListsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PrefixListIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeManagedPrefixListsRequestRequestTypeDef = TypedDict(
    "DescribeManagedPrefixListsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PrefixListIds": NotRequired[Sequence[str]],
    },
)
DescribeMovingAddressesRequestDescribeMovingAddressesPaginateTypeDef = TypedDict(
    "DescribeMovingAddressesRequestDescribeMovingAddressesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PublicIps": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMovingAddressesRequestRequestTypeDef = TypedDict(
    "DescribeMovingAddressesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PublicIps": NotRequired[Sequence[str]],
    },
)
DescribeNatGatewaysRequestDescribeNatGatewaysPaginateTypeDef = TypedDict(
    "DescribeNatGatewaysRequestDescribeNatGatewaysPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NatGatewayIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNatGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeNatGatewaysRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NatGatewayIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)
DescribeNetworkAclsRequestDescribeNetworkAclsPaginateTypeDef = TypedDict(
    "DescribeNetworkAclsRequestDescribeNetworkAclsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "NetworkAclIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNetworkAclsRequestRequestTypeDef = TypedDict(
    "DescribeNetworkAclsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "NetworkAclIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeNetworkInsightsAccessScopeAnalysesRequestDescribeNetworkInsightsAccessScopeAnalysesPaginateTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopeAnalysesRequestDescribeNetworkInsightsAccessScopeAnalysesPaginateTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisIds": NotRequired[Sequence[str]],
        "NetworkInsightsAccessScopeId": NotRequired[str],
        "AnalysisStartTimeBegin": NotRequired[TimestampTypeDef],
        "AnalysisStartTimeEnd": NotRequired[TimestampTypeDef],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNetworkInsightsAccessScopeAnalysesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopeAnalysesRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisIds": NotRequired[Sequence[str]],
        "NetworkInsightsAccessScopeId": NotRequired[str],
        "AnalysisStartTimeBegin": NotRequired[TimestampTypeDef],
        "AnalysisStartTimeEnd": NotRequired[TimestampTypeDef],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)
DescribeNetworkInsightsAccessScopesRequestDescribeNetworkInsightsAccessScopesPaginateTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopesRequestDescribeNetworkInsightsAccessScopesPaginateTypeDef",
    {
        "NetworkInsightsAccessScopeIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNetworkInsightsAccessScopesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopesRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)
DescribeNetworkInsightsAnalysesRequestDescribeNetworkInsightsAnalysesPaginateTypeDef = TypedDict(
    "DescribeNetworkInsightsAnalysesRequestDescribeNetworkInsightsAnalysesPaginateTypeDef",
    {
        "NetworkInsightsAnalysisIds": NotRequired[Sequence[str]],
        "NetworkInsightsPathId": NotRequired[str],
        "AnalysisStartTime": NotRequired[TimestampTypeDef],
        "AnalysisEndTime": NotRequired[TimestampTypeDef],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNetworkInsightsAnalysesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsAnalysesRequestRequestTypeDef",
    {
        "NetworkInsightsAnalysisIds": NotRequired[Sequence[str]],
        "NetworkInsightsPathId": NotRequired[str],
        "AnalysisStartTime": NotRequired[TimestampTypeDef],
        "AnalysisEndTime": NotRequired[TimestampTypeDef],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)
DescribeNetworkInsightsPathsRequestDescribeNetworkInsightsPathsPaginateTypeDef = TypedDict(
    "DescribeNetworkInsightsPathsRequestDescribeNetworkInsightsPathsPaginateTypeDef",
    {
        "NetworkInsightsPathIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNetworkInsightsPathsRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsPathsRequestRequestTypeDef",
    {
        "NetworkInsightsPathIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)
DescribeNetworkInterfacePermissionsRequestDescribeNetworkInterfacePermissionsPaginateTypeDef = TypedDict(
    "DescribeNetworkInterfacePermissionsRequestDescribeNetworkInterfacePermissionsPaginateTypeDef",
    {
        "NetworkInterfacePermissionIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNetworkInterfacePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInterfacePermissionsRequestRequestTypeDef",
    {
        "NetworkInterfacePermissionIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeNetworkInterfacesRequestDescribeNetworkInterfacesPaginateTypeDef = TypedDict(
    "DescribeNetworkInterfacesRequestDescribeNetworkInterfacesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "NetworkInterfaceIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNetworkInterfacesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInterfacesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "NetworkInterfaceIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribePlacementGroupsRequestRequestTypeDef = TypedDict(
    "DescribePlacementGroupsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "GroupNames": NotRequired[Sequence[str]],
        "GroupIds": NotRequired[Sequence[str]],
    },
)
DescribePrefixListsRequestDescribePrefixListsPaginateTypeDef = TypedDict(
    "DescribePrefixListsRequestDescribePrefixListsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PrefixListIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePrefixListsRequestRequestTypeDef = TypedDict(
    "DescribePrefixListsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PrefixListIds": NotRequired[Sequence[str]],
    },
)
DescribePublicIpv4PoolsRequestDescribePublicIpv4PoolsPaginateTypeDef = TypedDict(
    "DescribePublicIpv4PoolsRequestDescribePublicIpv4PoolsPaginateTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePublicIpv4PoolsRequestRequestTypeDef = TypedDict(
    "DescribePublicIpv4PoolsRequestRequestTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeRegionsRequestRequestTypeDef = TypedDict(
    "DescribeRegionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "RegionNames": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "AllRegions": NotRequired[bool],
    },
)
DescribeReplaceRootVolumeTasksRequestDescribeReplaceRootVolumeTasksPaginateTypeDef = TypedDict(
    "DescribeReplaceRootVolumeTasksRequestDescribeReplaceRootVolumeTasksPaginateTypeDef",
    {
        "ReplaceRootVolumeTaskIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReplaceRootVolumeTasksRequestRequestTypeDef = TypedDict(
    "DescribeReplaceRootVolumeTasksRequestRequestTypeDef",
    {
        "ReplaceRootVolumeTaskIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeReservedInstancesListingsRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesListingsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ReservedInstancesId": NotRequired[str],
        "ReservedInstancesListingId": NotRequired[str],
    },
)
DescribeReservedInstancesModificationsRequestDescribeReservedInstancesModificationsPaginateTypeDef = TypedDict(
    "DescribeReservedInstancesModificationsRequestDescribeReservedInstancesModificationsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ReservedInstancesModificationIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReservedInstancesModificationsRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesModificationsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ReservedInstancesModificationIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)
DescribeReservedInstancesOfferingsRequestDescribeReservedInstancesOfferingsPaginateTypeDef = TypedDict(
    "DescribeReservedInstancesOfferingsRequestDescribeReservedInstancesOfferingsPaginateTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "IncludeMarketplace": NotRequired[bool],
        "InstanceType": NotRequired[InstanceTypeType],
        "MaxDuration": NotRequired[int],
        "MaxInstanceCount": NotRequired[int],
        "MinDuration": NotRequired[int],
        "OfferingClass": NotRequired[OfferingClassTypeType],
        "ProductDescription": NotRequired[RIProductDescriptionType],
        "ReservedInstancesOfferingIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "InstanceTenancy": NotRequired[TenancyType],
        "OfferingType": NotRequired[OfferingTypeValuesType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReservedInstancesOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesOfferingsRequestRequestTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "IncludeMarketplace": NotRequired[bool],
        "InstanceType": NotRequired[InstanceTypeType],
        "MaxDuration": NotRequired[int],
        "MaxInstanceCount": NotRequired[int],
        "MinDuration": NotRequired[int],
        "OfferingClass": NotRequired[OfferingClassTypeType],
        "ProductDescription": NotRequired[RIProductDescriptionType],
        "ReservedInstancesOfferingIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "InstanceTenancy": NotRequired[TenancyType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "OfferingType": NotRequired[OfferingTypeValuesType],
    },
)
DescribeReservedInstancesRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "OfferingClass": NotRequired[OfferingClassTypeType],
        "ReservedInstancesIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "OfferingType": NotRequired[OfferingTypeValuesType],
    },
)
DescribeRouteTablesRequestDescribeRouteTablesPaginateTypeDef = TypedDict(
    "DescribeRouteTablesRequestDescribeRouteTablesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "RouteTableIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRouteTablesRequestRequestTypeDef = TypedDict(
    "DescribeRouteTablesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "RouteTableIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeSecurityGroupRulesRequestDescribeSecurityGroupRulesPaginateTypeDef = TypedDict(
    "DescribeSecurityGroupRulesRequestDescribeSecurityGroupRulesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "SecurityGroupRuleIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSecurityGroupRulesRequestRequestTypeDef = TypedDict(
    "DescribeSecurityGroupRulesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "SecurityGroupRuleIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeSecurityGroupsRequestDescribeSecurityGroupsPaginateTypeDef = TypedDict(
    "DescribeSecurityGroupsRequestDescribeSecurityGroupsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "GroupIds": NotRequired[Sequence[str]],
        "GroupNames": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSecurityGroupsRequestRequestTypeDef = TypedDict(
    "DescribeSecurityGroupsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "GroupIds": NotRequired[Sequence[str]],
        "GroupNames": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeSnapshotTierStatusRequestDescribeSnapshotTierStatusPaginateTypeDef = TypedDict(
    "DescribeSnapshotTierStatusRequestDescribeSnapshotTierStatusPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSnapshotTierStatusRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotTierStatusRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef = TypedDict(
    "DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "OwnerIds": NotRequired[Sequence[str]],
        "RestorableByUserIds": NotRequired[Sequence[str]],
        "SnapshotIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "OwnerIds": NotRequired[Sequence[str]],
        "RestorableByUserIds": NotRequired[Sequence[str]],
        "SnapshotIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
DescribeSpotInstanceRequestsRequestDescribeSpotInstanceRequestsPaginateTypeDef = TypedDict(
    "DescribeSpotInstanceRequestsRequestDescribeSpotInstanceRequestsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "SpotInstanceRequestIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSpotInstanceRequestsRequestRequestTypeDef = TypedDict(
    "DescribeSpotInstanceRequestsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "SpotInstanceRequestIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeSpotPriceHistoryRequestDescribeSpotPriceHistoryPaginateTypeDef = TypedDict(
    "DescribeSpotPriceHistoryRequestDescribeSpotPriceHistoryPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "DryRun": NotRequired[bool],
        "EndTime": NotRequired[TimestampTypeDef],
        "InstanceTypes": NotRequired[Sequence[InstanceTypeType]],
        "ProductDescriptions": NotRequired[Sequence[str]],
        "StartTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSpotPriceHistoryRequestRequestTypeDef = TypedDict(
    "DescribeSpotPriceHistoryRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "DryRun": NotRequired[bool],
        "EndTime": NotRequired[TimestampTypeDef],
        "InstanceTypes": NotRequired[Sequence[InstanceTypeType]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ProductDescriptions": NotRequired[Sequence[str]],
        "StartTime": NotRequired[TimestampTypeDef],
    },
)
DescribeStoreImageTasksRequestDescribeStoreImageTasksPaginateTypeDef = TypedDict(
    "DescribeStoreImageTasksRequestDescribeStoreImageTasksPaginateTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeStoreImageTasksRequestRequestTypeDef = TypedDict(
    "DescribeStoreImageTasksRequestRequestTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeSubnetsRequestDescribeSubnetsPaginateTypeDef = TypedDict(
    "DescribeSubnetsRequestDescribeSubnetsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "SubnetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSubnetsRequestRequestTypeDef = TypedDict(
    "DescribeSubnetsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "SubnetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeTagsRequestDescribeTagsPaginateTypeDef = TypedDict(
    "DescribeTagsRequestDescribeTagsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeTrafficMirrorFiltersRequestDescribeTrafficMirrorFiltersPaginateTypeDef = TypedDict(
    "DescribeTrafficMirrorFiltersRequestDescribeTrafficMirrorFiltersPaginateTypeDef",
    {
        "TrafficMirrorFilterIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTrafficMirrorFiltersRequestRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorFiltersRequestRequestTypeDef",
    {
        "TrafficMirrorFilterIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeTrafficMirrorSessionsRequestDescribeTrafficMirrorSessionsPaginateTypeDef = TypedDict(
    "DescribeTrafficMirrorSessionsRequestDescribeTrafficMirrorSessionsPaginateTypeDef",
    {
        "TrafficMirrorSessionIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTrafficMirrorSessionsRequestRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorSessionsRequestRequestTypeDef",
    {
        "TrafficMirrorSessionIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeTrafficMirrorTargetsRequestDescribeTrafficMirrorTargetsPaginateTypeDef = TypedDict(
    "DescribeTrafficMirrorTargetsRequestDescribeTrafficMirrorTargetsPaginateTypeDef",
    {
        "TrafficMirrorTargetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTrafficMirrorTargetsRequestRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorTargetsRequestRequestTypeDef",
    {
        "TrafficMirrorTargetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeTransitGatewayAttachmentsRequestDescribeTransitGatewayAttachmentsPaginateTypeDef = (
    TypedDict(
        "DescribeTransitGatewayAttachmentsRequestDescribeTransitGatewayAttachmentsPaginateTypeDef",
        {
            "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
            "Filters": NotRequired[Sequence[FilterTypeDef]],
            "DryRun": NotRequired[bool],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeTransitGatewayAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayAttachmentsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeTransitGatewayConnectPeersRequestDescribeTransitGatewayConnectPeersPaginateTypeDef = TypedDict(
    "DescribeTransitGatewayConnectPeersRequestDescribeTransitGatewayConnectPeersPaginateTypeDef",
    {
        "TransitGatewayConnectPeerIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTransitGatewayConnectPeersRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayConnectPeersRequestRequestTypeDef",
    {
        "TransitGatewayConnectPeerIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeTransitGatewayConnectsRequestDescribeTransitGatewayConnectsPaginateTypeDef = TypedDict(
    "DescribeTransitGatewayConnectsRequestDescribeTransitGatewayConnectsPaginateTypeDef",
    {
        "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTransitGatewayConnectsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayConnectsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeTransitGatewayMulticastDomainsRequestDescribeTransitGatewayMulticastDomainsPaginateTypeDef = TypedDict(
    "DescribeTransitGatewayMulticastDomainsRequestDescribeTransitGatewayMulticastDomainsPaginateTypeDef",
    {
        "TransitGatewayMulticastDomainIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTransitGatewayMulticastDomainsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayMulticastDomainsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeTransitGatewayPeeringAttachmentsRequestDescribeTransitGatewayPeeringAttachmentsPaginateTypeDef = TypedDict(
    "DescribeTransitGatewayPeeringAttachmentsRequestDescribeTransitGatewayPeeringAttachmentsPaginateTypeDef",
    {
        "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTransitGatewayPeeringAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayPeeringAttachmentsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeTransitGatewayPolicyTablesRequestDescribeTransitGatewayPolicyTablesPaginateTypeDef = TypedDict(
    "DescribeTransitGatewayPolicyTablesRequestDescribeTransitGatewayPolicyTablesPaginateTypeDef",
    {
        "TransitGatewayPolicyTableIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTransitGatewayPolicyTablesRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayPolicyTablesRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeTransitGatewayRouteTableAnnouncementsRequestDescribeTransitGatewayRouteTableAnnouncementsPaginateTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTableAnnouncementsRequestDescribeTransitGatewayRouteTableAnnouncementsPaginateTypeDef",
    {
        "TransitGatewayRouteTableAnnouncementIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTransitGatewayRouteTableAnnouncementsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTableAnnouncementsRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableAnnouncementIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeTransitGatewayRouteTablesRequestDescribeTransitGatewayRouteTablesPaginateTypeDef = (
    TypedDict(
        "DescribeTransitGatewayRouteTablesRequestDescribeTransitGatewayRouteTablesPaginateTypeDef",
        {
            "TransitGatewayRouteTableIds": NotRequired[Sequence[str]],
            "Filters": NotRequired[Sequence[FilterTypeDef]],
            "DryRun": NotRequired[bool],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeTransitGatewayRouteTablesRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTablesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeTransitGatewayVpcAttachmentsRequestDescribeTransitGatewayVpcAttachmentsPaginateTypeDef = TypedDict(
    "DescribeTransitGatewayVpcAttachmentsRequestDescribeTransitGatewayVpcAttachmentsPaginateTypeDef",
    {
        "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTransitGatewayVpcAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayVpcAttachmentsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeTransitGatewaysRequestDescribeTransitGatewaysPaginateTypeDef = TypedDict(
    "DescribeTransitGatewaysRequestDescribeTransitGatewaysPaginateTypeDef",
    {
        "TransitGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTransitGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewaysRequestRequestTypeDef",
    {
        "TransitGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeTrunkInterfaceAssociationsRequestDescribeTrunkInterfaceAssociationsPaginateTypeDef = TypedDict(
    "DescribeTrunkInterfaceAssociationsRequestDescribeTrunkInterfaceAssociationsPaginateTypeDef",
    {
        "AssociationIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTrunkInterfaceAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeTrunkInterfaceAssociationsRequestRequestTypeDef",
    {
        "AssociationIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeVerifiedAccessEndpointsRequestDescribeVerifiedAccessEndpointsPaginateTypeDef = TypedDict(
    "DescribeVerifiedAccessEndpointsRequestDescribeVerifiedAccessEndpointsPaginateTypeDef",
    {
        "VerifiedAccessEndpointIds": NotRequired[Sequence[str]],
        "VerifiedAccessInstanceId": NotRequired[str],
        "VerifiedAccessGroupId": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVerifiedAccessEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedAccessEndpointsRequestRequestTypeDef",
    {
        "VerifiedAccessEndpointIds": NotRequired[Sequence[str]],
        "VerifiedAccessInstanceId": NotRequired[str],
        "VerifiedAccessGroupId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeVerifiedAccessGroupsRequestDescribeVerifiedAccessGroupsPaginateTypeDef = TypedDict(
    "DescribeVerifiedAccessGroupsRequestDescribeVerifiedAccessGroupsPaginateTypeDef",
    {
        "VerifiedAccessGroupIds": NotRequired[Sequence[str]],
        "VerifiedAccessInstanceId": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVerifiedAccessGroupsRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedAccessGroupsRequestRequestTypeDef",
    {
        "VerifiedAccessGroupIds": NotRequired[Sequence[str]],
        "VerifiedAccessInstanceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeVerifiedAccessInstanceLoggingConfigurationsRequestDescribeVerifiedAccessInstanceLoggingConfigurationsPaginateTypeDef = TypedDict(
    "DescribeVerifiedAccessInstanceLoggingConfigurationsRequestDescribeVerifiedAccessInstanceLoggingConfigurationsPaginateTypeDef",
    {
        "VerifiedAccessInstanceIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVerifiedAccessInstanceLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedAccessInstanceLoggingConfigurationsRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeVerifiedAccessInstancesRequestDescribeVerifiedAccessInstancesPaginateTypeDef = TypedDict(
    "DescribeVerifiedAccessInstancesRequestDescribeVerifiedAccessInstancesPaginateTypeDef",
    {
        "VerifiedAccessInstanceIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVerifiedAccessInstancesRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedAccessInstancesRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeVerifiedAccessTrustProvidersRequestDescribeVerifiedAccessTrustProvidersPaginateTypeDef = TypedDict(
    "DescribeVerifiedAccessTrustProvidersRequestDescribeVerifiedAccessTrustProvidersPaginateTypeDef",
    {
        "VerifiedAccessTrustProviderIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVerifiedAccessTrustProvidersRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedAccessTrustProvidersRequestRequestTypeDef",
    {
        "VerifiedAccessTrustProviderIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
DescribeVolumeStatusRequestDescribeVolumeStatusPaginateTypeDef = TypedDict(
    "DescribeVolumeStatusRequestDescribeVolumeStatusPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VolumeIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVolumeStatusRequestRequestTypeDef = TypedDict(
    "DescribeVolumeStatusRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "VolumeIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
DescribeVolumeStatusRequestVolumeDescribeStatusTypeDef = TypedDict(
    "DescribeVolumeStatusRequestVolumeDescribeStatusTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
DescribeVolumesModificationsRequestDescribeVolumesModificationsPaginateTypeDef = TypedDict(
    "DescribeVolumesModificationsRequestDescribeVolumesModificationsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "VolumeIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVolumesModificationsRequestRequestTypeDef = TypedDict(
    "DescribeVolumesModificationsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "VolumeIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeVolumesRequestDescribeVolumesPaginateTypeDef = TypedDict(
    "DescribeVolumesRequestDescribeVolumesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VolumeIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVolumesRequestRequestTypeDef = TypedDict(
    "DescribeVolumesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VolumeIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeVpcClassicLinkRequestRequestTypeDef = TypedDict(
    "DescribeVpcClassicLinkRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "VpcIds": NotRequired[Sequence[str]],
    },
)
DescribeVpcEndpointConnectionNotificationsRequestDescribeVpcEndpointConnectionNotificationsPaginateTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionNotificationsRequestDescribeVpcEndpointConnectionNotificationsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "ConnectionNotificationId": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVpcEndpointConnectionNotificationsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "ConnectionNotificationId": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeVpcEndpointConnectionsRequestDescribeVpcEndpointConnectionsPaginateTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionsRequestDescribeVpcEndpointConnectionsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVpcEndpointConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeVpcEndpointServiceConfigurationsRequestDescribeVpcEndpointServiceConfigurationsPaginateTypeDef = TypedDict(
    "DescribeVpcEndpointServiceConfigurationsRequestDescribeVpcEndpointServiceConfigurationsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "ServiceIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVpcEndpointServiceConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "ServiceIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeVpcEndpointServicePermissionsRequestDescribeVpcEndpointServicePermissionsPaginateTypeDef = TypedDict(
    "DescribeVpcEndpointServicePermissionsRequestDescribeVpcEndpointServicePermissionsPaginateTypeDef",
    {
        "ServiceId": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVpcEndpointServicePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointServicePermissionsRequestRequestTypeDef",
    {
        "ServiceId": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeVpcEndpointServicesRequestDescribeVpcEndpointServicesPaginateTypeDef = TypedDict(
    "DescribeVpcEndpointServicesRequestDescribeVpcEndpointServicesPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "ServiceNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVpcEndpointServicesRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointServicesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "ServiceNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeVpcEndpointsRequestDescribeVpcEndpointsPaginateTypeDef = TypedDict(
    "DescribeVpcEndpointsRequestDescribeVpcEndpointsPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "VpcEndpointIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVpcEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointsRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "VpcEndpointIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeVpcPeeringConnectionsRequestDescribeVpcPeeringConnectionsPaginateTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsRequestDescribeVpcPeeringConnectionsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "VpcPeeringConnectionIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVpcPeeringConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "VpcPeeringConnectionIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeVpcsRequestDescribeVpcsPaginateTypeDef = TypedDict(
    "DescribeVpcsRequestDescribeVpcsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VpcIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVpcsRequestRequestTypeDef = TypedDict(
    "DescribeVpcsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VpcIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeVpnConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeVpnConnectionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VpnConnectionIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
DescribeVpnGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeVpnGatewaysRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VpnGatewayIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
ExportTransitGatewayRoutesRequestRequestTypeDef = TypedDict(
    "ExportTransitGatewayRoutesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "S3Bucket": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
GetCoipPoolUsageRequestRequestTypeDef = TypedDict(
    "GetCoipPoolUsageRequestRequestTypeDef",
    {
        "PoolId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
GetIpamDiscoveredAccountsRequestGetIpamDiscoveredAccountsPaginateTypeDef = TypedDict(
    "GetIpamDiscoveredAccountsRequestGetIpamDiscoveredAccountsPaginateTypeDef",
    {
        "IpamResourceDiscoveryId": str,
        "DiscoveryRegion": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIpamDiscoveredAccountsRequestRequestTypeDef = TypedDict(
    "GetIpamDiscoveredAccountsRequestRequestTypeDef",
    {
        "IpamResourceDiscoveryId": str,
        "DiscoveryRegion": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetIpamDiscoveredPublicAddressesRequestRequestTypeDef = TypedDict(
    "GetIpamDiscoveredPublicAddressesRequestRequestTypeDef",
    {
        "IpamResourceDiscoveryId": str,
        "AddressRegion": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetIpamDiscoveredResourceCidrsRequestGetIpamDiscoveredResourceCidrsPaginateTypeDef = TypedDict(
    "GetIpamDiscoveredResourceCidrsRequestGetIpamDiscoveredResourceCidrsPaginateTypeDef",
    {
        "IpamResourceDiscoveryId": str,
        "ResourceRegion": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIpamDiscoveredResourceCidrsRequestRequestTypeDef = TypedDict(
    "GetIpamDiscoveredResourceCidrsRequestRequestTypeDef",
    {
        "IpamResourceDiscoveryId": str,
        "ResourceRegion": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetIpamPoolAllocationsRequestGetIpamPoolAllocationsPaginateTypeDef = TypedDict(
    "GetIpamPoolAllocationsRequestGetIpamPoolAllocationsPaginateTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "IpamPoolAllocationId": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIpamPoolAllocationsRequestRequestTypeDef = TypedDict(
    "GetIpamPoolAllocationsRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "IpamPoolAllocationId": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetIpamPoolCidrsRequestGetIpamPoolCidrsPaginateTypeDef = TypedDict(
    "GetIpamPoolCidrsRequestGetIpamPoolCidrsPaginateTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIpamPoolCidrsRequestRequestTypeDef = TypedDict(
    "GetIpamPoolCidrsRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetIpamResourceCidrsRequestGetIpamResourceCidrsPaginateTypeDef = TypedDict(
    "GetIpamResourceCidrsRequestGetIpamResourceCidrsPaginateTypeDef",
    {
        "IpamScopeId": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "IpamPoolId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[IpamResourceTypeType],
        "ResourceTag": NotRequired[RequestIpamResourceTagTypeDef],
        "ResourceOwner": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIpamResourceCidrsRequestRequestTypeDef = TypedDict(
    "GetIpamResourceCidrsRequestRequestTypeDef",
    {
        "IpamScopeId": str,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "IpamPoolId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[IpamResourceTypeType],
        "ResourceTag": NotRequired[RequestIpamResourceTagTypeDef],
        "ResourceOwner": NotRequired[str],
    },
)
GetSecurityGroupsForVpcRequestGetSecurityGroupsForVpcPaginateTypeDef = TypedDict(
    "GetSecurityGroupsForVpcRequestGetSecurityGroupsForVpcPaginateTypeDef",
    {
        "VpcId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSecurityGroupsForVpcRequestRequestTypeDef = TypedDict(
    "GetSecurityGroupsForVpcRequestRequestTypeDef",
    {
        "VpcId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
GetSubnetCidrReservationsRequestRequestTypeDef = TypedDict(
    "GetSubnetCidrReservationsRequestRequestTypeDef",
    {
        "SubnetId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetTransitGatewayAttachmentPropagationsRequestGetTransitGatewayAttachmentPropagationsPaginateTypeDef = TypedDict(
    "GetTransitGatewayAttachmentPropagationsRequestGetTransitGatewayAttachmentPropagationsPaginateTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTransitGatewayAttachmentPropagationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayAttachmentPropagationsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
GetTransitGatewayMulticastDomainAssociationsRequestGetTransitGatewayMulticastDomainAssociationsPaginateTypeDef = TypedDict(
    "GetTransitGatewayMulticastDomainAssociationsRequestGetTransitGatewayMulticastDomainAssociationsPaginateTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
GetTransitGatewayPolicyTableAssociationsRequestGetTransitGatewayPolicyTableAssociationsPaginateTypeDef = TypedDict(
    "GetTransitGatewayPolicyTableAssociationsRequestGetTransitGatewayPolicyTableAssociationsPaginateTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
GetTransitGatewayPolicyTableEntriesRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayPolicyTableEntriesRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
GetTransitGatewayPrefixListReferencesRequestGetTransitGatewayPrefixListReferencesPaginateTypeDef = TypedDict(
    "GetTransitGatewayPrefixListReferencesRequestGetTransitGatewayPrefixListReferencesPaginateTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTransitGatewayPrefixListReferencesRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayPrefixListReferencesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
GetTransitGatewayRouteTableAssociationsRequestGetTransitGatewayRouteTableAssociationsPaginateTypeDef = TypedDict(
    "GetTransitGatewayRouteTableAssociationsRequestGetTransitGatewayRouteTableAssociationsPaginateTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTransitGatewayRouteTableAssociationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayRouteTableAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
GetTransitGatewayRouteTablePropagationsRequestGetTransitGatewayRouteTablePropagationsPaginateTypeDef = TypedDict(
    "GetTransitGatewayRouteTablePropagationsRequestGetTransitGatewayRouteTablePropagationsPaginateTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTransitGatewayRouteTablePropagationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayRouteTablePropagationsRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
SearchLocalGatewayRoutesRequestRequestTypeDef = TypedDict(
    "SearchLocalGatewayRoutesRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
SearchLocalGatewayRoutesRequestSearchLocalGatewayRoutesPaginateTypeDef = TypedDict(
    "SearchLocalGatewayRoutesRequestSearchLocalGatewayRoutesPaginateTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchTransitGatewayMulticastGroupsRequestRequestTypeDef = TypedDict(
    "SearchTransitGatewayMulticastGroupsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
SearchTransitGatewayMulticastGroupsRequestSearchTransitGatewayMulticastGroupsPaginateTypeDef = TypedDict(
    "SearchTransitGatewayMulticastGroupsRequestSearchTransitGatewayMulticastGroupsPaginateTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchTransitGatewayRoutesRequestRequestTypeDef = TypedDict(
    "SearchTransitGatewayRoutesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": Sequence[FilterTypeDef],
        "MaxResults": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
DescribeAggregateIdFormatResultTypeDef = TypedDict(
    "DescribeAggregateIdFormatResultTypeDef",
    {
        "UseLongIdsAggregated": bool,
        "Statuses": List[IdFormatTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIdFormatResultTypeDef = TypedDict(
    "DescribeIdFormatResultTypeDef",
    {
        "Statuses": List[IdFormatTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIdentityIdFormatResultTypeDef = TypedDict(
    "DescribeIdentityIdFormatResultTypeDef",
    {
        "Statuses": List[IdFormatTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PrincipalIdFormatTypeDef = TypedDict(
    "PrincipalIdFormatTypeDef",
    {
        "Arn": NotRequired[str],
        "Statuses": NotRequired[List[IdFormatTypeDef]],
    },
)
DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef = TypedDict(
    "DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef",
    {
        "NextToken": str,
        "Subscriptions": List[SubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBundleTasksRequestBundleTaskCompleteWaitTypeDef = TypedDict(
    "DescribeBundleTasksRequestBundleTaskCompleteWaitTypeDef",
    {
        "BundleIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeConversionTasksRequestConversionTaskCancelledWaitTypeDef = TypedDict(
    "DescribeConversionTasksRequestConversionTaskCancelledWaitTypeDef",
    {
        "ConversionTaskIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeConversionTasksRequestConversionTaskCompletedWaitTypeDef = TypedDict(
    "DescribeConversionTasksRequestConversionTaskCompletedWaitTypeDef",
    {
        "ConversionTaskIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeConversionTasksRequestConversionTaskDeletedWaitTypeDef = TypedDict(
    "DescribeConversionTasksRequestConversionTaskDeletedWaitTypeDef",
    {
        "ConversionTaskIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeCustomerGatewaysRequestCustomerGatewayAvailableWaitTypeDef = TypedDict(
    "DescribeCustomerGatewaysRequestCustomerGatewayAvailableWaitTypeDef",
    {
        "CustomerGatewayIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeExportTasksRequestExportTaskCancelledWaitTypeDef = TypedDict(
    "DescribeExportTasksRequestExportTaskCancelledWaitTypeDef",
    {
        "ExportTaskIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeExportTasksRequestExportTaskCompletedWaitTypeDef = TypedDict(
    "DescribeExportTasksRequestExportTaskCompletedWaitTypeDef",
    {
        "ExportTaskIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeImagesRequestImageAvailableWaitTypeDef = TypedDict(
    "DescribeImagesRequestImageAvailableWaitTypeDef",
    {
        "ExecutableUsers": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ImageIds": NotRequired[Sequence[str]],
        "Owners": NotRequired[Sequence[str]],
        "IncludeDeprecated": NotRequired[bool],
        "IncludeDisabled": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeImagesRequestImageExistsWaitTypeDef = TypedDict(
    "DescribeImagesRequestImageExistsWaitTypeDef",
    {
        "ExecutableUsers": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ImageIds": NotRequired[Sequence[str]],
        "Owners": NotRequired[Sequence[str]],
        "IncludeDeprecated": NotRequired[bool],
        "IncludeDisabled": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeImportSnapshotTasksRequestSnapshotImportedWaitTypeDef = TypedDict(
    "DescribeImportSnapshotTasksRequestSnapshotImportedWaitTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ImportTaskIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeInstanceStatusRequestInstanceStatusOkWaitTypeDef = TypedDict(
    "DescribeInstanceStatusRequestInstanceStatusOkWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IncludeAllInstances": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeInstanceStatusRequestSystemStatusOkWaitTypeDef = TypedDict(
    "DescribeInstanceStatusRequestSystemStatusOkWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "IncludeAllInstances": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeInstancesRequestInstanceExistsWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceExistsWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeInstancesRequestInstanceRunningWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceRunningWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeInstancesRequestInstanceStoppedWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceStoppedWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeInstancesRequestInstanceTerminatedWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceTerminatedWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "InstanceIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeInternetGatewaysRequestInternetGatewayExistsWaitTypeDef = TypedDict(
    "DescribeInternetGatewaysRequestInternetGatewayExistsWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "InternetGatewayIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeKeyPairsRequestKeyPairExistsWaitTypeDef = TypedDict(
    "DescribeKeyPairsRequestKeyPairExistsWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "KeyNames": NotRequired[Sequence[str]],
        "KeyPairIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "IncludePublicKey": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeNatGatewaysRequestNatGatewayAvailableWaitTypeDef = TypedDict(
    "DescribeNatGatewaysRequestNatGatewayAvailableWaitTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NatGatewayIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeNatGatewaysRequestNatGatewayDeletedWaitTypeDef = TypedDict(
    "DescribeNatGatewaysRequestNatGatewayDeletedWaitTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NatGatewayIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeNetworkInterfacesRequestNetworkInterfaceAvailableWaitTypeDef = TypedDict(
    "DescribeNetworkInterfacesRequestNetworkInterfaceAvailableWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "NetworkInterfaceIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeSecurityGroupsRequestSecurityGroupExistsWaitTypeDef = TypedDict(
    "DescribeSecurityGroupsRequestSecurityGroupExistsWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "GroupIds": NotRequired[Sequence[str]],
        "GroupNames": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeSnapshotsRequestSnapshotCompletedWaitTypeDef = TypedDict(
    "DescribeSnapshotsRequestSnapshotCompletedWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "OwnerIds": NotRequired[Sequence[str]],
        "RestorableByUserIds": NotRequired[Sequence[str]],
        "SnapshotIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeSpotInstanceRequestsRequestSpotInstanceRequestFulfilledWaitTypeDef = TypedDict(
    "DescribeSpotInstanceRequestsRequestSpotInstanceRequestFulfilledWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "SpotInstanceRequestIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeStoreImageTasksRequestStoreImageTaskCompleteWaitTypeDef = TypedDict(
    "DescribeStoreImageTasksRequestStoreImageTaskCompleteWaitTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeSubnetsRequestSubnetAvailableWaitTypeDef = TypedDict(
    "DescribeSubnetsRequestSubnetAvailableWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "SubnetIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeVolumesRequestVolumeAvailableWaitTypeDef = TypedDict(
    "DescribeVolumesRequestVolumeAvailableWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VolumeIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeVolumesRequestVolumeDeletedWaitTypeDef = TypedDict(
    "DescribeVolumesRequestVolumeDeletedWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VolumeIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeVolumesRequestVolumeInUseWaitTypeDef = TypedDict(
    "DescribeVolumesRequestVolumeInUseWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VolumeIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeVpcPeeringConnectionsRequestVpcPeeringConnectionDeletedWaitTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsRequestVpcPeeringConnectionDeletedWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "VpcPeeringConnectionIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeVpcPeeringConnectionsRequestVpcPeeringConnectionExistsWaitTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsRequestVpcPeeringConnectionExistsWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DryRun": NotRequired[bool],
        "VpcPeeringConnectionIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeVpcsRequestVpcAvailableWaitTypeDef = TypedDict(
    "DescribeVpcsRequestVpcAvailableWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VpcIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeVpcsRequestVpcExistsWaitTypeDef = TypedDict(
    "DescribeVpcsRequestVpcExistsWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VpcIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeVpnConnectionsRequestVpnConnectionAvailableWaitTypeDef = TypedDict(
    "DescribeVpnConnectionsRequestVpnConnectionAvailableWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VpnConnectionIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeVpnConnectionsRequestVpnConnectionDeletedWaitTypeDef = TypedDict(
    "DescribeVpnConnectionsRequestVpnConnectionDeletedWaitTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "VpnConnectionIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetPasswordDataRequestPasswordDataAvailableWaitTypeDef = TypedDict(
    "GetPasswordDataRequestPasswordDataAvailableWaitTypeDef",
    {
        "InstanceId": str,
        "DryRun": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeFastLaunchImagesSuccessItemTypeDef = TypedDict(
    "DescribeFastLaunchImagesSuccessItemTypeDef",
    {
        "ImageId": NotRequired[str],
        "ResourceType": NotRequired[Literal["snapshot"]],
        "SnapshotConfiguration": NotRequired[FastLaunchSnapshotConfigurationResponseTypeDef],
        "LaunchTemplate": NotRequired[FastLaunchLaunchTemplateSpecificationResponseTypeDef],
        "MaxParallelLaunches": NotRequired[int],
        "OwnerId": NotRequired[str],
        "State": NotRequired[FastLaunchStateCodeType],
        "StateTransitionReason": NotRequired[str],
        "StateTransitionTime": NotRequired[datetime],
    },
)
DisableFastLaunchResultTypeDef = TypedDict(
    "DisableFastLaunchResultTypeDef",
    {
        "ImageId": str,
        "ResourceType": Literal["snapshot"],
        "SnapshotConfiguration": FastLaunchSnapshotConfigurationResponseTypeDef,
        "LaunchTemplate": FastLaunchLaunchTemplateSpecificationResponseTypeDef,
        "MaxParallelLaunches": int,
        "OwnerId": str,
        "State": FastLaunchStateCodeType,
        "StateTransitionReason": str,
        "StateTransitionTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableFastLaunchResultTypeDef = TypedDict(
    "EnableFastLaunchResultTypeDef",
    {
        "ImageId": str,
        "ResourceType": Literal["snapshot"],
        "SnapshotConfiguration": FastLaunchSnapshotConfigurationResponseTypeDef,
        "LaunchTemplate": FastLaunchLaunchTemplateSpecificationResponseTypeDef,
        "MaxParallelLaunches": int,
        "OwnerId": str,
        "State": FastLaunchStateCodeType,
        "StateTransitionReason": str,
        "StateTransitionTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFastSnapshotRestoresResultTypeDef = TypedDict(
    "DescribeFastSnapshotRestoresResultTypeDef",
    {
        "FastSnapshotRestores": List[DescribeFastSnapshotRestoreSuccessItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHostReservationOfferingsResultTypeDef = TypedDict(
    "DescribeHostReservationOfferingsResultTypeDef",
    {
        "NextToken": str,
        "OfferingSet": List[HostOfferingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstanceCreditSpecificationsResultTypeDef = TypedDict(
    "DescribeInstanceCreditSpecificationsResultTypeDef",
    {
        "InstanceCreditSpecifications": List[InstanceCreditSpecificationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstanceTopologyResultTypeDef = TypedDict(
    "DescribeInstanceTopologyResultTypeDef",
    {
        "Instances": List[InstanceTopologyTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstanceTypeOfferingsResultTypeDef = TypedDict(
    "DescribeInstanceTypeOfferingsResultTypeDef",
    {
        "InstanceTypeOfferings": List[InstanceTypeOfferingTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLockedSnapshotsResultTypeDef = TypedDict(
    "DescribeLockedSnapshotsResultTypeDef",
    {
        "Snapshots": List[LockedSnapshotsInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMovingAddressesResultTypeDef = TypedDict(
    "DescribeMovingAddressesResultTypeDef",
    {
        "MovingAddressStatuses": List[MovingAddressStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePrefixListsResultTypeDef = TypedDict(
    "DescribePrefixListsResultTypeDef",
    {
        "NextToken": str,
        "PrefixLists": List[PrefixListTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRegionsResultTypeDef = TypedDict(
    "DescribeRegionsResultTypeDef",
    {
        "Regions": List[RegionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSecurityGroupReferencesResultTypeDef = TypedDict(
    "DescribeSecurityGroupReferencesResultTypeDef",
    {
        "SecurityGroupReferenceSet": List[SecurityGroupReferenceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSnapshotAttributeResultTypeDef = TypedDict(
    "DescribeSnapshotAttributeResultTypeDef",
    {
        "CreateVolumePermissions": List[CreateVolumePermissionTypeDef],
        "ProductCodes": List[ProductCodeTypeDef],
        "SnapshotId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVolumeAttributeResultTypeDef = TypedDict(
    "DescribeVolumeAttributeResultTypeDef",
    {
        "AutoEnableIO": AttributeBooleanValueTypeDef,
        "ProductCodes": List[ProductCodeTypeDef],
        "VolumeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSpotPriceHistoryResultTypeDef = TypedDict(
    "DescribeSpotPriceHistoryResultTypeDef",
    {
        "NextToken": str,
        "SpotPriceHistory": List[SpotPriceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStoreImageTasksResultTypeDef = TypedDict(
    "DescribeStoreImageTasksResultTypeDef",
    {
        "StoreImageTaskResults": List[StoreImageTaskResultTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTagsResultTypeDef = TypedDict(
    "DescribeTagsResultTypeDef",
    {
        "NextToken": str,
        "Tags": List[TagDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVolumesModificationsResultTypeDef = TypedDict(
    "DescribeVolumesModificationsResultTypeDef",
    {
        "VolumesModifications": List[VolumeModificationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVolumeResultTypeDef = TypedDict(
    "ModifyVolumeResultTypeDef",
    {
        "VolumeModification": VolumeModificationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FlowLogTypeDef = TypedDict(
    "FlowLogTypeDef",
    {
        "CreationTime": NotRequired[datetime],
        "DeliverLogsErrorMessage": NotRequired[str],
        "DeliverLogsPermissionArn": NotRequired[str],
        "DeliverCrossAccountRole": NotRequired[str],
        "DeliverLogsStatus": NotRequired[str],
        "FlowLogId": NotRequired[str],
        "FlowLogStatus": NotRequired[str],
        "LogGroupName": NotRequired[str],
        "ResourceId": NotRequired[str],
        "TrafficType": NotRequired[TrafficTypeType],
        "LogDestinationType": NotRequired[LogDestinationTypeType],
        "LogDestination": NotRequired[str],
        "LogFormat": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "MaxAggregationInterval": NotRequired[int],
        "DestinationOptions": NotRequired[DestinationOptionsResponseTypeDef],
    },
)
DisableFastSnapshotRestoreStateErrorItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreStateErrorItemTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Error": NotRequired[DisableFastSnapshotRestoreStateErrorTypeDef],
    },
)
DisableTransitGatewayRouteTablePropagationResultTypeDef = TypedDict(
    "DisableTransitGatewayRouteTablePropagationResultTypeDef",
    {
        "Propagation": TransitGatewayPropagationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableTransitGatewayRouteTablePropagationResultTypeDef = TypedDict(
    "EnableTransitGatewayRouteTablePropagationResultTypeDef",
    {
        "Propagation": TransitGatewayPropagationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DiskImageTypeDef = TypedDict(
    "DiskImageTypeDef",
    {
        "Description": NotRequired[str],
        "Image": NotRequired[DiskImageDetailTypeDef],
        "Volume": NotRequired[VolumeDetailTypeDef],
    },
)
ImportVolumeRequestRequestTypeDef = TypedDict(
    "ImportVolumeRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Image": DiskImageDetailTypeDef,
        "Volume": VolumeDetailTypeDef,
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
ImportInstanceVolumeDetailItemTypeDef = TypedDict(
    "ImportInstanceVolumeDetailItemTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "BytesConverted": NotRequired[int],
        "Description": NotRequired[str],
        "Image": NotRequired[DiskImageDescriptionTypeDef],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "Volume": NotRequired[DiskImageVolumeDescriptionTypeDef],
    },
)
ImportVolumeTaskDetailsTypeDef = TypedDict(
    "ImportVolumeTaskDetailsTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "BytesConverted": NotRequired[int],
        "Description": NotRequired[str],
        "Image": NotRequired[DiskImageDescriptionTypeDef],
        "Volume": NotRequired[DiskImageVolumeDescriptionTypeDef],
    },
)
InstanceStorageInfoTypeDef = TypedDict(
    "InstanceStorageInfoTypeDef",
    {
        "TotalSizeInGB": NotRequired[int],
        "Disks": NotRequired[List[DiskInfoTypeDef]],
        "NvmeSupport": NotRequired[EphemeralNvmeSupportType],
        "EncryptionSupport": NotRequired[InstanceStorageEncryptionSupportType],
    },
)
VpcEndpointConnectionTypeDef = TypedDict(
    "VpcEndpointConnectionTypeDef",
    {
        "ServiceId": NotRequired[str],
        "VpcEndpointId": NotRequired[str],
        "VpcEndpointOwner": NotRequired[str],
        "VpcEndpointState": NotRequired[StateType],
        "CreationTimestamp": NotRequired[datetime],
        "DnsEntries": NotRequired[List[DnsEntryTypeDef]],
        "NetworkLoadBalancerArns": NotRequired[List[str]],
        "GatewayLoadBalancerArns": NotRequired[List[str]],
        "IpAddressType": NotRequired[IpAddressTypeType],
        "VpcEndpointConnectionId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ModifyClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "ModifyClientVpnEndpointRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "ServerCertificateArn": NotRequired[str],
        "ConnectionLogOptions": NotRequired[ConnectionLogOptionsTypeDef],
        "DnsServers": NotRequired[DnsServersOptionsModifyStructureTypeDef],
        "VpnPort": NotRequired[int],
        "Description": NotRequired[str],
        "SplitTunnel": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
        "SelfServicePortal": NotRequired[SelfServicePortalType],
        "ClientConnectOptions": NotRequired[ClientConnectOptionsTypeDef],
        "SessionTimeoutHours": NotRequired[int],
        "ClientLoginBannerOptions": NotRequired[ClientLoginBannerOptionsTypeDef],
    },
)
EbsInfoTypeDef = TypedDict(
    "EbsInfoTypeDef",
    {
        "EbsOptimizedSupport": NotRequired[EbsOptimizedSupportType],
        "EncryptionSupport": NotRequired[EbsEncryptionSupportType],
        "EbsOptimizedInfo": NotRequired[EbsOptimizedInfoTypeDef],
        "NvmeSupport": NotRequired[EbsNvmeSupportType],
    },
)
InstanceBlockDeviceMappingSpecificationTypeDef = TypedDict(
    "InstanceBlockDeviceMappingSpecificationTypeDef",
    {
        "DeviceName": NotRequired[str],
        "Ebs": NotRequired[EbsInstanceBlockDeviceSpecificationTypeDef],
        "NoDevice": NotRequired[str],
        "VirtualName": NotRequired[str],
    },
)
InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "DeviceName": NotRequired[str],
        "Ebs": NotRequired[EbsInstanceBlockDeviceTypeDef],
    },
)
EgressOnlyInternetGatewayTypeDef = TypedDict(
    "EgressOnlyInternetGatewayTypeDef",
    {
        "Attachments": NotRequired[List[InternetGatewayAttachmentTypeDef]],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
InternetGatewayTypeDef = TypedDict(
    "InternetGatewayTypeDef",
    {
        "Attachments": NotRequired[List[InternetGatewayAttachmentTypeDef]],
        "InternetGatewayId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ElasticGpusTypeDef = TypedDict(
    "ElasticGpusTypeDef",
    {
        "ElasticGpuId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "ElasticGpuType": NotRequired[str],
        "ElasticGpuHealth": NotRequired[ElasticGpuHealthTypeDef],
        "ElasticGpuState": NotRequired[Literal["ATTACHED"]],
        "InstanceId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
EnaSrdSpecificationRequestTypeDef = TypedDict(
    "EnaSrdSpecificationRequestTypeDef",
    {
        "EnaSrdEnabled": NotRequired[bool],
        "EnaSrdUdpSpecification": NotRequired[EnaSrdUdpSpecificationRequestTypeDef],
    },
)
EnaSrdSpecificationTypeDef = TypedDict(
    "EnaSrdSpecificationTypeDef",
    {
        "EnaSrdEnabled": NotRequired[bool],
        "EnaSrdUdpSpecification": NotRequired[EnaSrdUdpSpecificationTypeDef],
    },
)
EnableFastLaunchRequestRequestTypeDef = TypedDict(
    "EnableFastLaunchRequestRequestTypeDef",
    {
        "ImageId": str,
        "ResourceType": NotRequired[str],
        "SnapshotConfiguration": NotRequired[FastLaunchSnapshotConfigurationRequestTypeDef],
        "LaunchTemplate": NotRequired[FastLaunchLaunchTemplateSpecificationRequestTypeDef],
        "MaxParallelLaunches": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
EnableFastSnapshotRestoreStateErrorItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreStateErrorItemTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Error": NotRequired[EnableFastSnapshotRestoreStateErrorTypeDef],
    },
)
HistoryRecordEntryTypeDef = TypedDict(
    "HistoryRecordEntryTypeDef",
    {
        "EventInformation": NotRequired[EventInformationTypeDef],
        "EventType": NotRequired[FleetEventTypeType],
        "Timestamp": NotRequired[datetime],
    },
)
HistoryRecordTypeDef = TypedDict(
    "HistoryRecordTypeDef",
    {
        "EventInformation": NotRequired[EventInformationTypeDef],
        "EventType": NotRequired[EventTypeType],
        "Timestamp": NotRequired[datetime],
    },
)
ExportImageResultTypeDef = TypedDict(
    "ExportImageResultTypeDef",
    {
        "Description": str,
        "DiskImageFormat": DiskImageFormatType,
        "ExportImageTaskId": str,
        "ImageId": str,
        "RoleName": str,
        "Progress": str,
        "S3ExportLocation": ExportTaskS3LocationTypeDef,
        "Status": str,
        "StatusMessage": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportImageTaskTypeDef = TypedDict(
    "ExportImageTaskTypeDef",
    {
        "Description": NotRequired[str],
        "ExportImageTaskId": NotRequired[str],
        "ImageId": NotRequired[str],
        "Progress": NotRequired[str],
        "S3ExportLocation": NotRequired[ExportTaskS3LocationTypeDef],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "Description": NotRequired[str],
        "ExportTaskId": NotRequired[str],
        "ExportToS3Task": NotRequired[ExportToS3TaskTypeDef],
        "InstanceExportDetails": NotRequired[InstanceExportDetailsTypeDef],
        "State": NotRequired[ExportTaskStateType],
        "StatusMessage": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
PathFilterTypeDef = TypedDict(
    "PathFilterTypeDef",
    {
        "SourceAddress": NotRequired[str],
        "SourcePortRange": NotRequired[FilterPortRangeTypeDef],
        "DestinationAddress": NotRequired[str],
        "DestinationPortRange": NotRequired[FilterPortRangeTypeDef],
    },
)
FleetSpotMaintenanceStrategiesRequestTypeDef = TypedDict(
    "FleetSpotMaintenanceStrategiesRequestTypeDef",
    {
        "CapacityRebalance": NotRequired[FleetSpotCapacityRebalanceRequestTypeDef],
    },
)
FleetSpotMaintenanceStrategiesTypeDef = TypedDict(
    "FleetSpotMaintenanceStrategiesTypeDef",
    {
        "CapacityRebalance": NotRequired[FleetSpotCapacityRebalanceTypeDef],
    },
)
FpgaDeviceInfoTypeDef = TypedDict(
    "FpgaDeviceInfoTypeDef",
    {
        "Name": NotRequired[str],
        "Manufacturer": NotRequired[str],
        "Count": NotRequired[int],
        "MemoryInfo": NotRequired[FpgaDeviceMemoryInfoTypeDef],
    },
)
FpgaImageAttributeTypeDef = TypedDict(
    "FpgaImageAttributeTypeDef",
    {
        "FpgaImageId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LoadPermissions": NotRequired[List[LoadPermissionTypeDef]],
        "ProductCodes": NotRequired[List[ProductCodeTypeDef]],
    },
)
FpgaImageTypeDef = TypedDict(
    "FpgaImageTypeDef",
    {
        "FpgaImageId": NotRequired[str],
        "FpgaImageGlobalId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ShellVersion": NotRequired[str],
        "PciId": NotRequired[PciIdTypeDef],
        "State": NotRequired[FpgaImageStateTypeDef],
        "CreateTime": NotRequired[datetime],
        "UpdateTime": NotRequired[datetime],
        "OwnerId": NotRequired[str],
        "OwnerAlias": NotRequired[str],
        "ProductCodes": NotRequired[List[ProductCodeTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "Public": NotRequired[bool],
        "DataRetentionSupport": NotRequired[bool],
        "InstanceTypes": NotRequired[List[str]],
    },
)
GetAssociatedIpv6PoolCidrsResultTypeDef = TypedDict(
    "GetAssociatedIpv6PoolCidrsResultTypeDef",
    {
        "Ipv6CidrAssociations": List[Ipv6CidrAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCapacityReservationUsageResultTypeDef = TypedDict(
    "GetCapacityReservationUsageResultTypeDef",
    {
        "NextToken": str,
        "CapacityReservationId": str,
        "InstanceType": str,
        "TotalInstanceCount": int,
        "AvailableInstanceCount": int,
        "State": CapacityReservationStateType,
        "InstanceUsages": List[InstanceUsageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDefaultCreditSpecificationResultTypeDef = TypedDict(
    "GetDefaultCreditSpecificationResultTypeDef",
    {
        "InstanceFamilyCreditSpecification": InstanceFamilyCreditSpecificationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDefaultCreditSpecificationResultTypeDef = TypedDict(
    "ModifyDefaultCreditSpecificationResultTypeDef",
    {
        "InstanceFamilyCreditSpecification": InstanceFamilyCreditSpecificationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHostReservationPurchasePreviewResultTypeDef = TypedDict(
    "GetHostReservationPurchasePreviewResultTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Purchase": List[PurchaseTypeDef],
        "TotalHourlyPrice": str,
        "TotalUpfrontPrice": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PurchaseHostReservationResultTypeDef = TypedDict(
    "PurchaseHostReservationResultTypeDef",
    {
        "ClientToken": str,
        "CurrencyCode": Literal["USD"],
        "Purchase": List[PurchaseTypeDef],
        "TotalHourlyPrice": str,
        "TotalUpfrontPrice": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstanceTypesFromInstanceRequirementsResultTypeDef = TypedDict(
    "GetInstanceTypesFromInstanceRequirementsResultTypeDef",
    {
        "InstanceTypes": List[InstanceTypeInfoFromInstanceRequirementsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIpamAddressHistoryResultTypeDef = TypedDict(
    "GetIpamAddressHistoryResultTypeDef",
    {
        "HistoryRecords": List[IpamAddressHistoryRecordTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetManagedPrefixListAssociationsResultTypeDef = TypedDict(
    "GetManagedPrefixListAssociationsResultTypeDef",
    {
        "PrefixListAssociations": List[PrefixListAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetManagedPrefixListEntriesResultTypeDef = TypedDict(
    "GetManagedPrefixListEntriesResultTypeDef",
    {
        "Entries": List[PrefixListEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReservedInstanceReservationValueTypeDef = TypedDict(
    "ReservedInstanceReservationValueTypeDef",
    {
        "ReservationValue": NotRequired[ReservationValueTypeDef],
        "ReservedInstanceId": NotRequired[str],
    },
)
GetSpotPlacementScoresResultTypeDef = TypedDict(
    "GetSpotPlacementScoresResultTypeDef",
    {
        "SpotPlacementScores": List[SpotPlacementScoreTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransitGatewayAttachmentPropagationsResultTypeDef = TypedDict(
    "GetTransitGatewayAttachmentPropagationsResultTypeDef",
    {
        "TransitGatewayAttachmentPropagations": List[TransitGatewayAttachmentPropagationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransitGatewayRouteTableAssociationsResultTypeDef = TypedDict(
    "GetTransitGatewayRouteTableAssociationsResultTypeDef",
    {
        "Associations": List[TransitGatewayRouteTableAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransitGatewayRouteTablePropagationsResultTypeDef = TypedDict(
    "GetTransitGatewayRouteTablePropagationsResultTypeDef",
    {
        "TransitGatewayRouteTablePropagations": List[TransitGatewayRouteTablePropagationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVpnConnectionDeviceTypesResultTypeDef = TypedDict(
    "GetVpnConnectionDeviceTypesResultTypeDef",
    {
        "VpnConnectionDeviceTypes": List[VpnConnectionDeviceTypeTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVpnTunnelReplacementStatusResultTypeDef = TypedDict(
    "GetVpnTunnelReplacementStatusResultTypeDef",
    {
        "VpnConnectionId": str,
        "TransitGatewayId": str,
        "CustomerGatewayId": str,
        "VpnGatewayId": str,
        "VpnTunnelOutsideIpAddress": str,
        "MaintenanceDetails": MaintenanceDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GpuDeviceInfoTypeDef = TypedDict(
    "GpuDeviceInfoTypeDef",
    {
        "Name": NotRequired[str],
        "Manufacturer": NotRequired[str],
        "Count": NotRequired[int],
        "MemoryInfo": NotRequired[GpuDeviceMemoryInfoTypeDef],
    },
)
IamInstanceProfileAssociationTypeDef = TypedDict(
    "IamInstanceProfileAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "IamInstanceProfile": NotRequired[IamInstanceProfileTypeDef],
        "State": NotRequired[IamInstanceProfileAssociationStateType],
        "Timestamp": NotRequired[datetime],
    },
)
LaunchPermissionModificationsTypeDef = TypedDict(
    "LaunchPermissionModificationsTypeDef",
    {
        "Add": NotRequired[Sequence[LaunchPermissionTypeDef]],
        "Remove": NotRequired[Sequence[LaunchPermissionTypeDef]],
    },
)
ImageDiskContainerTypeDef = TypedDict(
    "ImageDiskContainerTypeDef",
    {
        "Description": NotRequired[str],
        "DeviceName": NotRequired[str],
        "Format": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Url": NotRequired[str],
        "UserBucket": NotRequired[UserBucketTypeDef],
    },
)
SnapshotDiskContainerTypeDef = TypedDict(
    "SnapshotDiskContainerTypeDef",
    {
        "Description": NotRequired[str],
        "Format": NotRequired[str],
        "Url": NotRequired[str],
        "UserBucket": NotRequired[UserBucketTypeDef],
    },
)
ListImagesInRecycleBinResultTypeDef = TypedDict(
    "ListImagesInRecycleBinResultTypeDef",
    {
        "Images": List[ImageRecycleBinInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportInstanceLaunchSpecificationTypeDef = TypedDict(
    "ImportInstanceLaunchSpecificationTypeDef",
    {
        "AdditionalInfo": NotRequired[str],
        "Architecture": NotRequired[ArchitectureValuesType],
        "GroupIds": NotRequired[Sequence[str]],
        "GroupNames": NotRequired[Sequence[str]],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "InstanceType": NotRequired[InstanceTypeType],
        "Monitoring": NotRequired[bool],
        "Placement": NotRequired[PlacementTypeDef],
        "PrivateIpAddress": NotRequired[str],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired[UserDataTypeDef],
    },
)
InferenceDeviceInfoTypeDef = TypedDict(
    "InferenceDeviceInfoTypeDef",
    {
        "Count": NotRequired[int],
        "Name": NotRequired[str],
        "Manufacturer": NotRequired[str],
        "MemoryInfo": NotRequired[InferenceDeviceMemoryInfoTypeDef],
    },
)
InstanceAttachmentEnaSrdSpecificationTypeDef = TypedDict(
    "InstanceAttachmentEnaSrdSpecificationTypeDef",
    {
        "EnaSrdEnabled": NotRequired[bool],
        "EnaSrdUdpSpecification": NotRequired[InstanceAttachmentEnaSrdUdpSpecificationTypeDef],
    },
)
ModifyInstanceCreditSpecificationRequestRequestTypeDef = TypedDict(
    "ModifyInstanceCreditSpecificationRequestRequestTypeDef",
    {
        "InstanceCreditSpecifications": Sequence[InstanceCreditSpecificationRequestTypeDef],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)
ModifyInstanceMetadataOptionsResultTypeDef = TypedDict(
    "ModifyInstanceMetadataOptionsResultTypeDef",
    {
        "InstanceId": str,
        "InstanceMetadataOptions": InstanceMetadataOptionsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceMonitoringTypeDef = TypedDict(
    "InstanceMonitoringTypeDef",
    {
        "InstanceId": NotRequired[str],
        "Monitoring": NotRequired[MonitoringTypeDef],
    },
)
InstancePrivateIpAddressTypeDef = TypedDict(
    "InstancePrivateIpAddressTypeDef",
    {
        "Association": NotRequired[InstanceNetworkInterfaceAssociationTypeDef],
        "Primary": NotRequired[bool],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)
InstanceRequirementsRequestTypeDef = TypedDict(
    "InstanceRequirementsRequestTypeDef",
    {
        "VCpuCount": VCpuCountRangeRequestTypeDef,
        "MemoryMiB": MemoryMiBRequestTypeDef,
        "CpuManufacturers": NotRequired[Sequence[CpuManufacturerType]],
        "MemoryGiBPerVCpu": NotRequired[MemoryGiBPerVCpuRequestTypeDef],
        "ExcludedInstanceTypes": NotRequired[Sequence[str]],
        "InstanceGenerations": NotRequired[Sequence[InstanceGenerationType]],
        "SpotMaxPricePercentageOverLowestPrice": NotRequired[int],
        "OnDemandMaxPricePercentageOverLowestPrice": NotRequired[int],
        "BareMetal": NotRequired[BareMetalType],
        "BurstablePerformance": NotRequired[BurstablePerformanceType],
        "RequireHibernateSupport": NotRequired[bool],
        "NetworkInterfaceCount": NotRequired[NetworkInterfaceCountRequestTypeDef],
        "LocalStorage": NotRequired[LocalStorageType],
        "LocalStorageTypes": NotRequired[Sequence[LocalStorageTypeType]],
        "TotalLocalStorageGB": NotRequired[TotalLocalStorageGBRequestTypeDef],
        "BaselineEbsBandwidthMbps": NotRequired[BaselineEbsBandwidthMbpsRequestTypeDef],
        "AcceleratorTypes": NotRequired[Sequence[AcceleratorTypeType]],
        "AcceleratorCount": NotRequired[AcceleratorCountRequestTypeDef],
        "AcceleratorManufacturers": NotRequired[Sequence[AcceleratorManufacturerType]],
        "AcceleratorNames": NotRequired[Sequence[AcceleratorNameType]],
        "AcceleratorTotalMemoryMiB": NotRequired[AcceleratorTotalMemoryMiBRequestTypeDef],
        "NetworkBandwidthGbps": NotRequired[NetworkBandwidthGbpsRequestTypeDef],
        "AllowedInstanceTypes": NotRequired[Sequence[str]],
    },
)
InstanceRequirementsTypeDef = TypedDict(
    "InstanceRequirementsTypeDef",
    {
        "VCpuCount": NotRequired[VCpuCountRangeTypeDef],
        "MemoryMiB": NotRequired[MemoryMiBTypeDef],
        "CpuManufacturers": NotRequired[List[CpuManufacturerType]],
        "MemoryGiBPerVCpu": NotRequired[MemoryGiBPerVCpuTypeDef],
        "ExcludedInstanceTypes": NotRequired[List[str]],
        "InstanceGenerations": NotRequired[List[InstanceGenerationType]],
        "SpotMaxPricePercentageOverLowestPrice": NotRequired[int],
        "OnDemandMaxPricePercentageOverLowestPrice": NotRequired[int],
        "BareMetal": NotRequired[BareMetalType],
        "BurstablePerformance": NotRequired[BurstablePerformanceType],
        "RequireHibernateSupport": NotRequired[bool],
        "NetworkInterfaceCount": NotRequired[NetworkInterfaceCountTypeDef],
        "LocalStorage": NotRequired[LocalStorageType],
        "LocalStorageTypes": NotRequired[List[LocalStorageTypeType]],
        "TotalLocalStorageGB": NotRequired[TotalLocalStorageGBTypeDef],
        "BaselineEbsBandwidthMbps": NotRequired[BaselineEbsBandwidthMbpsTypeDef],
        "AcceleratorTypes": NotRequired[List[AcceleratorTypeType]],
        "AcceleratorCount": NotRequired[AcceleratorCountTypeDef],
        "AcceleratorManufacturers": NotRequired[List[AcceleratorManufacturerType]],
        "AcceleratorNames": NotRequired[List[AcceleratorNameType]],
        "AcceleratorTotalMemoryMiB": NotRequired[AcceleratorTotalMemoryMiBTypeDef],
        "NetworkBandwidthGbps": NotRequired[NetworkBandwidthGbpsTypeDef],
        "AllowedInstanceTypes": NotRequired[List[str]],
    },
)
InstanceStateChangeTypeDef = TypedDict(
    "InstanceStateChangeTypeDef",
    {
        "CurrentState": NotRequired[InstanceStateTypeDef],
        "InstanceId": NotRequired[str],
        "PreviousState": NotRequired[InstanceStateTypeDef],
    },
)
InstanceStatusSummaryTypeDef = TypedDict(
    "InstanceStatusSummaryTypeDef",
    {
        "Details": NotRequired[List[InstanceStatusDetailsTypeDef]],
        "Status": NotRequired[SummaryStatusType],
    },
)
ModifyInstanceEventStartTimeResultTypeDef = TypedDict(
    "ModifyInstanceEventStartTimeResultTypeDef",
    {
        "Event": InstanceStatusEventTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IpPermissionPaginatorTypeDef = TypedDict(
    "IpPermissionPaginatorTypeDef",
    {
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "IpRanges": NotRequired[List[IpRangeTypeDef]],
        "Ipv6Ranges": NotRequired[List[Ipv6RangeTypeDef]],
        "PrefixListIds": NotRequired[List[PrefixListIdTypeDef]],
        "ToPort": NotRequired[int],
        "UserIdGroupPairs": NotRequired[List[UserIdGroupPairTypeDef]],
    },
)
IpPermissionTypeDef = TypedDict(
    "IpPermissionTypeDef",
    {
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "IpRanges": NotRequired[Sequence[IpRangeTypeDef]],
        "Ipv6Ranges": NotRequired[Sequence[Ipv6RangeTypeDef]],
        "PrefixListIds": NotRequired[Sequence[PrefixListIdTypeDef]],
        "ToPort": NotRequired[int],
        "UserIdGroupPairs": NotRequired[Sequence[UserIdGroupPairTypeDef]],
    },
)
StaleIpPermissionTypeDef = TypedDict(
    "StaleIpPermissionTypeDef",
    {
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "IpRanges": NotRequired[List[str]],
        "PrefixListIds": NotRequired[List[str]],
        "ToPort": NotRequired[int],
        "UserIdGroupPairs": NotRequired[List[UserIdGroupPairTypeDef]],
    },
)
ProvisionIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "ProvisionIpamPoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "DryRun": NotRequired[bool],
        "Cidr": NotRequired[str],
        "CidrAuthorizationContext": NotRequired[IpamCidrAuthorizationContextTypeDef],
        "NetmaskLength": NotRequired[int],
        "ClientToken": NotRequired[str],
    },
)
IpamDiscoveredAccountTypeDef = TypedDict(
    "IpamDiscoveredAccountTypeDef",
    {
        "AccountId": NotRequired[str],
        "DiscoveryRegion": NotRequired[str],
        "FailureReason": NotRequired[IpamDiscoveryFailureReasonTypeDef],
        "LastAttemptedDiscoveryTime": NotRequired[datetime],
        "LastSuccessfulDiscoveryTime": NotRequired[datetime],
    },
)
IpamDiscoveredResourceCidrTypeDef = TypedDict(
    "IpamDiscoveredResourceCidrTypeDef",
    {
        "IpamResourceDiscoveryId": NotRequired[str],
        "ResourceRegion": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceOwnerId": NotRequired[str],
        "ResourceCidr": NotRequired[str],
        "ResourceType": NotRequired[IpamResourceTypeType],
        "ResourceTags": NotRequired[List[IpamResourceTagTypeDef]],
        "IpUsage": NotRequired[float],
        "VpcId": NotRequired[str],
        "SampleTime": NotRequired[datetime],
    },
)
IpamResourceCidrTypeDef = TypedDict(
    "IpamResourceCidrTypeDef",
    {
        "IpamId": NotRequired[str],
        "IpamScopeId": NotRequired[str],
        "IpamPoolId": NotRequired[str],
        "ResourceRegion": NotRequired[str],
        "ResourceOwnerId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceName": NotRequired[str],
        "ResourceCidr": NotRequired[str],
        "ResourceType": NotRequired[IpamResourceTypeType],
        "ResourceTags": NotRequired[List[IpamResourceTagTypeDef]],
        "IpUsage": NotRequired[float],
        "ComplianceStatus": NotRequired[IpamComplianceStatusType],
        "ManagementState": NotRequired[IpamManagementStateType],
        "OverlapStatus": NotRequired[IpamOverlapStatusType],
        "VpcId": NotRequired[str],
    },
)
IpamResourceDiscoveryTypeDef = TypedDict(
    "IpamResourceDiscoveryTypeDef",
    {
        "OwnerId": NotRequired[str],
        "IpamResourceDiscoveryId": NotRequired[str],
        "IpamResourceDiscoveryArn": NotRequired[str],
        "IpamResourceDiscoveryRegion": NotRequired[str],
        "Description": NotRequired[str],
        "OperatingRegions": NotRequired[List[IpamOperatingRegionTypeDef]],
        "IsDefault": NotRequired[bool],
        "State": NotRequired[IpamResourceDiscoveryStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
IpamTypeDef = TypedDict(
    "IpamTypeDef",
    {
        "OwnerId": NotRequired[str],
        "IpamId": NotRequired[str],
        "IpamArn": NotRequired[str],
        "IpamRegion": NotRequired[str],
        "PublicDefaultScopeId": NotRequired[str],
        "PrivateDefaultScopeId": NotRequired[str],
        "ScopeCount": NotRequired[int],
        "Description": NotRequired[str],
        "OperatingRegions": NotRequired[List[IpamOperatingRegionTypeDef]],
        "State": NotRequired[IpamStateType],
        "Tags": NotRequired[List[TagTypeDef]],
        "DefaultResourceDiscoveryId": NotRequired[str],
        "DefaultResourceDiscoveryAssociationId": NotRequired[str],
        "ResourceDiscoveryAssociationCount": NotRequired[int],
        "StateMessage": NotRequired[str],
        "Tier": NotRequired[IpamTierType],
    },
)
IpamPoolCidrTypeDef = TypedDict(
    "IpamPoolCidrTypeDef",
    {
        "Cidr": NotRequired[str],
        "State": NotRequired[IpamPoolCidrStateType],
        "FailureReason": NotRequired[IpamPoolCidrFailureReasonTypeDef],
        "IpamPoolCidrId": NotRequired[str],
        "NetmaskLength": NotRequired[int],
    },
)
IpamPoolTypeDef = TypedDict(
    "IpamPoolTypeDef",
    {
        "OwnerId": NotRequired[str],
        "IpamPoolId": NotRequired[str],
        "SourceIpamPoolId": NotRequired[str],
        "IpamPoolArn": NotRequired[str],
        "IpamScopeArn": NotRequired[str],
        "IpamScopeType": NotRequired[IpamScopeTypeType],
        "IpamArn": NotRequired[str],
        "IpamRegion": NotRequired[str],
        "Locale": NotRequired[str],
        "PoolDepth": NotRequired[int],
        "State": NotRequired[IpamPoolStateType],
        "StateMessage": NotRequired[str],
        "Description": NotRequired[str],
        "AutoImport": NotRequired[bool],
        "PubliclyAdvertisable": NotRequired[bool],
        "AddressFamily": NotRequired[AddressFamilyType],
        "AllocationMinNetmaskLength": NotRequired[int],
        "AllocationMaxNetmaskLength": NotRequired[int],
        "AllocationDefaultNetmaskLength": NotRequired[int],
        "AllocationResourceTags": NotRequired[List[IpamResourceTagTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "AwsService": NotRequired[Literal["ec2"]],
        "PublicIpSource": NotRequired[IpamPoolPublicIpSourceType],
        "SourceResource": NotRequired[IpamPoolSourceResourceTypeDef],
    },
)
IpamPublicAddressTagsTypeDef = TypedDict(
    "IpamPublicAddressTagsTypeDef",
    {
        "EipTags": NotRequired[List[IpamPublicAddressTagTypeDef]],
    },
)
Ipv6PoolTypeDef = TypedDict(
    "Ipv6PoolTypeDef",
    {
        "PoolId": NotRequired[str],
        "Description": NotRequired[str],
        "PoolCidrBlocks": NotRequired[List[PoolCidrBlockTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
LaunchTemplateBlockDeviceMappingRequestTypeDef = TypedDict(
    "LaunchTemplateBlockDeviceMappingRequestTypeDef",
    {
        "DeviceName": NotRequired[str],
        "VirtualName": NotRequired[str],
        "Ebs": NotRequired[LaunchTemplateEbsBlockDeviceRequestTypeDef],
        "NoDevice": NotRequired[str],
    },
)
LaunchTemplateBlockDeviceMappingTypeDef = TypedDict(
    "LaunchTemplateBlockDeviceMappingTypeDef",
    {
        "DeviceName": NotRequired[str],
        "VirtualName": NotRequired[str],
        "Ebs": NotRequired[LaunchTemplateEbsBlockDeviceTypeDef],
        "NoDevice": NotRequired[str],
    },
)
LaunchTemplateEnaSrdSpecificationTypeDef = TypedDict(
    "LaunchTemplateEnaSrdSpecificationTypeDef",
    {
        "EnaSrdEnabled": NotRequired[bool],
        "EnaSrdUdpSpecification": NotRequired[LaunchTemplateEnaSrdUdpSpecificationTypeDef],
    },
)
LaunchTemplateInstanceMarketOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMarketOptionsTypeDef",
    {
        "MarketType": NotRequired[MarketTypeType],
        "SpotOptions": NotRequired[LaunchTemplateSpotMarketOptionsTypeDef],
    },
)
ListSnapshotsInRecycleBinResultTypeDef = TypedDict(
    "ListSnapshotsInRecycleBinResultTypeDef",
    {
        "Snapshots": List[SnapshotRecycleBinInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoadPermissionModificationsTypeDef = TypedDict(
    "LoadPermissionModificationsTypeDef",
    {
        "Add": NotRequired[Sequence[LoadPermissionRequestTypeDef]],
        "Remove": NotRequired[Sequence[LoadPermissionRequestTypeDef]],
    },
)
ModifyIpamRequestRequestTypeDef = TypedDict(
    "ModifyIpamRequestRequestTypeDef",
    {
        "IpamId": str,
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "AddOperatingRegions": NotRequired[Sequence[AddIpamOperatingRegionTypeDef]],
        "RemoveOperatingRegions": NotRequired[Sequence[RemoveIpamOperatingRegionTypeDef]],
        "Tier": NotRequired[IpamTierType],
    },
)
ModifyIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "ModifyIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "IpamResourceDiscoveryId": str,
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "AddOperatingRegions": NotRequired[Sequence[AddIpamOperatingRegionTypeDef]],
        "RemoveOperatingRegions": NotRequired[Sequence[RemoveIpamOperatingRegionTypeDef]],
    },
)
ModifyManagedPrefixListRequestRequestTypeDef = TypedDict(
    "ModifyManagedPrefixListRequestRequestTypeDef",
    {
        "PrefixListId": str,
        "DryRun": NotRequired[bool],
        "CurrentVersion": NotRequired[int],
        "PrefixListName": NotRequired[str],
        "AddEntries": NotRequired[Sequence[AddPrefixListEntryTypeDef]],
        "RemoveEntries": NotRequired[Sequence[RemovePrefixListEntryTypeDef]],
        "MaxEntries": NotRequired[int],
    },
)
ModifyReservedInstancesRequestRequestTypeDef = TypedDict(
    "ModifyReservedInstancesRequestRequestTypeDef",
    {
        "ReservedInstancesIds": Sequence[str],
        "TargetConfigurations": Sequence[ReservedInstancesConfigurationTypeDef],
        "ClientToken": NotRequired[str],
    },
)
ReservedInstancesModificationResultTypeDef = TypedDict(
    "ReservedInstancesModificationResultTypeDef",
    {
        "ReservedInstancesId": NotRequired[str],
        "TargetConfiguration": NotRequired[ReservedInstancesConfigurationTypeDef],
    },
)
ModifyTransitGatewayRequestRequestTypeDef = TypedDict(
    "ModifyTransitGatewayRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "Description": NotRequired[str],
        "Options": NotRequired[ModifyTransitGatewayOptionsTypeDef],
        "DryRun": NotRequired[bool],
    },
)
ModifyTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "AddSubnetIds": NotRequired[Sequence[str]],
        "RemoveSubnetIds": NotRequired[Sequence[str]],
        "Options": NotRequired[ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef],
        "DryRun": NotRequired[bool],
    },
)
ModifyVerifiedAccessEndpointRequestRequestTypeDef = TypedDict(
    "ModifyVerifiedAccessEndpointRequestRequestTypeDef",
    {
        "VerifiedAccessEndpointId": str,
        "VerifiedAccessGroupId": NotRequired[str],
        "LoadBalancerOptions": NotRequired[ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef],
        "NetworkInterfaceOptions": NotRequired[ModifyVerifiedAccessEndpointEniOptionsTypeDef],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
ModifyVerifiedAccessEndpointPolicyResultTypeDef = TypedDict(
    "ModifyVerifiedAccessEndpointPolicyResultTypeDef",
    {
        "PolicyEnabled": bool,
        "PolicyDocument": str,
        "SseSpecification": VerifiedAccessSseSpecificationResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVerifiedAccessGroupPolicyResultTypeDef = TypedDict(
    "ModifyVerifiedAccessGroupPolicyResultTypeDef",
    {
        "PolicyEnabled": bool,
        "PolicyDocument": str,
        "SseSpecification": VerifiedAccessSseSpecificationResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifiedAccessGroupTypeDef = TypedDict(
    "VerifiedAccessGroupTypeDef",
    {
        "VerifiedAccessGroupId": NotRequired[str],
        "VerifiedAccessInstanceId": NotRequired[str],
        "Description": NotRequired[str],
        "Owner": NotRequired[str],
        "VerifiedAccessGroupArn": NotRequired[str],
        "CreationTime": NotRequired[str],
        "LastUpdatedTime": NotRequired[str],
        "DeletionTime": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "SseSpecification": NotRequired[VerifiedAccessSseSpecificationResponseTypeDef],
    },
)
ModifyVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "ModifyVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "VerifiedAccessTrustProviderId": str,
        "OidcOptions": NotRequired[ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef],
        "DeviceOptions": NotRequired[ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "SseSpecification": NotRequired[VerifiedAccessSseSpecificationRequestTypeDef],
    },
)
ModifyVpcPeeringConnectionOptionsRequestRequestTypeDef = TypedDict(
    "ModifyVpcPeeringConnectionOptionsRequestRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
        "AccepterPeeringConnectionOptions": NotRequired[PeeringConnectionOptionsRequestTypeDef],
        "DryRun": NotRequired[bool],
        "RequesterPeeringConnectionOptions": NotRequired[PeeringConnectionOptionsRequestTypeDef],
    },
)
ModifyVpcPeeringConnectionOptionsResultTypeDef = TypedDict(
    "ModifyVpcPeeringConnectionOptionsResultTypeDef",
    {
        "AccepterPeeringConnectionOptions": PeeringConnectionOptionsTypeDef,
        "RequesterPeeringConnectionOptions": PeeringConnectionOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NatGatewayTypeDef = TypedDict(
    "NatGatewayTypeDef",
    {
        "CreateTime": NotRequired[datetime],
        "DeleteTime": NotRequired[datetime],
        "FailureCode": NotRequired[str],
        "FailureMessage": NotRequired[str],
        "NatGatewayAddresses": NotRequired[List[NatGatewayAddressTypeDef]],
        "NatGatewayId": NotRequired[str],
        "ProvisionedBandwidth": NotRequired[ProvisionedBandwidthTypeDef],
        "State": NotRequired[NatGatewayStateType],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "ConnectivityType": NotRequired[ConnectivityTypeType],
    },
)
NetworkInfoTypeDef = TypedDict(
    "NetworkInfoTypeDef",
    {
        "NetworkPerformance": NotRequired[str],
        "MaximumNetworkInterfaces": NotRequired[int],
        "MaximumNetworkCards": NotRequired[int],
        "DefaultNetworkCardIndex": NotRequired[int],
        "NetworkCards": NotRequired[List[NetworkCardInfoTypeDef]],
        "Ipv4AddressesPerInterface": NotRequired[int],
        "Ipv6AddressesPerInterface": NotRequired[int],
        "Ipv6Supported": NotRequired[bool],
        "EnaSupport": NotRequired[EnaSupportType],
        "EfaSupported": NotRequired[bool],
        "EfaInfo": NotRequired[EfaInfoTypeDef],
        "EncryptionInTransitSupported": NotRequired[bool],
        "EnaSrdSupported": NotRequired[bool],
    },
)
NetworkInterfacePrivateIpAddressTypeDef = TypedDict(
    "NetworkInterfacePrivateIpAddressTypeDef",
    {
        "Association": NotRequired[NetworkInterfaceAssociationTypeDef],
        "Primary": NotRequired[bool],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)
NetworkInterfacePermissionTypeDef = TypedDict(
    "NetworkInterfacePermissionTypeDef",
    {
        "NetworkInterfacePermissionId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "AwsAccountId": NotRequired[str],
        "AwsService": NotRequired[str],
        "Permission": NotRequired[InterfacePermissionTypeType],
        "PermissionState": NotRequired[NetworkInterfacePermissionStateTypeDef],
    },
)
VerifiedAccessTrustProviderTypeDef = TypedDict(
    "VerifiedAccessTrustProviderTypeDef",
    {
        "VerifiedAccessTrustProviderId": NotRequired[str],
        "Description": NotRequired[str],
        "TrustProviderType": NotRequired[TrustProviderTypeType],
        "UserTrustProviderType": NotRequired[UserTrustProviderTypeType],
        "DeviceTrustProviderType": NotRequired[DeviceTrustProviderTypeType],
        "OidcOptions": NotRequired[OidcOptionsTypeDef],
        "DeviceOptions": NotRequired[DeviceOptionsTypeDef],
        "PolicyReferenceName": NotRequired[str],
        "CreationTime": NotRequired[str],
        "LastUpdatedTime": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "SseSpecification": NotRequired[VerifiedAccessSseSpecificationResponseTypeDef],
    },
)
PathRequestFilterTypeDef = TypedDict(
    "PathRequestFilterTypeDef",
    {
        "SourceAddress": NotRequired[str],
        "SourcePortRange": NotRequired[RequestFilterPortRangeTypeDef],
        "DestinationAddress": NotRequired[str],
        "DestinationPortRange": NotRequired[RequestFilterPortRangeTypeDef],
    },
)
PathStatementRequestTypeDef = TypedDict(
    "PathStatementRequestTypeDef",
    {
        "PacketHeaderStatement": NotRequired[PacketHeaderStatementRequestTypeDef],
        "ResourceStatement": NotRequired[ResourceStatementRequestTypeDef],
    },
)
ThroughResourcesStatementRequestTypeDef = TypedDict(
    "ThroughResourcesStatementRequestTypeDef",
    {
        "ResourceStatement": NotRequired[ResourceStatementRequestTypeDef],
    },
)
PathStatementTypeDef = TypedDict(
    "PathStatementTypeDef",
    {
        "PacketHeaderStatement": NotRequired[PacketHeaderStatementTypeDef],
        "ResourceStatement": NotRequired[ResourceStatementTypeDef],
    },
)
ThroughResourcesStatementTypeDef = TypedDict(
    "ThroughResourcesStatementTypeDef",
    {
        "ResourceStatement": NotRequired[ResourceStatementTypeDef],
    },
)
ReservedInstancesListingTypeDef = TypedDict(
    "ReservedInstancesListingTypeDef",
    {
        "ClientToken": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "InstanceCounts": NotRequired[List[InstanceCountTypeDef]],
        "PriceSchedules": NotRequired[List[PriceScheduleTypeDef]],
        "ReservedInstancesId": NotRequired[str],
        "ReservedInstancesListingId": NotRequired[str],
        "Status": NotRequired[ListingStatusType],
        "StatusMessage": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "UpdateDate": NotRequired[datetime],
    },
)
ProvisionPublicIpv4PoolCidrResultTypeDef = TypedDict(
    "ProvisionPublicIpv4PoolCidrResultTypeDef",
    {
        "PoolId": str,
        "PoolAddressRange": PublicIpv4PoolRangeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PublicIpv4PoolTypeDef = TypedDict(
    "PublicIpv4PoolTypeDef",
    {
        "PoolId": NotRequired[str],
        "Description": NotRequired[str],
        "PoolAddressRanges": NotRequired[List[PublicIpv4PoolRangeTypeDef]],
        "TotalAddressCount": NotRequired[int],
        "TotalAvailableAddressCount": NotRequired[int],
        "NetworkBorderGroup": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
PurchaseScheduledInstancesRequestRequestTypeDef = TypedDict(
    "PurchaseScheduledInstancesRequestRequestTypeDef",
    {
        "PurchaseRequests": Sequence[PurchaseRequestTypeDef],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
PurchaseReservedInstancesOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseReservedInstancesOfferingRequestRequestTypeDef",
    {
        "InstanceCount": int,
        "ReservedInstancesOfferingId": str,
        "DryRun": NotRequired[bool],
        "LimitPrice": NotRequired[ReservedInstanceLimitPriceTypeDef],
        "PurchaseTime": NotRequired[TimestampTypeDef],
    },
)
ReservedInstancesOfferingTypeDef = TypedDict(
    "ReservedInstancesOfferingTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "InstanceType": NotRequired[InstanceTypeType],
        "ProductDescription": NotRequired[RIProductDescriptionType],
        "ReservedInstancesOfferingId": NotRequired[str],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[Literal["USD"]],
        "InstanceTenancy": NotRequired[TenancyType],
        "Marketplace": NotRequired[bool],
        "OfferingClass": NotRequired[OfferingClassTypeType],
        "OfferingType": NotRequired[OfferingTypeValuesType],
        "PricingDetails": NotRequired[List[PricingDetailTypeDef]],
        "RecurringCharges": NotRequired[List[RecurringChargeTypeDef]],
        "Scope": NotRequired[scopeType],
    },
)
ReservedInstancesTypeDef = TypedDict(
    "ReservedInstancesTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "Duration": NotRequired[int],
        "End": NotRequired[datetime],
        "FixedPrice": NotRequired[float],
        "InstanceCount": NotRequired[int],
        "InstanceType": NotRequired[InstanceTypeType],
        "ProductDescription": NotRequired[RIProductDescriptionType],
        "ReservedInstancesId": NotRequired[str],
        "Start": NotRequired[datetime],
        "State": NotRequired[ReservedInstanceStateType],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[Literal["USD"]],
        "InstanceTenancy": NotRequired[TenancyType],
        "OfferingClass": NotRequired[OfferingClassTypeType],
        "OfferingType": NotRequired[OfferingTypeValuesType],
        "RecurringCharges": NotRequired[List[RecurringChargeTypeDef]],
        "Scope": NotRequired[scopeType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
SecurityGroupRuleTypeDef = TypedDict(
    "SecurityGroupRuleTypeDef",
    {
        "SecurityGroupRuleId": NotRequired[str],
        "GroupId": NotRequired[str],
        "GroupOwnerId": NotRequired[str],
        "IsEgress": NotRequired[bool],
        "IpProtocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
        "CidrIpv4": NotRequired[str],
        "CidrIpv6": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "ReferencedGroupInfo": NotRequired[ReferencedSecurityGroupTypeDef],
        "Description": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
RegisterInstanceEventNotificationAttributesRequestRequestTypeDef = TypedDict(
    "RegisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    {
        "InstanceTagAttribute": RegisterInstanceTagAttributeRequestTypeDef,
        "DryRun": NotRequired[bool],
    },
)
RegisterTransitGatewayMulticastGroupMembersResultTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupMembersResultTypeDef",
    {
        "RegisteredMulticastGroupMembers": TransitGatewayMulticastRegisteredGroupMembersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterTransitGatewayMulticastGroupSourcesResultTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    {
        "RegisteredMulticastGroupSources": TransitGatewayMulticastRegisteredGroupSourcesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScheduledInstanceAvailabilityTypeDef = TypedDict(
    "ScheduledInstanceAvailabilityTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "AvailableInstanceCount": NotRequired[int],
        "FirstSlotStartTime": NotRequired[datetime],
        "HourlyPrice": NotRequired[str],
        "InstanceType": NotRequired[str],
        "MaxTermDurationInDays": NotRequired[int],
        "MinTermDurationInDays": NotRequired[int],
        "NetworkPlatform": NotRequired[str],
        "Platform": NotRequired[str],
        "PurchaseToken": NotRequired[str],
        "Recurrence": NotRequired[ScheduledInstanceRecurrenceTypeDef],
        "SlotDurationInHours": NotRequired[int],
        "TotalScheduledInstanceHours": NotRequired[int],
    },
)
ScheduledInstanceTypeDef = TypedDict(
    "ScheduledInstanceTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "HourlyPrice": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "InstanceType": NotRequired[str],
        "NetworkPlatform": NotRequired[str],
        "NextSlotStartTime": NotRequired[datetime],
        "Platform": NotRequired[str],
        "PreviousSlotEndTime": NotRequired[datetime],
        "Recurrence": NotRequired[ScheduledInstanceRecurrenceTypeDef],
        "ScheduledInstanceId": NotRequired[str],
        "SlotDurationInHours": NotRequired[int],
        "TermEndDate": NotRequired[datetime],
        "TermStartDate": NotRequired[datetime],
        "TotalScheduledInstanceHours": NotRequired[int],
    },
)
ScheduledInstancesBlockDeviceMappingTypeDef = TypedDict(
    "ScheduledInstancesBlockDeviceMappingTypeDef",
    {
        "DeviceName": NotRequired[str],
        "Ebs": NotRequired[ScheduledInstancesEbsTypeDef],
        "NoDevice": NotRequired[str],
        "VirtualName": NotRequired[str],
    },
)
ScheduledInstancesNetworkInterfaceTypeDef = TypedDict(
    "ScheduledInstancesNetworkInterfaceTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[Sequence[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[ScheduledInstancesIpv6AddressTypeDef]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddressConfigs": NotRequired[
            Sequence[ScheduledInstancesPrivateIpAddressConfigTypeDef]
        ],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
    },
)
SearchTransitGatewayMulticastGroupsResultTypeDef = TypedDict(
    "SearchTransitGatewayMulticastGroupsResultTypeDef",
    {
        "MulticastGroups": List[TransitGatewayMulticastGroupTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "VpcEndpointId": NotRequired[str],
        "VpcEndpointType": NotRequired[VpcEndpointTypeType],
        "VpcId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "State": NotRequired[StateType],
        "PolicyDocument": NotRequired[str],
        "RouteTableIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
        "Groups": NotRequired[List[SecurityGroupIdentifierTypeDef]],
        "IpAddressType": NotRequired[IpAddressTypeType],
        "DnsOptions": NotRequired[DnsOptionsTypeDef],
        "PrivateDnsEnabled": NotRequired[bool],
        "RequesterManaged": NotRequired[bool],
        "NetworkInterfaceIds": NotRequired[List[str]],
        "DnsEntries": NotRequired[List[DnsEntryTypeDef]],
        "CreationTimestamp": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
        "OwnerId": NotRequired[str],
        "LastError": NotRequired[LastErrorTypeDef],
    },
)
SecurityGroupRuleUpdateTypeDef = TypedDict(
    "SecurityGroupRuleUpdateTypeDef",
    {
        "SecurityGroupRuleId": str,
        "SecurityGroupRule": NotRequired[SecurityGroupRuleRequestTypeDef],
    },
)
ServiceConfigurationTypeDef = TypedDict(
    "ServiceConfigurationTypeDef",
    {
        "ServiceType": NotRequired[List[ServiceTypeDetailTypeDef]],
        "ServiceId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceState": NotRequired[ServiceStateType],
        "AvailabilityZones": NotRequired[List[str]],
        "AcceptanceRequired": NotRequired[bool],
        "ManagesVpcEndpoints": NotRequired[bool],
        "NetworkLoadBalancerArns": NotRequired[List[str]],
        "GatewayLoadBalancerArns": NotRequired[List[str]],
        "SupportedIpAddressTypes": NotRequired[List[ServiceConnectivityTypeType]],
        "BaseEndpointDnsNames": NotRequired[List[str]],
        "PrivateDnsName": NotRequired[str],
        "PrivateDnsNameConfiguration": NotRequired[PrivateDnsNameConfigurationTypeDef],
        "PayerResponsibility": NotRequired[Literal["ServiceOwner"]],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ServiceDetailTypeDef = TypedDict(
    "ServiceDetailTypeDef",
    {
        "ServiceName": NotRequired[str],
        "ServiceId": NotRequired[str],
        "ServiceType": NotRequired[List[ServiceTypeDetailTypeDef]],
        "AvailabilityZones": NotRequired[List[str]],
        "Owner": NotRequired[str],
        "BaseEndpointDnsNames": NotRequired[List[str]],
        "PrivateDnsName": NotRequired[str],
        "PrivateDnsNames": NotRequired[List[PrivateDnsDetailsTypeDef]],
        "VpcEndpointPolicySupported": NotRequired[bool],
        "AcceptanceRequired": NotRequired[bool],
        "ManagesVpcEndpoints": NotRequired[bool],
        "PayerResponsibility": NotRequired[Literal["ServiceOwner"]],
        "Tags": NotRequired[List[TagTypeDef]],
        "PrivateDnsNameVerificationState": NotRequired[DnsNameStateType],
        "SupportedIpAddressTypes": NotRequired[List[ServiceConnectivityTypeType]],
    },
)
SnapshotDetailTypeDef = TypedDict(
    "SnapshotDetailTypeDef",
    {
        "Description": NotRequired[str],
        "DeviceName": NotRequired[str],
        "DiskImageSize": NotRequired[float],
        "Format": NotRequired[str],
        "Progress": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "Url": NotRequired[str],
        "UserBucket": NotRequired[UserBucketDetailsTypeDef],
    },
)
SnapshotTaskDetailTypeDef = TypedDict(
    "SnapshotTaskDetailTypeDef",
    {
        "Description": NotRequired[str],
        "DiskImageSize": NotRequired[float],
        "Encrypted": NotRequired[bool],
        "Format": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Progress": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "Url": NotRequired[str],
        "UserBucket": NotRequired[UserBucketDetailsTypeDef],
    },
)
SpotMaintenanceStrategiesTypeDef = TypedDict(
    "SpotMaintenanceStrategiesTypeDef",
    {
        "CapacityRebalance": NotRequired[SpotCapacityRebalanceTypeDef],
    },
)
SpotDatafeedSubscriptionTypeDef = TypedDict(
    "SpotDatafeedSubscriptionTypeDef",
    {
        "Bucket": NotRequired[str],
        "Fault": NotRequired[SpotInstanceStateFaultTypeDef],
        "OwnerId": NotRequired[str],
        "Prefix": NotRequired[str],
        "State": NotRequired[DatafeedSubscriptionStateType],
    },
)
TransitGatewayMulticastDomainAssociationTypeDef = TypedDict(
    "TransitGatewayMulticastDomainAssociationTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "ResourceOwnerId": NotRequired[str],
        "Subnet": NotRequired[SubnetAssociationTypeDef],
    },
)
TransitGatewayMulticastDomainAssociationsTypeDef = TypedDict(
    "TransitGatewayMulticastDomainAssociationsTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "ResourceOwnerId": NotRequired[str],
        "Subnets": NotRequired[List[SubnetAssociationTypeDef]],
    },
)
SubnetIpv6CidrBlockAssociationTypeDef = TypedDict(
    "SubnetIpv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "Ipv6CidrBlockState": NotRequired[SubnetCidrBlockStateTypeDef],
    },
)
TargetReservationValueTypeDef = TypedDict(
    "TargetReservationValueTypeDef",
    {
        "ReservationValue": NotRequired[ReservationValueTypeDef],
        "TargetConfiguration": NotRequired[TargetConfigurationTypeDef],
    },
)
TargetGroupsConfigTypeDef = TypedDict(
    "TargetGroupsConfigTypeDef",
    {
        "TargetGroups": NotRequired[List[TargetGroupTypeDef]],
    },
)
TrafficMirrorFilterRuleTypeDef = TypedDict(
    "TrafficMirrorFilterRuleTypeDef",
    {
        "TrafficMirrorFilterRuleId": NotRequired[str],
        "TrafficMirrorFilterId": NotRequired[str],
        "TrafficDirection": NotRequired[TrafficDirectionType],
        "RuleNumber": NotRequired[int],
        "RuleAction": NotRequired[TrafficMirrorRuleActionType],
        "Protocol": NotRequired[int],
        "DestinationPortRange": NotRequired[TrafficMirrorPortRangeTypeDef],
        "SourcePortRange": NotRequired[TrafficMirrorPortRangeTypeDef],
        "DestinationCidrBlock": NotRequired[str],
        "SourceCidrBlock": NotRequired[str],
        "Description": NotRequired[str],
    },
)
TransitGatewayAttachmentTypeDef = TypedDict(
    "TransitGatewayAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "TransitGatewayOwnerId": NotRequired[str],
        "ResourceOwnerId": NotRequired[str],
        "ResourceType": NotRequired[TransitGatewayAttachmentResourceTypeType],
        "ResourceId": NotRequired[str],
        "State": NotRequired[TransitGatewayAttachmentStateType],
        "Association": NotRequired[TransitGatewayAttachmentAssociationTypeDef],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TransitGatewayConnectPeerConfigurationTypeDef = TypedDict(
    "TransitGatewayConnectPeerConfigurationTypeDef",
    {
        "TransitGatewayAddress": NotRequired[str],
        "PeerAddress": NotRequired[str],
        "InsideCidrBlocks": NotRequired[List[str]],
        "Protocol": NotRequired[Literal["gre"]],
        "BgpConfigurations": NotRequired[List[TransitGatewayAttachmentBgpConfigurationTypeDef]],
    },
)
TransitGatewayConnectTypeDef = TypedDict(
    "TransitGatewayConnectTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "TransportTransitGatewayAttachmentId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "State": NotRequired[TransitGatewayAttachmentStateType],
        "CreationTime": NotRequired[datetime],
        "Options": NotRequired[TransitGatewayConnectOptionsTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TransitGatewayMulticastDomainTypeDef = TypedDict(
    "TransitGatewayMulticastDomainTypeDef",
    {
        "TransitGatewayMulticastDomainId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "TransitGatewayMulticastDomainArn": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Options": NotRequired[TransitGatewayMulticastDomainOptionsTypeDef],
        "State": NotRequired[TransitGatewayMulticastDomainStateType],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TransitGatewayTypeDef = TypedDict(
    "TransitGatewayTypeDef",
    {
        "TransitGatewayId": NotRequired[str],
        "TransitGatewayArn": NotRequired[str],
        "State": NotRequired[TransitGatewayStateType],
        "OwnerId": NotRequired[str],
        "Description": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Options": NotRequired[TransitGatewayOptionsTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TransitGatewayPeeringAttachmentTypeDef = TypedDict(
    "TransitGatewayPeeringAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "AccepterTransitGatewayAttachmentId": NotRequired[str],
        "RequesterTgwInfo": NotRequired[PeeringTgwInfoTypeDef],
        "AccepterTgwInfo": NotRequired[PeeringTgwInfoTypeDef],
        "Options": NotRequired[TransitGatewayPeeringAttachmentOptionsTypeDef],
        "Status": NotRequired[PeeringAttachmentStatusTypeDef],
        "State": NotRequired[TransitGatewayAttachmentStateType],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TransitGatewayPolicyRuleTypeDef = TypedDict(
    "TransitGatewayPolicyRuleTypeDef",
    {
        "SourceCidrBlock": NotRequired[str],
        "SourcePortRange": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationPortRange": NotRequired[str],
        "Protocol": NotRequired[str],
        "MetaData": NotRequired[TransitGatewayPolicyRuleMetaDataTypeDef],
    },
)
TransitGatewayPrefixListReferenceTypeDef = TypedDict(
    "TransitGatewayPrefixListReferenceTypeDef",
    {
        "TransitGatewayRouteTableId": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "PrefixListOwnerId": NotRequired[str],
        "State": NotRequired[TransitGatewayPrefixListReferenceStateType],
        "Blackhole": NotRequired[bool],
        "TransitGatewayAttachment": NotRequired[TransitGatewayPrefixListAttachmentTypeDef],
    },
)
TransitGatewayRouteTypeDef = TypedDict(
    "TransitGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "TransitGatewayRouteTableAnnouncementId": NotRequired[str],
        "TransitGatewayAttachments": NotRequired[List[TransitGatewayRouteAttachmentTypeDef]],
        "Type": NotRequired[TransitGatewayRouteTypeType],
        "State": NotRequired[TransitGatewayRouteStateType],
    },
)
TransitGatewayVpcAttachmentTypeDef = TypedDict(
    "TransitGatewayVpcAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcOwnerId": NotRequired[str],
        "State": NotRequired[TransitGatewayAttachmentStateType],
        "SubnetIds": NotRequired[List[str]],
        "CreationTime": NotRequired[datetime],
        "Options": NotRequired[TransitGatewayVpcAttachmentOptionsTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
UnsuccessfulInstanceCreditSpecificationItemTypeDef = TypedDict(
    "UnsuccessfulInstanceCreditSpecificationItemTypeDef",
    {
        "InstanceId": NotRequired[str],
        "Error": NotRequired[UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef],
    },
)
UnsuccessfulItemTypeDef = TypedDict(
    "UnsuccessfulItemTypeDef",
    {
        "Error": NotRequired[UnsuccessfulItemErrorTypeDef],
        "ResourceId": NotRequired[str],
    },
)
ValidationWarningTypeDef = TypedDict(
    "ValidationWarningTypeDef",
    {
        "Errors": NotRequired[List[ValidationErrorTypeDef]],
    },
)
VerifiedAccessEndpointTypeDef = TypedDict(
    "VerifiedAccessEndpointTypeDef",
    {
        "VerifiedAccessInstanceId": NotRequired[str],
        "VerifiedAccessGroupId": NotRequired[str],
        "VerifiedAccessEndpointId": NotRequired[str],
        "ApplicationDomain": NotRequired[str],
        "EndpointType": NotRequired[VerifiedAccessEndpointTypeType],
        "AttachmentType": NotRequired[Literal["vpc"]],
        "DomainCertificateArn": NotRequired[str],
        "EndpointDomain": NotRequired[str],
        "DeviceValidationDomain": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "LoadBalancerOptions": NotRequired[VerifiedAccessEndpointLoadBalancerOptionsTypeDef],
        "NetworkInterfaceOptions": NotRequired[VerifiedAccessEndpointEniOptionsTypeDef],
        "Status": NotRequired[VerifiedAccessEndpointStatusTypeDef],
        "Description": NotRequired[str],
        "CreationTime": NotRequired[str],
        "LastUpdatedTime": NotRequired[str],
        "DeletionTime": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "SseSpecification": NotRequired[VerifiedAccessSseSpecificationResponseTypeDef],
    },
)
VerifiedAccessInstanceTypeDef = TypedDict(
    "VerifiedAccessInstanceTypeDef",
    {
        "VerifiedAccessInstanceId": NotRequired[str],
        "Description": NotRequired[str],
        "VerifiedAccessTrustProviders": NotRequired[
            List[VerifiedAccessTrustProviderCondensedTypeDef]
        ],
        "CreationTime": NotRequired[str],
        "LastUpdatedTime": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "FipsEnabled": NotRequired[bool],
    },
)
VerifiedAccessLogCloudWatchLogsDestinationTypeDef = TypedDict(
    "VerifiedAccessLogCloudWatchLogsDestinationTypeDef",
    {
        "Enabled": NotRequired[bool],
        "DeliveryStatus": NotRequired[VerifiedAccessLogDeliveryStatusTypeDef],
        "LogGroup": NotRequired[str],
    },
)
VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef = TypedDict(
    "VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef",
    {
        "Enabled": NotRequired[bool],
        "DeliveryStatus": NotRequired[VerifiedAccessLogDeliveryStatusTypeDef],
        "DeliveryStream": NotRequired[str],
    },
)
VerifiedAccessLogS3DestinationTypeDef = TypedDict(
    "VerifiedAccessLogS3DestinationTypeDef",
    {
        "Enabled": NotRequired[bool],
        "DeliveryStatus": NotRequired[VerifiedAccessLogDeliveryStatusTypeDef],
        "BucketName": NotRequired[str],
        "Prefix": NotRequired[str],
        "BucketOwner": NotRequired[str],
    },
)
VerifiedAccessLogOptionsTypeDef = TypedDict(
    "VerifiedAccessLogOptionsTypeDef",
    {
        "S3": NotRequired[VerifiedAccessLogS3DestinationOptionsTypeDef],
        "CloudWatchLogs": NotRequired[VerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef],
        "KinesisDataFirehose": NotRequired[
            VerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef
        ],
        "LogVersion": NotRequired[str],
        "IncludeTrustContext": NotRequired[bool],
    },
)
VolumeStatusInfoTypeDef = TypedDict(
    "VolumeStatusInfoTypeDef",
    {
        "Details": NotRequired[List[VolumeStatusDetailsTypeDef]],
        "Status": NotRequired[VolumeStatusInfoStatusType],
    },
)
VpcCidrBlockAssociationTypeDef = TypedDict(
    "VpcCidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "CidrBlockState": NotRequired[VpcCidrBlockStateTypeDef],
    },
)
VpcIpv6CidrBlockAssociationTypeDef = TypedDict(
    "VpcIpv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "Ipv6CidrBlockState": NotRequired[VpcCidrBlockStateTypeDef],
        "NetworkBorderGroup": NotRequired[str],
        "Ipv6Pool": NotRequired[str],
    },
)
VpcPeeringConnectionVpcInfoResponseTypeDef = TypedDict(
    "VpcPeeringConnectionVpcInfoResponseTypeDef",
    {
        "CidrBlock": str,
        "Ipv6CidrBlockSet": List[Ipv6CidrBlockTypeDef],
        "CidrBlockSet": List[CidrBlockTypeDef],
        "OwnerId": str,
        "PeeringOptions": VpcPeeringConnectionOptionsDescriptionTypeDef,
        "VpcId": str,
        "Region": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VpcPeeringConnectionVpcInfoTypeDef = TypedDict(
    "VpcPeeringConnectionVpcInfoTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "Ipv6CidrBlockSet": NotRequired[List[Ipv6CidrBlockTypeDef]],
        "CidrBlockSet": NotRequired[List[CidrBlockTypeDef]],
        "OwnerId": NotRequired[str],
        "PeeringOptions": NotRequired[VpcPeeringConnectionOptionsDescriptionTypeDef],
        "VpcId": NotRequired[str],
        "Region": NotRequired[str],
    },
)
LocalGatewayRouteTableTypeDef = TypedDict(
    "LocalGatewayRouteTableTypeDef",
    {
        "LocalGatewayRouteTableId": NotRequired[str],
        "LocalGatewayRouteTableArn": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "Mode": NotRequired[LocalGatewayRouteTableModeType],
        "StateReason": NotRequired[StateReasonTypeDef],
    },
)
VolumeResponseTypeDef = TypedDict(
    "VolumeResponseTypeDef",
    {
        "Attachments": List[VolumeAttachmentTypeDef],
        "AvailabilityZone": str,
        "CreateTime": datetime,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OutpostArn": str,
        "Size": int,
        "SnapshotId": str,
        "State": VolumeStateType,
        "VolumeId": str,
        "Iops": int,
        "Tags": List[TagTypeDef],
        "VolumeType": VolumeTypeType,
        "FastRestored": bool,
        "MultiAttachEnabled": bool,
        "Throughput": int,
        "SseType": SSETypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "Attachments": NotRequired[List[VolumeAttachmentTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Size": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "State": NotRequired[VolumeStateType],
        "VolumeId": NotRequired[str],
        "Iops": NotRequired[int],
        "Tags": NotRequired[List[TagTypeDef]],
        "VolumeType": NotRequired[VolumeTypeType],
        "FastRestored": NotRequired[bool],
        "MultiAttachEnabled": NotRequired[bool],
        "Throughput": NotRequired[int],
        "SseType": NotRequired[SSETypeType],
    },
)
DescribeAccountAttributesResultTypeDef = TypedDict(
    "DescribeAccountAttributesResultTypeDef",
    {
        "AccountAttributes": List[AccountAttributeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdditionalDetailTypeDef = TypedDict(
    "AdditionalDetailTypeDef",
    {
        "AdditionalDetailType": NotRequired[str],
        "Component": NotRequired[AnalysisComponentTypeDef],
        "VpcEndpointService": NotRequired[AnalysisComponentTypeDef],
        "RuleOptions": NotRequired[List[RuleOptionTypeDef]],
        "RuleGroupTypePairs": NotRequired[List[RuleGroupTypePairTypeDef]],
        "RuleGroupRuleOptionsPairs": NotRequired[List[RuleGroupRuleOptionsPairTypeDef]],
        "ServiceName": NotRequired[str],
        "LoadBalancers": NotRequired[List[AnalysisComponentTypeDef]],
    },
)
DescribeAddressesAttributeResultTypeDef = TypedDict(
    "DescribeAddressesAttributeResultTypeDef",
    {
        "Addresses": List[AddressAttributeTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyAddressAttributeResultTypeDef = TypedDict(
    "ModifyAddressAttributeResultTypeDef",
    {
        "Address": AddressAttributeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetAddressAttributeResultTypeDef = TypedDict(
    "ResetAddressAttributeResultTypeDef",
    {
        "Address": AddressAttributeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef",
    {
        "Addresses": List[AddressTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcEndpointServicePermissionsResultTypeDef = TypedDict(
    "DescribeVpcEndpointServicePermissionsResultTypeDef",
    {
        "AllowedPrincipals": List[AllowedPrincipalTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCarrierGatewayResultTypeDef = TypedDict(
    "CreateCarrierGatewayResultTypeDef",
    {
        "CarrierGateway": CarrierGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCarrierGatewayResultTypeDef = TypedDict(
    "DeleteCarrierGatewayResultTypeDef",
    {
        "CarrierGateway": CarrierGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCarrierGatewaysResultTypeDef = TypedDict(
    "DescribeCarrierGatewaysResultTypeDef",
    {
        "CarrierGateways": List[CarrierGatewayTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCoipPoolResultTypeDef = TypedDict(
    "CreateCoipPoolResultTypeDef",
    {
        "CoipPool": CoipPoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCoipPoolResultTypeDef = TypedDict(
    "DeleteCoipPoolResultTypeDef",
    {
        "CoipPool": CoipPoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCoipPoolsResultTypeDef = TypedDict(
    "DescribeCoipPoolsResultTypeDef",
    {
        "CoipPools": List[CoipPoolTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCustomerGatewayResultTypeDef = TypedDict(
    "CreateCustomerGatewayResultTypeDef",
    {
        "CustomerGateway": CustomerGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCustomerGatewaysResultTypeDef = TypedDict(
    "DescribeCustomerGatewaysResultTypeDef",
    {
        "CustomerGateways": List[CustomerGatewayTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceConnectEndpointResultTypeDef = TypedDict(
    "CreateInstanceConnectEndpointResultTypeDef",
    {
        "InstanceConnectEndpoint": Ec2InstanceConnectEndpointTypeDef,
        "ClientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInstanceConnectEndpointResultTypeDef = TypedDict(
    "DeleteInstanceConnectEndpointResultTypeDef",
    {
        "InstanceConnectEndpoint": Ec2InstanceConnectEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstanceConnectEndpointsResultTypeDef = TypedDict(
    "DescribeInstanceConnectEndpointsResultTypeDef",
    {
        "InstanceConnectEndpoints": List[Ec2InstanceConnectEndpointTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHostReservationsResultTypeDef = TypedDict(
    "DescribeHostReservationsResultTypeDef",
    {
        "HostReservationSet": List[HostReservationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "AssociateInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
        "AssociationTarget": InstanceEventWindowAssociationRequestTypeDef,
        "DryRun": NotRequired[bool],
    },
)
InstanceEventWindowTypeDef = TypedDict(
    "InstanceEventWindowTypeDef",
    {
        "InstanceEventWindowId": NotRequired[str],
        "TimeRanges": NotRequired[List[InstanceEventWindowTimeRangeTypeDef]],
        "Name": NotRequired[str],
        "CronExpression": NotRequired[str],
        "AssociationTarget": NotRequired[InstanceEventWindowAssociationTargetTypeDef],
        "State": NotRequired[InstanceEventWindowStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
DisassociateInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "DisassociateInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
        "AssociationTarget": InstanceEventWindowDisassociationRequestTypeDef,
        "DryRun": NotRequired[bool],
    },
)
AssociateIpamResourceDiscoveryResultTypeDef = TypedDict(
    "AssociateIpamResourceDiscoveryResultTypeDef",
    {
        "IpamResourceDiscoveryAssociation": IpamResourceDiscoveryAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIpamResourceDiscoveryAssociationsResultTypeDef = TypedDict(
    "DescribeIpamResourceDiscoveryAssociationsResultTypeDef",
    {
        "IpamResourceDiscoveryAssociations": List[IpamResourceDiscoveryAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateIpamResourceDiscoveryResultTypeDef = TypedDict(
    "DisassociateIpamResourceDiscoveryResultTypeDef",
    {
        "IpamResourceDiscoveryAssociation": IpamResourceDiscoveryAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIpamScopeResultTypeDef = TypedDict(
    "CreateIpamScopeResultTypeDef",
    {
        "IpamScope": IpamScopeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIpamScopeResultTypeDef = TypedDict(
    "DeleteIpamScopeResultTypeDef",
    {
        "IpamScope": IpamScopeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIpamScopesResultTypeDef = TypedDict(
    "DescribeIpamScopesResultTypeDef",
    {
        "NextToken": str,
        "IpamScopes": List[IpamScopeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyIpamScopeResultTypeDef = TypedDict(
    "ModifyIpamScopeResultTypeDef",
    {
        "IpamScope": IpamScopeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeKeyPairsResultTypeDef = TypedDict(
    "DescribeKeyPairsResultTypeDef",
    {
        "KeyPairs": List[KeyPairInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLaunchTemplateResultTypeDef = TypedDict(
    "DeleteLaunchTemplateResultTypeDef",
    {
        "LaunchTemplate": LaunchTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLaunchTemplatesResultTypeDef = TypedDict(
    "DescribeLaunchTemplatesResultTypeDef",
    {
        "LaunchTemplates": List[LaunchTemplateTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyLaunchTemplateResultTypeDef = TypedDict(
    "ModifyLaunchTemplateResultTypeDef",
    {
        "LaunchTemplate": LaunchTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociation": (
            LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef
        ),
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociation": (
            LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef
        ),
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociations": List[
            LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLocalGatewayRouteTableVpcAssociationResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableVpcAssociationResultTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociation": LocalGatewayRouteTableVpcAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociation": LocalGatewayRouteTableVpcAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociations": List[LocalGatewayRouteTableVpcAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLocalGatewaysResultTypeDef = TypedDict(
    "DescribeLocalGatewaysResultTypeDef",
    {
        "LocalGateways": List[LocalGatewayTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroups": List[LocalGatewayVirtualInterfaceGroupTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLocalGatewayVirtualInterfacesResultTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfacesResultTypeDef",
    {
        "LocalGatewayVirtualInterfaces": List[LocalGatewayVirtualInterfaceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateManagedPrefixListResultTypeDef = TypedDict(
    "CreateManagedPrefixListResultTypeDef",
    {
        "PrefixList": ManagedPrefixListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteManagedPrefixListResultTypeDef = TypedDict(
    "DeleteManagedPrefixListResultTypeDef",
    {
        "PrefixList": ManagedPrefixListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeManagedPrefixListsResultTypeDef = TypedDict(
    "DescribeManagedPrefixListsResultTypeDef",
    {
        "NextToken": str,
        "PrefixLists": List[ManagedPrefixListTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyManagedPrefixListResultTypeDef = TypedDict(
    "ModifyManagedPrefixListResultTypeDef",
    {
        "PrefixList": ManagedPrefixListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreManagedPrefixListVersionResultTypeDef = TypedDict(
    "RestoreManagedPrefixListVersionResultTypeDef",
    {
        "PrefixList": ManagedPrefixListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalyses": List[NetworkInsightsAccessScopeAnalysisTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartNetworkInsightsAccessScopeAnalysisResultTypeDef = TypedDict(
    "StartNetworkInsightsAccessScopeAnalysisResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysis": NetworkInsightsAccessScopeAnalysisTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNetworkInsightsAccessScopesResultTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopesResultTypeDef",
    {
        "NetworkInsightsAccessScopes": List[NetworkInsightsAccessScopeTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePlacementGroupResultTypeDef = TypedDict(
    "CreatePlacementGroupResultTypeDef",
    {
        "PlacementGroup": PlacementGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePlacementGroupsResultTypeDef = TypedDict(
    "DescribePlacementGroupsResultTypeDef",
    {
        "PlacementGroups": List[PlacementGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateReplaceRootVolumeTaskResultTypeDef = TypedDict(
    "CreateReplaceRootVolumeTaskResultTypeDef",
    {
        "ReplaceRootVolumeTask": ReplaceRootVolumeTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReplaceRootVolumeTasksResultTypeDef = TypedDict(
    "DescribeReplaceRootVolumeTasksResultTypeDef",
    {
        "ReplaceRootVolumeTasks": List[ReplaceRootVolumeTaskTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSecurityGroupsForVpcResultTypeDef = TypedDict(
    "GetSecurityGroupsForVpcResultTypeDef",
    {
        "NextToken": str,
        "SecurityGroupForVpcs": List[SecurityGroupForVpcTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSnapshotsResultTypeDef = TypedDict(
    "CreateSnapshotsResultTypeDef",
    {
        "Snapshots": List[SnapshotInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSnapshotTierStatusResultTypeDef = TypedDict(
    "DescribeSnapshotTierStatusResultTypeDef",
    {
        "SnapshotTierStatuses": List[SnapshotTierStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSnapshotsResultTypeDef = TypedDict(
    "DescribeSnapshotsResultTypeDef",
    {
        "Snapshots": List[SnapshotTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSubnetCidrReservationResultTypeDef = TypedDict(
    "CreateSubnetCidrReservationResultTypeDef",
    {
        "SubnetCidrReservation": SubnetCidrReservationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSubnetCidrReservationResultTypeDef = TypedDict(
    "DeleteSubnetCidrReservationResultTypeDef",
    {
        "DeletedSubnetCidrReservation": SubnetCidrReservationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubnetCidrReservationsResultTypeDef = TypedDict(
    "GetSubnetCidrReservationsResultTypeDef",
    {
        "SubnetIpv4CidrReservations": List[SubnetCidrReservationTypeDef],
        "SubnetIpv6CidrReservations": List[SubnetCidrReservationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptAddressTransferRequestRequestTypeDef = TypedDict(
    "AcceptAddressTransferRequestRequestTypeDef",
    {
        "Address": str,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
AllocateAddressRequestRequestTypeDef = TypedDict(
    "AllocateAddressRequestRequestTypeDef",
    {
        "Domain": NotRequired[DomainTypeType],
        "Address": NotRequired[str],
        "PublicIpv4Pool": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "CustomerOwnedIpv4Pool": NotRequired[str],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
AllocateHostsRequestRequestTypeDef = TypedDict(
    "AllocateHostsRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "AutoPlacement": NotRequired[AutoPlacementType],
        "ClientToken": NotRequired[str],
        "InstanceType": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "Quantity": NotRequired[int],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "HostRecovery": NotRequired[HostRecoveryType],
        "OutpostArn": NotRequired[str],
        "HostMaintenance": NotRequired[HostMaintenanceType],
        "AssetIds": NotRequired[Sequence[str]],
    },
)
AssociateIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "AssociateIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "IpamId": str,
        "IpamResourceDiscoveryId": str,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CopySnapshotRequestRequestTypeDef = TypedDict(
    "CopySnapshotRequestRequestTypeDef",
    {
        "SourceRegion": str,
        "SourceSnapshotId": str,
        "Description": NotRequired[str],
        "DestinationOutpostArn": NotRequired[str],
        "DestinationRegion": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "PresignedUrl": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CopySnapshotRequestSnapshotCopyTypeDef = TypedDict(
    "CopySnapshotRequestSnapshotCopyTypeDef",
    {
        "SourceRegion": str,
        "Description": NotRequired[str],
        "DestinationOutpostArn": NotRequired[str],
        "DestinationRegion": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "PresignedUrl": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateCapacityReservationFleetRequestRequestTypeDef = TypedDict(
    "CreateCapacityReservationFleetRequestRequestTypeDef",
    {
        "InstanceTypeSpecifications": Sequence[ReservationFleetInstanceSpecificationTypeDef],
        "TotalTargetCapacity": int,
        "AllocationStrategy": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Tenancy": NotRequired[Literal["default"]],
        "EndDate": NotRequired[TimestampTypeDef],
        "InstanceMatchCriteria": NotRequired[Literal["open"]],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateCapacityReservationRequestRequestTypeDef = TypedDict(
    "CreateCapacityReservationRequestRequestTypeDef",
    {
        "InstanceType": str,
        "InstancePlatform": CapacityReservationInstancePlatformType,
        "InstanceCount": int,
        "ClientToken": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "Tenancy": NotRequired[CapacityReservationTenancyType],
        "EbsOptimized": NotRequired[bool],
        "EphemeralStorage": NotRequired[bool],
        "EndDate": NotRequired[TimestampTypeDef],
        "EndDateType": NotRequired[EndDateTypeType],
        "InstanceMatchCriteria": NotRequired[InstanceMatchCriteriaType],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
        "OutpostArn": NotRequired[str],
        "PlacementGroupArn": NotRequired[str],
    },
)
CreateCarrierGatewayRequestRequestTypeDef = TypedDict(
    "CreateCarrierGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)
CreateCoipPoolRequestRequestTypeDef = TypedDict(
    "CreateCoipPoolRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateCustomerGatewayRequestRequestTypeDef = TypedDict(
    "CreateCustomerGatewayRequestRequestTypeDef",
    {
        "Type": Literal["ipsec.1"],
        "BgpAsn": NotRequired[int],
        "PublicIp": NotRequired[str],
        "CertificateArn": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DeviceName": NotRequired[str],
        "IpAddress": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
CreateDhcpOptionsRequestRequestTypeDef = TypedDict(
    "CreateDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpConfigurations": Sequence[NewDhcpConfigurationTypeDef],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateDhcpOptionsRequestServiceResourceCreateDhcpOptionsTypeDef = TypedDict(
    "CreateDhcpOptionsRequestServiceResourceCreateDhcpOptionsTypeDef",
    {
        "DhcpConfigurations": Sequence[NewDhcpConfigurationTypeDef],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateEgressOnlyInternetGatewayRequestRequestTypeDef = TypedDict(
    "CreateEgressOnlyInternetGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateFlowLogsRequestRequestTypeDef = TypedDict(
    "CreateFlowLogsRequestRequestTypeDef",
    {
        "ResourceIds": Sequence[str],
        "ResourceType": FlowLogsResourceTypeType,
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "DeliverLogsPermissionArn": NotRequired[str],
        "DeliverCrossAccountRole": NotRequired[str],
        "LogGroupName": NotRequired[str],
        "TrafficType": NotRequired[TrafficTypeType],
        "LogDestinationType": NotRequired[LogDestinationTypeType],
        "LogDestination": NotRequired[str],
        "LogFormat": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "MaxAggregationInterval": NotRequired[int],
        "DestinationOptions": NotRequired[DestinationOptionsRequestTypeDef],
    },
)
CreateFpgaImageRequestRequestTypeDef = TypedDict(
    "CreateFpgaImageRequestRequestTypeDef",
    {
        "InputStorageLocation": StorageLocationTypeDef,
        "DryRun": NotRequired[bool],
        "LogsStorageLocation": NotRequired[StorageLocationTypeDef],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "ClientToken": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateInstanceConnectEndpointRequestRequestTypeDef = TypedDict(
    "CreateInstanceConnectEndpointRequestRequestTypeDef",
    {
        "SubnetId": str,
        "DryRun": NotRequired[bool],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "PreserveClientIp": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "CreateInstanceEventWindowRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Name": NotRequired[str],
        "TimeRanges": NotRequired[Sequence[InstanceEventWindowTimeRangeRequestTypeDef]],
        "CronExpression": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateInstanceExportTaskRequestRequestTypeDef = TypedDict(
    "CreateInstanceExportTaskRequestRequestTypeDef",
    {
        "ExportToS3Task": ExportToS3TaskSpecificationTypeDef,
        "InstanceId": str,
        "TargetEnvironment": ExportEnvironmentType,
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateInternetGatewayRequestRequestTypeDef = TypedDict(
    "CreateInternetGatewayRequestRequestTypeDef",
    {
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateInternetGatewayRequestServiceResourceCreateInternetGatewayTypeDef = TypedDict(
    "CreateInternetGatewayRequestServiceResourceCreateInternetGatewayTypeDef",
    {
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateIpamPoolRequestRequestTypeDef = TypedDict(
    "CreateIpamPoolRequestRequestTypeDef",
    {
        "IpamScopeId": str,
        "AddressFamily": AddressFamilyType,
        "DryRun": NotRequired[bool],
        "Locale": NotRequired[str],
        "SourceIpamPoolId": NotRequired[str],
        "Description": NotRequired[str],
        "AutoImport": NotRequired[bool],
        "PubliclyAdvertisable": NotRequired[bool],
        "AllocationMinNetmaskLength": NotRequired[int],
        "AllocationMaxNetmaskLength": NotRequired[int],
        "AllocationDefaultNetmaskLength": NotRequired[int],
        "AllocationResourceTags": NotRequired[Sequence[RequestIpamResourceTagTypeDef]],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
        "AwsService": NotRequired[Literal["ec2"]],
        "PublicIpSource": NotRequired[IpamPoolPublicIpSourceType],
        "SourceResource": NotRequired[IpamPoolSourceResourceRequestTypeDef],
    },
)
CreateIpamRequestRequestTypeDef = TypedDict(
    "CreateIpamRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "OperatingRegions": NotRequired[Sequence[AddIpamOperatingRegionTypeDef]],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
        "Tier": NotRequired[IpamTierType],
    },
)
CreateIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "CreateIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "OperatingRegions": NotRequired[Sequence[AddIpamOperatingRegionTypeDef]],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CreateIpamScopeRequestRequestTypeDef = TypedDict(
    "CreateIpamScopeRequestRequestTypeDef",
    {
        "IpamId": str,
        "DryRun": NotRequired[bool],
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CreateKeyPairRequestRequestTypeDef = TypedDict(
    "CreateKeyPairRequestRequestTypeDef",
    {
        "KeyName": str,
        "DryRun": NotRequired[bool],
        "KeyType": NotRequired[KeyTypeType],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "KeyFormat": NotRequired[KeyFormatType],
    },
)
CreateKeyPairRequestServiceResourceCreateKeyPairTypeDef = TypedDict(
    "CreateKeyPairRequestServiceResourceCreateKeyPairTypeDef",
    {
        "KeyName": str,
        "DryRun": NotRequired[bool],
        "KeyType": NotRequired[KeyTypeType],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "KeyFormat": NotRequired[KeyFormatType],
    },
)
CreateLocalGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableRequestRequestTypeDef",
    {
        "LocalGatewayId": str,
        "Mode": NotRequired[LocalGatewayRouteTableModeType],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "VpcId": str,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateManagedPrefixListRequestRequestTypeDef = TypedDict(
    "CreateManagedPrefixListRequestRequestTypeDef",
    {
        "PrefixListName": str,
        "MaxEntries": int,
        "AddressFamily": str,
        "DryRun": NotRequired[bool],
        "Entries": NotRequired[Sequence[AddPrefixListEntryTypeDef]],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CreateNatGatewayRequestRequestTypeDef = TypedDict(
    "CreateNatGatewayRequestRequestTypeDef",
    {
        "SubnetId": str,
        "AllocationId": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ConnectivityType": NotRequired[ConnectivityTypeType],
        "PrivateIpAddress": NotRequired[str],
        "SecondaryAllocationIds": NotRequired[Sequence[str]],
        "SecondaryPrivateIpAddresses": NotRequired[Sequence[str]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
    },
)
CreateNetworkAclRequestRequestTypeDef = TypedDict(
    "CreateNetworkAclRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateNetworkAclRequestServiceResourceCreateNetworkAclTypeDef = TypedDict(
    "CreateNetworkAclRequestServiceResourceCreateNetworkAclTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateNetworkAclRequestVpcCreateNetworkAclTypeDef = TypedDict(
    "CreateNetworkAclRequestVpcCreateNetworkAclTypeDef",
    {
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "CreateNetworkInterfaceRequestRequestTypeDef",
    {
        "SubnetId": str,
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[InstanceIpv6AddressTypeDef]],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[Sequence[PrivateIpAddressSpecificationTypeDef]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence[Ipv4PrefixSpecificationRequestTypeDef]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence[Ipv6PrefixSpecificationRequestTypeDef]],
        "Ipv6PrefixCount": NotRequired[int],
        "InterfaceType": NotRequired[NetworkInterfaceCreationTypeType],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
        "EnablePrimaryIpv6": NotRequired[bool],
        "ConnectionTrackingSpecification": NotRequired[
            ConnectionTrackingSpecificationRequestTypeDef
        ],
    },
)
CreateNetworkInterfaceRequestServiceResourceCreateNetworkInterfaceTypeDef = TypedDict(
    "CreateNetworkInterfaceRequestServiceResourceCreateNetworkInterfaceTypeDef",
    {
        "SubnetId": str,
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[InstanceIpv6AddressTypeDef]],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[Sequence[PrivateIpAddressSpecificationTypeDef]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence[Ipv4PrefixSpecificationRequestTypeDef]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence[Ipv6PrefixSpecificationRequestTypeDef]],
        "Ipv6PrefixCount": NotRequired[int],
        "InterfaceType": NotRequired[NetworkInterfaceCreationTypeType],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
        "EnablePrimaryIpv6": NotRequired[bool],
        "ConnectionTrackingSpecification": NotRequired[
            ConnectionTrackingSpecificationRequestTypeDef
        ],
    },
)
CreateNetworkInterfaceRequestSubnetCreateNetworkInterfaceTypeDef = TypedDict(
    "CreateNetworkInterfaceRequestSubnetCreateNetworkInterfaceTypeDef",
    {
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[InstanceIpv6AddressTypeDef]],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[Sequence[PrivateIpAddressSpecificationTypeDef]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence[Ipv4PrefixSpecificationRequestTypeDef]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence[Ipv6PrefixSpecificationRequestTypeDef]],
        "Ipv6PrefixCount": NotRequired[int],
        "InterfaceType": NotRequired[NetworkInterfaceCreationTypeType],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
        "EnablePrimaryIpv6": NotRequired[bool],
        "ConnectionTrackingSpecification": NotRequired[
            ConnectionTrackingSpecificationRequestTypeDef
        ],
    },
)
CreatePlacementGroupRequestRequestTypeDef = TypedDict(
    "CreatePlacementGroupRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "GroupName": NotRequired[str],
        "Strategy": NotRequired[PlacementStrategyType],
        "PartitionCount": NotRequired[int],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "SpreadLevel": NotRequired[SpreadLevelType],
    },
)
CreatePlacementGroupRequestServiceResourceCreatePlacementGroupTypeDef = TypedDict(
    "CreatePlacementGroupRequestServiceResourceCreatePlacementGroupTypeDef",
    {
        "DryRun": NotRequired[bool],
        "GroupName": NotRequired[str],
        "Strategy": NotRequired[PlacementStrategyType],
        "PartitionCount": NotRequired[int],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "SpreadLevel": NotRequired[SpreadLevelType],
    },
)
CreatePublicIpv4PoolRequestRequestTypeDef = TypedDict(
    "CreatePublicIpv4PoolRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateReplaceRootVolumeTaskRequestRequestTypeDef = TypedDict(
    "CreateReplaceRootVolumeTaskRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SnapshotId": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ImageId": NotRequired[str],
        "DeleteReplacedRootVolume": NotRequired[bool],
    },
)
CreateRestoreImageTaskRequestRequestTypeDef = TypedDict(
    "CreateRestoreImageTaskRequestRequestTypeDef",
    {
        "Bucket": str,
        "ObjectKey": str,
        "Name": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateRouteTableRequestRequestTypeDef = TypedDict(
    "CreateRouteTableRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateRouteTableRequestServiceResourceCreateRouteTableTypeDef = TypedDict(
    "CreateRouteTableRequestServiceResourceCreateRouteTableTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateRouteTableRequestVpcCreateRouteTableTypeDef = TypedDict(
    "CreateRouteTableRequestVpcCreateRouteTableTypeDef",
    {
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateSecurityGroupRequestRequestTypeDef = TypedDict(
    "CreateSecurityGroupRequestRequestTypeDef",
    {
        "Description": str,
        "GroupName": str,
        "VpcId": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateSecurityGroupRequestServiceResourceCreateSecurityGroupTypeDef = TypedDict(
    "CreateSecurityGroupRequestServiceResourceCreateSecurityGroupTypeDef",
    {
        "Description": str,
        "GroupName": str,
        "VpcId": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateSecurityGroupRequestVpcCreateSecurityGroupTypeDef = TypedDict(
    "CreateSecurityGroupRequestVpcCreateSecurityGroupTypeDef",
    {
        "Description": str,
        "GroupName": str,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateSnapshotRequestRequestTypeDef = TypedDict(
    "CreateSnapshotRequestRequestTypeDef",
    {
        "VolumeId": str,
        "Description": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateSnapshotRequestServiceResourceCreateSnapshotTypeDef = TypedDict(
    "CreateSnapshotRequestServiceResourceCreateSnapshotTypeDef",
    {
        "VolumeId": str,
        "Description": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateSnapshotRequestVolumeCreateSnapshotTypeDef = TypedDict(
    "CreateSnapshotRequestVolumeCreateSnapshotTypeDef",
    {
        "Description": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateSnapshotsRequestRequestTypeDef = TypedDict(
    "CreateSnapshotsRequestRequestTypeDef",
    {
        "InstanceSpecification": InstanceSpecificationTypeDef,
        "Description": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
        "CopyTagsFromSource": NotRequired[Literal["volume"]],
    },
)
CreateSubnetCidrReservationRequestRequestTypeDef = TypedDict(
    "CreateSubnetCidrReservationRequestRequestTypeDef",
    {
        "SubnetId": str,
        "Cidr": str,
        "ReservationType": SubnetCidrReservationTypeType,
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateSubnetRequestRequestTypeDef = TypedDict(
    "CreateSubnetRequestRequestTypeDef",
    {
        "VpcId": str,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
        "Ipv4IpamPoolId": NotRequired[str],
        "Ipv4NetmaskLength": NotRequired[int],
        "Ipv6IpamPoolId": NotRequired[str],
        "Ipv6NetmaskLength": NotRequired[int],
    },
)
CreateSubnetRequestServiceResourceCreateSubnetTypeDef = TypedDict(
    "CreateSubnetRequestServiceResourceCreateSubnetTypeDef",
    {
        "VpcId": str,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
        "Ipv4IpamPoolId": NotRequired[str],
        "Ipv4NetmaskLength": NotRequired[int],
        "Ipv6IpamPoolId": NotRequired[str],
        "Ipv6NetmaskLength": NotRequired[int],
    },
)
CreateSubnetRequestVpcCreateSubnetTypeDef = TypedDict(
    "CreateSubnetRequestVpcCreateSubnetTypeDef",
    {
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
        "Ipv4IpamPoolId": NotRequired[str],
        "Ipv4NetmaskLength": NotRequired[int],
        "Ipv6IpamPoolId": NotRequired[str],
        "Ipv6NetmaskLength": NotRequired[int],
    },
)
CreateTrafficMirrorFilterRequestRequestTypeDef = TypedDict(
    "CreateTrafficMirrorFilterRequestRequestTypeDef",
    {
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)
CreateTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "CreateTrafficMirrorSessionRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "TrafficMirrorTargetId": str,
        "TrafficMirrorFilterId": str,
        "SessionNumber": int,
        "PacketLength": NotRequired[int],
        "VirtualNetworkId": NotRequired[int],
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)
CreateTrafficMirrorTargetRequestRequestTypeDef = TypedDict(
    "CreateTrafficMirrorTargetRequestRequestTypeDef",
    {
        "NetworkInterfaceId": NotRequired[str],
        "NetworkLoadBalancerArn": NotRequired[str],
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "GatewayLoadBalancerEndpointId": NotRequired[str],
    },
)
CreateTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "PeerAddress": str,
        "InsideCidrBlocks": Sequence[str],
        "TransitGatewayAddress": NotRequired[str],
        "BgpOptions": NotRequired[TransitGatewayConnectRequestBgpOptionsTypeDef],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateTransitGatewayConnectRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayConnectRequestRequestTypeDef",
    {
        "TransportTransitGatewayAttachmentId": str,
        "Options": CreateTransitGatewayConnectRequestOptionsTypeDef,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "Options": NotRequired[CreateTransitGatewayMulticastDomainRequestOptionsTypeDef],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "PeerTransitGatewayId": str,
        "PeerAccountId": str,
        "PeerRegion": str,
        "Options": NotRequired[CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateTransitGatewayRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayRequestRequestTypeDef",
    {
        "Description": NotRequired[str],
        "Options": NotRequired[TransitGatewayRequestOptionsTypeDef],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PeeringAttachmentId": str,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "VpcId": str,
        "SubnetIds": Sequence[str],
        "Options": NotRequired[CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
CreateVerifiedAccessEndpointRequestRequestTypeDef = TypedDict(
    "CreateVerifiedAccessEndpointRequestRequestTypeDef",
    {
        "VerifiedAccessGroupId": str,
        "EndpointType": VerifiedAccessEndpointTypeType,
        "AttachmentType": Literal["vpc"],
        "DomainCertificateArn": str,
        "ApplicationDomain": str,
        "EndpointDomainPrefix": str,
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "LoadBalancerOptions": NotRequired[CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef],
        "NetworkInterfaceOptions": NotRequired[CreateVerifiedAccessEndpointEniOptionsTypeDef],
        "Description": NotRequired[str],
        "PolicyDocument": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "SseSpecification": NotRequired[VerifiedAccessSseSpecificationRequestTypeDef],
    },
)
CreateVerifiedAccessGroupRequestRequestTypeDef = TypedDict(
    "CreateVerifiedAccessGroupRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "Description": NotRequired[str],
        "PolicyDocument": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "SseSpecification": NotRequired[VerifiedAccessSseSpecificationRequestTypeDef],
    },
)
CreateVerifiedAccessInstanceRequestRequestTypeDef = TypedDict(
    "CreateVerifiedAccessInstanceRequestRequestTypeDef",
    {
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "FIPSEnabled": NotRequired[bool],
    },
)
CreateVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "CreateVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "TrustProviderType": TrustProviderTypeType,
        "PolicyReferenceName": str,
        "UserTrustProviderType": NotRequired[UserTrustProviderTypeType],
        "DeviceTrustProviderType": NotRequired[DeviceTrustProviderTypeType],
        "OidcOptions": NotRequired[CreateVerifiedAccessTrustProviderOidcOptionsTypeDef],
        "DeviceOptions": NotRequired[CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef],
        "Description": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "SseSpecification": NotRequired[VerifiedAccessSseSpecificationRequestTypeDef],
    },
)
CreateVolumeRequestRequestTypeDef = TypedDict(
    "CreateVolumeRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Encrypted": NotRequired[bool],
        "Iops": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Size": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "VolumeType": NotRequired[VolumeTypeType],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "MultiAttachEnabled": NotRequired[bool],
        "Throughput": NotRequired[int],
        "ClientToken": NotRequired[str],
    },
)
CreateVolumeRequestServiceResourceCreateVolumeTypeDef = TypedDict(
    "CreateVolumeRequestServiceResourceCreateVolumeTypeDef",
    {
        "AvailabilityZone": str,
        "Encrypted": NotRequired[bool],
        "Iops": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Size": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "VolumeType": NotRequired[VolumeTypeType],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "MultiAttachEnabled": NotRequired[bool],
        "Throughput": NotRequired[int],
        "ClientToken": NotRequired[str],
    },
)
CreateVpcEndpointRequestRequestTypeDef = TypedDict(
    "CreateVpcEndpointRequestRequestTypeDef",
    {
        "VpcId": str,
        "ServiceName": str,
        "DryRun": NotRequired[bool],
        "VpcEndpointType": NotRequired[VpcEndpointTypeType],
        "PolicyDocument": NotRequired[str],
        "RouteTableIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "IpAddressType": NotRequired[IpAddressTypeType],
        "DnsOptions": NotRequired[DnsOptionsSpecificationTypeDef],
        "ClientToken": NotRequired[str],
        "PrivateDnsEnabled": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "SubnetConfigurations": NotRequired[Sequence[SubnetConfigurationTypeDef]],
    },
)
CreateVpcEndpointServiceConfigurationRequestRequestTypeDef = TypedDict(
    "CreateVpcEndpointServiceConfigurationRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "AcceptanceRequired": NotRequired[bool],
        "PrivateDnsName": NotRequired[str],
        "NetworkLoadBalancerArns": NotRequired[Sequence[str]],
        "GatewayLoadBalancerArns": NotRequired[Sequence[str]],
        "SupportedIpAddressTypes": NotRequired[Sequence[str]],
        "ClientToken": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "CreateVpcPeeringConnectionRequestRequestTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "PeerOwnerId": NotRequired[str],
        "PeerVpcId": NotRequired[str],
        "PeerRegion": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateVpcPeeringConnectionRequestServiceResourceCreateVpcPeeringConnectionTypeDef = TypedDict(
    "CreateVpcPeeringConnectionRequestServiceResourceCreateVpcPeeringConnectionTypeDef",
    {
        "VpcId": str,
        "DryRun": NotRequired[bool],
        "PeerOwnerId": NotRequired[str],
        "PeerVpcId": NotRequired[str],
        "PeerRegion": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateVpcPeeringConnectionRequestVpcRequestVpcPeeringConnectionTypeDef = TypedDict(
    "CreateVpcPeeringConnectionRequestVpcRequestVpcPeeringConnectionTypeDef",
    {
        "DryRun": NotRequired[bool],
        "PeerOwnerId": NotRequired[str],
        "PeerVpcId": NotRequired[str],
        "PeerRegion": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateVpcRequestRequestTypeDef = TypedDict(
    "CreateVpcRequestRequestTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "AmazonProvidedIpv6CidrBlock": NotRequired[bool],
        "Ipv6Pool": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "Ipv4IpamPoolId": NotRequired[str],
        "Ipv4NetmaskLength": NotRequired[int],
        "Ipv6IpamPoolId": NotRequired[str],
        "Ipv6NetmaskLength": NotRequired[int],
        "DryRun": NotRequired[bool],
        "InstanceTenancy": NotRequired[TenancyType],
        "Ipv6CidrBlockNetworkBorderGroup": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateVpcRequestServiceResourceCreateVpcTypeDef = TypedDict(
    "CreateVpcRequestServiceResourceCreateVpcTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "AmazonProvidedIpv6CidrBlock": NotRequired[bool],
        "Ipv6Pool": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "Ipv4IpamPoolId": NotRequired[str],
        "Ipv4NetmaskLength": NotRequired[int],
        "Ipv6IpamPoolId": NotRequired[str],
        "Ipv6NetmaskLength": NotRequired[int],
        "DryRun": NotRequired[bool],
        "InstanceTenancy": NotRequired[TenancyType],
        "Ipv6CidrBlockNetworkBorderGroup": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateVpnGatewayRequestRequestTypeDef = TypedDict(
    "CreateVpnGatewayRequestRequestTypeDef",
    {
        "Type": Literal["ipsec.1"],
        "AvailabilityZone": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "AmazonSideAsn": NotRequired[int],
        "DryRun": NotRequired[bool],
    },
)
ExportImageRequestRequestTypeDef = TypedDict(
    "ExportImageRequestRequestTypeDef",
    {
        "DiskImageFormat": DiskImageFormatType,
        "ImageId": str,
        "S3ExportLocation": ExportTaskS3LocationRequestTypeDef,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "RoleName": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
ImportKeyPairRequestRequestTypeDef = TypedDict(
    "ImportKeyPairRequestRequestTypeDef",
    {
        "KeyName": str,
        "PublicKeyMaterial": BlobTypeDef,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
ImportKeyPairRequestServiceResourceImportKeyPairTypeDef = TypedDict(
    "ImportKeyPairRequestServiceResourceImportKeyPairTypeDef",
    {
        "KeyName": str,
        "PublicKeyMaterial": BlobTypeDef,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
ProvisionByoipCidrRequestRequestTypeDef = TypedDict(
    "ProvisionByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "CidrAuthorizationContext": NotRequired[CidrAuthorizationContextTypeDef],
        "PubliclyAdvertisable": NotRequired[bool],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "PoolTagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "MultiRegion": NotRequired[bool],
        "NetworkBorderGroup": NotRequired[str],
    },
)
PurchaseCapacityBlockRequestRequestTypeDef = TypedDict(
    "PurchaseCapacityBlockRequestRequestTypeDef",
    {
        "CapacityBlockOfferingId": str,
        "InstancePlatform": CapacityReservationInstancePlatformType,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
PurchaseHostReservationRequestRequestTypeDef = TypedDict(
    "PurchaseHostReservationRequestRequestTypeDef",
    {
        "HostIdSet": Sequence[str],
        "OfferingId": str,
        "ClientToken": NotRequired[str],
        "CurrencyCode": NotRequired[Literal["USD"]],
        "LimitPrice": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
StartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef = TypedDict(
    "StartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "ClientToken": str,
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
StartNetworkInsightsAnalysisRequestRequestTypeDef = TypedDict(
    "StartNetworkInsightsAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsPathId": str,
        "ClientToken": str,
        "AdditionalAccounts": NotRequired[Sequence[str]],
        "FilterInArns": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateTrafficMirrorSessionResultTypeDef = TypedDict(
    "CreateTrafficMirrorSessionResultTypeDef",
    {
        "TrafficMirrorSession": TrafficMirrorSessionTypeDef,
        "ClientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrafficMirrorSessionsResultTypeDef = TypedDict(
    "DescribeTrafficMirrorSessionsResultTypeDef",
    {
        "TrafficMirrorSessions": List[TrafficMirrorSessionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyTrafficMirrorSessionResultTypeDef = TypedDict(
    "ModifyTrafficMirrorSessionResultTypeDef",
    {
        "TrafficMirrorSession": TrafficMirrorSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrafficMirrorTargetResultTypeDef = TypedDict(
    "CreateTrafficMirrorTargetResultTypeDef",
    {
        "TrafficMirrorTarget": TrafficMirrorTargetTypeDef,
        "ClientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrafficMirrorTargetsResultTypeDef = TypedDict(
    "DescribeTrafficMirrorTargetsResultTypeDef",
    {
        "TrafficMirrorTargets": List[TrafficMirrorTargetTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitGatewayPolicyTableResultTypeDef = TypedDict(
    "CreateTransitGatewayPolicyTableResultTypeDef",
    {
        "TransitGatewayPolicyTable": TransitGatewayPolicyTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTransitGatewayPolicyTableResultTypeDef = TypedDict(
    "DeleteTransitGatewayPolicyTableResultTypeDef",
    {
        "TransitGatewayPolicyTable": TransitGatewayPolicyTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTransitGatewayPolicyTablesResultTypeDef = TypedDict(
    "DescribeTransitGatewayPolicyTablesResultTypeDef",
    {
        "TransitGatewayPolicyTables": List[TransitGatewayPolicyTableTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitGatewayRouteTableAnnouncementResultTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableAnnouncementResultTypeDef",
    {
        "TransitGatewayRouteTableAnnouncement": TransitGatewayRouteTableAnnouncementTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTransitGatewayRouteTableAnnouncementResultTypeDef = TypedDict(
    "DeleteTransitGatewayRouteTableAnnouncementResultTypeDef",
    {
        "TransitGatewayRouteTableAnnouncement": TransitGatewayRouteTableAnnouncementTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef",
    {
        "TransitGatewayRouteTableAnnouncements": List[TransitGatewayRouteTableAnnouncementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableResultTypeDef",
    {
        "TransitGatewayRouteTable": TransitGatewayRouteTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTransitGatewayRouteTableResultTypeDef = TypedDict(
    "DeleteTransitGatewayRouteTableResultTypeDef",
    {
        "TransitGatewayRouteTable": TransitGatewayRouteTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTransitGatewayRouteTablesResultTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTablesResultTypeDef",
    {
        "TransitGatewayRouteTables": List[TransitGatewayRouteTableTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateTrunkInterfaceResultTypeDef = TypedDict(
    "AssociateTrunkInterfaceResultTypeDef",
    {
        "InterfaceAssociation": TrunkInterfaceAssociationTypeDef,
        "ClientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrunkInterfaceAssociationsResultTypeDef = TypedDict(
    "DescribeTrunkInterfaceAssociationsResultTypeDef",
    {
        "InterfaceAssociations": List[TrunkInterfaceAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcClassicLinkResultTypeDef = TypedDict(
    "DescribeVpcClassicLinkResultTypeDef",
    {
        "Vpcs": List[VpcClassicLinkTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExplanationTypeDef = TypedDict(
    "ExplanationTypeDef",
    {
        "Acl": NotRequired[AnalysisComponentTypeDef],
        "AclRule": NotRequired[AnalysisAclRuleTypeDef],
        "Address": NotRequired[str],
        "Addresses": NotRequired[List[str]],
        "AttachedTo": NotRequired[AnalysisComponentTypeDef],
        "AvailabilityZones": NotRequired[List[str]],
        "Cidrs": NotRequired[List[str]],
        "Component": NotRequired[AnalysisComponentTypeDef],
        "CustomerGateway": NotRequired[AnalysisComponentTypeDef],
        "Destination": NotRequired[AnalysisComponentTypeDef],
        "DestinationVpc": NotRequired[AnalysisComponentTypeDef],
        "Direction": NotRequired[str],
        "ExplanationCode": NotRequired[str],
        "IngressRouteTable": NotRequired[AnalysisComponentTypeDef],
        "InternetGateway": NotRequired[AnalysisComponentTypeDef],
        "LoadBalancerArn": NotRequired[str],
        "ClassicLoadBalancerListener": NotRequired[AnalysisLoadBalancerListenerTypeDef],
        "LoadBalancerListenerPort": NotRequired[int],
        "LoadBalancerTarget": NotRequired[AnalysisLoadBalancerTargetTypeDef],
        "LoadBalancerTargetGroup": NotRequired[AnalysisComponentTypeDef],
        "LoadBalancerTargetGroups": NotRequired[List[AnalysisComponentTypeDef]],
        "LoadBalancerTargetPort": NotRequired[int],
        "ElasticLoadBalancerListener": NotRequired[AnalysisComponentTypeDef],
        "MissingComponent": NotRequired[str],
        "NatGateway": NotRequired[AnalysisComponentTypeDef],
        "NetworkInterface": NotRequired[AnalysisComponentTypeDef],
        "PacketField": NotRequired[str],
        "VpcPeeringConnection": NotRequired[AnalysisComponentTypeDef],
        "Port": NotRequired[int],
        "PortRanges": NotRequired[List[PortRangeTypeDef]],
        "PrefixList": NotRequired[AnalysisComponentTypeDef],
        "Protocols": NotRequired[List[str]],
        "RouteTableRoute": NotRequired[AnalysisRouteTableRouteTypeDef],
        "RouteTable": NotRequired[AnalysisComponentTypeDef],
        "SecurityGroup": NotRequired[AnalysisComponentTypeDef],
        "SecurityGroupRule": NotRequired[AnalysisSecurityGroupRuleTypeDef],
        "SecurityGroups": NotRequired[List[AnalysisComponentTypeDef]],
        "SourceVpc": NotRequired[AnalysisComponentTypeDef],
        "State": NotRequired[str],
        "Subnet": NotRequired[AnalysisComponentTypeDef],
        "SubnetRouteTable": NotRequired[AnalysisComponentTypeDef],
        "Vpc": NotRequired[AnalysisComponentTypeDef],
        "VpcEndpoint": NotRequired[AnalysisComponentTypeDef],
        "VpnConnection": NotRequired[AnalysisComponentTypeDef],
        "VpnGateway": NotRequired[AnalysisComponentTypeDef],
        "TransitGateway": NotRequired[AnalysisComponentTypeDef],
        "TransitGatewayRouteTable": NotRequired[AnalysisComponentTypeDef],
        "TransitGatewayRouteTableRoute": NotRequired[TransitGatewayRouteTableRouteTypeDef],
        "TransitGatewayAttachment": NotRequired[AnalysisComponentTypeDef],
        "ComponentAccount": NotRequired[str],
        "ComponentRegion": NotRequired[str],
        "FirewallStatelessRule": NotRequired[FirewallStatelessRuleTypeDef],
        "FirewallStatefulRule": NotRequired[FirewallStatefulRuleTypeDef],
    },
)
AdvertiseByoipCidrResultTypeDef = TypedDict(
    "AdvertiseByoipCidrResultTypeDef",
    {
        "ByoipCidr": ByoipCidrTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeprovisionByoipCidrResultTypeDef = TypedDict(
    "DeprovisionByoipCidrResultTypeDef",
    {
        "ByoipCidr": ByoipCidrTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeByoipCidrsResultTypeDef = TypedDict(
    "DescribeByoipCidrsResultTypeDef",
    {
        "ByoipCidrs": List[ByoipCidrTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MoveByoipCidrToIpamResultTypeDef = TypedDict(
    "MoveByoipCidrToIpamResultTypeDef",
    {
        "ByoipCidr": ByoipCidrTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisionByoipCidrResultTypeDef = TypedDict(
    "ProvisionByoipCidrResultTypeDef",
    {
        "ByoipCidr": ByoipCidrTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WithdrawByoipCidrResultTypeDef = TypedDict(
    "WithdrawByoipCidrResultTypeDef",
    {
        "ByoipCidr": ByoipCidrTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeClientVpnTargetNetworksResultTypeDef = TypedDict(
    "DescribeClientVpnTargetNetworksResultTypeDef",
    {
        "ClientVpnTargetNetworks": List[TargetNetworkTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RouteTableTypeDef = TypedDict(
    "RouteTableTypeDef",
    {
        "Associations": NotRequired[List[RouteTableAssociationTypeDef]],
        "PropagatingVgws": NotRequired[List[PropagatingVgwTypeDef]],
        "RouteTableId": NotRequired[str],
        "Routes": NotRequired[List[RouteTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "VpcId": NotRequired[str],
        "OwnerId": NotRequired[str],
    },
)
IntegrateServicesTypeDef = TypedDict(
    "IntegrateServicesTypeDef",
    {
        "AthenaIntegrations": NotRequired[Sequence[AthenaIntegrationTypeDef]],
    },
)
LaunchTemplateInstanceMarketOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
    {
        "MarketType": NotRequired[MarketTypeType],
        "SpotOptions": NotRequired[LaunchTemplateSpotMarketOptionsRequestTypeDef],
    },
)
DescribeScheduledInstanceAvailabilityRequestDescribeScheduledInstanceAvailabilityPaginateTypeDef = TypedDict(
    "DescribeScheduledInstanceAvailabilityRequestDescribeScheduledInstanceAvailabilityPaginateTypeDef",
    {
        "FirstSlotStartTimeRange": SlotDateTimeRangeRequestTypeDef,
        "Recurrence": ScheduledInstanceRecurrenceRequestTypeDef,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxSlotDurationInHours": NotRequired[int],
        "MinSlotDurationInHours": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeScheduledInstanceAvailabilityRequestRequestTypeDef = TypedDict(
    "DescribeScheduledInstanceAvailabilityRequestRequestTypeDef",
    {
        "FirstSlotStartTimeRange": SlotDateTimeRangeRequestTypeDef,
        "Recurrence": ScheduledInstanceRecurrenceRequestTypeDef,
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "MaxSlotDurationInHours": NotRequired[int],
        "MinSlotDurationInHours": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeScheduledInstancesRequestDescribeScheduledInstancesPaginateTypeDef = TypedDict(
    "DescribeScheduledInstancesRequestDescribeScheduledInstancesPaginateTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "ScheduledInstanceIds": NotRequired[Sequence[str]],
        "SlotStartTimeRange": NotRequired[SlotStartTimeRangeRequestTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeScheduledInstancesRequestRequestTypeDef = TypedDict(
    "DescribeScheduledInstancesRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ScheduledInstanceIds": NotRequired[Sequence[str]],
        "SlotStartTimeRange": NotRequired[SlotStartTimeRangeRequestTypeDef],
    },
)
InstanceMarketOptionsRequestTypeDef = TypedDict(
    "InstanceMarketOptionsRequestTypeDef",
    {
        "MarketType": NotRequired[MarketTypeType],
        "SpotOptions": NotRequired[SpotMarketOptionsTypeDef],
    },
)
CreateVpnGatewayResultTypeDef = TypedDict(
    "CreateVpnGatewayResultTypeDef",
    {
        "VpnGateway": VpnGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpnGatewaysResultTypeDef = TypedDict(
    "DescribeVpnGatewaysResultTypeDef",
    {
        "VpnGateways": List[VpnGatewayTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkInterfaceAttachmentResponseTypeDef = TypedDict(
    "NetworkInterfaceAttachmentResponseTypeDef",
    {
        "AttachTime": datetime,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "NetworkCardIndex": int,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "Status": AttachmentStatusType,
        "EnaSrdSpecification": AttachmentEnaSrdSpecificationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkInterfaceAttachmentTypeDef = TypedDict(
    "NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": NotRequired[datetime],
        "AttachmentId": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "DeviceIndex": NotRequired[int],
        "NetworkCardIndex": NotRequired[int],
        "InstanceId": NotRequired[str],
        "InstanceOwnerId": NotRequired[str],
        "Status": NotRequired[AttachmentStatusType],
        "EnaSrdSpecification": NotRequired[AttachmentEnaSrdSpecificationTypeDef],
    },
)
DhcpOptionsTypeDef = TypedDict(
    "DhcpOptionsTypeDef",
    {
        "DhcpConfigurations": NotRequired[List[DhcpConfigurationTypeDef]],
        "DhcpOptionsId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
DescribeClientVpnAuthorizationRulesResultTypeDef = TypedDict(
    "DescribeClientVpnAuthorizationRulesResultTypeDef",
    {
        "AuthorizationRules": List[AuthorizationRuleTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAvailabilityZonesResultTypeDef = TypedDict(
    "DescribeAvailabilityZonesResultTypeDef",
    {
        "AvailabilityZones": List[AvailabilityZoneTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "AutoPlacement": NotRequired[AutoPlacementType],
        "AvailabilityZone": NotRequired[str],
        "AvailableCapacity": NotRequired[AvailableCapacityTypeDef],
        "ClientToken": NotRequired[str],
        "HostId": NotRequired[str],
        "HostProperties": NotRequired[HostPropertiesTypeDef],
        "HostReservationId": NotRequired[str],
        "Instances": NotRequired[List[HostInstanceTypeDef]],
        "State": NotRequired[AllocationStateType],
        "AllocationTime": NotRequired[datetime],
        "ReleaseTime": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
        "HostRecovery": NotRequired[HostRecoveryType],
        "AllowsMultipleInstanceTypes": NotRequired[AllowsMultipleInstanceTypesType],
        "OwnerId": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "MemberOfServiceLinkedResourceGroup": NotRequired[bool],
        "OutpostArn": NotRequired[str],
        "HostMaintenance": NotRequired[HostMaintenanceType],
        "AssetId": NotRequired[str],
    },
)
StorageTypeDef = TypedDict(
    "StorageTypeDef",
    {
        "S3": NotRequired[S3StorageTypeDef],
    },
)
CreateImageRequestInstanceCreateImageTypeDef = TypedDict(
    "CreateImageRequestInstanceCreateImageTypeDef",
    {
        "Name": str,
        "BlockDeviceMappings": NotRequired[Sequence[BlockDeviceMappingTypeDef]],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "NoReboot": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateImageRequestRequestTypeDef = TypedDict(
    "CreateImageRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "BlockDeviceMappings": NotRequired[Sequence[BlockDeviceMappingTypeDef]],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "NoReboot": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
ImageAttributeTypeDef = TypedDict(
    "ImageAttributeTypeDef",
    {
        "BlockDeviceMappings": List[BlockDeviceMappingTypeDef],
        "ImageId": str,
        "LaunchPermissions": List[LaunchPermissionTypeDef],
        "ProductCodes": List[ProductCodeTypeDef],
        "Description": AttributeValueTypeDef,
        "KernelId": AttributeValueTypeDef,
        "RamdiskId": AttributeValueTypeDef,
        "SriovNetSupport": AttributeValueTypeDef,
        "BootMode": AttributeValueTypeDef,
        "TpmSupport": AttributeValueTypeDef,
        "UefiData": AttributeValueTypeDef,
        "LastLaunchedTime": AttributeValueTypeDef,
        "ImdsSupport": AttributeValueTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "Architecture": NotRequired[ArchitectureValuesType],
        "CreationDate": NotRequired[str],
        "ImageId": NotRequired[str],
        "ImageLocation": NotRequired[str],
        "ImageType": NotRequired[ImageTypeValuesType],
        "Public": NotRequired[bool],
        "KernelId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Platform": NotRequired[Literal["Windows"]],
        "PlatformDetails": NotRequired[str],
        "UsageOperation": NotRequired[str],
        "ProductCodes": NotRequired[List[ProductCodeTypeDef]],
        "RamdiskId": NotRequired[str],
        "State": NotRequired[ImageStateType],
        "BlockDeviceMappings": NotRequired[List[BlockDeviceMappingTypeDef]],
        "Description": NotRequired[str],
        "EnaSupport": NotRequired[bool],
        "Hypervisor": NotRequired[HypervisorTypeType],
        "ImageOwnerAlias": NotRequired[str],
        "Name": NotRequired[str],
        "RootDeviceName": NotRequired[str],
        "RootDeviceType": NotRequired[DeviceTypeType],
        "SriovNetSupport": NotRequired[str],
        "StateReason": NotRequired[StateReasonTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "VirtualizationType": NotRequired[VirtualizationTypeType],
        "BootMode": NotRequired[BootModeValuesType],
        "TpmSupport": NotRequired[Literal["v2.0"]],
        "DeprecationTime": NotRequired[str],
        "ImdsSupport": NotRequired[Literal["v2.0"]],
        "SourceInstanceId": NotRequired[str],
    },
)
RegisterImageRequestRequestTypeDef = TypedDict(
    "RegisterImageRequestRequestTypeDef",
    {
        "Name": str,
        "ImageLocation": NotRequired[str],
        "Architecture": NotRequired[ArchitectureValuesType],
        "BlockDeviceMappings": NotRequired[Sequence[BlockDeviceMappingTypeDef]],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "EnaSupport": NotRequired[bool],
        "KernelId": NotRequired[str],
        "BillingProducts": NotRequired[Sequence[str]],
        "RamdiskId": NotRequired[str],
        "RootDeviceName": NotRequired[str],
        "SriovNetSupport": NotRequired[str],
        "VirtualizationType": NotRequired[str],
        "BootMode": NotRequired[BootModeValuesType],
        "TpmSupport": NotRequired[Literal["v2.0"]],
        "UefiData": NotRequired[str],
        "ImdsSupport": NotRequired[Literal["v2.0"]],
    },
)
RegisterImageRequestServiceResourceRegisterImageTypeDef = TypedDict(
    "RegisterImageRequestServiceResourceRegisterImageTypeDef",
    {
        "Name": str,
        "ImageLocation": NotRequired[str],
        "Architecture": NotRequired[ArchitectureValuesType],
        "BlockDeviceMappings": NotRequired[Sequence[BlockDeviceMappingTypeDef]],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
        "EnaSupport": NotRequired[bool],
        "KernelId": NotRequired[str],
        "BillingProducts": NotRequired[Sequence[str]],
        "RamdiskId": NotRequired[str],
        "RootDeviceName": NotRequired[str],
        "SriovNetSupport": NotRequired[str],
        "VirtualizationType": NotRequired[str],
        "BootMode": NotRequired[BootModeValuesType],
        "TpmSupport": NotRequired[Literal["v2.0"]],
        "UefiData": NotRequired[str],
        "ImdsSupport": NotRequired[Literal["v2.0"]],
    },
)
CancelCapacityReservationFleetsResultTypeDef = TypedDict(
    "CancelCapacityReservationFleetsResultTypeDef",
    {
        "SuccessfulFleetCancellations": List[CapacityReservationFleetCancellationStateTypeDef],
        "FailedFleetCancellations": List[FailedCapacityReservationFleetCancellationResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelSpotFleetRequestsResponseTypeDef = TypedDict(
    "CancelSpotFleetRequestsResponseTypeDef",
    {
        "SuccessfulFleetRequests": List[CancelSpotFleetRequestsSuccessItemTypeDef],
        "UnsuccessfulFleetRequests": List[CancelSpotFleetRequestsErrorItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCapacityReservationResultTypeDef = TypedDict(
    "CreateCapacityReservationResultTypeDef",
    {
        "CapacityReservation": CapacityReservationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCapacityReservationsResultTypeDef = TypedDict(
    "DescribeCapacityReservationsResultTypeDef",
    {
        "NextToken": str,
        "CapacityReservations": List[CapacityReservationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PurchaseCapacityBlockResultTypeDef = TypedDict(
    "PurchaseCapacityBlockResultTypeDef",
    {
        "CapacityReservation": CapacityReservationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCapacityReservationFleetsResultTypeDef = TypedDict(
    "DescribeCapacityReservationFleetsResultTypeDef",
    {
        "CapacityReservationFleets": List[CapacityReservationFleetTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyInstanceCapacityReservationAttributesRequestRequestTypeDef = TypedDict(
    "ModifyInstanceCapacityReservationAttributesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "CapacityReservationSpecification": CapacityReservationSpecificationTypeDef,
        "DryRun": NotRequired[bool],
    },
)
DescribeClassicLinkInstancesResultTypeDef = TypedDict(
    "DescribeClassicLinkInstancesResultTypeDef",
    {
        "Instances": List[ClassicLinkInstanceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "CreateClientVpnEndpointRequestRequestTypeDef",
    {
        "ClientCidrBlock": str,
        "ServerCertificateArn": str,
        "AuthenticationOptions": Sequence[ClientVpnAuthenticationRequestTypeDef],
        "ConnectionLogOptions": ConnectionLogOptionsTypeDef,
        "DnsServers": NotRequired[Sequence[str]],
        "TransportProtocol": NotRequired[TransportProtocolType],
        "VpnPort": NotRequired[int],
        "Description": NotRequired[str],
        "SplitTunnel": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
        "SelfServicePortal": NotRequired[SelfServicePortalType],
        "ClientConnectOptions": NotRequired[ClientConnectOptionsTypeDef],
        "SessionTimeoutHours": NotRequired[int],
        "ClientLoginBannerOptions": NotRequired[ClientLoginBannerOptionsTypeDef],
    },
)
ClientVpnEndpointTypeDef = TypedDict(
    "ClientVpnEndpointTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[ClientVpnEndpointStatusTypeDef],
        "CreationTime": NotRequired[str],
        "DeletionTime": NotRequired[str],
        "DnsName": NotRequired[str],
        "ClientCidrBlock": NotRequired[str],
        "DnsServers": NotRequired[List[str]],
        "SplitTunnel": NotRequired[bool],
        "VpnProtocol": NotRequired[Literal["openvpn"]],
        "TransportProtocol": NotRequired[TransportProtocolType],
        "VpnPort": NotRequired[int],
        "AssociatedTargetNetworks": NotRequired[List[AssociatedTargetNetworkTypeDef]],
        "ServerCertificateArn": NotRequired[str],
        "AuthenticationOptions": NotRequired[List[ClientVpnAuthenticationTypeDef]],
        "ConnectionLogOptions": NotRequired[ConnectionLogResponseOptionsTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "SecurityGroupIds": NotRequired[List[str]],
        "VpcId": NotRequired[str],
        "SelfServicePortalUrl": NotRequired[str],
        "ClientConnectOptions": NotRequired[ClientConnectResponseOptionsTypeDef],
        "SessionTimeoutHours": NotRequired[int],
        "ClientLoginBannerOptions": NotRequired[ClientLoginBannerResponseOptionsTypeDef],
    },
)
DescribeClientVpnConnectionsResultTypeDef = TypedDict(
    "DescribeClientVpnConnectionsResultTypeDef",
    {
        "Connections": List[ClientVpnConnectionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TerminateClientVpnConnectionsResultTypeDef = TypedDict(
    "TerminateClientVpnConnectionsResultTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Username": str,
        "ConnectionStatuses": List[TerminateConnectionStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeClientVpnRoutesResultTypeDef = TypedDict(
    "DescribeClientVpnRoutesResultTypeDef",
    {
        "Routes": List[ClientVpnRouteTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpnTunnelOptionsSpecificationTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsSpecificationTypeDef",
    {
        "TunnelInsideCidr": NotRequired[str],
        "TunnelInsideIpv6Cidr": NotRequired[str],
        "PreSharedKey": NotRequired[str],
        "Phase1LifetimeSeconds": NotRequired[int],
        "Phase2LifetimeSeconds": NotRequired[int],
        "RekeyMarginTimeSeconds": NotRequired[int],
        "RekeyFuzzPercentage": NotRequired[int],
        "ReplayWindowSize": NotRequired[int],
        "DPDTimeoutSeconds": NotRequired[int],
        "DPDTimeoutAction": NotRequired[str],
        "Phase1EncryptionAlgorithms": NotRequired[
            Sequence[Phase1EncryptionAlgorithmsRequestListValueTypeDef]
        ],
        "Phase2EncryptionAlgorithms": NotRequired[
            Sequence[Phase2EncryptionAlgorithmsRequestListValueTypeDef]
        ],
        "Phase1IntegrityAlgorithms": NotRequired[
            Sequence[Phase1IntegrityAlgorithmsRequestListValueTypeDef]
        ],
        "Phase2IntegrityAlgorithms": NotRequired[
            Sequence[Phase2IntegrityAlgorithmsRequestListValueTypeDef]
        ],
        "Phase1DHGroupNumbers": NotRequired[Sequence[Phase1DHGroupNumbersRequestListValueTypeDef]],
        "Phase2DHGroupNumbers": NotRequired[Sequence[Phase2DHGroupNumbersRequestListValueTypeDef]],
        "IKEVersions": NotRequired[Sequence[IKEVersionsRequestListValueTypeDef]],
        "StartupAction": NotRequired[str],
        "LogOptions": NotRequired[VpnTunnelLogOptionsSpecificationTypeDef],
        "EnableTunnelLifecycleControl": NotRequired[bool],
    },
)
VpnTunnelOptionsSpecificationTypeDef = TypedDict(
    "VpnTunnelOptionsSpecificationTypeDef",
    {
        "TunnelInsideCidr": NotRequired[str],
        "TunnelInsideIpv6Cidr": NotRequired[str],
        "PreSharedKey": NotRequired[str],
        "Phase1LifetimeSeconds": NotRequired[int],
        "Phase2LifetimeSeconds": NotRequired[int],
        "RekeyMarginTimeSeconds": NotRequired[int],
        "RekeyFuzzPercentage": NotRequired[int],
        "ReplayWindowSize": NotRequired[int],
        "DPDTimeoutSeconds": NotRequired[int],
        "DPDTimeoutAction": NotRequired[str],
        "Phase1EncryptionAlgorithms": NotRequired[
            Sequence[Phase1EncryptionAlgorithmsRequestListValueTypeDef]
        ],
        "Phase2EncryptionAlgorithms": NotRequired[
            Sequence[Phase2EncryptionAlgorithmsRequestListValueTypeDef]
        ],
        "Phase1IntegrityAlgorithms": NotRequired[
            Sequence[Phase1IntegrityAlgorithmsRequestListValueTypeDef]
        ],
        "Phase2IntegrityAlgorithms": NotRequired[
            Sequence[Phase2IntegrityAlgorithmsRequestListValueTypeDef]
        ],
        "Phase1DHGroupNumbers": NotRequired[Sequence[Phase1DHGroupNumbersRequestListValueTypeDef]],
        "Phase2DHGroupNumbers": NotRequired[Sequence[Phase2DHGroupNumbersRequestListValueTypeDef]],
        "IKEVersions": NotRequired[Sequence[IKEVersionsRequestListValueTypeDef]],
        "StartupAction": NotRequired[str],
        "LogOptions": NotRequired[VpnTunnelLogOptionsSpecificationTypeDef],
        "EnableTunnelLifecycleControl": NotRequired[bool],
    },
)
TunnelOptionTypeDef = TypedDict(
    "TunnelOptionTypeDef",
    {
        "OutsideIpAddress": NotRequired[str],
        "TunnelInsideCidr": NotRequired[str],
        "TunnelInsideIpv6Cidr": NotRequired[str],
        "PreSharedKey": NotRequired[str],
        "Phase1LifetimeSeconds": NotRequired[int],
        "Phase2LifetimeSeconds": NotRequired[int],
        "RekeyMarginTimeSeconds": NotRequired[int],
        "RekeyFuzzPercentage": NotRequired[int],
        "ReplayWindowSize": NotRequired[int],
        "DpdTimeoutSeconds": NotRequired[int],
        "DpdTimeoutAction": NotRequired[str],
        "Phase1EncryptionAlgorithms": NotRequired[List[Phase1EncryptionAlgorithmsListValueTypeDef]],
        "Phase2EncryptionAlgorithms": NotRequired[List[Phase2EncryptionAlgorithmsListValueTypeDef]],
        "Phase1IntegrityAlgorithms": NotRequired[List[Phase1IntegrityAlgorithmsListValueTypeDef]],
        "Phase2IntegrityAlgorithms": NotRequired[List[Phase2IntegrityAlgorithmsListValueTypeDef]],
        "Phase1DHGroupNumbers": NotRequired[List[Phase1DHGroupNumbersListValueTypeDef]],
        "Phase2DHGroupNumbers": NotRequired[List[Phase2DHGroupNumbersListValueTypeDef]],
        "IkeVersions": NotRequired[List[IKEVersionsListValueTypeDef]],
        "StartupAction": NotRequired[str],
        "LogOptions": NotRequired[VpnTunnelLogOptionsTypeDef],
        "EnableTunnelLifecycleControl": NotRequired[bool],
    },
)
NetworkAclTypeDef = TypedDict(
    "NetworkAclTypeDef",
    {
        "Associations": NotRequired[List[NetworkAclAssociationTypeDef]],
        "Entries": NotRequired[List[NetworkAclEntryTypeDef]],
        "IsDefault": NotRequired[bool],
        "NetworkAclId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "VpcId": NotRequired[str],
        "OwnerId": NotRequired[str],
    },
)
ModifySnapshotAttributeRequestRequestTypeDef = TypedDict(
    "ModifySnapshotAttributeRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "Attribute": NotRequired[SnapshotAttributeNameType],
        "CreateVolumePermission": NotRequired[CreateVolumePermissionModificationsTypeDef],
        "GroupNames": NotRequired[Sequence[str]],
        "OperationType": NotRequired[OperationTypeType],
        "UserIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
ModifySnapshotAttributeRequestSnapshotModifyAttributeTypeDef = TypedDict(
    "ModifySnapshotAttributeRequestSnapshotModifyAttributeTypeDef",
    {
        "Attribute": NotRequired[SnapshotAttributeNameType],
        "CreateVolumePermission": NotRequired[CreateVolumePermissionModificationsTypeDef],
        "GroupNames": NotRequired[Sequence[str]],
        "OperationType": NotRequired[OperationTypeType],
        "UserIds": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
GetAwsNetworkPerformanceDataResultTypeDef = TypedDict(
    "GetAwsNetworkPerformanceDataResultTypeDef",
    {
        "DataResponses": List[DataResponseTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFleetsResultTypeDef = TypedDict(
    "DeleteFleetsResultTypeDef",
    {
        "SuccessfulFleetDeletions": List[DeleteFleetSuccessItemTypeDef],
        "UnsuccessfulFleetDeletions": List[DeleteFleetErrorItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLaunchTemplateVersionsResultTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResultTypeDef",
    {
        "SuccessfullyDeletedLaunchTemplateVersions": List[
            DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef
        ],
        "UnsuccessfullyDeletedLaunchTemplateVersions": List[
            DeleteLaunchTemplateVersionsResponseErrorItemTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteQueuedReservedInstancesResultTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesResultTypeDef",
    {
        "SuccessfulQueuedPurchaseDeletions": List[SuccessfulQueuedPurchaseDeletionTypeDef],
        "FailedQueuedPurchaseDeletions": List[FailedQueuedPurchaseDeletionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePrincipalIdFormatResultTypeDef = TypedDict(
    "DescribePrincipalIdFormatResultTypeDef",
    {
        "Principals": List[PrincipalIdFormatTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFastLaunchImagesResultTypeDef = TypedDict(
    "DescribeFastLaunchImagesResultTypeDef",
    {
        "FastLaunchImages": List[DescribeFastLaunchImagesSuccessItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFlowLogsResultTypeDef = TypedDict(
    "DescribeFlowLogsResultTypeDef",
    {
        "FlowLogs": List[FlowLogTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableFastSnapshotRestoreErrorItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreErrorItemTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "FastSnapshotRestoreStateErrors": NotRequired[
            List[DisableFastSnapshotRestoreStateErrorItemTypeDef]
        ],
    },
)
ImportInstanceTaskDetailsTypeDef = TypedDict(
    "ImportInstanceTaskDetailsTypeDef",
    {
        "Description": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Platform": NotRequired[Literal["Windows"]],
        "Volumes": NotRequired[List[ImportInstanceVolumeDetailItemTypeDef]],
    },
)
DescribeVpcEndpointConnectionsResultTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionsResultTypeDef",
    {
        "VpcEndpointConnections": List[VpcEndpointConnectionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyInstanceAttributeRequestInstanceModifyAttributeTypeDef = TypedDict(
    "ModifyInstanceAttributeRequestInstanceModifyAttributeTypeDef",
    {
        "SourceDestCheck": NotRequired[AttributeBooleanValueTypeDef],
        "Attribute": NotRequired[InstanceAttributeNameType],
        "BlockDeviceMappings": NotRequired[
            Sequence[InstanceBlockDeviceMappingSpecificationTypeDef]
        ],
        "DisableApiTermination": NotRequired[AttributeBooleanValueTypeDef],
        "DryRun": NotRequired[bool],
        "EbsOptimized": NotRequired[AttributeBooleanValueTypeDef],
        "EnaSupport": NotRequired[AttributeBooleanValueTypeDef],
        "Groups": NotRequired[Sequence[str]],
        "InstanceInitiatedShutdownBehavior": NotRequired[AttributeValueTypeDef],
        "InstanceType": NotRequired[AttributeValueTypeDef],
        "Kernel": NotRequired[AttributeValueTypeDef],
        "Ramdisk": NotRequired[AttributeValueTypeDef],
        "SriovNetSupport": NotRequired[AttributeValueTypeDef],
        "UserData": NotRequired[BlobAttributeValueTypeDef],
        "Value": NotRequired[str],
        "DisableApiStop": NotRequired[AttributeBooleanValueTypeDef],
    },
)
ModifyInstanceAttributeRequestRequestTypeDef = TypedDict(
    "ModifyInstanceAttributeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SourceDestCheck": NotRequired[AttributeBooleanValueTypeDef],
        "Attribute": NotRequired[InstanceAttributeNameType],
        "BlockDeviceMappings": NotRequired[
            Sequence[InstanceBlockDeviceMappingSpecificationTypeDef]
        ],
        "DisableApiTermination": NotRequired[AttributeBooleanValueTypeDef],
        "DryRun": NotRequired[bool],
        "EbsOptimized": NotRequired[AttributeBooleanValueTypeDef],
        "EnaSupport": NotRequired[AttributeBooleanValueTypeDef],
        "Groups": NotRequired[Sequence[str]],
        "InstanceInitiatedShutdownBehavior": NotRequired[AttributeValueTypeDef],
        "InstanceType": NotRequired[AttributeValueTypeDef],
        "Kernel": NotRequired[AttributeValueTypeDef],
        "Ramdisk": NotRequired[AttributeValueTypeDef],
        "SriovNetSupport": NotRequired[AttributeValueTypeDef],
        "UserData": NotRequired[BlobAttributeValueTypeDef],
        "Value": NotRequired[str],
        "DisableApiStop": NotRequired[AttributeBooleanValueTypeDef],
    },
)
InstanceAttributeTypeDef = TypedDict(
    "InstanceAttributeTypeDef",
    {
        "Groups": List[GroupIdentifierTypeDef],
        "BlockDeviceMappings": List[InstanceBlockDeviceMappingTypeDef],
        "DisableApiTermination": AttributeBooleanValueTypeDef,
        "EnaSupport": AttributeBooleanValueTypeDef,
        "EnclaveOptions": EnclaveOptionsTypeDef,
        "EbsOptimized": AttributeBooleanValueTypeDef,
        "InstanceId": str,
        "InstanceInitiatedShutdownBehavior": AttributeValueTypeDef,
        "InstanceType": AttributeValueTypeDef,
        "KernelId": AttributeValueTypeDef,
        "ProductCodes": List[ProductCodeTypeDef],
        "RamdiskId": AttributeValueTypeDef,
        "RootDeviceName": AttributeValueTypeDef,
        "SourceDestCheck": AttributeBooleanValueTypeDef,
        "SriovNetSupport": AttributeValueTypeDef,
        "UserData": AttributeValueTypeDef,
        "DisableApiStop": AttributeBooleanValueTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEgressOnlyInternetGatewayResultTypeDef = TypedDict(
    "CreateEgressOnlyInternetGatewayResultTypeDef",
    {
        "ClientToken": str,
        "EgressOnlyInternetGateway": EgressOnlyInternetGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEgressOnlyInternetGatewaysResultTypeDef = TypedDict(
    "DescribeEgressOnlyInternetGatewaysResultTypeDef",
    {
        "EgressOnlyInternetGateways": List[EgressOnlyInternetGatewayTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInternetGatewayResultTypeDef = TypedDict(
    "CreateInternetGatewayResultTypeDef",
    {
        "InternetGateway": InternetGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInternetGatewaysResultTypeDef = TypedDict(
    "DescribeInternetGatewaysResultTypeDef",
    {
        "InternetGateways": List[InternetGatewayTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeElasticGpusResultTypeDef = TypedDict(
    "DescribeElasticGpusResultTypeDef",
    {
        "ElasticGpuSet": List[ElasticGpusTypeDef],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceNetworkInterfaceSpecificationServiceResourceTypeDef = TypedDict(
    "InstanceNetworkInterfaceSpecificationServiceResourceTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[Sequence[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[InstanceIpv6AddressTypeDef]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[Sequence[PrivateIpAddressSpecificationTypeDef]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
        "AssociateCarrierIpAddress": NotRequired[bool],
        "InterfaceType": NotRequired[str],
        "NetworkCardIndex": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence[Ipv4PrefixSpecificationRequestTypeDef]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence[Ipv6PrefixSpecificationRequestTypeDef]],
        "Ipv6PrefixCount": NotRequired[int],
        "PrimaryIpv6": NotRequired[bool],
        "EnaSrdSpecification": NotRequired[EnaSrdSpecificationRequestTypeDef],
        "ConnectionTrackingSpecification": NotRequired[
            ConnectionTrackingSpecificationRequestTypeDef
        ],
    },
)
InstanceNetworkInterfaceSpecificationSubnetTypeDef = TypedDict(
    "InstanceNetworkInterfaceSpecificationSubnetTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[Sequence[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[InstanceIpv6AddressTypeDef]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[Sequence[PrivateIpAddressSpecificationTypeDef]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
        "AssociateCarrierIpAddress": NotRequired[bool],
        "InterfaceType": NotRequired[str],
        "NetworkCardIndex": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence[Ipv4PrefixSpecificationRequestTypeDef]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence[Ipv6PrefixSpecificationRequestTypeDef]],
        "Ipv6PrefixCount": NotRequired[int],
        "PrimaryIpv6": NotRequired[bool],
        "EnaSrdSpecification": NotRequired[EnaSrdSpecificationRequestTypeDef],
        "ConnectionTrackingSpecification": NotRequired[
            ConnectionTrackingSpecificationRequestTypeDef
        ],
    },
)
InstanceNetworkInterfaceSpecificationTypeDef = TypedDict(
    "InstanceNetworkInterfaceSpecificationTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[List[str]],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[List[InstanceIpv6AddressTypeDef]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[List[PrivateIpAddressSpecificationTypeDef]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
        "AssociateCarrierIpAddress": NotRequired[bool],
        "InterfaceType": NotRequired[str],
        "NetworkCardIndex": NotRequired[int],
        "Ipv4Prefixes": NotRequired[List[Ipv4PrefixSpecificationRequestTypeDef]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[List[Ipv6PrefixSpecificationRequestTypeDef]],
        "Ipv6PrefixCount": NotRequired[int],
        "PrimaryIpv6": NotRequired[bool],
        "EnaSrdSpecification": NotRequired[EnaSrdSpecificationRequestTypeDef],
        "ConnectionTrackingSpecification": NotRequired[
            ConnectionTrackingSpecificationRequestTypeDef
        ],
    },
)
LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef",
    {
        "AssociateCarrierIpAddress": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[Sequence[str]],
        "InterfaceType": NotRequired[str],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[InstanceIpv6AddressRequestTypeDef]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[Sequence[PrivateIpAddressSpecificationTypeDef]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
        "NetworkCardIndex": NotRequired[int],
        "Ipv4Prefixes": NotRequired[Sequence[Ipv4PrefixSpecificationRequestTypeDef]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[Sequence[Ipv6PrefixSpecificationRequestTypeDef]],
        "Ipv6PrefixCount": NotRequired[int],
        "PrimaryIpv6": NotRequired[bool],
        "EnaSrdSpecification": NotRequired[EnaSrdSpecificationRequestTypeDef],
        "ConnectionTrackingSpecification": NotRequired[
            ConnectionTrackingSpecificationRequestTypeDef
        ],
    },
)
AttachNetworkInterfaceRequestNetworkInterfaceAttachTypeDef = TypedDict(
    "AttachNetworkInterfaceRequestNetworkInterfaceAttachTypeDef",
    {
        "DeviceIndex": int,
        "InstanceId": str,
        "DryRun": NotRequired[bool],
        "NetworkCardIndex": NotRequired[int],
        "EnaSrdSpecification": NotRequired[EnaSrdSpecificationTypeDef],
    },
)
AttachNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "AttachNetworkInterfaceRequestRequestTypeDef",
    {
        "DeviceIndex": int,
        "InstanceId": str,
        "NetworkInterfaceId": str,
        "DryRun": NotRequired[bool],
        "NetworkCardIndex": NotRequired[int],
        "EnaSrdSpecification": NotRequired[EnaSrdSpecificationTypeDef],
    },
)
ModifyNetworkInterfaceAttributeRequestNetworkInterfaceModifyAttributeTypeDef = TypedDict(
    "ModifyNetworkInterfaceAttributeRequestNetworkInterfaceModifyAttributeTypeDef",
    {
        "Attachment": NotRequired[NetworkInterfaceAttachmentChangesTypeDef],
        "Description": NotRequired[AttributeValueTypeDef],
        "DryRun": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "SourceDestCheck": NotRequired[AttributeBooleanValueTypeDef],
        "EnaSrdSpecification": NotRequired[EnaSrdSpecificationTypeDef],
        "EnablePrimaryIpv6": NotRequired[bool],
        "ConnectionTrackingSpecification": NotRequired[
            ConnectionTrackingSpecificationRequestTypeDef
        ],
    },
)
ModifyNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "ModifyNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Attachment": NotRequired[NetworkInterfaceAttachmentChangesTypeDef],
        "Description": NotRequired[AttributeValueTypeDef],
        "DryRun": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "SourceDestCheck": NotRequired[AttributeBooleanValueTypeDef],
        "EnaSrdSpecification": NotRequired[EnaSrdSpecificationTypeDef],
        "EnablePrimaryIpv6": NotRequired[bool],
        "ConnectionTrackingSpecification": NotRequired[
            ConnectionTrackingSpecificationRequestTypeDef
        ],
    },
)
EnableFastSnapshotRestoreErrorItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreErrorItemTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "FastSnapshotRestoreStateErrors": NotRequired[
            List[EnableFastSnapshotRestoreStateErrorItemTypeDef]
        ],
    },
)
DescribeFleetHistoryResultTypeDef = TypedDict(
    "DescribeFleetHistoryResultTypeDef",
    {
        "HistoryRecords": List[HistoryRecordEntryTypeDef],
        "LastEvaluatedTime": datetime,
        "NextToken": str,
        "FleetId": str,
        "StartTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSpotFleetRequestHistoryResponseTypeDef = TypedDict(
    "DescribeSpotFleetRequestHistoryResponseTypeDef",
    {
        "HistoryRecords": List[HistoryRecordTypeDef],
        "LastEvaluatedTime": datetime,
        "NextToken": str,
        "SpotFleetRequestId": str,
        "StartTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeExportImageTasksResultTypeDef = TypedDict(
    "DescribeExportImageTasksResultTypeDef",
    {
        "ExportImageTasks": List[ExportImageTaskTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceExportTaskResultTypeDef = TypedDict(
    "CreateInstanceExportTaskResultTypeDef",
    {
        "ExportTask": ExportTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeExportTasksResultTypeDef = TypedDict(
    "DescribeExportTasksResultTypeDef",
    {
        "ExportTasks": List[ExportTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkInsightsPathTypeDef = TypedDict(
    "NetworkInsightsPathTypeDef",
    {
        "NetworkInsightsPathId": NotRequired[str],
        "NetworkInsightsPathArn": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "Source": NotRequired[str],
        "Destination": NotRequired[str],
        "SourceArn": NotRequired[str],
        "DestinationArn": NotRequired[str],
        "SourceIp": NotRequired[str],
        "DestinationIp": NotRequired[str],
        "Protocol": NotRequired[ProtocolType],
        "DestinationPort": NotRequired[int],
        "Tags": NotRequired[List[TagTypeDef]],
        "FilterAtSource": NotRequired[PathFilterTypeDef],
        "FilterAtDestination": NotRequired[PathFilterTypeDef],
    },
)
SpotOptionsRequestTypeDef = TypedDict(
    "SpotOptionsRequestTypeDef",
    {
        "AllocationStrategy": NotRequired[SpotAllocationStrategyType],
        "MaintenanceStrategies": NotRequired[FleetSpotMaintenanceStrategiesRequestTypeDef],
        "InstanceInterruptionBehavior": NotRequired[SpotInstanceInterruptionBehaviorType],
        "InstancePoolsToUseCount": NotRequired[int],
        "SingleInstanceType": NotRequired[bool],
        "SingleAvailabilityZone": NotRequired[bool],
        "MinTargetCapacity": NotRequired[int],
        "MaxTotalPrice": NotRequired[str],
    },
)
SpotOptionsTypeDef = TypedDict(
    "SpotOptionsTypeDef",
    {
        "AllocationStrategy": NotRequired[SpotAllocationStrategyType],
        "MaintenanceStrategies": NotRequired[FleetSpotMaintenanceStrategiesTypeDef],
        "InstanceInterruptionBehavior": NotRequired[SpotInstanceInterruptionBehaviorType],
        "InstancePoolsToUseCount": NotRequired[int],
        "SingleInstanceType": NotRequired[bool],
        "SingleAvailabilityZone": NotRequired[bool],
        "MinTargetCapacity": NotRequired[int],
        "MaxTotalPrice": NotRequired[str],
    },
)
FpgaInfoTypeDef = TypedDict(
    "FpgaInfoTypeDef",
    {
        "Fpgas": NotRequired[List[FpgaDeviceInfoTypeDef]],
        "TotalFpgaMemoryInMiB": NotRequired[int],
    },
)
DescribeFpgaImageAttributeResultTypeDef = TypedDict(
    "DescribeFpgaImageAttributeResultTypeDef",
    {
        "FpgaImageAttribute": FpgaImageAttributeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyFpgaImageAttributeResultTypeDef = TypedDict(
    "ModifyFpgaImageAttributeResultTypeDef",
    {
        "FpgaImageAttribute": FpgaImageAttributeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFpgaImagesResultTypeDef = TypedDict(
    "DescribeFpgaImagesResultTypeDef",
    {
        "FpgaImages": List[FpgaImageTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GpuInfoTypeDef = TypedDict(
    "GpuInfoTypeDef",
    {
        "Gpus": NotRequired[List[GpuDeviceInfoTypeDef]],
        "TotalGpuMemoryInMiB": NotRequired[int],
    },
)
AssociateIamInstanceProfileResultTypeDef = TypedDict(
    "AssociateIamInstanceProfileResultTypeDef",
    {
        "IamInstanceProfileAssociation": IamInstanceProfileAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIamInstanceProfileAssociationsResultTypeDef = TypedDict(
    "DescribeIamInstanceProfileAssociationsResultTypeDef",
    {
        "IamInstanceProfileAssociations": List[IamInstanceProfileAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateIamInstanceProfileResultTypeDef = TypedDict(
    "DisassociateIamInstanceProfileResultTypeDef",
    {
        "IamInstanceProfileAssociation": IamInstanceProfileAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplaceIamInstanceProfileAssociationResultTypeDef = TypedDict(
    "ReplaceIamInstanceProfileAssociationResultTypeDef",
    {
        "IamInstanceProfileAssociation": IamInstanceProfileAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyImageAttributeRequestImageModifyAttributeTypeDef = TypedDict(
    "ModifyImageAttributeRequestImageModifyAttributeTypeDef",
    {
        "Attribute": NotRequired[str],
        "Description": NotRequired[AttributeValueTypeDef],
        "LaunchPermission": NotRequired[LaunchPermissionModificationsTypeDef],
        "OperationType": NotRequired[OperationTypeType],
        "ProductCodes": NotRequired[Sequence[str]],
        "UserGroups": NotRequired[Sequence[str]],
        "UserIds": NotRequired[Sequence[str]],
        "Value": NotRequired[str],
        "DryRun": NotRequired[bool],
        "OrganizationArns": NotRequired[Sequence[str]],
        "OrganizationalUnitArns": NotRequired[Sequence[str]],
        "ImdsSupport": NotRequired[AttributeValueTypeDef],
    },
)
ModifyImageAttributeRequestRequestTypeDef = TypedDict(
    "ModifyImageAttributeRequestRequestTypeDef",
    {
        "ImageId": str,
        "Attribute": NotRequired[str],
        "Description": NotRequired[AttributeValueTypeDef],
        "LaunchPermission": NotRequired[LaunchPermissionModificationsTypeDef],
        "OperationType": NotRequired[OperationTypeType],
        "ProductCodes": NotRequired[Sequence[str]],
        "UserGroups": NotRequired[Sequence[str]],
        "UserIds": NotRequired[Sequence[str]],
        "Value": NotRequired[str],
        "DryRun": NotRequired[bool],
        "OrganizationArns": NotRequired[Sequence[str]],
        "OrganizationalUnitArns": NotRequired[Sequence[str]],
        "ImdsSupport": NotRequired[AttributeValueTypeDef],
    },
)
ImportImageRequestRequestTypeDef = TypedDict(
    "ImportImageRequestRequestTypeDef",
    {
        "Architecture": NotRequired[str],
        "ClientData": NotRequired[ClientDataTypeDef],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "DiskContainers": NotRequired[Sequence[ImageDiskContainerTypeDef]],
        "DryRun": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "Hypervisor": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "LicenseType": NotRequired[str],
        "Platform": NotRequired[str],
        "RoleName": NotRequired[str],
        "LicenseSpecifications": NotRequired[
            Sequence[ImportImageLicenseConfigurationRequestTypeDef]
        ],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "UsageOperation": NotRequired[str],
        "BootMode": NotRequired[BootModeValuesType],
    },
)
ImportSnapshotRequestRequestTypeDef = TypedDict(
    "ImportSnapshotRequestRequestTypeDef",
    {
        "ClientData": NotRequired[ClientDataTypeDef],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "DiskContainer": NotRequired[SnapshotDiskContainerTypeDef],
        "DryRun": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "RoleName": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
ImportInstanceRequestRequestTypeDef = TypedDict(
    "ImportInstanceRequestRequestTypeDef",
    {
        "Platform": Literal["Windows"],
        "Description": NotRequired[str],
        "DiskImages": NotRequired[Sequence[DiskImageTypeDef]],
        "DryRun": NotRequired[bool],
        "LaunchSpecification": NotRequired[ImportInstanceLaunchSpecificationTypeDef],
    },
)
InferenceAcceleratorInfoTypeDef = TypedDict(
    "InferenceAcceleratorInfoTypeDef",
    {
        "Accelerators": NotRequired[List[InferenceDeviceInfoTypeDef]],
        "TotalInferenceMemoryInMiB": NotRequired[int],
    },
)
InstanceNetworkInterfaceAttachmentTypeDef = TypedDict(
    "InstanceNetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": NotRequired[datetime],
        "AttachmentId": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "DeviceIndex": NotRequired[int],
        "Status": NotRequired[AttachmentStatusType],
        "NetworkCardIndex": NotRequired[int],
        "EnaSrdSpecification": NotRequired[InstanceAttachmentEnaSrdSpecificationTypeDef],
    },
)
MonitorInstancesResultTypeDef = TypedDict(
    "MonitorInstancesResultTypeDef",
    {
        "InstanceMonitorings": List[InstanceMonitoringTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UnmonitorInstancesResultTypeDef = TypedDict(
    "UnmonitorInstancesResultTypeDef",
    {
        "InstanceMonitorings": List[InstanceMonitoringTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FleetLaunchTemplateOverridesRequestTypeDef = TypedDict(
    "FleetLaunchTemplateOverridesRequestTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "MaxPrice": NotRequired[str],
        "SubnetId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "WeightedCapacity": NotRequired[float],
        "Priority": NotRequired[float],
        "Placement": NotRequired[PlacementTypeDef],
        "InstanceRequirements": NotRequired[InstanceRequirementsRequestTypeDef],
        "ImageId": NotRequired[str],
    },
)
GetInstanceTypesFromInstanceRequirementsRequestGetInstanceTypesFromInstanceRequirementsPaginateTypeDef = TypedDict(
    "GetInstanceTypesFromInstanceRequirementsRequestGetInstanceTypesFromInstanceRequirementsPaginateTypeDef",
    {
        "ArchitectureTypes": Sequence[ArchitectureTypeType],
        "VirtualizationTypes": Sequence[VirtualizationTypeType],
        "InstanceRequirements": InstanceRequirementsRequestTypeDef,
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef = TypedDict(
    "GetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef",
    {
        "ArchitectureTypes": Sequence[ArchitectureTypeType],
        "VirtualizationTypes": Sequence[VirtualizationTypeType],
        "InstanceRequirements": InstanceRequirementsRequestTypeDef,
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
InstanceRequirementsWithMetadataRequestTypeDef = TypedDict(
    "InstanceRequirementsWithMetadataRequestTypeDef",
    {
        "ArchitectureTypes": NotRequired[Sequence[ArchitectureTypeType]],
        "VirtualizationTypes": NotRequired[Sequence[VirtualizationTypeType]],
        "InstanceRequirements": NotRequired[InstanceRequirementsRequestTypeDef],
    },
)
FleetLaunchTemplateOverridesTypeDef = TypedDict(
    "FleetLaunchTemplateOverridesTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "MaxPrice": NotRequired[str],
        "SubnetId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "WeightedCapacity": NotRequired[float],
        "Priority": NotRequired[float],
        "Placement": NotRequired[PlacementResponseTypeDef],
        "InstanceRequirements": NotRequired[InstanceRequirementsTypeDef],
        "ImageId": NotRequired[str],
    },
)
LaunchTemplateOverridesTypeDef = TypedDict(
    "LaunchTemplateOverridesTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "SpotPrice": NotRequired[str],
        "SubnetId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "WeightedCapacity": NotRequired[float],
        "Priority": NotRequired[float],
        "InstanceRequirements": NotRequired[InstanceRequirementsTypeDef],
    },
)
StartInstancesResultTypeDef = TypedDict(
    "StartInstancesResultTypeDef",
    {
        "StartingInstances": List[InstanceStateChangeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopInstancesResultTypeDef = TypedDict(
    "StopInstancesResultTypeDef",
    {
        "StoppingInstances": List[InstanceStateChangeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TerminateInstancesResultTypeDef = TypedDict(
    "TerminateInstancesResultTypeDef",
    {
        "TerminatingInstances": List[InstanceStateChangeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceStatusTypeDef = TypedDict(
    "InstanceStatusTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Events": NotRequired[List[InstanceStatusEventTypeDef]],
        "InstanceId": NotRequired[str],
        "InstanceState": NotRequired[InstanceStateTypeDef],
        "InstanceStatus": NotRequired[InstanceStatusSummaryTypeDef],
        "SystemStatus": NotRequired[InstanceStatusSummaryTypeDef],
    },
)
SecurityGroupPaginatorTypeDef = TypedDict(
    "SecurityGroupPaginatorTypeDef",
    {
        "Description": NotRequired[str],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[List[IpPermissionPaginatorTypeDef]],
        "OwnerId": NotRequired[str],
        "GroupId": NotRequired[str],
        "IpPermissionsEgress": NotRequired[List[IpPermissionPaginatorTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "VpcId": NotRequired[str],
    },
)
AuthorizeSecurityGroupEgressRequestRequestTypeDef = TypedDict(
    "AuthorizeSecurityGroupEgressRequestRequestTypeDef",
    {
        "GroupId": str,
        "DryRun": NotRequired[bool],
        "IpPermissions": NotRequired[Sequence[IpPermissionTypeDef]],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "ToPort": NotRequired[int],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
    },
)
AuthorizeSecurityGroupEgressRequestSecurityGroupAuthorizeEgressTypeDef = TypedDict(
    "AuthorizeSecurityGroupEgressRequestSecurityGroupAuthorizeEgressTypeDef",
    {
        "DryRun": NotRequired[bool],
        "IpPermissions": NotRequired[Sequence[IpPermissionTypeDef]],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "ToPort": NotRequired[int],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
    },
)
AuthorizeSecurityGroupIngressRequestRequestTypeDef = TypedDict(
    "AuthorizeSecurityGroupIngressRequestRequestTypeDef",
    {
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence[IpPermissionTypeDef]],
        "IpProtocol": NotRequired[str],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
        "ToPort": NotRequired[int],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
AuthorizeSecurityGroupIngressRequestSecurityGroupAuthorizeIngressTypeDef = TypedDict(
    "AuthorizeSecurityGroupIngressRequestSecurityGroupAuthorizeIngressTypeDef",
    {
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence[IpPermissionTypeDef]],
        "IpProtocol": NotRequired[str],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
        "ToPort": NotRequired[int],
        "DryRun": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
RevokeSecurityGroupEgressRequestRequestTypeDef = TypedDict(
    "RevokeSecurityGroupEgressRequestRequestTypeDef",
    {
        "GroupId": str,
        "DryRun": NotRequired[bool],
        "IpPermissions": NotRequired[Sequence[IpPermissionTypeDef]],
        "SecurityGroupRuleIds": NotRequired[Sequence[str]],
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "ToPort": NotRequired[int],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
    },
)
RevokeSecurityGroupEgressRequestSecurityGroupRevokeEgressTypeDef = TypedDict(
    "RevokeSecurityGroupEgressRequestSecurityGroupRevokeEgressTypeDef",
    {
        "DryRun": NotRequired[bool],
        "IpPermissions": NotRequired[Sequence[IpPermissionTypeDef]],
        "SecurityGroupRuleIds": NotRequired[Sequence[str]],
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "IpProtocol": NotRequired[str],
        "ToPort": NotRequired[int],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
    },
)
RevokeSecurityGroupEgressResultTypeDef = TypedDict(
    "RevokeSecurityGroupEgressResultTypeDef",
    {
        "Return": bool,
        "UnknownIpPermissions": List[IpPermissionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RevokeSecurityGroupIngressRequestRequestTypeDef = TypedDict(
    "RevokeSecurityGroupIngressRequestRequestTypeDef",
    {
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence[IpPermissionTypeDef]],
        "IpProtocol": NotRequired[str],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
        "ToPort": NotRequired[int],
        "DryRun": NotRequired[bool],
        "SecurityGroupRuleIds": NotRequired[Sequence[str]],
    },
)
RevokeSecurityGroupIngressRequestSecurityGroupRevokeIngressTypeDef = TypedDict(
    "RevokeSecurityGroupIngressRequestSecurityGroupRevokeIngressTypeDef",
    {
        "CidrIp": NotRequired[str],
        "FromPort": NotRequired[int],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence[IpPermissionTypeDef]],
        "IpProtocol": NotRequired[str],
        "SourceSecurityGroupName": NotRequired[str],
        "SourceSecurityGroupOwnerId": NotRequired[str],
        "ToPort": NotRequired[int],
        "DryRun": NotRequired[bool],
        "SecurityGroupRuleIds": NotRequired[Sequence[str]],
    },
)
RevokeSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeSecurityGroupIngressResultTypeDef",
    {
        "Return": bool,
        "UnknownIpPermissions": List[IpPermissionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "Description": NotRequired[str],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[List[IpPermissionTypeDef]],
        "OwnerId": NotRequired[str],
        "GroupId": NotRequired[str],
        "IpPermissionsEgress": NotRequired[List[IpPermissionTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "VpcId": NotRequired[str],
    },
)
UpdateSecurityGroupRuleDescriptionsEgressRequestRequestTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsEgressRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence[IpPermissionTypeDef]],
        "SecurityGroupRuleDescriptions": NotRequired[Sequence[SecurityGroupRuleDescriptionTypeDef]],
    },
)
UpdateSecurityGroupRuleDescriptionsIngressRequestRequestTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsIngressRequestRequestTypeDef",
    {
        "DryRun": NotRequired[bool],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "IpPermissions": NotRequired[Sequence[IpPermissionTypeDef]],
        "SecurityGroupRuleDescriptions": NotRequired[Sequence[SecurityGroupRuleDescriptionTypeDef]],
    },
)
StaleSecurityGroupTypeDef = TypedDict(
    "StaleSecurityGroupTypeDef",
    {
        "Description": NotRequired[str],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "StaleIpPermissions": NotRequired[List[StaleIpPermissionTypeDef]],
        "StaleIpPermissionsEgress": NotRequired[List[StaleIpPermissionTypeDef]],
        "VpcId": NotRequired[str],
    },
)
GetIpamDiscoveredAccountsResultTypeDef = TypedDict(
    "GetIpamDiscoveredAccountsResultTypeDef",
    {
        "IpamDiscoveredAccounts": List[IpamDiscoveredAccountTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIpamDiscoveredResourceCidrsResultTypeDef = TypedDict(
    "GetIpamDiscoveredResourceCidrsResultTypeDef",
    {
        "IpamDiscoveredResourceCidrs": List[IpamDiscoveredResourceCidrTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIpamResourceCidrsResultTypeDef = TypedDict(
    "GetIpamResourceCidrsResultTypeDef",
    {
        "NextToken": str,
        "IpamResourceCidrs": List[IpamResourceCidrTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyIpamResourceCidrResultTypeDef = TypedDict(
    "ModifyIpamResourceCidrResultTypeDef",
    {
        "IpamResourceCidr": IpamResourceCidrTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIpamResourceDiscoveryResultTypeDef = TypedDict(
    "CreateIpamResourceDiscoveryResultTypeDef",
    {
        "IpamResourceDiscovery": IpamResourceDiscoveryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIpamResourceDiscoveryResultTypeDef = TypedDict(
    "DeleteIpamResourceDiscoveryResultTypeDef",
    {
        "IpamResourceDiscovery": IpamResourceDiscoveryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIpamResourceDiscoveriesResultTypeDef = TypedDict(
    "DescribeIpamResourceDiscoveriesResultTypeDef",
    {
        "IpamResourceDiscoveries": List[IpamResourceDiscoveryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyIpamResourceDiscoveryResultTypeDef = TypedDict(
    "ModifyIpamResourceDiscoveryResultTypeDef",
    {
        "IpamResourceDiscovery": IpamResourceDiscoveryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIpamResultTypeDef = TypedDict(
    "CreateIpamResultTypeDef",
    {
        "Ipam": IpamTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIpamResultTypeDef = TypedDict(
    "DeleteIpamResultTypeDef",
    {
        "Ipam": IpamTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIpamsResultTypeDef = TypedDict(
    "DescribeIpamsResultTypeDef",
    {
        "NextToken": str,
        "Ipams": List[IpamTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyIpamResultTypeDef = TypedDict(
    "ModifyIpamResultTypeDef",
    {
        "Ipam": IpamTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeprovisionIpamPoolCidrResultTypeDef = TypedDict(
    "DeprovisionIpamPoolCidrResultTypeDef",
    {
        "IpamPoolCidr": IpamPoolCidrTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIpamPoolCidrsResultTypeDef = TypedDict(
    "GetIpamPoolCidrsResultTypeDef",
    {
        "IpamPoolCidrs": List[IpamPoolCidrTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisionIpamPoolCidrResultTypeDef = TypedDict(
    "ProvisionIpamPoolCidrResultTypeDef",
    {
        "IpamPoolCidr": IpamPoolCidrTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIpamPoolResultTypeDef = TypedDict(
    "CreateIpamPoolResultTypeDef",
    {
        "IpamPool": IpamPoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIpamPoolResultTypeDef = TypedDict(
    "DeleteIpamPoolResultTypeDef",
    {
        "IpamPool": IpamPoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIpamPoolsResultTypeDef = TypedDict(
    "DescribeIpamPoolsResultTypeDef",
    {
        "NextToken": str,
        "IpamPools": List[IpamPoolTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyIpamPoolResultTypeDef = TypedDict(
    "ModifyIpamPoolResultTypeDef",
    {
        "IpamPool": IpamPoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IpamDiscoveredPublicAddressTypeDef = TypedDict(
    "IpamDiscoveredPublicAddressTypeDef",
    {
        "IpamResourceDiscoveryId": NotRequired[str],
        "AddressRegion": NotRequired[str],
        "Address": NotRequired[str],
        "AddressOwnerId": NotRequired[str],
        "AddressAllocationId": NotRequired[str],
        "AssociationStatus": NotRequired[IpamPublicAddressAssociationStatusType],
        "AddressType": NotRequired[IpamPublicAddressTypeType],
        "Service": NotRequired[IpamPublicAddressAwsServiceType],
        "ServiceResource": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "PublicIpv4PoolId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkInterfaceDescription": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Tags": NotRequired[IpamPublicAddressTagsTypeDef],
        "NetworkBorderGroup": NotRequired[str],
        "SecurityGroups": NotRequired[List[IpamPublicAddressSecurityGroupTypeDef]],
        "SampleTime": NotRequired[datetime],
    },
)
DescribeIpv6PoolsResultTypeDef = TypedDict(
    "DescribeIpv6PoolsResultTypeDef",
    {
        "Ipv6Pools": List[Ipv6PoolTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef = TypedDict(
    "LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef",
    {
        "AssociateCarrierIpAddress": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[List[str]],
        "InterfaceType": NotRequired[str],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[List[InstanceIpv6AddressTypeDef]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[List[PrivateIpAddressSpecificationTypeDef]],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
        "NetworkCardIndex": NotRequired[int],
        "Ipv4Prefixes": NotRequired[List[Ipv4PrefixSpecificationResponseTypeDef]],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[List[Ipv6PrefixSpecificationResponseTypeDef]],
        "Ipv6PrefixCount": NotRequired[int],
        "PrimaryIpv6": NotRequired[bool],
        "EnaSrdSpecification": NotRequired[LaunchTemplateEnaSrdSpecificationTypeDef],
        "ConnectionTrackingSpecification": NotRequired[ConnectionTrackingSpecificationTypeDef],
    },
)
ModifyFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "ModifyFpgaImageAttributeRequestRequestTypeDef",
    {
        "FpgaImageId": str,
        "DryRun": NotRequired[bool],
        "Attribute": NotRequired[FpgaImageAttributeNameType],
        "OperationType": NotRequired[OperationTypeType],
        "UserIds": NotRequired[Sequence[str]],
        "UserGroups": NotRequired[Sequence[str]],
        "ProductCodes": NotRequired[Sequence[str]],
        "LoadPermission": NotRequired[LoadPermissionModificationsTypeDef],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ReservedInstancesModificationTypeDef = TypedDict(
    "ReservedInstancesModificationTypeDef",
    {
        "ClientToken": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "EffectiveDate": NotRequired[datetime],
        "ModificationResults": NotRequired[List[ReservedInstancesModificationResultTypeDef]],
        "ReservedInstancesIds": NotRequired[List[ReservedInstancesIdTypeDef]],
        "ReservedInstancesModificationId": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "UpdateDate": NotRequired[datetime],
    },
)
CreateVerifiedAccessGroupResultTypeDef = TypedDict(
    "CreateVerifiedAccessGroupResultTypeDef",
    {
        "VerifiedAccessGroup": VerifiedAccessGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVerifiedAccessGroupResultTypeDef = TypedDict(
    "DeleteVerifiedAccessGroupResultTypeDef",
    {
        "VerifiedAccessGroup": VerifiedAccessGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVerifiedAccessGroupsResultTypeDef = TypedDict(
    "DescribeVerifiedAccessGroupsResultTypeDef",
    {
        "VerifiedAccessGroups": List[VerifiedAccessGroupTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVerifiedAccessGroupResultTypeDef = TypedDict(
    "ModifyVerifiedAccessGroupResultTypeDef",
    {
        "VerifiedAccessGroup": VerifiedAccessGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNatGatewayResultTypeDef = TypedDict(
    "CreateNatGatewayResultTypeDef",
    {
        "ClientToken": str,
        "NatGateway": NatGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNatGatewaysResultTypeDef = TypedDict(
    "DescribeNatGatewaysResultTypeDef",
    {
        "NatGateways": List[NatGatewayTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkInterfacePermissionResultTypeDef = TypedDict(
    "CreateNetworkInterfacePermissionResultTypeDef",
    {
        "InterfacePermission": NetworkInterfacePermissionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNetworkInterfacePermissionsResultTypeDef = TypedDict(
    "DescribeNetworkInterfacePermissionsResultTypeDef",
    {
        "NetworkInterfacePermissions": List[NetworkInterfacePermissionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVerifiedAccessTrustProviderResultTypeDef = TypedDict(
    "CreateVerifiedAccessTrustProviderResultTypeDef",
    {
        "VerifiedAccessTrustProvider": VerifiedAccessTrustProviderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVerifiedAccessTrustProviderResultTypeDef = TypedDict(
    "DeleteVerifiedAccessTrustProviderResultTypeDef",
    {
        "VerifiedAccessTrustProvider": VerifiedAccessTrustProviderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVerifiedAccessTrustProvidersResultTypeDef = TypedDict(
    "DescribeVerifiedAccessTrustProvidersResultTypeDef",
    {
        "VerifiedAccessTrustProviders": List[VerifiedAccessTrustProviderTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVerifiedAccessTrustProviderResultTypeDef = TypedDict(
    "ModifyVerifiedAccessTrustProviderResultTypeDef",
    {
        "VerifiedAccessTrustProvider": VerifiedAccessTrustProviderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkInsightsPathRequestRequestTypeDef = TypedDict(
    "CreateNetworkInsightsPathRequestRequestTypeDef",
    {
        "Source": str,
        "Protocol": ProtocolType,
        "ClientToken": str,
        "SourceIp": NotRequired[str],
        "DestinationIp": NotRequired[str],
        "Destination": NotRequired[str],
        "DestinationPort": NotRequired[int],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
        "FilterAtSource": NotRequired[PathRequestFilterTypeDef],
        "FilterAtDestination": NotRequired[PathRequestFilterTypeDef],
    },
)
AccessScopePathRequestTypeDef = TypedDict(
    "AccessScopePathRequestTypeDef",
    {
        "Source": NotRequired[PathStatementRequestTypeDef],
        "Destination": NotRequired[PathStatementRequestTypeDef],
        "ThroughResources": NotRequired[Sequence[ThroughResourcesStatementRequestTypeDef]],
    },
)
AccessScopePathTypeDef = TypedDict(
    "AccessScopePathTypeDef",
    {
        "Source": NotRequired[PathStatementTypeDef],
        "Destination": NotRequired[PathStatementTypeDef],
        "ThroughResources": NotRequired[List[ThroughResourcesStatementTypeDef]],
    },
)
CancelReservedInstancesListingResultTypeDef = TypedDict(
    "CancelReservedInstancesListingResultTypeDef",
    {
        "ReservedInstancesListings": List[ReservedInstancesListingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateReservedInstancesListingResultTypeDef = TypedDict(
    "CreateReservedInstancesListingResultTypeDef",
    {
        "ReservedInstancesListings": List[ReservedInstancesListingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReservedInstancesListingsResultTypeDef = TypedDict(
    "DescribeReservedInstancesListingsResultTypeDef",
    {
        "ReservedInstancesListings": List[ReservedInstancesListingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePublicIpv4PoolsResultTypeDef = TypedDict(
    "DescribePublicIpv4PoolsResultTypeDef",
    {
        "PublicIpv4Pools": List[PublicIpv4PoolTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReservedInstancesOfferingsResultTypeDef = TypedDict(
    "DescribeReservedInstancesOfferingsResultTypeDef",
    {
        "ReservedInstancesOfferings": List[ReservedInstancesOfferingTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReservedInstancesResultTypeDef = TypedDict(
    "DescribeReservedInstancesResultTypeDef",
    {
        "ReservedInstances": List[ReservedInstancesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AuthorizeSecurityGroupEgressResultTypeDef = TypedDict(
    "AuthorizeSecurityGroupEgressResultTypeDef",
    {
        "Return": bool,
        "SecurityGroupRules": List[SecurityGroupRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AuthorizeSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeSecurityGroupIngressResultTypeDef",
    {
        "Return": bool,
        "SecurityGroupRules": List[SecurityGroupRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSecurityGroupRulesResultTypeDef = TypedDict(
    "DescribeSecurityGroupRulesResultTypeDef",
    {
        "SecurityGroupRules": List[SecurityGroupRuleTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeScheduledInstanceAvailabilityResultTypeDef = TypedDict(
    "DescribeScheduledInstanceAvailabilityResultTypeDef",
    {
        "NextToken": str,
        "ScheduledInstanceAvailabilitySet": List[ScheduledInstanceAvailabilityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeScheduledInstancesResultTypeDef = TypedDict(
    "DescribeScheduledInstancesResultTypeDef",
    {
        "NextToken": str,
        "ScheduledInstanceSet": List[ScheduledInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PurchaseScheduledInstancesResultTypeDef = TypedDict(
    "PurchaseScheduledInstancesResultTypeDef",
    {
        "ScheduledInstanceSet": List[ScheduledInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScheduledInstancesLaunchSpecificationTypeDef = TypedDict(
    "ScheduledInstancesLaunchSpecificationTypeDef",
    {
        "ImageId": str,
        "BlockDeviceMappings": NotRequired[Sequence[ScheduledInstancesBlockDeviceMappingTypeDef]],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[ScheduledInstancesIamInstanceProfileTypeDef],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired[ScheduledInstancesMonitoringTypeDef],
        "NetworkInterfaces": NotRequired[Sequence[ScheduledInstancesNetworkInterfaceTypeDef]],
        "Placement": NotRequired[ScheduledInstancesPlacementTypeDef],
        "RamdiskId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired[str],
    },
)
CreateVpcEndpointResultTypeDef = TypedDict(
    "CreateVpcEndpointResultTypeDef",
    {
        "VpcEndpoint": VpcEndpointTypeDef,
        "ClientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcEndpointsResultTypeDef = TypedDict(
    "DescribeVpcEndpointsResultTypeDef",
    {
        "VpcEndpoints": List[VpcEndpointTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifySecurityGroupRulesRequestRequestTypeDef = TypedDict(
    "ModifySecurityGroupRulesRequestRequestTypeDef",
    {
        "GroupId": str,
        "SecurityGroupRules": Sequence[SecurityGroupRuleUpdateTypeDef],
        "DryRun": NotRequired[bool],
    },
)
CreateVpcEndpointServiceConfigurationResultTypeDef = TypedDict(
    "CreateVpcEndpointServiceConfigurationResultTypeDef",
    {
        "ServiceConfiguration": ServiceConfigurationTypeDef,
        "ClientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcEndpointServiceConfigurationsResultTypeDef = TypedDict(
    "DescribeVpcEndpointServiceConfigurationsResultTypeDef",
    {
        "ServiceConfigurations": List[ServiceConfigurationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcEndpointServicesResultTypeDef = TypedDict(
    "DescribeVpcEndpointServicesResultTypeDef",
    {
        "ServiceNames": List[str],
        "ServiceDetails": List[ServiceDetailTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportImageResultTypeDef = TypedDict(
    "ImportImageResultTypeDef",
    {
        "Architecture": str,
        "Description": str,
        "Encrypted": bool,
        "Hypervisor": str,
        "ImageId": str,
        "ImportTaskId": str,
        "KmsKeyId": str,
        "LicenseType": str,
        "Platform": str,
        "Progress": str,
        "SnapshotDetails": List[SnapshotDetailTypeDef],
        "Status": str,
        "StatusMessage": str,
        "LicenseSpecifications": List[ImportImageLicenseConfigurationResponseTypeDef],
        "Tags": List[TagTypeDef],
        "UsageOperation": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportImageTaskTypeDef = TypedDict(
    "ImportImageTaskTypeDef",
    {
        "Architecture": NotRequired[str],
        "Description": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Hypervisor": NotRequired[str],
        "ImageId": NotRequired[str],
        "ImportTaskId": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "LicenseType": NotRequired[str],
        "Platform": NotRequired[str],
        "Progress": NotRequired[str],
        "SnapshotDetails": NotRequired[List[SnapshotDetailTypeDef]],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "LicenseSpecifications": NotRequired[List[ImportImageLicenseConfigurationResponseTypeDef]],
        "UsageOperation": NotRequired[str],
        "BootMode": NotRequired[BootModeValuesType],
    },
)
ImportSnapshotResultTypeDef = TypedDict(
    "ImportSnapshotResultTypeDef",
    {
        "Description": str,
        "ImportTaskId": str,
        "SnapshotTaskDetail": SnapshotTaskDetailTypeDef,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportSnapshotTaskTypeDef = TypedDict(
    "ImportSnapshotTaskTypeDef",
    {
        "Description": NotRequired[str],
        "ImportTaskId": NotRequired[str],
        "SnapshotTaskDetail": NotRequired[SnapshotTaskDetailTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
CreateSpotDatafeedSubscriptionResultTypeDef = TypedDict(
    "CreateSpotDatafeedSubscriptionResultTypeDef",
    {
        "SpotDatafeedSubscription": SpotDatafeedSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSpotDatafeedSubscriptionResultTypeDef = TypedDict(
    "DescribeSpotDatafeedSubscriptionResultTypeDef",
    {
        "SpotDatafeedSubscription": SpotDatafeedSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransitGatewayMulticastDomainAssociationsResultTypeDef = TypedDict(
    "GetTransitGatewayMulticastDomainAssociationsResultTypeDef",
    {
        "MulticastDomainAssociations": List[TransitGatewayMulticastDomainAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef = TypedDict(
    "AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef",
    {
        "Associations": TransitGatewayMulticastDomainAssociationsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "AssociateTransitGatewayMulticastDomainResultTypeDef",
    {
        "Associations": TransitGatewayMulticastDomainAssociationsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "DisassociateTransitGatewayMulticastDomainResultTypeDef",
    {
        "Associations": TransitGatewayMulticastDomainAssociationsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectTransitGatewayMulticastDomainAssociationsResultTypeDef = TypedDict(
    "RejectTransitGatewayMulticastDomainAssociationsResultTypeDef",
    {
        "Associations": TransitGatewayMulticastDomainAssociationsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateSubnetCidrBlockResultTypeDef = TypedDict(
    "AssociateSubnetCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": SubnetIpv6CidrBlockAssociationTypeDef,
        "SubnetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateSubnetCidrBlockResultTypeDef = TypedDict(
    "DisassociateSubnetCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": SubnetIpv6CidrBlockAssociationTypeDef,
        "SubnetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "AvailableIpAddressCount": NotRequired[int],
        "CidrBlock": NotRequired[str],
        "DefaultForAz": NotRequired[bool],
        "EnableLniAtDeviceIndex": NotRequired[int],
        "MapPublicIpOnLaunch": NotRequired[bool],
        "MapCustomerOwnedIpOnLaunch": NotRequired[bool],
        "CustomerOwnedIpv4Pool": NotRequired[str],
        "State": NotRequired[SubnetStateType],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "AssignIpv6AddressOnCreation": NotRequired[bool],
        "Ipv6CidrBlockAssociationSet": NotRequired[List[SubnetIpv6CidrBlockAssociationTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "SubnetArn": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "EnableDns64": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
        "PrivateDnsNameOptionsOnLaunch": NotRequired[PrivateDnsNameOptionsOnLaunchTypeDef],
    },
)
GetReservedInstancesExchangeQuoteResultTypeDef = TypedDict(
    "GetReservedInstancesExchangeQuoteResultTypeDef",
    {
        "CurrencyCode": str,
        "IsValidExchange": bool,
        "OutputReservedInstancesWillExpireAt": datetime,
        "PaymentDue": str,
        "ReservedInstanceValueRollup": ReservationValueTypeDef,
        "ReservedInstanceValueSet": List[ReservedInstanceReservationValueTypeDef],
        "TargetConfigurationValueRollup": ReservationValueTypeDef,
        "TargetConfigurationValueSet": List[TargetReservationValueTypeDef],
        "ValidationFailureReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoadBalancersConfigTypeDef = TypedDict(
    "LoadBalancersConfigTypeDef",
    {
        "ClassicLoadBalancersConfig": NotRequired[ClassicLoadBalancersConfigTypeDef],
        "TargetGroupsConfig": NotRequired[TargetGroupsConfigTypeDef],
    },
)
CreateTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "CreateTrafficMirrorFilterRuleResultTypeDef",
    {
        "TrafficMirrorFilterRule": TrafficMirrorFilterRuleTypeDef,
        "ClientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterRuleResultTypeDef",
    {
        "TrafficMirrorFilterRule": TrafficMirrorFilterRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TrafficMirrorFilterTypeDef = TypedDict(
    "TrafficMirrorFilterTypeDef",
    {
        "TrafficMirrorFilterId": NotRequired[str],
        "IngressFilterRules": NotRequired[List[TrafficMirrorFilterRuleTypeDef]],
        "EgressFilterRules": NotRequired[List[TrafficMirrorFilterRuleTypeDef]],
        "NetworkServices": NotRequired[List[Literal["amazon-dns"]]],
        "Description": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
DescribeTransitGatewayAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayAttachmentsResultTypeDef",
    {
        "TransitGatewayAttachments": List[TransitGatewayAttachmentTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TransitGatewayConnectPeerTypeDef = TypedDict(
    "TransitGatewayConnectPeerTypeDef",
    {
        "TransitGatewayAttachmentId": NotRequired[str],
        "TransitGatewayConnectPeerId": NotRequired[str],
        "State": NotRequired[TransitGatewayConnectPeerStateType],
        "CreationTime": NotRequired[datetime],
        "ConnectPeerConfiguration": NotRequired[TransitGatewayConnectPeerConfigurationTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
CreateTransitGatewayConnectResultTypeDef = TypedDict(
    "CreateTransitGatewayConnectResultTypeDef",
    {
        "TransitGatewayConnect": TransitGatewayConnectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTransitGatewayConnectResultTypeDef = TypedDict(
    "DeleteTransitGatewayConnectResultTypeDef",
    {
        "TransitGatewayConnect": TransitGatewayConnectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTransitGatewayConnectsResultTypeDef = TypedDict(
    "DescribeTransitGatewayConnectsResultTypeDef",
    {
        "TransitGatewayConnects": List[TransitGatewayConnectTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "CreateTransitGatewayMulticastDomainResultTypeDef",
    {
        "TransitGatewayMulticastDomain": TransitGatewayMulticastDomainTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "DeleteTransitGatewayMulticastDomainResultTypeDef",
    {
        "TransitGatewayMulticastDomain": TransitGatewayMulticastDomainTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTransitGatewayMulticastDomainsResultTypeDef = TypedDict(
    "DescribeTransitGatewayMulticastDomainsResultTypeDef",
    {
        "TransitGatewayMulticastDomains": List[TransitGatewayMulticastDomainTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitGatewayResultTypeDef = TypedDict(
    "CreateTransitGatewayResultTypeDef",
    {
        "TransitGateway": TransitGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTransitGatewayResultTypeDef = TypedDict(
    "DeleteTransitGatewayResultTypeDef",
    {
        "TransitGateway": TransitGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTransitGatewaysResultTypeDef = TypedDict(
    "DescribeTransitGatewaysResultTypeDef",
    {
        "TransitGateways": List[TransitGatewayTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyTransitGatewayResultTypeDef = TypedDict(
    "ModifyTransitGatewayResultTypeDef",
    {
        "TransitGateway": TransitGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "AcceptTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": TransitGatewayPeeringAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "CreateTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": TransitGatewayPeeringAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "DeleteTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": TransitGatewayPeeringAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTransitGatewayPeeringAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayPeeringAttachmentsResultTypeDef",
    {
        "TransitGatewayPeeringAttachments": List[TransitGatewayPeeringAttachmentTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "RejectTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": TransitGatewayPeeringAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TransitGatewayPolicyTableEntryTypeDef = TypedDict(
    "TransitGatewayPolicyTableEntryTypeDef",
    {
        "PolicyRuleNumber": NotRequired[str],
        "PolicyRule": NotRequired[TransitGatewayPolicyRuleTypeDef],
        "TargetRouteTableId": NotRequired[str],
    },
)
CreateTransitGatewayPrefixListReferenceResultTypeDef = TypedDict(
    "CreateTransitGatewayPrefixListReferenceResultTypeDef",
    {
        "TransitGatewayPrefixListReference": TransitGatewayPrefixListReferenceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTransitGatewayPrefixListReferenceResultTypeDef = TypedDict(
    "DeleteTransitGatewayPrefixListReferenceResultTypeDef",
    {
        "TransitGatewayPrefixListReference": TransitGatewayPrefixListReferenceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransitGatewayPrefixListReferencesResultTypeDef = TypedDict(
    "GetTransitGatewayPrefixListReferencesResultTypeDef",
    {
        "TransitGatewayPrefixListReferences": List[TransitGatewayPrefixListReferenceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyTransitGatewayPrefixListReferenceResultTypeDef = TypedDict(
    "ModifyTransitGatewayPrefixListReferenceResultTypeDef",
    {
        "TransitGatewayPrefixListReference": TransitGatewayPrefixListReferenceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitGatewayRouteResultTypeDef = TypedDict(
    "CreateTransitGatewayRouteResultTypeDef",
    {
        "Route": TransitGatewayRouteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTransitGatewayRouteResultTypeDef = TypedDict(
    "DeleteTransitGatewayRouteResultTypeDef",
    {
        "Route": TransitGatewayRouteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplaceTransitGatewayRouteResultTypeDef = TypedDict(
    "ReplaceTransitGatewayRouteResultTypeDef",
    {
        "Route": TransitGatewayRouteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchTransitGatewayRoutesResultTypeDef = TypedDict(
    "SearchTransitGatewayRoutesResultTypeDef",
    {
        "Routes": List[TransitGatewayRouteTypeDef],
        "AdditionalRoutesAvailable": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "AcceptTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": TransitGatewayVpcAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": TransitGatewayVpcAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "DeleteTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": TransitGatewayVpcAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTransitGatewayVpcAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayVpcAttachmentsResultTypeDef",
    {
        "TransitGatewayVpcAttachments": List[TransitGatewayVpcAttachmentTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": TransitGatewayVpcAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "RejectTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": TransitGatewayVpcAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyInstanceCreditSpecificationResultTypeDef = TypedDict(
    "ModifyInstanceCreditSpecificationResultTypeDef",
    {
        "SuccessfulInstanceCreditSpecifications": List[
            SuccessfulInstanceCreditSpecificationItemTypeDef
        ],
        "UnsuccessfulInstanceCreditSpecifications": List[
            UnsuccessfulInstanceCreditSpecificationItemTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptVpcEndpointConnectionsResultTypeDef = TypedDict(
    "AcceptVpcEndpointConnectionsResultTypeDef",
    {
        "Unsuccessful": List[UnsuccessfulItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFlowLogsResultTypeDef = TypedDict(
    "CreateFlowLogsResultTypeDef",
    {
        "ClientToken": str,
        "FlowLogIds": List[str],
        "Unsuccessful": List[UnsuccessfulItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFlowLogsResultTypeDef = TypedDict(
    "DeleteFlowLogsResultTypeDef",
    {
        "Unsuccessful": List[UnsuccessfulItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVpcEndpointConnectionNotificationsResultTypeDef = TypedDict(
    "DeleteVpcEndpointConnectionNotificationsResultTypeDef",
    {
        "Unsuccessful": List[UnsuccessfulItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVpcEndpointServiceConfigurationsResultTypeDef = TypedDict(
    "DeleteVpcEndpointServiceConfigurationsResultTypeDef",
    {
        "Unsuccessful": List[UnsuccessfulItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVpcEndpointsResultTypeDef = TypedDict(
    "DeleteVpcEndpointsResultTypeDef",
    {
        "Unsuccessful": List[UnsuccessfulItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyHostsResultTypeDef = TypedDict(
    "ModifyHostsResultTypeDef",
    {
        "Successful": List[str],
        "Unsuccessful": List[UnsuccessfulItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectVpcEndpointConnectionsResultTypeDef = TypedDict(
    "RejectVpcEndpointConnectionsResultTypeDef",
    {
        "Unsuccessful": List[UnsuccessfulItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReleaseHostsResultTypeDef = TypedDict(
    "ReleaseHostsResultTypeDef",
    {
        "Successful": List[str],
        "Unsuccessful": List[UnsuccessfulItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLaunchTemplateResultTypeDef = TypedDict(
    "CreateLaunchTemplateResultTypeDef",
    {
        "LaunchTemplate": LaunchTemplateTypeDef,
        "Warning": ValidationWarningTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVerifiedAccessEndpointResultTypeDef = TypedDict(
    "CreateVerifiedAccessEndpointResultTypeDef",
    {
        "VerifiedAccessEndpoint": VerifiedAccessEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVerifiedAccessEndpointResultTypeDef = TypedDict(
    "DeleteVerifiedAccessEndpointResultTypeDef",
    {
        "VerifiedAccessEndpoint": VerifiedAccessEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVerifiedAccessEndpointsResultTypeDef = TypedDict(
    "DescribeVerifiedAccessEndpointsResultTypeDef",
    {
        "VerifiedAccessEndpoints": List[VerifiedAccessEndpointTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVerifiedAccessEndpointResultTypeDef = TypedDict(
    "ModifyVerifiedAccessEndpointResultTypeDef",
    {
        "VerifiedAccessEndpoint": VerifiedAccessEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachVerifiedAccessTrustProviderResultTypeDef = TypedDict(
    "AttachVerifiedAccessTrustProviderResultTypeDef",
    {
        "VerifiedAccessTrustProvider": VerifiedAccessTrustProviderTypeDef,
        "VerifiedAccessInstance": VerifiedAccessInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVerifiedAccessInstanceResultTypeDef = TypedDict(
    "CreateVerifiedAccessInstanceResultTypeDef",
    {
        "VerifiedAccessInstance": VerifiedAccessInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVerifiedAccessInstanceResultTypeDef = TypedDict(
    "DeleteVerifiedAccessInstanceResultTypeDef",
    {
        "VerifiedAccessInstance": VerifiedAccessInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVerifiedAccessInstancesResultTypeDef = TypedDict(
    "DescribeVerifiedAccessInstancesResultTypeDef",
    {
        "VerifiedAccessInstances": List[VerifiedAccessInstanceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachVerifiedAccessTrustProviderResultTypeDef = TypedDict(
    "DetachVerifiedAccessTrustProviderResultTypeDef",
    {
        "VerifiedAccessTrustProvider": VerifiedAccessTrustProviderTypeDef,
        "VerifiedAccessInstance": VerifiedAccessInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVerifiedAccessInstanceResultTypeDef = TypedDict(
    "ModifyVerifiedAccessInstanceResultTypeDef",
    {
        "VerifiedAccessInstance": VerifiedAccessInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifiedAccessLogsTypeDef = TypedDict(
    "VerifiedAccessLogsTypeDef",
    {
        "S3": NotRequired[VerifiedAccessLogS3DestinationTypeDef],
        "CloudWatchLogs": NotRequired[VerifiedAccessLogCloudWatchLogsDestinationTypeDef],
        "KinesisDataFirehose": NotRequired[VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef],
        "LogVersion": NotRequired[str],
        "IncludeTrustContext": NotRequired[bool],
    },
)
ModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "ModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "AccessLogs": VerifiedAccessLogOptionsTypeDef,
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)
VolumeStatusItemTypeDef = TypedDict(
    "VolumeStatusItemTypeDef",
    {
        "Actions": NotRequired[List[VolumeStatusActionTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "Events": NotRequired[List[VolumeStatusEventTypeDef]],
        "VolumeId": NotRequired[str],
        "VolumeStatus": NotRequired[VolumeStatusInfoTypeDef],
        "AttachmentStatuses": NotRequired[List[VolumeStatusAttachmentStatusTypeDef]],
    },
)
AssociateVpcCidrBlockResultTypeDef = TypedDict(
    "AssociateVpcCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": VpcIpv6CidrBlockAssociationTypeDef,
        "CidrBlockAssociation": VpcCidrBlockAssociationTypeDef,
        "VpcId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateVpcCidrBlockResultTypeDef = TypedDict(
    "DisassociateVpcCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": VpcIpv6CidrBlockAssociationTypeDef,
        "CidrBlockAssociation": VpcCidrBlockAssociationTypeDef,
        "VpcId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VpcTypeDef = TypedDict(
    "VpcTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "DhcpOptionsId": NotRequired[str],
        "State": NotRequired[VpcStateType],
        "VpcId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "InstanceTenancy": NotRequired[TenancyType],
        "Ipv6CidrBlockAssociationSet": NotRequired[List[VpcIpv6CidrBlockAssociationTypeDef]],
        "CidrBlockAssociationSet": NotRequired[List[VpcCidrBlockAssociationTypeDef]],
        "IsDefault": NotRequired[bool],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
VpcPeeringConnectionTypeDef = TypedDict(
    "VpcPeeringConnectionTypeDef",
    {
        "AccepterVpcInfo": NotRequired[VpcPeeringConnectionVpcInfoTypeDef],
        "ExpirationTime": NotRequired[datetime],
        "RequesterVpcInfo": NotRequired[VpcPeeringConnectionVpcInfoTypeDef],
        "Status": NotRequired[VpcPeeringConnectionStateReasonTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)
CreateLocalGatewayRouteTableResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableResultTypeDef",
    {
        "LocalGatewayRouteTable": LocalGatewayRouteTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLocalGatewayRouteTableResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableResultTypeDef",
    {
        "LocalGatewayRouteTable": LocalGatewayRouteTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLocalGatewayRouteTablesResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTablesResultTypeDef",
    {
        "LocalGatewayRouteTables": List[LocalGatewayRouteTableTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVolumesResultTypeDef = TypedDict(
    "DescribeVolumesResultTypeDef",
    {
        "Volumes": List[VolumeTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateInstanceEventWindowResultTypeDef = TypedDict(
    "AssociateInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": InstanceEventWindowTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceEventWindowResultTypeDef = TypedDict(
    "CreateInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": InstanceEventWindowTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstanceEventWindowsResultTypeDef = TypedDict(
    "DescribeInstanceEventWindowsResultTypeDef",
    {
        "InstanceEventWindows": List[InstanceEventWindowTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateInstanceEventWindowResultTypeDef = TypedDict(
    "DisassociateInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": InstanceEventWindowTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyInstanceEventWindowResultTypeDef = TypedDict(
    "ModifyInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": InstanceEventWindowTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PathComponentTypeDef = TypedDict(
    "PathComponentTypeDef",
    {
        "SequenceNumber": NotRequired[int],
        "AclRule": NotRequired[AnalysisAclRuleTypeDef],
        "AttachedTo": NotRequired[AnalysisComponentTypeDef],
        "Component": NotRequired[AnalysisComponentTypeDef],
        "DestinationVpc": NotRequired[AnalysisComponentTypeDef],
        "OutboundHeader": NotRequired[AnalysisPacketHeaderTypeDef],
        "InboundHeader": NotRequired[AnalysisPacketHeaderTypeDef],
        "RouteTableRoute": NotRequired[AnalysisRouteTableRouteTypeDef],
        "SecurityGroupRule": NotRequired[AnalysisSecurityGroupRuleTypeDef],
        "SourceVpc": NotRequired[AnalysisComponentTypeDef],
        "Subnet": NotRequired[AnalysisComponentTypeDef],
        "Vpc": NotRequired[AnalysisComponentTypeDef],
        "AdditionalDetails": NotRequired[List[AdditionalDetailTypeDef]],
        "TransitGateway": NotRequired[AnalysisComponentTypeDef],
        "TransitGatewayRouteTableRoute": NotRequired[TransitGatewayRouteTableRouteTypeDef],
        "Explanations": NotRequired[List[ExplanationTypeDef]],
        "ElasticLoadBalancerListener": NotRequired[AnalysisComponentTypeDef],
        "FirewallStatelessRule": NotRequired[FirewallStatelessRuleTypeDef],
        "FirewallStatefulRule": NotRequired[FirewallStatefulRuleTypeDef],
        "ServiceName": NotRequired[str],
    },
)
CreateRouteTableResultTypeDef = TypedDict(
    "CreateRouteTableResultTypeDef",
    {
        "RouteTable": RouteTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRouteTablesResultTypeDef = TypedDict(
    "DescribeRouteTablesResultTypeDef",
    {
        "RouteTables": List[RouteTableTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFlowLogsIntegrationTemplateRequestRequestTypeDef = TypedDict(
    "GetFlowLogsIntegrationTemplateRequestRequestTypeDef",
    {
        "FlowLogId": str,
        "ConfigDeliveryS3DestinationArn": str,
        "IntegrateServices": IntegrateServicesTypeDef,
        "DryRun": NotRequired[bool],
    },
)
DescribeNetworkInterfaceAttributeResultTypeDef = TypedDict(
    "DescribeNetworkInterfaceAttributeResultTypeDef",
    {
        "Attachment": NetworkInterfaceAttachmentTypeDef,
        "Description": AttributeValueTypeDef,
        "Groups": List[GroupIdentifierTypeDef],
        "NetworkInterfaceId": str,
        "SourceDestCheck": AttributeBooleanValueTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Association": NotRequired[NetworkInterfaceAssociationTypeDef],
        "Attachment": NotRequired[NetworkInterfaceAttachmentTypeDef],
        "AvailabilityZone": NotRequired[str],
        "ConnectionTrackingConfiguration": NotRequired[ConnectionTrackingConfigurationTypeDef],
        "Description": NotRequired[str],
        "Groups": NotRequired[List[GroupIdentifierTypeDef]],
        "InterfaceType": NotRequired[NetworkInterfaceTypeType],
        "Ipv6Addresses": NotRequired[List[NetworkInterfaceIpv6AddressTypeDef]],
        "MacAddress": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "OwnerId": NotRequired[str],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[List[NetworkInterfacePrivateIpAddressTypeDef]],
        "Ipv4Prefixes": NotRequired[List[Ipv4PrefixSpecificationTypeDef]],
        "Ipv6Prefixes": NotRequired[List[Ipv6PrefixSpecificationTypeDef]],
        "RequesterId": NotRequired[str],
        "RequesterManaged": NotRequired[bool],
        "SourceDestCheck": NotRequired[bool],
        "Status": NotRequired[NetworkInterfaceStatusType],
        "SubnetId": NotRequired[str],
        "TagSet": NotRequired[List[TagTypeDef]],
        "VpcId": NotRequired[str],
        "DenyAllIgwTraffic": NotRequired[bool],
        "Ipv6Native": NotRequired[bool],
        "Ipv6Address": NotRequired[str],
    },
)
CreateDhcpOptionsResultTypeDef = TypedDict(
    "CreateDhcpOptionsResultTypeDef",
    {
        "DhcpOptions": DhcpOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDhcpOptionsResultTypeDef = TypedDict(
    "DescribeDhcpOptionsResultTypeDef",
    {
        "DhcpOptions": List[DhcpOptionsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHostsResultTypeDef = TypedDict(
    "DescribeHostsResultTypeDef",
    {
        "Hosts": List[HostTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BundleInstanceRequestRequestTypeDef = TypedDict(
    "BundleInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Storage": StorageTypeDef,
        "DryRun": NotRequired[bool],
    },
)
BundleTaskTypeDef = TypedDict(
    "BundleTaskTypeDef",
    {
        "BundleId": NotRequired[str],
        "BundleTaskError": NotRequired[BundleTaskErrorTypeDef],
        "InstanceId": NotRequired[str],
        "Progress": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "State": NotRequired[BundleTaskStateType],
        "Storage": NotRequired[StorageTypeDef],
        "UpdateTime": NotRequired[datetime],
    },
)
DescribeImagesResultTypeDef = TypedDict(
    "DescribeImagesResultTypeDef",
    {
        "Images": List[ImageTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeClientVpnEndpointsResultTypeDef = TypedDict(
    "DescribeClientVpnEndpointsResultTypeDef",
    {
        "ClientVpnEndpoints": List[ClientVpnEndpointTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpnTunnelOptionsRequestRequestTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
        "TunnelOptions": ModifyVpnTunnelOptionsSpecificationTypeDef,
        "DryRun": NotRequired[bool],
        "SkipTunnelReplacement": NotRequired[bool],
    },
)
VpnConnectionOptionsSpecificationTypeDef = TypedDict(
    "VpnConnectionOptionsSpecificationTypeDef",
    {
        "EnableAcceleration": NotRequired[bool],
        "StaticRoutesOnly": NotRequired[bool],
        "TunnelInsideIpVersion": NotRequired[TunnelInsideIpVersionType],
        "TunnelOptions": NotRequired[Sequence[VpnTunnelOptionsSpecificationTypeDef]],
        "LocalIpv4NetworkCidr": NotRequired[str],
        "RemoteIpv4NetworkCidr": NotRequired[str],
        "LocalIpv6NetworkCidr": NotRequired[str],
        "RemoteIpv6NetworkCidr": NotRequired[str],
        "OutsideIpAddressType": NotRequired[str],
        "TransportTransitGatewayAttachmentId": NotRequired[str],
    },
)
VpnConnectionOptionsTypeDef = TypedDict(
    "VpnConnectionOptionsTypeDef",
    {
        "EnableAcceleration": NotRequired[bool],
        "StaticRoutesOnly": NotRequired[bool],
        "LocalIpv4NetworkCidr": NotRequired[str],
        "RemoteIpv4NetworkCidr": NotRequired[str],
        "LocalIpv6NetworkCidr": NotRequired[str],
        "RemoteIpv6NetworkCidr": NotRequired[str],
        "OutsideIpAddressType": NotRequired[str],
        "TransportTransitGatewayAttachmentId": NotRequired[str],
        "TunnelInsideIpVersion": NotRequired[TunnelInsideIpVersionType],
        "TunnelOptions": NotRequired[List[TunnelOptionTypeDef]],
    },
)
CreateNetworkAclResultTypeDef = TypedDict(
    "CreateNetworkAclResultTypeDef",
    {
        "NetworkAcl": NetworkAclTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNetworkAclsResultTypeDef = TypedDict(
    "DescribeNetworkAclsResultTypeDef",
    {
        "NetworkAcls": List[NetworkAclTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableFastSnapshotRestoresResultTypeDef = TypedDict(
    "DisableFastSnapshotRestoresResultTypeDef",
    {
        "Successful": List[DisableFastSnapshotRestoreSuccessItemTypeDef],
        "Unsuccessful": List[DisableFastSnapshotRestoreErrorItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConversionTaskTypeDef = TypedDict(
    "ConversionTaskTypeDef",
    {
        "ConversionTaskId": NotRequired[str],
        "ExpirationTime": NotRequired[str],
        "ImportInstance": NotRequired[ImportInstanceTaskDetailsTypeDef],
        "ImportVolume": NotRequired[ImportVolumeTaskDetailsTypeDef],
        "State": NotRequired[ConversionTaskStateType],
        "StatusMessage": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
RunInstancesRequestServiceResourceCreateInstancesTypeDef = TypedDict(
    "RunInstancesRequestServiceResourceCreateInstancesTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
        "BlockDeviceMappings": NotRequired[Sequence[BlockDeviceMappingTypeDef]],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[InstanceIpv6AddressTypeDef]],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired[RunInstancesMonitoringEnabledTypeDef],
        "Placement": NotRequired[PlacementTypeDef],
        "RamdiskId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired[str],
        "AdditionalInfo": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DisableApiTermination": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[IamInstanceProfileSpecificationTypeDef],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "NetworkInterfaces": NotRequired[
            Sequence[InstanceNetworkInterfaceSpecificationServiceResourceTypeDef]
        ],
        "PrivateIpAddress": NotRequired[str],
        "ElasticGpuSpecification": NotRequired[Sequence[ElasticGpuSpecificationTypeDef]],
        "ElasticInferenceAccelerators": NotRequired[Sequence[ElasticInferenceAcceleratorTypeDef]],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "LaunchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "InstanceMarketOptions": NotRequired[InstanceMarketOptionsRequestTypeDef],
        "CreditSpecification": NotRequired[CreditSpecificationRequestTypeDef],
        "CpuOptions": NotRequired[CpuOptionsRequestTypeDef],
        "CapacityReservationSpecification": NotRequired[CapacityReservationSpecificationTypeDef],
        "HibernationOptions": NotRequired[HibernationOptionsRequestTypeDef],
        "LicenseSpecifications": NotRequired[Sequence[LicenseConfigurationRequestTypeDef]],
        "MetadataOptions": NotRequired[InstanceMetadataOptionsRequestTypeDef],
        "EnclaveOptions": NotRequired[EnclaveOptionsRequestTypeDef],
        "PrivateDnsNameOptions": NotRequired[PrivateDnsNameOptionsRequestTypeDef],
        "MaintenanceOptions": NotRequired[InstanceMaintenanceOptionsRequestTypeDef],
        "DisableApiStop": NotRequired[bool],
        "EnablePrimaryIpv6": NotRequired[bool],
    },
)
RunInstancesRequestSubnetCreateInstancesTypeDef = TypedDict(
    "RunInstancesRequestSubnetCreateInstancesTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
        "BlockDeviceMappings": NotRequired[Sequence[BlockDeviceMappingTypeDef]],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[InstanceIpv6AddressTypeDef]],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired[RunInstancesMonitoringEnabledTypeDef],
        "Placement": NotRequired[PlacementTypeDef],
        "RamdiskId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "UserData": NotRequired[str],
        "AdditionalInfo": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DisableApiTermination": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[IamInstanceProfileSpecificationTypeDef],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "NetworkInterfaces": NotRequired[
            Sequence[InstanceNetworkInterfaceSpecificationSubnetTypeDef]
        ],
        "PrivateIpAddress": NotRequired[str],
        "ElasticGpuSpecification": NotRequired[Sequence[ElasticGpuSpecificationTypeDef]],
        "ElasticInferenceAccelerators": NotRequired[Sequence[ElasticInferenceAcceleratorTypeDef]],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "LaunchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "InstanceMarketOptions": NotRequired[InstanceMarketOptionsRequestTypeDef],
        "CreditSpecification": NotRequired[CreditSpecificationRequestTypeDef],
        "CpuOptions": NotRequired[CpuOptionsRequestTypeDef],
        "CapacityReservationSpecification": NotRequired[CapacityReservationSpecificationTypeDef],
        "HibernationOptions": NotRequired[HibernationOptionsRequestTypeDef],
        "LicenseSpecifications": NotRequired[Sequence[LicenseConfigurationRequestTypeDef]],
        "MetadataOptions": NotRequired[InstanceMetadataOptionsRequestTypeDef],
        "EnclaveOptions": NotRequired[EnclaveOptionsRequestTypeDef],
        "PrivateDnsNameOptions": NotRequired[PrivateDnsNameOptionsRequestTypeDef],
        "MaintenanceOptions": NotRequired[InstanceMaintenanceOptionsRequestTypeDef],
        "DisableApiStop": NotRequired[bool],
        "EnablePrimaryIpv6": NotRequired[bool],
    },
)
LaunchSpecificationTypeDef = TypedDict(
    "LaunchSpecificationTypeDef",
    {
        "UserData": NotRequired[str],
        "SecurityGroups": NotRequired[List[GroupIdentifierTypeDef]],
        "AddressingType": NotRequired[str],
        "BlockDeviceMappings": NotRequired[List[BlockDeviceMappingTypeDef]],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[IamInstanceProfileSpecificationTypeDef],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "NetworkInterfaces": NotRequired[List[InstanceNetworkInterfaceSpecificationTypeDef]],
        "Placement": NotRequired[SpotPlacementTypeDef],
        "RamdiskId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Monitoring": NotRequired[RunInstancesMonitoringEnabledTypeDef],
    },
)
RequestSpotLaunchSpecificationTypeDef = TypedDict(
    "RequestSpotLaunchSpecificationTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "AddressingType": NotRequired[str],
        "BlockDeviceMappings": NotRequired[Sequence[BlockDeviceMappingTypeDef]],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[IamInstanceProfileSpecificationTypeDef],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired[RunInstancesMonitoringEnabledTypeDef],
        "NetworkInterfaces": NotRequired[Sequence[InstanceNetworkInterfaceSpecificationTypeDef]],
        "Placement": NotRequired[SpotPlacementTypeDef],
        "RamdiskId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired[str],
    },
)
RunInstancesRequestRequestTypeDef = TypedDict(
    "RunInstancesRequestRequestTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
        "BlockDeviceMappings": NotRequired[Sequence[BlockDeviceMappingTypeDef]],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[Sequence[InstanceIpv6AddressTypeDef]],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired[RunInstancesMonitoringEnabledTypeDef],
        "Placement": NotRequired[PlacementTypeDef],
        "RamdiskId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired[str],
        "AdditionalInfo": NotRequired[str],
        "ClientToken": NotRequired[str],
        "DisableApiTermination": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[IamInstanceProfileSpecificationTypeDef],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "NetworkInterfaces": NotRequired[Sequence[InstanceNetworkInterfaceSpecificationTypeDef]],
        "PrivateIpAddress": NotRequired[str],
        "ElasticGpuSpecification": NotRequired[Sequence[ElasticGpuSpecificationTypeDef]],
        "ElasticInferenceAccelerators": NotRequired[Sequence[ElasticInferenceAcceleratorTypeDef]],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "LaunchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "InstanceMarketOptions": NotRequired[InstanceMarketOptionsRequestTypeDef],
        "CreditSpecification": NotRequired[CreditSpecificationRequestTypeDef],
        "CpuOptions": NotRequired[CpuOptionsRequestTypeDef],
        "CapacityReservationSpecification": NotRequired[CapacityReservationSpecificationTypeDef],
        "HibernationOptions": NotRequired[HibernationOptionsRequestTypeDef],
        "LicenseSpecifications": NotRequired[Sequence[LicenseConfigurationRequestTypeDef]],
        "MetadataOptions": NotRequired[InstanceMetadataOptionsRequestTypeDef],
        "EnclaveOptions": NotRequired[EnclaveOptionsRequestTypeDef],
        "PrivateDnsNameOptions": NotRequired[PrivateDnsNameOptionsRequestTypeDef],
        "MaintenanceOptions": NotRequired[InstanceMaintenanceOptionsRequestTypeDef],
        "DisableApiStop": NotRequired[bool],
        "EnablePrimaryIpv6": NotRequired[bool],
    },
)
SpotFleetLaunchSpecificationTypeDef = TypedDict(
    "SpotFleetLaunchSpecificationTypeDef",
    {
        "SecurityGroups": NotRequired[List[GroupIdentifierTypeDef]],
        "AddressingType": NotRequired[str],
        "BlockDeviceMappings": NotRequired[List[BlockDeviceMappingTypeDef]],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[IamInstanceProfileSpecificationTypeDef],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired[SpotFleetMonitoringTypeDef],
        "NetworkInterfaces": NotRequired[List[InstanceNetworkInterfaceSpecificationTypeDef]],
        "Placement": NotRequired[SpotPlacementTypeDef],
        "RamdiskId": NotRequired[str],
        "SpotPrice": NotRequired[str],
        "SubnetId": NotRequired[str],
        "UserData": NotRequired[str],
        "WeightedCapacity": NotRequired[float],
        "TagSpecifications": NotRequired[List[SpotFleetTagSpecificationTypeDef]],
        "InstanceRequirements": NotRequired[InstanceRequirementsTypeDef],
    },
)
RequestLaunchTemplateDataTypeDef = TypedDict(
    "RequestLaunchTemplateDataTypeDef",
    {
        "KernelId": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[
            LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef
        ],
        "BlockDeviceMappings": NotRequired[
            Sequence[LaunchTemplateBlockDeviceMappingRequestTypeDef]
        ],
        "NetworkInterfaces": NotRequired[
            Sequence[LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef]
        ],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired[LaunchTemplatesMonitoringRequestTypeDef],
        "Placement": NotRequired[LaunchTemplatePlacementRequestTypeDef],
        "RamDiskId": NotRequired[str],
        "DisableApiTermination": NotRequired[bool],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "UserData": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[LaunchTemplateTagSpecificationRequestTypeDef]],
        "ElasticGpuSpecifications": NotRequired[Sequence[ElasticGpuSpecificationTypeDef]],
        "ElasticInferenceAccelerators": NotRequired[
            Sequence[LaunchTemplateElasticInferenceAcceleratorTypeDef]
        ],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "InstanceMarketOptions": NotRequired[LaunchTemplateInstanceMarketOptionsRequestTypeDef],
        "CreditSpecification": NotRequired[CreditSpecificationRequestTypeDef],
        "CpuOptions": NotRequired[LaunchTemplateCpuOptionsRequestTypeDef],
        "CapacityReservationSpecification": NotRequired[
            LaunchTemplateCapacityReservationSpecificationRequestTypeDef
        ],
        "LicenseSpecifications": NotRequired[
            Sequence[LaunchTemplateLicenseConfigurationRequestTypeDef]
        ],
        "HibernationOptions": NotRequired[LaunchTemplateHibernationOptionsRequestTypeDef],
        "MetadataOptions": NotRequired[LaunchTemplateInstanceMetadataOptionsRequestTypeDef],
        "EnclaveOptions": NotRequired[LaunchTemplateEnclaveOptionsRequestTypeDef],
        "InstanceRequirements": NotRequired[InstanceRequirementsRequestTypeDef],
        "PrivateDnsNameOptions": NotRequired[LaunchTemplatePrivateDnsNameOptionsRequestTypeDef],
        "MaintenanceOptions": NotRequired[LaunchTemplateInstanceMaintenanceOptionsRequestTypeDef],
        "DisableApiStop": NotRequired[bool],
    },
)
EnableFastSnapshotRestoresResultTypeDef = TypedDict(
    "EnableFastSnapshotRestoresResultTypeDef",
    {
        "Successful": List[EnableFastSnapshotRestoreSuccessItemTypeDef],
        "Unsuccessful": List[EnableFastSnapshotRestoreErrorItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkInsightsPathResultTypeDef = TypedDict(
    "CreateNetworkInsightsPathResultTypeDef",
    {
        "NetworkInsightsPath": NetworkInsightsPathTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNetworkInsightsPathsResultTypeDef = TypedDict(
    "DescribeNetworkInsightsPathsResultTypeDef",
    {
        "NetworkInsightsPaths": List[NetworkInsightsPathTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceTypeInfoTypeDef = TypedDict(
    "InstanceTypeInfoTypeDef",
    {
        "InstanceType": NotRequired[InstanceTypeType],
        "CurrentGeneration": NotRequired[bool],
        "FreeTierEligible": NotRequired[bool],
        "SupportedUsageClasses": NotRequired[List[UsageClassTypeType]],
        "SupportedRootDeviceTypes": NotRequired[List[RootDeviceTypeType]],
        "SupportedVirtualizationTypes": NotRequired[List[VirtualizationTypeType]],
        "BareMetal": NotRequired[bool],
        "Hypervisor": NotRequired[InstanceTypeHypervisorType],
        "ProcessorInfo": NotRequired[ProcessorInfoTypeDef],
        "VCpuInfo": NotRequired[VCpuInfoTypeDef],
        "MemoryInfo": NotRequired[MemoryInfoTypeDef],
        "InstanceStorageSupported": NotRequired[bool],
        "InstanceStorageInfo": NotRequired[InstanceStorageInfoTypeDef],
        "EbsInfo": NotRequired[EbsInfoTypeDef],
        "NetworkInfo": NotRequired[NetworkInfoTypeDef],
        "GpuInfo": NotRequired[GpuInfoTypeDef],
        "FpgaInfo": NotRequired[FpgaInfoTypeDef],
        "PlacementGroupInfo": NotRequired[PlacementGroupInfoTypeDef],
        "InferenceAcceleratorInfo": NotRequired[InferenceAcceleratorInfoTypeDef],
        "HibernationSupported": NotRequired[bool],
        "BurstablePerformanceSupported": NotRequired[bool],
        "DedicatedHostsSupported": NotRequired[bool],
        "AutoRecoverySupported": NotRequired[bool],
        "SupportedBootModes": NotRequired[List[BootModeTypeType]],
        "NitroEnclavesSupport": NotRequired[NitroEnclavesSupportType],
        "NitroTpmSupport": NotRequired[NitroTpmSupportType],
        "NitroTpmInfo": NotRequired[NitroTpmInfoTypeDef],
    },
)
InstanceNetworkInterfaceTypeDef = TypedDict(
    "InstanceNetworkInterfaceTypeDef",
    {
        "Association": NotRequired[InstanceNetworkInterfaceAssociationTypeDef],
        "Attachment": NotRequired[InstanceNetworkInterfaceAttachmentTypeDef],
        "Description": NotRequired[str],
        "Groups": NotRequired[List[GroupIdentifierTypeDef]],
        "Ipv6Addresses": NotRequired[List[InstanceIpv6AddressTypeDef]],
        "MacAddress": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[List[InstancePrivateIpAddressTypeDef]],
        "SourceDestCheck": NotRequired[bool],
        "Status": NotRequired[NetworkInterfaceStatusType],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "InterfaceType": NotRequired[str],
        "Ipv4Prefixes": NotRequired[List[InstanceIpv4PrefixTypeDef]],
        "Ipv6Prefixes": NotRequired[List[InstanceIpv6PrefixTypeDef]],
        "ConnectionTrackingConfiguration": NotRequired[
            ConnectionTrackingSpecificationResponseTypeDef
        ],
    },
)
FleetLaunchTemplateConfigRequestTypeDef = TypedDict(
    "FleetLaunchTemplateConfigRequestTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[FleetLaunchTemplateSpecificationRequestTypeDef],
        "Overrides": NotRequired[Sequence[FleetLaunchTemplateOverridesRequestTypeDef]],
    },
)
GetSpotPlacementScoresRequestGetSpotPlacementScoresPaginateTypeDef = TypedDict(
    "GetSpotPlacementScoresRequestGetSpotPlacementScoresPaginateTypeDef",
    {
        "TargetCapacity": int,
        "InstanceTypes": NotRequired[Sequence[str]],
        "TargetCapacityUnitType": NotRequired[TargetCapacityUnitTypeType],
        "SingleAvailabilityZone": NotRequired[bool],
        "RegionNames": NotRequired[Sequence[str]],
        "InstanceRequirementsWithMetadata": NotRequired[
            InstanceRequirementsWithMetadataRequestTypeDef
        ],
        "DryRun": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSpotPlacementScoresRequestRequestTypeDef = TypedDict(
    "GetSpotPlacementScoresRequestRequestTypeDef",
    {
        "TargetCapacity": int,
        "InstanceTypes": NotRequired[Sequence[str]],
        "TargetCapacityUnitType": NotRequired[TargetCapacityUnitTypeType],
        "SingleAvailabilityZone": NotRequired[bool],
        "RegionNames": NotRequired[Sequence[str]],
        "InstanceRequirementsWithMetadata": NotRequired[
            InstanceRequirementsWithMetadataRequestTypeDef
        ],
        "DryRun": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
FleetLaunchTemplateConfigTypeDef = TypedDict(
    "FleetLaunchTemplateConfigTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[FleetLaunchTemplateSpecificationTypeDef],
        "Overrides": NotRequired[List[FleetLaunchTemplateOverridesTypeDef]],
    },
)
LaunchTemplateAndOverridesResponseTypeDef = TypedDict(
    "LaunchTemplateAndOverridesResponseTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[FleetLaunchTemplateSpecificationTypeDef],
        "Overrides": NotRequired[FleetLaunchTemplateOverridesTypeDef],
    },
)
LaunchTemplateConfigTypeDef = TypedDict(
    "LaunchTemplateConfigTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[FleetLaunchTemplateSpecificationTypeDef],
        "Overrides": NotRequired[List[LaunchTemplateOverridesTypeDef]],
    },
)
DescribeInstanceStatusResultTypeDef = TypedDict(
    "DescribeInstanceStatusResultTypeDef",
    {
        "InstanceStatuses": List[InstanceStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSecurityGroupsResultPaginatorTypeDef = TypedDict(
    "DescribeSecurityGroupsResultPaginatorTypeDef",
    {
        "SecurityGroups": List[SecurityGroupPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSecurityGroupsResultTypeDef = TypedDict(
    "DescribeSecurityGroupsResultTypeDef",
    {
        "SecurityGroups": List[SecurityGroupTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStaleSecurityGroupsResultTypeDef = TypedDict(
    "DescribeStaleSecurityGroupsResultTypeDef",
    {
        "NextToken": str,
        "StaleSecurityGroupSet": List[StaleSecurityGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIpamDiscoveredPublicAddressesResultTypeDef = TypedDict(
    "GetIpamDiscoveredPublicAddressesResultTypeDef",
    {
        "IpamDiscoveredPublicAddresses": List[IpamDiscoveredPublicAddressTypeDef],
        "OldestSampleTime": datetime,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResponseLaunchTemplateDataTypeDef = TypedDict(
    "ResponseLaunchTemplateDataTypeDef",
    {
        "KernelId": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[LaunchTemplateIamInstanceProfileSpecificationTypeDef],
        "BlockDeviceMappings": NotRequired[List[LaunchTemplateBlockDeviceMappingTypeDef]],
        "NetworkInterfaces": NotRequired[
            List[LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef]
        ],
        "ImageId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KeyName": NotRequired[str],
        "Monitoring": NotRequired[LaunchTemplatesMonitoringTypeDef],
        "Placement": NotRequired[LaunchTemplatePlacementTypeDef],
        "RamDiskId": NotRequired[str],
        "DisableApiTermination": NotRequired[bool],
        "InstanceInitiatedShutdownBehavior": NotRequired[ShutdownBehaviorType],
        "UserData": NotRequired[str],
        "TagSpecifications": NotRequired[List[LaunchTemplateTagSpecificationTypeDef]],
        "ElasticGpuSpecifications": NotRequired[List[ElasticGpuSpecificationResponseTypeDef]],
        "ElasticInferenceAccelerators": NotRequired[
            List[LaunchTemplateElasticInferenceAcceleratorResponseTypeDef]
        ],
        "SecurityGroupIds": NotRequired[List[str]],
        "SecurityGroups": NotRequired[List[str]],
        "InstanceMarketOptions": NotRequired[LaunchTemplateInstanceMarketOptionsTypeDef],
        "CreditSpecification": NotRequired[CreditSpecificationTypeDef],
        "CpuOptions": NotRequired[LaunchTemplateCpuOptionsTypeDef],
        "CapacityReservationSpecification": NotRequired[
            LaunchTemplateCapacityReservationSpecificationResponseTypeDef
        ],
        "LicenseSpecifications": NotRequired[List[LaunchTemplateLicenseConfigurationTypeDef]],
        "HibernationOptions": NotRequired[LaunchTemplateHibernationOptionsTypeDef],
        "MetadataOptions": NotRequired[LaunchTemplateInstanceMetadataOptionsTypeDef],
        "EnclaveOptions": NotRequired[LaunchTemplateEnclaveOptionsTypeDef],
        "InstanceRequirements": NotRequired[InstanceRequirementsTypeDef],
        "PrivateDnsNameOptions": NotRequired[LaunchTemplatePrivateDnsNameOptionsTypeDef],
        "MaintenanceOptions": NotRequired[LaunchTemplateInstanceMaintenanceOptionsTypeDef],
        "DisableApiStop": NotRequired[bool],
    },
)
DescribeReservedInstancesModificationsResultTypeDef = TypedDict(
    "DescribeReservedInstancesModificationsResultTypeDef",
    {
        "NextToken": str,
        "ReservedInstancesModifications": List[ReservedInstancesModificationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkInsightsAccessScopeRequestRequestTypeDef = TypedDict(
    "CreateNetworkInsightsAccessScopeRequestRequestTypeDef",
    {
        "ClientToken": str,
        "MatchPaths": NotRequired[Sequence[AccessScopePathRequestTypeDef]],
        "ExcludePaths": NotRequired[Sequence[AccessScopePathRequestTypeDef]],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "DryRun": NotRequired[bool],
    },
)
NetworkInsightsAccessScopeContentTypeDef = TypedDict(
    "NetworkInsightsAccessScopeContentTypeDef",
    {
        "NetworkInsightsAccessScopeId": NotRequired[str],
        "MatchPaths": NotRequired[List[AccessScopePathTypeDef]],
        "ExcludePaths": NotRequired[List[AccessScopePathTypeDef]],
    },
)
RunScheduledInstancesRequestRequestTypeDef = TypedDict(
    "RunScheduledInstancesRequestRequestTypeDef",
    {
        "LaunchSpecification": ScheduledInstancesLaunchSpecificationTypeDef,
        "ScheduledInstanceId": str,
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "InstanceCount": NotRequired[int],
    },
)
DescribeImportImageTasksResultTypeDef = TypedDict(
    "DescribeImportImageTasksResultTypeDef",
    {
        "ImportImageTasks": List[ImportImageTaskTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeImportSnapshotTasksResultTypeDef = TypedDict(
    "DescribeImportSnapshotTasksResultTypeDef",
    {
        "ImportSnapshotTasks": List[ImportSnapshotTaskTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDefaultSubnetResultTypeDef = TypedDict(
    "CreateDefaultSubnetResultTypeDef",
    {
        "Subnet": SubnetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSubnetResultTypeDef = TypedDict(
    "CreateSubnetResultTypeDef",
    {
        "Subnet": SubnetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSubnetsResultTypeDef = TypedDict(
    "DescribeSubnetsResultTypeDef",
    {
        "Subnets": List[SubnetTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrafficMirrorFilterResultTypeDef = TypedDict(
    "CreateTrafficMirrorFilterResultTypeDef",
    {
        "TrafficMirrorFilter": TrafficMirrorFilterTypeDef,
        "ClientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrafficMirrorFiltersResultTypeDef = TypedDict(
    "DescribeTrafficMirrorFiltersResultTypeDef",
    {
        "TrafficMirrorFilters": List[TrafficMirrorFilterTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyTrafficMirrorFilterNetworkServicesResultTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterNetworkServicesResultTypeDef",
    {
        "TrafficMirrorFilter": TrafficMirrorFilterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitGatewayConnectPeerResultTypeDef = TypedDict(
    "CreateTransitGatewayConnectPeerResultTypeDef",
    {
        "TransitGatewayConnectPeer": TransitGatewayConnectPeerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTransitGatewayConnectPeerResultTypeDef = TypedDict(
    "DeleteTransitGatewayConnectPeerResultTypeDef",
    {
        "TransitGatewayConnectPeer": TransitGatewayConnectPeerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTransitGatewayConnectPeersResultTypeDef = TypedDict(
    "DescribeTransitGatewayConnectPeersResultTypeDef",
    {
        "TransitGatewayConnectPeers": List[TransitGatewayConnectPeerTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransitGatewayPolicyTableEntriesResultTypeDef = TypedDict(
    "GetTransitGatewayPolicyTableEntriesResultTypeDef",
    {
        "TransitGatewayPolicyTableEntries": List[TransitGatewayPolicyTableEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifiedAccessInstanceLoggingConfigurationTypeDef = TypedDict(
    "VerifiedAccessInstanceLoggingConfigurationTypeDef",
    {
        "VerifiedAccessInstanceId": NotRequired[str],
        "AccessLogs": NotRequired[VerifiedAccessLogsTypeDef],
    },
)
DescribeVolumeStatusResultTypeDef = TypedDict(
    "DescribeVolumeStatusResultTypeDef",
    {
        "NextToken": str,
        "VolumeStatuses": List[VolumeStatusItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDefaultVpcResultTypeDef = TypedDict(
    "CreateDefaultVpcResultTypeDef",
    {
        "Vpc": VpcTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVpcResultTypeDef = TypedDict(
    "CreateVpcResultTypeDef",
    {
        "Vpc": VpcTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcsResultTypeDef = TypedDict(
    "DescribeVpcsResultTypeDef",
    {
        "Vpcs": List[VpcTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptVpcPeeringConnectionResultTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionResultTypeDef",
    {
        "VpcPeeringConnection": VpcPeeringConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVpcPeeringConnectionResultTypeDef = TypedDict(
    "CreateVpcPeeringConnectionResultTypeDef",
    {
        "VpcPeeringConnection": VpcPeeringConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcPeeringConnectionsResultTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsResultTypeDef",
    {
        "VpcPeeringConnections": List[VpcPeeringConnectionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AccessScopeAnalysisFindingTypeDef = TypedDict(
    "AccessScopeAnalysisFindingTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": NotRequired[str],
        "NetworkInsightsAccessScopeId": NotRequired[str],
        "FindingId": NotRequired[str],
        "FindingComponents": NotRequired[List[PathComponentTypeDef]],
    },
)
NetworkInsightsAnalysisTypeDef = TypedDict(
    "NetworkInsightsAnalysisTypeDef",
    {
        "NetworkInsightsAnalysisId": NotRequired[str],
        "NetworkInsightsAnalysisArn": NotRequired[str],
        "NetworkInsightsPathId": NotRequired[str],
        "AdditionalAccounts": NotRequired[List[str]],
        "FilterInArns": NotRequired[List[str]],
        "StartDate": NotRequired[datetime],
        "Status": NotRequired[AnalysisStatusType],
        "StatusMessage": NotRequired[str],
        "WarningMessage": NotRequired[str],
        "NetworkPathFound": NotRequired[bool],
        "ForwardPathComponents": NotRequired[List[PathComponentTypeDef]],
        "ReturnPathComponents": NotRequired[List[PathComponentTypeDef]],
        "Explanations": NotRequired[List[ExplanationTypeDef]],
        "AlternatePathHints": NotRequired[List[AlternatePathHintTypeDef]],
        "SuggestedAccounts": NotRequired[List[str]],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
CreateNetworkInterfaceResultTypeDef = TypedDict(
    "CreateNetworkInterfaceResultTypeDef",
    {
        "NetworkInterface": NetworkInterfaceTypeDef,
        "ClientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNetworkInterfacesResultTypeDef = TypedDict(
    "DescribeNetworkInterfacesResultTypeDef",
    {
        "NetworkInterfaces": List[NetworkInterfaceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BundleInstanceResultTypeDef = TypedDict(
    "BundleInstanceResultTypeDef",
    {
        "BundleTask": BundleTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelBundleTaskResultTypeDef = TypedDict(
    "CancelBundleTaskResultTypeDef",
    {
        "BundleTask": BundleTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBundleTasksResultTypeDef = TypedDict(
    "DescribeBundleTasksResultTypeDef",
    {
        "BundleTasks": List[BundleTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVpnConnectionRequestRequestTypeDef = TypedDict(
    "CreateVpnConnectionRequestRequestTypeDef",
    {
        "CustomerGatewayId": str,
        "Type": str,
        "VpnGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "DryRun": NotRequired[bool],
        "Options": NotRequired[VpnConnectionOptionsSpecificationTypeDef],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
VpnConnectionTypeDef = TypedDict(
    "VpnConnectionTypeDef",
    {
        "CustomerGatewayConfiguration": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "Category": NotRequired[str],
        "State": NotRequired[VpnStateType],
        "Type": NotRequired[Literal["ipsec.1"]],
        "VpnConnectionId": NotRequired[str],
        "VpnGatewayId": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "CoreNetworkAttachmentArn": NotRequired[str],
        "GatewayAssociationState": NotRequired[GatewayAssociationStateType],
        "Options": NotRequired[VpnConnectionOptionsTypeDef],
        "Routes": NotRequired[List[VpnStaticRouteTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "VgwTelemetry": NotRequired[List[VgwTelemetryTypeDef]],
    },
)
DescribeConversionTasksResultTypeDef = TypedDict(
    "DescribeConversionTasksResultTypeDef",
    {
        "ConversionTasks": List[ConversionTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportInstanceResultTypeDef = TypedDict(
    "ImportInstanceResultTypeDef",
    {
        "ConversionTask": ConversionTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportVolumeResultTypeDef = TypedDict(
    "ImportVolumeResultTypeDef",
    {
        "ConversionTask": ConversionTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SpotInstanceRequestTypeDef = TypedDict(
    "SpotInstanceRequestTypeDef",
    {
        "ActualBlockHourlyPrice": NotRequired[str],
        "AvailabilityZoneGroup": NotRequired[str],
        "BlockDurationMinutes": NotRequired[int],
        "CreateTime": NotRequired[datetime],
        "Fault": NotRequired[SpotInstanceStateFaultTypeDef],
        "InstanceId": NotRequired[str],
        "LaunchGroup": NotRequired[str],
        "LaunchSpecification": NotRequired[LaunchSpecificationTypeDef],
        "LaunchedAvailabilityZone": NotRequired[str],
        "ProductDescription": NotRequired[RIProductDescriptionType],
        "SpotInstanceRequestId": NotRequired[str],
        "SpotPrice": NotRequired[str],
        "State": NotRequired[SpotInstanceStateType],
        "Status": NotRequired[SpotInstanceStatusTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "Type": NotRequired[SpotInstanceTypeType],
        "ValidFrom": NotRequired[datetime],
        "ValidUntil": NotRequired[datetime],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
    },
)
RequestSpotInstancesRequestRequestTypeDef = TypedDict(
    "RequestSpotInstancesRequestRequestTypeDef",
    {
        "AvailabilityZoneGroup": NotRequired[str],
        "BlockDurationMinutes": NotRequired[int],
        "ClientToken": NotRequired[str],
        "DryRun": NotRequired[bool],
        "InstanceCount": NotRequired[int],
        "LaunchGroup": NotRequired[str],
        "LaunchSpecification": NotRequired[RequestSpotLaunchSpecificationTypeDef],
        "SpotPrice": NotRequired[str],
        "Type": NotRequired[SpotInstanceTypeType],
        "ValidFrom": NotRequired[TimestampTypeDef],
        "ValidUntil": NotRequired[TimestampTypeDef],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
    },
)
CreateLaunchTemplateRequestRequestTypeDef = TypedDict(
    "CreateLaunchTemplateRequestRequestTypeDef",
    {
        "LaunchTemplateName": str,
        "LaunchTemplateData": RequestLaunchTemplateDataTypeDef,
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "VersionDescription": NotRequired[str],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
    },
)
CreateLaunchTemplateVersionRequestRequestTypeDef = TypedDict(
    "CreateLaunchTemplateVersionRequestRequestTypeDef",
    {
        "LaunchTemplateData": RequestLaunchTemplateDataTypeDef,
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "SourceVersion": NotRequired[str],
        "VersionDescription": NotRequired[str],
        "ResolveAlias": NotRequired[bool],
    },
)
DescribeInstanceTypesResultTypeDef = TypedDict(
    "DescribeInstanceTypesResultTypeDef",
    {
        "InstanceTypes": List[InstanceTypeInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AmiLaunchIndex": NotRequired[int],
        "ImageId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "LaunchTime": NotRequired[datetime],
        "Monitoring": NotRequired[MonitoringTypeDef],
        "Placement": NotRequired[PlacementTypeDef],
        "Platform": NotRequired[Literal["Windows"]],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "ProductCodes": NotRequired[List[ProductCodeTypeDef]],
        "PublicDnsName": NotRequired[str],
        "PublicIpAddress": NotRequired[str],
        "RamdiskId": NotRequired[str],
        "State": NotRequired[InstanceStateTypeDef],
        "StateTransitionReason": NotRequired[str],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Architecture": NotRequired[ArchitectureValuesType],
        "BlockDeviceMappings": NotRequired[List[InstanceBlockDeviceMappingTypeDef]],
        "ClientToken": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "EnaSupport": NotRequired[bool],
        "Hypervisor": NotRequired[HypervisorTypeType],
        "IamInstanceProfile": NotRequired[IamInstanceProfileTypeDef],
        "InstanceLifecycle": NotRequired[InstanceLifecycleTypeType],
        "ElasticGpuAssociations": NotRequired[List[ElasticGpuAssociationTypeDef]],
        "ElasticInferenceAcceleratorAssociations": NotRequired[
            List[ElasticInferenceAcceleratorAssociationTypeDef]
        ],
        "NetworkInterfaces": NotRequired[List[InstanceNetworkInterfaceTypeDef]],
        "OutpostArn": NotRequired[str],
        "RootDeviceName": NotRequired[str],
        "RootDeviceType": NotRequired[DeviceTypeType],
        "SecurityGroups": NotRequired[List[GroupIdentifierTypeDef]],
        "SourceDestCheck": NotRequired[bool],
        "SpotInstanceRequestId": NotRequired[str],
        "SriovNetSupport": NotRequired[str],
        "StateReason": NotRequired[StateReasonTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "VirtualizationType": NotRequired[VirtualizationTypeType],
        "CpuOptions": NotRequired[CpuOptionsTypeDef],
        "CapacityReservationId": NotRequired[str],
        "CapacityReservationSpecification": NotRequired[
            CapacityReservationSpecificationResponseTypeDef
        ],
        "HibernationOptions": NotRequired[HibernationOptionsTypeDef],
        "Licenses": NotRequired[List[LicenseConfigurationTypeDef]],
        "MetadataOptions": NotRequired[InstanceMetadataOptionsResponseTypeDef],
        "EnclaveOptions": NotRequired[EnclaveOptionsTypeDef],
        "BootMode": NotRequired[BootModeValuesType],
        "PlatformDetails": NotRequired[str],
        "UsageOperation": NotRequired[str],
        "UsageOperationUpdateTime": NotRequired[datetime],
        "PrivateDnsNameOptions": NotRequired[PrivateDnsNameOptionsResponseTypeDef],
        "Ipv6Address": NotRequired[str],
        "TpmSupport": NotRequired[str],
        "MaintenanceOptions": NotRequired[InstanceMaintenanceOptionsTypeDef],
        "CurrentInstanceBootMode": NotRequired[InstanceBootModeValuesType],
    },
)
CreateFleetRequestRequestTypeDef = TypedDict(
    "CreateFleetRequestRequestTypeDef",
    {
        "LaunchTemplateConfigs": Sequence[FleetLaunchTemplateConfigRequestTypeDef],
        "TargetCapacitySpecification": TargetCapacitySpecificationRequestTypeDef,
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
        "SpotOptions": NotRequired[SpotOptionsRequestTypeDef],
        "OnDemandOptions": NotRequired[OnDemandOptionsRequestTypeDef],
        "ExcessCapacityTerminationPolicy": NotRequired[FleetExcessCapacityTerminationPolicyType],
        "TerminateInstancesWithExpiration": NotRequired[bool],
        "Type": NotRequired[FleetTypeType],
        "ValidFrom": NotRequired[TimestampTypeDef],
        "ValidUntil": NotRequired[TimestampTypeDef],
        "ReplaceUnhealthyInstances": NotRequired[bool],
        "TagSpecifications": NotRequired[Sequence[TagSpecificationTypeDef]],
        "Context": NotRequired[str],
    },
)
ModifyFleetRequestRequestTypeDef = TypedDict(
    "ModifyFleetRequestRequestTypeDef",
    {
        "FleetId": str,
        "DryRun": NotRequired[bool],
        "ExcessCapacityTerminationPolicy": NotRequired[FleetExcessCapacityTerminationPolicyType],
        "LaunchTemplateConfigs": NotRequired[Sequence[FleetLaunchTemplateConfigRequestTypeDef]],
        "TargetCapacitySpecification": NotRequired[TargetCapacitySpecificationRequestTypeDef],
        "Context": NotRequired[str],
    },
)
CreateFleetErrorTypeDef = TypedDict(
    "CreateFleetErrorTypeDef",
    {
        "LaunchTemplateAndOverrides": NotRequired[LaunchTemplateAndOverridesResponseTypeDef],
        "Lifecycle": NotRequired[InstanceLifecycleType],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
CreateFleetInstanceTypeDef = TypedDict(
    "CreateFleetInstanceTypeDef",
    {
        "LaunchTemplateAndOverrides": NotRequired[LaunchTemplateAndOverridesResponseTypeDef],
        "Lifecycle": NotRequired[InstanceLifecycleType],
        "InstanceIds": NotRequired[List[str]],
        "InstanceType": NotRequired[InstanceTypeType],
        "Platform": NotRequired[Literal["Windows"]],
    },
)
DescribeFleetErrorTypeDef = TypedDict(
    "DescribeFleetErrorTypeDef",
    {
        "LaunchTemplateAndOverrides": NotRequired[LaunchTemplateAndOverridesResponseTypeDef],
        "Lifecycle": NotRequired[InstanceLifecycleType],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
DescribeFleetsInstancesTypeDef = TypedDict(
    "DescribeFleetsInstancesTypeDef",
    {
        "LaunchTemplateAndOverrides": NotRequired[LaunchTemplateAndOverridesResponseTypeDef],
        "Lifecycle": NotRequired[InstanceLifecycleType],
        "InstanceIds": NotRequired[List[str]],
        "InstanceType": NotRequired[InstanceTypeType],
        "Platform": NotRequired[Literal["Windows"]],
    },
)
ModifySpotFleetRequestRequestRequestTypeDef = TypedDict(
    "ModifySpotFleetRequestRequestRequestTypeDef",
    {
        "SpotFleetRequestId": str,
        "ExcessCapacityTerminationPolicy": NotRequired[ExcessCapacityTerminationPolicyType],
        "LaunchTemplateConfigs": NotRequired[Sequence[LaunchTemplateConfigTypeDef]],
        "TargetCapacity": NotRequired[int],
        "OnDemandTargetCapacity": NotRequired[int],
        "Context": NotRequired[str],
    },
)
SpotFleetRequestConfigDataPaginatorTypeDef = TypedDict(
    "SpotFleetRequestConfigDataPaginatorTypeDef",
    {
        "IamFleetRole": str,
        "TargetCapacity": int,
        "AllocationStrategy": NotRequired[AllocationStrategyType],
        "OnDemandAllocationStrategy": NotRequired[OnDemandAllocationStrategyType],
        "SpotMaintenanceStrategies": NotRequired[SpotMaintenanceStrategiesTypeDef],
        "ClientToken": NotRequired[str],
        "ExcessCapacityTerminationPolicy": NotRequired[ExcessCapacityTerminationPolicyType],
        "FulfilledCapacity": NotRequired[float],
        "OnDemandFulfilledCapacity": NotRequired[float],
        "LaunchSpecifications": NotRequired[List[SpotFleetLaunchSpecificationTypeDef]],
        "LaunchTemplateConfigs": NotRequired[List[LaunchTemplateConfigTypeDef]],
        "SpotPrice": NotRequired[str],
        "OnDemandTargetCapacity": NotRequired[int],
        "OnDemandMaxTotalPrice": NotRequired[str],
        "SpotMaxTotalPrice": NotRequired[str],
        "TerminateInstancesWithExpiration": NotRequired[bool],
        "Type": NotRequired[FleetTypeType],
        "ValidFrom": NotRequired[datetime],
        "ValidUntil": NotRequired[datetime],
        "ReplaceUnhealthyInstances": NotRequired[bool],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
        "LoadBalancersConfig": NotRequired[LoadBalancersConfigTypeDef],
        "InstancePoolsToUseCount": NotRequired[int],
        "Context": NotRequired[str],
        "TargetCapacityUnitType": NotRequired[TargetCapacityUnitTypeType],
        "TagSpecifications": NotRequired[List[TagSpecificationPaginatorTypeDef]],
    },
)
SpotFleetRequestConfigDataTypeDef = TypedDict(
    "SpotFleetRequestConfigDataTypeDef",
    {
        "IamFleetRole": str,
        "TargetCapacity": int,
        "AllocationStrategy": NotRequired[AllocationStrategyType],
        "OnDemandAllocationStrategy": NotRequired[OnDemandAllocationStrategyType],
        "SpotMaintenanceStrategies": NotRequired[SpotMaintenanceStrategiesTypeDef],
        "ClientToken": NotRequired[str],
        "ExcessCapacityTerminationPolicy": NotRequired[ExcessCapacityTerminationPolicyType],
        "FulfilledCapacity": NotRequired[float],
        "OnDemandFulfilledCapacity": NotRequired[float],
        "LaunchSpecifications": NotRequired[List[SpotFleetLaunchSpecificationTypeDef]],
        "LaunchTemplateConfigs": NotRequired[List[LaunchTemplateConfigTypeDef]],
        "SpotPrice": NotRequired[str],
        "OnDemandTargetCapacity": NotRequired[int],
        "OnDemandMaxTotalPrice": NotRequired[str],
        "SpotMaxTotalPrice": NotRequired[str],
        "TerminateInstancesWithExpiration": NotRequired[bool],
        "Type": NotRequired[FleetTypeType],
        "ValidFrom": NotRequired[datetime],
        "ValidUntil": NotRequired[datetime],
        "ReplaceUnhealthyInstances": NotRequired[bool],
        "InstanceInterruptionBehavior": NotRequired[InstanceInterruptionBehaviorType],
        "LoadBalancersConfig": NotRequired[LoadBalancersConfigTypeDef],
        "InstancePoolsToUseCount": NotRequired[int],
        "Context": NotRequired[str],
        "TargetCapacityUnitType": NotRequired[TargetCapacityUnitTypeType],
        "TagSpecifications": NotRequired[List[TagSpecificationTypeDef]],
    },
)
GetLaunchTemplateDataResultTypeDef = TypedDict(
    "GetLaunchTemplateDataResultTypeDef",
    {
        "LaunchTemplateData": ResponseLaunchTemplateDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LaunchTemplateVersionTypeDef = TypedDict(
    "LaunchTemplateVersionTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "VersionDescription": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
        "DefaultVersion": NotRequired[bool],
        "LaunchTemplateData": NotRequired[ResponseLaunchTemplateDataTypeDef],
    },
)
CreateNetworkInsightsAccessScopeResultTypeDef = TypedDict(
    "CreateNetworkInsightsAccessScopeResultTypeDef",
    {
        "NetworkInsightsAccessScope": NetworkInsightsAccessScopeTypeDef,
        "NetworkInsightsAccessScopeContent": NetworkInsightsAccessScopeContentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNetworkInsightsAccessScopeContentResultTypeDef = TypedDict(
    "GetNetworkInsightsAccessScopeContentResultTypeDef",
    {
        "NetworkInsightsAccessScopeContent": NetworkInsightsAccessScopeContentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef = TypedDict(
    "DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef",
    {
        "LoggingConfigurations": List[VerifiedAccessInstanceLoggingConfigurationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef = TypedDict(
    "ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef",
    {
        "LoggingConfiguration": VerifiedAccessInstanceLoggingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef = TypedDict(
    "GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "AnalysisStatus": AnalysisStatusType,
        "AnalysisFindings": List[AccessScopeAnalysisFindingTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNetworkInsightsAnalysesResultTypeDef = TypedDict(
    "DescribeNetworkInsightsAnalysesResultTypeDef",
    {
        "NetworkInsightsAnalyses": List[NetworkInsightsAnalysisTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartNetworkInsightsAnalysisResultTypeDef = TypedDict(
    "StartNetworkInsightsAnalysisResultTypeDef",
    {
        "NetworkInsightsAnalysis": NetworkInsightsAnalysisTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVpnConnectionResultTypeDef = TypedDict(
    "CreateVpnConnectionResultTypeDef",
    {
        "VpnConnection": VpnConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpnConnectionsResultTypeDef = TypedDict(
    "DescribeVpnConnectionsResultTypeDef",
    {
        "VpnConnections": List[VpnConnectionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpnConnectionOptionsResultTypeDef = TypedDict(
    "ModifyVpnConnectionOptionsResultTypeDef",
    {
        "VpnConnection": VpnConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpnConnectionResultTypeDef = TypedDict(
    "ModifyVpnConnectionResultTypeDef",
    {
        "VpnConnection": VpnConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpnTunnelCertificateResultTypeDef = TypedDict(
    "ModifyVpnTunnelCertificateResultTypeDef",
    {
        "VpnConnection": VpnConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyVpnTunnelOptionsResultTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsResultTypeDef",
    {
        "VpnConnection": VpnConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSpotInstanceRequestsResultTypeDef = TypedDict(
    "DescribeSpotInstanceRequestsResultTypeDef",
    {
        "SpotInstanceRequests": List[SpotInstanceRequestTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestSpotInstancesResultTypeDef = TypedDict(
    "RequestSpotInstancesResultTypeDef",
    {
        "SpotInstanceRequests": List[SpotInstanceRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReservationResponseTypeDef = TypedDict(
    "ReservationResponseTypeDef",
    {
        "Groups": List[GroupIdentifierTypeDef],
        "Instances": List[InstanceTypeDef],
        "OwnerId": str,
        "RequesterId": str,
        "ReservationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "Groups": NotRequired[List[GroupIdentifierTypeDef]],
        "Instances": NotRequired[List[InstanceTypeDef]],
        "OwnerId": NotRequired[str],
        "RequesterId": NotRequired[str],
        "ReservationId": NotRequired[str],
    },
)
CreateFleetResultTypeDef = TypedDict(
    "CreateFleetResultTypeDef",
    {
        "FleetId": str,
        "Errors": List[CreateFleetErrorTypeDef],
        "Instances": List[CreateFleetInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FleetDataTypeDef = TypedDict(
    "FleetDataTypeDef",
    {
        "ActivityStatus": NotRequired[FleetActivityStatusType],
        "CreateTime": NotRequired[datetime],
        "FleetId": NotRequired[str],
        "FleetState": NotRequired[FleetStateCodeType],
        "ClientToken": NotRequired[str],
        "ExcessCapacityTerminationPolicy": NotRequired[FleetExcessCapacityTerminationPolicyType],
        "FulfilledCapacity": NotRequired[float],
        "FulfilledOnDemandCapacity": NotRequired[float],
        "LaunchTemplateConfigs": NotRequired[List[FleetLaunchTemplateConfigTypeDef]],
        "TargetCapacitySpecification": NotRequired[TargetCapacitySpecificationTypeDef],
        "TerminateInstancesWithExpiration": NotRequired[bool],
        "Type": NotRequired[FleetTypeType],
        "ValidFrom": NotRequired[datetime],
        "ValidUntil": NotRequired[datetime],
        "ReplaceUnhealthyInstances": NotRequired[bool],
        "SpotOptions": NotRequired[SpotOptionsTypeDef],
        "OnDemandOptions": NotRequired[OnDemandOptionsTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "Errors": NotRequired[List[DescribeFleetErrorTypeDef]],
        "Instances": NotRequired[List[DescribeFleetsInstancesTypeDef]],
        "Context": NotRequired[str],
    },
)
SpotFleetRequestConfigPaginatorTypeDef = TypedDict(
    "SpotFleetRequestConfigPaginatorTypeDef",
    {
        "ActivityStatus": NotRequired[ActivityStatusType],
        "CreateTime": NotRequired[datetime],
        "SpotFleetRequestConfig": NotRequired[SpotFleetRequestConfigDataPaginatorTypeDef],
        "SpotFleetRequestId": NotRequired[str],
        "SpotFleetRequestState": NotRequired[BatchStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
RequestSpotFleetRequestRequestTypeDef = TypedDict(
    "RequestSpotFleetRequestRequestTypeDef",
    {
        "SpotFleetRequestConfig": SpotFleetRequestConfigDataTypeDef,
        "DryRun": NotRequired[bool],
    },
)
SpotFleetRequestConfigTypeDef = TypedDict(
    "SpotFleetRequestConfigTypeDef",
    {
        "ActivityStatus": NotRequired[ActivityStatusType],
        "CreateTime": NotRequired[datetime],
        "SpotFleetRequestConfig": NotRequired[SpotFleetRequestConfigDataTypeDef],
        "SpotFleetRequestId": NotRequired[str],
        "SpotFleetRequestState": NotRequired[BatchStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
CreateLaunchTemplateVersionResultTypeDef = TypedDict(
    "CreateLaunchTemplateVersionResultTypeDef",
    {
        "LaunchTemplateVersion": LaunchTemplateVersionTypeDef,
        "Warning": ValidationWarningTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLaunchTemplateVersionsResultTypeDef = TypedDict(
    "DescribeLaunchTemplateVersionsResultTypeDef",
    {
        "LaunchTemplateVersions": List[LaunchTemplateVersionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstancesResultTypeDef = TypedDict(
    "DescribeInstancesResultTypeDef",
    {
        "Reservations": List[ReservationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFleetsResultTypeDef = TypedDict(
    "DescribeFleetsResultTypeDef",
    {
        "NextToken": str,
        "Fleets": List[FleetDataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSpotFleetRequestsResponsePaginatorTypeDef = TypedDict(
    "DescribeSpotFleetRequestsResponsePaginatorTypeDef",
    {
        "NextToken": str,
        "SpotFleetRequestConfigs": List[SpotFleetRequestConfigPaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSpotFleetRequestsResponseTypeDef = TypedDict(
    "DescribeSpotFleetRequestsResponseTypeDef",
    {
        "NextToken": str,
        "SpotFleetRequestConfigs": List[SpotFleetRequestConfigTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
