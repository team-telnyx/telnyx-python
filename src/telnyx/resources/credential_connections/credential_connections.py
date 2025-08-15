# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...types import (
    DtmfType,
    EncryptedMedia,
    AnchorsiteOverride,
    credential_connection_list_params,
    credential_connection_create_params,
    credential_connection_update_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.dtmf_type import DtmfType
from ...types.encrypted_media import EncryptedMedia
from ...types.anchorsite_override import AnchorsiteOverride
from ...types.credential_inbound_param import CredentialInboundParam
from ...types.credential_outbound_param import CredentialOutboundParam
from ...types.connection_rtcp_settings_param import ConnectionRtcpSettingsParam
from ...types.credential_connection_list_response import CredentialConnectionListResponse
from ...types.credential_connection_create_response import CredentialConnectionCreateResponse
from ...types.credential_connection_delete_response import CredentialConnectionDeleteResponse
from ...types.credential_connection_update_response import CredentialConnectionUpdateResponse
from ...types.credential_connection_retrieve_response import CredentialConnectionRetrieveResponse

__all__ = ["CredentialConnectionsResource", "AsyncCredentialConnectionsResource"]


class CredentialConnectionsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CredentialConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CredentialConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CredentialConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CredentialConnectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connection_name: str,
        password: str,
        user_name: str,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: AnchorsiteOverride | NotGiven = NOT_GIVEN,
        android_push_credential_id: Optional[str] | NotGiven = NOT_GIVEN,
        default_on_hold_comfort_noise_enabled: bool | NotGiven = NOT_GIVEN,
        dtmf_type: DtmfType | NotGiven = NOT_GIVEN,
        encode_contact_header_enabled: bool | NotGiven = NOT_GIVEN,
        encrypted_media: Optional[EncryptedMedia] | NotGiven = NOT_GIVEN,
        inbound: CredentialInboundParam | NotGiven = NOT_GIVEN,
        ios_push_credential_id: Optional[str] | NotGiven = NOT_GIVEN,
        onnet_t38_passthrough_enabled: bool | NotGiven = NOT_GIVEN,
        outbound: CredentialOutboundParam | NotGiven = NOT_GIVEN,
        rtcp_settings: ConnectionRtcpSettingsParam | NotGiven = NOT_GIVEN,
        sip_uri_calling_preference: Literal["disabled", "unrestricted", "internal"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2", "texml"] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_event_url: str | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialConnectionCreateResponse:
        """
        Creates a credential connection.

        Args:
          connection_name: A user-assigned name to help manage the connection.

          password: The password to be used as part of the credentials. Must be 8 to 128 characters
              long.

          user_name: The user name to be used as part of the credentials. Must be 4-32 characters
              long and alphanumeric values only (no spaces or special characters).

          active: Defaults to true

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          android_push_credential_id: The uuid of the push credential for Android

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

          onnet_t38_passthrough_enabled: Enable on-net T38 if you prefer the sender and receiver negotiating T38 directly
              if both are on the Telnyx network. If this is disabled, Telnyx will be able to
              use T38 on just one leg of the call depending on each leg's settings.

          sip_uri_calling_preference: This feature enables inbound SIP URI calls to your Credential Auth Connection.
              If enabled for all (unrestricted) then anyone who calls the SIP URI
              <your-username>@telnyx.com will be connected to your Connection. You can also
              choose to allow only calls that are originated on any Connections under your
              account (internal).

          tags: Tags associated with the connection.

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
            "/credential_connections",
            body=maybe_transform(
                {
                    "connection_name": connection_name,
                    "password": password,
                    "user_name": user_name,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "android_push_credential_id": android_push_credential_id,
                    "default_on_hold_comfort_noise_enabled": default_on_hold_comfort_noise_enabled,
                    "dtmf_type": dtmf_type,
                    "encode_contact_header_enabled": encode_contact_header_enabled,
                    "encrypted_media": encrypted_media,
                    "inbound": inbound,
                    "ios_push_credential_id": ios_push_credential_id,
                    "onnet_t38_passthrough_enabled": onnet_t38_passthrough_enabled,
                    "outbound": outbound,
                    "rtcp_settings": rtcp_settings,
                    "sip_uri_calling_preference": sip_uri_calling_preference,
                    "tags": tags,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                credential_connection_create_params.CredentialConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialConnectionCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialConnectionRetrieveResponse:
        """
        Retrieves the details of an existing credential connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/credential_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialConnectionRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: AnchorsiteOverride | NotGiven = NOT_GIVEN,
        android_push_credential_id: Optional[str] | NotGiven = NOT_GIVEN,
        connection_name: str | NotGiven = NOT_GIVEN,
        default_on_hold_comfort_noise_enabled: bool | NotGiven = NOT_GIVEN,
        dtmf_type: DtmfType | NotGiven = NOT_GIVEN,
        encode_contact_header_enabled: bool | NotGiven = NOT_GIVEN,
        encrypted_media: Optional[EncryptedMedia] | NotGiven = NOT_GIVEN,
        inbound: CredentialInboundParam | NotGiven = NOT_GIVEN,
        ios_push_credential_id: Optional[str] | NotGiven = NOT_GIVEN,
        onnet_t38_passthrough_enabled: bool | NotGiven = NOT_GIVEN,
        outbound: CredentialOutboundParam | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        rtcp_settings: ConnectionRtcpSettingsParam | NotGiven = NOT_GIVEN,
        sip_uri_calling_preference: Literal["disabled", "unrestricted", "internal"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        user_name: str | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2"] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_event_url: str | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialConnectionUpdateResponse:
        """
        Updates settings of an existing credential connection.

        Args:
          active: Defaults to true

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          android_push_credential_id: The uuid of the push credential for Android

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
            f"/credential_connections/{id}",
            body=maybe_transform(
                {
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "android_push_credential_id": android_push_credential_id,
                    "connection_name": connection_name,
                    "default_on_hold_comfort_noise_enabled": default_on_hold_comfort_noise_enabled,
                    "dtmf_type": dtmf_type,
                    "encode_contact_header_enabled": encode_contact_header_enabled,
                    "encrypted_media": encrypted_media,
                    "inbound": inbound,
                    "ios_push_credential_id": ios_push_credential_id,
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
                credential_connection_update_params.CredentialConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        filter: credential_connection_list_params.Filter | NotGiven = NOT_GIVEN,
        page: credential_connection_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "connection_name", "active"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialConnectionListResponse:
        """
        Returns a list of your credential connections.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[connection_name], filter[fqdn], filter[outbound_voice_profile_id],
              filter[outbound.outbound_voice_profile_id]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

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
        return self._get(
            "/credential_connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    credential_connection_list_params.CredentialConnectionListParams,
                ),
            ),
            cast_to=CredentialConnectionListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialConnectionDeleteResponse:
        """
        Deletes an existing credential connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/credential_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialConnectionDeleteResponse,
        )


class AsyncCredentialConnectionsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCredentialConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCredentialConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCredentialConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCredentialConnectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connection_name: str,
        password: str,
        user_name: str,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: AnchorsiteOverride | NotGiven = NOT_GIVEN,
        android_push_credential_id: Optional[str] | NotGiven = NOT_GIVEN,
        default_on_hold_comfort_noise_enabled: bool | NotGiven = NOT_GIVEN,
        dtmf_type: DtmfType | NotGiven = NOT_GIVEN,
        encode_contact_header_enabled: bool | NotGiven = NOT_GIVEN,
        encrypted_media: Optional[EncryptedMedia] | NotGiven = NOT_GIVEN,
        inbound: CredentialInboundParam | NotGiven = NOT_GIVEN,
        ios_push_credential_id: Optional[str] | NotGiven = NOT_GIVEN,
        onnet_t38_passthrough_enabled: bool | NotGiven = NOT_GIVEN,
        outbound: CredentialOutboundParam | NotGiven = NOT_GIVEN,
        rtcp_settings: ConnectionRtcpSettingsParam | NotGiven = NOT_GIVEN,
        sip_uri_calling_preference: Literal["disabled", "unrestricted", "internal"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2", "texml"] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_event_url: str | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialConnectionCreateResponse:
        """
        Creates a credential connection.

        Args:
          connection_name: A user-assigned name to help manage the connection.

          password: The password to be used as part of the credentials. Must be 8 to 128 characters
              long.

          user_name: The user name to be used as part of the credentials. Must be 4-32 characters
              long and alphanumeric values only (no spaces or special characters).

          active: Defaults to true

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          android_push_credential_id: The uuid of the push credential for Android

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

          onnet_t38_passthrough_enabled: Enable on-net T38 if you prefer the sender and receiver negotiating T38 directly
              if both are on the Telnyx network. If this is disabled, Telnyx will be able to
              use T38 on just one leg of the call depending on each leg's settings.

          sip_uri_calling_preference: This feature enables inbound SIP URI calls to your Credential Auth Connection.
              If enabled for all (unrestricted) then anyone who calls the SIP URI
              <your-username>@telnyx.com will be connected to your Connection. You can also
              choose to allow only calls that are originated on any Connections under your
              account (internal).

          tags: Tags associated with the connection.

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
            "/credential_connections",
            body=await async_maybe_transform(
                {
                    "connection_name": connection_name,
                    "password": password,
                    "user_name": user_name,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "android_push_credential_id": android_push_credential_id,
                    "default_on_hold_comfort_noise_enabled": default_on_hold_comfort_noise_enabled,
                    "dtmf_type": dtmf_type,
                    "encode_contact_header_enabled": encode_contact_header_enabled,
                    "encrypted_media": encrypted_media,
                    "inbound": inbound,
                    "ios_push_credential_id": ios_push_credential_id,
                    "onnet_t38_passthrough_enabled": onnet_t38_passthrough_enabled,
                    "outbound": outbound,
                    "rtcp_settings": rtcp_settings,
                    "sip_uri_calling_preference": sip_uri_calling_preference,
                    "tags": tags,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                credential_connection_create_params.CredentialConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialConnectionCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialConnectionRetrieveResponse:
        """
        Retrieves the details of an existing credential connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/credential_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialConnectionRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: AnchorsiteOverride | NotGiven = NOT_GIVEN,
        android_push_credential_id: Optional[str] | NotGiven = NOT_GIVEN,
        connection_name: str | NotGiven = NOT_GIVEN,
        default_on_hold_comfort_noise_enabled: bool | NotGiven = NOT_GIVEN,
        dtmf_type: DtmfType | NotGiven = NOT_GIVEN,
        encode_contact_header_enabled: bool | NotGiven = NOT_GIVEN,
        encrypted_media: Optional[EncryptedMedia] | NotGiven = NOT_GIVEN,
        inbound: CredentialInboundParam | NotGiven = NOT_GIVEN,
        ios_push_credential_id: Optional[str] | NotGiven = NOT_GIVEN,
        onnet_t38_passthrough_enabled: bool | NotGiven = NOT_GIVEN,
        outbound: CredentialOutboundParam | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        rtcp_settings: ConnectionRtcpSettingsParam | NotGiven = NOT_GIVEN,
        sip_uri_calling_preference: Literal["disabled", "unrestricted", "internal"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        user_name: str | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2"] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_event_url: str | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialConnectionUpdateResponse:
        """
        Updates settings of an existing credential connection.

        Args:
          active: Defaults to true

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          android_push_credential_id: The uuid of the push credential for Android

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
            f"/credential_connections/{id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "android_push_credential_id": android_push_credential_id,
                    "connection_name": connection_name,
                    "default_on_hold_comfort_noise_enabled": default_on_hold_comfort_noise_enabled,
                    "dtmf_type": dtmf_type,
                    "encode_contact_header_enabled": encode_contact_header_enabled,
                    "encrypted_media": encrypted_media,
                    "inbound": inbound,
                    "ios_push_credential_id": ios_push_credential_id,
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
                credential_connection_update_params.CredentialConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialConnectionUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: credential_connection_list_params.Filter | NotGiven = NOT_GIVEN,
        page: credential_connection_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "connection_name", "active"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialConnectionListResponse:
        """
        Returns a list of your credential connections.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[connection_name], filter[fqdn], filter[outbound_voice_profile_id],
              filter[outbound.outbound_voice_profile_id]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

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
        return await self._get(
            "/credential_connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    credential_connection_list_params.CredentialConnectionListParams,
                ),
            ),
            cast_to=CredentialConnectionListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialConnectionDeleteResponse:
        """
        Deletes an existing credential connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/credential_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialConnectionDeleteResponse,
        )


class CredentialConnectionsResourceWithRawResponse:
    def __init__(self, credential_connections: CredentialConnectionsResource) -> None:
        self._credential_connections = credential_connections

        self.create = to_raw_response_wrapper(
            credential_connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            credential_connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            credential_connections.update,
        )
        self.list = to_raw_response_wrapper(
            credential_connections.list,
        )
        self.delete = to_raw_response_wrapper(
            credential_connections.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._credential_connections.actions)


class AsyncCredentialConnectionsResourceWithRawResponse:
    def __init__(self, credential_connections: AsyncCredentialConnectionsResource) -> None:
        self._credential_connections = credential_connections

        self.create = async_to_raw_response_wrapper(
            credential_connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            credential_connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            credential_connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            credential_connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            credential_connections.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._credential_connections.actions)


class CredentialConnectionsResourceWithStreamingResponse:
    def __init__(self, credential_connections: CredentialConnectionsResource) -> None:
        self._credential_connections = credential_connections

        self.create = to_streamed_response_wrapper(
            credential_connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            credential_connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            credential_connections.update,
        )
        self.list = to_streamed_response_wrapper(
            credential_connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            credential_connections.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._credential_connections.actions)


class AsyncCredentialConnectionsResourceWithStreamingResponse:
    def __init__(self, credential_connections: AsyncCredentialConnectionsResource) -> None:
        self._credential_connections = credential_connections

        self.create = async_to_streamed_response_wrapper(
            credential_connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            credential_connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            credential_connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            credential_connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            credential_connections.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._credential_connections.actions)
