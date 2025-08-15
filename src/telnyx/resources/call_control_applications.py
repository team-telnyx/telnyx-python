# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    call_control_application_list_params,
    call_control_application_create_params,
    call_control_application_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.call_control_application_inbound_param import CallControlApplicationInboundParam
from ..types.call_control_application_list_response import CallControlApplicationListResponse
from ..types.call_control_application_outbound_param import CallControlApplicationOutboundParam
from ..types.call_control_application_create_response import CallControlApplicationCreateResponse
from ..types.call_control_application_delete_response import CallControlApplicationDeleteResponse
from ..types.call_control_application_update_response import CallControlApplicationUpdateResponse
from ..types.call_control_application_retrieve_response import CallControlApplicationRetrieveResponse

__all__ = ["CallControlApplicationsResource", "AsyncCallControlApplicationsResource"]


class CallControlApplicationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallControlApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CallControlApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallControlApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CallControlApplicationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        application_name: str,
        webhook_event_url: str,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: Literal['"Latency"', '"Chicago, IL"', '"Ashburn, VA"', '"San Jose, CA"']
        | NotGiven = NOT_GIVEN,
        dtmf_type: Literal["RFC 2833", "Inband", "SIP INFO"] | NotGiven = NOT_GIVEN,
        first_command_timeout: bool | NotGiven = NOT_GIVEN,
        first_command_timeout_secs: int | NotGiven = NOT_GIVEN,
        inbound: CallControlApplicationInboundParam | NotGiven = NOT_GIVEN,
        outbound: CallControlApplicationOutboundParam | NotGiven = NOT_GIVEN,
        redact_dtmf_debug_logging: bool | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2"] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallControlApplicationCreateResponse:
        """
        Create a call control application.

        Args:
          application_name: A user-assigned name to help manage the application.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          active: Specifies whether the connection can be used.

          anchorsite_override: <code>Latency</code> directs Telnyx to route media through the site with the
              lowest round-trip time to the user's connection. Telnyx calculates this time
              using ICMP ping messages. This can be disabled by specifying a site to handle
              all media.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          first_command_timeout: Specifies whether calls to phone numbers associated with this connection should
              hangup after timing out.

          first_command_timeout_secs: Specifies how many seconds to wait before timing out a dial command.

          redact_dtmf_debug_logging: When enabled, DTMF digits entered by users will be redacted in debug logs to
              protect PII data entered through IVR interactions.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1 or v2.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/call_control_applications",
            body=maybe_transform(
                {
                    "application_name": application_name,
                    "webhook_event_url": webhook_event_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "dtmf_type": dtmf_type,
                    "first_command_timeout": first_command_timeout,
                    "first_command_timeout_secs": first_command_timeout_secs,
                    "inbound": inbound,
                    "outbound": outbound,
                    "redact_dtmf_debug_logging": redact_dtmf_debug_logging,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                call_control_application_create_params.CallControlApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallControlApplicationCreateResponse,
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
    ) -> CallControlApplicationRetrieveResponse:
        """
        Retrieves the details of an existing call control application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/call_control_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallControlApplicationRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        application_name: str,
        webhook_event_url: str,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: Literal['"Latency"', '"Chicago, IL"', '"Ashburn, VA"', '"San Jose, CA"']
        | NotGiven = NOT_GIVEN,
        dtmf_type: Literal["RFC 2833", "Inband", "SIP INFO"] | NotGiven = NOT_GIVEN,
        first_command_timeout: bool | NotGiven = NOT_GIVEN,
        first_command_timeout_secs: int | NotGiven = NOT_GIVEN,
        inbound: CallControlApplicationInboundParam | NotGiven = NOT_GIVEN,
        outbound: CallControlApplicationOutboundParam | NotGiven = NOT_GIVEN,
        redact_dtmf_debug_logging: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2"] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallControlApplicationUpdateResponse:
        """
        Updates settings of an existing call control application.

        Args:
          application_name: A user-assigned name to help manage the application.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          active: Specifies whether the connection can be used.

          anchorsite_override: <code>Latency</code> directs Telnyx to route media through the site with the
              lowest round-trip time to the user's connection. Telnyx calculates this time
              using ICMP ping messages. This can be disabled by specifying a site to handle
              all media.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          first_command_timeout: Specifies whether calls to phone numbers associated with this connection should
              hangup after timing out.

          first_command_timeout_secs: Specifies how many seconds to wait before timing out a dial command.

          redact_dtmf_debug_logging: When enabled, DTMF digits entered by users will be redacted in debug logs to
              protect PII data entered through IVR interactions.

          tags: Tags assigned to the Call Control Application.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1 or v2.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/call_control_applications/{id}",
            body=maybe_transform(
                {
                    "application_name": application_name,
                    "webhook_event_url": webhook_event_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "dtmf_type": dtmf_type,
                    "first_command_timeout": first_command_timeout,
                    "first_command_timeout_secs": first_command_timeout_secs,
                    "inbound": inbound,
                    "outbound": outbound,
                    "redact_dtmf_debug_logging": redact_dtmf_debug_logging,
                    "tags": tags,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                call_control_application_update_params.CallControlApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallControlApplicationUpdateResponse,
        )

    def list(
        self,
        *,
        filter: call_control_application_list_params.Filter | NotGiven = NOT_GIVEN,
        page: call_control_application_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "connection_name", "active"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallControlApplicationListResponse:
        """
        Return a list of call control applications.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[application_name][contains], filter[outbound.outbound_voice_profile_id],
              filter[leg_id], filter[application_session_id], filter[connection_id],
              filter[product], filter[failed], filter[from], filter[to], filter[name],
              filter[type], filter[occurred_at][eq/gt/gte/lt/lte], filter[status]

          page: Consolidated page parameter (deepObject style). Originally: page[after],
              page[before], page[limit], page[size], page[number]

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
            "/call_control_applications",
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
                    call_control_application_list_params.CallControlApplicationListParams,
                ),
            ),
            cast_to=CallControlApplicationListResponse,
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
    ) -> CallControlApplicationDeleteResponse:
        """
        Deletes a call control application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/call_control_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallControlApplicationDeleteResponse,
        )


class AsyncCallControlApplicationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallControlApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallControlApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallControlApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCallControlApplicationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        application_name: str,
        webhook_event_url: str,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: Literal['"Latency"', '"Chicago, IL"', '"Ashburn, VA"', '"San Jose, CA"']
        | NotGiven = NOT_GIVEN,
        dtmf_type: Literal["RFC 2833", "Inband", "SIP INFO"] | NotGiven = NOT_GIVEN,
        first_command_timeout: bool | NotGiven = NOT_GIVEN,
        first_command_timeout_secs: int | NotGiven = NOT_GIVEN,
        inbound: CallControlApplicationInboundParam | NotGiven = NOT_GIVEN,
        outbound: CallControlApplicationOutboundParam | NotGiven = NOT_GIVEN,
        redact_dtmf_debug_logging: bool | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2"] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallControlApplicationCreateResponse:
        """
        Create a call control application.

        Args:
          application_name: A user-assigned name to help manage the application.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          active: Specifies whether the connection can be used.

          anchorsite_override: <code>Latency</code> directs Telnyx to route media through the site with the
              lowest round-trip time to the user's connection. Telnyx calculates this time
              using ICMP ping messages. This can be disabled by specifying a site to handle
              all media.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          first_command_timeout: Specifies whether calls to phone numbers associated with this connection should
              hangup after timing out.

          first_command_timeout_secs: Specifies how many seconds to wait before timing out a dial command.

          redact_dtmf_debug_logging: When enabled, DTMF digits entered by users will be redacted in debug logs to
              protect PII data entered through IVR interactions.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1 or v2.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/call_control_applications",
            body=await async_maybe_transform(
                {
                    "application_name": application_name,
                    "webhook_event_url": webhook_event_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "dtmf_type": dtmf_type,
                    "first_command_timeout": first_command_timeout,
                    "first_command_timeout_secs": first_command_timeout_secs,
                    "inbound": inbound,
                    "outbound": outbound,
                    "redact_dtmf_debug_logging": redact_dtmf_debug_logging,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                call_control_application_create_params.CallControlApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallControlApplicationCreateResponse,
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
    ) -> CallControlApplicationRetrieveResponse:
        """
        Retrieves the details of an existing call control application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/call_control_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallControlApplicationRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        application_name: str,
        webhook_event_url: str,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: Literal['"Latency"', '"Chicago, IL"', '"Ashburn, VA"', '"San Jose, CA"']
        | NotGiven = NOT_GIVEN,
        dtmf_type: Literal["RFC 2833", "Inband", "SIP INFO"] | NotGiven = NOT_GIVEN,
        first_command_timeout: bool | NotGiven = NOT_GIVEN,
        first_command_timeout_secs: int | NotGiven = NOT_GIVEN,
        inbound: CallControlApplicationInboundParam | NotGiven = NOT_GIVEN,
        outbound: CallControlApplicationOutboundParam | NotGiven = NOT_GIVEN,
        redact_dtmf_debug_logging: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2"] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallControlApplicationUpdateResponse:
        """
        Updates settings of an existing call control application.

        Args:
          application_name: A user-assigned name to help manage the application.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          active: Specifies whether the connection can be used.

          anchorsite_override: <code>Latency</code> directs Telnyx to route media through the site with the
              lowest round-trip time to the user's connection. Telnyx calculates this time
              using ICMP ping messages. This can be disabled by specifying a site to handle
              all media.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          first_command_timeout: Specifies whether calls to phone numbers associated with this connection should
              hangup after timing out.

          first_command_timeout_secs: Specifies how many seconds to wait before timing out a dial command.

          redact_dtmf_debug_logging: When enabled, DTMF digits entered by users will be redacted in debug logs to
              protect PII data entered through IVR interactions.

          tags: Tags assigned to the Call Control Application.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1 or v2.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/call_control_applications/{id}",
            body=await async_maybe_transform(
                {
                    "application_name": application_name,
                    "webhook_event_url": webhook_event_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "dtmf_type": dtmf_type,
                    "first_command_timeout": first_command_timeout,
                    "first_command_timeout_secs": first_command_timeout_secs,
                    "inbound": inbound,
                    "outbound": outbound,
                    "redact_dtmf_debug_logging": redact_dtmf_debug_logging,
                    "tags": tags,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                call_control_application_update_params.CallControlApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallControlApplicationUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: call_control_application_list_params.Filter | NotGiven = NOT_GIVEN,
        page: call_control_application_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "connection_name", "active"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallControlApplicationListResponse:
        """
        Return a list of call control applications.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[application_name][contains], filter[outbound.outbound_voice_profile_id],
              filter[leg_id], filter[application_session_id], filter[connection_id],
              filter[product], filter[failed], filter[from], filter[to], filter[name],
              filter[type], filter[occurred_at][eq/gt/gte/lt/lte], filter[status]

          page: Consolidated page parameter (deepObject style). Originally: page[after],
              page[before], page[limit], page[size], page[number]

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
            "/call_control_applications",
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
                    call_control_application_list_params.CallControlApplicationListParams,
                ),
            ),
            cast_to=CallControlApplicationListResponse,
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
    ) -> CallControlApplicationDeleteResponse:
        """
        Deletes a call control application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/call_control_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallControlApplicationDeleteResponse,
        )


class CallControlApplicationsResourceWithRawResponse:
    def __init__(self, call_control_applications: CallControlApplicationsResource) -> None:
        self._call_control_applications = call_control_applications

        self.create = to_raw_response_wrapper(
            call_control_applications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            call_control_applications.retrieve,
        )
        self.update = to_raw_response_wrapper(
            call_control_applications.update,
        )
        self.list = to_raw_response_wrapper(
            call_control_applications.list,
        )
        self.delete = to_raw_response_wrapper(
            call_control_applications.delete,
        )


class AsyncCallControlApplicationsResourceWithRawResponse:
    def __init__(self, call_control_applications: AsyncCallControlApplicationsResource) -> None:
        self._call_control_applications = call_control_applications

        self.create = async_to_raw_response_wrapper(
            call_control_applications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            call_control_applications.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            call_control_applications.update,
        )
        self.list = async_to_raw_response_wrapper(
            call_control_applications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            call_control_applications.delete,
        )


class CallControlApplicationsResourceWithStreamingResponse:
    def __init__(self, call_control_applications: CallControlApplicationsResource) -> None:
        self._call_control_applications = call_control_applications

        self.create = to_streamed_response_wrapper(
            call_control_applications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            call_control_applications.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            call_control_applications.update,
        )
        self.list = to_streamed_response_wrapper(
            call_control_applications.list,
        )
        self.delete = to_streamed_response_wrapper(
            call_control_applications.delete,
        )


class AsyncCallControlApplicationsResourceWithStreamingResponse:
    def __init__(self, call_control_applications: AsyncCallControlApplicationsResource) -> None:
        self._call_control_applications = call_control_applications

        self.create = async_to_streamed_response_wrapper(
            call_control_applications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            call_control_applications.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            call_control_applications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            call_control_applications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            call_control_applications.delete,
        )
