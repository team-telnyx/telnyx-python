# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping, Iterable
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import (
    client_get_object_params,
    client_put_object_params,
    client_list_objects_params,
    client_create_bucket_params,
    client_delete_objects_params,
)
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NoneType,
    NotGiven,
    FileTypes,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .resources import (
    ips,
    enum,
    list,
    seti,
    fqdns,
    media,
    balance,
    regions,
    comments,
    invoices,
    webhooks,
    documents,
    messsages,
    user_tags,
    global_ips,
    call_events,
    connections,
    ota_updates,
    short_codes,
    audit_events,
    requirements,
    channel_zones,
    number_lookup,
    number_orders,
    usage_reports,
    billing_groups,
    detail_records,
    document_links,
    ip_connections,
    text_to_speech,
    user_addresses,
    advanced_orders,
    charges_summary,
    global_ip_usage,
    room_recordings,
    sim_card_orders,
    verify_profiles,
    wireguard_peers,
    access_ip_ranges,
    country_coverage,
    fax_applications,
    fqdn_connections,
    inbound_channels,
    network_coverage,
    numbers_features,
    access_ip_address,
    charges_breakdown,
    global_ip_latency,
    messaging_optouts,
    partner_campaigns,
    requirement_types,
    room_compositions,
    room_participants,
    siprec_connectors,
    sub_number_orders,
    inventory_coverage,
    portability_checks,
    requirement_groups,
    texml_applications,
    webhook_deliveries,
    global_ip_protocols,
    integration_secrets,
    notification_events,
    number_block_orders,
    wireless_blocklists,
    wireguard_interfaces,
    bulk_sim_card_actions,
    global_ip_assignments,
    messaging_url_domains,
    notification_channels,
    notification_profiles,
    notification_settings,
    porting_phone_numbers,
    telephony_credentials,
    dialogflow_connections,
    phone_number_campaigns,
    sim_card_order_preview,
    virtual_cross_connects,
    available_phone_numbers,
    global_ip_allowed_ports,
    global_ip_health_checks,
    mobile_push_credentials,
    outbound_voice_profiles,
    regulatory_requirements,
    authentication_providers,
    customer_service_records,
    messaging_hosted_numbers,
    mobile_network_operators,
    public_internet_gateways,
    recording_transcriptions,
    sub_number_orders_report,
    call_control_applications,
    private_wireless_gateways,
    wireless_blocklist_values,
    custom_storage_credentials,
    number_order_phone_numbers,
    dynamic_emergency_addresses,
    dynamic_emergency_endpoints,
    global_ip_assignment_health,
    global_ip_assignments_usage,
    global_ip_health_check_types,
    ledger_billing_group_reports,
    available_phone_number_blocks,
    notification_event_conditions,
    messaging_numbers_bulk_updates,
    virtual_cross_connects_coverage,
    sim_card_data_usage_notifications,
    phone_number_assignment_by_profile,
    phone_numbers_regulatory_requirements,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import TelnyxError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.ai import ai
from .resources.brand import brand
from .resources.calls import calls
from .resources.faxes import faxes
from .resources.rooms import rooms
from .resources.texml import texml
from .resources.queues import queues
from .resources.actions import actions
from .resources.payment import payment
from .resources.porting import porting
from .resources.reports import reports
from .resources.storage import storage
from .resources.campaign import campaign
from .resources.messages import messages
from .resources.networks import networks
from .resources.portouts import portouts
from .resources.wireless import wireless
from .resources.addresses import addresses
from .resources.messaging import messaging
from .resources.sim_cards import sim_cards
from .resources.recordings import recordings
from .resources.conferences import conferences
from .resources.phone_numbers import phone_numbers
from .resources.verifications import verifications
from .resources.bundle_pricing import bundle_pricing
from .resources.porting_orders import porting_orders
from .resources.sim_card_groups import sim_card_groups
from .resources.campaign_builder import campaign_builder
from .resources.managed_accounts import managed_accounts
from .resources.operator_connect import operator_connect
from .resources.verified_numbers import verified_numbers
from .types.list_buckets_response import ListBucketsResponse
from .types.list_objects_response import ListObjectsResponse
from .resources.messaging_profiles import messaging_profiles
from .resources.messaging_tollfree import messaging_tollfree
from .resources.number_reservations import number_reservations
from .resources.phone_number_blocks import phone_number_blocks
from .resources.external_connections import external_connections
from .resources.credential_connections import credential_connections
from .resources.messaging_hosted_number_orders import messaging_hosted_number_orders

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Telnyx", "AsyncTelnyx", "Client", "AsyncClient"]


class Telnyx(SyncAPIClient):
    webhooks: webhooks.WebhooksResource
    access_ip_address: access_ip_address.AccessIPAddressResource
    access_ip_ranges: access_ip_ranges.AccessIPRangesResource
    actions: actions.ActionsResource
    addresses: addresses.AddressesResource
    advanced_orders: advanced_orders.AdvancedOrdersResource
    ai: ai.AIResource
    audit_events: audit_events.AuditEventsResource
    authentication_providers: authentication_providers.AuthenticationProvidersResource
    available_phone_number_blocks: available_phone_number_blocks.AvailablePhoneNumberBlocksResource
    available_phone_numbers: available_phone_numbers.AvailablePhoneNumbersResource
    balance: balance.BalanceResource
    billing_groups: billing_groups.BillingGroupsResource
    brand: brand.BrandResource
    bulk_sim_card_actions: bulk_sim_card_actions.BulkSimCardActionsResource
    bundle_pricing: bundle_pricing.BundlePricingResource
    call_control_applications: call_control_applications.CallControlApplicationsResource
    call_events: call_events.CallEventsResource
    calls: calls.CallsResource
    campaign: campaign.CampaignResource
    campaign_builder: campaign_builder.CampaignBuilderResource
    channel_zones: channel_zones.ChannelZonesResource
    charges_breakdown: charges_breakdown.ChargesBreakdownResource
    charges_summary: charges_summary.ChargesSummaryResource
    comments: comments.CommentsResource
    conferences: conferences.ConferencesResource
    connections: connections.ConnectionsResource
    country_coverage: country_coverage.CountryCoverageResource
    credential_connections: credential_connections.CredentialConnectionsResource
    custom_storage_credentials: custom_storage_credentials.CustomStorageCredentialsResource
    customer_service_records: customer_service_records.CustomerServiceRecordsResource
    detail_records: detail_records.DetailRecordsResource
    dialogflow_connections: dialogflow_connections.DialogflowConnectionsResource
    document_links: document_links.DocumentLinksResource
    documents: documents.DocumentsResource
    dynamic_emergency_addresses: dynamic_emergency_addresses.DynamicEmergencyAddressesResource
    dynamic_emergency_endpoints: dynamic_emergency_endpoints.DynamicEmergencyEndpointsResource
    enum: enum.EnumResource
    external_connections: external_connections.ExternalConnectionsResource
    fax_applications: fax_applications.FaxApplicationsResource
    faxes: faxes.FaxesResource
    fqdn_connections: fqdn_connections.FqdnConnectionsResource
    fqdns: fqdns.FqdnsResource
    global_ip_allowed_ports: global_ip_allowed_ports.GlobalIPAllowedPortsResource
    global_ip_assignment_health: global_ip_assignment_health.GlobalIPAssignmentHealthResource
    global_ip_assignments: global_ip_assignments.GlobalIPAssignmentsResource
    global_ip_assignments_usage: global_ip_assignments_usage.GlobalIPAssignmentsUsageResource
    global_ip_health_check_types: global_ip_health_check_types.GlobalIPHealthCheckTypesResource
    global_ip_health_checks: global_ip_health_checks.GlobalIPHealthChecksResource
    global_ip_latency: global_ip_latency.GlobalIPLatencyResource
    global_ip_protocols: global_ip_protocols.GlobalIPProtocolsResource
    global_ip_usage: global_ip_usage.GlobalIPUsageResource
    global_ips: global_ips.GlobalIPsResource
    inbound_channels: inbound_channels.InboundChannelsResource
    integration_secrets: integration_secrets.IntegrationSecretsResource
    inventory_coverage: inventory_coverage.InventoryCoverageResource
    invoices: invoices.InvoicesResource
    ip_connections: ip_connections.IPConnectionsResource
    ips: ips.IPsResource
    ledger_billing_group_reports: ledger_billing_group_reports.LedgerBillingGroupReportsResource
    list: list.ListResource
    managed_accounts: managed_accounts.ManagedAccountsResource
    media: media.MediaResource
    messages: messages.MessagesResource
    messaging: messaging.MessagingResource
    messaging_hosted_number_orders: messaging_hosted_number_orders.MessagingHostedNumberOrdersResource
    messaging_hosted_numbers: messaging_hosted_numbers.MessagingHostedNumbersResource
    messaging_numbers_bulk_updates: messaging_numbers_bulk_updates.MessagingNumbersBulkUpdatesResource
    messaging_optouts: messaging_optouts.MessagingOptoutsResource
    messaging_profiles: messaging_profiles.MessagingProfilesResource
    messaging_tollfree: messaging_tollfree.MessagingTollfreeResource
    messaging_url_domains: messaging_url_domains.MessagingURLDomainsResource
    messsages: messsages.MesssagesResource
    mobile_network_operators: mobile_network_operators.MobileNetworkOperatorsResource
    mobile_push_credentials: mobile_push_credentials.MobilePushCredentialsResource
    network_coverage: network_coverage.NetworkCoverageResource
    networks: networks.NetworksResource
    notification_channels: notification_channels.NotificationChannelsResource
    notification_event_conditions: notification_event_conditions.NotificationEventConditionsResource
    notification_events: notification_events.NotificationEventsResource
    notification_profiles: notification_profiles.NotificationProfilesResource
    notification_settings: notification_settings.NotificationSettingsResource
    number_block_orders: number_block_orders.NumberBlockOrdersResource
    number_lookup: number_lookup.NumberLookupResource
    number_order_phone_numbers: number_order_phone_numbers.NumberOrderPhoneNumbersResource
    number_orders: number_orders.NumberOrdersResource
    number_reservations: number_reservations.NumberReservationsResource
    numbers_features: numbers_features.NumbersFeaturesResource
    operator_connect: operator_connect.OperatorConnectResource
    ota_updates: ota_updates.OtaUpdatesResource
    outbound_voice_profiles: outbound_voice_profiles.OutboundVoiceProfilesResource
    payment: payment.PaymentResource
    phone_number_assignment_by_profile: phone_number_assignment_by_profile.PhoneNumberAssignmentByProfileResource
    phone_number_blocks: phone_number_blocks.PhoneNumberBlocksResource
    phone_number_campaigns: phone_number_campaigns.PhoneNumberCampaignsResource
    phone_numbers: phone_numbers.PhoneNumbersResource
    phone_numbers_regulatory_requirements: (
        phone_numbers_regulatory_requirements.PhoneNumbersRegulatoryRequirementsResource
    )
    portability_checks: portability_checks.PortabilityChecksResource
    porting: porting.PortingResource
    porting_orders: porting_orders.PortingOrdersResource
    porting_phone_numbers: porting_phone_numbers.PortingPhoneNumbersResource
    portouts: portouts.PortoutsResource
    private_wireless_gateways: private_wireless_gateways.PrivateWirelessGatewaysResource
    public_internet_gateways: public_internet_gateways.PublicInternetGatewaysResource
    queues: queues.QueuesResource
    recording_transcriptions: recording_transcriptions.RecordingTranscriptionsResource
    recordings: recordings.RecordingsResource
    regions: regions.RegionsResource
    regulatory_requirements: regulatory_requirements.RegulatoryRequirementsResource
    reports: reports.ReportsResource
    requirement_groups: requirement_groups.RequirementGroupsResource
    requirement_types: requirement_types.RequirementTypesResource
    requirements: requirements.RequirementsResource
    room_compositions: room_compositions.RoomCompositionsResource
    room_participants: room_participants.RoomParticipantsResource
    room_recordings: room_recordings.RoomRecordingsResource
    rooms: rooms.RoomsResource
    seti: seti.SetiResource
    short_codes: short_codes.ShortCodesResource
    sim_card_data_usage_notifications: sim_card_data_usage_notifications.SimCardDataUsageNotificationsResource
    sim_card_groups: sim_card_groups.SimCardGroupsResource
    sim_card_order_preview: sim_card_order_preview.SimCardOrderPreviewResource
    sim_card_orders: sim_card_orders.SimCardOrdersResource
    sim_cards: sim_cards.SimCardsResource
    siprec_connectors: siprec_connectors.SiprecConnectorsResource
    storage: storage.StorageResource
    sub_number_orders: sub_number_orders.SubNumberOrdersResource
    sub_number_orders_report: sub_number_orders_report.SubNumberOrdersReportResource
    telephony_credentials: telephony_credentials.TelephonyCredentialsResource
    texml: texml.TexmlResource
    texml_applications: texml_applications.TexmlApplicationsResource
    text_to_speech: text_to_speech.TextToSpeechResource
    usage_reports: usage_reports.UsageReportsResource
    user_addresses: user_addresses.UserAddressesResource
    user_tags: user_tags.UserTagsResource
    verifications: verifications.VerificationsResource
    verified_numbers: verified_numbers.VerifiedNumbersResource
    verify_profiles: verify_profiles.VerifyProfilesResource
    virtual_cross_connects: virtual_cross_connects.VirtualCrossConnectsResource
    virtual_cross_connects_coverage: virtual_cross_connects_coverage.VirtualCrossConnectsCoverageResource
    webhook_deliveries: webhook_deliveries.WebhookDeliveriesResource
    wireguard_interfaces: wireguard_interfaces.WireguardInterfacesResource
    wireguard_peers: wireguard_peers.WireguardPeersResource
    wireless: wireless.WirelessResource
    wireless_blocklist_values: wireless_blocklist_values.WirelessBlocklistValuesResource
    wireless_blocklists: wireless_blocklists.WirelessBlocklistsResource
    partner_campaigns: partner_campaigns.PartnerCampaignsResource
    with_raw_response: TelnyxWithRawResponse
    with_streaming_response: TelnyxWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Telnyx client instance.

        This automatically infers the `api_key` argument from the `TELNYX_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("TELNYX_API_KEY")
        if api_key is None:
            raise TelnyxError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TELNYX_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("TELNYX_BASE_URL")
        if base_url is None:
            base_url = f"https://api.telnyx.com/v2"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.webhooks = webhooks.WebhooksResource(self)
        self.access_ip_address = access_ip_address.AccessIPAddressResource(self)
        self.access_ip_ranges = access_ip_ranges.AccessIPRangesResource(self)
        self.actions = actions.ActionsResource(self)
        self.addresses = addresses.AddressesResource(self)
        self.advanced_orders = advanced_orders.AdvancedOrdersResource(self)
        self.ai = ai.AIResource(self)
        self.audit_events = audit_events.AuditEventsResource(self)
        self.authentication_providers = authentication_providers.AuthenticationProvidersResource(self)
        self.available_phone_number_blocks = available_phone_number_blocks.AvailablePhoneNumberBlocksResource(self)
        self.available_phone_numbers = available_phone_numbers.AvailablePhoneNumbersResource(self)
        self.balance = balance.BalanceResource(self)
        self.billing_groups = billing_groups.BillingGroupsResource(self)
        self.brand = brand.BrandResource(self)
        self.bulk_sim_card_actions = bulk_sim_card_actions.BulkSimCardActionsResource(self)
        self.bundle_pricing = bundle_pricing.BundlePricingResource(self)
        self.call_control_applications = call_control_applications.CallControlApplicationsResource(self)
        self.call_events = call_events.CallEventsResource(self)
        self.calls = calls.CallsResource(self)
        self.campaign = campaign.CampaignResource(self)
        self.campaign_builder = campaign_builder.CampaignBuilderResource(self)
        self.channel_zones = channel_zones.ChannelZonesResource(self)
        self.charges_breakdown = charges_breakdown.ChargesBreakdownResource(self)
        self.charges_summary = charges_summary.ChargesSummaryResource(self)
        self.comments = comments.CommentsResource(self)
        self.conferences = conferences.ConferencesResource(self)
        self.connections = connections.ConnectionsResource(self)
        self.country_coverage = country_coverage.CountryCoverageResource(self)
        self.credential_connections = credential_connections.CredentialConnectionsResource(self)
        self.custom_storage_credentials = custom_storage_credentials.CustomStorageCredentialsResource(self)
        self.customer_service_records = customer_service_records.CustomerServiceRecordsResource(self)
        self.detail_records = detail_records.DetailRecordsResource(self)
        self.dialogflow_connections = dialogflow_connections.DialogflowConnectionsResource(self)
        self.document_links = document_links.DocumentLinksResource(self)
        self.documents = documents.DocumentsResource(self)
        self.dynamic_emergency_addresses = dynamic_emergency_addresses.DynamicEmergencyAddressesResource(self)
        self.dynamic_emergency_endpoints = dynamic_emergency_endpoints.DynamicEmergencyEndpointsResource(self)
        self.enum = enum.EnumResource(self)
        self.external_connections = external_connections.ExternalConnectionsResource(self)
        self.fax_applications = fax_applications.FaxApplicationsResource(self)
        self.faxes = faxes.FaxesResource(self)
        self.fqdn_connections = fqdn_connections.FqdnConnectionsResource(self)
        self.fqdns = fqdns.FqdnsResource(self)
        self.global_ip_allowed_ports = global_ip_allowed_ports.GlobalIPAllowedPortsResource(self)
        self.global_ip_assignment_health = global_ip_assignment_health.GlobalIPAssignmentHealthResource(self)
        self.global_ip_assignments = global_ip_assignments.GlobalIPAssignmentsResource(self)
        self.global_ip_assignments_usage = global_ip_assignments_usage.GlobalIPAssignmentsUsageResource(self)
        self.global_ip_health_check_types = global_ip_health_check_types.GlobalIPHealthCheckTypesResource(self)
        self.global_ip_health_checks = global_ip_health_checks.GlobalIPHealthChecksResource(self)
        self.global_ip_latency = global_ip_latency.GlobalIPLatencyResource(self)
        self.global_ip_protocols = global_ip_protocols.GlobalIPProtocolsResource(self)
        self.global_ip_usage = global_ip_usage.GlobalIPUsageResource(self)
        self.global_ips = global_ips.GlobalIPsResource(self)
        self.inbound_channels = inbound_channels.InboundChannelsResource(self)
        self.integration_secrets = integration_secrets.IntegrationSecretsResource(self)
        self.inventory_coverage = inventory_coverage.InventoryCoverageResource(self)
        self.invoices = invoices.InvoicesResource(self)
        self.ip_connections = ip_connections.IPConnectionsResource(self)
        self.ips = ips.IPsResource(self)
        self.ledger_billing_group_reports = ledger_billing_group_reports.LedgerBillingGroupReportsResource(self)
        self.list = list.ListResource(self)
        self.managed_accounts = managed_accounts.ManagedAccountsResource(self)
        self.media = media.MediaResource(self)
        self.messages = messages.MessagesResource(self)
        self.messaging = messaging.MessagingResource(self)
        self.messaging_hosted_number_orders = messaging_hosted_number_orders.MessagingHostedNumberOrdersResource(self)
        self.messaging_hosted_numbers = messaging_hosted_numbers.MessagingHostedNumbersResource(self)
        self.messaging_numbers_bulk_updates = messaging_numbers_bulk_updates.MessagingNumbersBulkUpdatesResource(self)
        self.messaging_optouts = messaging_optouts.MessagingOptoutsResource(self)
        self.messaging_profiles = messaging_profiles.MessagingProfilesResource(self)
        self.messaging_tollfree = messaging_tollfree.MessagingTollfreeResource(self)
        self.messaging_url_domains = messaging_url_domains.MessagingURLDomainsResource(self)
        self.messsages = messsages.MesssagesResource(self)
        self.mobile_network_operators = mobile_network_operators.MobileNetworkOperatorsResource(self)
        self.mobile_push_credentials = mobile_push_credentials.MobilePushCredentialsResource(self)
        self.network_coverage = network_coverage.NetworkCoverageResource(self)
        self.networks = networks.NetworksResource(self)
        self.notification_channels = notification_channels.NotificationChannelsResource(self)
        self.notification_event_conditions = notification_event_conditions.NotificationEventConditionsResource(self)
        self.notification_events = notification_events.NotificationEventsResource(self)
        self.notification_profiles = notification_profiles.NotificationProfilesResource(self)
        self.notification_settings = notification_settings.NotificationSettingsResource(self)
        self.number_block_orders = number_block_orders.NumberBlockOrdersResource(self)
        self.number_lookup = number_lookup.NumberLookupResource(self)
        self.number_order_phone_numbers = number_order_phone_numbers.NumberOrderPhoneNumbersResource(self)
        self.number_orders = number_orders.NumberOrdersResource(self)
        self.number_reservations = number_reservations.NumberReservationsResource(self)
        self.numbers_features = numbers_features.NumbersFeaturesResource(self)
        self.operator_connect = operator_connect.OperatorConnectResource(self)
        self.ota_updates = ota_updates.OtaUpdatesResource(self)
        self.outbound_voice_profiles = outbound_voice_profiles.OutboundVoiceProfilesResource(self)
        self.payment = payment.PaymentResource(self)
        self.phone_number_assignment_by_profile = (
            phone_number_assignment_by_profile.PhoneNumberAssignmentByProfileResource(self)
        )
        self.phone_number_blocks = phone_number_blocks.PhoneNumberBlocksResource(self)
        self.phone_number_campaigns = phone_number_campaigns.PhoneNumberCampaignsResource(self)
        self.phone_numbers = phone_numbers.PhoneNumbersResource(self)
        self.phone_numbers_regulatory_requirements = (
            phone_numbers_regulatory_requirements.PhoneNumbersRegulatoryRequirementsResource(self)
        )
        self.portability_checks = portability_checks.PortabilityChecksResource(self)
        self.porting = porting.PortingResource(self)
        self.porting_orders = porting_orders.PortingOrdersResource(self)
        self.porting_phone_numbers = porting_phone_numbers.PortingPhoneNumbersResource(self)
        self.portouts = portouts.PortoutsResource(self)
        self.private_wireless_gateways = private_wireless_gateways.PrivateWirelessGatewaysResource(self)
        self.public_internet_gateways = public_internet_gateways.PublicInternetGatewaysResource(self)
        self.queues = queues.QueuesResource(self)
        self.recording_transcriptions = recording_transcriptions.RecordingTranscriptionsResource(self)
        self.recordings = recordings.RecordingsResource(self)
        self.regions = regions.RegionsResource(self)
        self.regulatory_requirements = regulatory_requirements.RegulatoryRequirementsResource(self)
        self.reports = reports.ReportsResource(self)
        self.requirement_groups = requirement_groups.RequirementGroupsResource(self)
        self.requirement_types = requirement_types.RequirementTypesResource(self)
        self.requirements = requirements.RequirementsResource(self)
        self.room_compositions = room_compositions.RoomCompositionsResource(self)
        self.room_participants = room_participants.RoomParticipantsResource(self)
        self.room_recordings = room_recordings.RoomRecordingsResource(self)
        self.rooms = rooms.RoomsResource(self)
        self.seti = seti.SetiResource(self)
        self.short_codes = short_codes.ShortCodesResource(self)
        self.sim_card_data_usage_notifications = (
            sim_card_data_usage_notifications.SimCardDataUsageNotificationsResource(self)
        )
        self.sim_card_groups = sim_card_groups.SimCardGroupsResource(self)
        self.sim_card_order_preview = sim_card_order_preview.SimCardOrderPreviewResource(self)
        self.sim_card_orders = sim_card_orders.SimCardOrdersResource(self)
        self.sim_cards = sim_cards.SimCardsResource(self)
        self.siprec_connectors = siprec_connectors.SiprecConnectorsResource(self)
        self.storage = storage.StorageResource(self)
        self.sub_number_orders = sub_number_orders.SubNumberOrdersResource(self)
        self.sub_number_orders_report = sub_number_orders_report.SubNumberOrdersReportResource(self)
        self.telephony_credentials = telephony_credentials.TelephonyCredentialsResource(self)
        self.texml = texml.TexmlResource(self)
        self.texml_applications = texml_applications.TexmlApplicationsResource(self)
        self.text_to_speech = text_to_speech.TextToSpeechResource(self)
        self.usage_reports = usage_reports.UsageReportsResource(self)
        self.user_addresses = user_addresses.UserAddressesResource(self)
        self.user_tags = user_tags.UserTagsResource(self)
        self.verifications = verifications.VerificationsResource(self)
        self.verified_numbers = verified_numbers.VerifiedNumbersResource(self)
        self.verify_profiles = verify_profiles.VerifyProfilesResource(self)
        self.virtual_cross_connects = virtual_cross_connects.VirtualCrossConnectsResource(self)
        self.virtual_cross_connects_coverage = virtual_cross_connects_coverage.VirtualCrossConnectsCoverageResource(
            self
        )
        self.webhook_deliveries = webhook_deliveries.WebhookDeliveriesResource(self)
        self.wireguard_interfaces = wireguard_interfaces.WireguardInterfacesResource(self)
        self.wireguard_peers = wireguard_peers.WireguardPeersResource(self)
        self.wireless = wireless.WirelessResource(self)
        self.wireless_blocklist_values = wireless_blocklist_values.WirelessBlocklistValuesResource(self)
        self.wireless_blocklists = wireless_blocklists.WirelessBlocklistsResource(self)
        self.partner_campaigns = partner_campaigns.PartnerCampaignsResource(self)
        self.with_raw_response = TelnyxWithRawResponse(self)
        self.with_streaming_response = TelnyxWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def create_bucket(
        self,
        bucket_name: str,
        *,
        location_constraint: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create a bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self.put(
            f"/{bucket_name}",
            body=maybe_transform(
                {"location_constraint": location_constraint}, client_create_bucket_params.ClientCreateBucketParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_bucket(
        self,
        bucket_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a bucket.

        The bucket must be empty for it to be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self.delete(
            f"/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_object(
        self,
        object_name: str,
        *,
        bucket_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an object from a given bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self.delete(
            f"/{bucket_name}/{object_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_objects(
        self,
        bucket_name: str,
        *,
        delete: Literal[True],
        body: Iterable[client_delete_objects_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes one or multiple objects from a given bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "application/xml", **(extra_headers or {})}
        return self.post(
            f"/{bucket_name}",
            body=maybe_transform(body, Iterable[client_delete_objects_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"delete": delete}, client_delete_objects_params.ClientDeleteObjectsParams),
            ),
            cast_to=object,
        )

    def get_object(
        self,
        object_name: str,
        *,
        bucket_name: str,
        upload_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Retrieves an object from a given bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self.get(
            f"/{bucket_name}/{object_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"upload_id": upload_id}, client_get_object_params.ClientGetObjectParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def list_buckets(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListBucketsResponse:
        """List all Buckets."""
        extra_headers = {"Accept": "application/xml", **(extra_headers or {})}
        return self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListBucketsResponse,
        )

    def list_objects(
        self,
        bucket_name: str,
        *,
        list_type: Literal[2] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListObjectsResponse:
        """
        List all objects contained in a given bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "application/xml", **(extra_headers or {})}
        return self.get(
            f"/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"list_type": list_type}, client_list_objects_params.ClientListObjectsParams),
            ),
            cast_to=ListObjectsResponse,
        )

    def put_object(
        self,
        object_name: str,
        *,
        bucket_name: str,
        body: FileTypes,
        part_number: str | NotGiven = NOT_GIVEN,
        upload_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Add an object to a bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self.put(
            f"/{bucket_name}/{object_name}",
            body=maybe_transform(body, client_put_object_params.ClientPutObjectParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "part_number": part_number,
                        "upload_id": upload_id,
                    },
                    client_put_object_params.ClientPutObjectParams,
                ),
            ),
            cast_to=NoneType,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTelnyx(AsyncAPIClient):
    webhooks: webhooks.AsyncWebhooksResource
    access_ip_address: access_ip_address.AsyncAccessIPAddressResource
    access_ip_ranges: access_ip_ranges.AsyncAccessIPRangesResource
    actions: actions.AsyncActionsResource
    addresses: addresses.AsyncAddressesResource
    advanced_orders: advanced_orders.AsyncAdvancedOrdersResource
    ai: ai.AsyncAIResource
    audit_events: audit_events.AsyncAuditEventsResource
    authentication_providers: authentication_providers.AsyncAuthenticationProvidersResource
    available_phone_number_blocks: available_phone_number_blocks.AsyncAvailablePhoneNumberBlocksResource
    available_phone_numbers: available_phone_numbers.AsyncAvailablePhoneNumbersResource
    balance: balance.AsyncBalanceResource
    billing_groups: billing_groups.AsyncBillingGroupsResource
    brand: brand.AsyncBrandResource
    bulk_sim_card_actions: bulk_sim_card_actions.AsyncBulkSimCardActionsResource
    bundle_pricing: bundle_pricing.AsyncBundlePricingResource
    call_control_applications: call_control_applications.AsyncCallControlApplicationsResource
    call_events: call_events.AsyncCallEventsResource
    calls: calls.AsyncCallsResource
    campaign: campaign.AsyncCampaignResource
    campaign_builder: campaign_builder.AsyncCampaignBuilderResource
    channel_zones: channel_zones.AsyncChannelZonesResource
    charges_breakdown: charges_breakdown.AsyncChargesBreakdownResource
    charges_summary: charges_summary.AsyncChargesSummaryResource
    comments: comments.AsyncCommentsResource
    conferences: conferences.AsyncConferencesResource
    connections: connections.AsyncConnectionsResource
    country_coverage: country_coverage.AsyncCountryCoverageResource
    credential_connections: credential_connections.AsyncCredentialConnectionsResource
    custom_storage_credentials: custom_storage_credentials.AsyncCustomStorageCredentialsResource
    customer_service_records: customer_service_records.AsyncCustomerServiceRecordsResource
    detail_records: detail_records.AsyncDetailRecordsResource
    dialogflow_connections: dialogflow_connections.AsyncDialogflowConnectionsResource
    document_links: document_links.AsyncDocumentLinksResource
    documents: documents.AsyncDocumentsResource
    dynamic_emergency_addresses: dynamic_emergency_addresses.AsyncDynamicEmergencyAddressesResource
    dynamic_emergency_endpoints: dynamic_emergency_endpoints.AsyncDynamicEmergencyEndpointsResource
    enum: enum.AsyncEnumResource
    external_connections: external_connections.AsyncExternalConnectionsResource
    fax_applications: fax_applications.AsyncFaxApplicationsResource
    faxes: faxes.AsyncFaxesResource
    fqdn_connections: fqdn_connections.AsyncFqdnConnectionsResource
    fqdns: fqdns.AsyncFqdnsResource
    global_ip_allowed_ports: global_ip_allowed_ports.AsyncGlobalIPAllowedPortsResource
    global_ip_assignment_health: global_ip_assignment_health.AsyncGlobalIPAssignmentHealthResource
    global_ip_assignments: global_ip_assignments.AsyncGlobalIPAssignmentsResource
    global_ip_assignments_usage: global_ip_assignments_usage.AsyncGlobalIPAssignmentsUsageResource
    global_ip_health_check_types: global_ip_health_check_types.AsyncGlobalIPHealthCheckTypesResource
    global_ip_health_checks: global_ip_health_checks.AsyncGlobalIPHealthChecksResource
    global_ip_latency: global_ip_latency.AsyncGlobalIPLatencyResource
    global_ip_protocols: global_ip_protocols.AsyncGlobalIPProtocolsResource
    global_ip_usage: global_ip_usage.AsyncGlobalIPUsageResource
    global_ips: global_ips.AsyncGlobalIPsResource
    inbound_channels: inbound_channels.AsyncInboundChannelsResource
    integration_secrets: integration_secrets.AsyncIntegrationSecretsResource
    inventory_coverage: inventory_coverage.AsyncInventoryCoverageResource
    invoices: invoices.AsyncInvoicesResource
    ip_connections: ip_connections.AsyncIPConnectionsResource
    ips: ips.AsyncIPsResource
    ledger_billing_group_reports: ledger_billing_group_reports.AsyncLedgerBillingGroupReportsResource
    list: list.AsyncListResource
    managed_accounts: managed_accounts.AsyncManagedAccountsResource
    media: media.AsyncMediaResource
    messages: messages.AsyncMessagesResource
    messaging: messaging.AsyncMessagingResource
    messaging_hosted_number_orders: messaging_hosted_number_orders.AsyncMessagingHostedNumberOrdersResource
    messaging_hosted_numbers: messaging_hosted_numbers.AsyncMessagingHostedNumbersResource
    messaging_numbers_bulk_updates: messaging_numbers_bulk_updates.AsyncMessagingNumbersBulkUpdatesResource
    messaging_optouts: messaging_optouts.AsyncMessagingOptoutsResource
    messaging_profiles: messaging_profiles.AsyncMessagingProfilesResource
    messaging_tollfree: messaging_tollfree.AsyncMessagingTollfreeResource
    messaging_url_domains: messaging_url_domains.AsyncMessagingURLDomainsResource
    messsages: messsages.AsyncMesssagesResource
    mobile_network_operators: mobile_network_operators.AsyncMobileNetworkOperatorsResource
    mobile_push_credentials: mobile_push_credentials.AsyncMobilePushCredentialsResource
    network_coverage: network_coverage.AsyncNetworkCoverageResource
    networks: networks.AsyncNetworksResource
    notification_channels: notification_channels.AsyncNotificationChannelsResource
    notification_event_conditions: notification_event_conditions.AsyncNotificationEventConditionsResource
    notification_events: notification_events.AsyncNotificationEventsResource
    notification_profiles: notification_profiles.AsyncNotificationProfilesResource
    notification_settings: notification_settings.AsyncNotificationSettingsResource
    number_block_orders: number_block_orders.AsyncNumberBlockOrdersResource
    number_lookup: number_lookup.AsyncNumberLookupResource
    number_order_phone_numbers: number_order_phone_numbers.AsyncNumberOrderPhoneNumbersResource
    number_orders: number_orders.AsyncNumberOrdersResource
    number_reservations: number_reservations.AsyncNumberReservationsResource
    numbers_features: numbers_features.AsyncNumbersFeaturesResource
    operator_connect: operator_connect.AsyncOperatorConnectResource
    ota_updates: ota_updates.AsyncOtaUpdatesResource
    outbound_voice_profiles: outbound_voice_profiles.AsyncOutboundVoiceProfilesResource
    payment: payment.AsyncPaymentResource
    phone_number_assignment_by_profile: phone_number_assignment_by_profile.AsyncPhoneNumberAssignmentByProfileResource
    phone_number_blocks: phone_number_blocks.AsyncPhoneNumberBlocksResource
    phone_number_campaigns: phone_number_campaigns.AsyncPhoneNumberCampaignsResource
    phone_numbers: phone_numbers.AsyncPhoneNumbersResource
    phone_numbers_regulatory_requirements: (
        phone_numbers_regulatory_requirements.AsyncPhoneNumbersRegulatoryRequirementsResource
    )
    portability_checks: portability_checks.AsyncPortabilityChecksResource
    porting: porting.AsyncPortingResource
    porting_orders: porting_orders.AsyncPortingOrdersResource
    porting_phone_numbers: porting_phone_numbers.AsyncPortingPhoneNumbersResource
    portouts: portouts.AsyncPortoutsResource
    private_wireless_gateways: private_wireless_gateways.AsyncPrivateWirelessGatewaysResource
    public_internet_gateways: public_internet_gateways.AsyncPublicInternetGatewaysResource
    queues: queues.AsyncQueuesResource
    recording_transcriptions: recording_transcriptions.AsyncRecordingTranscriptionsResource
    recordings: recordings.AsyncRecordingsResource
    regions: regions.AsyncRegionsResource
    regulatory_requirements: regulatory_requirements.AsyncRegulatoryRequirementsResource
    reports: reports.AsyncReportsResource
    requirement_groups: requirement_groups.AsyncRequirementGroupsResource
    requirement_types: requirement_types.AsyncRequirementTypesResource
    requirements: requirements.AsyncRequirementsResource
    room_compositions: room_compositions.AsyncRoomCompositionsResource
    room_participants: room_participants.AsyncRoomParticipantsResource
    room_recordings: room_recordings.AsyncRoomRecordingsResource
    rooms: rooms.AsyncRoomsResource
    seti: seti.AsyncSetiResource
    short_codes: short_codes.AsyncShortCodesResource
    sim_card_data_usage_notifications: sim_card_data_usage_notifications.AsyncSimCardDataUsageNotificationsResource
    sim_card_groups: sim_card_groups.AsyncSimCardGroupsResource
    sim_card_order_preview: sim_card_order_preview.AsyncSimCardOrderPreviewResource
    sim_card_orders: sim_card_orders.AsyncSimCardOrdersResource
    sim_cards: sim_cards.AsyncSimCardsResource
    siprec_connectors: siprec_connectors.AsyncSiprecConnectorsResource
    storage: storage.AsyncStorageResource
    sub_number_orders: sub_number_orders.AsyncSubNumberOrdersResource
    sub_number_orders_report: sub_number_orders_report.AsyncSubNumberOrdersReportResource
    telephony_credentials: telephony_credentials.AsyncTelephonyCredentialsResource
    texml: texml.AsyncTexmlResource
    texml_applications: texml_applications.AsyncTexmlApplicationsResource
    text_to_speech: text_to_speech.AsyncTextToSpeechResource
    usage_reports: usage_reports.AsyncUsageReportsResource
    user_addresses: user_addresses.AsyncUserAddressesResource
    user_tags: user_tags.AsyncUserTagsResource
    verifications: verifications.AsyncVerificationsResource
    verified_numbers: verified_numbers.AsyncVerifiedNumbersResource
    verify_profiles: verify_profiles.AsyncVerifyProfilesResource
    virtual_cross_connects: virtual_cross_connects.AsyncVirtualCrossConnectsResource
    virtual_cross_connects_coverage: virtual_cross_connects_coverage.AsyncVirtualCrossConnectsCoverageResource
    webhook_deliveries: webhook_deliveries.AsyncWebhookDeliveriesResource
    wireguard_interfaces: wireguard_interfaces.AsyncWireguardInterfacesResource
    wireguard_peers: wireguard_peers.AsyncWireguardPeersResource
    wireless: wireless.AsyncWirelessResource
    wireless_blocklist_values: wireless_blocklist_values.AsyncWirelessBlocklistValuesResource
    wireless_blocklists: wireless_blocklists.AsyncWirelessBlocklistsResource
    partner_campaigns: partner_campaigns.AsyncPartnerCampaignsResource
    with_raw_response: AsyncTelnyxWithRawResponse
    with_streaming_response: AsyncTelnyxWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncTelnyx client instance.

        This automatically infers the `api_key` argument from the `TELNYX_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("TELNYX_API_KEY")
        if api_key is None:
            raise TelnyxError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TELNYX_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("TELNYX_BASE_URL")
        if base_url is None:
            base_url = f"https://api.telnyx.com/v2"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.webhooks = webhooks.AsyncWebhooksResource(self)
        self.access_ip_address = access_ip_address.AsyncAccessIPAddressResource(self)
        self.access_ip_ranges = access_ip_ranges.AsyncAccessIPRangesResource(self)
        self.actions = actions.AsyncActionsResource(self)
        self.addresses = addresses.AsyncAddressesResource(self)
        self.advanced_orders = advanced_orders.AsyncAdvancedOrdersResource(self)
        self.ai = ai.AsyncAIResource(self)
        self.audit_events = audit_events.AsyncAuditEventsResource(self)
        self.authentication_providers = authentication_providers.AsyncAuthenticationProvidersResource(self)
        self.available_phone_number_blocks = available_phone_number_blocks.AsyncAvailablePhoneNumberBlocksResource(self)
        self.available_phone_numbers = available_phone_numbers.AsyncAvailablePhoneNumbersResource(self)
        self.balance = balance.AsyncBalanceResource(self)
        self.billing_groups = billing_groups.AsyncBillingGroupsResource(self)
        self.brand = brand.AsyncBrandResource(self)
        self.bulk_sim_card_actions = bulk_sim_card_actions.AsyncBulkSimCardActionsResource(self)
        self.bundle_pricing = bundle_pricing.AsyncBundlePricingResource(self)
        self.call_control_applications = call_control_applications.AsyncCallControlApplicationsResource(self)
        self.call_events = call_events.AsyncCallEventsResource(self)
        self.calls = calls.AsyncCallsResource(self)
        self.campaign = campaign.AsyncCampaignResource(self)
        self.campaign_builder = campaign_builder.AsyncCampaignBuilderResource(self)
        self.channel_zones = channel_zones.AsyncChannelZonesResource(self)
        self.charges_breakdown = charges_breakdown.AsyncChargesBreakdownResource(self)
        self.charges_summary = charges_summary.AsyncChargesSummaryResource(self)
        self.comments = comments.AsyncCommentsResource(self)
        self.conferences = conferences.AsyncConferencesResource(self)
        self.connections = connections.AsyncConnectionsResource(self)
        self.country_coverage = country_coverage.AsyncCountryCoverageResource(self)
        self.credential_connections = credential_connections.AsyncCredentialConnectionsResource(self)
        self.custom_storage_credentials = custom_storage_credentials.AsyncCustomStorageCredentialsResource(self)
        self.customer_service_records = customer_service_records.AsyncCustomerServiceRecordsResource(self)
        self.detail_records = detail_records.AsyncDetailRecordsResource(self)
        self.dialogflow_connections = dialogflow_connections.AsyncDialogflowConnectionsResource(self)
        self.document_links = document_links.AsyncDocumentLinksResource(self)
        self.documents = documents.AsyncDocumentsResource(self)
        self.dynamic_emergency_addresses = dynamic_emergency_addresses.AsyncDynamicEmergencyAddressesResource(self)
        self.dynamic_emergency_endpoints = dynamic_emergency_endpoints.AsyncDynamicEmergencyEndpointsResource(self)
        self.enum = enum.AsyncEnumResource(self)
        self.external_connections = external_connections.AsyncExternalConnectionsResource(self)
        self.fax_applications = fax_applications.AsyncFaxApplicationsResource(self)
        self.faxes = faxes.AsyncFaxesResource(self)
        self.fqdn_connections = fqdn_connections.AsyncFqdnConnectionsResource(self)
        self.fqdns = fqdns.AsyncFqdnsResource(self)
        self.global_ip_allowed_ports = global_ip_allowed_ports.AsyncGlobalIPAllowedPortsResource(self)
        self.global_ip_assignment_health = global_ip_assignment_health.AsyncGlobalIPAssignmentHealthResource(self)
        self.global_ip_assignments = global_ip_assignments.AsyncGlobalIPAssignmentsResource(self)
        self.global_ip_assignments_usage = global_ip_assignments_usage.AsyncGlobalIPAssignmentsUsageResource(self)
        self.global_ip_health_check_types = global_ip_health_check_types.AsyncGlobalIPHealthCheckTypesResource(self)
        self.global_ip_health_checks = global_ip_health_checks.AsyncGlobalIPHealthChecksResource(self)
        self.global_ip_latency = global_ip_latency.AsyncGlobalIPLatencyResource(self)
        self.global_ip_protocols = global_ip_protocols.AsyncGlobalIPProtocolsResource(self)
        self.global_ip_usage = global_ip_usage.AsyncGlobalIPUsageResource(self)
        self.global_ips = global_ips.AsyncGlobalIPsResource(self)
        self.inbound_channels = inbound_channels.AsyncInboundChannelsResource(self)
        self.integration_secrets = integration_secrets.AsyncIntegrationSecretsResource(self)
        self.inventory_coverage = inventory_coverage.AsyncInventoryCoverageResource(self)
        self.invoices = invoices.AsyncInvoicesResource(self)
        self.ip_connections = ip_connections.AsyncIPConnectionsResource(self)
        self.ips = ips.AsyncIPsResource(self)
        self.ledger_billing_group_reports = ledger_billing_group_reports.AsyncLedgerBillingGroupReportsResource(self)
        self.list = list.AsyncListResource(self)
        self.managed_accounts = managed_accounts.AsyncManagedAccountsResource(self)
        self.media = media.AsyncMediaResource(self)
        self.messages = messages.AsyncMessagesResource(self)
        self.messaging = messaging.AsyncMessagingResource(self)
        self.messaging_hosted_number_orders = messaging_hosted_number_orders.AsyncMessagingHostedNumberOrdersResource(
            self
        )
        self.messaging_hosted_numbers = messaging_hosted_numbers.AsyncMessagingHostedNumbersResource(self)
        self.messaging_numbers_bulk_updates = messaging_numbers_bulk_updates.AsyncMessagingNumbersBulkUpdatesResource(
            self
        )
        self.messaging_optouts = messaging_optouts.AsyncMessagingOptoutsResource(self)
        self.messaging_profiles = messaging_profiles.AsyncMessagingProfilesResource(self)
        self.messaging_tollfree = messaging_tollfree.AsyncMessagingTollfreeResource(self)
        self.messaging_url_domains = messaging_url_domains.AsyncMessagingURLDomainsResource(self)
        self.messsages = messsages.AsyncMesssagesResource(self)
        self.mobile_network_operators = mobile_network_operators.AsyncMobileNetworkOperatorsResource(self)
        self.mobile_push_credentials = mobile_push_credentials.AsyncMobilePushCredentialsResource(self)
        self.network_coverage = network_coverage.AsyncNetworkCoverageResource(self)
        self.networks = networks.AsyncNetworksResource(self)
        self.notification_channels = notification_channels.AsyncNotificationChannelsResource(self)
        self.notification_event_conditions = notification_event_conditions.AsyncNotificationEventConditionsResource(
            self
        )
        self.notification_events = notification_events.AsyncNotificationEventsResource(self)
        self.notification_profiles = notification_profiles.AsyncNotificationProfilesResource(self)
        self.notification_settings = notification_settings.AsyncNotificationSettingsResource(self)
        self.number_block_orders = number_block_orders.AsyncNumberBlockOrdersResource(self)
        self.number_lookup = number_lookup.AsyncNumberLookupResource(self)
        self.number_order_phone_numbers = number_order_phone_numbers.AsyncNumberOrderPhoneNumbersResource(self)
        self.number_orders = number_orders.AsyncNumberOrdersResource(self)
        self.number_reservations = number_reservations.AsyncNumberReservationsResource(self)
        self.numbers_features = numbers_features.AsyncNumbersFeaturesResource(self)
        self.operator_connect = operator_connect.AsyncOperatorConnectResource(self)
        self.ota_updates = ota_updates.AsyncOtaUpdatesResource(self)
        self.outbound_voice_profiles = outbound_voice_profiles.AsyncOutboundVoiceProfilesResource(self)
        self.payment = payment.AsyncPaymentResource(self)
        self.phone_number_assignment_by_profile = (
            phone_number_assignment_by_profile.AsyncPhoneNumberAssignmentByProfileResource(self)
        )
        self.phone_number_blocks = phone_number_blocks.AsyncPhoneNumberBlocksResource(self)
        self.phone_number_campaigns = phone_number_campaigns.AsyncPhoneNumberCampaignsResource(self)
        self.phone_numbers = phone_numbers.AsyncPhoneNumbersResource(self)
        self.phone_numbers_regulatory_requirements = (
            phone_numbers_regulatory_requirements.AsyncPhoneNumbersRegulatoryRequirementsResource(self)
        )
        self.portability_checks = portability_checks.AsyncPortabilityChecksResource(self)
        self.porting = porting.AsyncPortingResource(self)
        self.porting_orders = porting_orders.AsyncPortingOrdersResource(self)
        self.porting_phone_numbers = porting_phone_numbers.AsyncPortingPhoneNumbersResource(self)
        self.portouts = portouts.AsyncPortoutsResource(self)
        self.private_wireless_gateways = private_wireless_gateways.AsyncPrivateWirelessGatewaysResource(self)
        self.public_internet_gateways = public_internet_gateways.AsyncPublicInternetGatewaysResource(self)
        self.queues = queues.AsyncQueuesResource(self)
        self.recording_transcriptions = recording_transcriptions.AsyncRecordingTranscriptionsResource(self)
        self.recordings = recordings.AsyncRecordingsResource(self)
        self.regions = regions.AsyncRegionsResource(self)
        self.regulatory_requirements = regulatory_requirements.AsyncRegulatoryRequirementsResource(self)
        self.reports = reports.AsyncReportsResource(self)
        self.requirement_groups = requirement_groups.AsyncRequirementGroupsResource(self)
        self.requirement_types = requirement_types.AsyncRequirementTypesResource(self)
        self.requirements = requirements.AsyncRequirementsResource(self)
        self.room_compositions = room_compositions.AsyncRoomCompositionsResource(self)
        self.room_participants = room_participants.AsyncRoomParticipantsResource(self)
        self.room_recordings = room_recordings.AsyncRoomRecordingsResource(self)
        self.rooms = rooms.AsyncRoomsResource(self)
        self.seti = seti.AsyncSetiResource(self)
        self.short_codes = short_codes.AsyncShortCodesResource(self)
        self.sim_card_data_usage_notifications = (
            sim_card_data_usage_notifications.AsyncSimCardDataUsageNotificationsResource(self)
        )
        self.sim_card_groups = sim_card_groups.AsyncSimCardGroupsResource(self)
        self.sim_card_order_preview = sim_card_order_preview.AsyncSimCardOrderPreviewResource(self)
        self.sim_card_orders = sim_card_orders.AsyncSimCardOrdersResource(self)
        self.sim_cards = sim_cards.AsyncSimCardsResource(self)
        self.siprec_connectors = siprec_connectors.AsyncSiprecConnectorsResource(self)
        self.storage = storage.AsyncStorageResource(self)
        self.sub_number_orders = sub_number_orders.AsyncSubNumberOrdersResource(self)
        self.sub_number_orders_report = sub_number_orders_report.AsyncSubNumberOrdersReportResource(self)
        self.telephony_credentials = telephony_credentials.AsyncTelephonyCredentialsResource(self)
        self.texml = texml.AsyncTexmlResource(self)
        self.texml_applications = texml_applications.AsyncTexmlApplicationsResource(self)
        self.text_to_speech = text_to_speech.AsyncTextToSpeechResource(self)
        self.usage_reports = usage_reports.AsyncUsageReportsResource(self)
        self.user_addresses = user_addresses.AsyncUserAddressesResource(self)
        self.user_tags = user_tags.AsyncUserTagsResource(self)
        self.verifications = verifications.AsyncVerificationsResource(self)
        self.verified_numbers = verified_numbers.AsyncVerifiedNumbersResource(self)
        self.verify_profiles = verify_profiles.AsyncVerifyProfilesResource(self)
        self.virtual_cross_connects = virtual_cross_connects.AsyncVirtualCrossConnectsResource(self)
        self.virtual_cross_connects_coverage = (
            virtual_cross_connects_coverage.AsyncVirtualCrossConnectsCoverageResource(self)
        )
        self.webhook_deliveries = webhook_deliveries.AsyncWebhookDeliveriesResource(self)
        self.wireguard_interfaces = wireguard_interfaces.AsyncWireguardInterfacesResource(self)
        self.wireguard_peers = wireguard_peers.AsyncWireguardPeersResource(self)
        self.wireless = wireless.AsyncWirelessResource(self)
        self.wireless_blocklist_values = wireless_blocklist_values.AsyncWirelessBlocklistValuesResource(self)
        self.wireless_blocklists = wireless_blocklists.AsyncWirelessBlocklistsResource(self)
        self.partner_campaigns = partner_campaigns.AsyncPartnerCampaignsResource(self)
        self.with_raw_response = AsyncTelnyxWithRawResponse(self)
        self.with_streaming_response = AsyncTelnyxWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def create_bucket(
        self,
        bucket_name: str,
        *,
        location_constraint: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create a bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self.put(
            f"/{bucket_name}",
            body=await async_maybe_transform(
                {"location_constraint": location_constraint}, client_create_bucket_params.ClientCreateBucketParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_bucket(
        self,
        bucket_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a bucket.

        The bucket must be empty for it to be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self.delete(
            f"/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_object(
        self,
        object_name: str,
        *,
        bucket_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an object from a given bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self.delete(
            f"/{bucket_name}/{object_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_objects(
        self,
        bucket_name: str,
        *,
        delete: Literal[True],
        body: Iterable[client_delete_objects_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes one or multiple objects from a given bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "application/xml", **(extra_headers or {})}
        return await self.post(
            f"/{bucket_name}",
            body=await async_maybe_transform(body, Iterable[client_delete_objects_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"delete": delete}, client_delete_objects_params.ClientDeleteObjectsParams
                ),
            ),
            cast_to=object,
        )

    async def get_object(
        self,
        object_name: str,
        *,
        bucket_name: str,
        upload_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Retrieves an object from a given bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self.get(
            f"/{bucket_name}/{object_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"upload_id": upload_id}, client_get_object_params.ClientGetObjectParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list_buckets(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListBucketsResponse:
        """List all Buckets."""
        extra_headers = {"Accept": "application/xml", **(extra_headers or {})}
        return await self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListBucketsResponse,
        )

    async def list_objects(
        self,
        bucket_name: str,
        *,
        list_type: Literal[2] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListObjectsResponse:
        """
        List all objects contained in a given bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {"Accept": "application/xml", **(extra_headers or {})}
        return await self.get(
            f"/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"list_type": list_type}, client_list_objects_params.ClientListObjectsParams
                ),
            ),
            cast_to=ListObjectsResponse,
        )

    async def put_object(
        self,
        object_name: str,
        *,
        bucket_name: str,
        body: FileTypes,
        part_number: str | NotGiven = NOT_GIVEN,
        upload_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Add an object to a bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self.put(
            f"/{bucket_name}/{object_name}",
            body=await async_maybe_transform(body, client_put_object_params.ClientPutObjectParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "part_number": part_number,
                        "upload_id": upload_id,
                    },
                    client_put_object_params.ClientPutObjectParams,
                ),
            ),
            cast_to=NoneType,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TelnyxWithRawResponse:
    def __init__(self, client: Telnyx) -> None:
        self.access_ip_address = access_ip_address.AccessIPAddressResourceWithRawResponse(client.access_ip_address)
        self.access_ip_ranges = access_ip_ranges.AccessIPRangesResourceWithRawResponse(client.access_ip_ranges)
        self.actions = actions.ActionsResourceWithRawResponse(client.actions)
        self.addresses = addresses.AddressesResourceWithRawResponse(client.addresses)
        self.advanced_orders = advanced_orders.AdvancedOrdersResourceWithRawResponse(client.advanced_orders)
        self.ai = ai.AIResourceWithRawResponse(client.ai)
        self.audit_events = audit_events.AuditEventsResourceWithRawResponse(client.audit_events)
        self.authentication_providers = authentication_providers.AuthenticationProvidersResourceWithRawResponse(
            client.authentication_providers
        )
        self.available_phone_number_blocks = (
            available_phone_number_blocks.AvailablePhoneNumberBlocksResourceWithRawResponse(
                client.available_phone_number_blocks
            )
        )
        self.available_phone_numbers = available_phone_numbers.AvailablePhoneNumbersResourceWithRawResponse(
            client.available_phone_numbers
        )
        self.balance = balance.BalanceResourceWithRawResponse(client.balance)
        self.billing_groups = billing_groups.BillingGroupsResourceWithRawResponse(client.billing_groups)
        self.brand = brand.BrandResourceWithRawResponse(client.brand)
        self.bulk_sim_card_actions = bulk_sim_card_actions.BulkSimCardActionsResourceWithRawResponse(
            client.bulk_sim_card_actions
        )
        self.bundle_pricing = bundle_pricing.BundlePricingResourceWithRawResponse(client.bundle_pricing)
        self.call_control_applications = call_control_applications.CallControlApplicationsResourceWithRawResponse(
            client.call_control_applications
        )
        self.call_events = call_events.CallEventsResourceWithRawResponse(client.call_events)
        self.calls = calls.CallsResourceWithRawResponse(client.calls)
        self.campaign = campaign.CampaignResourceWithRawResponse(client.campaign)
        self.campaign_builder = campaign_builder.CampaignBuilderResourceWithRawResponse(client.campaign_builder)
        self.channel_zones = channel_zones.ChannelZonesResourceWithRawResponse(client.channel_zones)
        self.charges_breakdown = charges_breakdown.ChargesBreakdownResourceWithRawResponse(client.charges_breakdown)
        self.charges_summary = charges_summary.ChargesSummaryResourceWithRawResponse(client.charges_summary)
        self.comments = comments.CommentsResourceWithRawResponse(client.comments)
        self.conferences = conferences.ConferencesResourceWithRawResponse(client.conferences)
        self.connections = connections.ConnectionsResourceWithRawResponse(client.connections)
        self.country_coverage = country_coverage.CountryCoverageResourceWithRawResponse(client.country_coverage)
        self.credential_connections = credential_connections.CredentialConnectionsResourceWithRawResponse(
            client.credential_connections
        )
        self.custom_storage_credentials = custom_storage_credentials.CustomStorageCredentialsResourceWithRawResponse(
            client.custom_storage_credentials
        )
        self.customer_service_records = customer_service_records.CustomerServiceRecordsResourceWithRawResponse(
            client.customer_service_records
        )
        self.detail_records = detail_records.DetailRecordsResourceWithRawResponse(client.detail_records)
        self.dialogflow_connections = dialogflow_connections.DialogflowConnectionsResourceWithRawResponse(
            client.dialogflow_connections
        )
        self.document_links = document_links.DocumentLinksResourceWithRawResponse(client.document_links)
        self.documents = documents.DocumentsResourceWithRawResponse(client.documents)
        self.dynamic_emergency_addresses = dynamic_emergency_addresses.DynamicEmergencyAddressesResourceWithRawResponse(
            client.dynamic_emergency_addresses
        )
        self.dynamic_emergency_endpoints = dynamic_emergency_endpoints.DynamicEmergencyEndpointsResourceWithRawResponse(
            client.dynamic_emergency_endpoints
        )
        self.enum = enum.EnumResourceWithRawResponse(client.enum)
        self.external_connections = external_connections.ExternalConnectionsResourceWithRawResponse(
            client.external_connections
        )
        self.fax_applications = fax_applications.FaxApplicationsResourceWithRawResponse(client.fax_applications)
        self.faxes = faxes.FaxesResourceWithRawResponse(client.faxes)
        self.fqdn_connections = fqdn_connections.FqdnConnectionsResourceWithRawResponse(client.fqdn_connections)
        self.fqdns = fqdns.FqdnsResourceWithRawResponse(client.fqdns)
        self.global_ip_allowed_ports = global_ip_allowed_ports.GlobalIPAllowedPortsResourceWithRawResponse(
            client.global_ip_allowed_ports
        )
        self.global_ip_assignment_health = global_ip_assignment_health.GlobalIPAssignmentHealthResourceWithRawResponse(
            client.global_ip_assignment_health
        )
        self.global_ip_assignments = global_ip_assignments.GlobalIPAssignmentsResourceWithRawResponse(
            client.global_ip_assignments
        )
        self.global_ip_assignments_usage = global_ip_assignments_usage.GlobalIPAssignmentsUsageResourceWithRawResponse(
            client.global_ip_assignments_usage
        )
        self.global_ip_health_check_types = (
            global_ip_health_check_types.GlobalIPHealthCheckTypesResourceWithRawResponse(
                client.global_ip_health_check_types
            )
        )
        self.global_ip_health_checks = global_ip_health_checks.GlobalIPHealthChecksResourceWithRawResponse(
            client.global_ip_health_checks
        )
        self.global_ip_latency = global_ip_latency.GlobalIPLatencyResourceWithRawResponse(client.global_ip_latency)
        self.global_ip_protocols = global_ip_protocols.GlobalIPProtocolsResourceWithRawResponse(
            client.global_ip_protocols
        )
        self.global_ip_usage = global_ip_usage.GlobalIPUsageResourceWithRawResponse(client.global_ip_usage)
        self.global_ips = global_ips.GlobalIPsResourceWithRawResponse(client.global_ips)
        self.inbound_channels = inbound_channels.InboundChannelsResourceWithRawResponse(client.inbound_channels)
        self.integration_secrets = integration_secrets.IntegrationSecretsResourceWithRawResponse(
            client.integration_secrets
        )
        self.inventory_coverage = inventory_coverage.InventoryCoverageResourceWithRawResponse(client.inventory_coverage)
        self.invoices = invoices.InvoicesResourceWithRawResponse(client.invoices)
        self.ip_connections = ip_connections.IPConnectionsResourceWithRawResponse(client.ip_connections)
        self.ips = ips.IPsResourceWithRawResponse(client.ips)
        self.ledger_billing_group_reports = (
            ledger_billing_group_reports.LedgerBillingGroupReportsResourceWithRawResponse(
                client.ledger_billing_group_reports
            )
        )
        self.list = list.ListResourceWithRawResponse(client.list)
        self.managed_accounts = managed_accounts.ManagedAccountsResourceWithRawResponse(client.managed_accounts)
        self.media = media.MediaResourceWithRawResponse(client.media)
        self.messages = messages.MessagesResourceWithRawResponse(client.messages)
        self.messaging = messaging.MessagingResourceWithRawResponse(client.messaging)
        self.messaging_hosted_number_orders = (
            messaging_hosted_number_orders.MessagingHostedNumberOrdersResourceWithRawResponse(
                client.messaging_hosted_number_orders
            )
        )
        self.messaging_hosted_numbers = messaging_hosted_numbers.MessagingHostedNumbersResourceWithRawResponse(
            client.messaging_hosted_numbers
        )
        self.messaging_numbers_bulk_updates = (
            messaging_numbers_bulk_updates.MessagingNumbersBulkUpdatesResourceWithRawResponse(
                client.messaging_numbers_bulk_updates
            )
        )
        self.messaging_optouts = messaging_optouts.MessagingOptoutsResourceWithRawResponse(client.messaging_optouts)
        self.messaging_profiles = messaging_profiles.MessagingProfilesResourceWithRawResponse(client.messaging_profiles)
        self.messaging_tollfree = messaging_tollfree.MessagingTollfreeResourceWithRawResponse(client.messaging_tollfree)
        self.messaging_url_domains = messaging_url_domains.MessagingURLDomainsResourceWithRawResponse(
            client.messaging_url_domains
        )
        self.messsages = messsages.MesssagesResourceWithRawResponse(client.messsages)
        self.mobile_network_operators = mobile_network_operators.MobileNetworkOperatorsResourceWithRawResponse(
            client.mobile_network_operators
        )
        self.mobile_push_credentials = mobile_push_credentials.MobilePushCredentialsResourceWithRawResponse(
            client.mobile_push_credentials
        )
        self.network_coverage = network_coverage.NetworkCoverageResourceWithRawResponse(client.network_coverage)
        self.networks = networks.NetworksResourceWithRawResponse(client.networks)
        self.notification_channels = notification_channels.NotificationChannelsResourceWithRawResponse(
            client.notification_channels
        )
        self.notification_event_conditions = (
            notification_event_conditions.NotificationEventConditionsResourceWithRawResponse(
                client.notification_event_conditions
            )
        )
        self.notification_events = notification_events.NotificationEventsResourceWithRawResponse(
            client.notification_events
        )
        self.notification_profiles = notification_profiles.NotificationProfilesResourceWithRawResponse(
            client.notification_profiles
        )
        self.notification_settings = notification_settings.NotificationSettingsResourceWithRawResponse(
            client.notification_settings
        )
        self.number_block_orders = number_block_orders.NumberBlockOrdersResourceWithRawResponse(
            client.number_block_orders
        )
        self.number_lookup = number_lookup.NumberLookupResourceWithRawResponse(client.number_lookup)
        self.number_order_phone_numbers = number_order_phone_numbers.NumberOrderPhoneNumbersResourceWithRawResponse(
            client.number_order_phone_numbers
        )
        self.number_orders = number_orders.NumberOrdersResourceWithRawResponse(client.number_orders)
        self.number_reservations = number_reservations.NumberReservationsResourceWithRawResponse(
            client.number_reservations
        )
        self.numbers_features = numbers_features.NumbersFeaturesResourceWithRawResponse(client.numbers_features)
        self.operator_connect = operator_connect.OperatorConnectResourceWithRawResponse(client.operator_connect)
        self.ota_updates = ota_updates.OtaUpdatesResourceWithRawResponse(client.ota_updates)
        self.outbound_voice_profiles = outbound_voice_profiles.OutboundVoiceProfilesResourceWithRawResponse(
            client.outbound_voice_profiles
        )
        self.payment = payment.PaymentResourceWithRawResponse(client.payment)
        self.phone_number_assignment_by_profile = (
            phone_number_assignment_by_profile.PhoneNumberAssignmentByProfileResourceWithRawResponse(
                client.phone_number_assignment_by_profile
            )
        )
        self.phone_number_blocks = phone_number_blocks.PhoneNumberBlocksResourceWithRawResponse(
            client.phone_number_blocks
        )
        self.phone_number_campaigns = phone_number_campaigns.PhoneNumberCampaignsResourceWithRawResponse(
            client.phone_number_campaigns
        )
        self.phone_numbers = phone_numbers.PhoneNumbersResourceWithRawResponse(client.phone_numbers)
        self.phone_numbers_regulatory_requirements = (
            phone_numbers_regulatory_requirements.PhoneNumbersRegulatoryRequirementsResourceWithRawResponse(
                client.phone_numbers_regulatory_requirements
            )
        )
        self.portability_checks = portability_checks.PortabilityChecksResourceWithRawResponse(client.portability_checks)
        self.porting = porting.PortingResourceWithRawResponse(client.porting)
        self.porting_orders = porting_orders.PortingOrdersResourceWithRawResponse(client.porting_orders)
        self.porting_phone_numbers = porting_phone_numbers.PortingPhoneNumbersResourceWithRawResponse(
            client.porting_phone_numbers
        )
        self.portouts = portouts.PortoutsResourceWithRawResponse(client.portouts)
        self.private_wireless_gateways = private_wireless_gateways.PrivateWirelessGatewaysResourceWithRawResponse(
            client.private_wireless_gateways
        )
        self.public_internet_gateways = public_internet_gateways.PublicInternetGatewaysResourceWithRawResponse(
            client.public_internet_gateways
        )
        self.queues = queues.QueuesResourceWithRawResponse(client.queues)
        self.recording_transcriptions = recording_transcriptions.RecordingTranscriptionsResourceWithRawResponse(
            client.recording_transcriptions
        )
        self.recordings = recordings.RecordingsResourceWithRawResponse(client.recordings)
        self.regions = regions.RegionsResourceWithRawResponse(client.regions)
        self.regulatory_requirements = regulatory_requirements.RegulatoryRequirementsResourceWithRawResponse(
            client.regulatory_requirements
        )
        self.reports = reports.ReportsResourceWithRawResponse(client.reports)
        self.requirement_groups = requirement_groups.RequirementGroupsResourceWithRawResponse(client.requirement_groups)
        self.requirement_types = requirement_types.RequirementTypesResourceWithRawResponse(client.requirement_types)
        self.requirements = requirements.RequirementsResourceWithRawResponse(client.requirements)
        self.room_compositions = room_compositions.RoomCompositionsResourceWithRawResponse(client.room_compositions)
        self.room_participants = room_participants.RoomParticipantsResourceWithRawResponse(client.room_participants)
        self.room_recordings = room_recordings.RoomRecordingsResourceWithRawResponse(client.room_recordings)
        self.rooms = rooms.RoomsResourceWithRawResponse(client.rooms)
        self.seti = seti.SetiResourceWithRawResponse(client.seti)
        self.short_codes = short_codes.ShortCodesResourceWithRawResponse(client.short_codes)
        self.sim_card_data_usage_notifications = (
            sim_card_data_usage_notifications.SimCardDataUsageNotificationsResourceWithRawResponse(
                client.sim_card_data_usage_notifications
            )
        )
        self.sim_card_groups = sim_card_groups.SimCardGroupsResourceWithRawResponse(client.sim_card_groups)
        self.sim_card_order_preview = sim_card_order_preview.SimCardOrderPreviewResourceWithRawResponse(
            client.sim_card_order_preview
        )
        self.sim_card_orders = sim_card_orders.SimCardOrdersResourceWithRawResponse(client.sim_card_orders)
        self.sim_cards = sim_cards.SimCardsResourceWithRawResponse(client.sim_cards)
        self.siprec_connectors = siprec_connectors.SiprecConnectorsResourceWithRawResponse(client.siprec_connectors)
        self.storage = storage.StorageResourceWithRawResponse(client.storage)
        self.sub_number_orders = sub_number_orders.SubNumberOrdersResourceWithRawResponse(client.sub_number_orders)
        self.sub_number_orders_report = sub_number_orders_report.SubNumberOrdersReportResourceWithRawResponse(
            client.sub_number_orders_report
        )
        self.telephony_credentials = telephony_credentials.TelephonyCredentialsResourceWithRawResponse(
            client.telephony_credentials
        )
        self.texml = texml.TexmlResourceWithRawResponse(client.texml)
        self.texml_applications = texml_applications.TexmlApplicationsResourceWithRawResponse(client.texml_applications)
        self.text_to_speech = text_to_speech.TextToSpeechResourceWithRawResponse(client.text_to_speech)
        self.usage_reports = usage_reports.UsageReportsResourceWithRawResponse(client.usage_reports)
        self.user_addresses = user_addresses.UserAddressesResourceWithRawResponse(client.user_addresses)
        self.user_tags = user_tags.UserTagsResourceWithRawResponse(client.user_tags)
        self.verifications = verifications.VerificationsResourceWithRawResponse(client.verifications)
        self.verified_numbers = verified_numbers.VerifiedNumbersResourceWithRawResponse(client.verified_numbers)
        self.verify_profiles = verify_profiles.VerifyProfilesResourceWithRawResponse(client.verify_profiles)
        self.virtual_cross_connects = virtual_cross_connects.VirtualCrossConnectsResourceWithRawResponse(
            client.virtual_cross_connects
        )
        self.virtual_cross_connects_coverage = (
            virtual_cross_connects_coverage.VirtualCrossConnectsCoverageResourceWithRawResponse(
                client.virtual_cross_connects_coverage
            )
        )
        self.webhook_deliveries = webhook_deliveries.WebhookDeliveriesResourceWithRawResponse(client.webhook_deliveries)
        self.wireguard_interfaces = wireguard_interfaces.WireguardInterfacesResourceWithRawResponse(
            client.wireguard_interfaces
        )
        self.wireguard_peers = wireguard_peers.WireguardPeersResourceWithRawResponse(client.wireguard_peers)
        self.wireless = wireless.WirelessResourceWithRawResponse(client.wireless)
        self.wireless_blocklist_values = wireless_blocklist_values.WirelessBlocklistValuesResourceWithRawResponse(
            client.wireless_blocklist_values
        )
        self.wireless_blocklists = wireless_blocklists.WirelessBlocklistsResourceWithRawResponse(
            client.wireless_blocklists
        )
        self.partner_campaigns = partner_campaigns.PartnerCampaignsResourceWithRawResponse(client.partner_campaigns)

        self.create_bucket = to_raw_response_wrapper(
            client.create_bucket,
        )
        self.delete_bucket = to_raw_response_wrapper(
            client.delete_bucket,
        )
        self.delete_object = to_raw_response_wrapper(
            client.delete_object,
        )
        self.delete_objects = to_raw_response_wrapper(
            client.delete_objects,
        )
        self.get_object = to_custom_raw_response_wrapper(
            client.get_object,
            BinaryAPIResponse,
        )
        self.list_buckets = to_raw_response_wrapper(
            client.list_buckets,
        )
        self.list_objects = to_raw_response_wrapper(
            client.list_objects,
        )
        self.put_object = to_raw_response_wrapper(
            client.put_object,
        )


class AsyncTelnyxWithRawResponse:
    def __init__(self, client: AsyncTelnyx) -> None:
        self.access_ip_address = access_ip_address.AsyncAccessIPAddressResourceWithRawResponse(client.access_ip_address)
        self.access_ip_ranges = access_ip_ranges.AsyncAccessIPRangesResourceWithRawResponse(client.access_ip_ranges)
        self.actions = actions.AsyncActionsResourceWithRawResponse(client.actions)
        self.addresses = addresses.AsyncAddressesResourceWithRawResponse(client.addresses)
        self.advanced_orders = advanced_orders.AsyncAdvancedOrdersResourceWithRawResponse(client.advanced_orders)
        self.ai = ai.AsyncAIResourceWithRawResponse(client.ai)
        self.audit_events = audit_events.AsyncAuditEventsResourceWithRawResponse(client.audit_events)
        self.authentication_providers = authentication_providers.AsyncAuthenticationProvidersResourceWithRawResponse(
            client.authentication_providers
        )
        self.available_phone_number_blocks = (
            available_phone_number_blocks.AsyncAvailablePhoneNumberBlocksResourceWithRawResponse(
                client.available_phone_number_blocks
            )
        )
        self.available_phone_numbers = available_phone_numbers.AsyncAvailablePhoneNumbersResourceWithRawResponse(
            client.available_phone_numbers
        )
        self.balance = balance.AsyncBalanceResourceWithRawResponse(client.balance)
        self.billing_groups = billing_groups.AsyncBillingGroupsResourceWithRawResponse(client.billing_groups)
        self.brand = brand.AsyncBrandResourceWithRawResponse(client.brand)
        self.bulk_sim_card_actions = bulk_sim_card_actions.AsyncBulkSimCardActionsResourceWithRawResponse(
            client.bulk_sim_card_actions
        )
        self.bundle_pricing = bundle_pricing.AsyncBundlePricingResourceWithRawResponse(client.bundle_pricing)
        self.call_control_applications = call_control_applications.AsyncCallControlApplicationsResourceWithRawResponse(
            client.call_control_applications
        )
        self.call_events = call_events.AsyncCallEventsResourceWithRawResponse(client.call_events)
        self.calls = calls.AsyncCallsResourceWithRawResponse(client.calls)
        self.campaign = campaign.AsyncCampaignResourceWithRawResponse(client.campaign)
        self.campaign_builder = campaign_builder.AsyncCampaignBuilderResourceWithRawResponse(client.campaign_builder)
        self.channel_zones = channel_zones.AsyncChannelZonesResourceWithRawResponse(client.channel_zones)
        self.charges_breakdown = charges_breakdown.AsyncChargesBreakdownResourceWithRawResponse(
            client.charges_breakdown
        )
        self.charges_summary = charges_summary.AsyncChargesSummaryResourceWithRawResponse(client.charges_summary)
        self.comments = comments.AsyncCommentsResourceWithRawResponse(client.comments)
        self.conferences = conferences.AsyncConferencesResourceWithRawResponse(client.conferences)
        self.connections = connections.AsyncConnectionsResourceWithRawResponse(client.connections)
        self.country_coverage = country_coverage.AsyncCountryCoverageResourceWithRawResponse(client.country_coverage)
        self.credential_connections = credential_connections.AsyncCredentialConnectionsResourceWithRawResponse(
            client.credential_connections
        )
        self.custom_storage_credentials = (
            custom_storage_credentials.AsyncCustomStorageCredentialsResourceWithRawResponse(
                client.custom_storage_credentials
            )
        )
        self.customer_service_records = customer_service_records.AsyncCustomerServiceRecordsResourceWithRawResponse(
            client.customer_service_records
        )
        self.detail_records = detail_records.AsyncDetailRecordsResourceWithRawResponse(client.detail_records)
        self.dialogflow_connections = dialogflow_connections.AsyncDialogflowConnectionsResourceWithRawResponse(
            client.dialogflow_connections
        )
        self.document_links = document_links.AsyncDocumentLinksResourceWithRawResponse(client.document_links)
        self.documents = documents.AsyncDocumentsResourceWithRawResponse(client.documents)
        self.dynamic_emergency_addresses = (
            dynamic_emergency_addresses.AsyncDynamicEmergencyAddressesResourceWithRawResponse(
                client.dynamic_emergency_addresses
            )
        )
        self.dynamic_emergency_endpoints = (
            dynamic_emergency_endpoints.AsyncDynamicEmergencyEndpointsResourceWithRawResponse(
                client.dynamic_emergency_endpoints
            )
        )
        self.enum = enum.AsyncEnumResourceWithRawResponse(client.enum)
        self.external_connections = external_connections.AsyncExternalConnectionsResourceWithRawResponse(
            client.external_connections
        )
        self.fax_applications = fax_applications.AsyncFaxApplicationsResourceWithRawResponse(client.fax_applications)
        self.faxes = faxes.AsyncFaxesResourceWithRawResponse(client.faxes)
        self.fqdn_connections = fqdn_connections.AsyncFqdnConnectionsResourceWithRawResponse(client.fqdn_connections)
        self.fqdns = fqdns.AsyncFqdnsResourceWithRawResponse(client.fqdns)
        self.global_ip_allowed_ports = global_ip_allowed_ports.AsyncGlobalIPAllowedPortsResourceWithRawResponse(
            client.global_ip_allowed_ports
        )
        self.global_ip_assignment_health = (
            global_ip_assignment_health.AsyncGlobalIPAssignmentHealthResourceWithRawResponse(
                client.global_ip_assignment_health
            )
        )
        self.global_ip_assignments = global_ip_assignments.AsyncGlobalIPAssignmentsResourceWithRawResponse(
            client.global_ip_assignments
        )
        self.global_ip_assignments_usage = (
            global_ip_assignments_usage.AsyncGlobalIPAssignmentsUsageResourceWithRawResponse(
                client.global_ip_assignments_usage
            )
        )
        self.global_ip_health_check_types = (
            global_ip_health_check_types.AsyncGlobalIPHealthCheckTypesResourceWithRawResponse(
                client.global_ip_health_check_types
            )
        )
        self.global_ip_health_checks = global_ip_health_checks.AsyncGlobalIPHealthChecksResourceWithRawResponse(
            client.global_ip_health_checks
        )
        self.global_ip_latency = global_ip_latency.AsyncGlobalIPLatencyResourceWithRawResponse(client.global_ip_latency)
        self.global_ip_protocols = global_ip_protocols.AsyncGlobalIPProtocolsResourceWithRawResponse(
            client.global_ip_protocols
        )
        self.global_ip_usage = global_ip_usage.AsyncGlobalIPUsageResourceWithRawResponse(client.global_ip_usage)
        self.global_ips = global_ips.AsyncGlobalIPsResourceWithRawResponse(client.global_ips)
        self.inbound_channels = inbound_channels.AsyncInboundChannelsResourceWithRawResponse(client.inbound_channels)
        self.integration_secrets = integration_secrets.AsyncIntegrationSecretsResourceWithRawResponse(
            client.integration_secrets
        )
        self.inventory_coverage = inventory_coverage.AsyncInventoryCoverageResourceWithRawResponse(
            client.inventory_coverage
        )
        self.invoices = invoices.AsyncInvoicesResourceWithRawResponse(client.invoices)
        self.ip_connections = ip_connections.AsyncIPConnectionsResourceWithRawResponse(client.ip_connections)
        self.ips = ips.AsyncIPsResourceWithRawResponse(client.ips)
        self.ledger_billing_group_reports = (
            ledger_billing_group_reports.AsyncLedgerBillingGroupReportsResourceWithRawResponse(
                client.ledger_billing_group_reports
            )
        )
        self.list = list.AsyncListResourceWithRawResponse(client.list)
        self.managed_accounts = managed_accounts.AsyncManagedAccountsResourceWithRawResponse(client.managed_accounts)
        self.media = media.AsyncMediaResourceWithRawResponse(client.media)
        self.messages = messages.AsyncMessagesResourceWithRawResponse(client.messages)
        self.messaging = messaging.AsyncMessagingResourceWithRawResponse(client.messaging)
        self.messaging_hosted_number_orders = (
            messaging_hosted_number_orders.AsyncMessagingHostedNumberOrdersResourceWithRawResponse(
                client.messaging_hosted_number_orders
            )
        )
        self.messaging_hosted_numbers = messaging_hosted_numbers.AsyncMessagingHostedNumbersResourceWithRawResponse(
            client.messaging_hosted_numbers
        )
        self.messaging_numbers_bulk_updates = (
            messaging_numbers_bulk_updates.AsyncMessagingNumbersBulkUpdatesResourceWithRawResponse(
                client.messaging_numbers_bulk_updates
            )
        )
        self.messaging_optouts = messaging_optouts.AsyncMessagingOptoutsResourceWithRawResponse(
            client.messaging_optouts
        )
        self.messaging_profiles = messaging_profiles.AsyncMessagingProfilesResourceWithRawResponse(
            client.messaging_profiles
        )
        self.messaging_tollfree = messaging_tollfree.AsyncMessagingTollfreeResourceWithRawResponse(
            client.messaging_tollfree
        )
        self.messaging_url_domains = messaging_url_domains.AsyncMessagingURLDomainsResourceWithRawResponse(
            client.messaging_url_domains
        )
        self.messsages = messsages.AsyncMesssagesResourceWithRawResponse(client.messsages)
        self.mobile_network_operators = mobile_network_operators.AsyncMobileNetworkOperatorsResourceWithRawResponse(
            client.mobile_network_operators
        )
        self.mobile_push_credentials = mobile_push_credentials.AsyncMobilePushCredentialsResourceWithRawResponse(
            client.mobile_push_credentials
        )
        self.network_coverage = network_coverage.AsyncNetworkCoverageResourceWithRawResponse(client.network_coverage)
        self.networks = networks.AsyncNetworksResourceWithRawResponse(client.networks)
        self.notification_channels = notification_channels.AsyncNotificationChannelsResourceWithRawResponse(
            client.notification_channels
        )
        self.notification_event_conditions = (
            notification_event_conditions.AsyncNotificationEventConditionsResourceWithRawResponse(
                client.notification_event_conditions
            )
        )
        self.notification_events = notification_events.AsyncNotificationEventsResourceWithRawResponse(
            client.notification_events
        )
        self.notification_profiles = notification_profiles.AsyncNotificationProfilesResourceWithRawResponse(
            client.notification_profiles
        )
        self.notification_settings = notification_settings.AsyncNotificationSettingsResourceWithRawResponse(
            client.notification_settings
        )
        self.number_block_orders = number_block_orders.AsyncNumberBlockOrdersResourceWithRawResponse(
            client.number_block_orders
        )
        self.number_lookup = number_lookup.AsyncNumberLookupResourceWithRawResponse(client.number_lookup)
        self.number_order_phone_numbers = (
            number_order_phone_numbers.AsyncNumberOrderPhoneNumbersResourceWithRawResponse(
                client.number_order_phone_numbers
            )
        )
        self.number_orders = number_orders.AsyncNumberOrdersResourceWithRawResponse(client.number_orders)
        self.number_reservations = number_reservations.AsyncNumberReservationsResourceWithRawResponse(
            client.number_reservations
        )
        self.numbers_features = numbers_features.AsyncNumbersFeaturesResourceWithRawResponse(client.numbers_features)
        self.operator_connect = operator_connect.AsyncOperatorConnectResourceWithRawResponse(client.operator_connect)
        self.ota_updates = ota_updates.AsyncOtaUpdatesResourceWithRawResponse(client.ota_updates)
        self.outbound_voice_profiles = outbound_voice_profiles.AsyncOutboundVoiceProfilesResourceWithRawResponse(
            client.outbound_voice_profiles
        )
        self.payment = payment.AsyncPaymentResourceWithRawResponse(client.payment)
        self.phone_number_assignment_by_profile = (
            phone_number_assignment_by_profile.AsyncPhoneNumberAssignmentByProfileResourceWithRawResponse(
                client.phone_number_assignment_by_profile
            )
        )
        self.phone_number_blocks = phone_number_blocks.AsyncPhoneNumberBlocksResourceWithRawResponse(
            client.phone_number_blocks
        )
        self.phone_number_campaigns = phone_number_campaigns.AsyncPhoneNumberCampaignsResourceWithRawResponse(
            client.phone_number_campaigns
        )
        self.phone_numbers = phone_numbers.AsyncPhoneNumbersResourceWithRawResponse(client.phone_numbers)
        self.phone_numbers_regulatory_requirements = (
            phone_numbers_regulatory_requirements.AsyncPhoneNumbersRegulatoryRequirementsResourceWithRawResponse(
                client.phone_numbers_regulatory_requirements
            )
        )
        self.portability_checks = portability_checks.AsyncPortabilityChecksResourceWithRawResponse(
            client.portability_checks
        )
        self.porting = porting.AsyncPortingResourceWithRawResponse(client.porting)
        self.porting_orders = porting_orders.AsyncPortingOrdersResourceWithRawResponse(client.porting_orders)
        self.porting_phone_numbers = porting_phone_numbers.AsyncPortingPhoneNumbersResourceWithRawResponse(
            client.porting_phone_numbers
        )
        self.portouts = portouts.AsyncPortoutsResourceWithRawResponse(client.portouts)
        self.private_wireless_gateways = private_wireless_gateways.AsyncPrivateWirelessGatewaysResourceWithRawResponse(
            client.private_wireless_gateways
        )
        self.public_internet_gateways = public_internet_gateways.AsyncPublicInternetGatewaysResourceWithRawResponse(
            client.public_internet_gateways
        )
        self.queues = queues.AsyncQueuesResourceWithRawResponse(client.queues)
        self.recording_transcriptions = recording_transcriptions.AsyncRecordingTranscriptionsResourceWithRawResponse(
            client.recording_transcriptions
        )
        self.recordings = recordings.AsyncRecordingsResourceWithRawResponse(client.recordings)
        self.regions = regions.AsyncRegionsResourceWithRawResponse(client.regions)
        self.regulatory_requirements = regulatory_requirements.AsyncRegulatoryRequirementsResourceWithRawResponse(
            client.regulatory_requirements
        )
        self.reports = reports.AsyncReportsResourceWithRawResponse(client.reports)
        self.requirement_groups = requirement_groups.AsyncRequirementGroupsResourceWithRawResponse(
            client.requirement_groups
        )
        self.requirement_types = requirement_types.AsyncRequirementTypesResourceWithRawResponse(
            client.requirement_types
        )
        self.requirements = requirements.AsyncRequirementsResourceWithRawResponse(client.requirements)
        self.room_compositions = room_compositions.AsyncRoomCompositionsResourceWithRawResponse(
            client.room_compositions
        )
        self.room_participants = room_participants.AsyncRoomParticipantsResourceWithRawResponse(
            client.room_participants
        )
        self.room_recordings = room_recordings.AsyncRoomRecordingsResourceWithRawResponse(client.room_recordings)
        self.rooms = rooms.AsyncRoomsResourceWithRawResponse(client.rooms)
        self.seti = seti.AsyncSetiResourceWithRawResponse(client.seti)
        self.short_codes = short_codes.AsyncShortCodesResourceWithRawResponse(client.short_codes)
        self.sim_card_data_usage_notifications = (
            sim_card_data_usage_notifications.AsyncSimCardDataUsageNotificationsResourceWithRawResponse(
                client.sim_card_data_usage_notifications
            )
        )
        self.sim_card_groups = sim_card_groups.AsyncSimCardGroupsResourceWithRawResponse(client.sim_card_groups)
        self.sim_card_order_preview = sim_card_order_preview.AsyncSimCardOrderPreviewResourceWithRawResponse(
            client.sim_card_order_preview
        )
        self.sim_card_orders = sim_card_orders.AsyncSimCardOrdersResourceWithRawResponse(client.sim_card_orders)
        self.sim_cards = sim_cards.AsyncSimCardsResourceWithRawResponse(client.sim_cards)
        self.siprec_connectors = siprec_connectors.AsyncSiprecConnectorsResourceWithRawResponse(
            client.siprec_connectors
        )
        self.storage = storage.AsyncStorageResourceWithRawResponse(client.storage)
        self.sub_number_orders = sub_number_orders.AsyncSubNumberOrdersResourceWithRawResponse(client.sub_number_orders)
        self.sub_number_orders_report = sub_number_orders_report.AsyncSubNumberOrdersReportResourceWithRawResponse(
            client.sub_number_orders_report
        )
        self.telephony_credentials = telephony_credentials.AsyncTelephonyCredentialsResourceWithRawResponse(
            client.telephony_credentials
        )
        self.texml = texml.AsyncTexmlResourceWithRawResponse(client.texml)
        self.texml_applications = texml_applications.AsyncTexmlApplicationsResourceWithRawResponse(
            client.texml_applications
        )
        self.text_to_speech = text_to_speech.AsyncTextToSpeechResourceWithRawResponse(client.text_to_speech)
        self.usage_reports = usage_reports.AsyncUsageReportsResourceWithRawResponse(client.usage_reports)
        self.user_addresses = user_addresses.AsyncUserAddressesResourceWithRawResponse(client.user_addresses)
        self.user_tags = user_tags.AsyncUserTagsResourceWithRawResponse(client.user_tags)
        self.verifications = verifications.AsyncVerificationsResourceWithRawResponse(client.verifications)
        self.verified_numbers = verified_numbers.AsyncVerifiedNumbersResourceWithRawResponse(client.verified_numbers)
        self.verify_profiles = verify_profiles.AsyncVerifyProfilesResourceWithRawResponse(client.verify_profiles)
        self.virtual_cross_connects = virtual_cross_connects.AsyncVirtualCrossConnectsResourceWithRawResponse(
            client.virtual_cross_connects
        )
        self.virtual_cross_connects_coverage = (
            virtual_cross_connects_coverage.AsyncVirtualCrossConnectsCoverageResourceWithRawResponse(
                client.virtual_cross_connects_coverage
            )
        )
        self.webhook_deliveries = webhook_deliveries.AsyncWebhookDeliveriesResourceWithRawResponse(
            client.webhook_deliveries
        )
        self.wireguard_interfaces = wireguard_interfaces.AsyncWireguardInterfacesResourceWithRawResponse(
            client.wireguard_interfaces
        )
        self.wireguard_peers = wireguard_peers.AsyncWireguardPeersResourceWithRawResponse(client.wireguard_peers)
        self.wireless = wireless.AsyncWirelessResourceWithRawResponse(client.wireless)
        self.wireless_blocklist_values = wireless_blocklist_values.AsyncWirelessBlocklistValuesResourceWithRawResponse(
            client.wireless_blocklist_values
        )
        self.wireless_blocklists = wireless_blocklists.AsyncWirelessBlocklistsResourceWithRawResponse(
            client.wireless_blocklists
        )
        self.partner_campaigns = partner_campaigns.AsyncPartnerCampaignsResourceWithRawResponse(
            client.partner_campaigns
        )

        self.create_bucket = async_to_raw_response_wrapper(
            client.create_bucket,
        )
        self.delete_bucket = async_to_raw_response_wrapper(
            client.delete_bucket,
        )
        self.delete_object = async_to_raw_response_wrapper(
            client.delete_object,
        )
        self.delete_objects = async_to_raw_response_wrapper(
            client.delete_objects,
        )
        self.get_object = async_to_custom_raw_response_wrapper(
            client.get_object,
            AsyncBinaryAPIResponse,
        )
        self.list_buckets = async_to_raw_response_wrapper(
            client.list_buckets,
        )
        self.list_objects = async_to_raw_response_wrapper(
            client.list_objects,
        )
        self.put_object = async_to_raw_response_wrapper(
            client.put_object,
        )


class TelnyxWithStreamedResponse:
    def __init__(self, client: Telnyx) -> None:
        self.access_ip_address = access_ip_address.AccessIPAddressResourceWithStreamingResponse(
            client.access_ip_address
        )
        self.access_ip_ranges = access_ip_ranges.AccessIPRangesResourceWithStreamingResponse(client.access_ip_ranges)
        self.actions = actions.ActionsResourceWithStreamingResponse(client.actions)
        self.addresses = addresses.AddressesResourceWithStreamingResponse(client.addresses)
        self.advanced_orders = advanced_orders.AdvancedOrdersResourceWithStreamingResponse(client.advanced_orders)
        self.ai = ai.AIResourceWithStreamingResponse(client.ai)
        self.audit_events = audit_events.AuditEventsResourceWithStreamingResponse(client.audit_events)
        self.authentication_providers = authentication_providers.AuthenticationProvidersResourceWithStreamingResponse(
            client.authentication_providers
        )
        self.available_phone_number_blocks = (
            available_phone_number_blocks.AvailablePhoneNumberBlocksResourceWithStreamingResponse(
                client.available_phone_number_blocks
            )
        )
        self.available_phone_numbers = available_phone_numbers.AvailablePhoneNumbersResourceWithStreamingResponse(
            client.available_phone_numbers
        )
        self.balance = balance.BalanceResourceWithStreamingResponse(client.balance)
        self.billing_groups = billing_groups.BillingGroupsResourceWithStreamingResponse(client.billing_groups)
        self.brand = brand.BrandResourceWithStreamingResponse(client.brand)
        self.bulk_sim_card_actions = bulk_sim_card_actions.BulkSimCardActionsResourceWithStreamingResponse(
            client.bulk_sim_card_actions
        )
        self.bundle_pricing = bundle_pricing.BundlePricingResourceWithStreamingResponse(client.bundle_pricing)
        self.call_control_applications = call_control_applications.CallControlApplicationsResourceWithStreamingResponse(
            client.call_control_applications
        )
        self.call_events = call_events.CallEventsResourceWithStreamingResponse(client.call_events)
        self.calls = calls.CallsResourceWithStreamingResponse(client.calls)
        self.campaign = campaign.CampaignResourceWithStreamingResponse(client.campaign)
        self.campaign_builder = campaign_builder.CampaignBuilderResourceWithStreamingResponse(client.campaign_builder)
        self.channel_zones = channel_zones.ChannelZonesResourceWithStreamingResponse(client.channel_zones)
        self.charges_breakdown = charges_breakdown.ChargesBreakdownResourceWithStreamingResponse(
            client.charges_breakdown
        )
        self.charges_summary = charges_summary.ChargesSummaryResourceWithStreamingResponse(client.charges_summary)
        self.comments = comments.CommentsResourceWithStreamingResponse(client.comments)
        self.conferences = conferences.ConferencesResourceWithStreamingResponse(client.conferences)
        self.connections = connections.ConnectionsResourceWithStreamingResponse(client.connections)
        self.country_coverage = country_coverage.CountryCoverageResourceWithStreamingResponse(client.country_coverage)
        self.credential_connections = credential_connections.CredentialConnectionsResourceWithStreamingResponse(
            client.credential_connections
        )
        self.custom_storage_credentials = (
            custom_storage_credentials.CustomStorageCredentialsResourceWithStreamingResponse(
                client.custom_storage_credentials
            )
        )
        self.customer_service_records = customer_service_records.CustomerServiceRecordsResourceWithStreamingResponse(
            client.customer_service_records
        )
        self.detail_records = detail_records.DetailRecordsResourceWithStreamingResponse(client.detail_records)
        self.dialogflow_connections = dialogflow_connections.DialogflowConnectionsResourceWithStreamingResponse(
            client.dialogflow_connections
        )
        self.document_links = document_links.DocumentLinksResourceWithStreamingResponse(client.document_links)
        self.documents = documents.DocumentsResourceWithStreamingResponse(client.documents)
        self.dynamic_emergency_addresses = (
            dynamic_emergency_addresses.DynamicEmergencyAddressesResourceWithStreamingResponse(
                client.dynamic_emergency_addresses
            )
        )
        self.dynamic_emergency_endpoints = (
            dynamic_emergency_endpoints.DynamicEmergencyEndpointsResourceWithStreamingResponse(
                client.dynamic_emergency_endpoints
            )
        )
        self.enum = enum.EnumResourceWithStreamingResponse(client.enum)
        self.external_connections = external_connections.ExternalConnectionsResourceWithStreamingResponse(
            client.external_connections
        )
        self.fax_applications = fax_applications.FaxApplicationsResourceWithStreamingResponse(client.fax_applications)
        self.faxes = faxes.FaxesResourceWithStreamingResponse(client.faxes)
        self.fqdn_connections = fqdn_connections.FqdnConnectionsResourceWithStreamingResponse(client.fqdn_connections)
        self.fqdns = fqdns.FqdnsResourceWithStreamingResponse(client.fqdns)
        self.global_ip_allowed_ports = global_ip_allowed_ports.GlobalIPAllowedPortsResourceWithStreamingResponse(
            client.global_ip_allowed_ports
        )
        self.global_ip_assignment_health = (
            global_ip_assignment_health.GlobalIPAssignmentHealthResourceWithStreamingResponse(
                client.global_ip_assignment_health
            )
        )
        self.global_ip_assignments = global_ip_assignments.GlobalIPAssignmentsResourceWithStreamingResponse(
            client.global_ip_assignments
        )
        self.global_ip_assignments_usage = (
            global_ip_assignments_usage.GlobalIPAssignmentsUsageResourceWithStreamingResponse(
                client.global_ip_assignments_usage
            )
        )
        self.global_ip_health_check_types = (
            global_ip_health_check_types.GlobalIPHealthCheckTypesResourceWithStreamingResponse(
                client.global_ip_health_check_types
            )
        )
        self.global_ip_health_checks = global_ip_health_checks.GlobalIPHealthChecksResourceWithStreamingResponse(
            client.global_ip_health_checks
        )
        self.global_ip_latency = global_ip_latency.GlobalIPLatencyResourceWithStreamingResponse(
            client.global_ip_latency
        )
        self.global_ip_protocols = global_ip_protocols.GlobalIPProtocolsResourceWithStreamingResponse(
            client.global_ip_protocols
        )
        self.global_ip_usage = global_ip_usage.GlobalIPUsageResourceWithStreamingResponse(client.global_ip_usage)
        self.global_ips = global_ips.GlobalIPsResourceWithStreamingResponse(client.global_ips)
        self.inbound_channels = inbound_channels.InboundChannelsResourceWithStreamingResponse(client.inbound_channels)
        self.integration_secrets = integration_secrets.IntegrationSecretsResourceWithStreamingResponse(
            client.integration_secrets
        )
        self.inventory_coverage = inventory_coverage.InventoryCoverageResourceWithStreamingResponse(
            client.inventory_coverage
        )
        self.invoices = invoices.InvoicesResourceWithStreamingResponse(client.invoices)
        self.ip_connections = ip_connections.IPConnectionsResourceWithStreamingResponse(client.ip_connections)
        self.ips = ips.IPsResourceWithStreamingResponse(client.ips)
        self.ledger_billing_group_reports = (
            ledger_billing_group_reports.LedgerBillingGroupReportsResourceWithStreamingResponse(
                client.ledger_billing_group_reports
            )
        )
        self.list = list.ListResourceWithStreamingResponse(client.list)
        self.managed_accounts = managed_accounts.ManagedAccountsResourceWithStreamingResponse(client.managed_accounts)
        self.media = media.MediaResourceWithStreamingResponse(client.media)
        self.messages = messages.MessagesResourceWithStreamingResponse(client.messages)
        self.messaging = messaging.MessagingResourceWithStreamingResponse(client.messaging)
        self.messaging_hosted_number_orders = (
            messaging_hosted_number_orders.MessagingHostedNumberOrdersResourceWithStreamingResponse(
                client.messaging_hosted_number_orders
            )
        )
        self.messaging_hosted_numbers = messaging_hosted_numbers.MessagingHostedNumbersResourceWithStreamingResponse(
            client.messaging_hosted_numbers
        )
        self.messaging_numbers_bulk_updates = (
            messaging_numbers_bulk_updates.MessagingNumbersBulkUpdatesResourceWithStreamingResponse(
                client.messaging_numbers_bulk_updates
            )
        )
        self.messaging_optouts = messaging_optouts.MessagingOptoutsResourceWithStreamingResponse(
            client.messaging_optouts
        )
        self.messaging_profiles = messaging_profiles.MessagingProfilesResourceWithStreamingResponse(
            client.messaging_profiles
        )
        self.messaging_tollfree = messaging_tollfree.MessagingTollfreeResourceWithStreamingResponse(
            client.messaging_tollfree
        )
        self.messaging_url_domains = messaging_url_domains.MessagingURLDomainsResourceWithStreamingResponse(
            client.messaging_url_domains
        )
        self.messsages = messsages.MesssagesResourceWithStreamingResponse(client.messsages)
        self.mobile_network_operators = mobile_network_operators.MobileNetworkOperatorsResourceWithStreamingResponse(
            client.mobile_network_operators
        )
        self.mobile_push_credentials = mobile_push_credentials.MobilePushCredentialsResourceWithStreamingResponse(
            client.mobile_push_credentials
        )
        self.network_coverage = network_coverage.NetworkCoverageResourceWithStreamingResponse(client.network_coverage)
        self.networks = networks.NetworksResourceWithStreamingResponse(client.networks)
        self.notification_channels = notification_channels.NotificationChannelsResourceWithStreamingResponse(
            client.notification_channels
        )
        self.notification_event_conditions = (
            notification_event_conditions.NotificationEventConditionsResourceWithStreamingResponse(
                client.notification_event_conditions
            )
        )
        self.notification_events = notification_events.NotificationEventsResourceWithStreamingResponse(
            client.notification_events
        )
        self.notification_profiles = notification_profiles.NotificationProfilesResourceWithStreamingResponse(
            client.notification_profiles
        )
        self.notification_settings = notification_settings.NotificationSettingsResourceWithStreamingResponse(
            client.notification_settings
        )
        self.number_block_orders = number_block_orders.NumberBlockOrdersResourceWithStreamingResponse(
            client.number_block_orders
        )
        self.number_lookup = number_lookup.NumberLookupResourceWithStreamingResponse(client.number_lookup)
        self.number_order_phone_numbers = (
            number_order_phone_numbers.NumberOrderPhoneNumbersResourceWithStreamingResponse(
                client.number_order_phone_numbers
            )
        )
        self.number_orders = number_orders.NumberOrdersResourceWithStreamingResponse(client.number_orders)
        self.number_reservations = number_reservations.NumberReservationsResourceWithStreamingResponse(
            client.number_reservations
        )
        self.numbers_features = numbers_features.NumbersFeaturesResourceWithStreamingResponse(client.numbers_features)
        self.operator_connect = operator_connect.OperatorConnectResourceWithStreamingResponse(client.operator_connect)
        self.ota_updates = ota_updates.OtaUpdatesResourceWithStreamingResponse(client.ota_updates)
        self.outbound_voice_profiles = outbound_voice_profiles.OutboundVoiceProfilesResourceWithStreamingResponse(
            client.outbound_voice_profiles
        )
        self.payment = payment.PaymentResourceWithStreamingResponse(client.payment)
        self.phone_number_assignment_by_profile = (
            phone_number_assignment_by_profile.PhoneNumberAssignmentByProfileResourceWithStreamingResponse(
                client.phone_number_assignment_by_profile
            )
        )
        self.phone_number_blocks = phone_number_blocks.PhoneNumberBlocksResourceWithStreamingResponse(
            client.phone_number_blocks
        )
        self.phone_number_campaigns = phone_number_campaigns.PhoneNumberCampaignsResourceWithStreamingResponse(
            client.phone_number_campaigns
        )
        self.phone_numbers = phone_numbers.PhoneNumbersResourceWithStreamingResponse(client.phone_numbers)
        self.phone_numbers_regulatory_requirements = (
            phone_numbers_regulatory_requirements.PhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse(
                client.phone_numbers_regulatory_requirements
            )
        )
        self.portability_checks = portability_checks.PortabilityChecksResourceWithStreamingResponse(
            client.portability_checks
        )
        self.porting = porting.PortingResourceWithStreamingResponse(client.porting)
        self.porting_orders = porting_orders.PortingOrdersResourceWithStreamingResponse(client.porting_orders)
        self.porting_phone_numbers = porting_phone_numbers.PortingPhoneNumbersResourceWithStreamingResponse(
            client.porting_phone_numbers
        )
        self.portouts = portouts.PortoutsResourceWithStreamingResponse(client.portouts)
        self.private_wireless_gateways = private_wireless_gateways.PrivateWirelessGatewaysResourceWithStreamingResponse(
            client.private_wireless_gateways
        )
        self.public_internet_gateways = public_internet_gateways.PublicInternetGatewaysResourceWithStreamingResponse(
            client.public_internet_gateways
        )
        self.queues = queues.QueuesResourceWithStreamingResponse(client.queues)
        self.recording_transcriptions = recording_transcriptions.RecordingTranscriptionsResourceWithStreamingResponse(
            client.recording_transcriptions
        )
        self.recordings = recordings.RecordingsResourceWithStreamingResponse(client.recordings)
        self.regions = regions.RegionsResourceWithStreamingResponse(client.regions)
        self.regulatory_requirements = regulatory_requirements.RegulatoryRequirementsResourceWithStreamingResponse(
            client.regulatory_requirements
        )
        self.reports = reports.ReportsResourceWithStreamingResponse(client.reports)
        self.requirement_groups = requirement_groups.RequirementGroupsResourceWithStreamingResponse(
            client.requirement_groups
        )
        self.requirement_types = requirement_types.RequirementTypesResourceWithStreamingResponse(
            client.requirement_types
        )
        self.requirements = requirements.RequirementsResourceWithStreamingResponse(client.requirements)
        self.room_compositions = room_compositions.RoomCompositionsResourceWithStreamingResponse(
            client.room_compositions
        )
        self.room_participants = room_participants.RoomParticipantsResourceWithStreamingResponse(
            client.room_participants
        )
        self.room_recordings = room_recordings.RoomRecordingsResourceWithStreamingResponse(client.room_recordings)
        self.rooms = rooms.RoomsResourceWithStreamingResponse(client.rooms)
        self.seti = seti.SetiResourceWithStreamingResponse(client.seti)
        self.short_codes = short_codes.ShortCodesResourceWithStreamingResponse(client.short_codes)
        self.sim_card_data_usage_notifications = (
            sim_card_data_usage_notifications.SimCardDataUsageNotificationsResourceWithStreamingResponse(
                client.sim_card_data_usage_notifications
            )
        )
        self.sim_card_groups = sim_card_groups.SimCardGroupsResourceWithStreamingResponse(client.sim_card_groups)
        self.sim_card_order_preview = sim_card_order_preview.SimCardOrderPreviewResourceWithStreamingResponse(
            client.sim_card_order_preview
        )
        self.sim_card_orders = sim_card_orders.SimCardOrdersResourceWithStreamingResponse(client.sim_card_orders)
        self.sim_cards = sim_cards.SimCardsResourceWithStreamingResponse(client.sim_cards)
        self.siprec_connectors = siprec_connectors.SiprecConnectorsResourceWithStreamingResponse(
            client.siprec_connectors
        )
        self.storage = storage.StorageResourceWithStreamingResponse(client.storage)
        self.sub_number_orders = sub_number_orders.SubNumberOrdersResourceWithStreamingResponse(
            client.sub_number_orders
        )
        self.sub_number_orders_report = sub_number_orders_report.SubNumberOrdersReportResourceWithStreamingResponse(
            client.sub_number_orders_report
        )
        self.telephony_credentials = telephony_credentials.TelephonyCredentialsResourceWithStreamingResponse(
            client.telephony_credentials
        )
        self.texml = texml.TexmlResourceWithStreamingResponse(client.texml)
        self.texml_applications = texml_applications.TexmlApplicationsResourceWithStreamingResponse(
            client.texml_applications
        )
        self.text_to_speech = text_to_speech.TextToSpeechResourceWithStreamingResponse(client.text_to_speech)
        self.usage_reports = usage_reports.UsageReportsResourceWithStreamingResponse(client.usage_reports)
        self.user_addresses = user_addresses.UserAddressesResourceWithStreamingResponse(client.user_addresses)
        self.user_tags = user_tags.UserTagsResourceWithStreamingResponse(client.user_tags)
        self.verifications = verifications.VerificationsResourceWithStreamingResponse(client.verifications)
        self.verified_numbers = verified_numbers.VerifiedNumbersResourceWithStreamingResponse(client.verified_numbers)
        self.verify_profiles = verify_profiles.VerifyProfilesResourceWithStreamingResponse(client.verify_profiles)
        self.virtual_cross_connects = virtual_cross_connects.VirtualCrossConnectsResourceWithStreamingResponse(
            client.virtual_cross_connects
        )
        self.virtual_cross_connects_coverage = (
            virtual_cross_connects_coverage.VirtualCrossConnectsCoverageResourceWithStreamingResponse(
                client.virtual_cross_connects_coverage
            )
        )
        self.webhook_deliveries = webhook_deliveries.WebhookDeliveriesResourceWithStreamingResponse(
            client.webhook_deliveries
        )
        self.wireguard_interfaces = wireguard_interfaces.WireguardInterfacesResourceWithStreamingResponse(
            client.wireguard_interfaces
        )
        self.wireguard_peers = wireguard_peers.WireguardPeersResourceWithStreamingResponse(client.wireguard_peers)
        self.wireless = wireless.WirelessResourceWithStreamingResponse(client.wireless)
        self.wireless_blocklist_values = wireless_blocklist_values.WirelessBlocklistValuesResourceWithStreamingResponse(
            client.wireless_blocklist_values
        )
        self.wireless_blocklists = wireless_blocklists.WirelessBlocklistsResourceWithStreamingResponse(
            client.wireless_blocklists
        )
        self.partner_campaigns = partner_campaigns.PartnerCampaignsResourceWithStreamingResponse(
            client.partner_campaigns
        )

        self.create_bucket = to_streamed_response_wrapper(
            client.create_bucket,
        )
        self.delete_bucket = to_streamed_response_wrapper(
            client.delete_bucket,
        )
        self.delete_object = to_streamed_response_wrapper(
            client.delete_object,
        )
        self.delete_objects = to_streamed_response_wrapper(
            client.delete_objects,
        )
        self.get_object = to_custom_streamed_response_wrapper(
            client.get_object,
            StreamedBinaryAPIResponse,
        )
        self.list_buckets = to_streamed_response_wrapper(
            client.list_buckets,
        )
        self.list_objects = to_streamed_response_wrapper(
            client.list_objects,
        )
        self.put_object = to_streamed_response_wrapper(
            client.put_object,
        )


class AsyncTelnyxWithStreamedResponse:
    def __init__(self, client: AsyncTelnyx) -> None:
        self.access_ip_address = access_ip_address.AsyncAccessIPAddressResourceWithStreamingResponse(
            client.access_ip_address
        )
        self.access_ip_ranges = access_ip_ranges.AsyncAccessIPRangesResourceWithStreamingResponse(
            client.access_ip_ranges
        )
        self.actions = actions.AsyncActionsResourceWithStreamingResponse(client.actions)
        self.addresses = addresses.AsyncAddressesResourceWithStreamingResponse(client.addresses)
        self.advanced_orders = advanced_orders.AsyncAdvancedOrdersResourceWithStreamingResponse(client.advanced_orders)
        self.ai = ai.AsyncAIResourceWithStreamingResponse(client.ai)
        self.audit_events = audit_events.AsyncAuditEventsResourceWithStreamingResponse(client.audit_events)
        self.authentication_providers = (
            authentication_providers.AsyncAuthenticationProvidersResourceWithStreamingResponse(
                client.authentication_providers
            )
        )
        self.available_phone_number_blocks = (
            available_phone_number_blocks.AsyncAvailablePhoneNumberBlocksResourceWithStreamingResponse(
                client.available_phone_number_blocks
            )
        )
        self.available_phone_numbers = available_phone_numbers.AsyncAvailablePhoneNumbersResourceWithStreamingResponse(
            client.available_phone_numbers
        )
        self.balance = balance.AsyncBalanceResourceWithStreamingResponse(client.balance)
        self.billing_groups = billing_groups.AsyncBillingGroupsResourceWithStreamingResponse(client.billing_groups)
        self.brand = brand.AsyncBrandResourceWithStreamingResponse(client.brand)
        self.bulk_sim_card_actions = bulk_sim_card_actions.AsyncBulkSimCardActionsResourceWithStreamingResponse(
            client.bulk_sim_card_actions
        )
        self.bundle_pricing = bundle_pricing.AsyncBundlePricingResourceWithStreamingResponse(client.bundle_pricing)
        self.call_control_applications = (
            call_control_applications.AsyncCallControlApplicationsResourceWithStreamingResponse(
                client.call_control_applications
            )
        )
        self.call_events = call_events.AsyncCallEventsResourceWithStreamingResponse(client.call_events)
        self.calls = calls.AsyncCallsResourceWithStreamingResponse(client.calls)
        self.campaign = campaign.AsyncCampaignResourceWithStreamingResponse(client.campaign)
        self.campaign_builder = campaign_builder.AsyncCampaignBuilderResourceWithStreamingResponse(
            client.campaign_builder
        )
        self.channel_zones = channel_zones.AsyncChannelZonesResourceWithStreamingResponse(client.channel_zones)
        self.charges_breakdown = charges_breakdown.AsyncChargesBreakdownResourceWithStreamingResponse(
            client.charges_breakdown
        )
        self.charges_summary = charges_summary.AsyncChargesSummaryResourceWithStreamingResponse(client.charges_summary)
        self.comments = comments.AsyncCommentsResourceWithStreamingResponse(client.comments)
        self.conferences = conferences.AsyncConferencesResourceWithStreamingResponse(client.conferences)
        self.connections = connections.AsyncConnectionsResourceWithStreamingResponse(client.connections)
        self.country_coverage = country_coverage.AsyncCountryCoverageResourceWithStreamingResponse(
            client.country_coverage
        )
        self.credential_connections = credential_connections.AsyncCredentialConnectionsResourceWithStreamingResponse(
            client.credential_connections
        )
        self.custom_storage_credentials = (
            custom_storage_credentials.AsyncCustomStorageCredentialsResourceWithStreamingResponse(
                client.custom_storage_credentials
            )
        )
        self.customer_service_records = (
            customer_service_records.AsyncCustomerServiceRecordsResourceWithStreamingResponse(
                client.customer_service_records
            )
        )
        self.detail_records = detail_records.AsyncDetailRecordsResourceWithStreamingResponse(client.detail_records)
        self.dialogflow_connections = dialogflow_connections.AsyncDialogflowConnectionsResourceWithStreamingResponse(
            client.dialogflow_connections
        )
        self.document_links = document_links.AsyncDocumentLinksResourceWithStreamingResponse(client.document_links)
        self.documents = documents.AsyncDocumentsResourceWithStreamingResponse(client.documents)
        self.dynamic_emergency_addresses = (
            dynamic_emergency_addresses.AsyncDynamicEmergencyAddressesResourceWithStreamingResponse(
                client.dynamic_emergency_addresses
            )
        )
        self.dynamic_emergency_endpoints = (
            dynamic_emergency_endpoints.AsyncDynamicEmergencyEndpointsResourceWithStreamingResponse(
                client.dynamic_emergency_endpoints
            )
        )
        self.enum = enum.AsyncEnumResourceWithStreamingResponse(client.enum)
        self.external_connections = external_connections.AsyncExternalConnectionsResourceWithStreamingResponse(
            client.external_connections
        )
        self.fax_applications = fax_applications.AsyncFaxApplicationsResourceWithStreamingResponse(
            client.fax_applications
        )
        self.faxes = faxes.AsyncFaxesResourceWithStreamingResponse(client.faxes)
        self.fqdn_connections = fqdn_connections.AsyncFqdnConnectionsResourceWithStreamingResponse(
            client.fqdn_connections
        )
        self.fqdns = fqdns.AsyncFqdnsResourceWithStreamingResponse(client.fqdns)
        self.global_ip_allowed_ports = global_ip_allowed_ports.AsyncGlobalIPAllowedPortsResourceWithStreamingResponse(
            client.global_ip_allowed_ports
        )
        self.global_ip_assignment_health = (
            global_ip_assignment_health.AsyncGlobalIPAssignmentHealthResourceWithStreamingResponse(
                client.global_ip_assignment_health
            )
        )
        self.global_ip_assignments = global_ip_assignments.AsyncGlobalIPAssignmentsResourceWithStreamingResponse(
            client.global_ip_assignments
        )
        self.global_ip_assignments_usage = (
            global_ip_assignments_usage.AsyncGlobalIPAssignmentsUsageResourceWithStreamingResponse(
                client.global_ip_assignments_usage
            )
        )
        self.global_ip_health_check_types = (
            global_ip_health_check_types.AsyncGlobalIPHealthCheckTypesResourceWithStreamingResponse(
                client.global_ip_health_check_types
            )
        )
        self.global_ip_health_checks = global_ip_health_checks.AsyncGlobalIPHealthChecksResourceWithStreamingResponse(
            client.global_ip_health_checks
        )
        self.global_ip_latency = global_ip_latency.AsyncGlobalIPLatencyResourceWithStreamingResponse(
            client.global_ip_latency
        )
        self.global_ip_protocols = global_ip_protocols.AsyncGlobalIPProtocolsResourceWithStreamingResponse(
            client.global_ip_protocols
        )
        self.global_ip_usage = global_ip_usage.AsyncGlobalIPUsageResourceWithStreamingResponse(client.global_ip_usage)
        self.global_ips = global_ips.AsyncGlobalIPsResourceWithStreamingResponse(client.global_ips)
        self.inbound_channels = inbound_channels.AsyncInboundChannelsResourceWithStreamingResponse(
            client.inbound_channels
        )
        self.integration_secrets = integration_secrets.AsyncIntegrationSecretsResourceWithStreamingResponse(
            client.integration_secrets
        )
        self.inventory_coverage = inventory_coverage.AsyncInventoryCoverageResourceWithStreamingResponse(
            client.inventory_coverage
        )
        self.invoices = invoices.AsyncInvoicesResourceWithStreamingResponse(client.invoices)
        self.ip_connections = ip_connections.AsyncIPConnectionsResourceWithStreamingResponse(client.ip_connections)
        self.ips = ips.AsyncIPsResourceWithStreamingResponse(client.ips)
        self.ledger_billing_group_reports = (
            ledger_billing_group_reports.AsyncLedgerBillingGroupReportsResourceWithStreamingResponse(
                client.ledger_billing_group_reports
            )
        )
        self.list = list.AsyncListResourceWithStreamingResponse(client.list)
        self.managed_accounts = managed_accounts.AsyncManagedAccountsResourceWithStreamingResponse(
            client.managed_accounts
        )
        self.media = media.AsyncMediaResourceWithStreamingResponse(client.media)
        self.messages = messages.AsyncMessagesResourceWithStreamingResponse(client.messages)
        self.messaging = messaging.AsyncMessagingResourceWithStreamingResponse(client.messaging)
        self.messaging_hosted_number_orders = (
            messaging_hosted_number_orders.AsyncMessagingHostedNumberOrdersResourceWithStreamingResponse(
                client.messaging_hosted_number_orders
            )
        )
        self.messaging_hosted_numbers = (
            messaging_hosted_numbers.AsyncMessagingHostedNumbersResourceWithStreamingResponse(
                client.messaging_hosted_numbers
            )
        )
        self.messaging_numbers_bulk_updates = (
            messaging_numbers_bulk_updates.AsyncMessagingNumbersBulkUpdatesResourceWithStreamingResponse(
                client.messaging_numbers_bulk_updates
            )
        )
        self.messaging_optouts = messaging_optouts.AsyncMessagingOptoutsResourceWithStreamingResponse(
            client.messaging_optouts
        )
        self.messaging_profiles = messaging_profiles.AsyncMessagingProfilesResourceWithStreamingResponse(
            client.messaging_profiles
        )
        self.messaging_tollfree = messaging_tollfree.AsyncMessagingTollfreeResourceWithStreamingResponse(
            client.messaging_tollfree
        )
        self.messaging_url_domains = messaging_url_domains.AsyncMessagingURLDomainsResourceWithStreamingResponse(
            client.messaging_url_domains
        )
        self.messsages = messsages.AsyncMesssagesResourceWithStreamingResponse(client.messsages)
        self.mobile_network_operators = (
            mobile_network_operators.AsyncMobileNetworkOperatorsResourceWithStreamingResponse(
                client.mobile_network_operators
            )
        )
        self.mobile_push_credentials = mobile_push_credentials.AsyncMobilePushCredentialsResourceWithStreamingResponse(
            client.mobile_push_credentials
        )
        self.network_coverage = network_coverage.AsyncNetworkCoverageResourceWithStreamingResponse(
            client.network_coverage
        )
        self.networks = networks.AsyncNetworksResourceWithStreamingResponse(client.networks)
        self.notification_channels = notification_channels.AsyncNotificationChannelsResourceWithStreamingResponse(
            client.notification_channels
        )
        self.notification_event_conditions = (
            notification_event_conditions.AsyncNotificationEventConditionsResourceWithStreamingResponse(
                client.notification_event_conditions
            )
        )
        self.notification_events = notification_events.AsyncNotificationEventsResourceWithStreamingResponse(
            client.notification_events
        )
        self.notification_profiles = notification_profiles.AsyncNotificationProfilesResourceWithStreamingResponse(
            client.notification_profiles
        )
        self.notification_settings = notification_settings.AsyncNotificationSettingsResourceWithStreamingResponse(
            client.notification_settings
        )
        self.number_block_orders = number_block_orders.AsyncNumberBlockOrdersResourceWithStreamingResponse(
            client.number_block_orders
        )
        self.number_lookup = number_lookup.AsyncNumberLookupResourceWithStreamingResponse(client.number_lookup)
        self.number_order_phone_numbers = (
            number_order_phone_numbers.AsyncNumberOrderPhoneNumbersResourceWithStreamingResponse(
                client.number_order_phone_numbers
            )
        )
        self.number_orders = number_orders.AsyncNumberOrdersResourceWithStreamingResponse(client.number_orders)
        self.number_reservations = number_reservations.AsyncNumberReservationsResourceWithStreamingResponse(
            client.number_reservations
        )
        self.numbers_features = numbers_features.AsyncNumbersFeaturesResourceWithStreamingResponse(
            client.numbers_features
        )
        self.operator_connect = operator_connect.AsyncOperatorConnectResourceWithStreamingResponse(
            client.operator_connect
        )
        self.ota_updates = ota_updates.AsyncOtaUpdatesResourceWithStreamingResponse(client.ota_updates)
        self.outbound_voice_profiles = outbound_voice_profiles.AsyncOutboundVoiceProfilesResourceWithStreamingResponse(
            client.outbound_voice_profiles
        )
        self.payment = payment.AsyncPaymentResourceWithStreamingResponse(client.payment)
        self.phone_number_assignment_by_profile = (
            phone_number_assignment_by_profile.AsyncPhoneNumberAssignmentByProfileResourceWithStreamingResponse(
                client.phone_number_assignment_by_profile
            )
        )
        self.phone_number_blocks = phone_number_blocks.AsyncPhoneNumberBlocksResourceWithStreamingResponse(
            client.phone_number_blocks
        )
        self.phone_number_campaigns = phone_number_campaigns.AsyncPhoneNumberCampaignsResourceWithStreamingResponse(
            client.phone_number_campaigns
        )
        self.phone_numbers = phone_numbers.AsyncPhoneNumbersResourceWithStreamingResponse(client.phone_numbers)
        self.phone_numbers_regulatory_requirements = (
            phone_numbers_regulatory_requirements.AsyncPhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse(
                client.phone_numbers_regulatory_requirements
            )
        )
        self.portability_checks = portability_checks.AsyncPortabilityChecksResourceWithStreamingResponse(
            client.portability_checks
        )
        self.porting = porting.AsyncPortingResourceWithStreamingResponse(client.porting)
        self.porting_orders = porting_orders.AsyncPortingOrdersResourceWithStreamingResponse(client.porting_orders)
        self.porting_phone_numbers = porting_phone_numbers.AsyncPortingPhoneNumbersResourceWithStreamingResponse(
            client.porting_phone_numbers
        )
        self.portouts = portouts.AsyncPortoutsResourceWithStreamingResponse(client.portouts)
        self.private_wireless_gateways = (
            private_wireless_gateways.AsyncPrivateWirelessGatewaysResourceWithStreamingResponse(
                client.private_wireless_gateways
            )
        )
        self.public_internet_gateways = (
            public_internet_gateways.AsyncPublicInternetGatewaysResourceWithStreamingResponse(
                client.public_internet_gateways
            )
        )
        self.queues = queues.AsyncQueuesResourceWithStreamingResponse(client.queues)
        self.recording_transcriptions = (
            recording_transcriptions.AsyncRecordingTranscriptionsResourceWithStreamingResponse(
                client.recording_transcriptions
            )
        )
        self.recordings = recordings.AsyncRecordingsResourceWithStreamingResponse(client.recordings)
        self.regions = regions.AsyncRegionsResourceWithStreamingResponse(client.regions)
        self.regulatory_requirements = regulatory_requirements.AsyncRegulatoryRequirementsResourceWithStreamingResponse(
            client.regulatory_requirements
        )
        self.reports = reports.AsyncReportsResourceWithStreamingResponse(client.reports)
        self.requirement_groups = requirement_groups.AsyncRequirementGroupsResourceWithStreamingResponse(
            client.requirement_groups
        )
        self.requirement_types = requirement_types.AsyncRequirementTypesResourceWithStreamingResponse(
            client.requirement_types
        )
        self.requirements = requirements.AsyncRequirementsResourceWithStreamingResponse(client.requirements)
        self.room_compositions = room_compositions.AsyncRoomCompositionsResourceWithStreamingResponse(
            client.room_compositions
        )
        self.room_participants = room_participants.AsyncRoomParticipantsResourceWithStreamingResponse(
            client.room_participants
        )
        self.room_recordings = room_recordings.AsyncRoomRecordingsResourceWithStreamingResponse(client.room_recordings)
        self.rooms = rooms.AsyncRoomsResourceWithStreamingResponse(client.rooms)
        self.seti = seti.AsyncSetiResourceWithStreamingResponse(client.seti)
        self.short_codes = short_codes.AsyncShortCodesResourceWithStreamingResponse(client.short_codes)
        self.sim_card_data_usage_notifications = (
            sim_card_data_usage_notifications.AsyncSimCardDataUsageNotificationsResourceWithStreamingResponse(
                client.sim_card_data_usage_notifications
            )
        )
        self.sim_card_groups = sim_card_groups.AsyncSimCardGroupsResourceWithStreamingResponse(client.sim_card_groups)
        self.sim_card_order_preview = sim_card_order_preview.AsyncSimCardOrderPreviewResourceWithStreamingResponse(
            client.sim_card_order_preview
        )
        self.sim_card_orders = sim_card_orders.AsyncSimCardOrdersResourceWithStreamingResponse(client.sim_card_orders)
        self.sim_cards = sim_cards.AsyncSimCardsResourceWithStreamingResponse(client.sim_cards)
        self.siprec_connectors = siprec_connectors.AsyncSiprecConnectorsResourceWithStreamingResponse(
            client.siprec_connectors
        )
        self.storage = storage.AsyncStorageResourceWithStreamingResponse(client.storage)
        self.sub_number_orders = sub_number_orders.AsyncSubNumberOrdersResourceWithStreamingResponse(
            client.sub_number_orders
        )
        self.sub_number_orders_report = (
            sub_number_orders_report.AsyncSubNumberOrdersReportResourceWithStreamingResponse(
                client.sub_number_orders_report
            )
        )
        self.telephony_credentials = telephony_credentials.AsyncTelephonyCredentialsResourceWithStreamingResponse(
            client.telephony_credentials
        )
        self.texml = texml.AsyncTexmlResourceWithStreamingResponse(client.texml)
        self.texml_applications = texml_applications.AsyncTexmlApplicationsResourceWithStreamingResponse(
            client.texml_applications
        )
        self.text_to_speech = text_to_speech.AsyncTextToSpeechResourceWithStreamingResponse(client.text_to_speech)
        self.usage_reports = usage_reports.AsyncUsageReportsResourceWithStreamingResponse(client.usage_reports)
        self.user_addresses = user_addresses.AsyncUserAddressesResourceWithStreamingResponse(client.user_addresses)
        self.user_tags = user_tags.AsyncUserTagsResourceWithStreamingResponse(client.user_tags)
        self.verifications = verifications.AsyncVerificationsResourceWithStreamingResponse(client.verifications)
        self.verified_numbers = verified_numbers.AsyncVerifiedNumbersResourceWithStreamingResponse(
            client.verified_numbers
        )
        self.verify_profiles = verify_profiles.AsyncVerifyProfilesResourceWithStreamingResponse(client.verify_profiles)
        self.virtual_cross_connects = virtual_cross_connects.AsyncVirtualCrossConnectsResourceWithStreamingResponse(
            client.virtual_cross_connects
        )
        self.virtual_cross_connects_coverage = (
            virtual_cross_connects_coverage.AsyncVirtualCrossConnectsCoverageResourceWithStreamingResponse(
                client.virtual_cross_connects_coverage
            )
        )
        self.webhook_deliveries = webhook_deliveries.AsyncWebhookDeliveriesResourceWithStreamingResponse(
            client.webhook_deliveries
        )
        self.wireguard_interfaces = wireguard_interfaces.AsyncWireguardInterfacesResourceWithStreamingResponse(
            client.wireguard_interfaces
        )
        self.wireguard_peers = wireguard_peers.AsyncWireguardPeersResourceWithStreamingResponse(client.wireguard_peers)
        self.wireless = wireless.AsyncWirelessResourceWithStreamingResponse(client.wireless)
        self.wireless_blocklist_values = (
            wireless_blocklist_values.AsyncWirelessBlocklistValuesResourceWithStreamingResponse(
                client.wireless_blocklist_values
            )
        )
        self.wireless_blocklists = wireless_blocklists.AsyncWirelessBlocklistsResourceWithStreamingResponse(
            client.wireless_blocklists
        )
        self.partner_campaigns = partner_campaigns.AsyncPartnerCampaignsResourceWithStreamingResponse(
            client.partner_campaigns
        )

        self.create_bucket = async_to_streamed_response_wrapper(
            client.create_bucket,
        )
        self.delete_bucket = async_to_streamed_response_wrapper(
            client.delete_bucket,
        )
        self.delete_object = async_to_streamed_response_wrapper(
            client.delete_object,
        )
        self.delete_objects = async_to_streamed_response_wrapper(
            client.delete_objects,
        )
        self.get_object = async_to_custom_streamed_response_wrapper(
            client.get_object,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list_buckets = async_to_streamed_response_wrapper(
            client.list_buckets,
        )
        self.list_objects = async_to_streamed_response_wrapper(
            client.list_objects,
        )
        self.put_object = async_to_streamed_response_wrapper(
            client.put_object,
        )


Client = Telnyx

AsyncClient = AsyncTelnyx
