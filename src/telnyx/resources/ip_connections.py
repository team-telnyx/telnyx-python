# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    DtmfType,
    EncryptedMedia,
    AnchorsiteOverride,
    ip_connection_list_params,
    ip_connection_create_params,
    ip_connection_update_params,
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
from ..types.ip_connection import IPConnection
from ..types.encrypted_media import EncryptedMedia
from ..types.inbound_ip_param import InboundIPParam
from ..types.outbound_ip_param import OutboundIPParam
from ..types.anchorsite_override import AnchorsiteOverride
from ..types.ip_connection_create_response import IPConnectionCreateResponse
from ..types.ip_connection_delete_response import IPConnectionDeleteResponse
from ..types.ip_connection_update_response import IPConnectionUpdateResponse
from ..types.connection_rtcp_settings_param import ConnectionRtcpSettingsParam
from ..types.ip_connection_retrieve_response import IPConnectionRetrieveResponse
from ..types.shared_params.connection_noise_suppression_details import ConnectionNoiseSuppressionDetails

__all__ = ["IPConnectionsResource", "AsyncIPConnectionsResource"]


class IPConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return IPConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return IPConnectionsResourceWithStreamingResponse(self)

    def create(
        self,
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
        inbound: ip_connection_create_params.Inbound | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: ip_connection_create_params.JitterBuffer | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: OutboundIPParam | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transport_protocol: Literal["UDP", "TCP", "TLS"] | Omit = omit,
        webhook_api_version: Literal["1", "2"] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPConnectionCreateResponse:
        """
        Creates an IP connection.

        Args:
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
            "/ip_connections",
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
                ip_connection_create_params.IPConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPConnectionCreateResponse,
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
    ) -> IPConnectionRetrieveResponse:
        """
        Retrieves the details of an existing ip connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/ip_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPConnectionRetrieveResponse,
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
        inbound: InboundIPParam | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: ip_connection_update_params.JitterBuffer | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: OutboundIPParam | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transport_protocol: Literal["UDP", "TCP", "TLS"] | Omit = omit,
        webhook_api_version: Literal["1", "2"] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPConnectionUpdateResponse:
        """
        Updates settings of an existing IP connection.

        Args:
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/ip_connections/{id}",
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
                ip_connection_update_params.IPConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        filter: ip_connection_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "connection_name", "active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[IPConnection]:
        """
        Returns a list of your IP connections.

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
            "/ip_connections",
            page=SyncDefaultFlatPagination[IPConnection],
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
                    ip_connection_list_params.IPConnectionListParams,
                ),
            ),
            model=IPConnection,
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
    ) -> IPConnectionDeleteResponse:
        """
        Deletes an existing IP connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/ip_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPConnectionDeleteResponse,
        )


class AsyncIPConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncIPConnectionsResourceWithStreamingResponse(self)

    async def create(
        self,
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
        inbound: ip_connection_create_params.Inbound | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: ip_connection_create_params.JitterBuffer | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: OutboundIPParam | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transport_protocol: Literal["UDP", "TCP", "TLS"] | Omit = omit,
        webhook_api_version: Literal["1", "2"] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPConnectionCreateResponse:
        """
        Creates an IP connection.

        Args:
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
            "/ip_connections",
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
                ip_connection_create_params.IPConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPConnectionCreateResponse,
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
    ) -> IPConnectionRetrieveResponse:
        """
        Retrieves the details of an existing ip connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/ip_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPConnectionRetrieveResponse,
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
        inbound: InboundIPParam | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: ip_connection_update_params.JitterBuffer | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: OutboundIPParam | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transport_protocol: Literal["UDP", "TCP", "TLS"] | Omit = omit,
        webhook_api_version: Literal["1", "2"] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPConnectionUpdateResponse:
        """
        Updates settings of an existing IP connection.

        Args:
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/ip_connections/{id}",
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
                ip_connection_update_params.IPConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        filter: ip_connection_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "connection_name", "active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[IPConnection, AsyncDefaultFlatPagination[IPConnection]]:
        """
        Returns a list of your IP connections.

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
            "/ip_connections",
            page=AsyncDefaultFlatPagination[IPConnection],
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
                    ip_connection_list_params.IPConnectionListParams,
                ),
            ),
            model=IPConnection,
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
    ) -> IPConnectionDeleteResponse:
        """
        Deletes an existing IP connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/ip_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPConnectionDeleteResponse,
        )


class IPConnectionsResourceWithRawResponse:
    def __init__(self, ip_connections: IPConnectionsResource) -> None:
        self._ip_connections = ip_connections

        self.create = to_raw_response_wrapper(
            ip_connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ip_connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ip_connections.update,
        )
        self.list = to_raw_response_wrapper(
            ip_connections.list,
        )
        self.delete = to_raw_response_wrapper(
            ip_connections.delete,
        )


class AsyncIPConnectionsResourceWithRawResponse:
    def __init__(self, ip_connections: AsyncIPConnectionsResource) -> None:
        self._ip_connections = ip_connections

        self.create = async_to_raw_response_wrapper(
            ip_connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ip_connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ip_connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            ip_connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ip_connections.delete,
        )


class IPConnectionsResourceWithStreamingResponse:
    def __init__(self, ip_connections: IPConnectionsResource) -> None:
        self._ip_connections = ip_connections

        self.create = to_streamed_response_wrapper(
            ip_connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ip_connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ip_connections.update,
        )
        self.list = to_streamed_response_wrapper(
            ip_connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            ip_connections.delete,
        )


class AsyncIPConnectionsResourceWithStreamingResponse:
    def __init__(self, ip_connections: AsyncIPConnectionsResource) -> None:
        self._ip_connections = ip_connections

        self.create = async_to_streamed_response_wrapper(
            ip_connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ip_connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ip_connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ip_connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ip_connections.delete,
        )
