# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import (
    DtmfType,
    EncryptedMedia,
    AnchorsiteOverride,
    uac_connection_list_params,
    uac_connection_create_params,
    uac_connection_update_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.dtmf_type import DtmfType
from ...types.encrypted_media import EncryptedMedia
from ...types.anchorsite_override import AnchorsiteOverride
from ...types.uac_connection_list_response import UacConnectionListResponse
from ...types.connection_rtcp_settings_param import ConnectionRtcpSettingsParam
from ...types.uac_connection_create_response import UacConnectionCreateResponse
from ...types.uac_connection_delete_response import UacConnectionDeleteResponse
from ...types.uac_connection_update_response import UacConnectionUpdateResponse
from ...types.uac_connection_retrieve_response import UacConnectionRetrieveResponse
from ...types.shared_params.connection_jitter_buffer import ConnectionJitterBuffer
from ...types.shared_params.connection_noise_suppression_details import ConnectionNoiseSuppressionDetails

__all__ = ["UacConnectionsResource", "AsyncUacConnectionsResource"]


class UacConnectionsResource(SyncAPIResource):
    """UAC connection operations"""

    @cached_property
    def actions(self) -> ActionsResource:
        """UAC connection operations"""
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> UacConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UacConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UacConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return UacConnectionsResourceWithStreamingResponse(self)

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
        external_uac_settings: uac_connection_create_params.ExternalUacSettings | Omit = omit,
        inbound: uac_connection_create_params.Inbound | Omit = omit,
        internal_uac_settings: uac_connection_create_params.InternalUacSettings | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: ConnectionJitterBuffer | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: uac_connection_create_params.Outbound | Omit = omit,
        password: str | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        sip_uri_calling_preference: Literal["disabled", "unrestricted", "internal"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        user_name: str | Omit = omit,
        webhook_api_version: Literal["1", "2", "texml"] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UacConnectionCreateResponse:
        """Creates a UAC connection.

        A UAC (User Agent Client) Connection registers Telnyx
        to your PBX — the opposite of a standard SIP trunk, where the PBX registers to
        Telnyx. Use UAC when your PBX doesn’t support outbound SIP registration or you
        need Telnyx to maintain the registration.

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

          external_uac_settings: External SIP peer settings used by Telnyx when registering to your PBX and
              routing outbound calls.

          inbound: Inbound settings that can be supplied when creating or updating a UAC
              connection. The SIP subdomain fields returned in UAC connection responses are
              generated by Telnyx and are not accepted as request parameters.

          internal_uac_settings: Internal Telnyx-side settings for a UAC connection.

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

          password: The password to be used as part of the credentials. Must be 8 to 128 characters
              long.

          sip_uri_calling_preference: This feature enables inbound SIP URI calls to your Credential Auth Connection.
              If enabled for all (unrestricted) then anyone who calls the SIP URI
              <your-username>@telnyx.com will be connected to your Connection. You can also
              choose to allow only calls that are originated on any Connections under your
              account (internal).

          tags: Tags associated with the connection.

          user_name: The user name to be used as part of the credentials. Must be 4-32 characters
              long and alphanumeric values only (no spaces or special characters).

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1, v2 or texml. Note -
              texml can only be set when the outbound object parameter call_parking_enabled is
              included and set to true.

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
            "/uac_connections",
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
                    "external_uac_settings": external_uac_settings,
                    "inbound": inbound,
                    "internal_uac_settings": internal_uac_settings,
                    "ios_push_credential_id": ios_push_credential_id,
                    "jitter_buffer": jitter_buffer,
                    "noise_suppression": noise_suppression,
                    "noise_suppression_details": noise_suppression_details,
                    "onnet_t38_passthrough_enabled": onnet_t38_passthrough_enabled,
                    "outbound": outbound,
                    "password": password,
                    "rtcp_settings": rtcp_settings,
                    "sip_uri_calling_preference": sip_uri_calling_preference,
                    "tags": tags,
                    "user_name": user_name,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                uac_connection_create_params.UacConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UacConnectionCreateResponse,
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
    ) -> UacConnectionRetrieveResponse:
        """
        Retrieves the details of an existing UAC connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/uac_connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UacConnectionRetrieveResponse,
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
        external_uac_settings: uac_connection_update_params.ExternalUacSettings | Omit = omit,
        inbound: uac_connection_update_params.Inbound | Omit = omit,
        internal_uac_settings: uac_connection_update_params.InternalUacSettings | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: ConnectionJitterBuffer | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: uac_connection_update_params.Outbound | Omit = omit,
        password: str | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        sip_uri_calling_preference: Literal["disabled", "unrestricted", "internal"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        user_name: str | Omit = omit,
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
    ) -> UacConnectionUpdateResponse:
        """
        Updates settings of an existing UAC connection.

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

          external_uac_settings: External SIP peer settings used by Telnyx when registering to your PBX and
              routing outbound calls.

          inbound: Inbound settings that can be supplied when creating or updating a UAC
              connection. The SIP subdomain fields returned in UAC connection responses are
              generated by Telnyx and are not accepted as request parameters.

          internal_uac_settings: Internal Telnyx-side settings for a UAC connection.

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

          password: The password to be used as part of the credentials. Must be 8 to 128 characters
              long.

          sip_uri_calling_preference: This feature enables inbound SIP URI calls to your Credential Auth Connection.
              If enabled for all (unrestricted) then anyone who calls the SIP URI
              <your-username>@telnyx.com will be connected to your Connection. You can also
              choose to allow only calls that are originated on any Connections under your
              account (internal).

          tags: Tags associated with the connection.

          user_name: The user name to be used as part of the credentials. Must be 4-32 characters
              long and alphanumeric values only (no spaces or special characters).

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
            path_template("/uac_connections/{id}", id=id),
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
                    "external_uac_settings": external_uac_settings,
                    "inbound": inbound,
                    "internal_uac_settings": internal_uac_settings,
                    "ios_push_credential_id": ios_push_credential_id,
                    "jitter_buffer": jitter_buffer,
                    "noise_suppression": noise_suppression,
                    "noise_suppression_details": noise_suppression_details,
                    "onnet_t38_passthrough_enabled": onnet_t38_passthrough_enabled,
                    "outbound": outbound,
                    "password": password,
                    "rtcp_settings": rtcp_settings,
                    "sip_uri_calling_preference": sip_uri_calling_preference,
                    "tags": tags,
                    "user_name": user_name,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                uac_connection_update_params.UacConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UacConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        filter: uac_connection_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "connection_name", "active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[UacConnectionListResponse]:
        """Returns a list of your UAC connections.

        A UAC (User Agent Client) Connection
        registers Telnyx to your PBX — the opposite of a standard SIP trunk, where the
        PBX registers to Telnyx. Use UAC when your PBX doesn’t support outbound SIP
        registration or you need Telnyx to maintain the registration.

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
            "/uac_connections",
            page=SyncDefaultFlatPagination[UacConnectionListResponse],
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
                    uac_connection_list_params.UacConnectionListParams,
                ),
            ),
            model=UacConnectionListResponse,
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
    ) -> UacConnectionDeleteResponse:
        """
        Deletes an existing UAC connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/uac_connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UacConnectionDeleteResponse,
        )


class AsyncUacConnectionsResource(AsyncAPIResource):
    """UAC connection operations"""

    @cached_property
    def actions(self) -> AsyncActionsResource:
        """UAC connection operations"""
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUacConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUacConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUacConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncUacConnectionsResourceWithStreamingResponse(self)

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
        external_uac_settings: uac_connection_create_params.ExternalUacSettings | Omit = omit,
        inbound: uac_connection_create_params.Inbound | Omit = omit,
        internal_uac_settings: uac_connection_create_params.InternalUacSettings | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: ConnectionJitterBuffer | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: uac_connection_create_params.Outbound | Omit = omit,
        password: str | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        sip_uri_calling_preference: Literal["disabled", "unrestricted", "internal"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        user_name: str | Omit = omit,
        webhook_api_version: Literal["1", "2", "texml"] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UacConnectionCreateResponse:
        """Creates a UAC connection.

        A UAC (User Agent Client) Connection registers Telnyx
        to your PBX — the opposite of a standard SIP trunk, where the PBX registers to
        Telnyx. Use UAC when your PBX doesn’t support outbound SIP registration or you
        need Telnyx to maintain the registration.

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

          external_uac_settings: External SIP peer settings used by Telnyx when registering to your PBX and
              routing outbound calls.

          inbound: Inbound settings that can be supplied when creating or updating a UAC
              connection. The SIP subdomain fields returned in UAC connection responses are
              generated by Telnyx and are not accepted as request parameters.

          internal_uac_settings: Internal Telnyx-side settings for a UAC connection.

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

          password: The password to be used as part of the credentials. Must be 8 to 128 characters
              long.

          sip_uri_calling_preference: This feature enables inbound SIP URI calls to your Credential Auth Connection.
              If enabled for all (unrestricted) then anyone who calls the SIP URI
              <your-username>@telnyx.com will be connected to your Connection. You can also
              choose to allow only calls that are originated on any Connections under your
              account (internal).

          tags: Tags associated with the connection.

          user_name: The user name to be used as part of the credentials. Must be 4-32 characters
              long and alphanumeric values only (no spaces or special characters).

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1, v2 or texml. Note -
              texml can only be set when the outbound object parameter call_parking_enabled is
              included and set to true.

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
            "/uac_connections",
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
                    "external_uac_settings": external_uac_settings,
                    "inbound": inbound,
                    "internal_uac_settings": internal_uac_settings,
                    "ios_push_credential_id": ios_push_credential_id,
                    "jitter_buffer": jitter_buffer,
                    "noise_suppression": noise_suppression,
                    "noise_suppression_details": noise_suppression_details,
                    "onnet_t38_passthrough_enabled": onnet_t38_passthrough_enabled,
                    "outbound": outbound,
                    "password": password,
                    "rtcp_settings": rtcp_settings,
                    "sip_uri_calling_preference": sip_uri_calling_preference,
                    "tags": tags,
                    "user_name": user_name,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                uac_connection_create_params.UacConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UacConnectionCreateResponse,
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
    ) -> UacConnectionRetrieveResponse:
        """
        Retrieves the details of an existing UAC connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/uac_connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UacConnectionRetrieveResponse,
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
        external_uac_settings: uac_connection_update_params.ExternalUacSettings | Omit = omit,
        inbound: uac_connection_update_params.Inbound | Omit = omit,
        internal_uac_settings: uac_connection_update_params.InternalUacSettings | Omit = omit,
        ios_push_credential_id: Optional[str] | Omit = omit,
        jitter_buffer: ConnectionJitterBuffer | Omit = omit,
        noise_suppression: Literal["inbound", "outbound", "both", "disabled"] | Omit = omit,
        noise_suppression_details: ConnectionNoiseSuppressionDetails | Omit = omit,
        onnet_t38_passthrough_enabled: bool | Omit = omit,
        outbound: uac_connection_update_params.Outbound | Omit = omit,
        password: str | Omit = omit,
        rtcp_settings: ConnectionRtcpSettingsParam | Omit = omit,
        sip_uri_calling_preference: Literal["disabled", "unrestricted", "internal"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        user_name: str | Omit = omit,
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
    ) -> UacConnectionUpdateResponse:
        """
        Updates settings of an existing UAC connection.

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

          external_uac_settings: External SIP peer settings used by Telnyx when registering to your PBX and
              routing outbound calls.

          inbound: Inbound settings that can be supplied when creating or updating a UAC
              connection. The SIP subdomain fields returned in UAC connection responses are
              generated by Telnyx and are not accepted as request parameters.

          internal_uac_settings: Internal Telnyx-side settings for a UAC connection.

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

          password: The password to be used as part of the credentials. Must be 8 to 128 characters
              long.

          sip_uri_calling_preference: This feature enables inbound SIP URI calls to your Credential Auth Connection.
              If enabled for all (unrestricted) then anyone who calls the SIP URI
              <your-username>@telnyx.com will be connected to your Connection. You can also
              choose to allow only calls that are originated on any Connections under your
              account (internal).

          tags: Tags associated with the connection.

          user_name: The user name to be used as part of the credentials. Must be 4-32 characters
              long and alphanumeric values only (no spaces or special characters).

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
            path_template("/uac_connections/{id}", id=id),
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
                    "external_uac_settings": external_uac_settings,
                    "inbound": inbound,
                    "internal_uac_settings": internal_uac_settings,
                    "ios_push_credential_id": ios_push_credential_id,
                    "jitter_buffer": jitter_buffer,
                    "noise_suppression": noise_suppression,
                    "noise_suppression_details": noise_suppression_details,
                    "onnet_t38_passthrough_enabled": onnet_t38_passthrough_enabled,
                    "outbound": outbound,
                    "password": password,
                    "rtcp_settings": rtcp_settings,
                    "sip_uri_calling_preference": sip_uri_calling_preference,
                    "tags": tags,
                    "user_name": user_name,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                uac_connection_update_params.UacConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UacConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        filter: uac_connection_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "connection_name", "active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UacConnectionListResponse, AsyncDefaultFlatPagination[UacConnectionListResponse]]:
        """Returns a list of your UAC connections.

        A UAC (User Agent Client) Connection
        registers Telnyx to your PBX — the opposite of a standard SIP trunk, where the
        PBX registers to Telnyx. Use UAC when your PBX doesn’t support outbound SIP
        registration or you need Telnyx to maintain the registration.

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
            "/uac_connections",
            page=AsyncDefaultFlatPagination[UacConnectionListResponse],
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
                    uac_connection_list_params.UacConnectionListParams,
                ),
            ),
            model=UacConnectionListResponse,
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
    ) -> UacConnectionDeleteResponse:
        """
        Deletes an existing UAC connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/uac_connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UacConnectionDeleteResponse,
        )


class UacConnectionsResourceWithRawResponse:
    def __init__(self, uac_connections: UacConnectionsResource) -> None:
        self._uac_connections = uac_connections

        self.create = to_raw_response_wrapper(
            uac_connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            uac_connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            uac_connections.update,
        )
        self.list = to_raw_response_wrapper(
            uac_connections.list,
        )
        self.delete = to_raw_response_wrapper(
            uac_connections.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """UAC connection operations"""
        return ActionsResourceWithRawResponse(self._uac_connections.actions)


class AsyncUacConnectionsResourceWithRawResponse:
    def __init__(self, uac_connections: AsyncUacConnectionsResource) -> None:
        self._uac_connections = uac_connections

        self.create = async_to_raw_response_wrapper(
            uac_connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            uac_connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            uac_connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            uac_connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            uac_connections.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """UAC connection operations"""
        return AsyncActionsResourceWithRawResponse(self._uac_connections.actions)


class UacConnectionsResourceWithStreamingResponse:
    def __init__(self, uac_connections: UacConnectionsResource) -> None:
        self._uac_connections = uac_connections

        self.create = to_streamed_response_wrapper(
            uac_connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            uac_connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            uac_connections.update,
        )
        self.list = to_streamed_response_wrapper(
            uac_connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            uac_connections.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """UAC connection operations"""
        return ActionsResourceWithStreamingResponse(self._uac_connections.actions)


class AsyncUacConnectionsResourceWithStreamingResponse:
    def __init__(self, uac_connections: AsyncUacConnectionsResource) -> None:
        self._uac_connections = uac_connections

        self.create = async_to_streamed_response_wrapper(
            uac_connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            uac_connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            uac_connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            uac_connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            uac_connections.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """UAC connection operations"""
        return AsyncActionsResourceWithStreamingResponse(self._uac_connections.actions)
