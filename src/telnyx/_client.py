# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._oauth2 import OAuth2ClientCredentials, make_oauth2
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        ai,
        ips,
        list,
        seti,
        calls,
        faxes,
        fqdns,
        media,
        oauth,
        rooms,
        texml,
        legacy,
        queues,
        actions,
        balance,
        payment,
        porting,
        regions,
        reports,
        storage,
        comments,
        invoices,
        messages,
        networks,
        portouts,
        wireless,
        addresses,
        documents,
        messaging,
        sim_cards,
        user_tags,
        global_ips,
        recordings,
        well_known,
        call_events,
        conferences,
        connections,
        ota_updates,
        short_codes,
        audit_events,
        oauth_grants,
        requirements,
        channel_zones,
        number_lookup,
        number_orders,
        oauth_clients,
        organizations,
        phone_numbers,
        usage_reports,
        verifications,
        billing_groups,
        bundle_pricing,
        detail_records,
        document_links,
        ip_connections,
        porting_orders,
        text_to_speech,
        user_addresses,
        advanced_orders,
        charges_summary,
        global_ip_usage,
        messaging_10dlc,
        room_recordings,
        sim_card_groups,
        sim_card_orders,
        verify_profiles,
        wireguard_peers,
        access_ip_ranges,
        country_coverage,
        fax_applications,
        fqdn_connections,
        inbound_channels,
        managed_accounts,
        network_coverage,
        numbers_features,
        operator_connect,
        session_analysis,
        verified_numbers,
        access_ip_address,
        charges_breakdown,
        global_ip_latency,
        messaging_optouts,
        requirement_types,
        room_compositions,
        room_participants,
        siprec_connectors,
        sub_number_orders,
        inventory_coverage,
        messaging_profiles,
        messaging_tollfree,
        portability_checks,
        requirement_groups,
        texml_applications,
        webhook_deliveries,
        global_ip_protocols,
        integration_secrets,
        notification_events,
        number_block_orders,
        number_reservations,
        phone_number_blocks,
        wireless_blocklists,
        external_connections,
        mobile_phone_numbers,
        wireguard_interfaces,
        bulk_sim_card_actions,
        global_ip_assignments,
        messaging_url_domains,
        notification_channels,
        notification_profiles,
        notification_settings,
        porting_phone_numbers,
        telephony_credentials,
        credential_connections,
        dialogflow_connections,
        sim_card_order_preview,
        virtual_cross_connects,
        alphanumeric_sender_ids,
        available_phone_numbers,
        global_ip_allowed_ports,
        global_ip_health_checks,
        mobile_push_credentials,
        outbound_voice_profiles,
        regulatory_requirements,
        authentication_providers,
        customer_service_records,
        inexplicit_number_orders,
        messaging_hosted_numbers,
        mobile_network_operators,
        mobile_voice_connections,
        public_internet_gateways,
        recording_transcriptions,
        sub_number_orders_report,
        call_control_applications,
        messaging_profile_metrics,
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
        messaging_hosted_number_orders,
        messaging_numbers_bulk_updates,
        virtual_cross_connects_coverage,
        sim_card_data_usage_notifications,
        phone_numbers_regulatory_requirements,
    )
    from .resources.ips import IPsResource, AsyncIPsResource
    from .resources.list import ListResource, AsyncListResource
    from .resources.seti import SetiResource, AsyncSetiResource
    from .resources.ai.ai import AIResource, AsyncAIResource
    from .resources.fqdns import FqdnsResource, AsyncFqdnsResource
    from .resources.media import MediaResource, AsyncMediaResource
    from .resources.oauth import OAuthResource, AsyncOAuthResource
    from .resources.balance import BalanceResource, AsyncBalanceResource
    from .resources.regions import RegionsResource, AsyncRegionsResource
    from .resources.comments import CommentsResource, AsyncCommentsResource
    from .resources.invoices import InvoicesResource, AsyncInvoicesResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.documents import DocumentsResource, AsyncDocumentsResource
    from .resources.user_tags import UserTagsResource, AsyncUserTagsResource
    from .resources.global_ips import GlobalIPsResource, AsyncGlobalIPsResource
    from .resources.well_known import WellKnownResource, AsyncWellKnownResource
    from .resources.call_events import CallEventsResource, AsyncCallEventsResource
    from .resources.calls.calls import CallsResource, AsyncCallsResource
    from .resources.connections import ConnectionsResource, AsyncConnectionsResource
    from .resources.faxes.faxes import FaxesResource, AsyncFaxesResource
    from .resources.ota_updates import OtaUpdatesResource, AsyncOtaUpdatesResource
    from .resources.rooms.rooms import RoomsResource, AsyncRoomsResource
    from .resources.short_codes import ShortCodesResource, AsyncShortCodesResource
    from .resources.texml.texml import TexmlResource, AsyncTexmlResource
    from .resources.audit_events import AuditEventsResource, AsyncAuditEventsResource
    from .resources.oauth_grants import OAuthGrantsResource, AsyncOAuthGrantsResource
    from .resources.requirements import RequirementsResource, AsyncRequirementsResource
    from .resources.channel_zones import ChannelZonesResource, AsyncChannelZonesResource
    from .resources.legacy.legacy import LegacyResource, AsyncLegacyResource
    from .resources.number_lookup import NumberLookupResource, AsyncNumberLookupResource
    from .resources.number_orders import NumberOrdersResource, AsyncNumberOrdersResource
    from .resources.oauth_clients import OAuthClientsResource, AsyncOAuthClientsResource
    from .resources.queues.queues import QueuesResource, AsyncQueuesResource
    from .resources.usage_reports import UsageReportsResource, AsyncUsageReportsResource
    from .resources.billing_groups import BillingGroupsResource, AsyncBillingGroupsResource
    from .resources.detail_records import DetailRecordsResource, AsyncDetailRecordsResource
    from .resources.document_links import DocumentLinksResource, AsyncDocumentLinksResource
    from .resources.ip_connections import IPConnectionsResource, AsyncIPConnectionsResource
    from .resources.speech_to_text import SpeechToTextResource, AsyncSpeechToTextResource
    from .resources.text_to_speech import TextToSpeechResource, AsyncTextToSpeechResource
    from .resources.user_addresses import UserAddressesResource, AsyncUserAddressesResource
    from .resources.actions.actions import ActionsResource, AsyncActionsResource
    from .resources.advanced_orders import AdvancedOrdersResource, AsyncAdvancedOrdersResource
    from .resources.charges_summary import ChargesSummaryResource, AsyncChargesSummaryResource
    from .resources.global_ip_usage import GlobalIPUsageResource, AsyncGlobalIPUsageResource
    from .resources.payment.payment import PaymentResource, AsyncPaymentResource
    from .resources.porting.porting import PortingResource, AsyncPortingResource
    from .resources.reports.reports import ReportsResource, AsyncReportsResource
    from .resources.room_recordings import RoomRecordingsResource, AsyncRoomRecordingsResource
    from .resources.sim_card_orders import SimCardOrdersResource, AsyncSimCardOrdersResource
    from .resources.storage.storage import StorageResource, AsyncStorageResource
    from .resources.verify_profiles import VerifyProfilesResource, AsyncVerifyProfilesResource
    from .resources.wireguard_peers import WireguardPeersResource, AsyncWireguardPeersResource
    from .resources.access_ip_ranges import AccessIPRangesResource, AsyncAccessIPRangesResource
    from .resources.country_coverage import CountryCoverageResource, AsyncCountryCoverageResource
    from .resources.fax_applications import FaxApplicationsResource, AsyncFaxApplicationsResource
    from .resources.fqdn_connections import FqdnConnectionsResource, AsyncFqdnConnectionsResource
    from .resources.inbound_channels import InboundChannelsResource, AsyncInboundChannelsResource
    from .resources.network_coverage import NetworkCoverageResource, AsyncNetworkCoverageResource
    from .resources.numbers_features import NumbersFeaturesResource, AsyncNumbersFeaturesResource
    from .resources.access_ip_address import AccessIPAddressResource, AsyncAccessIPAddressResource
    from .resources.charges_breakdown import ChargesBreakdownResource, AsyncChargesBreakdownResource
    from .resources.global_ip_latency import GlobalIPLatencyResource, AsyncGlobalIPLatencyResource
    from .resources.messages.messages import MessagesResource, AsyncMessagesResource
    from .resources.messaging_optouts import MessagingOptoutsResource, AsyncMessagingOptoutsResource
    from .resources.networks.networks import NetworksResource, AsyncNetworksResource
    from .resources.portouts.portouts import PortoutsResource, AsyncPortoutsResource
    from .resources.requirement_types import RequirementTypesResource, AsyncRequirementTypesResource
    from .resources.room_compositions import RoomCompositionsResource, AsyncRoomCompositionsResource
    from .resources.room_participants import RoomParticipantsResource, AsyncRoomParticipantsResource
    from .resources.siprec_connectors import SiprecConnectorsResource, AsyncSiprecConnectorsResource
    from .resources.sub_number_orders import SubNumberOrdersResource, AsyncSubNumberOrdersResource
    from .resources.wireless.wireless import WirelessResource, AsyncWirelessResource
    from .resources.inventory_coverage import InventoryCoverageResource, AsyncInventoryCoverageResource
    from .resources.portability_checks import PortabilityChecksResource, AsyncPortabilityChecksResource
    from .resources.requirement_groups import RequirementGroupsResource, AsyncRequirementGroupsResource
    from .resources.texml_applications import TexmlApplicationsResource, AsyncTexmlApplicationsResource
    from .resources.webhook_deliveries import WebhookDeliveriesResource, AsyncWebhookDeliveriesResource
    from .resources.addresses.addresses import AddressesResource, AsyncAddressesResource
    from .resources.global_ip_protocols import GlobalIPProtocolsResource, AsyncGlobalIPProtocolsResource
    from .resources.integration_secrets import IntegrationSecretsResource, AsyncIntegrationSecretsResource
    from .resources.messaging.messaging import MessagingResource, AsyncMessagingResource
    from .resources.notification_events import NotificationEventsResource, AsyncNotificationEventsResource
    from .resources.number_block_orders import NumberBlockOrdersResource, AsyncNumberBlockOrdersResource
    from .resources.sim_cards.sim_cards import SimCardsResource, AsyncSimCardsResource
    from .resources.wireless_blocklists import WirelessBlocklistsResource, AsyncWirelessBlocklistsResource
    from .resources.wireguard_interfaces import WireguardInterfacesResource, AsyncWireguardInterfacesResource
    from .resources.bulk_sim_card_actions import BulkSimCardActionsResource, AsyncBulkSimCardActionsResource
    from .resources.global_ip_assignments import GlobalIPAssignmentsResource, AsyncGlobalIPAssignmentsResource
    from .resources.messaging_url_domains import MessagingURLDomainsResource, AsyncMessagingURLDomainsResource
    from .resources.notification_channels import NotificationChannelsResource, AsyncNotificationChannelsResource
    from .resources.notification_profiles import NotificationProfilesResource, AsyncNotificationProfilesResource
    from .resources.notification_settings import NotificationSettingsResource, AsyncNotificationSettingsResource
    from .resources.porting_phone_numbers import PortingPhoneNumbersResource, AsyncPortingPhoneNumbersResource
    from .resources.recordings.recordings import RecordingsResource, AsyncRecordingsResource
    from .resources.telephony_credentials import TelephonyCredentialsResource, AsyncTelephonyCredentialsResource
    from .resources.dialogflow_connections import DialogflowConnectionsResource, AsyncDialogflowConnectionsResource
    from .resources.sim_card_order_preview import SimCardOrderPreviewResource, AsyncSimCardOrderPreviewResource
    from .resources.virtual_cross_connects import VirtualCrossConnectsResource, AsyncVirtualCrossConnectsResource
    from .resources.alphanumeric_sender_ids import AlphanumericSenderIDsResource, AsyncAlphanumericSenderIDsResource
    from .resources.available_phone_numbers import AvailablePhoneNumbersResource, AsyncAvailablePhoneNumbersResource
    from .resources.conferences.conferences import ConferencesResource, AsyncConferencesResource
    from .resources.global_ip_allowed_ports import GlobalIPAllowedPortsResource, AsyncGlobalIPAllowedPortsResource
    from .resources.global_ip_health_checks import GlobalIPHealthChecksResource, AsyncGlobalIPHealthChecksResource
    from .resources.mobile_push_credentials import MobilePushCredentialsResource, AsyncMobilePushCredentialsResource
    from .resources.outbound_voice_profiles import OutboundVoiceProfilesResource, AsyncOutboundVoiceProfilesResource
    from .resources.regulatory_requirements import RegulatoryRequirementsResource, AsyncRegulatoryRequirementsResource
    from .resources.authentication_providers import (
        AuthenticationProvidersResource,
        AsyncAuthenticationProvidersResource,
    )
    from .resources.customer_service_records import CustomerServiceRecordsResource, AsyncCustomerServiceRecordsResource
    from .resources.inexplicit_number_orders import InexplicitNumberOrdersResource, AsyncInexplicitNumberOrdersResource
    from .resources.messaging_hosted_numbers import MessagingHostedNumbersResource, AsyncMessagingHostedNumbersResource
    from .resources.mobile_network_operators import MobileNetworkOperatorsResource, AsyncMobileNetworkOperatorsResource
    from .resources.mobile_voice_connections import MobileVoiceConnectionsResource, AsyncMobileVoiceConnectionsResource
    from .resources.public_internet_gateways import PublicInternetGatewaysResource, AsyncPublicInternetGatewaysResource
    from .resources.recording_transcriptions import (
        RecordingTranscriptionsResource,
        AsyncRecordingTranscriptionsResource,
    )
    from .resources.sub_number_orders_report import SubNumberOrdersReportResource, AsyncSubNumberOrdersReportResource
    from .resources.call_control_applications import (
        CallControlApplicationsResource,
        AsyncCallControlApplicationsResource,
    )
    from .resources.messaging_profile_metrics import (
        MessagingProfileMetricsResource,
        AsyncMessagingProfileMetricsResource,
    )
    from .resources.private_wireless_gateways import (
        PrivateWirelessGatewaysResource,
        AsyncPrivateWirelessGatewaysResource,
    )
    from .resources.wireless_blocklist_values import (
        WirelessBlocklistValuesResource,
        AsyncWirelessBlocklistValuesResource,
    )
    from .resources.custom_storage_credentials import (
        CustomStorageCredentialsResource,
        AsyncCustomStorageCredentialsResource,
    )
    from .resources.number_order_phone_numbers import (
        NumberOrderPhoneNumbersResource,
        AsyncNumberOrderPhoneNumbersResource,
    )
    from .resources.dynamic_emergency_addresses import (
        DynamicEmergencyAddressesResource,
        AsyncDynamicEmergencyAddressesResource,
    )
    from .resources.dynamic_emergency_endpoints import (
        DynamicEmergencyEndpointsResource,
        AsyncDynamicEmergencyEndpointsResource,
    )
    from .resources.global_ip_assignment_health import (
        GlobalIPAssignmentHealthResource,
        AsyncGlobalIPAssignmentHealthResource,
    )
    from .resources.global_ip_assignments_usage import (
        GlobalIPAssignmentsUsageResource,
        AsyncGlobalIPAssignmentsUsageResource,
    )
    from .resources.organizations.organizations import OrganizationsResource, AsyncOrganizationsResource
    from .resources.phone_numbers.phone_numbers import PhoneNumbersResource, AsyncPhoneNumbersResource
    from .resources.verifications.verifications import VerificationsResource, AsyncVerificationsResource
    from .resources.global_ip_health_check_types import (
        GlobalIPHealthCheckTypesResource,
        AsyncGlobalIPHealthCheckTypesResource,
    )
    from .resources.ledger_billing_group_reports import (
        LedgerBillingGroupReportsResource,
        AsyncLedgerBillingGroupReportsResource,
    )
    from .resources.available_phone_number_blocks import (
        AvailablePhoneNumberBlocksResource,
        AsyncAvailablePhoneNumberBlocksResource,
    )
    from .resources.bundle_pricing.bundle_pricing import BundlePricingResource, AsyncBundlePricingResource
    from .resources.notification_event_conditions import (
        NotificationEventConditionsResource,
        AsyncNotificationEventConditionsResource,
    )
    from .resources.porting_orders.porting_orders import PortingOrdersResource, AsyncPortingOrdersResource
    from .resources.messaging_numbers_bulk_updates import (
        MessagingNumbersBulkUpdatesResource,
        AsyncMessagingNumbersBulkUpdatesResource,
    )
    from .resources.messaging_10dlc.messaging_10dlc import Messaging10dlcResource, AsyncMessaging10dlcResource
    from .resources.sim_card_groups.sim_card_groups import SimCardGroupsResource, AsyncSimCardGroupsResource
    from .resources.virtual_cross_connects_coverage import (
        VirtualCrossConnectsCoverageResource,
        AsyncVirtualCrossConnectsCoverageResource,
    )
    from .resources.managed_accounts.managed_accounts import ManagedAccountsResource, AsyncManagedAccountsResource
    from .resources.operator_connect.operator_connect import OperatorConnectResource, AsyncOperatorConnectResource
    from .resources.session_analysis.session_analysis import SessionAnalysisResource, AsyncSessionAnalysisResource
    from .resources.sim_card_data_usage_notifications import (
        SimCardDataUsageNotificationsResource,
        AsyncSimCardDataUsageNotificationsResource,
    )
    from .resources.verified_numbers.verified_numbers import VerifiedNumbersResource, AsyncVerifiedNumbersResource
    from .resources.messaging_profiles.messaging_profiles import (
        MessagingProfilesResource,
        AsyncMessagingProfilesResource,
    )
    from .resources.messaging_tollfree.messaging_tollfree import (
        MessagingTollfreeResource,
        AsyncMessagingTollfreeResource,
    )
    from .resources.phone_numbers_regulatory_requirements import (
        PhoneNumbersRegulatoryRequirementsResource,
        AsyncPhoneNumbersRegulatoryRequirementsResource,
    )
    from .resources.number_reservations.number_reservations import (
        NumberReservationsResource,
        AsyncNumberReservationsResource,
    )
    from .resources.phone_number_blocks.phone_number_blocks import (
        PhoneNumberBlocksResource,
        AsyncPhoneNumberBlocksResource,
    )
    from .resources.external_connections.external_connections import (
        ExternalConnectionsResource,
        AsyncExternalConnectionsResource,
    )
    from .resources.mobile_phone_numbers.mobile_phone_numbers import (
        MobilePhoneNumbersResource,
        AsyncMobilePhoneNumbersResource,
    )
    from .resources.credential_connections.credential_connections import (
        CredentialConnectionsResource,
        AsyncCredentialConnectionsResource,
    )
    from .resources.messaging_hosted_number_orders.messaging_hosted_number_orders import (
        MessagingHostedNumberOrdersResource,
        AsyncMessagingHostedNumberOrdersResource,
    )

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Telnyx", "AsyncTelnyx", "Client", "AsyncClient"]


class Telnyx(SyncAPIClient):
    # client options
    api_key: str | None
    public_key: str | None
    client_id: str | None
    client_secret: str | None

    websocket_base_url: str | httpx.URL | None
    """Base URL for WebSocket connections.

    If not specified, the default base URL will be used, with 'wss://' replacing the
    'http://' or 'https://' scheme. For example: 'http://example.com' becomes
    'wss://example.com'
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        public_key: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        websocket_base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `TELNYX_API_KEY`
        - `public_key` from `TELNYX_PUBLIC_KEY`
        - `client_id` from `TELNYX_CLIENT_ID`
        - `client_secret` from `TELNYX_CLIENT_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("TELNYX_API_KEY")
        self.api_key = api_key

        if public_key is None:
            public_key = os.environ.get("TELNYX_PUBLIC_KEY")
        self.public_key = public_key

        if client_id is None:
            client_id = os.environ.get("TELNYX_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("TELNYX_CLIENT_SECRET")
        self.client_secret = client_secret

        self.websocket_base_url = websocket_base_url

        if base_url is None:
            base_url = os.environ.get("TELNYX_BASE_URL")
        self._base_url_overridden = base_url is not None
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

    @cached_property
    def legacy(self) -> LegacyResource:
        from .resources.legacy import LegacyResource

        return LegacyResource(self)

    @cached_property
    def oauth(self) -> OAuthResource:
        from .resources.oauth import OAuthResource

        return OAuthResource(self)

    @cached_property
    def oauth_clients(self) -> OAuthClientsResource:
        from .resources.oauth_clients import OAuthClientsResource

        return OAuthClientsResource(self)

    @cached_property
    def oauth_grants(self) -> OAuthGrantsResource:
        from .resources.oauth_grants import OAuthGrantsResource

        return OAuthGrantsResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def access_ip_address(self) -> AccessIPAddressResource:
        """IP Address Operations"""
        from .resources.access_ip_address import AccessIPAddressResource

        return AccessIPAddressResource(self)

    @cached_property
    def access_ip_ranges(self) -> AccessIPRangesResource:
        """IP Range Operations"""
        from .resources.access_ip_ranges import AccessIPRangesResource

        return AccessIPRangesResource(self)

    @cached_property
    def actions(self) -> ActionsResource:
        from .resources.actions import ActionsResource

        return ActionsResource(self)

    @cached_property
    def addresses(self) -> AddressesResource:
        """Operations to work with Address records.

        Address records are emergency-validated addresses meant to be associated with phone numbers. They are validated for emergency usage purposes at creation time, although you may validate them separately with a custom workflow using the ValidateAddress operation separately. Address records are not usable for physical orders, such as for Telnyx SIM cards, please use UserAddress for that. It is not possible to entirely skip emergency service validation for Address records; if an emergency provider for a phone number rejects the address then it cannot be used on a phone number. To prevent records from getting out of sync, Address records are immutable and cannot be altered once created. If you realize you need to alter an address, a new record must be created with the differing address.
        """
        from .resources.addresses import AddressesResource

        return AddressesResource(self)

    @cached_property
    def advanced_orders(self) -> AdvancedOrdersResource:
        from .resources.advanced_orders import AdvancedOrdersResource

        return AdvancedOrdersResource(self)

    @cached_property
    def ai(self) -> AIResource:
        """Generate text with LLMs"""
        from .resources.ai import AIResource

        return AIResource(self)

    @cached_property
    def audit_events(self) -> AuditEventsResource:
        """Audit log operations."""
        from .resources.audit_events import AuditEventsResource

        return AuditEventsResource(self)

    @cached_property
    def authentication_providers(self) -> AuthenticationProvidersResource:
        from .resources.authentication_providers import AuthenticationProvidersResource

        return AuthenticationProvidersResource(self)

    @cached_property
    def available_phone_number_blocks(self) -> AvailablePhoneNumberBlocksResource:
        """Number search"""
        from .resources.available_phone_number_blocks import AvailablePhoneNumberBlocksResource

        return AvailablePhoneNumberBlocksResource(self)

    @cached_property
    def available_phone_numbers(self) -> AvailablePhoneNumbersResource:
        """Number search"""
        from .resources.available_phone_numbers import AvailablePhoneNumbersResource

        return AvailablePhoneNumbersResource(self)

    @cached_property
    def balance(self) -> BalanceResource:
        """Billing operations"""
        from .resources.balance import BalanceResource

        return BalanceResource(self)

    @cached_property
    def billing_groups(self) -> BillingGroupsResource:
        """Billing groups operations"""
        from .resources.billing_groups import BillingGroupsResource

        return BillingGroupsResource(self)

    @cached_property
    def bulk_sim_card_actions(self) -> BulkSimCardActionsResource:
        """
        View SIM card actions, their progress and timestamps using the SIM Card Actions API
        """
        from .resources.bulk_sim_card_actions import BulkSimCardActionsResource

        return BulkSimCardActionsResource(self)

    @cached_property
    def bundle_pricing(self) -> BundlePricingResource:
        from .resources.bundle_pricing import BundlePricingResource

        return BundlePricingResource(self)

    @cached_property
    def call_control_applications(self) -> CallControlApplicationsResource:
        """Call Control applications operations"""
        from .resources.call_control_applications import CallControlApplicationsResource

        return CallControlApplicationsResource(self)

    @cached_property
    def call_events(self) -> CallEventsResource:
        """Call Control debugging"""
        from .resources.call_events import CallEventsResource

        return CallEventsResource(self)

    @cached_property
    def calls(self) -> CallsResource:
        from .resources.calls import CallsResource

        return CallsResource(self)

    @cached_property
    def channel_zones(self) -> ChannelZonesResource:
        """Voice Channels"""
        from .resources.channel_zones import ChannelZonesResource

        return ChannelZonesResource(self)

    @cached_property
    def charges_breakdown(self) -> ChargesBreakdownResource:
        from .resources.charges_breakdown import ChargesBreakdownResource

        return ChargesBreakdownResource(self)

    @cached_property
    def charges_summary(self) -> ChargesSummaryResource:
        from .resources.charges_summary import ChargesSummaryResource

        return ChargesSummaryResource(self)

    @cached_property
    def comments(self) -> CommentsResource:
        """Number orders"""
        from .resources.comments import CommentsResource

        return CommentsResource(self)

    @cached_property
    def conferences(self) -> ConferencesResource:
        """Conference command operations"""
        from .resources.conferences import ConferencesResource

        return ConferencesResource(self)

    @cached_property
    def connections(self) -> ConnectionsResource:
        from .resources.connections import ConnectionsResource

        return ConnectionsResource(self)

    @cached_property
    def country_coverage(self) -> CountryCoverageResource:
        """Country Coverage"""
        from .resources.country_coverage import CountryCoverageResource

        return CountryCoverageResource(self)

    @cached_property
    def credential_connections(self) -> CredentialConnectionsResource:
        """Credential connection operations"""
        from .resources.credential_connections import CredentialConnectionsResource

        return CredentialConnectionsResource(self)

    @cached_property
    def custom_storage_credentials(self) -> CustomStorageCredentialsResource:
        """Call Recordings operations."""
        from .resources.custom_storage_credentials import CustomStorageCredentialsResource

        return CustomStorageCredentialsResource(self)

    @cached_property
    def customer_service_records(self) -> CustomerServiceRecordsResource:
        """Customer Service Record operations"""
        from .resources.customer_service_records import CustomerServiceRecordsResource

        return CustomerServiceRecordsResource(self)

    @cached_property
    def detail_records(self) -> DetailRecordsResource:
        """Detail Records operations"""
        from .resources.detail_records import DetailRecordsResource

        return DetailRecordsResource(self)

    @cached_property
    def dialogflow_connections(self) -> DialogflowConnectionsResource:
        """Dialogflow Connection Operations."""
        from .resources.dialogflow_connections import DialogflowConnectionsResource

        return DialogflowConnectionsResource(self)

    @cached_property
    def document_links(self) -> DocumentLinksResource:
        """Documents"""
        from .resources.document_links import DocumentLinksResource

        return DocumentLinksResource(self)

    @cached_property
    def documents(self) -> DocumentsResource:
        """Documents"""
        from .resources.documents import DocumentsResource

        return DocumentsResource(self)

    @cached_property
    def dynamic_emergency_addresses(self) -> DynamicEmergencyAddressesResource:
        """Dynamic emergency address operations"""
        from .resources.dynamic_emergency_addresses import DynamicEmergencyAddressesResource

        return DynamicEmergencyAddressesResource(self)

    @cached_property
    def dynamic_emergency_endpoints(self) -> DynamicEmergencyEndpointsResource:
        """Dynamic Emergency Endpoints"""
        from .resources.dynamic_emergency_endpoints import DynamicEmergencyEndpointsResource

        return DynamicEmergencyEndpointsResource(self)

    @cached_property
    def external_connections(self) -> ExternalConnectionsResource:
        """External Connections operations"""
        from .resources.external_connections import ExternalConnectionsResource

        return ExternalConnectionsResource(self)

    @cached_property
    def fax_applications(self) -> FaxApplicationsResource:
        """Fax Applications operations"""
        from .resources.fax_applications import FaxApplicationsResource

        return FaxApplicationsResource(self)

    @cached_property
    def faxes(self) -> FaxesResource:
        """Programmable fax command operations"""
        from .resources.faxes import FaxesResource

        return FaxesResource(self)

    @cached_property
    def fqdn_connections(self) -> FqdnConnectionsResource:
        """FQDN connection operations"""
        from .resources.fqdn_connections import FqdnConnectionsResource

        return FqdnConnectionsResource(self)

    @cached_property
    def fqdns(self) -> FqdnsResource:
        """FQDN operations"""
        from .resources.fqdns import FqdnsResource

        return FqdnsResource(self)

    @cached_property
    def global_ip_allowed_ports(self) -> GlobalIPAllowedPortsResource:
        """Global IPs"""
        from .resources.global_ip_allowed_ports import GlobalIPAllowedPortsResource

        return GlobalIPAllowedPortsResource(self)

    @cached_property
    def global_ip_assignment_health(self) -> GlobalIPAssignmentHealthResource:
        """Global IPs"""
        from .resources.global_ip_assignment_health import GlobalIPAssignmentHealthResource

        return GlobalIPAssignmentHealthResource(self)

    @cached_property
    def global_ip_assignments(self) -> GlobalIPAssignmentsResource:
        """Global IPs"""
        from .resources.global_ip_assignments import GlobalIPAssignmentsResource

        return GlobalIPAssignmentsResource(self)

    @cached_property
    def global_ip_assignments_usage(self) -> GlobalIPAssignmentsUsageResource:
        """Global IPs"""
        from .resources.global_ip_assignments_usage import GlobalIPAssignmentsUsageResource

        return GlobalIPAssignmentsUsageResource(self)

    @cached_property
    def global_ip_health_check_types(self) -> GlobalIPHealthCheckTypesResource:
        """Global IPs"""
        from .resources.global_ip_health_check_types import GlobalIPHealthCheckTypesResource

        return GlobalIPHealthCheckTypesResource(self)

    @cached_property
    def global_ip_health_checks(self) -> GlobalIPHealthChecksResource:
        """Global IPs"""
        from .resources.global_ip_health_checks import GlobalIPHealthChecksResource

        return GlobalIPHealthChecksResource(self)

    @cached_property
    def global_ip_latency(self) -> GlobalIPLatencyResource:
        """Global IPs"""
        from .resources.global_ip_latency import GlobalIPLatencyResource

        return GlobalIPLatencyResource(self)

    @cached_property
    def global_ip_protocols(self) -> GlobalIPProtocolsResource:
        """Global IPs"""
        from .resources.global_ip_protocols import GlobalIPProtocolsResource

        return GlobalIPProtocolsResource(self)

    @cached_property
    def global_ip_usage(self) -> GlobalIPUsageResource:
        """Global IPs"""
        from .resources.global_ip_usage import GlobalIPUsageResource

        return GlobalIPUsageResource(self)

    @cached_property
    def global_ips(self) -> GlobalIPsResource:
        """Global IPs"""
        from .resources.global_ips import GlobalIPsResource

        return GlobalIPsResource(self)

    @cached_property
    def inbound_channels(self) -> InboundChannelsResource:
        """Voice Channels"""
        from .resources.inbound_channels import InboundChannelsResource

        return InboundChannelsResource(self)

    @cached_property
    def integration_secrets(self) -> IntegrationSecretsResource:
        """Store and retrieve integration secrets"""
        from .resources.integration_secrets import IntegrationSecretsResource

        return IntegrationSecretsResource(self)

    @cached_property
    def inventory_coverage(self) -> InventoryCoverageResource:
        """Inventory Level"""
        from .resources.inventory_coverage import InventoryCoverageResource

        return InventoryCoverageResource(self)

    @cached_property
    def invoices(self) -> InvoicesResource:
        from .resources.invoices import InvoicesResource

        return InvoicesResource(self)

    @cached_property
    def ip_connections(self) -> IPConnectionsResource:
        """IP connection operations"""
        from .resources.ip_connections import IPConnectionsResource

        return IPConnectionsResource(self)

    @cached_property
    def ips(self) -> IPsResource:
        """IP operations"""
        from .resources.ips import IPsResource

        return IPsResource(self)

    @cached_property
    def ledger_billing_group_reports(self) -> LedgerBillingGroupReportsResource:
        """Ledger billing reports"""
        from .resources.ledger_billing_group_reports import LedgerBillingGroupReportsResource

        return LedgerBillingGroupReportsResource(self)

    @cached_property
    def list(self) -> ListResource:
        """Voice Channels"""
        from .resources.list import ListResource

        return ListResource(self)

    @cached_property
    def managed_accounts(self) -> ManagedAccountsResource:
        """Managed Accounts operations"""
        from .resources.managed_accounts import ManagedAccountsResource

        return ManagedAccountsResource(self)

    @cached_property
    def media(self) -> MediaResource:
        """Media Storage operations"""
        from .resources.media import MediaResource

        return MediaResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def messaging(self) -> MessagingResource:
        from .resources.messaging import MessagingResource

        return MessagingResource(self)

    @cached_property
    def messaging_hosted_number_orders(self) -> MessagingHostedNumberOrdersResource:
        """Manage your messaging hosted numbers"""
        from .resources.messaging_hosted_number_orders import MessagingHostedNumberOrdersResource

        return MessagingHostedNumberOrdersResource(self)

    @cached_property
    def messaging_hosted_numbers(self) -> MessagingHostedNumbersResource:
        from .resources.messaging_hosted_numbers import MessagingHostedNumbersResource

        return MessagingHostedNumbersResource(self)

    @cached_property
    def messaging_numbers_bulk_updates(self) -> MessagingNumbersBulkUpdatesResource:
        """Configure your phone numbers"""
        from .resources.messaging_numbers_bulk_updates import MessagingNumbersBulkUpdatesResource

        return MessagingNumbersBulkUpdatesResource(self)

    @cached_property
    def messaging_optouts(self) -> MessagingOptoutsResource:
        """Opt-Out Management"""
        from .resources.messaging_optouts import MessagingOptoutsResource

        return MessagingOptoutsResource(self)

    @cached_property
    def messaging_profiles(self) -> MessagingProfilesResource:
        from .resources.messaging_profiles import MessagingProfilesResource

        return MessagingProfilesResource(self)

    @cached_property
    def messaging_tollfree(self) -> MessagingTollfreeResource:
        from .resources.messaging_tollfree import MessagingTollfreeResource

        return MessagingTollfreeResource(self)

    @cached_property
    def messaging_url_domains(self) -> MessagingURLDomainsResource:
        """Messaging URL Domains"""
        from .resources.messaging_url_domains import MessagingURLDomainsResource

        return MessagingURLDomainsResource(self)

    @cached_property
    def mobile_network_operators(self) -> MobileNetworkOperatorsResource:
        """Mobile network operators operations"""
        from .resources.mobile_network_operators import MobileNetworkOperatorsResource

        return MobileNetworkOperatorsResource(self)

    @cached_property
    def mobile_push_credentials(self) -> MobilePushCredentialsResource:
        """Mobile push credential management"""
        from .resources.mobile_push_credentials import MobilePushCredentialsResource

        return MobilePushCredentialsResource(self)

    @cached_property
    def network_coverage(self) -> NetworkCoverageResource:
        from .resources.network_coverage import NetworkCoverageResource

        return NetworkCoverageResource(self)

    @cached_property
    def networks(self) -> NetworksResource:
        """Network operations"""
        from .resources.networks import NetworksResource

        return NetworksResource(self)

    @cached_property
    def notification_channels(self) -> NotificationChannelsResource:
        """Notification settings operations"""
        from .resources.notification_channels import NotificationChannelsResource

        return NotificationChannelsResource(self)

    @cached_property
    def notification_event_conditions(self) -> NotificationEventConditionsResource:
        """Notification settings operations"""
        from .resources.notification_event_conditions import NotificationEventConditionsResource

        return NotificationEventConditionsResource(self)

    @cached_property
    def notification_events(self) -> NotificationEventsResource:
        """Notification settings operations"""
        from .resources.notification_events import NotificationEventsResource

        return NotificationEventsResource(self)

    @cached_property
    def notification_profiles(self) -> NotificationProfilesResource:
        """Notification settings operations"""
        from .resources.notification_profiles import NotificationProfilesResource

        return NotificationProfilesResource(self)

    @cached_property
    def notification_settings(self) -> NotificationSettingsResource:
        """Notification settings operations"""
        from .resources.notification_settings import NotificationSettingsResource

        return NotificationSettingsResource(self)

    @cached_property
    def number_block_orders(self) -> NumberBlockOrdersResource:
        from .resources.number_block_orders import NumberBlockOrdersResource

        return NumberBlockOrdersResource(self)

    @cached_property
    def number_lookup(self) -> NumberLookupResource:
        """Look up phone number data"""
        from .resources.number_lookup import NumberLookupResource

        return NumberLookupResource(self)

    @cached_property
    def number_order_phone_numbers(self) -> NumberOrderPhoneNumbersResource:
        from .resources.number_order_phone_numbers import NumberOrderPhoneNumbersResource

        return NumberOrderPhoneNumbersResource(self)

    @cached_property
    def number_orders(self) -> NumberOrdersResource:
        """Number orders"""
        from .resources.number_orders import NumberOrdersResource

        return NumberOrdersResource(self)

    @cached_property
    def number_reservations(self) -> NumberReservationsResource:
        """Number reservations"""
        from .resources.number_reservations import NumberReservationsResource

        return NumberReservationsResource(self)

    @cached_property
    def numbers_features(self) -> NumbersFeaturesResource:
        from .resources.numbers_features import NumbersFeaturesResource

        return NumbersFeaturesResource(self)

    @cached_property
    def operator_connect(self) -> OperatorConnectResource:
        from .resources.operator_connect import OperatorConnectResource

        return OperatorConnectResource(self)

    @cached_property
    def ota_updates(self) -> OtaUpdatesResource:
        """OTA updates operations"""
        from .resources.ota_updates import OtaUpdatesResource

        return OtaUpdatesResource(self)

    @cached_property
    def outbound_voice_profiles(self) -> OutboundVoiceProfilesResource:
        """Outbound voice profiles operations"""
        from .resources.outbound_voice_profiles import OutboundVoiceProfilesResource

        return OutboundVoiceProfilesResource(self)

    @cached_property
    def payment(self) -> PaymentResource:
        """Operations for managing stored payment transactions."""
        from .resources.payment import PaymentResource

        return PaymentResource(self)

    @cached_property
    def phone_number_blocks(self) -> PhoneNumberBlocksResource:
        from .resources.phone_number_blocks import PhoneNumberBlocksResource

        return PhoneNumberBlocksResource(self)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        """Configure your phone numbers"""
        from .resources.phone_numbers import PhoneNumbersResource

        return PhoneNumbersResource(self)

    @cached_property
    def phone_numbers_regulatory_requirements(self) -> PhoneNumbersRegulatoryRequirementsResource:
        """Regulatory Requirements"""
        from .resources.phone_numbers_regulatory_requirements import PhoneNumbersRegulatoryRequirementsResource

        return PhoneNumbersRegulatoryRequirementsResource(self)

    @cached_property
    def portability_checks(self) -> PortabilityChecksResource:
        """Determining portability of phone numbers"""
        from .resources.portability_checks import PortabilityChecksResource

        return PortabilityChecksResource(self)

    @cached_property
    def porting(self) -> PortingResource:
        """Endpoints related to porting orders management."""
        from .resources.porting import PortingResource

        return PortingResource(self)

    @cached_property
    def porting_orders(self) -> PortingOrdersResource:
        """Endpoints related to porting orders management."""
        from .resources.porting_orders import PortingOrdersResource

        return PortingOrdersResource(self)

    @cached_property
    def porting_phone_numbers(self) -> PortingPhoneNumbersResource:
        """Endpoints related to porting orders management."""
        from .resources.porting_phone_numbers import PortingPhoneNumbersResource

        return PortingPhoneNumbersResource(self)

    @cached_property
    def portouts(self) -> PortoutsResource:
        """Number portout operations"""
        from .resources.portouts import PortoutsResource

        return PortoutsResource(self)

    @cached_property
    def private_wireless_gateways(self) -> PrivateWirelessGatewaysResource:
        """Private Wireless Gateways operations"""
        from .resources.private_wireless_gateways import PrivateWirelessGatewaysResource

        return PrivateWirelessGatewaysResource(self)

    @cached_property
    def public_internet_gateways(self) -> PublicInternetGatewaysResource:
        """Public Internet Gateway operations"""
        from .resources.public_internet_gateways import PublicInternetGatewaysResource

        return PublicInternetGatewaysResource(self)

    @cached_property
    def queues(self) -> QueuesResource:
        """Queue commands operations"""
        from .resources.queues import QueuesResource

        return QueuesResource(self)

    @cached_property
    def recording_transcriptions(self) -> RecordingTranscriptionsResource:
        """Call Recordings operations."""
        from .resources.recording_transcriptions import RecordingTranscriptionsResource

        return RecordingTranscriptionsResource(self)

    @cached_property
    def recordings(self) -> RecordingsResource:
        """Call Recordings operations."""
        from .resources.recordings import RecordingsResource

        return RecordingsResource(self)

    @cached_property
    def regions(self) -> RegionsResource:
        """Regions"""
        from .resources.regions import RegionsResource

        return RegionsResource(self)

    @cached_property
    def regulatory_requirements(self) -> RegulatoryRequirementsResource:
        """Regulatory Requirements"""
        from .resources.regulatory_requirements import RegulatoryRequirementsResource

        return RegulatoryRequirementsResource(self)

    @cached_property
    def reports(self) -> ReportsResource:
        from .resources.reports import ReportsResource

        return ReportsResource(self)

    @cached_property
    def requirement_groups(self) -> RequirementGroupsResource:
        """Requirement Groups"""
        from .resources.requirement_groups import RequirementGroupsResource

        return RequirementGroupsResource(self)

    @cached_property
    def requirement_types(self) -> RequirementTypesResource:
        """Types of requirements for international numbers and porting orders"""
        from .resources.requirement_types import RequirementTypesResource

        return RequirementTypesResource(self)

    @cached_property
    def requirements(self) -> RequirementsResource:
        """Requirements for international numbers and porting orders"""
        from .resources.requirements import RequirementsResource

        return RequirementsResource(self)

    @cached_property
    def room_compositions(self) -> RoomCompositionsResource:
        """Rooms Compositions operations."""
        from .resources.room_compositions import RoomCompositionsResource

        return RoomCompositionsResource(self)

    @cached_property
    def room_participants(self) -> RoomParticipantsResource:
        """Rooms Participants operations."""
        from .resources.room_participants import RoomParticipantsResource

        return RoomParticipantsResource(self)

    @cached_property
    def room_recordings(self) -> RoomRecordingsResource:
        """Rooms Recordings operations."""
        from .resources.room_recordings import RoomRecordingsResource

        return RoomRecordingsResource(self)

    @cached_property
    def rooms(self) -> RoomsResource:
        """Rooms operations."""
        from .resources.rooms import RoomsResource

        return RoomsResource(self)

    @cached_property
    def seti(self) -> SetiResource:
        """Observability into Telnyx platform stability and performance."""
        from .resources.seti import SetiResource

        return SetiResource(self)

    @cached_property
    def short_codes(self) -> ShortCodesResource:
        """Short codes"""
        from .resources.short_codes import ShortCodesResource

        return ShortCodesResource(self)

    @cached_property
    def sim_card_data_usage_notifications(self) -> SimCardDataUsageNotificationsResource:
        """SIM Cards operations"""
        from .resources.sim_card_data_usage_notifications import SimCardDataUsageNotificationsResource

        return SimCardDataUsageNotificationsResource(self)

    @cached_property
    def sim_card_groups(self) -> SimCardGroupsResource:
        """SIM Card Groups operations"""
        from .resources.sim_card_groups import SimCardGroupsResource

        return SimCardGroupsResource(self)

    @cached_property
    def sim_card_order_preview(self) -> SimCardOrderPreviewResource:
        """SIM Card Orders operations"""
        from .resources.sim_card_order_preview import SimCardOrderPreviewResource

        return SimCardOrderPreviewResource(self)

    @cached_property
    def sim_card_orders(self) -> SimCardOrdersResource:
        """SIM Card Orders operations"""
        from .resources.sim_card_orders import SimCardOrdersResource

        return SimCardOrdersResource(self)

    @cached_property
    def sim_cards(self) -> SimCardsResource:
        """SIM Cards operations"""
        from .resources.sim_cards import SimCardsResource

        return SimCardsResource(self)

    @cached_property
    def siprec_connectors(self) -> SiprecConnectorsResource:
        """SIPREC connectors configuration."""
        from .resources.siprec_connectors import SiprecConnectorsResource

        return SiprecConnectorsResource(self)

    @cached_property
    def storage(self) -> StorageResource:
        """Migrate data from an external provider into Telnyx Cloud Storage"""
        from .resources.storage import StorageResource

        return StorageResource(self)

    @cached_property
    def sub_number_orders(self) -> SubNumberOrdersResource:
        from .resources.sub_number_orders import SubNumberOrdersResource

        return SubNumberOrdersResource(self)

    @cached_property
    def sub_number_orders_report(self) -> SubNumberOrdersReportResource:
        """Number orders"""
        from .resources.sub_number_orders_report import SubNumberOrdersReportResource

        return SubNumberOrdersReportResource(self)

    @cached_property
    def telephony_credentials(self) -> TelephonyCredentialsResource:
        from .resources.telephony_credentials import TelephonyCredentialsResource

        return TelephonyCredentialsResource(self)

    @cached_property
    def texml(self) -> TexmlResource:
        """TeXML REST Commands"""
        from .resources.texml import TexmlResource

        return TexmlResource(self)

    @cached_property
    def texml_applications(self) -> TexmlApplicationsResource:
        """TeXML Applications operations"""
        from .resources.texml_applications import TexmlApplicationsResource

        return TexmlApplicationsResource(self)

    @cached_property
    def text_to_speech(self) -> TextToSpeechResource:
        """Text to speech streaming command operations"""
        from .resources.text_to_speech import TextToSpeechResource

        return TextToSpeechResource(self)

    @cached_property
    def speech_to_text(self) -> SpeechToTextResource:
        """Speech to text streaming command operations via WebSocket"""
        from .resources.speech_to_text import SpeechToTextResource

        return SpeechToTextResource(self)

    @cached_property
    def usage_reports(self) -> UsageReportsResource:
        """Usage data reporting across Telnyx products"""
        from .resources.usage_reports import UsageReportsResource

        return UsageReportsResource(self)

    @cached_property
    def user_addresses(self) -> UserAddressesResource:
        """Operations for working with UserAddress records.

        UserAddress records are stored addresses that users can use for non-emergency-calling purposes, such as for shipping addresses for orders of wireless SIMs (or other physical items). They cannot be used for emergency calling and are distinct from Address records, which are used on phone numbers.
        """
        from .resources.user_addresses import UserAddressesResource

        return UserAddressesResource(self)

    @cached_property
    def user_tags(self) -> UserTagsResource:
        """User-defined tags for Telnyx resources"""
        from .resources.user_tags import UserTagsResource

        return UserTagsResource(self)

    @cached_property
    def verifications(self) -> VerificationsResource:
        """Two factor authentication API"""
        from .resources.verifications import VerificationsResource

        return VerificationsResource(self)

    @cached_property
    def verified_numbers(self) -> VerifiedNumbersResource:
        """Verified Numbers operations"""
        from .resources.verified_numbers import VerifiedNumbersResource

        return VerifiedNumbersResource(self)

    @cached_property
    def verify_profiles(self) -> VerifyProfilesResource:
        """Two factor authentication API"""
        from .resources.verify_profiles import VerifyProfilesResource

        return VerifyProfilesResource(self)

    @cached_property
    def virtual_cross_connects(self) -> VirtualCrossConnectsResource:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects import VirtualCrossConnectsResource

        return VirtualCrossConnectsResource(self)

    @cached_property
    def virtual_cross_connects_coverage(self) -> VirtualCrossConnectsCoverageResource:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects_coverage import VirtualCrossConnectsCoverageResource

        return VirtualCrossConnectsCoverageResource(self)

    @cached_property
    def webhook_deliveries(self) -> WebhookDeliveriesResource:
        """Webhooks operations"""
        from .resources.webhook_deliveries import WebhookDeliveriesResource

        return WebhookDeliveriesResource(self)

    @cached_property
    def wireguard_interfaces(self) -> WireguardInterfacesResource:
        """WireGuard Interface operations"""
        from .resources.wireguard_interfaces import WireguardInterfacesResource

        return WireguardInterfacesResource(self)

    @cached_property
    def wireguard_peers(self) -> WireguardPeersResource:
        """WireGuard Interface operations"""
        from .resources.wireguard_peers import WireguardPeersResource

        return WireguardPeersResource(self)

    @cached_property
    def wireless(self) -> WirelessResource:
        """Regions for wireless services"""
        from .resources.wireless import WirelessResource

        return WirelessResource(self)

    @cached_property
    def wireless_blocklist_values(self) -> WirelessBlocklistValuesResource:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklist_values import WirelessBlocklistValuesResource

        return WirelessBlocklistValuesResource(self)

    @cached_property
    def wireless_blocklists(self) -> WirelessBlocklistsResource:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklists import WirelessBlocklistsResource

        return WirelessBlocklistsResource(self)

    @cached_property
    def well_known(self) -> WellKnownResource:
        from .resources.well_known import WellKnownResource

        return WellKnownResource(self)

    @cached_property
    def inexplicit_number_orders(self) -> InexplicitNumberOrdersResource:
        """Inexplicit number orders for bulk purchasing without specifying exact numbers"""
        from .resources.inexplicit_number_orders import InexplicitNumberOrdersResource

        return InexplicitNumberOrdersResource(self)

    @cached_property
    def mobile_phone_numbers(self) -> MobilePhoneNumbersResource:
        """Mobile phone number operations"""
        from .resources.mobile_phone_numbers import MobilePhoneNumbersResource

        return MobilePhoneNumbersResource(self)

    @cached_property
    def mobile_voice_connections(self) -> MobileVoiceConnectionsResource:
        """Mobile voice connection operations"""
        from .resources.mobile_voice_connections import MobileVoiceConnectionsResource

        return MobileVoiceConnectionsResource(self)

    @cached_property
    def messaging_10dlc(self) -> Messaging10dlcResource:
        from .resources.messaging_10dlc import Messaging10dlcResource

        return Messaging10dlcResource(self)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        from .resources.organizations import OrganizationsResource

        return OrganizationsResource(self)

    @cached_property
    def alphanumeric_sender_ids(self) -> AlphanumericSenderIDsResource:
        from .resources.alphanumeric_sender_ids import AlphanumericSenderIDsResource

        return AlphanumericSenderIDsResource(self)

    @cached_property
    def messaging_profile_metrics(self) -> MessagingProfileMetricsResource:
        from .resources.messaging_profile_metrics import MessagingProfileMetricsResource

        return MessagingProfileMetricsResource(self)

    @cached_property
    def session_analysis(self) -> SessionAnalysisResource:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        from .resources.session_analysis import SessionAnalysisResource

        return SessionAnalysisResource(self)

    @cached_property
    def with_raw_response(self) -> TelnyxWithRawResponse:
        return TelnyxWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelnyxWithStreamedResponse:
        return TelnyxWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def custom_auth(self) -> httpx.Auth | None:
        if self.client_id and self.client_secret:
            return make_oauth2(
                client_id=self.client_id,
                client_secret=self.client_secret,
                token_url=self._prepare_url("https://api.telnyx.com/v2/oauth/token"),
                header="Authorization",
            )
        return None

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _should_retry(self, response: httpx.Response) -> bool:
        # Retry on 401 if we are using OAuth2 and the token might be expired
        if response.status_code == 401 and isinstance(self.custom_auth, OAuth2ClientCredentials):
            if self.custom_auth.token_is_expired():
                self.custom_auth.invalidate_token()
                return True
        return super()._should_retry(response)

    def copy(
        self,
        *,
        api_key: str | None = None,
        public_key: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        websocket_base_url: str | httpx.URL | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
        client = self.__class__(
            api_key=api_key or self.api_key,
            public_key=public_key or self.public_key,
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            websocket_base_url=websocket_base_url or self.websocket_base_url,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

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
    # client options
    api_key: str | None
    public_key: str | None
    client_id: str | None
    client_secret: str | None

    websocket_base_url: str | httpx.URL | None
    """Base URL for WebSocket connections.

    If not specified, the default base URL will be used, with 'wss://' replacing the
    'http://' or 'https://' scheme. For example: 'http://example.com' becomes
    'wss://example.com'
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        public_key: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        websocket_base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `TELNYX_API_KEY`
        - `public_key` from `TELNYX_PUBLIC_KEY`
        - `client_id` from `TELNYX_CLIENT_ID`
        - `client_secret` from `TELNYX_CLIENT_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("TELNYX_API_KEY")
        self.api_key = api_key

        if public_key is None:
            public_key = os.environ.get("TELNYX_PUBLIC_KEY")
        self.public_key = public_key

        if client_id is None:
            client_id = os.environ.get("TELNYX_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("TELNYX_CLIENT_SECRET")
        self.client_secret = client_secret

        self.websocket_base_url = websocket_base_url

        if base_url is None:
            base_url = os.environ.get("TELNYX_BASE_URL")
        self._base_url_overridden = base_url is not None
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

    @cached_property
    def legacy(self) -> AsyncLegacyResource:
        from .resources.legacy import AsyncLegacyResource

        return AsyncLegacyResource(self)

    @cached_property
    def oauth(self) -> AsyncOAuthResource:
        from .resources.oauth import AsyncOAuthResource

        return AsyncOAuthResource(self)

    @cached_property
    def oauth_clients(self) -> AsyncOAuthClientsResource:
        from .resources.oauth_clients import AsyncOAuthClientsResource

        return AsyncOAuthClientsResource(self)

    @cached_property
    def oauth_grants(self) -> AsyncOAuthGrantsResource:
        from .resources.oauth_grants import AsyncOAuthGrantsResource

        return AsyncOAuthGrantsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def access_ip_address(self) -> AsyncAccessIPAddressResource:
        """IP Address Operations"""
        from .resources.access_ip_address import AsyncAccessIPAddressResource

        return AsyncAccessIPAddressResource(self)

    @cached_property
    def access_ip_ranges(self) -> AsyncAccessIPRangesResource:
        """IP Range Operations"""
        from .resources.access_ip_ranges import AsyncAccessIPRangesResource

        return AsyncAccessIPRangesResource(self)

    @cached_property
    def actions(self) -> AsyncActionsResource:
        from .resources.actions import AsyncActionsResource

        return AsyncActionsResource(self)

    @cached_property
    def addresses(self) -> AsyncAddressesResource:
        """Operations to work with Address records.

        Address records are emergency-validated addresses meant to be associated with phone numbers. They are validated for emergency usage purposes at creation time, although you may validate them separately with a custom workflow using the ValidateAddress operation separately. Address records are not usable for physical orders, such as for Telnyx SIM cards, please use UserAddress for that. It is not possible to entirely skip emergency service validation for Address records; if an emergency provider for a phone number rejects the address then it cannot be used on a phone number. To prevent records from getting out of sync, Address records are immutable and cannot be altered once created. If you realize you need to alter an address, a new record must be created with the differing address.
        """
        from .resources.addresses import AsyncAddressesResource

        return AsyncAddressesResource(self)

    @cached_property
    def advanced_orders(self) -> AsyncAdvancedOrdersResource:
        from .resources.advanced_orders import AsyncAdvancedOrdersResource

        return AsyncAdvancedOrdersResource(self)

    @cached_property
    def ai(self) -> AsyncAIResource:
        """Generate text with LLMs"""
        from .resources.ai import AsyncAIResource

        return AsyncAIResource(self)

    @cached_property
    def audit_events(self) -> AsyncAuditEventsResource:
        """Audit log operations."""
        from .resources.audit_events import AsyncAuditEventsResource

        return AsyncAuditEventsResource(self)

    @cached_property
    def authentication_providers(self) -> AsyncAuthenticationProvidersResource:
        from .resources.authentication_providers import AsyncAuthenticationProvidersResource

        return AsyncAuthenticationProvidersResource(self)

    @cached_property
    def available_phone_number_blocks(self) -> AsyncAvailablePhoneNumberBlocksResource:
        """Number search"""
        from .resources.available_phone_number_blocks import AsyncAvailablePhoneNumberBlocksResource

        return AsyncAvailablePhoneNumberBlocksResource(self)

    @cached_property
    def available_phone_numbers(self) -> AsyncAvailablePhoneNumbersResource:
        """Number search"""
        from .resources.available_phone_numbers import AsyncAvailablePhoneNumbersResource

        return AsyncAvailablePhoneNumbersResource(self)

    @cached_property
    def balance(self) -> AsyncBalanceResource:
        """Billing operations"""
        from .resources.balance import AsyncBalanceResource

        return AsyncBalanceResource(self)

    @cached_property
    def billing_groups(self) -> AsyncBillingGroupsResource:
        """Billing groups operations"""
        from .resources.billing_groups import AsyncBillingGroupsResource

        return AsyncBillingGroupsResource(self)

    @cached_property
    def bulk_sim_card_actions(self) -> AsyncBulkSimCardActionsResource:
        """
        View SIM card actions, their progress and timestamps using the SIM Card Actions API
        """
        from .resources.bulk_sim_card_actions import AsyncBulkSimCardActionsResource

        return AsyncBulkSimCardActionsResource(self)

    @cached_property
    def bundle_pricing(self) -> AsyncBundlePricingResource:
        from .resources.bundle_pricing import AsyncBundlePricingResource

        return AsyncBundlePricingResource(self)

    @cached_property
    def call_control_applications(self) -> AsyncCallControlApplicationsResource:
        """Call Control applications operations"""
        from .resources.call_control_applications import AsyncCallControlApplicationsResource

        return AsyncCallControlApplicationsResource(self)

    @cached_property
    def call_events(self) -> AsyncCallEventsResource:
        """Call Control debugging"""
        from .resources.call_events import AsyncCallEventsResource

        return AsyncCallEventsResource(self)

    @cached_property
    def calls(self) -> AsyncCallsResource:
        from .resources.calls import AsyncCallsResource

        return AsyncCallsResource(self)

    @cached_property
    def channel_zones(self) -> AsyncChannelZonesResource:
        """Voice Channels"""
        from .resources.channel_zones import AsyncChannelZonesResource

        return AsyncChannelZonesResource(self)

    @cached_property
    def charges_breakdown(self) -> AsyncChargesBreakdownResource:
        from .resources.charges_breakdown import AsyncChargesBreakdownResource

        return AsyncChargesBreakdownResource(self)

    @cached_property
    def charges_summary(self) -> AsyncChargesSummaryResource:
        from .resources.charges_summary import AsyncChargesSummaryResource

        return AsyncChargesSummaryResource(self)

    @cached_property
    def comments(self) -> AsyncCommentsResource:
        """Number orders"""
        from .resources.comments import AsyncCommentsResource

        return AsyncCommentsResource(self)

    @cached_property
    def conferences(self) -> AsyncConferencesResource:
        """Conference command operations"""
        from .resources.conferences import AsyncConferencesResource

        return AsyncConferencesResource(self)

    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        from .resources.connections import AsyncConnectionsResource

        return AsyncConnectionsResource(self)

    @cached_property
    def country_coverage(self) -> AsyncCountryCoverageResource:
        """Country Coverage"""
        from .resources.country_coverage import AsyncCountryCoverageResource

        return AsyncCountryCoverageResource(self)

    @cached_property
    def credential_connections(self) -> AsyncCredentialConnectionsResource:
        """Credential connection operations"""
        from .resources.credential_connections import AsyncCredentialConnectionsResource

        return AsyncCredentialConnectionsResource(self)

    @cached_property
    def custom_storage_credentials(self) -> AsyncCustomStorageCredentialsResource:
        """Call Recordings operations."""
        from .resources.custom_storage_credentials import AsyncCustomStorageCredentialsResource

        return AsyncCustomStorageCredentialsResource(self)

    @cached_property
    def customer_service_records(self) -> AsyncCustomerServiceRecordsResource:
        """Customer Service Record operations"""
        from .resources.customer_service_records import AsyncCustomerServiceRecordsResource

        return AsyncCustomerServiceRecordsResource(self)

    @cached_property
    def detail_records(self) -> AsyncDetailRecordsResource:
        """Detail Records operations"""
        from .resources.detail_records import AsyncDetailRecordsResource

        return AsyncDetailRecordsResource(self)

    @cached_property
    def dialogflow_connections(self) -> AsyncDialogflowConnectionsResource:
        """Dialogflow Connection Operations."""
        from .resources.dialogflow_connections import AsyncDialogflowConnectionsResource

        return AsyncDialogflowConnectionsResource(self)

    @cached_property
    def document_links(self) -> AsyncDocumentLinksResource:
        """Documents"""
        from .resources.document_links import AsyncDocumentLinksResource

        return AsyncDocumentLinksResource(self)

    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        """Documents"""
        from .resources.documents import AsyncDocumentsResource

        return AsyncDocumentsResource(self)

    @cached_property
    def dynamic_emergency_addresses(self) -> AsyncDynamicEmergencyAddressesResource:
        """Dynamic emergency address operations"""
        from .resources.dynamic_emergency_addresses import AsyncDynamicEmergencyAddressesResource

        return AsyncDynamicEmergencyAddressesResource(self)

    @cached_property
    def dynamic_emergency_endpoints(self) -> AsyncDynamicEmergencyEndpointsResource:
        """Dynamic Emergency Endpoints"""
        from .resources.dynamic_emergency_endpoints import AsyncDynamicEmergencyEndpointsResource

        return AsyncDynamicEmergencyEndpointsResource(self)

    @cached_property
    def external_connections(self) -> AsyncExternalConnectionsResource:
        """External Connections operations"""
        from .resources.external_connections import AsyncExternalConnectionsResource

        return AsyncExternalConnectionsResource(self)

    @cached_property
    def fax_applications(self) -> AsyncFaxApplicationsResource:
        """Fax Applications operations"""
        from .resources.fax_applications import AsyncFaxApplicationsResource

        return AsyncFaxApplicationsResource(self)

    @cached_property
    def faxes(self) -> AsyncFaxesResource:
        """Programmable fax command operations"""
        from .resources.faxes import AsyncFaxesResource

        return AsyncFaxesResource(self)

    @cached_property
    def fqdn_connections(self) -> AsyncFqdnConnectionsResource:
        """FQDN connection operations"""
        from .resources.fqdn_connections import AsyncFqdnConnectionsResource

        return AsyncFqdnConnectionsResource(self)

    @cached_property
    def fqdns(self) -> AsyncFqdnsResource:
        """FQDN operations"""
        from .resources.fqdns import AsyncFqdnsResource

        return AsyncFqdnsResource(self)

    @cached_property
    def global_ip_allowed_ports(self) -> AsyncGlobalIPAllowedPortsResource:
        """Global IPs"""
        from .resources.global_ip_allowed_ports import AsyncGlobalIPAllowedPortsResource

        return AsyncGlobalIPAllowedPortsResource(self)

    @cached_property
    def global_ip_assignment_health(self) -> AsyncGlobalIPAssignmentHealthResource:
        """Global IPs"""
        from .resources.global_ip_assignment_health import AsyncGlobalIPAssignmentHealthResource

        return AsyncGlobalIPAssignmentHealthResource(self)

    @cached_property
    def global_ip_assignments(self) -> AsyncGlobalIPAssignmentsResource:
        """Global IPs"""
        from .resources.global_ip_assignments import AsyncGlobalIPAssignmentsResource

        return AsyncGlobalIPAssignmentsResource(self)

    @cached_property
    def global_ip_assignments_usage(self) -> AsyncGlobalIPAssignmentsUsageResource:
        """Global IPs"""
        from .resources.global_ip_assignments_usage import AsyncGlobalIPAssignmentsUsageResource

        return AsyncGlobalIPAssignmentsUsageResource(self)

    @cached_property
    def global_ip_health_check_types(self) -> AsyncGlobalIPHealthCheckTypesResource:
        """Global IPs"""
        from .resources.global_ip_health_check_types import AsyncGlobalIPHealthCheckTypesResource

        return AsyncGlobalIPHealthCheckTypesResource(self)

    @cached_property
    def global_ip_health_checks(self) -> AsyncGlobalIPHealthChecksResource:
        """Global IPs"""
        from .resources.global_ip_health_checks import AsyncGlobalIPHealthChecksResource

        return AsyncGlobalIPHealthChecksResource(self)

    @cached_property
    def global_ip_latency(self) -> AsyncGlobalIPLatencyResource:
        """Global IPs"""
        from .resources.global_ip_latency import AsyncGlobalIPLatencyResource

        return AsyncGlobalIPLatencyResource(self)

    @cached_property
    def global_ip_protocols(self) -> AsyncGlobalIPProtocolsResource:
        """Global IPs"""
        from .resources.global_ip_protocols import AsyncGlobalIPProtocolsResource

        return AsyncGlobalIPProtocolsResource(self)

    @cached_property
    def global_ip_usage(self) -> AsyncGlobalIPUsageResource:
        """Global IPs"""
        from .resources.global_ip_usage import AsyncGlobalIPUsageResource

        return AsyncGlobalIPUsageResource(self)

    @cached_property
    def global_ips(self) -> AsyncGlobalIPsResource:
        """Global IPs"""
        from .resources.global_ips import AsyncGlobalIPsResource

        return AsyncGlobalIPsResource(self)

    @cached_property
    def inbound_channels(self) -> AsyncInboundChannelsResource:
        """Voice Channels"""
        from .resources.inbound_channels import AsyncInboundChannelsResource

        return AsyncInboundChannelsResource(self)

    @cached_property
    def integration_secrets(self) -> AsyncIntegrationSecretsResource:
        """Store and retrieve integration secrets"""
        from .resources.integration_secrets import AsyncIntegrationSecretsResource

        return AsyncIntegrationSecretsResource(self)

    @cached_property
    def inventory_coverage(self) -> AsyncInventoryCoverageResource:
        """Inventory Level"""
        from .resources.inventory_coverage import AsyncInventoryCoverageResource

        return AsyncInventoryCoverageResource(self)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        from .resources.invoices import AsyncInvoicesResource

        return AsyncInvoicesResource(self)

    @cached_property
    def ip_connections(self) -> AsyncIPConnectionsResource:
        """IP connection operations"""
        from .resources.ip_connections import AsyncIPConnectionsResource

        return AsyncIPConnectionsResource(self)

    @cached_property
    def ips(self) -> AsyncIPsResource:
        """IP operations"""
        from .resources.ips import AsyncIPsResource

        return AsyncIPsResource(self)

    @cached_property
    def ledger_billing_group_reports(self) -> AsyncLedgerBillingGroupReportsResource:
        """Ledger billing reports"""
        from .resources.ledger_billing_group_reports import AsyncLedgerBillingGroupReportsResource

        return AsyncLedgerBillingGroupReportsResource(self)

    @cached_property
    def list(self) -> AsyncListResource:
        """Voice Channels"""
        from .resources.list import AsyncListResource

        return AsyncListResource(self)

    @cached_property
    def managed_accounts(self) -> AsyncManagedAccountsResource:
        """Managed Accounts operations"""
        from .resources.managed_accounts import AsyncManagedAccountsResource

        return AsyncManagedAccountsResource(self)

    @cached_property
    def media(self) -> AsyncMediaResource:
        """Media Storage operations"""
        from .resources.media import AsyncMediaResource

        return AsyncMediaResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def messaging(self) -> AsyncMessagingResource:
        from .resources.messaging import AsyncMessagingResource

        return AsyncMessagingResource(self)

    @cached_property
    def messaging_hosted_number_orders(self) -> AsyncMessagingHostedNumberOrdersResource:
        """Manage your messaging hosted numbers"""
        from .resources.messaging_hosted_number_orders import AsyncMessagingHostedNumberOrdersResource

        return AsyncMessagingHostedNumberOrdersResource(self)

    @cached_property
    def messaging_hosted_numbers(self) -> AsyncMessagingHostedNumbersResource:
        from .resources.messaging_hosted_numbers import AsyncMessagingHostedNumbersResource

        return AsyncMessagingHostedNumbersResource(self)

    @cached_property
    def messaging_numbers_bulk_updates(self) -> AsyncMessagingNumbersBulkUpdatesResource:
        """Configure your phone numbers"""
        from .resources.messaging_numbers_bulk_updates import AsyncMessagingNumbersBulkUpdatesResource

        return AsyncMessagingNumbersBulkUpdatesResource(self)

    @cached_property
    def messaging_optouts(self) -> AsyncMessagingOptoutsResource:
        """Opt-Out Management"""
        from .resources.messaging_optouts import AsyncMessagingOptoutsResource

        return AsyncMessagingOptoutsResource(self)

    @cached_property
    def messaging_profiles(self) -> AsyncMessagingProfilesResource:
        from .resources.messaging_profiles import AsyncMessagingProfilesResource

        return AsyncMessagingProfilesResource(self)

    @cached_property
    def messaging_tollfree(self) -> AsyncMessagingTollfreeResource:
        from .resources.messaging_tollfree import AsyncMessagingTollfreeResource

        return AsyncMessagingTollfreeResource(self)

    @cached_property
    def messaging_url_domains(self) -> AsyncMessagingURLDomainsResource:
        """Messaging URL Domains"""
        from .resources.messaging_url_domains import AsyncMessagingURLDomainsResource

        return AsyncMessagingURLDomainsResource(self)

    @cached_property
    def mobile_network_operators(self) -> AsyncMobileNetworkOperatorsResource:
        """Mobile network operators operations"""
        from .resources.mobile_network_operators import AsyncMobileNetworkOperatorsResource

        return AsyncMobileNetworkOperatorsResource(self)

    @cached_property
    def mobile_push_credentials(self) -> AsyncMobilePushCredentialsResource:
        """Mobile push credential management"""
        from .resources.mobile_push_credentials import AsyncMobilePushCredentialsResource

        return AsyncMobilePushCredentialsResource(self)

    @cached_property
    def network_coverage(self) -> AsyncNetworkCoverageResource:
        from .resources.network_coverage import AsyncNetworkCoverageResource

        return AsyncNetworkCoverageResource(self)

    @cached_property
    def networks(self) -> AsyncNetworksResource:
        """Network operations"""
        from .resources.networks import AsyncNetworksResource

        return AsyncNetworksResource(self)

    @cached_property
    def notification_channels(self) -> AsyncNotificationChannelsResource:
        """Notification settings operations"""
        from .resources.notification_channels import AsyncNotificationChannelsResource

        return AsyncNotificationChannelsResource(self)

    @cached_property
    def notification_event_conditions(self) -> AsyncNotificationEventConditionsResource:
        """Notification settings operations"""
        from .resources.notification_event_conditions import AsyncNotificationEventConditionsResource

        return AsyncNotificationEventConditionsResource(self)

    @cached_property
    def notification_events(self) -> AsyncNotificationEventsResource:
        """Notification settings operations"""
        from .resources.notification_events import AsyncNotificationEventsResource

        return AsyncNotificationEventsResource(self)

    @cached_property
    def notification_profiles(self) -> AsyncNotificationProfilesResource:
        """Notification settings operations"""
        from .resources.notification_profiles import AsyncNotificationProfilesResource

        return AsyncNotificationProfilesResource(self)

    @cached_property
    def notification_settings(self) -> AsyncNotificationSettingsResource:
        """Notification settings operations"""
        from .resources.notification_settings import AsyncNotificationSettingsResource

        return AsyncNotificationSettingsResource(self)

    @cached_property
    def number_block_orders(self) -> AsyncNumberBlockOrdersResource:
        from .resources.number_block_orders import AsyncNumberBlockOrdersResource

        return AsyncNumberBlockOrdersResource(self)

    @cached_property
    def number_lookup(self) -> AsyncNumberLookupResource:
        """Look up phone number data"""
        from .resources.number_lookup import AsyncNumberLookupResource

        return AsyncNumberLookupResource(self)

    @cached_property
    def number_order_phone_numbers(self) -> AsyncNumberOrderPhoneNumbersResource:
        from .resources.number_order_phone_numbers import AsyncNumberOrderPhoneNumbersResource

        return AsyncNumberOrderPhoneNumbersResource(self)

    @cached_property
    def number_orders(self) -> AsyncNumberOrdersResource:
        """Number orders"""
        from .resources.number_orders import AsyncNumberOrdersResource

        return AsyncNumberOrdersResource(self)

    @cached_property
    def number_reservations(self) -> AsyncNumberReservationsResource:
        """Number reservations"""
        from .resources.number_reservations import AsyncNumberReservationsResource

        return AsyncNumberReservationsResource(self)

    @cached_property
    def numbers_features(self) -> AsyncNumbersFeaturesResource:
        from .resources.numbers_features import AsyncNumbersFeaturesResource

        return AsyncNumbersFeaturesResource(self)

    @cached_property
    def operator_connect(self) -> AsyncOperatorConnectResource:
        from .resources.operator_connect import AsyncOperatorConnectResource

        return AsyncOperatorConnectResource(self)

    @cached_property
    def ota_updates(self) -> AsyncOtaUpdatesResource:
        """OTA updates operations"""
        from .resources.ota_updates import AsyncOtaUpdatesResource

        return AsyncOtaUpdatesResource(self)

    @cached_property
    def outbound_voice_profiles(self) -> AsyncOutboundVoiceProfilesResource:
        """Outbound voice profiles operations"""
        from .resources.outbound_voice_profiles import AsyncOutboundVoiceProfilesResource

        return AsyncOutboundVoiceProfilesResource(self)

    @cached_property
    def payment(self) -> AsyncPaymentResource:
        """Operations for managing stored payment transactions."""
        from .resources.payment import AsyncPaymentResource

        return AsyncPaymentResource(self)

    @cached_property
    def phone_number_blocks(self) -> AsyncPhoneNumberBlocksResource:
        from .resources.phone_number_blocks import AsyncPhoneNumberBlocksResource

        return AsyncPhoneNumberBlocksResource(self)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        """Configure your phone numbers"""
        from .resources.phone_numbers import AsyncPhoneNumbersResource

        return AsyncPhoneNumbersResource(self)

    @cached_property
    def phone_numbers_regulatory_requirements(self) -> AsyncPhoneNumbersRegulatoryRequirementsResource:
        """Regulatory Requirements"""
        from .resources.phone_numbers_regulatory_requirements import AsyncPhoneNumbersRegulatoryRequirementsResource

        return AsyncPhoneNumbersRegulatoryRequirementsResource(self)

    @cached_property
    def portability_checks(self) -> AsyncPortabilityChecksResource:
        """Determining portability of phone numbers"""
        from .resources.portability_checks import AsyncPortabilityChecksResource

        return AsyncPortabilityChecksResource(self)

    @cached_property
    def porting(self) -> AsyncPortingResource:
        """Endpoints related to porting orders management."""
        from .resources.porting import AsyncPortingResource

        return AsyncPortingResource(self)

    @cached_property
    def porting_orders(self) -> AsyncPortingOrdersResource:
        """Endpoints related to porting orders management."""
        from .resources.porting_orders import AsyncPortingOrdersResource

        return AsyncPortingOrdersResource(self)

    @cached_property
    def porting_phone_numbers(self) -> AsyncPortingPhoneNumbersResource:
        """Endpoints related to porting orders management."""
        from .resources.porting_phone_numbers import AsyncPortingPhoneNumbersResource

        return AsyncPortingPhoneNumbersResource(self)

    @cached_property
    def portouts(self) -> AsyncPortoutsResource:
        """Number portout operations"""
        from .resources.portouts import AsyncPortoutsResource

        return AsyncPortoutsResource(self)

    @cached_property
    def private_wireless_gateways(self) -> AsyncPrivateWirelessGatewaysResource:
        """Private Wireless Gateways operations"""
        from .resources.private_wireless_gateways import AsyncPrivateWirelessGatewaysResource

        return AsyncPrivateWirelessGatewaysResource(self)

    @cached_property
    def public_internet_gateways(self) -> AsyncPublicInternetGatewaysResource:
        """Public Internet Gateway operations"""
        from .resources.public_internet_gateways import AsyncPublicInternetGatewaysResource

        return AsyncPublicInternetGatewaysResource(self)

    @cached_property
    def queues(self) -> AsyncQueuesResource:
        """Queue commands operations"""
        from .resources.queues import AsyncQueuesResource

        return AsyncQueuesResource(self)

    @cached_property
    def recording_transcriptions(self) -> AsyncRecordingTranscriptionsResource:
        """Call Recordings operations."""
        from .resources.recording_transcriptions import AsyncRecordingTranscriptionsResource

        return AsyncRecordingTranscriptionsResource(self)

    @cached_property
    def recordings(self) -> AsyncRecordingsResource:
        """Call Recordings operations."""
        from .resources.recordings import AsyncRecordingsResource

        return AsyncRecordingsResource(self)

    @cached_property
    def regions(self) -> AsyncRegionsResource:
        """Regions"""
        from .resources.regions import AsyncRegionsResource

        return AsyncRegionsResource(self)

    @cached_property
    def regulatory_requirements(self) -> AsyncRegulatoryRequirementsResource:
        """Regulatory Requirements"""
        from .resources.regulatory_requirements import AsyncRegulatoryRequirementsResource

        return AsyncRegulatoryRequirementsResource(self)

    @cached_property
    def reports(self) -> AsyncReportsResource:
        from .resources.reports import AsyncReportsResource

        return AsyncReportsResource(self)

    @cached_property
    def requirement_groups(self) -> AsyncRequirementGroupsResource:
        """Requirement Groups"""
        from .resources.requirement_groups import AsyncRequirementGroupsResource

        return AsyncRequirementGroupsResource(self)

    @cached_property
    def requirement_types(self) -> AsyncRequirementTypesResource:
        """Types of requirements for international numbers and porting orders"""
        from .resources.requirement_types import AsyncRequirementTypesResource

        return AsyncRequirementTypesResource(self)

    @cached_property
    def requirements(self) -> AsyncRequirementsResource:
        """Requirements for international numbers and porting orders"""
        from .resources.requirements import AsyncRequirementsResource

        return AsyncRequirementsResource(self)

    @cached_property
    def room_compositions(self) -> AsyncRoomCompositionsResource:
        """Rooms Compositions operations."""
        from .resources.room_compositions import AsyncRoomCompositionsResource

        return AsyncRoomCompositionsResource(self)

    @cached_property
    def room_participants(self) -> AsyncRoomParticipantsResource:
        """Rooms Participants operations."""
        from .resources.room_participants import AsyncRoomParticipantsResource

        return AsyncRoomParticipantsResource(self)

    @cached_property
    def room_recordings(self) -> AsyncRoomRecordingsResource:
        """Rooms Recordings operations."""
        from .resources.room_recordings import AsyncRoomRecordingsResource

        return AsyncRoomRecordingsResource(self)

    @cached_property
    def rooms(self) -> AsyncRoomsResource:
        """Rooms operations."""
        from .resources.rooms import AsyncRoomsResource

        return AsyncRoomsResource(self)

    @cached_property
    def seti(self) -> AsyncSetiResource:
        """Observability into Telnyx platform stability and performance."""
        from .resources.seti import AsyncSetiResource

        return AsyncSetiResource(self)

    @cached_property
    def short_codes(self) -> AsyncShortCodesResource:
        """Short codes"""
        from .resources.short_codes import AsyncShortCodesResource

        return AsyncShortCodesResource(self)

    @cached_property
    def sim_card_data_usage_notifications(self) -> AsyncSimCardDataUsageNotificationsResource:
        """SIM Cards operations"""
        from .resources.sim_card_data_usage_notifications import AsyncSimCardDataUsageNotificationsResource

        return AsyncSimCardDataUsageNotificationsResource(self)

    @cached_property
    def sim_card_groups(self) -> AsyncSimCardGroupsResource:
        """SIM Card Groups operations"""
        from .resources.sim_card_groups import AsyncSimCardGroupsResource

        return AsyncSimCardGroupsResource(self)

    @cached_property
    def sim_card_order_preview(self) -> AsyncSimCardOrderPreviewResource:
        """SIM Card Orders operations"""
        from .resources.sim_card_order_preview import AsyncSimCardOrderPreviewResource

        return AsyncSimCardOrderPreviewResource(self)

    @cached_property
    def sim_card_orders(self) -> AsyncSimCardOrdersResource:
        """SIM Card Orders operations"""
        from .resources.sim_card_orders import AsyncSimCardOrdersResource

        return AsyncSimCardOrdersResource(self)

    @cached_property
    def sim_cards(self) -> AsyncSimCardsResource:
        """SIM Cards operations"""
        from .resources.sim_cards import AsyncSimCardsResource

        return AsyncSimCardsResource(self)

    @cached_property
    def siprec_connectors(self) -> AsyncSiprecConnectorsResource:
        """SIPREC connectors configuration."""
        from .resources.siprec_connectors import AsyncSiprecConnectorsResource

        return AsyncSiprecConnectorsResource(self)

    @cached_property
    def storage(self) -> AsyncStorageResource:
        """Migrate data from an external provider into Telnyx Cloud Storage"""
        from .resources.storage import AsyncStorageResource

        return AsyncStorageResource(self)

    @cached_property
    def sub_number_orders(self) -> AsyncSubNumberOrdersResource:
        from .resources.sub_number_orders import AsyncSubNumberOrdersResource

        return AsyncSubNumberOrdersResource(self)

    @cached_property
    def sub_number_orders_report(self) -> AsyncSubNumberOrdersReportResource:
        """Number orders"""
        from .resources.sub_number_orders_report import AsyncSubNumberOrdersReportResource

        return AsyncSubNumberOrdersReportResource(self)

    @cached_property
    def telephony_credentials(self) -> AsyncTelephonyCredentialsResource:
        from .resources.telephony_credentials import AsyncTelephonyCredentialsResource

        return AsyncTelephonyCredentialsResource(self)

    @cached_property
    def texml(self) -> AsyncTexmlResource:
        """TeXML REST Commands"""
        from .resources.texml import AsyncTexmlResource

        return AsyncTexmlResource(self)

    @cached_property
    def texml_applications(self) -> AsyncTexmlApplicationsResource:
        """TeXML Applications operations"""
        from .resources.texml_applications import AsyncTexmlApplicationsResource

        return AsyncTexmlApplicationsResource(self)

    @cached_property
    def text_to_speech(self) -> AsyncTextToSpeechResource:
        """Text to speech streaming command operations"""
        from .resources.text_to_speech import AsyncTextToSpeechResource

        return AsyncTextToSpeechResource(self)

    @cached_property
    def speech_to_text(self) -> AsyncSpeechToTextResource:
        """Speech to text streaming command operations via WebSocket"""
        from .resources.speech_to_text import AsyncSpeechToTextResource

        return AsyncSpeechToTextResource(self)

    @cached_property
    def usage_reports(self) -> AsyncUsageReportsResource:
        """Usage data reporting across Telnyx products"""
        from .resources.usage_reports import AsyncUsageReportsResource

        return AsyncUsageReportsResource(self)

    @cached_property
    def user_addresses(self) -> AsyncUserAddressesResource:
        """Operations for working with UserAddress records.

        UserAddress records are stored addresses that users can use for non-emergency-calling purposes, such as for shipping addresses for orders of wireless SIMs (or other physical items). They cannot be used for emergency calling and are distinct from Address records, which are used on phone numbers.
        """
        from .resources.user_addresses import AsyncUserAddressesResource

        return AsyncUserAddressesResource(self)

    @cached_property
    def user_tags(self) -> AsyncUserTagsResource:
        """User-defined tags for Telnyx resources"""
        from .resources.user_tags import AsyncUserTagsResource

        return AsyncUserTagsResource(self)

    @cached_property
    def verifications(self) -> AsyncVerificationsResource:
        """Two factor authentication API"""
        from .resources.verifications import AsyncVerificationsResource

        return AsyncVerificationsResource(self)

    @cached_property
    def verified_numbers(self) -> AsyncVerifiedNumbersResource:
        """Verified Numbers operations"""
        from .resources.verified_numbers import AsyncVerifiedNumbersResource

        return AsyncVerifiedNumbersResource(self)

    @cached_property
    def verify_profiles(self) -> AsyncVerifyProfilesResource:
        """Two factor authentication API"""
        from .resources.verify_profiles import AsyncVerifyProfilesResource

        return AsyncVerifyProfilesResource(self)

    @cached_property
    def virtual_cross_connects(self) -> AsyncVirtualCrossConnectsResource:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects import AsyncVirtualCrossConnectsResource

        return AsyncVirtualCrossConnectsResource(self)

    @cached_property
    def virtual_cross_connects_coverage(self) -> AsyncVirtualCrossConnectsCoverageResource:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects_coverage import AsyncVirtualCrossConnectsCoverageResource

        return AsyncVirtualCrossConnectsCoverageResource(self)

    @cached_property
    def webhook_deliveries(self) -> AsyncWebhookDeliveriesResource:
        """Webhooks operations"""
        from .resources.webhook_deliveries import AsyncWebhookDeliveriesResource

        return AsyncWebhookDeliveriesResource(self)

    @cached_property
    def wireguard_interfaces(self) -> AsyncWireguardInterfacesResource:
        """WireGuard Interface operations"""
        from .resources.wireguard_interfaces import AsyncWireguardInterfacesResource

        return AsyncWireguardInterfacesResource(self)

    @cached_property
    def wireguard_peers(self) -> AsyncWireguardPeersResource:
        """WireGuard Interface operations"""
        from .resources.wireguard_peers import AsyncWireguardPeersResource

        return AsyncWireguardPeersResource(self)

    @cached_property
    def wireless(self) -> AsyncWirelessResource:
        """Regions for wireless services"""
        from .resources.wireless import AsyncWirelessResource

        return AsyncWirelessResource(self)

    @cached_property
    def wireless_blocklist_values(self) -> AsyncWirelessBlocklistValuesResource:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklist_values import AsyncWirelessBlocklistValuesResource

        return AsyncWirelessBlocklistValuesResource(self)

    @cached_property
    def wireless_blocklists(self) -> AsyncWirelessBlocklistsResource:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklists import AsyncWirelessBlocklistsResource

        return AsyncWirelessBlocklistsResource(self)

    @cached_property
    def well_known(self) -> AsyncWellKnownResource:
        from .resources.well_known import AsyncWellKnownResource

        return AsyncWellKnownResource(self)

    @cached_property
    def inexplicit_number_orders(self) -> AsyncInexplicitNumberOrdersResource:
        """Inexplicit number orders for bulk purchasing without specifying exact numbers"""
        from .resources.inexplicit_number_orders import AsyncInexplicitNumberOrdersResource

        return AsyncInexplicitNumberOrdersResource(self)

    @cached_property
    def mobile_phone_numbers(self) -> AsyncMobilePhoneNumbersResource:
        """Mobile phone number operations"""
        from .resources.mobile_phone_numbers import AsyncMobilePhoneNumbersResource

        return AsyncMobilePhoneNumbersResource(self)

    @cached_property
    def mobile_voice_connections(self) -> AsyncMobileVoiceConnectionsResource:
        """Mobile voice connection operations"""
        from .resources.mobile_voice_connections import AsyncMobileVoiceConnectionsResource

        return AsyncMobileVoiceConnectionsResource(self)

    @cached_property
    def messaging_10dlc(self) -> AsyncMessaging10dlcResource:
        from .resources.messaging_10dlc import AsyncMessaging10dlcResource

        return AsyncMessaging10dlcResource(self)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        from .resources.organizations import AsyncOrganizationsResource

        return AsyncOrganizationsResource(self)

    @cached_property
    def alphanumeric_sender_ids(self) -> AsyncAlphanumericSenderIDsResource:
        from .resources.alphanumeric_sender_ids import AsyncAlphanumericSenderIDsResource

        return AsyncAlphanumericSenderIDsResource(self)

    @cached_property
    def messaging_profile_metrics(self) -> AsyncMessagingProfileMetricsResource:
        from .resources.messaging_profile_metrics import AsyncMessagingProfileMetricsResource

        return AsyncMessagingProfileMetricsResource(self)

    @cached_property
    def session_analysis(self) -> AsyncSessionAnalysisResource:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        from .resources.session_analysis import AsyncSessionAnalysisResource

        return AsyncSessionAnalysisResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncTelnyxWithRawResponse:
        return AsyncTelnyxWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelnyxWithStreamedResponse:
        return AsyncTelnyxWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def custom_auth(self) -> httpx.Auth | None:
        if self.client_id and self.client_secret:
            return make_oauth2(
                client_id=self.client_id,
                client_secret=self.client_secret,
                token_url=self._prepare_url("https://api.telnyx.com/v2/oauth/token"),
                header="Authorization",
            )
        return None

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _should_retry(self, response: httpx.Response) -> bool:
        # Retry on 401 if we are using OAuth2 and the token might be expired
        if response.status_code == 401 and isinstance(self.custom_auth, OAuth2ClientCredentials):
            if self.custom_auth.token_is_expired():
                self.custom_auth.invalidate_token()
                return True
        return super()._should_retry(response)

    def copy(
        self,
        *,
        api_key: str | None = None,
        public_key: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        websocket_base_url: str | httpx.URL | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
        client = self.__class__(
            api_key=api_key or self.api_key,
            public_key=public_key or self.public_key,
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            websocket_base_url=websocket_base_url or self.websocket_base_url,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

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
    _client: Telnyx

    def __init__(self, client: Telnyx) -> None:
        self._client = client

    @cached_property
    def legacy(self) -> legacy.LegacyResourceWithRawResponse:
        from .resources.legacy import LegacyResourceWithRawResponse

        return LegacyResourceWithRawResponse(self._client.legacy)

    @cached_property
    def oauth(self) -> oauth.OAuthResourceWithRawResponse:
        from .resources.oauth import OAuthResourceWithRawResponse

        return OAuthResourceWithRawResponse(self._client.oauth)

    @cached_property
    def oauth_clients(self) -> oauth_clients.OAuthClientsResourceWithRawResponse:
        from .resources.oauth_clients import OAuthClientsResourceWithRawResponse

        return OAuthClientsResourceWithRawResponse(self._client.oauth_clients)

    @cached_property
    def oauth_grants(self) -> oauth_grants.OAuthGrantsResourceWithRawResponse:
        from .resources.oauth_grants import OAuthGrantsResourceWithRawResponse

        return OAuthGrantsResourceWithRawResponse(self._client.oauth_grants)

    @cached_property
    def access_ip_address(self) -> access_ip_address.AccessIPAddressResourceWithRawResponse:
        """IP Address Operations"""
        from .resources.access_ip_address import AccessIPAddressResourceWithRawResponse

        return AccessIPAddressResourceWithRawResponse(self._client.access_ip_address)

    @cached_property
    def access_ip_ranges(self) -> access_ip_ranges.AccessIPRangesResourceWithRawResponse:
        """IP Range Operations"""
        from .resources.access_ip_ranges import AccessIPRangesResourceWithRawResponse

        return AccessIPRangesResourceWithRawResponse(self._client.access_ip_ranges)

    @cached_property
    def actions(self) -> actions.ActionsResourceWithRawResponse:
        from .resources.actions import ActionsResourceWithRawResponse

        return ActionsResourceWithRawResponse(self._client.actions)

    @cached_property
    def addresses(self) -> addresses.AddressesResourceWithRawResponse:
        """Operations to work with Address records.

        Address records are emergency-validated addresses meant to be associated with phone numbers. They are validated for emergency usage purposes at creation time, although you may validate them separately with a custom workflow using the ValidateAddress operation separately. Address records are not usable for physical orders, such as for Telnyx SIM cards, please use UserAddress for that. It is not possible to entirely skip emergency service validation for Address records; if an emergency provider for a phone number rejects the address then it cannot be used on a phone number. To prevent records from getting out of sync, Address records are immutable and cannot be altered once created. If you realize you need to alter an address, a new record must be created with the differing address.
        """
        from .resources.addresses import AddressesResourceWithRawResponse

        return AddressesResourceWithRawResponse(self._client.addresses)

    @cached_property
    def advanced_orders(self) -> advanced_orders.AdvancedOrdersResourceWithRawResponse:
        from .resources.advanced_orders import AdvancedOrdersResourceWithRawResponse

        return AdvancedOrdersResourceWithRawResponse(self._client.advanced_orders)

    @cached_property
    def ai(self) -> ai.AIResourceWithRawResponse:
        """Generate text with LLMs"""
        from .resources.ai import AIResourceWithRawResponse

        return AIResourceWithRawResponse(self._client.ai)

    @cached_property
    def audit_events(self) -> audit_events.AuditEventsResourceWithRawResponse:
        """Audit log operations."""
        from .resources.audit_events import AuditEventsResourceWithRawResponse

        return AuditEventsResourceWithRawResponse(self._client.audit_events)

    @cached_property
    def authentication_providers(self) -> authentication_providers.AuthenticationProvidersResourceWithRawResponse:
        from .resources.authentication_providers import AuthenticationProvidersResourceWithRawResponse

        return AuthenticationProvidersResourceWithRawResponse(self._client.authentication_providers)

    @cached_property
    def available_phone_number_blocks(
        self,
    ) -> available_phone_number_blocks.AvailablePhoneNumberBlocksResourceWithRawResponse:
        """Number search"""
        from .resources.available_phone_number_blocks import AvailablePhoneNumberBlocksResourceWithRawResponse

        return AvailablePhoneNumberBlocksResourceWithRawResponse(self._client.available_phone_number_blocks)

    @cached_property
    def available_phone_numbers(self) -> available_phone_numbers.AvailablePhoneNumbersResourceWithRawResponse:
        """Number search"""
        from .resources.available_phone_numbers import AvailablePhoneNumbersResourceWithRawResponse

        return AvailablePhoneNumbersResourceWithRawResponse(self._client.available_phone_numbers)

    @cached_property
    def balance(self) -> balance.BalanceResourceWithRawResponse:
        """Billing operations"""
        from .resources.balance import BalanceResourceWithRawResponse

        return BalanceResourceWithRawResponse(self._client.balance)

    @cached_property
    def billing_groups(self) -> billing_groups.BillingGroupsResourceWithRawResponse:
        """Billing groups operations"""
        from .resources.billing_groups import BillingGroupsResourceWithRawResponse

        return BillingGroupsResourceWithRawResponse(self._client.billing_groups)

    @cached_property
    def bulk_sim_card_actions(self) -> bulk_sim_card_actions.BulkSimCardActionsResourceWithRawResponse:
        """
        View SIM card actions, their progress and timestamps using the SIM Card Actions API
        """
        from .resources.bulk_sim_card_actions import BulkSimCardActionsResourceWithRawResponse

        return BulkSimCardActionsResourceWithRawResponse(self._client.bulk_sim_card_actions)

    @cached_property
    def bundle_pricing(self) -> bundle_pricing.BundlePricingResourceWithRawResponse:
        from .resources.bundle_pricing import BundlePricingResourceWithRawResponse

        return BundlePricingResourceWithRawResponse(self._client.bundle_pricing)

    @cached_property
    def call_control_applications(self) -> call_control_applications.CallControlApplicationsResourceWithRawResponse:
        """Call Control applications operations"""
        from .resources.call_control_applications import CallControlApplicationsResourceWithRawResponse

        return CallControlApplicationsResourceWithRawResponse(self._client.call_control_applications)

    @cached_property
    def call_events(self) -> call_events.CallEventsResourceWithRawResponse:
        """Call Control debugging"""
        from .resources.call_events import CallEventsResourceWithRawResponse

        return CallEventsResourceWithRawResponse(self._client.call_events)

    @cached_property
    def calls(self) -> calls.CallsResourceWithRawResponse:
        from .resources.calls import CallsResourceWithRawResponse

        return CallsResourceWithRawResponse(self._client.calls)

    @cached_property
    def channel_zones(self) -> channel_zones.ChannelZonesResourceWithRawResponse:
        """Voice Channels"""
        from .resources.channel_zones import ChannelZonesResourceWithRawResponse

        return ChannelZonesResourceWithRawResponse(self._client.channel_zones)

    @cached_property
    def charges_breakdown(self) -> charges_breakdown.ChargesBreakdownResourceWithRawResponse:
        from .resources.charges_breakdown import ChargesBreakdownResourceWithRawResponse

        return ChargesBreakdownResourceWithRawResponse(self._client.charges_breakdown)

    @cached_property
    def charges_summary(self) -> charges_summary.ChargesSummaryResourceWithRawResponse:
        from .resources.charges_summary import ChargesSummaryResourceWithRawResponse

        return ChargesSummaryResourceWithRawResponse(self._client.charges_summary)

    @cached_property
    def comments(self) -> comments.CommentsResourceWithRawResponse:
        """Number orders"""
        from .resources.comments import CommentsResourceWithRawResponse

        return CommentsResourceWithRawResponse(self._client.comments)

    @cached_property
    def conferences(self) -> conferences.ConferencesResourceWithRawResponse:
        """Conference command operations"""
        from .resources.conferences import ConferencesResourceWithRawResponse

        return ConferencesResourceWithRawResponse(self._client.conferences)

    @cached_property
    def connections(self) -> connections.ConnectionsResourceWithRawResponse:
        from .resources.connections import ConnectionsResourceWithRawResponse

        return ConnectionsResourceWithRawResponse(self._client.connections)

    @cached_property
    def country_coverage(self) -> country_coverage.CountryCoverageResourceWithRawResponse:
        """Country Coverage"""
        from .resources.country_coverage import CountryCoverageResourceWithRawResponse

        return CountryCoverageResourceWithRawResponse(self._client.country_coverage)

    @cached_property
    def credential_connections(self) -> credential_connections.CredentialConnectionsResourceWithRawResponse:
        """Credential connection operations"""
        from .resources.credential_connections import CredentialConnectionsResourceWithRawResponse

        return CredentialConnectionsResourceWithRawResponse(self._client.credential_connections)

    @cached_property
    def custom_storage_credentials(self) -> custom_storage_credentials.CustomStorageCredentialsResourceWithRawResponse:
        """Call Recordings operations."""
        from .resources.custom_storage_credentials import CustomStorageCredentialsResourceWithRawResponse

        return CustomStorageCredentialsResourceWithRawResponse(self._client.custom_storage_credentials)

    @cached_property
    def customer_service_records(self) -> customer_service_records.CustomerServiceRecordsResourceWithRawResponse:
        """Customer Service Record operations"""
        from .resources.customer_service_records import CustomerServiceRecordsResourceWithRawResponse

        return CustomerServiceRecordsResourceWithRawResponse(self._client.customer_service_records)

    @cached_property
    def detail_records(self) -> detail_records.DetailRecordsResourceWithRawResponse:
        """Detail Records operations"""
        from .resources.detail_records import DetailRecordsResourceWithRawResponse

        return DetailRecordsResourceWithRawResponse(self._client.detail_records)

    @cached_property
    def dialogflow_connections(self) -> dialogflow_connections.DialogflowConnectionsResourceWithRawResponse:
        """Dialogflow Connection Operations."""
        from .resources.dialogflow_connections import DialogflowConnectionsResourceWithRawResponse

        return DialogflowConnectionsResourceWithRawResponse(self._client.dialogflow_connections)

    @cached_property
    def document_links(self) -> document_links.DocumentLinksResourceWithRawResponse:
        """Documents"""
        from .resources.document_links import DocumentLinksResourceWithRawResponse

        return DocumentLinksResourceWithRawResponse(self._client.document_links)

    @cached_property
    def documents(self) -> documents.DocumentsResourceWithRawResponse:
        """Documents"""
        from .resources.documents import DocumentsResourceWithRawResponse

        return DocumentsResourceWithRawResponse(self._client.documents)

    @cached_property
    def dynamic_emergency_addresses(
        self,
    ) -> dynamic_emergency_addresses.DynamicEmergencyAddressesResourceWithRawResponse:
        """Dynamic emergency address operations"""
        from .resources.dynamic_emergency_addresses import DynamicEmergencyAddressesResourceWithRawResponse

        return DynamicEmergencyAddressesResourceWithRawResponse(self._client.dynamic_emergency_addresses)

    @cached_property
    def dynamic_emergency_endpoints(
        self,
    ) -> dynamic_emergency_endpoints.DynamicEmergencyEndpointsResourceWithRawResponse:
        """Dynamic Emergency Endpoints"""
        from .resources.dynamic_emergency_endpoints import DynamicEmergencyEndpointsResourceWithRawResponse

        return DynamicEmergencyEndpointsResourceWithRawResponse(self._client.dynamic_emergency_endpoints)

    @cached_property
    def external_connections(self) -> external_connections.ExternalConnectionsResourceWithRawResponse:
        """External Connections operations"""
        from .resources.external_connections import ExternalConnectionsResourceWithRawResponse

        return ExternalConnectionsResourceWithRawResponse(self._client.external_connections)

    @cached_property
    def fax_applications(self) -> fax_applications.FaxApplicationsResourceWithRawResponse:
        """Fax Applications operations"""
        from .resources.fax_applications import FaxApplicationsResourceWithRawResponse

        return FaxApplicationsResourceWithRawResponse(self._client.fax_applications)

    @cached_property
    def faxes(self) -> faxes.FaxesResourceWithRawResponse:
        """Programmable fax command operations"""
        from .resources.faxes import FaxesResourceWithRawResponse

        return FaxesResourceWithRawResponse(self._client.faxes)

    @cached_property
    def fqdn_connections(self) -> fqdn_connections.FqdnConnectionsResourceWithRawResponse:
        """FQDN connection operations"""
        from .resources.fqdn_connections import FqdnConnectionsResourceWithRawResponse

        return FqdnConnectionsResourceWithRawResponse(self._client.fqdn_connections)

    @cached_property
    def fqdns(self) -> fqdns.FqdnsResourceWithRawResponse:
        """FQDN operations"""
        from .resources.fqdns import FqdnsResourceWithRawResponse

        return FqdnsResourceWithRawResponse(self._client.fqdns)

    @cached_property
    def global_ip_allowed_ports(self) -> global_ip_allowed_ports.GlobalIPAllowedPortsResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_allowed_ports import GlobalIPAllowedPortsResourceWithRawResponse

        return GlobalIPAllowedPortsResourceWithRawResponse(self._client.global_ip_allowed_ports)

    @cached_property
    def global_ip_assignment_health(
        self,
    ) -> global_ip_assignment_health.GlobalIPAssignmentHealthResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_assignment_health import GlobalIPAssignmentHealthResourceWithRawResponse

        return GlobalIPAssignmentHealthResourceWithRawResponse(self._client.global_ip_assignment_health)

    @cached_property
    def global_ip_assignments(self) -> global_ip_assignments.GlobalIPAssignmentsResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_assignments import GlobalIPAssignmentsResourceWithRawResponse

        return GlobalIPAssignmentsResourceWithRawResponse(self._client.global_ip_assignments)

    @cached_property
    def global_ip_assignments_usage(
        self,
    ) -> global_ip_assignments_usage.GlobalIPAssignmentsUsageResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_assignments_usage import GlobalIPAssignmentsUsageResourceWithRawResponse

        return GlobalIPAssignmentsUsageResourceWithRawResponse(self._client.global_ip_assignments_usage)

    @cached_property
    def global_ip_health_check_types(
        self,
    ) -> global_ip_health_check_types.GlobalIPHealthCheckTypesResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_health_check_types import GlobalIPHealthCheckTypesResourceWithRawResponse

        return GlobalIPHealthCheckTypesResourceWithRawResponse(self._client.global_ip_health_check_types)

    @cached_property
    def global_ip_health_checks(self) -> global_ip_health_checks.GlobalIPHealthChecksResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_health_checks import GlobalIPHealthChecksResourceWithRawResponse

        return GlobalIPHealthChecksResourceWithRawResponse(self._client.global_ip_health_checks)

    @cached_property
    def global_ip_latency(self) -> global_ip_latency.GlobalIPLatencyResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_latency import GlobalIPLatencyResourceWithRawResponse

        return GlobalIPLatencyResourceWithRawResponse(self._client.global_ip_latency)

    @cached_property
    def global_ip_protocols(self) -> global_ip_protocols.GlobalIPProtocolsResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_protocols import GlobalIPProtocolsResourceWithRawResponse

        return GlobalIPProtocolsResourceWithRawResponse(self._client.global_ip_protocols)

    @cached_property
    def global_ip_usage(self) -> global_ip_usage.GlobalIPUsageResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_usage import GlobalIPUsageResourceWithRawResponse

        return GlobalIPUsageResourceWithRawResponse(self._client.global_ip_usage)

    @cached_property
    def global_ips(self) -> global_ips.GlobalIPsResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ips import GlobalIPsResourceWithRawResponse

        return GlobalIPsResourceWithRawResponse(self._client.global_ips)

    @cached_property
    def inbound_channels(self) -> inbound_channels.InboundChannelsResourceWithRawResponse:
        """Voice Channels"""
        from .resources.inbound_channels import InboundChannelsResourceWithRawResponse

        return InboundChannelsResourceWithRawResponse(self._client.inbound_channels)

    @cached_property
    def integration_secrets(self) -> integration_secrets.IntegrationSecretsResourceWithRawResponse:
        """Store and retrieve integration secrets"""
        from .resources.integration_secrets import IntegrationSecretsResourceWithRawResponse

        return IntegrationSecretsResourceWithRawResponse(self._client.integration_secrets)

    @cached_property
    def inventory_coverage(self) -> inventory_coverage.InventoryCoverageResourceWithRawResponse:
        """Inventory Level"""
        from .resources.inventory_coverage import InventoryCoverageResourceWithRawResponse

        return InventoryCoverageResourceWithRawResponse(self._client.inventory_coverage)

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithRawResponse:
        from .resources.invoices import InvoicesResourceWithRawResponse

        return InvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def ip_connections(self) -> ip_connections.IPConnectionsResourceWithRawResponse:
        """IP connection operations"""
        from .resources.ip_connections import IPConnectionsResourceWithRawResponse

        return IPConnectionsResourceWithRawResponse(self._client.ip_connections)

    @cached_property
    def ips(self) -> ips.IPsResourceWithRawResponse:
        """IP operations"""
        from .resources.ips import IPsResourceWithRawResponse

        return IPsResourceWithRawResponse(self._client.ips)

    @cached_property
    def ledger_billing_group_reports(
        self,
    ) -> ledger_billing_group_reports.LedgerBillingGroupReportsResourceWithRawResponse:
        """Ledger billing reports"""
        from .resources.ledger_billing_group_reports import LedgerBillingGroupReportsResourceWithRawResponse

        return LedgerBillingGroupReportsResourceWithRawResponse(self._client.ledger_billing_group_reports)

    @cached_property
    def list(self) -> list.ListResourceWithRawResponse:
        """Voice Channels"""
        from .resources.list import ListResourceWithRawResponse

        return ListResourceWithRawResponse(self._client.list)

    @cached_property
    def managed_accounts(self) -> managed_accounts.ManagedAccountsResourceWithRawResponse:
        """Managed Accounts operations"""
        from .resources.managed_accounts import ManagedAccountsResourceWithRawResponse

        return ManagedAccountsResourceWithRawResponse(self._client.managed_accounts)

    @cached_property
    def media(self) -> media.MediaResourceWithRawResponse:
        """Media Storage operations"""
        from .resources.media import MediaResourceWithRawResponse

        return MediaResourceWithRawResponse(self._client.media)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def messaging(self) -> messaging.MessagingResourceWithRawResponse:
        from .resources.messaging import MessagingResourceWithRawResponse

        return MessagingResourceWithRawResponse(self._client.messaging)

    @cached_property
    def messaging_hosted_number_orders(
        self,
    ) -> messaging_hosted_number_orders.MessagingHostedNumberOrdersResourceWithRawResponse:
        """Manage your messaging hosted numbers"""
        from .resources.messaging_hosted_number_orders import MessagingHostedNumberOrdersResourceWithRawResponse

        return MessagingHostedNumberOrdersResourceWithRawResponse(self._client.messaging_hosted_number_orders)

    @cached_property
    def messaging_hosted_numbers(self) -> messaging_hosted_numbers.MessagingHostedNumbersResourceWithRawResponse:
        from .resources.messaging_hosted_numbers import MessagingHostedNumbersResourceWithRawResponse

        return MessagingHostedNumbersResourceWithRawResponse(self._client.messaging_hosted_numbers)

    @cached_property
    def messaging_numbers_bulk_updates(
        self,
    ) -> messaging_numbers_bulk_updates.MessagingNumbersBulkUpdatesResourceWithRawResponse:
        """Configure your phone numbers"""
        from .resources.messaging_numbers_bulk_updates import MessagingNumbersBulkUpdatesResourceWithRawResponse

        return MessagingNumbersBulkUpdatesResourceWithRawResponse(self._client.messaging_numbers_bulk_updates)

    @cached_property
    def messaging_optouts(self) -> messaging_optouts.MessagingOptoutsResourceWithRawResponse:
        """Opt-Out Management"""
        from .resources.messaging_optouts import MessagingOptoutsResourceWithRawResponse

        return MessagingOptoutsResourceWithRawResponse(self._client.messaging_optouts)

    @cached_property
    def messaging_profiles(self) -> messaging_profiles.MessagingProfilesResourceWithRawResponse:
        from .resources.messaging_profiles import MessagingProfilesResourceWithRawResponse

        return MessagingProfilesResourceWithRawResponse(self._client.messaging_profiles)

    @cached_property
    def messaging_tollfree(self) -> messaging_tollfree.MessagingTollfreeResourceWithRawResponse:
        from .resources.messaging_tollfree import MessagingTollfreeResourceWithRawResponse

        return MessagingTollfreeResourceWithRawResponse(self._client.messaging_tollfree)

    @cached_property
    def messaging_url_domains(self) -> messaging_url_domains.MessagingURLDomainsResourceWithRawResponse:
        """Messaging URL Domains"""
        from .resources.messaging_url_domains import MessagingURLDomainsResourceWithRawResponse

        return MessagingURLDomainsResourceWithRawResponse(self._client.messaging_url_domains)

    @cached_property
    def mobile_network_operators(self) -> mobile_network_operators.MobileNetworkOperatorsResourceWithRawResponse:
        """Mobile network operators operations"""
        from .resources.mobile_network_operators import MobileNetworkOperatorsResourceWithRawResponse

        return MobileNetworkOperatorsResourceWithRawResponse(self._client.mobile_network_operators)

    @cached_property
    def mobile_push_credentials(self) -> mobile_push_credentials.MobilePushCredentialsResourceWithRawResponse:
        """Mobile push credential management"""
        from .resources.mobile_push_credentials import MobilePushCredentialsResourceWithRawResponse

        return MobilePushCredentialsResourceWithRawResponse(self._client.mobile_push_credentials)

    @cached_property
    def network_coverage(self) -> network_coverage.NetworkCoverageResourceWithRawResponse:
        from .resources.network_coverage import NetworkCoverageResourceWithRawResponse

        return NetworkCoverageResourceWithRawResponse(self._client.network_coverage)

    @cached_property
    def networks(self) -> networks.NetworksResourceWithRawResponse:
        """Network operations"""
        from .resources.networks import NetworksResourceWithRawResponse

        return NetworksResourceWithRawResponse(self._client.networks)

    @cached_property
    def notification_channels(self) -> notification_channels.NotificationChannelsResourceWithRawResponse:
        """Notification settings operations"""
        from .resources.notification_channels import NotificationChannelsResourceWithRawResponse

        return NotificationChannelsResourceWithRawResponse(self._client.notification_channels)

    @cached_property
    def notification_event_conditions(
        self,
    ) -> notification_event_conditions.NotificationEventConditionsResourceWithRawResponse:
        """Notification settings operations"""
        from .resources.notification_event_conditions import NotificationEventConditionsResourceWithRawResponse

        return NotificationEventConditionsResourceWithRawResponse(self._client.notification_event_conditions)

    @cached_property
    def notification_events(self) -> notification_events.NotificationEventsResourceWithRawResponse:
        """Notification settings operations"""
        from .resources.notification_events import NotificationEventsResourceWithRawResponse

        return NotificationEventsResourceWithRawResponse(self._client.notification_events)

    @cached_property
    def notification_profiles(self) -> notification_profiles.NotificationProfilesResourceWithRawResponse:
        """Notification settings operations"""
        from .resources.notification_profiles import NotificationProfilesResourceWithRawResponse

        return NotificationProfilesResourceWithRawResponse(self._client.notification_profiles)

    @cached_property
    def notification_settings(self) -> notification_settings.NotificationSettingsResourceWithRawResponse:
        """Notification settings operations"""
        from .resources.notification_settings import NotificationSettingsResourceWithRawResponse

        return NotificationSettingsResourceWithRawResponse(self._client.notification_settings)

    @cached_property
    def number_block_orders(self) -> number_block_orders.NumberBlockOrdersResourceWithRawResponse:
        from .resources.number_block_orders import NumberBlockOrdersResourceWithRawResponse

        return NumberBlockOrdersResourceWithRawResponse(self._client.number_block_orders)

    @cached_property
    def number_lookup(self) -> number_lookup.NumberLookupResourceWithRawResponse:
        """Look up phone number data"""
        from .resources.number_lookup import NumberLookupResourceWithRawResponse

        return NumberLookupResourceWithRawResponse(self._client.number_lookup)

    @cached_property
    def number_order_phone_numbers(self) -> number_order_phone_numbers.NumberOrderPhoneNumbersResourceWithRawResponse:
        from .resources.number_order_phone_numbers import NumberOrderPhoneNumbersResourceWithRawResponse

        return NumberOrderPhoneNumbersResourceWithRawResponse(self._client.number_order_phone_numbers)

    @cached_property
    def number_orders(self) -> number_orders.NumberOrdersResourceWithRawResponse:
        """Number orders"""
        from .resources.number_orders import NumberOrdersResourceWithRawResponse

        return NumberOrdersResourceWithRawResponse(self._client.number_orders)

    @cached_property
    def number_reservations(self) -> number_reservations.NumberReservationsResourceWithRawResponse:
        """Number reservations"""
        from .resources.number_reservations import NumberReservationsResourceWithRawResponse

        return NumberReservationsResourceWithRawResponse(self._client.number_reservations)

    @cached_property
    def numbers_features(self) -> numbers_features.NumbersFeaturesResourceWithRawResponse:
        from .resources.numbers_features import NumbersFeaturesResourceWithRawResponse

        return NumbersFeaturesResourceWithRawResponse(self._client.numbers_features)

    @cached_property
    def operator_connect(self) -> operator_connect.OperatorConnectResourceWithRawResponse:
        from .resources.operator_connect import OperatorConnectResourceWithRawResponse

        return OperatorConnectResourceWithRawResponse(self._client.operator_connect)

    @cached_property
    def ota_updates(self) -> ota_updates.OtaUpdatesResourceWithRawResponse:
        """OTA updates operations"""
        from .resources.ota_updates import OtaUpdatesResourceWithRawResponse

        return OtaUpdatesResourceWithRawResponse(self._client.ota_updates)

    @cached_property
    def outbound_voice_profiles(self) -> outbound_voice_profiles.OutboundVoiceProfilesResourceWithRawResponse:
        """Outbound voice profiles operations"""
        from .resources.outbound_voice_profiles import OutboundVoiceProfilesResourceWithRawResponse

        return OutboundVoiceProfilesResourceWithRawResponse(self._client.outbound_voice_profiles)

    @cached_property
    def payment(self) -> payment.PaymentResourceWithRawResponse:
        """Operations for managing stored payment transactions."""
        from .resources.payment import PaymentResourceWithRawResponse

        return PaymentResourceWithRawResponse(self._client.payment)

    @cached_property
    def phone_number_blocks(self) -> phone_number_blocks.PhoneNumberBlocksResourceWithRawResponse:
        from .resources.phone_number_blocks import PhoneNumberBlocksResourceWithRawResponse

        return PhoneNumberBlocksResourceWithRawResponse(self._client.phone_number_blocks)

    @cached_property
    def phone_numbers(self) -> phone_numbers.PhoneNumbersResourceWithRawResponse:
        """Configure your phone numbers"""
        from .resources.phone_numbers import PhoneNumbersResourceWithRawResponse

        return PhoneNumbersResourceWithRawResponse(self._client.phone_numbers)

    @cached_property
    def phone_numbers_regulatory_requirements(
        self,
    ) -> phone_numbers_regulatory_requirements.PhoneNumbersRegulatoryRequirementsResourceWithRawResponse:
        """Regulatory Requirements"""
        from .resources.phone_numbers_regulatory_requirements import (
            PhoneNumbersRegulatoryRequirementsResourceWithRawResponse,
        )

        return PhoneNumbersRegulatoryRequirementsResourceWithRawResponse(
            self._client.phone_numbers_regulatory_requirements
        )

    @cached_property
    def portability_checks(self) -> portability_checks.PortabilityChecksResourceWithRawResponse:
        """Determining portability of phone numbers"""
        from .resources.portability_checks import PortabilityChecksResourceWithRawResponse

        return PortabilityChecksResourceWithRawResponse(self._client.portability_checks)

    @cached_property
    def porting(self) -> porting.PortingResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting import PortingResourceWithRawResponse

        return PortingResourceWithRawResponse(self._client.porting)

    @cached_property
    def porting_orders(self) -> porting_orders.PortingOrdersResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting_orders import PortingOrdersResourceWithRawResponse

        return PortingOrdersResourceWithRawResponse(self._client.porting_orders)

    @cached_property
    def porting_phone_numbers(self) -> porting_phone_numbers.PortingPhoneNumbersResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting_phone_numbers import PortingPhoneNumbersResourceWithRawResponse

        return PortingPhoneNumbersResourceWithRawResponse(self._client.porting_phone_numbers)

    @cached_property
    def portouts(self) -> portouts.PortoutsResourceWithRawResponse:
        """Number portout operations"""
        from .resources.portouts import PortoutsResourceWithRawResponse

        return PortoutsResourceWithRawResponse(self._client.portouts)

    @cached_property
    def private_wireless_gateways(self) -> private_wireless_gateways.PrivateWirelessGatewaysResourceWithRawResponse:
        """Private Wireless Gateways operations"""
        from .resources.private_wireless_gateways import PrivateWirelessGatewaysResourceWithRawResponse

        return PrivateWirelessGatewaysResourceWithRawResponse(self._client.private_wireless_gateways)

    @cached_property
    def public_internet_gateways(self) -> public_internet_gateways.PublicInternetGatewaysResourceWithRawResponse:
        """Public Internet Gateway operations"""
        from .resources.public_internet_gateways import PublicInternetGatewaysResourceWithRawResponse

        return PublicInternetGatewaysResourceWithRawResponse(self._client.public_internet_gateways)

    @cached_property
    def queues(self) -> queues.QueuesResourceWithRawResponse:
        """Queue commands operations"""
        from .resources.queues import QueuesResourceWithRawResponse

        return QueuesResourceWithRawResponse(self._client.queues)

    @cached_property
    def recording_transcriptions(self) -> recording_transcriptions.RecordingTranscriptionsResourceWithRawResponse:
        """Call Recordings operations."""
        from .resources.recording_transcriptions import RecordingTranscriptionsResourceWithRawResponse

        return RecordingTranscriptionsResourceWithRawResponse(self._client.recording_transcriptions)

    @cached_property
    def recordings(self) -> recordings.RecordingsResourceWithRawResponse:
        """Call Recordings operations."""
        from .resources.recordings import RecordingsResourceWithRawResponse

        return RecordingsResourceWithRawResponse(self._client.recordings)

    @cached_property
    def regions(self) -> regions.RegionsResourceWithRawResponse:
        """Regions"""
        from .resources.regions import RegionsResourceWithRawResponse

        return RegionsResourceWithRawResponse(self._client.regions)

    @cached_property
    def regulatory_requirements(self) -> regulatory_requirements.RegulatoryRequirementsResourceWithRawResponse:
        """Regulatory Requirements"""
        from .resources.regulatory_requirements import RegulatoryRequirementsResourceWithRawResponse

        return RegulatoryRequirementsResourceWithRawResponse(self._client.regulatory_requirements)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithRawResponse:
        from .resources.reports import ReportsResourceWithRawResponse

        return ReportsResourceWithRawResponse(self._client.reports)

    @cached_property
    def requirement_groups(self) -> requirement_groups.RequirementGroupsResourceWithRawResponse:
        """Requirement Groups"""
        from .resources.requirement_groups import RequirementGroupsResourceWithRawResponse

        return RequirementGroupsResourceWithRawResponse(self._client.requirement_groups)

    @cached_property
    def requirement_types(self) -> requirement_types.RequirementTypesResourceWithRawResponse:
        """Types of requirements for international numbers and porting orders"""
        from .resources.requirement_types import RequirementTypesResourceWithRawResponse

        return RequirementTypesResourceWithRawResponse(self._client.requirement_types)

    @cached_property
    def requirements(self) -> requirements.RequirementsResourceWithRawResponse:
        """Requirements for international numbers and porting orders"""
        from .resources.requirements import RequirementsResourceWithRawResponse

        return RequirementsResourceWithRawResponse(self._client.requirements)

    @cached_property
    def room_compositions(self) -> room_compositions.RoomCompositionsResourceWithRawResponse:
        """Rooms Compositions operations."""
        from .resources.room_compositions import RoomCompositionsResourceWithRawResponse

        return RoomCompositionsResourceWithRawResponse(self._client.room_compositions)

    @cached_property
    def room_participants(self) -> room_participants.RoomParticipantsResourceWithRawResponse:
        """Rooms Participants operations."""
        from .resources.room_participants import RoomParticipantsResourceWithRawResponse

        return RoomParticipantsResourceWithRawResponse(self._client.room_participants)

    @cached_property
    def room_recordings(self) -> room_recordings.RoomRecordingsResourceWithRawResponse:
        """Rooms Recordings operations."""
        from .resources.room_recordings import RoomRecordingsResourceWithRawResponse

        return RoomRecordingsResourceWithRawResponse(self._client.room_recordings)

    @cached_property
    def rooms(self) -> rooms.RoomsResourceWithRawResponse:
        """Rooms operations."""
        from .resources.rooms import RoomsResourceWithRawResponse

        return RoomsResourceWithRawResponse(self._client.rooms)

    @cached_property
    def seti(self) -> seti.SetiResourceWithRawResponse:
        """Observability into Telnyx platform stability and performance."""
        from .resources.seti import SetiResourceWithRawResponse

        return SetiResourceWithRawResponse(self._client.seti)

    @cached_property
    def short_codes(self) -> short_codes.ShortCodesResourceWithRawResponse:
        """Short codes"""
        from .resources.short_codes import ShortCodesResourceWithRawResponse

        return ShortCodesResourceWithRawResponse(self._client.short_codes)

    @cached_property
    def sim_card_data_usage_notifications(
        self,
    ) -> sim_card_data_usage_notifications.SimCardDataUsageNotificationsResourceWithRawResponse:
        """SIM Cards operations"""
        from .resources.sim_card_data_usage_notifications import SimCardDataUsageNotificationsResourceWithRawResponse

        return SimCardDataUsageNotificationsResourceWithRawResponse(self._client.sim_card_data_usage_notifications)

    @cached_property
    def sim_card_groups(self) -> sim_card_groups.SimCardGroupsResourceWithRawResponse:
        """SIM Card Groups operations"""
        from .resources.sim_card_groups import SimCardGroupsResourceWithRawResponse

        return SimCardGroupsResourceWithRawResponse(self._client.sim_card_groups)

    @cached_property
    def sim_card_order_preview(self) -> sim_card_order_preview.SimCardOrderPreviewResourceWithRawResponse:
        """SIM Card Orders operations"""
        from .resources.sim_card_order_preview import SimCardOrderPreviewResourceWithRawResponse

        return SimCardOrderPreviewResourceWithRawResponse(self._client.sim_card_order_preview)

    @cached_property
    def sim_card_orders(self) -> sim_card_orders.SimCardOrdersResourceWithRawResponse:
        """SIM Card Orders operations"""
        from .resources.sim_card_orders import SimCardOrdersResourceWithRawResponse

        return SimCardOrdersResourceWithRawResponse(self._client.sim_card_orders)

    @cached_property
    def sim_cards(self) -> sim_cards.SimCardsResourceWithRawResponse:
        """SIM Cards operations"""
        from .resources.sim_cards import SimCardsResourceWithRawResponse

        return SimCardsResourceWithRawResponse(self._client.sim_cards)

    @cached_property
    def siprec_connectors(self) -> siprec_connectors.SiprecConnectorsResourceWithRawResponse:
        """SIPREC connectors configuration."""
        from .resources.siprec_connectors import SiprecConnectorsResourceWithRawResponse

        return SiprecConnectorsResourceWithRawResponse(self._client.siprec_connectors)

    @cached_property
    def storage(self) -> storage.StorageResourceWithRawResponse:
        """Migrate data from an external provider into Telnyx Cloud Storage"""
        from .resources.storage import StorageResourceWithRawResponse

        return StorageResourceWithRawResponse(self._client.storage)

    @cached_property
    def sub_number_orders(self) -> sub_number_orders.SubNumberOrdersResourceWithRawResponse:
        from .resources.sub_number_orders import SubNumberOrdersResourceWithRawResponse

        return SubNumberOrdersResourceWithRawResponse(self._client.sub_number_orders)

    @cached_property
    def sub_number_orders_report(self) -> sub_number_orders_report.SubNumberOrdersReportResourceWithRawResponse:
        """Number orders"""
        from .resources.sub_number_orders_report import SubNumberOrdersReportResourceWithRawResponse

        return SubNumberOrdersReportResourceWithRawResponse(self._client.sub_number_orders_report)

    @cached_property
    def telephony_credentials(self) -> telephony_credentials.TelephonyCredentialsResourceWithRawResponse:
        from .resources.telephony_credentials import TelephonyCredentialsResourceWithRawResponse

        return TelephonyCredentialsResourceWithRawResponse(self._client.telephony_credentials)

    @cached_property
    def texml(self) -> texml.TexmlResourceWithRawResponse:
        """TeXML REST Commands"""
        from .resources.texml import TexmlResourceWithRawResponse

        return TexmlResourceWithRawResponse(self._client.texml)

    @cached_property
    def texml_applications(self) -> texml_applications.TexmlApplicationsResourceWithRawResponse:
        """TeXML Applications operations"""
        from .resources.texml_applications import TexmlApplicationsResourceWithRawResponse

        return TexmlApplicationsResourceWithRawResponse(self._client.texml_applications)

    @cached_property
    def text_to_speech(self) -> text_to_speech.TextToSpeechResourceWithRawResponse:
        """Text to speech streaming command operations"""
        from .resources.text_to_speech import TextToSpeechResourceWithRawResponse

        return TextToSpeechResourceWithRawResponse(self._client.text_to_speech)

    @cached_property
    def usage_reports(self) -> usage_reports.UsageReportsResourceWithRawResponse:
        """Usage data reporting across Telnyx products"""
        from .resources.usage_reports import UsageReportsResourceWithRawResponse

        return UsageReportsResourceWithRawResponse(self._client.usage_reports)

    @cached_property
    def user_addresses(self) -> user_addresses.UserAddressesResourceWithRawResponse:
        """Operations for working with UserAddress records.

        UserAddress records are stored addresses that users can use for non-emergency-calling purposes, such as for shipping addresses for orders of wireless SIMs (or other physical items). They cannot be used for emergency calling and are distinct from Address records, which are used on phone numbers.
        """
        from .resources.user_addresses import UserAddressesResourceWithRawResponse

        return UserAddressesResourceWithRawResponse(self._client.user_addresses)

    @cached_property
    def user_tags(self) -> user_tags.UserTagsResourceWithRawResponse:
        """User-defined tags for Telnyx resources"""
        from .resources.user_tags import UserTagsResourceWithRawResponse

        return UserTagsResourceWithRawResponse(self._client.user_tags)

    @cached_property
    def verifications(self) -> verifications.VerificationsResourceWithRawResponse:
        """Two factor authentication API"""
        from .resources.verifications import VerificationsResourceWithRawResponse

        return VerificationsResourceWithRawResponse(self._client.verifications)

    @cached_property
    def verified_numbers(self) -> verified_numbers.VerifiedNumbersResourceWithRawResponse:
        """Verified Numbers operations"""
        from .resources.verified_numbers import VerifiedNumbersResourceWithRawResponse

        return VerifiedNumbersResourceWithRawResponse(self._client.verified_numbers)

    @cached_property
    def verify_profiles(self) -> verify_profiles.VerifyProfilesResourceWithRawResponse:
        """Two factor authentication API"""
        from .resources.verify_profiles import VerifyProfilesResourceWithRawResponse

        return VerifyProfilesResourceWithRawResponse(self._client.verify_profiles)

    @cached_property
    def virtual_cross_connects(self) -> virtual_cross_connects.VirtualCrossConnectsResourceWithRawResponse:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects import VirtualCrossConnectsResourceWithRawResponse

        return VirtualCrossConnectsResourceWithRawResponse(self._client.virtual_cross_connects)

    @cached_property
    def virtual_cross_connects_coverage(
        self,
    ) -> virtual_cross_connects_coverage.VirtualCrossConnectsCoverageResourceWithRawResponse:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects_coverage import VirtualCrossConnectsCoverageResourceWithRawResponse

        return VirtualCrossConnectsCoverageResourceWithRawResponse(self._client.virtual_cross_connects_coverage)

    @cached_property
    def webhook_deliveries(self) -> webhook_deliveries.WebhookDeliveriesResourceWithRawResponse:
        """Webhooks operations"""
        from .resources.webhook_deliveries import WebhookDeliveriesResourceWithRawResponse

        return WebhookDeliveriesResourceWithRawResponse(self._client.webhook_deliveries)

    @cached_property
    def wireguard_interfaces(self) -> wireguard_interfaces.WireguardInterfacesResourceWithRawResponse:
        """WireGuard Interface operations"""
        from .resources.wireguard_interfaces import WireguardInterfacesResourceWithRawResponse

        return WireguardInterfacesResourceWithRawResponse(self._client.wireguard_interfaces)

    @cached_property
    def wireguard_peers(self) -> wireguard_peers.WireguardPeersResourceWithRawResponse:
        """WireGuard Interface operations"""
        from .resources.wireguard_peers import WireguardPeersResourceWithRawResponse

        return WireguardPeersResourceWithRawResponse(self._client.wireguard_peers)

    @cached_property
    def wireless(self) -> wireless.WirelessResourceWithRawResponse:
        """Regions for wireless services"""
        from .resources.wireless import WirelessResourceWithRawResponse

        return WirelessResourceWithRawResponse(self._client.wireless)

    @cached_property
    def wireless_blocklist_values(self) -> wireless_blocklist_values.WirelessBlocklistValuesResourceWithRawResponse:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklist_values import WirelessBlocklistValuesResourceWithRawResponse

        return WirelessBlocklistValuesResourceWithRawResponse(self._client.wireless_blocklist_values)

    @cached_property
    def wireless_blocklists(self) -> wireless_blocklists.WirelessBlocklistsResourceWithRawResponse:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklists import WirelessBlocklistsResourceWithRawResponse

        return WirelessBlocklistsResourceWithRawResponse(self._client.wireless_blocklists)

    @cached_property
    def well_known(self) -> well_known.WellKnownResourceWithRawResponse:
        from .resources.well_known import WellKnownResourceWithRawResponse

        return WellKnownResourceWithRawResponse(self._client.well_known)

    @cached_property
    def inexplicit_number_orders(self) -> inexplicit_number_orders.InexplicitNumberOrdersResourceWithRawResponse:
        """Inexplicit number orders for bulk purchasing without specifying exact numbers"""
        from .resources.inexplicit_number_orders import InexplicitNumberOrdersResourceWithRawResponse

        return InexplicitNumberOrdersResourceWithRawResponse(self._client.inexplicit_number_orders)

    @cached_property
    def mobile_phone_numbers(self) -> mobile_phone_numbers.MobilePhoneNumbersResourceWithRawResponse:
        """Mobile phone number operations"""
        from .resources.mobile_phone_numbers import MobilePhoneNumbersResourceWithRawResponse

        return MobilePhoneNumbersResourceWithRawResponse(self._client.mobile_phone_numbers)

    @cached_property
    def mobile_voice_connections(self) -> mobile_voice_connections.MobileVoiceConnectionsResourceWithRawResponse:
        """Mobile voice connection operations"""
        from .resources.mobile_voice_connections import MobileVoiceConnectionsResourceWithRawResponse

        return MobileVoiceConnectionsResourceWithRawResponse(self._client.mobile_voice_connections)

    @cached_property
    def messaging_10dlc(self) -> messaging_10dlc.Messaging10dlcResourceWithRawResponse:
        from .resources.messaging_10dlc import Messaging10dlcResourceWithRawResponse

        return Messaging10dlcResourceWithRawResponse(self._client.messaging_10dlc)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithRawResponse:
        from .resources.organizations import OrganizationsResourceWithRawResponse

        return OrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def alphanumeric_sender_ids(self) -> alphanumeric_sender_ids.AlphanumericSenderIDsResourceWithRawResponse:
        from .resources.alphanumeric_sender_ids import AlphanumericSenderIDsResourceWithRawResponse

        return AlphanumericSenderIDsResourceWithRawResponse(self._client.alphanumeric_sender_ids)

    @cached_property
    def messaging_profile_metrics(self) -> messaging_profile_metrics.MessagingProfileMetricsResourceWithRawResponse:
        from .resources.messaging_profile_metrics import MessagingProfileMetricsResourceWithRawResponse

        return MessagingProfileMetricsResourceWithRawResponse(self._client.messaging_profile_metrics)

    @cached_property
    def session_analysis(self) -> session_analysis.SessionAnalysisResourceWithRawResponse:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        from .resources.session_analysis import SessionAnalysisResourceWithRawResponse

        return SessionAnalysisResourceWithRawResponse(self._client.session_analysis)


class AsyncTelnyxWithRawResponse:
    _client: AsyncTelnyx

    def __init__(self, client: AsyncTelnyx) -> None:
        self._client = client

    @cached_property
    def legacy(self) -> legacy.AsyncLegacyResourceWithRawResponse:
        from .resources.legacy import AsyncLegacyResourceWithRawResponse

        return AsyncLegacyResourceWithRawResponse(self._client.legacy)

    @cached_property
    def oauth(self) -> oauth.AsyncOAuthResourceWithRawResponse:
        from .resources.oauth import AsyncOAuthResourceWithRawResponse

        return AsyncOAuthResourceWithRawResponse(self._client.oauth)

    @cached_property
    def oauth_clients(self) -> oauth_clients.AsyncOAuthClientsResourceWithRawResponse:
        from .resources.oauth_clients import AsyncOAuthClientsResourceWithRawResponse

        return AsyncOAuthClientsResourceWithRawResponse(self._client.oauth_clients)

    @cached_property
    def oauth_grants(self) -> oauth_grants.AsyncOAuthGrantsResourceWithRawResponse:
        from .resources.oauth_grants import AsyncOAuthGrantsResourceWithRawResponse

        return AsyncOAuthGrantsResourceWithRawResponse(self._client.oauth_grants)

    @cached_property
    def access_ip_address(self) -> access_ip_address.AsyncAccessIPAddressResourceWithRawResponse:
        """IP Address Operations"""
        from .resources.access_ip_address import AsyncAccessIPAddressResourceWithRawResponse

        return AsyncAccessIPAddressResourceWithRawResponse(self._client.access_ip_address)

    @cached_property
    def access_ip_ranges(self) -> access_ip_ranges.AsyncAccessIPRangesResourceWithRawResponse:
        """IP Range Operations"""
        from .resources.access_ip_ranges import AsyncAccessIPRangesResourceWithRawResponse

        return AsyncAccessIPRangesResourceWithRawResponse(self._client.access_ip_ranges)

    @cached_property
    def actions(self) -> actions.AsyncActionsResourceWithRawResponse:
        from .resources.actions import AsyncActionsResourceWithRawResponse

        return AsyncActionsResourceWithRawResponse(self._client.actions)

    @cached_property
    def addresses(self) -> addresses.AsyncAddressesResourceWithRawResponse:
        """Operations to work with Address records.

        Address records are emergency-validated addresses meant to be associated with phone numbers. They are validated for emergency usage purposes at creation time, although you may validate them separately with a custom workflow using the ValidateAddress operation separately. Address records are not usable for physical orders, such as for Telnyx SIM cards, please use UserAddress for that. It is not possible to entirely skip emergency service validation for Address records; if an emergency provider for a phone number rejects the address then it cannot be used on a phone number. To prevent records from getting out of sync, Address records are immutable and cannot be altered once created. If you realize you need to alter an address, a new record must be created with the differing address.
        """
        from .resources.addresses import AsyncAddressesResourceWithRawResponse

        return AsyncAddressesResourceWithRawResponse(self._client.addresses)

    @cached_property
    def advanced_orders(self) -> advanced_orders.AsyncAdvancedOrdersResourceWithRawResponse:
        from .resources.advanced_orders import AsyncAdvancedOrdersResourceWithRawResponse

        return AsyncAdvancedOrdersResourceWithRawResponse(self._client.advanced_orders)

    @cached_property
    def ai(self) -> ai.AsyncAIResourceWithRawResponse:
        """Generate text with LLMs"""
        from .resources.ai import AsyncAIResourceWithRawResponse

        return AsyncAIResourceWithRawResponse(self._client.ai)

    @cached_property
    def audit_events(self) -> audit_events.AsyncAuditEventsResourceWithRawResponse:
        """Audit log operations."""
        from .resources.audit_events import AsyncAuditEventsResourceWithRawResponse

        return AsyncAuditEventsResourceWithRawResponse(self._client.audit_events)

    @cached_property
    def authentication_providers(self) -> authentication_providers.AsyncAuthenticationProvidersResourceWithRawResponse:
        from .resources.authentication_providers import AsyncAuthenticationProvidersResourceWithRawResponse

        return AsyncAuthenticationProvidersResourceWithRawResponse(self._client.authentication_providers)

    @cached_property
    def available_phone_number_blocks(
        self,
    ) -> available_phone_number_blocks.AsyncAvailablePhoneNumberBlocksResourceWithRawResponse:
        """Number search"""
        from .resources.available_phone_number_blocks import AsyncAvailablePhoneNumberBlocksResourceWithRawResponse

        return AsyncAvailablePhoneNumberBlocksResourceWithRawResponse(self._client.available_phone_number_blocks)

    @cached_property
    def available_phone_numbers(self) -> available_phone_numbers.AsyncAvailablePhoneNumbersResourceWithRawResponse:
        """Number search"""
        from .resources.available_phone_numbers import AsyncAvailablePhoneNumbersResourceWithRawResponse

        return AsyncAvailablePhoneNumbersResourceWithRawResponse(self._client.available_phone_numbers)

    @cached_property
    def balance(self) -> balance.AsyncBalanceResourceWithRawResponse:
        """Billing operations"""
        from .resources.balance import AsyncBalanceResourceWithRawResponse

        return AsyncBalanceResourceWithRawResponse(self._client.balance)

    @cached_property
    def billing_groups(self) -> billing_groups.AsyncBillingGroupsResourceWithRawResponse:
        """Billing groups operations"""
        from .resources.billing_groups import AsyncBillingGroupsResourceWithRawResponse

        return AsyncBillingGroupsResourceWithRawResponse(self._client.billing_groups)

    @cached_property
    def bulk_sim_card_actions(self) -> bulk_sim_card_actions.AsyncBulkSimCardActionsResourceWithRawResponse:
        """
        View SIM card actions, their progress and timestamps using the SIM Card Actions API
        """
        from .resources.bulk_sim_card_actions import AsyncBulkSimCardActionsResourceWithRawResponse

        return AsyncBulkSimCardActionsResourceWithRawResponse(self._client.bulk_sim_card_actions)

    @cached_property
    def bundle_pricing(self) -> bundle_pricing.AsyncBundlePricingResourceWithRawResponse:
        from .resources.bundle_pricing import AsyncBundlePricingResourceWithRawResponse

        return AsyncBundlePricingResourceWithRawResponse(self._client.bundle_pricing)

    @cached_property
    def call_control_applications(
        self,
    ) -> call_control_applications.AsyncCallControlApplicationsResourceWithRawResponse:
        """Call Control applications operations"""
        from .resources.call_control_applications import AsyncCallControlApplicationsResourceWithRawResponse

        return AsyncCallControlApplicationsResourceWithRawResponse(self._client.call_control_applications)

    @cached_property
    def call_events(self) -> call_events.AsyncCallEventsResourceWithRawResponse:
        """Call Control debugging"""
        from .resources.call_events import AsyncCallEventsResourceWithRawResponse

        return AsyncCallEventsResourceWithRawResponse(self._client.call_events)

    @cached_property
    def calls(self) -> calls.AsyncCallsResourceWithRawResponse:
        from .resources.calls import AsyncCallsResourceWithRawResponse

        return AsyncCallsResourceWithRawResponse(self._client.calls)

    @cached_property
    def channel_zones(self) -> channel_zones.AsyncChannelZonesResourceWithRawResponse:
        """Voice Channels"""
        from .resources.channel_zones import AsyncChannelZonesResourceWithRawResponse

        return AsyncChannelZonesResourceWithRawResponse(self._client.channel_zones)

    @cached_property
    def charges_breakdown(self) -> charges_breakdown.AsyncChargesBreakdownResourceWithRawResponse:
        from .resources.charges_breakdown import AsyncChargesBreakdownResourceWithRawResponse

        return AsyncChargesBreakdownResourceWithRawResponse(self._client.charges_breakdown)

    @cached_property
    def charges_summary(self) -> charges_summary.AsyncChargesSummaryResourceWithRawResponse:
        from .resources.charges_summary import AsyncChargesSummaryResourceWithRawResponse

        return AsyncChargesSummaryResourceWithRawResponse(self._client.charges_summary)

    @cached_property
    def comments(self) -> comments.AsyncCommentsResourceWithRawResponse:
        """Number orders"""
        from .resources.comments import AsyncCommentsResourceWithRawResponse

        return AsyncCommentsResourceWithRawResponse(self._client.comments)

    @cached_property
    def conferences(self) -> conferences.AsyncConferencesResourceWithRawResponse:
        """Conference command operations"""
        from .resources.conferences import AsyncConferencesResourceWithRawResponse

        return AsyncConferencesResourceWithRawResponse(self._client.conferences)

    @cached_property
    def connections(self) -> connections.AsyncConnectionsResourceWithRawResponse:
        from .resources.connections import AsyncConnectionsResourceWithRawResponse

        return AsyncConnectionsResourceWithRawResponse(self._client.connections)

    @cached_property
    def country_coverage(self) -> country_coverage.AsyncCountryCoverageResourceWithRawResponse:
        """Country Coverage"""
        from .resources.country_coverage import AsyncCountryCoverageResourceWithRawResponse

        return AsyncCountryCoverageResourceWithRawResponse(self._client.country_coverage)

    @cached_property
    def credential_connections(self) -> credential_connections.AsyncCredentialConnectionsResourceWithRawResponse:
        """Credential connection operations"""
        from .resources.credential_connections import AsyncCredentialConnectionsResourceWithRawResponse

        return AsyncCredentialConnectionsResourceWithRawResponse(self._client.credential_connections)

    @cached_property
    def custom_storage_credentials(
        self,
    ) -> custom_storage_credentials.AsyncCustomStorageCredentialsResourceWithRawResponse:
        """Call Recordings operations."""
        from .resources.custom_storage_credentials import AsyncCustomStorageCredentialsResourceWithRawResponse

        return AsyncCustomStorageCredentialsResourceWithRawResponse(self._client.custom_storage_credentials)

    @cached_property
    def customer_service_records(self) -> customer_service_records.AsyncCustomerServiceRecordsResourceWithRawResponse:
        """Customer Service Record operations"""
        from .resources.customer_service_records import AsyncCustomerServiceRecordsResourceWithRawResponse

        return AsyncCustomerServiceRecordsResourceWithRawResponse(self._client.customer_service_records)

    @cached_property
    def detail_records(self) -> detail_records.AsyncDetailRecordsResourceWithRawResponse:
        """Detail Records operations"""
        from .resources.detail_records import AsyncDetailRecordsResourceWithRawResponse

        return AsyncDetailRecordsResourceWithRawResponse(self._client.detail_records)

    @cached_property
    def dialogflow_connections(self) -> dialogflow_connections.AsyncDialogflowConnectionsResourceWithRawResponse:
        """Dialogflow Connection Operations."""
        from .resources.dialogflow_connections import AsyncDialogflowConnectionsResourceWithRawResponse

        return AsyncDialogflowConnectionsResourceWithRawResponse(self._client.dialogflow_connections)

    @cached_property
    def document_links(self) -> document_links.AsyncDocumentLinksResourceWithRawResponse:
        """Documents"""
        from .resources.document_links import AsyncDocumentLinksResourceWithRawResponse

        return AsyncDocumentLinksResourceWithRawResponse(self._client.document_links)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsResourceWithRawResponse:
        """Documents"""
        from .resources.documents import AsyncDocumentsResourceWithRawResponse

        return AsyncDocumentsResourceWithRawResponse(self._client.documents)

    @cached_property
    def dynamic_emergency_addresses(
        self,
    ) -> dynamic_emergency_addresses.AsyncDynamicEmergencyAddressesResourceWithRawResponse:
        """Dynamic emergency address operations"""
        from .resources.dynamic_emergency_addresses import AsyncDynamicEmergencyAddressesResourceWithRawResponse

        return AsyncDynamicEmergencyAddressesResourceWithRawResponse(self._client.dynamic_emergency_addresses)

    @cached_property
    def dynamic_emergency_endpoints(
        self,
    ) -> dynamic_emergency_endpoints.AsyncDynamicEmergencyEndpointsResourceWithRawResponse:
        """Dynamic Emergency Endpoints"""
        from .resources.dynamic_emergency_endpoints import AsyncDynamicEmergencyEndpointsResourceWithRawResponse

        return AsyncDynamicEmergencyEndpointsResourceWithRawResponse(self._client.dynamic_emergency_endpoints)

    @cached_property
    def external_connections(self) -> external_connections.AsyncExternalConnectionsResourceWithRawResponse:
        """External Connections operations"""
        from .resources.external_connections import AsyncExternalConnectionsResourceWithRawResponse

        return AsyncExternalConnectionsResourceWithRawResponse(self._client.external_connections)

    @cached_property
    def fax_applications(self) -> fax_applications.AsyncFaxApplicationsResourceWithRawResponse:
        """Fax Applications operations"""
        from .resources.fax_applications import AsyncFaxApplicationsResourceWithRawResponse

        return AsyncFaxApplicationsResourceWithRawResponse(self._client.fax_applications)

    @cached_property
    def faxes(self) -> faxes.AsyncFaxesResourceWithRawResponse:
        """Programmable fax command operations"""
        from .resources.faxes import AsyncFaxesResourceWithRawResponse

        return AsyncFaxesResourceWithRawResponse(self._client.faxes)

    @cached_property
    def fqdn_connections(self) -> fqdn_connections.AsyncFqdnConnectionsResourceWithRawResponse:
        """FQDN connection operations"""
        from .resources.fqdn_connections import AsyncFqdnConnectionsResourceWithRawResponse

        return AsyncFqdnConnectionsResourceWithRawResponse(self._client.fqdn_connections)

    @cached_property
    def fqdns(self) -> fqdns.AsyncFqdnsResourceWithRawResponse:
        """FQDN operations"""
        from .resources.fqdns import AsyncFqdnsResourceWithRawResponse

        return AsyncFqdnsResourceWithRawResponse(self._client.fqdns)

    @cached_property
    def global_ip_allowed_ports(self) -> global_ip_allowed_ports.AsyncGlobalIPAllowedPortsResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_allowed_ports import AsyncGlobalIPAllowedPortsResourceWithRawResponse

        return AsyncGlobalIPAllowedPortsResourceWithRawResponse(self._client.global_ip_allowed_ports)

    @cached_property
    def global_ip_assignment_health(
        self,
    ) -> global_ip_assignment_health.AsyncGlobalIPAssignmentHealthResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_assignment_health import AsyncGlobalIPAssignmentHealthResourceWithRawResponse

        return AsyncGlobalIPAssignmentHealthResourceWithRawResponse(self._client.global_ip_assignment_health)

    @cached_property
    def global_ip_assignments(self) -> global_ip_assignments.AsyncGlobalIPAssignmentsResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_assignments import AsyncGlobalIPAssignmentsResourceWithRawResponse

        return AsyncGlobalIPAssignmentsResourceWithRawResponse(self._client.global_ip_assignments)

    @cached_property
    def global_ip_assignments_usage(
        self,
    ) -> global_ip_assignments_usage.AsyncGlobalIPAssignmentsUsageResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_assignments_usage import AsyncGlobalIPAssignmentsUsageResourceWithRawResponse

        return AsyncGlobalIPAssignmentsUsageResourceWithRawResponse(self._client.global_ip_assignments_usage)

    @cached_property
    def global_ip_health_check_types(
        self,
    ) -> global_ip_health_check_types.AsyncGlobalIPHealthCheckTypesResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_health_check_types import AsyncGlobalIPHealthCheckTypesResourceWithRawResponse

        return AsyncGlobalIPHealthCheckTypesResourceWithRawResponse(self._client.global_ip_health_check_types)

    @cached_property
    def global_ip_health_checks(self) -> global_ip_health_checks.AsyncGlobalIPHealthChecksResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_health_checks import AsyncGlobalIPHealthChecksResourceWithRawResponse

        return AsyncGlobalIPHealthChecksResourceWithRawResponse(self._client.global_ip_health_checks)

    @cached_property
    def global_ip_latency(self) -> global_ip_latency.AsyncGlobalIPLatencyResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_latency import AsyncGlobalIPLatencyResourceWithRawResponse

        return AsyncGlobalIPLatencyResourceWithRawResponse(self._client.global_ip_latency)

    @cached_property
    def global_ip_protocols(self) -> global_ip_protocols.AsyncGlobalIPProtocolsResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_protocols import AsyncGlobalIPProtocolsResourceWithRawResponse

        return AsyncGlobalIPProtocolsResourceWithRawResponse(self._client.global_ip_protocols)

    @cached_property
    def global_ip_usage(self) -> global_ip_usage.AsyncGlobalIPUsageResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ip_usage import AsyncGlobalIPUsageResourceWithRawResponse

        return AsyncGlobalIPUsageResourceWithRawResponse(self._client.global_ip_usage)

    @cached_property
    def global_ips(self) -> global_ips.AsyncGlobalIPsResourceWithRawResponse:
        """Global IPs"""
        from .resources.global_ips import AsyncGlobalIPsResourceWithRawResponse

        return AsyncGlobalIPsResourceWithRawResponse(self._client.global_ips)

    @cached_property
    def inbound_channels(self) -> inbound_channels.AsyncInboundChannelsResourceWithRawResponse:
        """Voice Channels"""
        from .resources.inbound_channels import AsyncInboundChannelsResourceWithRawResponse

        return AsyncInboundChannelsResourceWithRawResponse(self._client.inbound_channels)

    @cached_property
    def integration_secrets(self) -> integration_secrets.AsyncIntegrationSecretsResourceWithRawResponse:
        """Store and retrieve integration secrets"""
        from .resources.integration_secrets import AsyncIntegrationSecretsResourceWithRawResponse

        return AsyncIntegrationSecretsResourceWithRawResponse(self._client.integration_secrets)

    @cached_property
    def inventory_coverage(self) -> inventory_coverage.AsyncInventoryCoverageResourceWithRawResponse:
        """Inventory Level"""
        from .resources.inventory_coverage import AsyncInventoryCoverageResourceWithRawResponse

        return AsyncInventoryCoverageResourceWithRawResponse(self._client.inventory_coverage)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithRawResponse:
        from .resources.invoices import AsyncInvoicesResourceWithRawResponse

        return AsyncInvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def ip_connections(self) -> ip_connections.AsyncIPConnectionsResourceWithRawResponse:
        """IP connection operations"""
        from .resources.ip_connections import AsyncIPConnectionsResourceWithRawResponse

        return AsyncIPConnectionsResourceWithRawResponse(self._client.ip_connections)

    @cached_property
    def ips(self) -> ips.AsyncIPsResourceWithRawResponse:
        """IP operations"""
        from .resources.ips import AsyncIPsResourceWithRawResponse

        return AsyncIPsResourceWithRawResponse(self._client.ips)

    @cached_property
    def ledger_billing_group_reports(
        self,
    ) -> ledger_billing_group_reports.AsyncLedgerBillingGroupReportsResourceWithRawResponse:
        """Ledger billing reports"""
        from .resources.ledger_billing_group_reports import AsyncLedgerBillingGroupReportsResourceWithRawResponse

        return AsyncLedgerBillingGroupReportsResourceWithRawResponse(self._client.ledger_billing_group_reports)

    @cached_property
    def list(self) -> list.AsyncListResourceWithRawResponse:
        """Voice Channels"""
        from .resources.list import AsyncListResourceWithRawResponse

        return AsyncListResourceWithRawResponse(self._client.list)

    @cached_property
    def managed_accounts(self) -> managed_accounts.AsyncManagedAccountsResourceWithRawResponse:
        """Managed Accounts operations"""
        from .resources.managed_accounts import AsyncManagedAccountsResourceWithRawResponse

        return AsyncManagedAccountsResourceWithRawResponse(self._client.managed_accounts)

    @cached_property
    def media(self) -> media.AsyncMediaResourceWithRawResponse:
        """Media Storage operations"""
        from .resources.media import AsyncMediaResourceWithRawResponse

        return AsyncMediaResourceWithRawResponse(self._client.media)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def messaging(self) -> messaging.AsyncMessagingResourceWithRawResponse:
        from .resources.messaging import AsyncMessagingResourceWithRawResponse

        return AsyncMessagingResourceWithRawResponse(self._client.messaging)

    @cached_property
    def messaging_hosted_number_orders(
        self,
    ) -> messaging_hosted_number_orders.AsyncMessagingHostedNumberOrdersResourceWithRawResponse:
        """Manage your messaging hosted numbers"""
        from .resources.messaging_hosted_number_orders import AsyncMessagingHostedNumberOrdersResourceWithRawResponse

        return AsyncMessagingHostedNumberOrdersResourceWithRawResponse(self._client.messaging_hosted_number_orders)

    @cached_property
    def messaging_hosted_numbers(self) -> messaging_hosted_numbers.AsyncMessagingHostedNumbersResourceWithRawResponse:
        from .resources.messaging_hosted_numbers import AsyncMessagingHostedNumbersResourceWithRawResponse

        return AsyncMessagingHostedNumbersResourceWithRawResponse(self._client.messaging_hosted_numbers)

    @cached_property
    def messaging_numbers_bulk_updates(
        self,
    ) -> messaging_numbers_bulk_updates.AsyncMessagingNumbersBulkUpdatesResourceWithRawResponse:
        """Configure your phone numbers"""
        from .resources.messaging_numbers_bulk_updates import AsyncMessagingNumbersBulkUpdatesResourceWithRawResponse

        return AsyncMessagingNumbersBulkUpdatesResourceWithRawResponse(self._client.messaging_numbers_bulk_updates)

    @cached_property
    def messaging_optouts(self) -> messaging_optouts.AsyncMessagingOptoutsResourceWithRawResponse:
        """Opt-Out Management"""
        from .resources.messaging_optouts import AsyncMessagingOptoutsResourceWithRawResponse

        return AsyncMessagingOptoutsResourceWithRawResponse(self._client.messaging_optouts)

    @cached_property
    def messaging_profiles(self) -> messaging_profiles.AsyncMessagingProfilesResourceWithRawResponse:
        from .resources.messaging_profiles import AsyncMessagingProfilesResourceWithRawResponse

        return AsyncMessagingProfilesResourceWithRawResponse(self._client.messaging_profiles)

    @cached_property
    def messaging_tollfree(self) -> messaging_tollfree.AsyncMessagingTollfreeResourceWithRawResponse:
        from .resources.messaging_tollfree import AsyncMessagingTollfreeResourceWithRawResponse

        return AsyncMessagingTollfreeResourceWithRawResponse(self._client.messaging_tollfree)

    @cached_property
    def messaging_url_domains(self) -> messaging_url_domains.AsyncMessagingURLDomainsResourceWithRawResponse:
        """Messaging URL Domains"""
        from .resources.messaging_url_domains import AsyncMessagingURLDomainsResourceWithRawResponse

        return AsyncMessagingURLDomainsResourceWithRawResponse(self._client.messaging_url_domains)

    @cached_property
    def mobile_network_operators(self) -> mobile_network_operators.AsyncMobileNetworkOperatorsResourceWithRawResponse:
        """Mobile network operators operations"""
        from .resources.mobile_network_operators import AsyncMobileNetworkOperatorsResourceWithRawResponse

        return AsyncMobileNetworkOperatorsResourceWithRawResponse(self._client.mobile_network_operators)

    @cached_property
    def mobile_push_credentials(self) -> mobile_push_credentials.AsyncMobilePushCredentialsResourceWithRawResponse:
        """Mobile push credential management"""
        from .resources.mobile_push_credentials import AsyncMobilePushCredentialsResourceWithRawResponse

        return AsyncMobilePushCredentialsResourceWithRawResponse(self._client.mobile_push_credentials)

    @cached_property
    def network_coverage(self) -> network_coverage.AsyncNetworkCoverageResourceWithRawResponse:
        from .resources.network_coverage import AsyncNetworkCoverageResourceWithRawResponse

        return AsyncNetworkCoverageResourceWithRawResponse(self._client.network_coverage)

    @cached_property
    def networks(self) -> networks.AsyncNetworksResourceWithRawResponse:
        """Network operations"""
        from .resources.networks import AsyncNetworksResourceWithRawResponse

        return AsyncNetworksResourceWithRawResponse(self._client.networks)

    @cached_property
    def notification_channels(self) -> notification_channels.AsyncNotificationChannelsResourceWithRawResponse:
        """Notification settings operations"""
        from .resources.notification_channels import AsyncNotificationChannelsResourceWithRawResponse

        return AsyncNotificationChannelsResourceWithRawResponse(self._client.notification_channels)

    @cached_property
    def notification_event_conditions(
        self,
    ) -> notification_event_conditions.AsyncNotificationEventConditionsResourceWithRawResponse:
        """Notification settings operations"""
        from .resources.notification_event_conditions import AsyncNotificationEventConditionsResourceWithRawResponse

        return AsyncNotificationEventConditionsResourceWithRawResponse(self._client.notification_event_conditions)

    @cached_property
    def notification_events(self) -> notification_events.AsyncNotificationEventsResourceWithRawResponse:
        """Notification settings operations"""
        from .resources.notification_events import AsyncNotificationEventsResourceWithRawResponse

        return AsyncNotificationEventsResourceWithRawResponse(self._client.notification_events)

    @cached_property
    def notification_profiles(self) -> notification_profiles.AsyncNotificationProfilesResourceWithRawResponse:
        """Notification settings operations"""
        from .resources.notification_profiles import AsyncNotificationProfilesResourceWithRawResponse

        return AsyncNotificationProfilesResourceWithRawResponse(self._client.notification_profiles)

    @cached_property
    def notification_settings(self) -> notification_settings.AsyncNotificationSettingsResourceWithRawResponse:
        """Notification settings operations"""
        from .resources.notification_settings import AsyncNotificationSettingsResourceWithRawResponse

        return AsyncNotificationSettingsResourceWithRawResponse(self._client.notification_settings)

    @cached_property
    def number_block_orders(self) -> number_block_orders.AsyncNumberBlockOrdersResourceWithRawResponse:
        from .resources.number_block_orders import AsyncNumberBlockOrdersResourceWithRawResponse

        return AsyncNumberBlockOrdersResourceWithRawResponse(self._client.number_block_orders)

    @cached_property
    def number_lookup(self) -> number_lookup.AsyncNumberLookupResourceWithRawResponse:
        """Look up phone number data"""
        from .resources.number_lookup import AsyncNumberLookupResourceWithRawResponse

        return AsyncNumberLookupResourceWithRawResponse(self._client.number_lookup)

    @cached_property
    def number_order_phone_numbers(
        self,
    ) -> number_order_phone_numbers.AsyncNumberOrderPhoneNumbersResourceWithRawResponse:
        from .resources.number_order_phone_numbers import AsyncNumberOrderPhoneNumbersResourceWithRawResponse

        return AsyncNumberOrderPhoneNumbersResourceWithRawResponse(self._client.number_order_phone_numbers)

    @cached_property
    def number_orders(self) -> number_orders.AsyncNumberOrdersResourceWithRawResponse:
        """Number orders"""
        from .resources.number_orders import AsyncNumberOrdersResourceWithRawResponse

        return AsyncNumberOrdersResourceWithRawResponse(self._client.number_orders)

    @cached_property
    def number_reservations(self) -> number_reservations.AsyncNumberReservationsResourceWithRawResponse:
        """Number reservations"""
        from .resources.number_reservations import AsyncNumberReservationsResourceWithRawResponse

        return AsyncNumberReservationsResourceWithRawResponse(self._client.number_reservations)

    @cached_property
    def numbers_features(self) -> numbers_features.AsyncNumbersFeaturesResourceWithRawResponse:
        from .resources.numbers_features import AsyncNumbersFeaturesResourceWithRawResponse

        return AsyncNumbersFeaturesResourceWithRawResponse(self._client.numbers_features)

    @cached_property
    def operator_connect(self) -> operator_connect.AsyncOperatorConnectResourceWithRawResponse:
        from .resources.operator_connect import AsyncOperatorConnectResourceWithRawResponse

        return AsyncOperatorConnectResourceWithRawResponse(self._client.operator_connect)

    @cached_property
    def ota_updates(self) -> ota_updates.AsyncOtaUpdatesResourceWithRawResponse:
        """OTA updates operations"""
        from .resources.ota_updates import AsyncOtaUpdatesResourceWithRawResponse

        return AsyncOtaUpdatesResourceWithRawResponse(self._client.ota_updates)

    @cached_property
    def outbound_voice_profiles(self) -> outbound_voice_profiles.AsyncOutboundVoiceProfilesResourceWithRawResponse:
        """Outbound voice profiles operations"""
        from .resources.outbound_voice_profiles import AsyncOutboundVoiceProfilesResourceWithRawResponse

        return AsyncOutboundVoiceProfilesResourceWithRawResponse(self._client.outbound_voice_profiles)

    @cached_property
    def payment(self) -> payment.AsyncPaymentResourceWithRawResponse:
        """Operations for managing stored payment transactions."""
        from .resources.payment import AsyncPaymentResourceWithRawResponse

        return AsyncPaymentResourceWithRawResponse(self._client.payment)

    @cached_property
    def phone_number_blocks(self) -> phone_number_blocks.AsyncPhoneNumberBlocksResourceWithRawResponse:
        from .resources.phone_number_blocks import AsyncPhoneNumberBlocksResourceWithRawResponse

        return AsyncPhoneNumberBlocksResourceWithRawResponse(self._client.phone_number_blocks)

    @cached_property
    def phone_numbers(self) -> phone_numbers.AsyncPhoneNumbersResourceWithRawResponse:
        """Configure your phone numbers"""
        from .resources.phone_numbers import AsyncPhoneNumbersResourceWithRawResponse

        return AsyncPhoneNumbersResourceWithRawResponse(self._client.phone_numbers)

    @cached_property
    def phone_numbers_regulatory_requirements(
        self,
    ) -> phone_numbers_regulatory_requirements.AsyncPhoneNumbersRegulatoryRequirementsResourceWithRawResponse:
        """Regulatory Requirements"""
        from .resources.phone_numbers_regulatory_requirements import (
            AsyncPhoneNumbersRegulatoryRequirementsResourceWithRawResponse,
        )

        return AsyncPhoneNumbersRegulatoryRequirementsResourceWithRawResponse(
            self._client.phone_numbers_regulatory_requirements
        )

    @cached_property
    def portability_checks(self) -> portability_checks.AsyncPortabilityChecksResourceWithRawResponse:
        """Determining portability of phone numbers"""
        from .resources.portability_checks import AsyncPortabilityChecksResourceWithRawResponse

        return AsyncPortabilityChecksResourceWithRawResponse(self._client.portability_checks)

    @cached_property
    def porting(self) -> porting.AsyncPortingResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting import AsyncPortingResourceWithRawResponse

        return AsyncPortingResourceWithRawResponse(self._client.porting)

    @cached_property
    def porting_orders(self) -> porting_orders.AsyncPortingOrdersResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting_orders import AsyncPortingOrdersResourceWithRawResponse

        return AsyncPortingOrdersResourceWithRawResponse(self._client.porting_orders)

    @cached_property
    def porting_phone_numbers(self) -> porting_phone_numbers.AsyncPortingPhoneNumbersResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting_phone_numbers import AsyncPortingPhoneNumbersResourceWithRawResponse

        return AsyncPortingPhoneNumbersResourceWithRawResponse(self._client.porting_phone_numbers)

    @cached_property
    def portouts(self) -> portouts.AsyncPortoutsResourceWithRawResponse:
        """Number portout operations"""
        from .resources.portouts import AsyncPortoutsResourceWithRawResponse

        return AsyncPortoutsResourceWithRawResponse(self._client.portouts)

    @cached_property
    def private_wireless_gateways(
        self,
    ) -> private_wireless_gateways.AsyncPrivateWirelessGatewaysResourceWithRawResponse:
        """Private Wireless Gateways operations"""
        from .resources.private_wireless_gateways import AsyncPrivateWirelessGatewaysResourceWithRawResponse

        return AsyncPrivateWirelessGatewaysResourceWithRawResponse(self._client.private_wireless_gateways)

    @cached_property
    def public_internet_gateways(self) -> public_internet_gateways.AsyncPublicInternetGatewaysResourceWithRawResponse:
        """Public Internet Gateway operations"""
        from .resources.public_internet_gateways import AsyncPublicInternetGatewaysResourceWithRawResponse

        return AsyncPublicInternetGatewaysResourceWithRawResponse(self._client.public_internet_gateways)

    @cached_property
    def queues(self) -> queues.AsyncQueuesResourceWithRawResponse:
        """Queue commands operations"""
        from .resources.queues import AsyncQueuesResourceWithRawResponse

        return AsyncQueuesResourceWithRawResponse(self._client.queues)

    @cached_property
    def recording_transcriptions(self) -> recording_transcriptions.AsyncRecordingTranscriptionsResourceWithRawResponse:
        """Call Recordings operations."""
        from .resources.recording_transcriptions import AsyncRecordingTranscriptionsResourceWithRawResponse

        return AsyncRecordingTranscriptionsResourceWithRawResponse(self._client.recording_transcriptions)

    @cached_property
    def recordings(self) -> recordings.AsyncRecordingsResourceWithRawResponse:
        """Call Recordings operations."""
        from .resources.recordings import AsyncRecordingsResourceWithRawResponse

        return AsyncRecordingsResourceWithRawResponse(self._client.recordings)

    @cached_property
    def regions(self) -> regions.AsyncRegionsResourceWithRawResponse:
        """Regions"""
        from .resources.regions import AsyncRegionsResourceWithRawResponse

        return AsyncRegionsResourceWithRawResponse(self._client.regions)

    @cached_property
    def regulatory_requirements(self) -> regulatory_requirements.AsyncRegulatoryRequirementsResourceWithRawResponse:
        """Regulatory Requirements"""
        from .resources.regulatory_requirements import AsyncRegulatoryRequirementsResourceWithRawResponse

        return AsyncRegulatoryRequirementsResourceWithRawResponse(self._client.regulatory_requirements)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithRawResponse:
        from .resources.reports import AsyncReportsResourceWithRawResponse

        return AsyncReportsResourceWithRawResponse(self._client.reports)

    @cached_property
    def requirement_groups(self) -> requirement_groups.AsyncRequirementGroupsResourceWithRawResponse:
        """Requirement Groups"""
        from .resources.requirement_groups import AsyncRequirementGroupsResourceWithRawResponse

        return AsyncRequirementGroupsResourceWithRawResponse(self._client.requirement_groups)

    @cached_property
    def requirement_types(self) -> requirement_types.AsyncRequirementTypesResourceWithRawResponse:
        """Types of requirements for international numbers and porting orders"""
        from .resources.requirement_types import AsyncRequirementTypesResourceWithRawResponse

        return AsyncRequirementTypesResourceWithRawResponse(self._client.requirement_types)

    @cached_property
    def requirements(self) -> requirements.AsyncRequirementsResourceWithRawResponse:
        """Requirements for international numbers and porting orders"""
        from .resources.requirements import AsyncRequirementsResourceWithRawResponse

        return AsyncRequirementsResourceWithRawResponse(self._client.requirements)

    @cached_property
    def room_compositions(self) -> room_compositions.AsyncRoomCompositionsResourceWithRawResponse:
        """Rooms Compositions operations."""
        from .resources.room_compositions import AsyncRoomCompositionsResourceWithRawResponse

        return AsyncRoomCompositionsResourceWithRawResponse(self._client.room_compositions)

    @cached_property
    def room_participants(self) -> room_participants.AsyncRoomParticipantsResourceWithRawResponse:
        """Rooms Participants operations."""
        from .resources.room_participants import AsyncRoomParticipantsResourceWithRawResponse

        return AsyncRoomParticipantsResourceWithRawResponse(self._client.room_participants)

    @cached_property
    def room_recordings(self) -> room_recordings.AsyncRoomRecordingsResourceWithRawResponse:
        """Rooms Recordings operations."""
        from .resources.room_recordings import AsyncRoomRecordingsResourceWithRawResponse

        return AsyncRoomRecordingsResourceWithRawResponse(self._client.room_recordings)

    @cached_property
    def rooms(self) -> rooms.AsyncRoomsResourceWithRawResponse:
        """Rooms operations."""
        from .resources.rooms import AsyncRoomsResourceWithRawResponse

        return AsyncRoomsResourceWithRawResponse(self._client.rooms)

    @cached_property
    def seti(self) -> seti.AsyncSetiResourceWithRawResponse:
        """Observability into Telnyx platform stability and performance."""
        from .resources.seti import AsyncSetiResourceWithRawResponse

        return AsyncSetiResourceWithRawResponse(self._client.seti)

    @cached_property
    def short_codes(self) -> short_codes.AsyncShortCodesResourceWithRawResponse:
        """Short codes"""
        from .resources.short_codes import AsyncShortCodesResourceWithRawResponse

        return AsyncShortCodesResourceWithRawResponse(self._client.short_codes)

    @cached_property
    def sim_card_data_usage_notifications(
        self,
    ) -> sim_card_data_usage_notifications.AsyncSimCardDataUsageNotificationsResourceWithRawResponse:
        """SIM Cards operations"""
        from .resources.sim_card_data_usage_notifications import (
            AsyncSimCardDataUsageNotificationsResourceWithRawResponse,
        )

        return AsyncSimCardDataUsageNotificationsResourceWithRawResponse(self._client.sim_card_data_usage_notifications)

    @cached_property
    def sim_card_groups(self) -> sim_card_groups.AsyncSimCardGroupsResourceWithRawResponse:
        """SIM Card Groups operations"""
        from .resources.sim_card_groups import AsyncSimCardGroupsResourceWithRawResponse

        return AsyncSimCardGroupsResourceWithRawResponse(self._client.sim_card_groups)

    @cached_property
    def sim_card_order_preview(self) -> sim_card_order_preview.AsyncSimCardOrderPreviewResourceWithRawResponse:
        """SIM Card Orders operations"""
        from .resources.sim_card_order_preview import AsyncSimCardOrderPreviewResourceWithRawResponse

        return AsyncSimCardOrderPreviewResourceWithRawResponse(self._client.sim_card_order_preview)

    @cached_property
    def sim_card_orders(self) -> sim_card_orders.AsyncSimCardOrdersResourceWithRawResponse:
        """SIM Card Orders operations"""
        from .resources.sim_card_orders import AsyncSimCardOrdersResourceWithRawResponse

        return AsyncSimCardOrdersResourceWithRawResponse(self._client.sim_card_orders)

    @cached_property
    def sim_cards(self) -> sim_cards.AsyncSimCardsResourceWithRawResponse:
        """SIM Cards operations"""
        from .resources.sim_cards import AsyncSimCardsResourceWithRawResponse

        return AsyncSimCardsResourceWithRawResponse(self._client.sim_cards)

    @cached_property
    def siprec_connectors(self) -> siprec_connectors.AsyncSiprecConnectorsResourceWithRawResponse:
        """SIPREC connectors configuration."""
        from .resources.siprec_connectors import AsyncSiprecConnectorsResourceWithRawResponse

        return AsyncSiprecConnectorsResourceWithRawResponse(self._client.siprec_connectors)

    @cached_property
    def storage(self) -> storage.AsyncStorageResourceWithRawResponse:
        """Migrate data from an external provider into Telnyx Cloud Storage"""
        from .resources.storage import AsyncStorageResourceWithRawResponse

        return AsyncStorageResourceWithRawResponse(self._client.storage)

    @cached_property
    def sub_number_orders(self) -> sub_number_orders.AsyncSubNumberOrdersResourceWithRawResponse:
        from .resources.sub_number_orders import AsyncSubNumberOrdersResourceWithRawResponse

        return AsyncSubNumberOrdersResourceWithRawResponse(self._client.sub_number_orders)

    @cached_property
    def sub_number_orders_report(self) -> sub_number_orders_report.AsyncSubNumberOrdersReportResourceWithRawResponse:
        """Number orders"""
        from .resources.sub_number_orders_report import AsyncSubNumberOrdersReportResourceWithRawResponse

        return AsyncSubNumberOrdersReportResourceWithRawResponse(self._client.sub_number_orders_report)

    @cached_property
    def telephony_credentials(self) -> telephony_credentials.AsyncTelephonyCredentialsResourceWithRawResponse:
        from .resources.telephony_credentials import AsyncTelephonyCredentialsResourceWithRawResponse

        return AsyncTelephonyCredentialsResourceWithRawResponse(self._client.telephony_credentials)

    @cached_property
    def texml(self) -> texml.AsyncTexmlResourceWithRawResponse:
        """TeXML REST Commands"""
        from .resources.texml import AsyncTexmlResourceWithRawResponse

        return AsyncTexmlResourceWithRawResponse(self._client.texml)

    @cached_property
    def texml_applications(self) -> texml_applications.AsyncTexmlApplicationsResourceWithRawResponse:
        """TeXML Applications operations"""
        from .resources.texml_applications import AsyncTexmlApplicationsResourceWithRawResponse

        return AsyncTexmlApplicationsResourceWithRawResponse(self._client.texml_applications)

    @cached_property
    def text_to_speech(self) -> text_to_speech.AsyncTextToSpeechResourceWithRawResponse:
        """Text to speech streaming command operations"""
        from .resources.text_to_speech import AsyncTextToSpeechResourceWithRawResponse

        return AsyncTextToSpeechResourceWithRawResponse(self._client.text_to_speech)

    @cached_property
    def usage_reports(self) -> usage_reports.AsyncUsageReportsResourceWithRawResponse:
        """Usage data reporting across Telnyx products"""
        from .resources.usage_reports import AsyncUsageReportsResourceWithRawResponse

        return AsyncUsageReportsResourceWithRawResponse(self._client.usage_reports)

    @cached_property
    def user_addresses(self) -> user_addresses.AsyncUserAddressesResourceWithRawResponse:
        """Operations for working with UserAddress records.

        UserAddress records are stored addresses that users can use for non-emergency-calling purposes, such as for shipping addresses for orders of wireless SIMs (or other physical items). They cannot be used for emergency calling and are distinct from Address records, which are used on phone numbers.
        """
        from .resources.user_addresses import AsyncUserAddressesResourceWithRawResponse

        return AsyncUserAddressesResourceWithRawResponse(self._client.user_addresses)

    @cached_property
    def user_tags(self) -> user_tags.AsyncUserTagsResourceWithRawResponse:
        """User-defined tags for Telnyx resources"""
        from .resources.user_tags import AsyncUserTagsResourceWithRawResponse

        return AsyncUserTagsResourceWithRawResponse(self._client.user_tags)

    @cached_property
    def verifications(self) -> verifications.AsyncVerificationsResourceWithRawResponse:
        """Two factor authentication API"""
        from .resources.verifications import AsyncVerificationsResourceWithRawResponse

        return AsyncVerificationsResourceWithRawResponse(self._client.verifications)

    @cached_property
    def verified_numbers(self) -> verified_numbers.AsyncVerifiedNumbersResourceWithRawResponse:
        """Verified Numbers operations"""
        from .resources.verified_numbers import AsyncVerifiedNumbersResourceWithRawResponse

        return AsyncVerifiedNumbersResourceWithRawResponse(self._client.verified_numbers)

    @cached_property
    def verify_profiles(self) -> verify_profiles.AsyncVerifyProfilesResourceWithRawResponse:
        """Two factor authentication API"""
        from .resources.verify_profiles import AsyncVerifyProfilesResourceWithRawResponse

        return AsyncVerifyProfilesResourceWithRawResponse(self._client.verify_profiles)

    @cached_property
    def virtual_cross_connects(self) -> virtual_cross_connects.AsyncVirtualCrossConnectsResourceWithRawResponse:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects import AsyncVirtualCrossConnectsResourceWithRawResponse

        return AsyncVirtualCrossConnectsResourceWithRawResponse(self._client.virtual_cross_connects)

    @cached_property
    def virtual_cross_connects_coverage(
        self,
    ) -> virtual_cross_connects_coverage.AsyncVirtualCrossConnectsCoverageResourceWithRawResponse:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects_coverage import AsyncVirtualCrossConnectsCoverageResourceWithRawResponse

        return AsyncVirtualCrossConnectsCoverageResourceWithRawResponse(self._client.virtual_cross_connects_coverage)

    @cached_property
    def webhook_deliveries(self) -> webhook_deliveries.AsyncWebhookDeliveriesResourceWithRawResponse:
        """Webhooks operations"""
        from .resources.webhook_deliveries import AsyncWebhookDeliveriesResourceWithRawResponse

        return AsyncWebhookDeliveriesResourceWithRawResponse(self._client.webhook_deliveries)

    @cached_property
    def wireguard_interfaces(self) -> wireguard_interfaces.AsyncWireguardInterfacesResourceWithRawResponse:
        """WireGuard Interface operations"""
        from .resources.wireguard_interfaces import AsyncWireguardInterfacesResourceWithRawResponse

        return AsyncWireguardInterfacesResourceWithRawResponse(self._client.wireguard_interfaces)

    @cached_property
    def wireguard_peers(self) -> wireguard_peers.AsyncWireguardPeersResourceWithRawResponse:
        """WireGuard Interface operations"""
        from .resources.wireguard_peers import AsyncWireguardPeersResourceWithRawResponse

        return AsyncWireguardPeersResourceWithRawResponse(self._client.wireguard_peers)

    @cached_property
    def wireless(self) -> wireless.AsyncWirelessResourceWithRawResponse:
        """Regions for wireless services"""
        from .resources.wireless import AsyncWirelessResourceWithRawResponse

        return AsyncWirelessResourceWithRawResponse(self._client.wireless)

    @cached_property
    def wireless_blocklist_values(
        self,
    ) -> wireless_blocklist_values.AsyncWirelessBlocklistValuesResourceWithRawResponse:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklist_values import AsyncWirelessBlocklistValuesResourceWithRawResponse

        return AsyncWirelessBlocklistValuesResourceWithRawResponse(self._client.wireless_blocklist_values)

    @cached_property
    def wireless_blocklists(self) -> wireless_blocklists.AsyncWirelessBlocklistsResourceWithRawResponse:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklists import AsyncWirelessBlocklistsResourceWithRawResponse

        return AsyncWirelessBlocklistsResourceWithRawResponse(self._client.wireless_blocklists)

    @cached_property
    def well_known(self) -> well_known.AsyncWellKnownResourceWithRawResponse:
        from .resources.well_known import AsyncWellKnownResourceWithRawResponse

        return AsyncWellKnownResourceWithRawResponse(self._client.well_known)

    @cached_property
    def inexplicit_number_orders(self) -> inexplicit_number_orders.AsyncInexplicitNumberOrdersResourceWithRawResponse:
        """Inexplicit number orders for bulk purchasing without specifying exact numbers"""
        from .resources.inexplicit_number_orders import AsyncInexplicitNumberOrdersResourceWithRawResponse

        return AsyncInexplicitNumberOrdersResourceWithRawResponse(self._client.inexplicit_number_orders)

    @cached_property
    def mobile_phone_numbers(self) -> mobile_phone_numbers.AsyncMobilePhoneNumbersResourceWithRawResponse:
        """Mobile phone number operations"""
        from .resources.mobile_phone_numbers import AsyncMobilePhoneNumbersResourceWithRawResponse

        return AsyncMobilePhoneNumbersResourceWithRawResponse(self._client.mobile_phone_numbers)

    @cached_property
    def mobile_voice_connections(self) -> mobile_voice_connections.AsyncMobileVoiceConnectionsResourceWithRawResponse:
        """Mobile voice connection operations"""
        from .resources.mobile_voice_connections import AsyncMobileVoiceConnectionsResourceWithRawResponse

        return AsyncMobileVoiceConnectionsResourceWithRawResponse(self._client.mobile_voice_connections)

    @cached_property
    def messaging_10dlc(self) -> messaging_10dlc.AsyncMessaging10dlcResourceWithRawResponse:
        from .resources.messaging_10dlc import AsyncMessaging10dlcResourceWithRawResponse

        return AsyncMessaging10dlcResourceWithRawResponse(self._client.messaging_10dlc)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithRawResponse

        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def alphanumeric_sender_ids(self) -> alphanumeric_sender_ids.AsyncAlphanumericSenderIDsResourceWithRawResponse:
        from .resources.alphanumeric_sender_ids import AsyncAlphanumericSenderIDsResourceWithRawResponse

        return AsyncAlphanumericSenderIDsResourceWithRawResponse(self._client.alphanumeric_sender_ids)

    @cached_property
    def messaging_profile_metrics(
        self,
    ) -> messaging_profile_metrics.AsyncMessagingProfileMetricsResourceWithRawResponse:
        from .resources.messaging_profile_metrics import AsyncMessagingProfileMetricsResourceWithRawResponse

        return AsyncMessagingProfileMetricsResourceWithRawResponse(self._client.messaging_profile_metrics)

    @cached_property
    def session_analysis(self) -> session_analysis.AsyncSessionAnalysisResourceWithRawResponse:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        from .resources.session_analysis import AsyncSessionAnalysisResourceWithRawResponse

        return AsyncSessionAnalysisResourceWithRawResponse(self._client.session_analysis)


class TelnyxWithStreamedResponse:
    _client: Telnyx

    def __init__(self, client: Telnyx) -> None:
        self._client = client

    @cached_property
    def legacy(self) -> legacy.LegacyResourceWithStreamingResponse:
        from .resources.legacy import LegacyResourceWithStreamingResponse

        return LegacyResourceWithStreamingResponse(self._client.legacy)

    @cached_property
    def oauth(self) -> oauth.OAuthResourceWithStreamingResponse:
        from .resources.oauth import OAuthResourceWithStreamingResponse

        return OAuthResourceWithStreamingResponse(self._client.oauth)

    @cached_property
    def oauth_clients(self) -> oauth_clients.OAuthClientsResourceWithStreamingResponse:
        from .resources.oauth_clients import OAuthClientsResourceWithStreamingResponse

        return OAuthClientsResourceWithStreamingResponse(self._client.oauth_clients)

    @cached_property
    def oauth_grants(self) -> oauth_grants.OAuthGrantsResourceWithStreamingResponse:
        from .resources.oauth_grants import OAuthGrantsResourceWithStreamingResponse

        return OAuthGrantsResourceWithStreamingResponse(self._client.oauth_grants)

    @cached_property
    def access_ip_address(self) -> access_ip_address.AccessIPAddressResourceWithStreamingResponse:
        """IP Address Operations"""
        from .resources.access_ip_address import AccessIPAddressResourceWithStreamingResponse

        return AccessIPAddressResourceWithStreamingResponse(self._client.access_ip_address)

    @cached_property
    def access_ip_ranges(self) -> access_ip_ranges.AccessIPRangesResourceWithStreamingResponse:
        """IP Range Operations"""
        from .resources.access_ip_ranges import AccessIPRangesResourceWithStreamingResponse

        return AccessIPRangesResourceWithStreamingResponse(self._client.access_ip_ranges)

    @cached_property
    def actions(self) -> actions.ActionsResourceWithStreamingResponse:
        from .resources.actions import ActionsResourceWithStreamingResponse

        return ActionsResourceWithStreamingResponse(self._client.actions)

    @cached_property
    def addresses(self) -> addresses.AddressesResourceWithStreamingResponse:
        """Operations to work with Address records.

        Address records are emergency-validated addresses meant to be associated with phone numbers. They are validated for emergency usage purposes at creation time, although you may validate them separately with a custom workflow using the ValidateAddress operation separately. Address records are not usable for physical orders, such as for Telnyx SIM cards, please use UserAddress for that. It is not possible to entirely skip emergency service validation for Address records; if an emergency provider for a phone number rejects the address then it cannot be used on a phone number. To prevent records from getting out of sync, Address records are immutable and cannot be altered once created. If you realize you need to alter an address, a new record must be created with the differing address.
        """
        from .resources.addresses import AddressesResourceWithStreamingResponse

        return AddressesResourceWithStreamingResponse(self._client.addresses)

    @cached_property
    def advanced_orders(self) -> advanced_orders.AdvancedOrdersResourceWithStreamingResponse:
        from .resources.advanced_orders import AdvancedOrdersResourceWithStreamingResponse

        return AdvancedOrdersResourceWithStreamingResponse(self._client.advanced_orders)

    @cached_property
    def ai(self) -> ai.AIResourceWithStreamingResponse:
        """Generate text with LLMs"""
        from .resources.ai import AIResourceWithStreamingResponse

        return AIResourceWithStreamingResponse(self._client.ai)

    @cached_property
    def audit_events(self) -> audit_events.AuditEventsResourceWithStreamingResponse:
        """Audit log operations."""
        from .resources.audit_events import AuditEventsResourceWithStreamingResponse

        return AuditEventsResourceWithStreamingResponse(self._client.audit_events)

    @cached_property
    def authentication_providers(self) -> authentication_providers.AuthenticationProvidersResourceWithStreamingResponse:
        from .resources.authentication_providers import AuthenticationProvidersResourceWithStreamingResponse

        return AuthenticationProvidersResourceWithStreamingResponse(self._client.authentication_providers)

    @cached_property
    def available_phone_number_blocks(
        self,
    ) -> available_phone_number_blocks.AvailablePhoneNumberBlocksResourceWithStreamingResponse:
        """Number search"""
        from .resources.available_phone_number_blocks import AvailablePhoneNumberBlocksResourceWithStreamingResponse

        return AvailablePhoneNumberBlocksResourceWithStreamingResponse(self._client.available_phone_number_blocks)

    @cached_property
    def available_phone_numbers(self) -> available_phone_numbers.AvailablePhoneNumbersResourceWithStreamingResponse:
        """Number search"""
        from .resources.available_phone_numbers import AvailablePhoneNumbersResourceWithStreamingResponse

        return AvailablePhoneNumbersResourceWithStreamingResponse(self._client.available_phone_numbers)

    @cached_property
    def balance(self) -> balance.BalanceResourceWithStreamingResponse:
        """Billing operations"""
        from .resources.balance import BalanceResourceWithStreamingResponse

        return BalanceResourceWithStreamingResponse(self._client.balance)

    @cached_property
    def billing_groups(self) -> billing_groups.BillingGroupsResourceWithStreamingResponse:
        """Billing groups operations"""
        from .resources.billing_groups import BillingGroupsResourceWithStreamingResponse

        return BillingGroupsResourceWithStreamingResponse(self._client.billing_groups)

    @cached_property
    def bulk_sim_card_actions(self) -> bulk_sim_card_actions.BulkSimCardActionsResourceWithStreamingResponse:
        """
        View SIM card actions, their progress and timestamps using the SIM Card Actions API
        """
        from .resources.bulk_sim_card_actions import BulkSimCardActionsResourceWithStreamingResponse

        return BulkSimCardActionsResourceWithStreamingResponse(self._client.bulk_sim_card_actions)

    @cached_property
    def bundle_pricing(self) -> bundle_pricing.BundlePricingResourceWithStreamingResponse:
        from .resources.bundle_pricing import BundlePricingResourceWithStreamingResponse

        return BundlePricingResourceWithStreamingResponse(self._client.bundle_pricing)

    @cached_property
    def call_control_applications(
        self,
    ) -> call_control_applications.CallControlApplicationsResourceWithStreamingResponse:
        """Call Control applications operations"""
        from .resources.call_control_applications import CallControlApplicationsResourceWithStreamingResponse

        return CallControlApplicationsResourceWithStreamingResponse(self._client.call_control_applications)

    @cached_property
    def call_events(self) -> call_events.CallEventsResourceWithStreamingResponse:
        """Call Control debugging"""
        from .resources.call_events import CallEventsResourceWithStreamingResponse

        return CallEventsResourceWithStreamingResponse(self._client.call_events)

    @cached_property
    def calls(self) -> calls.CallsResourceWithStreamingResponse:
        from .resources.calls import CallsResourceWithStreamingResponse

        return CallsResourceWithStreamingResponse(self._client.calls)

    @cached_property
    def channel_zones(self) -> channel_zones.ChannelZonesResourceWithStreamingResponse:
        """Voice Channels"""
        from .resources.channel_zones import ChannelZonesResourceWithStreamingResponse

        return ChannelZonesResourceWithStreamingResponse(self._client.channel_zones)

    @cached_property
    def charges_breakdown(self) -> charges_breakdown.ChargesBreakdownResourceWithStreamingResponse:
        from .resources.charges_breakdown import ChargesBreakdownResourceWithStreamingResponse

        return ChargesBreakdownResourceWithStreamingResponse(self._client.charges_breakdown)

    @cached_property
    def charges_summary(self) -> charges_summary.ChargesSummaryResourceWithStreamingResponse:
        from .resources.charges_summary import ChargesSummaryResourceWithStreamingResponse

        return ChargesSummaryResourceWithStreamingResponse(self._client.charges_summary)

    @cached_property
    def comments(self) -> comments.CommentsResourceWithStreamingResponse:
        """Number orders"""
        from .resources.comments import CommentsResourceWithStreamingResponse

        return CommentsResourceWithStreamingResponse(self._client.comments)

    @cached_property
    def conferences(self) -> conferences.ConferencesResourceWithStreamingResponse:
        """Conference command operations"""
        from .resources.conferences import ConferencesResourceWithStreamingResponse

        return ConferencesResourceWithStreamingResponse(self._client.conferences)

    @cached_property
    def connections(self) -> connections.ConnectionsResourceWithStreamingResponse:
        from .resources.connections import ConnectionsResourceWithStreamingResponse

        return ConnectionsResourceWithStreamingResponse(self._client.connections)

    @cached_property
    def country_coverage(self) -> country_coverage.CountryCoverageResourceWithStreamingResponse:
        """Country Coverage"""
        from .resources.country_coverage import CountryCoverageResourceWithStreamingResponse

        return CountryCoverageResourceWithStreamingResponse(self._client.country_coverage)

    @cached_property
    def credential_connections(self) -> credential_connections.CredentialConnectionsResourceWithStreamingResponse:
        """Credential connection operations"""
        from .resources.credential_connections import CredentialConnectionsResourceWithStreamingResponse

        return CredentialConnectionsResourceWithStreamingResponse(self._client.credential_connections)

    @cached_property
    def custom_storage_credentials(
        self,
    ) -> custom_storage_credentials.CustomStorageCredentialsResourceWithStreamingResponse:
        """Call Recordings operations."""
        from .resources.custom_storage_credentials import CustomStorageCredentialsResourceWithStreamingResponse

        return CustomStorageCredentialsResourceWithStreamingResponse(self._client.custom_storage_credentials)

    @cached_property
    def customer_service_records(self) -> customer_service_records.CustomerServiceRecordsResourceWithStreamingResponse:
        """Customer Service Record operations"""
        from .resources.customer_service_records import CustomerServiceRecordsResourceWithStreamingResponse

        return CustomerServiceRecordsResourceWithStreamingResponse(self._client.customer_service_records)

    @cached_property
    def detail_records(self) -> detail_records.DetailRecordsResourceWithStreamingResponse:
        """Detail Records operations"""
        from .resources.detail_records import DetailRecordsResourceWithStreamingResponse

        return DetailRecordsResourceWithStreamingResponse(self._client.detail_records)

    @cached_property
    def dialogflow_connections(self) -> dialogflow_connections.DialogflowConnectionsResourceWithStreamingResponse:
        """Dialogflow Connection Operations."""
        from .resources.dialogflow_connections import DialogflowConnectionsResourceWithStreamingResponse

        return DialogflowConnectionsResourceWithStreamingResponse(self._client.dialogflow_connections)

    @cached_property
    def document_links(self) -> document_links.DocumentLinksResourceWithStreamingResponse:
        """Documents"""
        from .resources.document_links import DocumentLinksResourceWithStreamingResponse

        return DocumentLinksResourceWithStreamingResponse(self._client.document_links)

    @cached_property
    def documents(self) -> documents.DocumentsResourceWithStreamingResponse:
        """Documents"""
        from .resources.documents import DocumentsResourceWithStreamingResponse

        return DocumentsResourceWithStreamingResponse(self._client.documents)

    @cached_property
    def dynamic_emergency_addresses(
        self,
    ) -> dynamic_emergency_addresses.DynamicEmergencyAddressesResourceWithStreamingResponse:
        """Dynamic emergency address operations"""
        from .resources.dynamic_emergency_addresses import DynamicEmergencyAddressesResourceWithStreamingResponse

        return DynamicEmergencyAddressesResourceWithStreamingResponse(self._client.dynamic_emergency_addresses)

    @cached_property
    def dynamic_emergency_endpoints(
        self,
    ) -> dynamic_emergency_endpoints.DynamicEmergencyEndpointsResourceWithStreamingResponse:
        """Dynamic Emergency Endpoints"""
        from .resources.dynamic_emergency_endpoints import DynamicEmergencyEndpointsResourceWithStreamingResponse

        return DynamicEmergencyEndpointsResourceWithStreamingResponse(self._client.dynamic_emergency_endpoints)

    @cached_property
    def external_connections(self) -> external_connections.ExternalConnectionsResourceWithStreamingResponse:
        """External Connections operations"""
        from .resources.external_connections import ExternalConnectionsResourceWithStreamingResponse

        return ExternalConnectionsResourceWithStreamingResponse(self._client.external_connections)

    @cached_property
    def fax_applications(self) -> fax_applications.FaxApplicationsResourceWithStreamingResponse:
        """Fax Applications operations"""
        from .resources.fax_applications import FaxApplicationsResourceWithStreamingResponse

        return FaxApplicationsResourceWithStreamingResponse(self._client.fax_applications)

    @cached_property
    def faxes(self) -> faxes.FaxesResourceWithStreamingResponse:
        """Programmable fax command operations"""
        from .resources.faxes import FaxesResourceWithStreamingResponse

        return FaxesResourceWithStreamingResponse(self._client.faxes)

    @cached_property
    def fqdn_connections(self) -> fqdn_connections.FqdnConnectionsResourceWithStreamingResponse:
        """FQDN connection operations"""
        from .resources.fqdn_connections import FqdnConnectionsResourceWithStreamingResponse

        return FqdnConnectionsResourceWithStreamingResponse(self._client.fqdn_connections)

    @cached_property
    def fqdns(self) -> fqdns.FqdnsResourceWithStreamingResponse:
        """FQDN operations"""
        from .resources.fqdns import FqdnsResourceWithStreamingResponse

        return FqdnsResourceWithStreamingResponse(self._client.fqdns)

    @cached_property
    def global_ip_allowed_ports(self) -> global_ip_allowed_ports.GlobalIPAllowedPortsResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_allowed_ports import GlobalIPAllowedPortsResourceWithStreamingResponse

        return GlobalIPAllowedPortsResourceWithStreamingResponse(self._client.global_ip_allowed_ports)

    @cached_property
    def global_ip_assignment_health(
        self,
    ) -> global_ip_assignment_health.GlobalIPAssignmentHealthResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_assignment_health import GlobalIPAssignmentHealthResourceWithStreamingResponse

        return GlobalIPAssignmentHealthResourceWithStreamingResponse(self._client.global_ip_assignment_health)

    @cached_property
    def global_ip_assignments(self) -> global_ip_assignments.GlobalIPAssignmentsResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_assignments import GlobalIPAssignmentsResourceWithStreamingResponse

        return GlobalIPAssignmentsResourceWithStreamingResponse(self._client.global_ip_assignments)

    @cached_property
    def global_ip_assignments_usage(
        self,
    ) -> global_ip_assignments_usage.GlobalIPAssignmentsUsageResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_assignments_usage import GlobalIPAssignmentsUsageResourceWithStreamingResponse

        return GlobalIPAssignmentsUsageResourceWithStreamingResponse(self._client.global_ip_assignments_usage)

    @cached_property
    def global_ip_health_check_types(
        self,
    ) -> global_ip_health_check_types.GlobalIPHealthCheckTypesResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_health_check_types import GlobalIPHealthCheckTypesResourceWithStreamingResponse

        return GlobalIPHealthCheckTypesResourceWithStreamingResponse(self._client.global_ip_health_check_types)

    @cached_property
    def global_ip_health_checks(self) -> global_ip_health_checks.GlobalIPHealthChecksResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_health_checks import GlobalIPHealthChecksResourceWithStreamingResponse

        return GlobalIPHealthChecksResourceWithStreamingResponse(self._client.global_ip_health_checks)

    @cached_property
    def global_ip_latency(self) -> global_ip_latency.GlobalIPLatencyResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_latency import GlobalIPLatencyResourceWithStreamingResponse

        return GlobalIPLatencyResourceWithStreamingResponse(self._client.global_ip_latency)

    @cached_property
    def global_ip_protocols(self) -> global_ip_protocols.GlobalIPProtocolsResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_protocols import GlobalIPProtocolsResourceWithStreamingResponse

        return GlobalIPProtocolsResourceWithStreamingResponse(self._client.global_ip_protocols)

    @cached_property
    def global_ip_usage(self) -> global_ip_usage.GlobalIPUsageResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_usage import GlobalIPUsageResourceWithStreamingResponse

        return GlobalIPUsageResourceWithStreamingResponse(self._client.global_ip_usage)

    @cached_property
    def global_ips(self) -> global_ips.GlobalIPsResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ips import GlobalIPsResourceWithStreamingResponse

        return GlobalIPsResourceWithStreamingResponse(self._client.global_ips)

    @cached_property
    def inbound_channels(self) -> inbound_channels.InboundChannelsResourceWithStreamingResponse:
        """Voice Channels"""
        from .resources.inbound_channels import InboundChannelsResourceWithStreamingResponse

        return InboundChannelsResourceWithStreamingResponse(self._client.inbound_channels)

    @cached_property
    def integration_secrets(self) -> integration_secrets.IntegrationSecretsResourceWithStreamingResponse:
        """Store and retrieve integration secrets"""
        from .resources.integration_secrets import IntegrationSecretsResourceWithStreamingResponse

        return IntegrationSecretsResourceWithStreamingResponse(self._client.integration_secrets)

    @cached_property
    def inventory_coverage(self) -> inventory_coverage.InventoryCoverageResourceWithStreamingResponse:
        """Inventory Level"""
        from .resources.inventory_coverage import InventoryCoverageResourceWithStreamingResponse

        return InventoryCoverageResourceWithStreamingResponse(self._client.inventory_coverage)

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithStreamingResponse:
        from .resources.invoices import InvoicesResourceWithStreamingResponse

        return InvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def ip_connections(self) -> ip_connections.IPConnectionsResourceWithStreamingResponse:
        """IP connection operations"""
        from .resources.ip_connections import IPConnectionsResourceWithStreamingResponse

        return IPConnectionsResourceWithStreamingResponse(self._client.ip_connections)

    @cached_property
    def ips(self) -> ips.IPsResourceWithStreamingResponse:
        """IP operations"""
        from .resources.ips import IPsResourceWithStreamingResponse

        return IPsResourceWithStreamingResponse(self._client.ips)

    @cached_property
    def ledger_billing_group_reports(
        self,
    ) -> ledger_billing_group_reports.LedgerBillingGroupReportsResourceWithStreamingResponse:
        """Ledger billing reports"""
        from .resources.ledger_billing_group_reports import LedgerBillingGroupReportsResourceWithStreamingResponse

        return LedgerBillingGroupReportsResourceWithStreamingResponse(self._client.ledger_billing_group_reports)

    @cached_property
    def list(self) -> list.ListResourceWithStreamingResponse:
        """Voice Channels"""
        from .resources.list import ListResourceWithStreamingResponse

        return ListResourceWithStreamingResponse(self._client.list)

    @cached_property
    def managed_accounts(self) -> managed_accounts.ManagedAccountsResourceWithStreamingResponse:
        """Managed Accounts operations"""
        from .resources.managed_accounts import ManagedAccountsResourceWithStreamingResponse

        return ManagedAccountsResourceWithStreamingResponse(self._client.managed_accounts)

    @cached_property
    def media(self) -> media.MediaResourceWithStreamingResponse:
        """Media Storage operations"""
        from .resources.media import MediaResourceWithStreamingResponse

        return MediaResourceWithStreamingResponse(self._client.media)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def messaging(self) -> messaging.MessagingResourceWithStreamingResponse:
        from .resources.messaging import MessagingResourceWithStreamingResponse

        return MessagingResourceWithStreamingResponse(self._client.messaging)

    @cached_property
    def messaging_hosted_number_orders(
        self,
    ) -> messaging_hosted_number_orders.MessagingHostedNumberOrdersResourceWithStreamingResponse:
        """Manage your messaging hosted numbers"""
        from .resources.messaging_hosted_number_orders import MessagingHostedNumberOrdersResourceWithStreamingResponse

        return MessagingHostedNumberOrdersResourceWithStreamingResponse(self._client.messaging_hosted_number_orders)

    @cached_property
    def messaging_hosted_numbers(self) -> messaging_hosted_numbers.MessagingHostedNumbersResourceWithStreamingResponse:
        from .resources.messaging_hosted_numbers import MessagingHostedNumbersResourceWithStreamingResponse

        return MessagingHostedNumbersResourceWithStreamingResponse(self._client.messaging_hosted_numbers)

    @cached_property
    def messaging_numbers_bulk_updates(
        self,
    ) -> messaging_numbers_bulk_updates.MessagingNumbersBulkUpdatesResourceWithStreamingResponse:
        """Configure your phone numbers"""
        from .resources.messaging_numbers_bulk_updates import MessagingNumbersBulkUpdatesResourceWithStreamingResponse

        return MessagingNumbersBulkUpdatesResourceWithStreamingResponse(self._client.messaging_numbers_bulk_updates)

    @cached_property
    def messaging_optouts(self) -> messaging_optouts.MessagingOptoutsResourceWithStreamingResponse:
        """Opt-Out Management"""
        from .resources.messaging_optouts import MessagingOptoutsResourceWithStreamingResponse

        return MessagingOptoutsResourceWithStreamingResponse(self._client.messaging_optouts)

    @cached_property
    def messaging_profiles(self) -> messaging_profiles.MessagingProfilesResourceWithStreamingResponse:
        from .resources.messaging_profiles import MessagingProfilesResourceWithStreamingResponse

        return MessagingProfilesResourceWithStreamingResponse(self._client.messaging_profiles)

    @cached_property
    def messaging_tollfree(self) -> messaging_tollfree.MessagingTollfreeResourceWithStreamingResponse:
        from .resources.messaging_tollfree import MessagingTollfreeResourceWithStreamingResponse

        return MessagingTollfreeResourceWithStreamingResponse(self._client.messaging_tollfree)

    @cached_property
    def messaging_url_domains(self) -> messaging_url_domains.MessagingURLDomainsResourceWithStreamingResponse:
        """Messaging URL Domains"""
        from .resources.messaging_url_domains import MessagingURLDomainsResourceWithStreamingResponse

        return MessagingURLDomainsResourceWithStreamingResponse(self._client.messaging_url_domains)

    @cached_property
    def mobile_network_operators(self) -> mobile_network_operators.MobileNetworkOperatorsResourceWithStreamingResponse:
        """Mobile network operators operations"""
        from .resources.mobile_network_operators import MobileNetworkOperatorsResourceWithStreamingResponse

        return MobileNetworkOperatorsResourceWithStreamingResponse(self._client.mobile_network_operators)

    @cached_property
    def mobile_push_credentials(self) -> mobile_push_credentials.MobilePushCredentialsResourceWithStreamingResponse:
        """Mobile push credential management"""
        from .resources.mobile_push_credentials import MobilePushCredentialsResourceWithStreamingResponse

        return MobilePushCredentialsResourceWithStreamingResponse(self._client.mobile_push_credentials)

    @cached_property
    def network_coverage(self) -> network_coverage.NetworkCoverageResourceWithStreamingResponse:
        from .resources.network_coverage import NetworkCoverageResourceWithStreamingResponse

        return NetworkCoverageResourceWithStreamingResponse(self._client.network_coverage)

    @cached_property
    def networks(self) -> networks.NetworksResourceWithStreamingResponse:
        """Network operations"""
        from .resources.networks import NetworksResourceWithStreamingResponse

        return NetworksResourceWithStreamingResponse(self._client.networks)

    @cached_property
    def notification_channels(self) -> notification_channels.NotificationChannelsResourceWithStreamingResponse:
        """Notification settings operations"""
        from .resources.notification_channels import NotificationChannelsResourceWithStreamingResponse

        return NotificationChannelsResourceWithStreamingResponse(self._client.notification_channels)

    @cached_property
    def notification_event_conditions(
        self,
    ) -> notification_event_conditions.NotificationEventConditionsResourceWithStreamingResponse:
        """Notification settings operations"""
        from .resources.notification_event_conditions import NotificationEventConditionsResourceWithStreamingResponse

        return NotificationEventConditionsResourceWithStreamingResponse(self._client.notification_event_conditions)

    @cached_property
    def notification_events(self) -> notification_events.NotificationEventsResourceWithStreamingResponse:
        """Notification settings operations"""
        from .resources.notification_events import NotificationEventsResourceWithStreamingResponse

        return NotificationEventsResourceWithStreamingResponse(self._client.notification_events)

    @cached_property
    def notification_profiles(self) -> notification_profiles.NotificationProfilesResourceWithStreamingResponse:
        """Notification settings operations"""
        from .resources.notification_profiles import NotificationProfilesResourceWithStreamingResponse

        return NotificationProfilesResourceWithStreamingResponse(self._client.notification_profiles)

    @cached_property
    def notification_settings(self) -> notification_settings.NotificationSettingsResourceWithStreamingResponse:
        """Notification settings operations"""
        from .resources.notification_settings import NotificationSettingsResourceWithStreamingResponse

        return NotificationSettingsResourceWithStreamingResponse(self._client.notification_settings)

    @cached_property
    def number_block_orders(self) -> number_block_orders.NumberBlockOrdersResourceWithStreamingResponse:
        from .resources.number_block_orders import NumberBlockOrdersResourceWithStreamingResponse

        return NumberBlockOrdersResourceWithStreamingResponse(self._client.number_block_orders)

    @cached_property
    def number_lookup(self) -> number_lookup.NumberLookupResourceWithStreamingResponse:
        """Look up phone number data"""
        from .resources.number_lookup import NumberLookupResourceWithStreamingResponse

        return NumberLookupResourceWithStreamingResponse(self._client.number_lookup)

    @cached_property
    def number_order_phone_numbers(
        self,
    ) -> number_order_phone_numbers.NumberOrderPhoneNumbersResourceWithStreamingResponse:
        from .resources.number_order_phone_numbers import NumberOrderPhoneNumbersResourceWithStreamingResponse

        return NumberOrderPhoneNumbersResourceWithStreamingResponse(self._client.number_order_phone_numbers)

    @cached_property
    def number_orders(self) -> number_orders.NumberOrdersResourceWithStreamingResponse:
        """Number orders"""
        from .resources.number_orders import NumberOrdersResourceWithStreamingResponse

        return NumberOrdersResourceWithStreamingResponse(self._client.number_orders)

    @cached_property
    def number_reservations(self) -> number_reservations.NumberReservationsResourceWithStreamingResponse:
        """Number reservations"""
        from .resources.number_reservations import NumberReservationsResourceWithStreamingResponse

        return NumberReservationsResourceWithStreamingResponse(self._client.number_reservations)

    @cached_property
    def numbers_features(self) -> numbers_features.NumbersFeaturesResourceWithStreamingResponse:
        from .resources.numbers_features import NumbersFeaturesResourceWithStreamingResponse

        return NumbersFeaturesResourceWithStreamingResponse(self._client.numbers_features)

    @cached_property
    def operator_connect(self) -> operator_connect.OperatorConnectResourceWithStreamingResponse:
        from .resources.operator_connect import OperatorConnectResourceWithStreamingResponse

        return OperatorConnectResourceWithStreamingResponse(self._client.operator_connect)

    @cached_property
    def ota_updates(self) -> ota_updates.OtaUpdatesResourceWithStreamingResponse:
        """OTA updates operations"""
        from .resources.ota_updates import OtaUpdatesResourceWithStreamingResponse

        return OtaUpdatesResourceWithStreamingResponse(self._client.ota_updates)

    @cached_property
    def outbound_voice_profiles(self) -> outbound_voice_profiles.OutboundVoiceProfilesResourceWithStreamingResponse:
        """Outbound voice profiles operations"""
        from .resources.outbound_voice_profiles import OutboundVoiceProfilesResourceWithStreamingResponse

        return OutboundVoiceProfilesResourceWithStreamingResponse(self._client.outbound_voice_profiles)

    @cached_property
    def payment(self) -> payment.PaymentResourceWithStreamingResponse:
        """Operations for managing stored payment transactions."""
        from .resources.payment import PaymentResourceWithStreamingResponse

        return PaymentResourceWithStreamingResponse(self._client.payment)

    @cached_property
    def phone_number_blocks(self) -> phone_number_blocks.PhoneNumberBlocksResourceWithStreamingResponse:
        from .resources.phone_number_blocks import PhoneNumberBlocksResourceWithStreamingResponse

        return PhoneNumberBlocksResourceWithStreamingResponse(self._client.phone_number_blocks)

    @cached_property
    def phone_numbers(self) -> phone_numbers.PhoneNumbersResourceWithStreamingResponse:
        """Configure your phone numbers"""
        from .resources.phone_numbers import PhoneNumbersResourceWithStreamingResponse

        return PhoneNumbersResourceWithStreamingResponse(self._client.phone_numbers)

    @cached_property
    def phone_numbers_regulatory_requirements(
        self,
    ) -> phone_numbers_regulatory_requirements.PhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse:
        """Regulatory Requirements"""
        from .resources.phone_numbers_regulatory_requirements import (
            PhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse,
        )

        return PhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse(
            self._client.phone_numbers_regulatory_requirements
        )

    @cached_property
    def portability_checks(self) -> portability_checks.PortabilityChecksResourceWithStreamingResponse:
        """Determining portability of phone numbers"""
        from .resources.portability_checks import PortabilityChecksResourceWithStreamingResponse

        return PortabilityChecksResourceWithStreamingResponse(self._client.portability_checks)

    @cached_property
    def porting(self) -> porting.PortingResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting import PortingResourceWithStreamingResponse

        return PortingResourceWithStreamingResponse(self._client.porting)

    @cached_property
    def porting_orders(self) -> porting_orders.PortingOrdersResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting_orders import PortingOrdersResourceWithStreamingResponse

        return PortingOrdersResourceWithStreamingResponse(self._client.porting_orders)

    @cached_property
    def porting_phone_numbers(self) -> porting_phone_numbers.PortingPhoneNumbersResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting_phone_numbers import PortingPhoneNumbersResourceWithStreamingResponse

        return PortingPhoneNumbersResourceWithStreamingResponse(self._client.porting_phone_numbers)

    @cached_property
    def portouts(self) -> portouts.PortoutsResourceWithStreamingResponse:
        """Number portout operations"""
        from .resources.portouts import PortoutsResourceWithStreamingResponse

        return PortoutsResourceWithStreamingResponse(self._client.portouts)

    @cached_property
    def private_wireless_gateways(
        self,
    ) -> private_wireless_gateways.PrivateWirelessGatewaysResourceWithStreamingResponse:
        """Private Wireless Gateways operations"""
        from .resources.private_wireless_gateways import PrivateWirelessGatewaysResourceWithStreamingResponse

        return PrivateWirelessGatewaysResourceWithStreamingResponse(self._client.private_wireless_gateways)

    @cached_property
    def public_internet_gateways(self) -> public_internet_gateways.PublicInternetGatewaysResourceWithStreamingResponse:
        """Public Internet Gateway operations"""
        from .resources.public_internet_gateways import PublicInternetGatewaysResourceWithStreamingResponse

        return PublicInternetGatewaysResourceWithStreamingResponse(self._client.public_internet_gateways)

    @cached_property
    def queues(self) -> queues.QueuesResourceWithStreamingResponse:
        """Queue commands operations"""
        from .resources.queues import QueuesResourceWithStreamingResponse

        return QueuesResourceWithStreamingResponse(self._client.queues)

    @cached_property
    def recording_transcriptions(self) -> recording_transcriptions.RecordingTranscriptionsResourceWithStreamingResponse:
        """Call Recordings operations."""
        from .resources.recording_transcriptions import RecordingTranscriptionsResourceWithStreamingResponse

        return RecordingTranscriptionsResourceWithStreamingResponse(self._client.recording_transcriptions)

    @cached_property
    def recordings(self) -> recordings.RecordingsResourceWithStreamingResponse:
        """Call Recordings operations."""
        from .resources.recordings import RecordingsResourceWithStreamingResponse

        return RecordingsResourceWithStreamingResponse(self._client.recordings)

    @cached_property
    def regions(self) -> regions.RegionsResourceWithStreamingResponse:
        """Regions"""
        from .resources.regions import RegionsResourceWithStreamingResponse

        return RegionsResourceWithStreamingResponse(self._client.regions)

    @cached_property
    def regulatory_requirements(self) -> regulatory_requirements.RegulatoryRequirementsResourceWithStreamingResponse:
        """Regulatory Requirements"""
        from .resources.regulatory_requirements import RegulatoryRequirementsResourceWithStreamingResponse

        return RegulatoryRequirementsResourceWithStreamingResponse(self._client.regulatory_requirements)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithStreamingResponse:
        from .resources.reports import ReportsResourceWithStreamingResponse

        return ReportsResourceWithStreamingResponse(self._client.reports)

    @cached_property
    def requirement_groups(self) -> requirement_groups.RequirementGroupsResourceWithStreamingResponse:
        """Requirement Groups"""
        from .resources.requirement_groups import RequirementGroupsResourceWithStreamingResponse

        return RequirementGroupsResourceWithStreamingResponse(self._client.requirement_groups)

    @cached_property
    def requirement_types(self) -> requirement_types.RequirementTypesResourceWithStreamingResponse:
        """Types of requirements for international numbers and porting orders"""
        from .resources.requirement_types import RequirementTypesResourceWithStreamingResponse

        return RequirementTypesResourceWithStreamingResponse(self._client.requirement_types)

    @cached_property
    def requirements(self) -> requirements.RequirementsResourceWithStreamingResponse:
        """Requirements for international numbers and porting orders"""
        from .resources.requirements import RequirementsResourceWithStreamingResponse

        return RequirementsResourceWithStreamingResponse(self._client.requirements)

    @cached_property
    def room_compositions(self) -> room_compositions.RoomCompositionsResourceWithStreamingResponse:
        """Rooms Compositions operations."""
        from .resources.room_compositions import RoomCompositionsResourceWithStreamingResponse

        return RoomCompositionsResourceWithStreamingResponse(self._client.room_compositions)

    @cached_property
    def room_participants(self) -> room_participants.RoomParticipantsResourceWithStreamingResponse:
        """Rooms Participants operations."""
        from .resources.room_participants import RoomParticipantsResourceWithStreamingResponse

        return RoomParticipantsResourceWithStreamingResponse(self._client.room_participants)

    @cached_property
    def room_recordings(self) -> room_recordings.RoomRecordingsResourceWithStreamingResponse:
        """Rooms Recordings operations."""
        from .resources.room_recordings import RoomRecordingsResourceWithStreamingResponse

        return RoomRecordingsResourceWithStreamingResponse(self._client.room_recordings)

    @cached_property
    def rooms(self) -> rooms.RoomsResourceWithStreamingResponse:
        """Rooms operations."""
        from .resources.rooms import RoomsResourceWithStreamingResponse

        return RoomsResourceWithStreamingResponse(self._client.rooms)

    @cached_property
    def seti(self) -> seti.SetiResourceWithStreamingResponse:
        """Observability into Telnyx platform stability and performance."""
        from .resources.seti import SetiResourceWithStreamingResponse

        return SetiResourceWithStreamingResponse(self._client.seti)

    @cached_property
    def short_codes(self) -> short_codes.ShortCodesResourceWithStreamingResponse:
        """Short codes"""
        from .resources.short_codes import ShortCodesResourceWithStreamingResponse

        return ShortCodesResourceWithStreamingResponse(self._client.short_codes)

    @cached_property
    def sim_card_data_usage_notifications(
        self,
    ) -> sim_card_data_usage_notifications.SimCardDataUsageNotificationsResourceWithStreamingResponse:
        """SIM Cards operations"""
        from .resources.sim_card_data_usage_notifications import (
            SimCardDataUsageNotificationsResourceWithStreamingResponse,
        )

        return SimCardDataUsageNotificationsResourceWithStreamingResponse(
            self._client.sim_card_data_usage_notifications
        )

    @cached_property
    def sim_card_groups(self) -> sim_card_groups.SimCardGroupsResourceWithStreamingResponse:
        """SIM Card Groups operations"""
        from .resources.sim_card_groups import SimCardGroupsResourceWithStreamingResponse

        return SimCardGroupsResourceWithStreamingResponse(self._client.sim_card_groups)

    @cached_property
    def sim_card_order_preview(self) -> sim_card_order_preview.SimCardOrderPreviewResourceWithStreamingResponse:
        """SIM Card Orders operations"""
        from .resources.sim_card_order_preview import SimCardOrderPreviewResourceWithStreamingResponse

        return SimCardOrderPreviewResourceWithStreamingResponse(self._client.sim_card_order_preview)

    @cached_property
    def sim_card_orders(self) -> sim_card_orders.SimCardOrdersResourceWithStreamingResponse:
        """SIM Card Orders operations"""
        from .resources.sim_card_orders import SimCardOrdersResourceWithStreamingResponse

        return SimCardOrdersResourceWithStreamingResponse(self._client.sim_card_orders)

    @cached_property
    def sim_cards(self) -> sim_cards.SimCardsResourceWithStreamingResponse:
        """SIM Cards operations"""
        from .resources.sim_cards import SimCardsResourceWithStreamingResponse

        return SimCardsResourceWithStreamingResponse(self._client.sim_cards)

    @cached_property
    def siprec_connectors(self) -> siprec_connectors.SiprecConnectorsResourceWithStreamingResponse:
        """SIPREC connectors configuration."""
        from .resources.siprec_connectors import SiprecConnectorsResourceWithStreamingResponse

        return SiprecConnectorsResourceWithStreamingResponse(self._client.siprec_connectors)

    @cached_property
    def storage(self) -> storage.StorageResourceWithStreamingResponse:
        """Migrate data from an external provider into Telnyx Cloud Storage"""
        from .resources.storage import StorageResourceWithStreamingResponse

        return StorageResourceWithStreamingResponse(self._client.storage)

    @cached_property
    def sub_number_orders(self) -> sub_number_orders.SubNumberOrdersResourceWithStreamingResponse:
        from .resources.sub_number_orders import SubNumberOrdersResourceWithStreamingResponse

        return SubNumberOrdersResourceWithStreamingResponse(self._client.sub_number_orders)

    @cached_property
    def sub_number_orders_report(self) -> sub_number_orders_report.SubNumberOrdersReportResourceWithStreamingResponse:
        """Number orders"""
        from .resources.sub_number_orders_report import SubNumberOrdersReportResourceWithStreamingResponse

        return SubNumberOrdersReportResourceWithStreamingResponse(self._client.sub_number_orders_report)

    @cached_property
    def telephony_credentials(self) -> telephony_credentials.TelephonyCredentialsResourceWithStreamingResponse:
        from .resources.telephony_credentials import TelephonyCredentialsResourceWithStreamingResponse

        return TelephonyCredentialsResourceWithStreamingResponse(self._client.telephony_credentials)

    @cached_property
    def texml(self) -> texml.TexmlResourceWithStreamingResponse:
        """TeXML REST Commands"""
        from .resources.texml import TexmlResourceWithStreamingResponse

        return TexmlResourceWithStreamingResponse(self._client.texml)

    @cached_property
    def texml_applications(self) -> texml_applications.TexmlApplicationsResourceWithStreamingResponse:
        """TeXML Applications operations"""
        from .resources.texml_applications import TexmlApplicationsResourceWithStreamingResponse

        return TexmlApplicationsResourceWithStreamingResponse(self._client.texml_applications)

    @cached_property
    def text_to_speech(self) -> text_to_speech.TextToSpeechResourceWithStreamingResponse:
        """Text to speech streaming command operations"""
        from .resources.text_to_speech import TextToSpeechResourceWithStreamingResponse

        return TextToSpeechResourceWithStreamingResponse(self._client.text_to_speech)

    @cached_property
    def usage_reports(self) -> usage_reports.UsageReportsResourceWithStreamingResponse:
        """Usage data reporting across Telnyx products"""
        from .resources.usage_reports import UsageReportsResourceWithStreamingResponse

        return UsageReportsResourceWithStreamingResponse(self._client.usage_reports)

    @cached_property
    def user_addresses(self) -> user_addresses.UserAddressesResourceWithStreamingResponse:
        """Operations for working with UserAddress records.

        UserAddress records are stored addresses that users can use for non-emergency-calling purposes, such as for shipping addresses for orders of wireless SIMs (or other physical items). They cannot be used for emergency calling and are distinct from Address records, which are used on phone numbers.
        """
        from .resources.user_addresses import UserAddressesResourceWithStreamingResponse

        return UserAddressesResourceWithStreamingResponse(self._client.user_addresses)

    @cached_property
    def user_tags(self) -> user_tags.UserTagsResourceWithStreamingResponse:
        """User-defined tags for Telnyx resources"""
        from .resources.user_tags import UserTagsResourceWithStreamingResponse

        return UserTagsResourceWithStreamingResponse(self._client.user_tags)

    @cached_property
    def verifications(self) -> verifications.VerificationsResourceWithStreamingResponse:
        """Two factor authentication API"""
        from .resources.verifications import VerificationsResourceWithStreamingResponse

        return VerificationsResourceWithStreamingResponse(self._client.verifications)

    @cached_property
    def verified_numbers(self) -> verified_numbers.VerifiedNumbersResourceWithStreamingResponse:
        """Verified Numbers operations"""
        from .resources.verified_numbers import VerifiedNumbersResourceWithStreamingResponse

        return VerifiedNumbersResourceWithStreamingResponse(self._client.verified_numbers)

    @cached_property
    def verify_profiles(self) -> verify_profiles.VerifyProfilesResourceWithStreamingResponse:
        """Two factor authentication API"""
        from .resources.verify_profiles import VerifyProfilesResourceWithStreamingResponse

        return VerifyProfilesResourceWithStreamingResponse(self._client.verify_profiles)

    @cached_property
    def virtual_cross_connects(self) -> virtual_cross_connects.VirtualCrossConnectsResourceWithStreamingResponse:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects import VirtualCrossConnectsResourceWithStreamingResponse

        return VirtualCrossConnectsResourceWithStreamingResponse(self._client.virtual_cross_connects)

    @cached_property
    def virtual_cross_connects_coverage(
        self,
    ) -> virtual_cross_connects_coverage.VirtualCrossConnectsCoverageResourceWithStreamingResponse:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects_coverage import VirtualCrossConnectsCoverageResourceWithStreamingResponse

        return VirtualCrossConnectsCoverageResourceWithStreamingResponse(self._client.virtual_cross_connects_coverage)

    @cached_property
    def webhook_deliveries(self) -> webhook_deliveries.WebhookDeliveriesResourceWithStreamingResponse:
        """Webhooks operations"""
        from .resources.webhook_deliveries import WebhookDeliveriesResourceWithStreamingResponse

        return WebhookDeliveriesResourceWithStreamingResponse(self._client.webhook_deliveries)

    @cached_property
    def wireguard_interfaces(self) -> wireguard_interfaces.WireguardInterfacesResourceWithStreamingResponse:
        """WireGuard Interface operations"""
        from .resources.wireguard_interfaces import WireguardInterfacesResourceWithStreamingResponse

        return WireguardInterfacesResourceWithStreamingResponse(self._client.wireguard_interfaces)

    @cached_property
    def wireguard_peers(self) -> wireguard_peers.WireguardPeersResourceWithStreamingResponse:
        """WireGuard Interface operations"""
        from .resources.wireguard_peers import WireguardPeersResourceWithStreamingResponse

        return WireguardPeersResourceWithStreamingResponse(self._client.wireguard_peers)

    @cached_property
    def wireless(self) -> wireless.WirelessResourceWithStreamingResponse:
        """Regions for wireless services"""
        from .resources.wireless import WirelessResourceWithStreamingResponse

        return WirelessResourceWithStreamingResponse(self._client.wireless)

    @cached_property
    def wireless_blocklist_values(
        self,
    ) -> wireless_blocklist_values.WirelessBlocklistValuesResourceWithStreamingResponse:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklist_values import WirelessBlocklistValuesResourceWithStreamingResponse

        return WirelessBlocklistValuesResourceWithStreamingResponse(self._client.wireless_blocklist_values)

    @cached_property
    def wireless_blocklists(self) -> wireless_blocklists.WirelessBlocklistsResourceWithStreamingResponse:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklists import WirelessBlocklistsResourceWithStreamingResponse

        return WirelessBlocklistsResourceWithStreamingResponse(self._client.wireless_blocklists)

    @cached_property
    def well_known(self) -> well_known.WellKnownResourceWithStreamingResponse:
        from .resources.well_known import WellKnownResourceWithStreamingResponse

        return WellKnownResourceWithStreamingResponse(self._client.well_known)

    @cached_property
    def inexplicit_number_orders(self) -> inexplicit_number_orders.InexplicitNumberOrdersResourceWithStreamingResponse:
        """Inexplicit number orders for bulk purchasing without specifying exact numbers"""
        from .resources.inexplicit_number_orders import InexplicitNumberOrdersResourceWithStreamingResponse

        return InexplicitNumberOrdersResourceWithStreamingResponse(self._client.inexplicit_number_orders)

    @cached_property
    def mobile_phone_numbers(self) -> mobile_phone_numbers.MobilePhoneNumbersResourceWithStreamingResponse:
        """Mobile phone number operations"""
        from .resources.mobile_phone_numbers import MobilePhoneNumbersResourceWithStreamingResponse

        return MobilePhoneNumbersResourceWithStreamingResponse(self._client.mobile_phone_numbers)

    @cached_property
    def mobile_voice_connections(self) -> mobile_voice_connections.MobileVoiceConnectionsResourceWithStreamingResponse:
        """Mobile voice connection operations"""
        from .resources.mobile_voice_connections import MobileVoiceConnectionsResourceWithStreamingResponse

        return MobileVoiceConnectionsResourceWithStreamingResponse(self._client.mobile_voice_connections)

    @cached_property
    def messaging_10dlc(self) -> messaging_10dlc.Messaging10dlcResourceWithStreamingResponse:
        from .resources.messaging_10dlc import Messaging10dlcResourceWithStreamingResponse

        return Messaging10dlcResourceWithStreamingResponse(self._client.messaging_10dlc)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        from .resources.organizations import OrganizationsResourceWithStreamingResponse

        return OrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def alphanumeric_sender_ids(self) -> alphanumeric_sender_ids.AlphanumericSenderIDsResourceWithStreamingResponse:
        from .resources.alphanumeric_sender_ids import AlphanumericSenderIDsResourceWithStreamingResponse

        return AlphanumericSenderIDsResourceWithStreamingResponse(self._client.alphanumeric_sender_ids)

    @cached_property
    def messaging_profile_metrics(
        self,
    ) -> messaging_profile_metrics.MessagingProfileMetricsResourceWithStreamingResponse:
        from .resources.messaging_profile_metrics import MessagingProfileMetricsResourceWithStreamingResponse

        return MessagingProfileMetricsResourceWithStreamingResponse(self._client.messaging_profile_metrics)

    @cached_property
    def session_analysis(self) -> session_analysis.SessionAnalysisResourceWithStreamingResponse:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        from .resources.session_analysis import SessionAnalysisResourceWithStreamingResponse

        return SessionAnalysisResourceWithStreamingResponse(self._client.session_analysis)


class AsyncTelnyxWithStreamedResponse:
    _client: AsyncTelnyx

    def __init__(self, client: AsyncTelnyx) -> None:
        self._client = client

    @cached_property
    def legacy(self) -> legacy.AsyncLegacyResourceWithStreamingResponse:
        from .resources.legacy import AsyncLegacyResourceWithStreamingResponse

        return AsyncLegacyResourceWithStreamingResponse(self._client.legacy)

    @cached_property
    def oauth(self) -> oauth.AsyncOAuthResourceWithStreamingResponse:
        from .resources.oauth import AsyncOAuthResourceWithStreamingResponse

        return AsyncOAuthResourceWithStreamingResponse(self._client.oauth)

    @cached_property
    def oauth_clients(self) -> oauth_clients.AsyncOAuthClientsResourceWithStreamingResponse:
        from .resources.oauth_clients import AsyncOAuthClientsResourceWithStreamingResponse

        return AsyncOAuthClientsResourceWithStreamingResponse(self._client.oauth_clients)

    @cached_property
    def oauth_grants(self) -> oauth_grants.AsyncOAuthGrantsResourceWithStreamingResponse:
        from .resources.oauth_grants import AsyncOAuthGrantsResourceWithStreamingResponse

        return AsyncOAuthGrantsResourceWithStreamingResponse(self._client.oauth_grants)

    @cached_property
    def access_ip_address(self) -> access_ip_address.AsyncAccessIPAddressResourceWithStreamingResponse:
        """IP Address Operations"""
        from .resources.access_ip_address import AsyncAccessIPAddressResourceWithStreamingResponse

        return AsyncAccessIPAddressResourceWithStreamingResponse(self._client.access_ip_address)

    @cached_property
    def access_ip_ranges(self) -> access_ip_ranges.AsyncAccessIPRangesResourceWithStreamingResponse:
        """IP Range Operations"""
        from .resources.access_ip_ranges import AsyncAccessIPRangesResourceWithStreamingResponse

        return AsyncAccessIPRangesResourceWithStreamingResponse(self._client.access_ip_ranges)

    @cached_property
    def actions(self) -> actions.AsyncActionsResourceWithStreamingResponse:
        from .resources.actions import AsyncActionsResourceWithStreamingResponse

        return AsyncActionsResourceWithStreamingResponse(self._client.actions)

    @cached_property
    def addresses(self) -> addresses.AsyncAddressesResourceWithStreamingResponse:
        """Operations to work with Address records.

        Address records are emergency-validated addresses meant to be associated with phone numbers. They are validated for emergency usage purposes at creation time, although you may validate them separately with a custom workflow using the ValidateAddress operation separately. Address records are not usable for physical orders, such as for Telnyx SIM cards, please use UserAddress for that. It is not possible to entirely skip emergency service validation for Address records; if an emergency provider for a phone number rejects the address then it cannot be used on a phone number. To prevent records from getting out of sync, Address records are immutable and cannot be altered once created. If you realize you need to alter an address, a new record must be created with the differing address.
        """
        from .resources.addresses import AsyncAddressesResourceWithStreamingResponse

        return AsyncAddressesResourceWithStreamingResponse(self._client.addresses)

    @cached_property
    def advanced_orders(self) -> advanced_orders.AsyncAdvancedOrdersResourceWithStreamingResponse:
        from .resources.advanced_orders import AsyncAdvancedOrdersResourceWithStreamingResponse

        return AsyncAdvancedOrdersResourceWithStreamingResponse(self._client.advanced_orders)

    @cached_property
    def ai(self) -> ai.AsyncAIResourceWithStreamingResponse:
        """Generate text with LLMs"""
        from .resources.ai import AsyncAIResourceWithStreamingResponse

        return AsyncAIResourceWithStreamingResponse(self._client.ai)

    @cached_property
    def audit_events(self) -> audit_events.AsyncAuditEventsResourceWithStreamingResponse:
        """Audit log operations."""
        from .resources.audit_events import AsyncAuditEventsResourceWithStreamingResponse

        return AsyncAuditEventsResourceWithStreamingResponse(self._client.audit_events)

    @cached_property
    def authentication_providers(
        self,
    ) -> authentication_providers.AsyncAuthenticationProvidersResourceWithStreamingResponse:
        from .resources.authentication_providers import AsyncAuthenticationProvidersResourceWithStreamingResponse

        return AsyncAuthenticationProvidersResourceWithStreamingResponse(self._client.authentication_providers)

    @cached_property
    def available_phone_number_blocks(
        self,
    ) -> available_phone_number_blocks.AsyncAvailablePhoneNumberBlocksResourceWithStreamingResponse:
        """Number search"""
        from .resources.available_phone_number_blocks import (
            AsyncAvailablePhoneNumberBlocksResourceWithStreamingResponse,
        )

        return AsyncAvailablePhoneNumberBlocksResourceWithStreamingResponse(self._client.available_phone_number_blocks)

    @cached_property
    def available_phone_numbers(
        self,
    ) -> available_phone_numbers.AsyncAvailablePhoneNumbersResourceWithStreamingResponse:
        """Number search"""
        from .resources.available_phone_numbers import AsyncAvailablePhoneNumbersResourceWithStreamingResponse

        return AsyncAvailablePhoneNumbersResourceWithStreamingResponse(self._client.available_phone_numbers)

    @cached_property
    def balance(self) -> balance.AsyncBalanceResourceWithStreamingResponse:
        """Billing operations"""
        from .resources.balance import AsyncBalanceResourceWithStreamingResponse

        return AsyncBalanceResourceWithStreamingResponse(self._client.balance)

    @cached_property
    def billing_groups(self) -> billing_groups.AsyncBillingGroupsResourceWithStreamingResponse:
        """Billing groups operations"""
        from .resources.billing_groups import AsyncBillingGroupsResourceWithStreamingResponse

        return AsyncBillingGroupsResourceWithStreamingResponse(self._client.billing_groups)

    @cached_property
    def bulk_sim_card_actions(self) -> bulk_sim_card_actions.AsyncBulkSimCardActionsResourceWithStreamingResponse:
        """
        View SIM card actions, their progress and timestamps using the SIM Card Actions API
        """
        from .resources.bulk_sim_card_actions import AsyncBulkSimCardActionsResourceWithStreamingResponse

        return AsyncBulkSimCardActionsResourceWithStreamingResponse(self._client.bulk_sim_card_actions)

    @cached_property
    def bundle_pricing(self) -> bundle_pricing.AsyncBundlePricingResourceWithStreamingResponse:
        from .resources.bundle_pricing import AsyncBundlePricingResourceWithStreamingResponse

        return AsyncBundlePricingResourceWithStreamingResponse(self._client.bundle_pricing)

    @cached_property
    def call_control_applications(
        self,
    ) -> call_control_applications.AsyncCallControlApplicationsResourceWithStreamingResponse:
        """Call Control applications operations"""
        from .resources.call_control_applications import AsyncCallControlApplicationsResourceWithStreamingResponse

        return AsyncCallControlApplicationsResourceWithStreamingResponse(self._client.call_control_applications)

    @cached_property
    def call_events(self) -> call_events.AsyncCallEventsResourceWithStreamingResponse:
        """Call Control debugging"""
        from .resources.call_events import AsyncCallEventsResourceWithStreamingResponse

        return AsyncCallEventsResourceWithStreamingResponse(self._client.call_events)

    @cached_property
    def calls(self) -> calls.AsyncCallsResourceWithStreamingResponse:
        from .resources.calls import AsyncCallsResourceWithStreamingResponse

        return AsyncCallsResourceWithStreamingResponse(self._client.calls)

    @cached_property
    def channel_zones(self) -> channel_zones.AsyncChannelZonesResourceWithStreamingResponse:
        """Voice Channels"""
        from .resources.channel_zones import AsyncChannelZonesResourceWithStreamingResponse

        return AsyncChannelZonesResourceWithStreamingResponse(self._client.channel_zones)

    @cached_property
    def charges_breakdown(self) -> charges_breakdown.AsyncChargesBreakdownResourceWithStreamingResponse:
        from .resources.charges_breakdown import AsyncChargesBreakdownResourceWithStreamingResponse

        return AsyncChargesBreakdownResourceWithStreamingResponse(self._client.charges_breakdown)

    @cached_property
    def charges_summary(self) -> charges_summary.AsyncChargesSummaryResourceWithStreamingResponse:
        from .resources.charges_summary import AsyncChargesSummaryResourceWithStreamingResponse

        return AsyncChargesSummaryResourceWithStreamingResponse(self._client.charges_summary)

    @cached_property
    def comments(self) -> comments.AsyncCommentsResourceWithStreamingResponse:
        """Number orders"""
        from .resources.comments import AsyncCommentsResourceWithStreamingResponse

        return AsyncCommentsResourceWithStreamingResponse(self._client.comments)

    @cached_property
    def conferences(self) -> conferences.AsyncConferencesResourceWithStreamingResponse:
        """Conference command operations"""
        from .resources.conferences import AsyncConferencesResourceWithStreamingResponse

        return AsyncConferencesResourceWithStreamingResponse(self._client.conferences)

    @cached_property
    def connections(self) -> connections.AsyncConnectionsResourceWithStreamingResponse:
        from .resources.connections import AsyncConnectionsResourceWithStreamingResponse

        return AsyncConnectionsResourceWithStreamingResponse(self._client.connections)

    @cached_property
    def country_coverage(self) -> country_coverage.AsyncCountryCoverageResourceWithStreamingResponse:
        """Country Coverage"""
        from .resources.country_coverage import AsyncCountryCoverageResourceWithStreamingResponse

        return AsyncCountryCoverageResourceWithStreamingResponse(self._client.country_coverage)

    @cached_property
    def credential_connections(self) -> credential_connections.AsyncCredentialConnectionsResourceWithStreamingResponse:
        """Credential connection operations"""
        from .resources.credential_connections import AsyncCredentialConnectionsResourceWithStreamingResponse

        return AsyncCredentialConnectionsResourceWithStreamingResponse(self._client.credential_connections)

    @cached_property
    def custom_storage_credentials(
        self,
    ) -> custom_storage_credentials.AsyncCustomStorageCredentialsResourceWithStreamingResponse:
        """Call Recordings operations."""
        from .resources.custom_storage_credentials import AsyncCustomStorageCredentialsResourceWithStreamingResponse

        return AsyncCustomStorageCredentialsResourceWithStreamingResponse(self._client.custom_storage_credentials)

    @cached_property
    def customer_service_records(
        self,
    ) -> customer_service_records.AsyncCustomerServiceRecordsResourceWithStreamingResponse:
        """Customer Service Record operations"""
        from .resources.customer_service_records import AsyncCustomerServiceRecordsResourceWithStreamingResponse

        return AsyncCustomerServiceRecordsResourceWithStreamingResponse(self._client.customer_service_records)

    @cached_property
    def detail_records(self) -> detail_records.AsyncDetailRecordsResourceWithStreamingResponse:
        """Detail Records operations"""
        from .resources.detail_records import AsyncDetailRecordsResourceWithStreamingResponse

        return AsyncDetailRecordsResourceWithStreamingResponse(self._client.detail_records)

    @cached_property
    def dialogflow_connections(self) -> dialogflow_connections.AsyncDialogflowConnectionsResourceWithStreamingResponse:
        """Dialogflow Connection Operations."""
        from .resources.dialogflow_connections import AsyncDialogflowConnectionsResourceWithStreamingResponse

        return AsyncDialogflowConnectionsResourceWithStreamingResponse(self._client.dialogflow_connections)

    @cached_property
    def document_links(self) -> document_links.AsyncDocumentLinksResourceWithStreamingResponse:
        """Documents"""
        from .resources.document_links import AsyncDocumentLinksResourceWithStreamingResponse

        return AsyncDocumentLinksResourceWithStreamingResponse(self._client.document_links)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsResourceWithStreamingResponse:
        """Documents"""
        from .resources.documents import AsyncDocumentsResourceWithStreamingResponse

        return AsyncDocumentsResourceWithStreamingResponse(self._client.documents)

    @cached_property
    def dynamic_emergency_addresses(
        self,
    ) -> dynamic_emergency_addresses.AsyncDynamicEmergencyAddressesResourceWithStreamingResponse:
        """Dynamic emergency address operations"""
        from .resources.dynamic_emergency_addresses import AsyncDynamicEmergencyAddressesResourceWithStreamingResponse

        return AsyncDynamicEmergencyAddressesResourceWithStreamingResponse(self._client.dynamic_emergency_addresses)

    @cached_property
    def dynamic_emergency_endpoints(
        self,
    ) -> dynamic_emergency_endpoints.AsyncDynamicEmergencyEndpointsResourceWithStreamingResponse:
        """Dynamic Emergency Endpoints"""
        from .resources.dynamic_emergency_endpoints import AsyncDynamicEmergencyEndpointsResourceWithStreamingResponse

        return AsyncDynamicEmergencyEndpointsResourceWithStreamingResponse(self._client.dynamic_emergency_endpoints)

    @cached_property
    def external_connections(self) -> external_connections.AsyncExternalConnectionsResourceWithStreamingResponse:
        """External Connections operations"""
        from .resources.external_connections import AsyncExternalConnectionsResourceWithStreamingResponse

        return AsyncExternalConnectionsResourceWithStreamingResponse(self._client.external_connections)

    @cached_property
    def fax_applications(self) -> fax_applications.AsyncFaxApplicationsResourceWithStreamingResponse:
        """Fax Applications operations"""
        from .resources.fax_applications import AsyncFaxApplicationsResourceWithStreamingResponse

        return AsyncFaxApplicationsResourceWithStreamingResponse(self._client.fax_applications)

    @cached_property
    def faxes(self) -> faxes.AsyncFaxesResourceWithStreamingResponse:
        """Programmable fax command operations"""
        from .resources.faxes import AsyncFaxesResourceWithStreamingResponse

        return AsyncFaxesResourceWithStreamingResponse(self._client.faxes)

    @cached_property
    def fqdn_connections(self) -> fqdn_connections.AsyncFqdnConnectionsResourceWithStreamingResponse:
        """FQDN connection operations"""
        from .resources.fqdn_connections import AsyncFqdnConnectionsResourceWithStreamingResponse

        return AsyncFqdnConnectionsResourceWithStreamingResponse(self._client.fqdn_connections)

    @cached_property
    def fqdns(self) -> fqdns.AsyncFqdnsResourceWithStreamingResponse:
        """FQDN operations"""
        from .resources.fqdns import AsyncFqdnsResourceWithStreamingResponse

        return AsyncFqdnsResourceWithStreamingResponse(self._client.fqdns)

    @cached_property
    def global_ip_allowed_ports(self) -> global_ip_allowed_ports.AsyncGlobalIPAllowedPortsResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_allowed_ports import AsyncGlobalIPAllowedPortsResourceWithStreamingResponse

        return AsyncGlobalIPAllowedPortsResourceWithStreamingResponse(self._client.global_ip_allowed_ports)

    @cached_property
    def global_ip_assignment_health(
        self,
    ) -> global_ip_assignment_health.AsyncGlobalIPAssignmentHealthResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_assignment_health import AsyncGlobalIPAssignmentHealthResourceWithStreamingResponse

        return AsyncGlobalIPAssignmentHealthResourceWithStreamingResponse(self._client.global_ip_assignment_health)

    @cached_property
    def global_ip_assignments(self) -> global_ip_assignments.AsyncGlobalIPAssignmentsResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_assignments import AsyncGlobalIPAssignmentsResourceWithStreamingResponse

        return AsyncGlobalIPAssignmentsResourceWithStreamingResponse(self._client.global_ip_assignments)

    @cached_property
    def global_ip_assignments_usage(
        self,
    ) -> global_ip_assignments_usage.AsyncGlobalIPAssignmentsUsageResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_assignments_usage import AsyncGlobalIPAssignmentsUsageResourceWithStreamingResponse

        return AsyncGlobalIPAssignmentsUsageResourceWithStreamingResponse(self._client.global_ip_assignments_usage)

    @cached_property
    def global_ip_health_check_types(
        self,
    ) -> global_ip_health_check_types.AsyncGlobalIPHealthCheckTypesResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_health_check_types import AsyncGlobalIPHealthCheckTypesResourceWithStreamingResponse

        return AsyncGlobalIPHealthCheckTypesResourceWithStreamingResponse(self._client.global_ip_health_check_types)

    @cached_property
    def global_ip_health_checks(self) -> global_ip_health_checks.AsyncGlobalIPHealthChecksResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_health_checks import AsyncGlobalIPHealthChecksResourceWithStreamingResponse

        return AsyncGlobalIPHealthChecksResourceWithStreamingResponse(self._client.global_ip_health_checks)

    @cached_property
    def global_ip_latency(self) -> global_ip_latency.AsyncGlobalIPLatencyResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_latency import AsyncGlobalIPLatencyResourceWithStreamingResponse

        return AsyncGlobalIPLatencyResourceWithStreamingResponse(self._client.global_ip_latency)

    @cached_property
    def global_ip_protocols(self) -> global_ip_protocols.AsyncGlobalIPProtocolsResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_protocols import AsyncGlobalIPProtocolsResourceWithStreamingResponse

        return AsyncGlobalIPProtocolsResourceWithStreamingResponse(self._client.global_ip_protocols)

    @cached_property
    def global_ip_usage(self) -> global_ip_usage.AsyncGlobalIPUsageResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ip_usage import AsyncGlobalIPUsageResourceWithStreamingResponse

        return AsyncGlobalIPUsageResourceWithStreamingResponse(self._client.global_ip_usage)

    @cached_property
    def global_ips(self) -> global_ips.AsyncGlobalIPsResourceWithStreamingResponse:
        """Global IPs"""
        from .resources.global_ips import AsyncGlobalIPsResourceWithStreamingResponse

        return AsyncGlobalIPsResourceWithStreamingResponse(self._client.global_ips)

    @cached_property
    def inbound_channels(self) -> inbound_channels.AsyncInboundChannelsResourceWithStreamingResponse:
        """Voice Channels"""
        from .resources.inbound_channels import AsyncInboundChannelsResourceWithStreamingResponse

        return AsyncInboundChannelsResourceWithStreamingResponse(self._client.inbound_channels)

    @cached_property
    def integration_secrets(self) -> integration_secrets.AsyncIntegrationSecretsResourceWithStreamingResponse:
        """Store and retrieve integration secrets"""
        from .resources.integration_secrets import AsyncIntegrationSecretsResourceWithStreamingResponse

        return AsyncIntegrationSecretsResourceWithStreamingResponse(self._client.integration_secrets)

    @cached_property
    def inventory_coverage(self) -> inventory_coverage.AsyncInventoryCoverageResourceWithStreamingResponse:
        """Inventory Level"""
        from .resources.inventory_coverage import AsyncInventoryCoverageResourceWithStreamingResponse

        return AsyncInventoryCoverageResourceWithStreamingResponse(self._client.inventory_coverage)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithStreamingResponse:
        from .resources.invoices import AsyncInvoicesResourceWithStreamingResponse

        return AsyncInvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def ip_connections(self) -> ip_connections.AsyncIPConnectionsResourceWithStreamingResponse:
        """IP connection operations"""
        from .resources.ip_connections import AsyncIPConnectionsResourceWithStreamingResponse

        return AsyncIPConnectionsResourceWithStreamingResponse(self._client.ip_connections)

    @cached_property
    def ips(self) -> ips.AsyncIPsResourceWithStreamingResponse:
        """IP operations"""
        from .resources.ips import AsyncIPsResourceWithStreamingResponse

        return AsyncIPsResourceWithStreamingResponse(self._client.ips)

    @cached_property
    def ledger_billing_group_reports(
        self,
    ) -> ledger_billing_group_reports.AsyncLedgerBillingGroupReportsResourceWithStreamingResponse:
        """Ledger billing reports"""
        from .resources.ledger_billing_group_reports import AsyncLedgerBillingGroupReportsResourceWithStreamingResponse

        return AsyncLedgerBillingGroupReportsResourceWithStreamingResponse(self._client.ledger_billing_group_reports)

    @cached_property
    def list(self) -> list.AsyncListResourceWithStreamingResponse:
        """Voice Channels"""
        from .resources.list import AsyncListResourceWithStreamingResponse

        return AsyncListResourceWithStreamingResponse(self._client.list)

    @cached_property
    def managed_accounts(self) -> managed_accounts.AsyncManagedAccountsResourceWithStreamingResponse:
        """Managed Accounts operations"""
        from .resources.managed_accounts import AsyncManagedAccountsResourceWithStreamingResponse

        return AsyncManagedAccountsResourceWithStreamingResponse(self._client.managed_accounts)

    @cached_property
    def media(self) -> media.AsyncMediaResourceWithStreamingResponse:
        """Media Storage operations"""
        from .resources.media import AsyncMediaResourceWithStreamingResponse

        return AsyncMediaResourceWithStreamingResponse(self._client.media)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def messaging(self) -> messaging.AsyncMessagingResourceWithStreamingResponse:
        from .resources.messaging import AsyncMessagingResourceWithStreamingResponse

        return AsyncMessagingResourceWithStreamingResponse(self._client.messaging)

    @cached_property
    def messaging_hosted_number_orders(
        self,
    ) -> messaging_hosted_number_orders.AsyncMessagingHostedNumberOrdersResourceWithStreamingResponse:
        """Manage your messaging hosted numbers"""
        from .resources.messaging_hosted_number_orders import (
            AsyncMessagingHostedNumberOrdersResourceWithStreamingResponse,
        )

        return AsyncMessagingHostedNumberOrdersResourceWithStreamingResponse(
            self._client.messaging_hosted_number_orders
        )

    @cached_property
    def messaging_hosted_numbers(
        self,
    ) -> messaging_hosted_numbers.AsyncMessagingHostedNumbersResourceWithStreamingResponse:
        from .resources.messaging_hosted_numbers import AsyncMessagingHostedNumbersResourceWithStreamingResponse

        return AsyncMessagingHostedNumbersResourceWithStreamingResponse(self._client.messaging_hosted_numbers)

    @cached_property
    def messaging_numbers_bulk_updates(
        self,
    ) -> messaging_numbers_bulk_updates.AsyncMessagingNumbersBulkUpdatesResourceWithStreamingResponse:
        """Configure your phone numbers"""
        from .resources.messaging_numbers_bulk_updates import (
            AsyncMessagingNumbersBulkUpdatesResourceWithStreamingResponse,
        )

        return AsyncMessagingNumbersBulkUpdatesResourceWithStreamingResponse(
            self._client.messaging_numbers_bulk_updates
        )

    @cached_property
    def messaging_optouts(self) -> messaging_optouts.AsyncMessagingOptoutsResourceWithStreamingResponse:
        """Opt-Out Management"""
        from .resources.messaging_optouts import AsyncMessagingOptoutsResourceWithStreamingResponse

        return AsyncMessagingOptoutsResourceWithStreamingResponse(self._client.messaging_optouts)

    @cached_property
    def messaging_profiles(self) -> messaging_profiles.AsyncMessagingProfilesResourceWithStreamingResponse:
        from .resources.messaging_profiles import AsyncMessagingProfilesResourceWithStreamingResponse

        return AsyncMessagingProfilesResourceWithStreamingResponse(self._client.messaging_profiles)

    @cached_property
    def messaging_tollfree(self) -> messaging_tollfree.AsyncMessagingTollfreeResourceWithStreamingResponse:
        from .resources.messaging_tollfree import AsyncMessagingTollfreeResourceWithStreamingResponse

        return AsyncMessagingTollfreeResourceWithStreamingResponse(self._client.messaging_tollfree)

    @cached_property
    def messaging_url_domains(self) -> messaging_url_domains.AsyncMessagingURLDomainsResourceWithStreamingResponse:
        """Messaging URL Domains"""
        from .resources.messaging_url_domains import AsyncMessagingURLDomainsResourceWithStreamingResponse

        return AsyncMessagingURLDomainsResourceWithStreamingResponse(self._client.messaging_url_domains)

    @cached_property
    def mobile_network_operators(
        self,
    ) -> mobile_network_operators.AsyncMobileNetworkOperatorsResourceWithStreamingResponse:
        """Mobile network operators operations"""
        from .resources.mobile_network_operators import AsyncMobileNetworkOperatorsResourceWithStreamingResponse

        return AsyncMobileNetworkOperatorsResourceWithStreamingResponse(self._client.mobile_network_operators)

    @cached_property
    def mobile_push_credentials(
        self,
    ) -> mobile_push_credentials.AsyncMobilePushCredentialsResourceWithStreamingResponse:
        """Mobile push credential management"""
        from .resources.mobile_push_credentials import AsyncMobilePushCredentialsResourceWithStreamingResponse

        return AsyncMobilePushCredentialsResourceWithStreamingResponse(self._client.mobile_push_credentials)

    @cached_property
    def network_coverage(self) -> network_coverage.AsyncNetworkCoverageResourceWithStreamingResponse:
        from .resources.network_coverage import AsyncNetworkCoverageResourceWithStreamingResponse

        return AsyncNetworkCoverageResourceWithStreamingResponse(self._client.network_coverage)

    @cached_property
    def networks(self) -> networks.AsyncNetworksResourceWithStreamingResponse:
        """Network operations"""
        from .resources.networks import AsyncNetworksResourceWithStreamingResponse

        return AsyncNetworksResourceWithStreamingResponse(self._client.networks)

    @cached_property
    def notification_channels(self) -> notification_channels.AsyncNotificationChannelsResourceWithStreamingResponse:
        """Notification settings operations"""
        from .resources.notification_channels import AsyncNotificationChannelsResourceWithStreamingResponse

        return AsyncNotificationChannelsResourceWithStreamingResponse(self._client.notification_channels)

    @cached_property
    def notification_event_conditions(
        self,
    ) -> notification_event_conditions.AsyncNotificationEventConditionsResourceWithStreamingResponse:
        """Notification settings operations"""
        from .resources.notification_event_conditions import (
            AsyncNotificationEventConditionsResourceWithStreamingResponse,
        )

        return AsyncNotificationEventConditionsResourceWithStreamingResponse(self._client.notification_event_conditions)

    @cached_property
    def notification_events(self) -> notification_events.AsyncNotificationEventsResourceWithStreamingResponse:
        """Notification settings operations"""
        from .resources.notification_events import AsyncNotificationEventsResourceWithStreamingResponse

        return AsyncNotificationEventsResourceWithStreamingResponse(self._client.notification_events)

    @cached_property
    def notification_profiles(self) -> notification_profiles.AsyncNotificationProfilesResourceWithStreamingResponse:
        """Notification settings operations"""
        from .resources.notification_profiles import AsyncNotificationProfilesResourceWithStreamingResponse

        return AsyncNotificationProfilesResourceWithStreamingResponse(self._client.notification_profiles)

    @cached_property
    def notification_settings(self) -> notification_settings.AsyncNotificationSettingsResourceWithStreamingResponse:
        """Notification settings operations"""
        from .resources.notification_settings import AsyncNotificationSettingsResourceWithStreamingResponse

        return AsyncNotificationSettingsResourceWithStreamingResponse(self._client.notification_settings)

    @cached_property
    def number_block_orders(self) -> number_block_orders.AsyncNumberBlockOrdersResourceWithStreamingResponse:
        from .resources.number_block_orders import AsyncNumberBlockOrdersResourceWithStreamingResponse

        return AsyncNumberBlockOrdersResourceWithStreamingResponse(self._client.number_block_orders)

    @cached_property
    def number_lookup(self) -> number_lookup.AsyncNumberLookupResourceWithStreamingResponse:
        """Look up phone number data"""
        from .resources.number_lookup import AsyncNumberLookupResourceWithStreamingResponse

        return AsyncNumberLookupResourceWithStreamingResponse(self._client.number_lookup)

    @cached_property
    def number_order_phone_numbers(
        self,
    ) -> number_order_phone_numbers.AsyncNumberOrderPhoneNumbersResourceWithStreamingResponse:
        from .resources.number_order_phone_numbers import AsyncNumberOrderPhoneNumbersResourceWithStreamingResponse

        return AsyncNumberOrderPhoneNumbersResourceWithStreamingResponse(self._client.number_order_phone_numbers)

    @cached_property
    def number_orders(self) -> number_orders.AsyncNumberOrdersResourceWithStreamingResponse:
        """Number orders"""
        from .resources.number_orders import AsyncNumberOrdersResourceWithStreamingResponse

        return AsyncNumberOrdersResourceWithStreamingResponse(self._client.number_orders)

    @cached_property
    def number_reservations(self) -> number_reservations.AsyncNumberReservationsResourceWithStreamingResponse:
        """Number reservations"""
        from .resources.number_reservations import AsyncNumberReservationsResourceWithStreamingResponse

        return AsyncNumberReservationsResourceWithStreamingResponse(self._client.number_reservations)

    @cached_property
    def numbers_features(self) -> numbers_features.AsyncNumbersFeaturesResourceWithStreamingResponse:
        from .resources.numbers_features import AsyncNumbersFeaturesResourceWithStreamingResponse

        return AsyncNumbersFeaturesResourceWithStreamingResponse(self._client.numbers_features)

    @cached_property
    def operator_connect(self) -> operator_connect.AsyncOperatorConnectResourceWithStreamingResponse:
        from .resources.operator_connect import AsyncOperatorConnectResourceWithStreamingResponse

        return AsyncOperatorConnectResourceWithStreamingResponse(self._client.operator_connect)

    @cached_property
    def ota_updates(self) -> ota_updates.AsyncOtaUpdatesResourceWithStreamingResponse:
        """OTA updates operations"""
        from .resources.ota_updates import AsyncOtaUpdatesResourceWithStreamingResponse

        return AsyncOtaUpdatesResourceWithStreamingResponse(self._client.ota_updates)

    @cached_property
    def outbound_voice_profiles(
        self,
    ) -> outbound_voice_profiles.AsyncOutboundVoiceProfilesResourceWithStreamingResponse:
        """Outbound voice profiles operations"""
        from .resources.outbound_voice_profiles import AsyncOutboundVoiceProfilesResourceWithStreamingResponse

        return AsyncOutboundVoiceProfilesResourceWithStreamingResponse(self._client.outbound_voice_profiles)

    @cached_property
    def payment(self) -> payment.AsyncPaymentResourceWithStreamingResponse:
        """Operations for managing stored payment transactions."""
        from .resources.payment import AsyncPaymentResourceWithStreamingResponse

        return AsyncPaymentResourceWithStreamingResponse(self._client.payment)

    @cached_property
    def phone_number_blocks(self) -> phone_number_blocks.AsyncPhoneNumberBlocksResourceWithStreamingResponse:
        from .resources.phone_number_blocks import AsyncPhoneNumberBlocksResourceWithStreamingResponse

        return AsyncPhoneNumberBlocksResourceWithStreamingResponse(self._client.phone_number_blocks)

    @cached_property
    def phone_numbers(self) -> phone_numbers.AsyncPhoneNumbersResourceWithStreamingResponse:
        """Configure your phone numbers"""
        from .resources.phone_numbers import AsyncPhoneNumbersResourceWithStreamingResponse

        return AsyncPhoneNumbersResourceWithStreamingResponse(self._client.phone_numbers)

    @cached_property
    def phone_numbers_regulatory_requirements(
        self,
    ) -> phone_numbers_regulatory_requirements.AsyncPhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse:
        """Regulatory Requirements"""
        from .resources.phone_numbers_regulatory_requirements import (
            AsyncPhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse,
        )

        return AsyncPhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse(
            self._client.phone_numbers_regulatory_requirements
        )

    @cached_property
    def portability_checks(self) -> portability_checks.AsyncPortabilityChecksResourceWithStreamingResponse:
        """Determining portability of phone numbers"""
        from .resources.portability_checks import AsyncPortabilityChecksResourceWithStreamingResponse

        return AsyncPortabilityChecksResourceWithStreamingResponse(self._client.portability_checks)

    @cached_property
    def porting(self) -> porting.AsyncPortingResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting import AsyncPortingResourceWithStreamingResponse

        return AsyncPortingResourceWithStreamingResponse(self._client.porting)

    @cached_property
    def porting_orders(self) -> porting_orders.AsyncPortingOrdersResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting_orders import AsyncPortingOrdersResourceWithStreamingResponse

        return AsyncPortingOrdersResourceWithStreamingResponse(self._client.porting_orders)

    @cached_property
    def porting_phone_numbers(self) -> porting_phone_numbers.AsyncPortingPhoneNumbersResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        from .resources.porting_phone_numbers import AsyncPortingPhoneNumbersResourceWithStreamingResponse

        return AsyncPortingPhoneNumbersResourceWithStreamingResponse(self._client.porting_phone_numbers)

    @cached_property
    def portouts(self) -> portouts.AsyncPortoutsResourceWithStreamingResponse:
        """Number portout operations"""
        from .resources.portouts import AsyncPortoutsResourceWithStreamingResponse

        return AsyncPortoutsResourceWithStreamingResponse(self._client.portouts)

    @cached_property
    def private_wireless_gateways(
        self,
    ) -> private_wireless_gateways.AsyncPrivateWirelessGatewaysResourceWithStreamingResponse:
        """Private Wireless Gateways operations"""
        from .resources.private_wireless_gateways import AsyncPrivateWirelessGatewaysResourceWithStreamingResponse

        return AsyncPrivateWirelessGatewaysResourceWithStreamingResponse(self._client.private_wireless_gateways)

    @cached_property
    def public_internet_gateways(
        self,
    ) -> public_internet_gateways.AsyncPublicInternetGatewaysResourceWithStreamingResponse:
        """Public Internet Gateway operations"""
        from .resources.public_internet_gateways import AsyncPublicInternetGatewaysResourceWithStreamingResponse

        return AsyncPublicInternetGatewaysResourceWithStreamingResponse(self._client.public_internet_gateways)

    @cached_property
    def queues(self) -> queues.AsyncQueuesResourceWithStreamingResponse:
        """Queue commands operations"""
        from .resources.queues import AsyncQueuesResourceWithStreamingResponse

        return AsyncQueuesResourceWithStreamingResponse(self._client.queues)

    @cached_property
    def recording_transcriptions(
        self,
    ) -> recording_transcriptions.AsyncRecordingTranscriptionsResourceWithStreamingResponse:
        """Call Recordings operations."""
        from .resources.recording_transcriptions import AsyncRecordingTranscriptionsResourceWithStreamingResponse

        return AsyncRecordingTranscriptionsResourceWithStreamingResponse(self._client.recording_transcriptions)

    @cached_property
    def recordings(self) -> recordings.AsyncRecordingsResourceWithStreamingResponse:
        """Call Recordings operations."""
        from .resources.recordings import AsyncRecordingsResourceWithStreamingResponse

        return AsyncRecordingsResourceWithStreamingResponse(self._client.recordings)

    @cached_property
    def regions(self) -> regions.AsyncRegionsResourceWithStreamingResponse:
        """Regions"""
        from .resources.regions import AsyncRegionsResourceWithStreamingResponse

        return AsyncRegionsResourceWithStreamingResponse(self._client.regions)

    @cached_property
    def regulatory_requirements(
        self,
    ) -> regulatory_requirements.AsyncRegulatoryRequirementsResourceWithStreamingResponse:
        """Regulatory Requirements"""
        from .resources.regulatory_requirements import AsyncRegulatoryRequirementsResourceWithStreamingResponse

        return AsyncRegulatoryRequirementsResourceWithStreamingResponse(self._client.regulatory_requirements)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithStreamingResponse:
        from .resources.reports import AsyncReportsResourceWithStreamingResponse

        return AsyncReportsResourceWithStreamingResponse(self._client.reports)

    @cached_property
    def requirement_groups(self) -> requirement_groups.AsyncRequirementGroupsResourceWithStreamingResponse:
        """Requirement Groups"""
        from .resources.requirement_groups import AsyncRequirementGroupsResourceWithStreamingResponse

        return AsyncRequirementGroupsResourceWithStreamingResponse(self._client.requirement_groups)

    @cached_property
    def requirement_types(self) -> requirement_types.AsyncRequirementTypesResourceWithStreamingResponse:
        """Types of requirements for international numbers and porting orders"""
        from .resources.requirement_types import AsyncRequirementTypesResourceWithStreamingResponse

        return AsyncRequirementTypesResourceWithStreamingResponse(self._client.requirement_types)

    @cached_property
    def requirements(self) -> requirements.AsyncRequirementsResourceWithStreamingResponse:
        """Requirements for international numbers and porting orders"""
        from .resources.requirements import AsyncRequirementsResourceWithStreamingResponse

        return AsyncRequirementsResourceWithStreamingResponse(self._client.requirements)

    @cached_property
    def room_compositions(self) -> room_compositions.AsyncRoomCompositionsResourceWithStreamingResponse:
        """Rooms Compositions operations."""
        from .resources.room_compositions import AsyncRoomCompositionsResourceWithStreamingResponse

        return AsyncRoomCompositionsResourceWithStreamingResponse(self._client.room_compositions)

    @cached_property
    def room_participants(self) -> room_participants.AsyncRoomParticipantsResourceWithStreamingResponse:
        """Rooms Participants operations."""
        from .resources.room_participants import AsyncRoomParticipantsResourceWithStreamingResponse

        return AsyncRoomParticipantsResourceWithStreamingResponse(self._client.room_participants)

    @cached_property
    def room_recordings(self) -> room_recordings.AsyncRoomRecordingsResourceWithStreamingResponse:
        """Rooms Recordings operations."""
        from .resources.room_recordings import AsyncRoomRecordingsResourceWithStreamingResponse

        return AsyncRoomRecordingsResourceWithStreamingResponse(self._client.room_recordings)

    @cached_property
    def rooms(self) -> rooms.AsyncRoomsResourceWithStreamingResponse:
        """Rooms operations."""
        from .resources.rooms import AsyncRoomsResourceWithStreamingResponse

        return AsyncRoomsResourceWithStreamingResponse(self._client.rooms)

    @cached_property
    def seti(self) -> seti.AsyncSetiResourceWithStreamingResponse:
        """Observability into Telnyx platform stability and performance."""
        from .resources.seti import AsyncSetiResourceWithStreamingResponse

        return AsyncSetiResourceWithStreamingResponse(self._client.seti)

    @cached_property
    def short_codes(self) -> short_codes.AsyncShortCodesResourceWithStreamingResponse:
        """Short codes"""
        from .resources.short_codes import AsyncShortCodesResourceWithStreamingResponse

        return AsyncShortCodesResourceWithStreamingResponse(self._client.short_codes)

    @cached_property
    def sim_card_data_usage_notifications(
        self,
    ) -> sim_card_data_usage_notifications.AsyncSimCardDataUsageNotificationsResourceWithStreamingResponse:
        """SIM Cards operations"""
        from .resources.sim_card_data_usage_notifications import (
            AsyncSimCardDataUsageNotificationsResourceWithStreamingResponse,
        )

        return AsyncSimCardDataUsageNotificationsResourceWithStreamingResponse(
            self._client.sim_card_data_usage_notifications
        )

    @cached_property
    def sim_card_groups(self) -> sim_card_groups.AsyncSimCardGroupsResourceWithStreamingResponse:
        """SIM Card Groups operations"""
        from .resources.sim_card_groups import AsyncSimCardGroupsResourceWithStreamingResponse

        return AsyncSimCardGroupsResourceWithStreamingResponse(self._client.sim_card_groups)

    @cached_property
    def sim_card_order_preview(self) -> sim_card_order_preview.AsyncSimCardOrderPreviewResourceWithStreamingResponse:
        """SIM Card Orders operations"""
        from .resources.sim_card_order_preview import AsyncSimCardOrderPreviewResourceWithStreamingResponse

        return AsyncSimCardOrderPreviewResourceWithStreamingResponse(self._client.sim_card_order_preview)

    @cached_property
    def sim_card_orders(self) -> sim_card_orders.AsyncSimCardOrdersResourceWithStreamingResponse:
        """SIM Card Orders operations"""
        from .resources.sim_card_orders import AsyncSimCardOrdersResourceWithStreamingResponse

        return AsyncSimCardOrdersResourceWithStreamingResponse(self._client.sim_card_orders)

    @cached_property
    def sim_cards(self) -> sim_cards.AsyncSimCardsResourceWithStreamingResponse:
        """SIM Cards operations"""
        from .resources.sim_cards import AsyncSimCardsResourceWithStreamingResponse

        return AsyncSimCardsResourceWithStreamingResponse(self._client.sim_cards)

    @cached_property
    def siprec_connectors(self) -> siprec_connectors.AsyncSiprecConnectorsResourceWithStreamingResponse:
        """SIPREC connectors configuration."""
        from .resources.siprec_connectors import AsyncSiprecConnectorsResourceWithStreamingResponse

        return AsyncSiprecConnectorsResourceWithStreamingResponse(self._client.siprec_connectors)

    @cached_property
    def storage(self) -> storage.AsyncStorageResourceWithStreamingResponse:
        """Migrate data from an external provider into Telnyx Cloud Storage"""
        from .resources.storage import AsyncStorageResourceWithStreamingResponse

        return AsyncStorageResourceWithStreamingResponse(self._client.storage)

    @cached_property
    def sub_number_orders(self) -> sub_number_orders.AsyncSubNumberOrdersResourceWithStreamingResponse:
        from .resources.sub_number_orders import AsyncSubNumberOrdersResourceWithStreamingResponse

        return AsyncSubNumberOrdersResourceWithStreamingResponse(self._client.sub_number_orders)

    @cached_property
    def sub_number_orders_report(
        self,
    ) -> sub_number_orders_report.AsyncSubNumberOrdersReportResourceWithStreamingResponse:
        """Number orders"""
        from .resources.sub_number_orders_report import AsyncSubNumberOrdersReportResourceWithStreamingResponse

        return AsyncSubNumberOrdersReportResourceWithStreamingResponse(self._client.sub_number_orders_report)

    @cached_property
    def telephony_credentials(self) -> telephony_credentials.AsyncTelephonyCredentialsResourceWithStreamingResponse:
        from .resources.telephony_credentials import AsyncTelephonyCredentialsResourceWithStreamingResponse

        return AsyncTelephonyCredentialsResourceWithStreamingResponse(self._client.telephony_credentials)

    @cached_property
    def texml(self) -> texml.AsyncTexmlResourceWithStreamingResponse:
        """TeXML REST Commands"""
        from .resources.texml import AsyncTexmlResourceWithStreamingResponse

        return AsyncTexmlResourceWithStreamingResponse(self._client.texml)

    @cached_property
    def texml_applications(self) -> texml_applications.AsyncTexmlApplicationsResourceWithStreamingResponse:
        """TeXML Applications operations"""
        from .resources.texml_applications import AsyncTexmlApplicationsResourceWithStreamingResponse

        return AsyncTexmlApplicationsResourceWithStreamingResponse(self._client.texml_applications)

    @cached_property
    def text_to_speech(self) -> text_to_speech.AsyncTextToSpeechResourceWithStreamingResponse:
        """Text to speech streaming command operations"""
        from .resources.text_to_speech import AsyncTextToSpeechResourceWithStreamingResponse

        return AsyncTextToSpeechResourceWithStreamingResponse(self._client.text_to_speech)

    @cached_property
    def usage_reports(self) -> usage_reports.AsyncUsageReportsResourceWithStreamingResponse:
        """Usage data reporting across Telnyx products"""
        from .resources.usage_reports import AsyncUsageReportsResourceWithStreamingResponse

        return AsyncUsageReportsResourceWithStreamingResponse(self._client.usage_reports)

    @cached_property
    def user_addresses(self) -> user_addresses.AsyncUserAddressesResourceWithStreamingResponse:
        """Operations for working with UserAddress records.

        UserAddress records are stored addresses that users can use for non-emergency-calling purposes, such as for shipping addresses for orders of wireless SIMs (or other physical items). They cannot be used for emergency calling and are distinct from Address records, which are used on phone numbers.
        """
        from .resources.user_addresses import AsyncUserAddressesResourceWithStreamingResponse

        return AsyncUserAddressesResourceWithStreamingResponse(self._client.user_addresses)

    @cached_property
    def user_tags(self) -> user_tags.AsyncUserTagsResourceWithStreamingResponse:
        """User-defined tags for Telnyx resources"""
        from .resources.user_tags import AsyncUserTagsResourceWithStreamingResponse

        return AsyncUserTagsResourceWithStreamingResponse(self._client.user_tags)

    @cached_property
    def verifications(self) -> verifications.AsyncVerificationsResourceWithStreamingResponse:
        """Two factor authentication API"""
        from .resources.verifications import AsyncVerificationsResourceWithStreamingResponse

        return AsyncVerificationsResourceWithStreamingResponse(self._client.verifications)

    @cached_property
    def verified_numbers(self) -> verified_numbers.AsyncVerifiedNumbersResourceWithStreamingResponse:
        """Verified Numbers operations"""
        from .resources.verified_numbers import AsyncVerifiedNumbersResourceWithStreamingResponse

        return AsyncVerifiedNumbersResourceWithStreamingResponse(self._client.verified_numbers)

    @cached_property
    def verify_profiles(self) -> verify_profiles.AsyncVerifyProfilesResourceWithStreamingResponse:
        """Two factor authentication API"""
        from .resources.verify_profiles import AsyncVerifyProfilesResourceWithStreamingResponse

        return AsyncVerifyProfilesResourceWithStreamingResponse(self._client.verify_profiles)

    @cached_property
    def virtual_cross_connects(self) -> virtual_cross_connects.AsyncVirtualCrossConnectsResourceWithStreamingResponse:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects import AsyncVirtualCrossConnectsResourceWithStreamingResponse

        return AsyncVirtualCrossConnectsResourceWithStreamingResponse(self._client.virtual_cross_connects)

    @cached_property
    def virtual_cross_connects_coverage(
        self,
    ) -> virtual_cross_connects_coverage.AsyncVirtualCrossConnectsCoverageResourceWithStreamingResponse:
        """Virtual Cross Connect operations"""
        from .resources.virtual_cross_connects_coverage import (
            AsyncVirtualCrossConnectsCoverageResourceWithStreamingResponse,
        )

        return AsyncVirtualCrossConnectsCoverageResourceWithStreamingResponse(
            self._client.virtual_cross_connects_coverage
        )

    @cached_property
    def webhook_deliveries(self) -> webhook_deliveries.AsyncWebhookDeliveriesResourceWithStreamingResponse:
        """Webhooks operations"""
        from .resources.webhook_deliveries import AsyncWebhookDeliveriesResourceWithStreamingResponse

        return AsyncWebhookDeliveriesResourceWithStreamingResponse(self._client.webhook_deliveries)

    @cached_property
    def wireguard_interfaces(self) -> wireguard_interfaces.AsyncWireguardInterfacesResourceWithStreamingResponse:
        """WireGuard Interface operations"""
        from .resources.wireguard_interfaces import AsyncWireguardInterfacesResourceWithStreamingResponse

        return AsyncWireguardInterfacesResourceWithStreamingResponse(self._client.wireguard_interfaces)

    @cached_property
    def wireguard_peers(self) -> wireguard_peers.AsyncWireguardPeersResourceWithStreamingResponse:
        """WireGuard Interface operations"""
        from .resources.wireguard_peers import AsyncWireguardPeersResourceWithStreamingResponse

        return AsyncWireguardPeersResourceWithStreamingResponse(self._client.wireguard_peers)

    @cached_property
    def wireless(self) -> wireless.AsyncWirelessResourceWithStreamingResponse:
        """Regions for wireless services"""
        from .resources.wireless import AsyncWirelessResourceWithStreamingResponse

        return AsyncWirelessResourceWithStreamingResponse(self._client.wireless)

    @cached_property
    def wireless_blocklist_values(
        self,
    ) -> wireless_blocklist_values.AsyncWirelessBlocklistValuesResourceWithStreamingResponse:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklist_values import AsyncWirelessBlocklistValuesResourceWithStreamingResponse

        return AsyncWirelessBlocklistValuesResourceWithStreamingResponse(self._client.wireless_blocklist_values)

    @cached_property
    def wireless_blocklists(self) -> wireless_blocklists.AsyncWirelessBlocklistsResourceWithStreamingResponse:
        """Wireless Blocklists operations"""
        from .resources.wireless_blocklists import AsyncWirelessBlocklistsResourceWithStreamingResponse

        return AsyncWirelessBlocklistsResourceWithStreamingResponse(self._client.wireless_blocklists)

    @cached_property
    def well_known(self) -> well_known.AsyncWellKnownResourceWithStreamingResponse:
        from .resources.well_known import AsyncWellKnownResourceWithStreamingResponse

        return AsyncWellKnownResourceWithStreamingResponse(self._client.well_known)

    @cached_property
    def inexplicit_number_orders(
        self,
    ) -> inexplicit_number_orders.AsyncInexplicitNumberOrdersResourceWithStreamingResponse:
        """Inexplicit number orders for bulk purchasing without specifying exact numbers"""
        from .resources.inexplicit_number_orders import AsyncInexplicitNumberOrdersResourceWithStreamingResponse

        return AsyncInexplicitNumberOrdersResourceWithStreamingResponse(self._client.inexplicit_number_orders)

    @cached_property
    def mobile_phone_numbers(self) -> mobile_phone_numbers.AsyncMobilePhoneNumbersResourceWithStreamingResponse:
        """Mobile phone number operations"""
        from .resources.mobile_phone_numbers import AsyncMobilePhoneNumbersResourceWithStreamingResponse

        return AsyncMobilePhoneNumbersResourceWithStreamingResponse(self._client.mobile_phone_numbers)

    @cached_property
    def mobile_voice_connections(
        self,
    ) -> mobile_voice_connections.AsyncMobileVoiceConnectionsResourceWithStreamingResponse:
        """Mobile voice connection operations"""
        from .resources.mobile_voice_connections import AsyncMobileVoiceConnectionsResourceWithStreamingResponse

        return AsyncMobileVoiceConnectionsResourceWithStreamingResponse(self._client.mobile_voice_connections)

    @cached_property
    def messaging_10dlc(self) -> messaging_10dlc.AsyncMessaging10dlcResourceWithStreamingResponse:
        from .resources.messaging_10dlc import AsyncMessaging10dlcResourceWithStreamingResponse

        return AsyncMessaging10dlcResourceWithStreamingResponse(self._client.messaging_10dlc)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse

        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def alphanumeric_sender_ids(
        self,
    ) -> alphanumeric_sender_ids.AsyncAlphanumericSenderIDsResourceWithStreamingResponse:
        from .resources.alphanumeric_sender_ids import AsyncAlphanumericSenderIDsResourceWithStreamingResponse

        return AsyncAlphanumericSenderIDsResourceWithStreamingResponse(self._client.alphanumeric_sender_ids)

    @cached_property
    def messaging_profile_metrics(
        self,
    ) -> messaging_profile_metrics.AsyncMessagingProfileMetricsResourceWithStreamingResponse:
        from .resources.messaging_profile_metrics import AsyncMessagingProfileMetricsResourceWithStreamingResponse

        return AsyncMessagingProfileMetricsResourceWithStreamingResponse(self._client.messaging_profile_metrics)

    @cached_property
    def session_analysis(self) -> session_analysis.AsyncSessionAnalysisResourceWithStreamingResponse:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        from .resources.session_analysis import AsyncSessionAnalysisResourceWithStreamingResponse

        return AsyncSessionAnalysisResourceWithStreamingResponse(self._client.session_analysis)


Client = Telnyx

AsyncClient = AsyncTelnyx
