# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    DtmfType,
    EncryptedMedia,
    TransportProtocol,
    WebhookAPIVersion,
    AnchorsiteOverride,
    fqdn_connection_list_params,
    fqdn_connection_create_params,
    fqdn_connection_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.dtmf_type import DtmfType
from ..types.encrypted_media import EncryptedMedia
from ..types.fqdn_connection import FqdnConnection
from ..types.inbound_fqdn_param import InboundFqdnParam
from ..types.transport_protocol import TransportProtocol
from ..types.anchorsite_override import AnchorsiteOverride
from ..types.outbound_fqdn_param import OutboundFqdnParam
from ..types.webhook_api_version import WebhookAPIVersion
from ..types.connection_rtcp_settings_param import ConnectionRtcpSettingsParam
from ..types.fqdn_connection_create_response import FqdnConnectionCreateResponse
from ..types.fqdn_connection_delete_response import FqdnConnectionDeleteResponse
from ..types.fqdn_connection_update_response import FqdnConnectionUpdateResponse
from ..types.fqdn_connection_retrieve_response import FqdnConnectionRetrieveResponse
from ..types.shared_params.connection_noise_suppression_details import ConnectionNoiseSuppressionDetails

__all__ = ["FqdnConnectionsResource", "AsyncFqdnConnectionsResource"]


class FqdnConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FqdnConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return FqdnConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FqdnConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return FqdnConnectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connection_name: str,
        active: bool | Omit = omit,
        anchorsite_override: AnchorsiteOverride | Omit = omit,
        android_push_credential_id: Optional[str] | Omit = omit,
        call_cost_in_webhooks: bool | Omit = omit,
        default_on_hold_comfort_noise_enabled: bool | Omit = omit,
        dtmf_type: DtmfType | Omit = omit,
        encode_contact_header_enabled: bool | Omit = omit,
        encrypted_media: Optional[EncryptedMedia] | Omit = omit,
        inbound: InboundFqdnParam | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: fqdn_connection_create_params.JitterBuffer | Omit = omit,
        microsoft_teams_sbc: bool | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: OutboundFqdnParam | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transport_protocol: TransportProtocol | Omit = omit,
        webhook_api_version: WebhookAPIVersion | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnConnectionCreateResponse:
        """
        Creates a FQDN connection.

        Args:
          connection_name: A user-assigned name to help manage the connection.

          active: Defaults to true

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          android_push_credential_id: The uuid of the push credential for Android

          call_cost_in_webhooks: Specifies if call cost webhooks should be sent for this connection.

          default_on_hold_comfort_noise_enabled: When enabled, Telnyx will generate comfort noise when you place the call on
              hold. If disabled, you will need to generate comfort noise or on hold music to
              avoid RTP timeout.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          encode_contact_header_enabled: Encode the SIP contact header sent by Telnyx to avoid issues for NAT or ALG
              scenarios.

          encrypted_media: Enable use of SRTP for encryption. Cannot be set if the transport_portocol is
              TLS.

          ios_push_credential_id: The uuid of the push credential for Ios

          jitter_buffer: Configuration options for Jitter Buffer. Enables Jitter Buffer for RTP streams
              of SIP Trunking calls. The feature is off unless enabled. You may define min and
              max values in msec for customized buffering behaviors. Larger values add latency
              but tolerate more jitter, while smaller values reduce latency but are more
              sensitive to jitter and reordering.

          microsoft_teams_sbc: When enabled, the connection will be created for Microsoft Teams Direct Routing.
              A \\**.mstsbc.telnyx.tech FQDN will be created for the connection automatically.

          noise_suppression: Controls when noise suppression is applied to calls. When set to 'inbound',
              noise suppression is applied to incoming audio. When set to 'outbound', it's
              applied to outgoing audio. When set to 'both', it's applied in both directions.
              When set to 'disabled', noise suppression is turned off.

          noise_suppression_details: Configuration options for noise suppression. These settings are stored
              regardless of the noise_suppression value, but only take effect when
              noise_suppression is not 'disabled'. If you disable noise suppression and later
              re-enable it, the previously configured settings will be used.

          onnet_t38_passthrough_enabled: Enable on-net T38 if you prefer the sender and receiver negotiating T38 directly
              if both are on the Telnyx network. If this is disabled, Telnyx will be able to
              use T38 on just one leg of the call depending on each leg's settings.

          tags: Tags associated with the connection.

          transport_protocol: One of UDP, TLS, or TCP. Applies only to connections with IP authentication or
              FQDN authentication.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1 or v2.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fqdn_connections",
            body=maybe_transform(
                {
                    "connection_name": connection_name,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "android_push_credential_id": android_push_credential_id,
                    "call_cost_in_webhooks": call_cost_in_webhooks,
                    "default_on_hold_comfort_noise_enabled": default_on_hold_comfort_noise_enabled,
                    "dtmf_type": dtmf_type,
                    "encode_contact_header_enabled": encode_contact_header_enabled,
                    "encrypted_media": encrypted_media,
                    "inbound": inbound,
                    "ios_push_credential_id": ios_push_credential_id,
                    "jitter_buffer": jitter_buffer,
                    "microsoft_teams_sbc": microsoft_teams_sbc,
                    "noise_suppression": noise_suppression,
                    "noise_suppression_details": noise_suppression_details,
                    "onnet_t38_passthrough_enabled": onnet_t38_passthrough_enabled,
                    "outbound": outbound,
                    "rtcp_settings": rtcp_settings,
                    "tags": tags,
                    "transport_protocol": transport_protocol,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                fqdn_connection_create_params.FqdnConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnConnectionCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnConnectionRetrieveResponse:
        """
        Retrieves the details of an existing FQDN connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/fqdn_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnConnectionRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        anchorsite_override: AnchorsiteOverride | Omit = omit,
        android_push_credential_id: Optional[str] | Omit = omit,
        call_cost_in_webhooks: bool | Omit = omit,
        connection_name: str | Omit = omit,
        default_on_hold_comfort_noise_enabled: bool | Omit = omit,
        dtmf_type: DtmfType | Omit = omit,
        encode_contact_header_enabled: bool | Omit = omit,
        encrypted_media: Optional[EncryptedMedia] | Omit = omit,
        inbound: InboundFqdnParam | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: fqdn_connection_update_params.JitterBuffer | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: OutboundFqdnParam | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transport_protocol: TransportProtocol | Omit = omit,
        webhook_api_version: WebhookAPIVersion | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnConnectionUpdateResponse:
        """
        Updates settings of an existing FQDN connection.

        Args:
          active: Defaults to true

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          android_push_credential_id: The uuid of the push credential for Android

          call_cost_in_webhooks: Specifies if call cost webhooks should be sent for this connection.

          connection_name: A user-assigned name to help manage the connection.

          default_on_hold_comfort_noise_enabled: When enabled, Telnyx will generate comfort noise when you place the call on
              hold. If disabled, you will need to generate comfort noise or on hold music to
              avoid RTP timeout.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          encode_contact_header_enabled: Encode the SIP contact header sent by Telnyx to avoid issues for NAT or ALG
              scenarios.

          encrypted_media: Enable use of SRTP for encryption. Cannot be set if the transport_portocol is
              TLS.

          ios_push_credential_id: The uuid of the push credential for Ios

          jitter_buffer: Configuration options for Jitter Buffer. Enables Jitter Buffer for RTP streams
              of SIP Trunking calls. The feature is off unless enabled. You may define min and
              max values in msec for customized buffering behaviors. Larger values add latency
              but tolerate more jitter, while smaller values reduce latency but are more
              sensitive to jitter and reordering.

          noise_suppression: Controls when noise suppression is applied to calls. When set to 'inbound',
              noise suppression is applied to incoming audio. When set to 'outbound', it's
              applied to outgoing audio. When set to 'both', it's applied in both directions.
              When set to 'disabled', noise suppression is turned off.

          noise_suppression_details: Configuration options for noise suppression. These settings are stored
              regardless of the noise_suppression value, but only take effect when
              noise_suppression is not 'disabled'. If you disable noise suppression and later
              re-enable it, the previously configured settings will be used.

          onnet_t38_passthrough_enabled: Enable on-net T38 if you prefer that the sender and receiver negotiate T38
              directly when both are on the Telnyx network. If this is disabled, Telnyx will
              be able to use T38 on just one leg of the call according to each leg's settings.

          tags: Tags associated with the connection.

          transport_protocol: One of UDP, TLS, or TCP. Applies only to connections with IP authentication or
              FQDN authentication.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1 or v2.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/fqdn_connections/{id}",
            body=maybe_transform(
                {
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "android_push_credential_id": android_push_credential_id,
                    "call_cost_in_webhooks": call_cost_in_webhooks,
                    "connection_name": connection_name,
                    "default_on_hold_comfort_noise_enabled": default_on_hold_comfort_noise_enabled,
                    "dtmf_type": dtmf_type,
                    "encode_contact_header_enabled": encode_contact_header_enabled,
                    "encrypted_media": encrypted_media,
                    "inbound": inbound,
                    "ios_push_credential_id": ios_push_credential_id,
                    "jitter_buffer": jitter_buffer,
                    "noise_suppression": noise_suppression,
                    "noise_suppression_details": noise_suppression_details,
                    "onnet_t38_passthrough_enabled": onnet_t38_passthrough_enabled,
                    "outbound": outbound,
                    "rtcp_settings": rtcp_settings,
                    "tags": tags,
                    "transport_protocol": transport_protocol,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                fqdn_connection_update_params.FqdnConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        filter: fqdn_connection_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "connection_name", "active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[FqdnConnection]:
        """
        Returns a list of your FQDN connections.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[connection_name], filter[fqdn], filter[outbound_voice_profile_id],
              filter[outbound.outbound_voice_profile_id]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>connection_name</code>: sorts the result by the
                  <code>connection_name</code> field in ascending order.
                </li>

                <li>
                  <code>-connection_name</code>: sorts the result by the
                  <code>connection_name</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/fqdn_connections",
            page=SyncDefaultFlatPagination[FqdnConnection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    fqdn_connection_list_params.FqdnConnectionListParams,
                ),
            ),
            model=FqdnConnection,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnConnectionDeleteResponse:
        """
        Deletes an FQDN connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/fqdn_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnConnectionDeleteResponse,
        )


class AsyncFqdnConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFqdnConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFqdnConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFqdnConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncFqdnConnectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connection_name: str,
        active: bool | Omit = omit,
        anchorsite_override: AnchorsiteOverride | Omit = omit,
        android_push_credential_id: Optional[str] | Omit = omit,
        call_cost_in_webhooks: bool | Omit = omit,
        default_on_hold_comfort_noise_enabled: bool | Omit = omit,
        dtmf_type: DtmfType | Omit = omit,
        encode_contact_header_enabled: bool | Omit = omit,
        encrypted_media: Optional[EncryptedMedia] | Omit = omit,
        inbound: InboundFqdnParam | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: fqdn_connection_create_params.JitterBuffer | Omit = omit,
        microsoft_teams_sbc: bool | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: OutboundFqdnParam | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transport_protocol: TransportProtocol | Omit = omit,
        webhook_api_version: WebhookAPIVersion | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnConnectionCreateResponse:
        """
        Creates a FQDN connection.

        Args:
          connection_name: A user-assigned name to help manage the connection.

          active: Defaults to true

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          android_push_credential_id: The uuid of the push credential for Android

          call_cost_in_webhooks: Specifies if call cost webhooks should be sent for this connection.

          default_on_hold_comfort_noise_enabled: When enabled, Telnyx will generate comfort noise when you place the call on
              hold. If disabled, you will need to generate comfort noise or on hold music to
              avoid RTP timeout.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          encode_contact_header_enabled: Encode the SIP contact header sent by Telnyx to avoid issues for NAT or ALG
              scenarios.

          encrypted_media: Enable use of SRTP for encryption. Cannot be set if the transport_portocol is
              TLS.

          ios_push_credential_id: The uuid of the push credential for Ios

          jitter_buffer: Configuration options for Jitter Buffer. Enables Jitter Buffer for RTP streams
              of SIP Trunking calls. The feature is off unless enabled. You may define min and
              max values in msec for customized buffering behaviors. Larger values add latency
              but tolerate more jitter, while smaller values reduce latency but are more
              sensitive to jitter and reordering.

          microsoft_teams_sbc: When enabled, the connection will be created for Microsoft Teams Direct Routing.
              A \\**.mstsbc.telnyx.tech FQDN will be created for the connection automatically.

          noise_suppression: Controls when noise suppression is applied to calls. When set to 'inbound',
              noise suppression is applied to incoming audio. When set to 'outbound', it's
              applied to outgoing audio. When set to 'both', it's applied in both directions.
              When set to 'disabled', noise suppression is turned off.

          noise_suppression_details: Configuration options for noise suppression. These settings are stored
              regardless of the noise_suppression value, but only take effect when
              noise_suppression is not 'disabled'. If you disable noise suppression and later
              re-enable it, the previously configured settings will be used.

          onnet_t38_passthrough_enabled: Enable on-net T38 if you prefer the sender and receiver negotiating T38 directly
              if both are on the Telnyx network. If this is disabled, Telnyx will be able to
              use T38 on just one leg of the call depending on each leg's settings.

          tags: Tags associated with the connection.

          transport_protocol: One of UDP, TLS, or TCP. Applies only to connections with IP authentication or
              FQDN authentication.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1 or v2.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fqdn_connections",
            body=await async_maybe_transform(
                {
                    "connection_name": connection_name,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "android_push_credential_id": android_push_credential_id,
                    "call_cost_in_webhooks": call_cost_in_webhooks,
                    "default_on_hold_comfort_noise_enabled": default_on_hold_comfort_noise_enabled,
                    "dtmf_type": dtmf_type,
                    "encode_contact_header_enabled": encode_contact_header_enabled,
                    "encrypted_media": encrypted_media,
                    "inbound": inbound,
                    "ios_push_credential_id": ios_push_credential_id,
                    "jitter_buffer": jitter_buffer,
                    "microsoft_teams_sbc": microsoft_teams_sbc,
                    "noise_suppression": noise_suppression,
                    "noise_suppression_details": noise_suppression_details,
                    "onnet_t38_passthrough_enabled": onnet_t38_passthrough_enabled,
                    "outbound": outbound,
                    "rtcp_settings": rtcp_settings,
                    "tags": tags,
                    "transport_protocol": transport_protocol,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                fqdn_connection_create_params.FqdnConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnConnectionCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnConnectionRetrieveResponse:
        """
        Retrieves the details of an existing FQDN connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/fqdn_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnConnectionRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        anchorsite_override: AnchorsiteOverride | Omit = omit,
        android_push_credential_id: Optional[str] | Omit = omit,
        call_cost_in_webhooks: bool | Omit = omit,
        connection_name: str | Omit = omit,
        default_on_hold_comfort_noise_enabled: bool | Omit = omit,
        dtmf_type: DtmfType | Omit = omit,
        encode_contact_header_enabled: bool | Omit = omit,
        encrypted_media: Optional[EncryptedMedia] | Omit = omit,
        inbound: InboundFqdnParam | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: fqdn_connection_update_params.JitterBuffer | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: OutboundFqdnParam | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transport_protocol: TransportProtocol | Omit = omit,
        webhook_api_version: WebhookAPIVersion | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnConnectionUpdateResponse:
        """
        Updates settings of an existing FQDN connection.

        Args:
          active: Defaults to true

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          android_push_credential_id: The uuid of the push credential for Android

          call_cost_in_webhooks: Specifies if call cost webhooks should be sent for this connection.

          connection_name: A user-assigned name to help manage the connection.

          default_on_hold_comfort_noise_enabled: When enabled, Telnyx will generate comfort noise when you place the call on
              hold. If disabled, you will need to generate comfort noise or on hold music to
              avoid RTP timeout.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          encode_contact_header_enabled: Encode the SIP contact header sent by Telnyx to avoid issues for NAT or ALG
              scenarios.

          encrypted_media: Enable use of SRTP for encryption. Cannot be set if the transport_portocol is
              TLS.

          ios_push_credential_id: The uuid of the push credential for Ios

          jitter_buffer: Configuration options for Jitter Buffer. Enables Jitter Buffer for RTP streams
              of SIP Trunking calls. The feature is off unless enabled. You may define min and
              max values in msec for customized buffering behaviors. Larger values add latency
              but tolerate more jitter, while smaller values reduce latency but are more
              sensitive to jitter and reordering.

          noise_suppression: Controls when noise suppression is applied to calls. When set to 'inbound',
              noise suppression is applied to incoming audio. When set to 'outbound', it's
              applied to outgoing audio. When set to 'both', it's applied in both directions.
              When set to 'disabled', noise suppression is turned off.

          noise_suppression_details: Configuration options for noise suppression. These settings are stored
              regardless of the noise_suppression value, but only take effect when
              noise_suppression is not 'disabled'. If you disable noise suppression and later
              re-enable it, the previously configured settings will be used.

          onnet_t38_passthrough_enabled: Enable on-net T38 if you prefer that the sender and receiver negotiate T38
              directly when both are on the Telnyx network. If this is disabled, Telnyx will
              be able to use T38 on just one leg of the call according to each leg's settings.

          tags: Tags associated with the connection.

          transport_protocol: One of UDP, TLS, or TCP. Applies only to connections with IP authentication or
              FQDN authentication.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1 or v2.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/fqdn_connections/{id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "android_push_credential_id": android_push_credential_id,
                    "call_cost_in_webhooks": call_cost_in_webhooks,
                    "connection_name": connection_name,
                    "default_on_hold_comfort_noise_enabled": default_on_hold_comfort_noise_enabled,
                    "dtmf_type": dtmf_type,
                    "encode_contact_header_enabled": encode_contact_header_enabled,
                    "encrypted_media": encrypted_media,
                    "inbound": inbound,
                    "ios_push_credential_id": ios_push_credential_id,
                    "jitter_buffer": jitter_buffer,
                    "noise_suppression": noise_suppression,
                    "noise_suppression_details": noise_suppression_details,
                    "onnet_t38_passthrough_enabled": onnet_t38_passthrough_enabled,
                    "outbound": outbound,
                    "rtcp_settings": rtcp_settings,
                    "tags": tags,
                    "transport_protocol": transport_protocol,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                fqdn_connection_update_params.FqdnConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        filter: fqdn_connection_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "connection_name", "active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FqdnConnection, AsyncDefaultFlatPagination[FqdnConnection]]:
        """
        Returns a list of your FQDN connections.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[connection_name], filter[fqdn], filter[outbound_voice_profile_id],
              filter[outbound.outbound_voice_profile_id]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>connection_name</code>: sorts the result by the
                  <code>connection_name</code> field in ascending order.
                </li>

                <li>
                  <code>-connection_name</code>: sorts the result by the
                  <code>connection_name</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/fqdn_connections",
            page=AsyncDefaultFlatPagination[FqdnConnection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    fqdn_connection_list_params.FqdnConnectionListParams,
                ),
            ),
            model=FqdnConnection,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnConnectionDeleteResponse:
        """
        Deletes an FQDN connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/fqdn_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnConnectionDeleteResponse,
        )


class FqdnConnectionsResourceWithRawResponse:
    def __init__(self, fqdn_connections: FqdnConnectionsResource) -> None:
        self._fqdn_connections = fqdn_connections

        self.create = to_raw_response_wrapper(
            fqdn_connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            fqdn_connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            fqdn_connections.update,
        )
        self.list = to_raw_response_wrapper(
            fqdn_connections.list,
        )
        self.delete = to_raw_response_wrapper(
            fqdn_connections.delete,
        )


class AsyncFqdnConnectionsResourceWithRawResponse:
    def __init__(self, fqdn_connections: AsyncFqdnConnectionsResource) -> None:
        self._fqdn_connections = fqdn_connections

        self.create = async_to_raw_response_wrapper(
            fqdn_connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            fqdn_connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            fqdn_connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            fqdn_connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            fqdn_connections.delete,
        )


class FqdnConnectionsResourceWithStreamingResponse:
    def __init__(self, fqdn_connections: FqdnConnectionsResource) -> None:
        self._fqdn_connections = fqdn_connections

        self.create = to_streamed_response_wrapper(
            fqdn_connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            fqdn_connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            fqdn_connections.update,
        )
        self.list = to_streamed_response_wrapper(
            fqdn_connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            fqdn_connections.delete,
        )


class AsyncFqdnConnectionsResourceWithStreamingResponse:
    def __init__(self, fqdn_connections: AsyncFqdnConnectionsResource) -> None:
        self._fqdn_connections = fqdn_connections

        self.create = async_to_streamed_response_wrapper(
            fqdn_connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            fqdn_connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            fqdn_connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            fqdn_connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            fqdn_connections.delete,
        )
