# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    DtmfType,
    AnchorsiteOverride,
    texml_application_list_params,
    texml_application_create_params,
    texml_application_update_params,
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
from ..types.dtmf_type import DtmfType
from ..types.anchorsite_override import AnchorsiteOverride
from ..types.texml_application_list_response import TexmlApplicationListResponse
from ..types.texml_application_create_response import TexmlApplicationCreateResponse
from ..types.texml_application_delete_response import TexmlApplicationDeleteResponse
from ..types.texml_application_update_response import TexmlApplicationUpdateResponse
from ..types.texml_application_retrieve_response import TexmlApplicationRetrieveResponse

__all__ = ["TexmlApplicationsResource", "AsyncTexmlApplicationsResource"]


class TexmlApplicationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TexmlApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TexmlApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TexmlApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TexmlApplicationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        friendly_name: str,
        voice_url: str,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: AnchorsiteOverride | NotGiven = NOT_GIVEN,
        dtmf_type: DtmfType | NotGiven = NOT_GIVEN,
        first_command_timeout: bool | NotGiven = NOT_GIVEN,
        first_command_timeout_secs: int | NotGiven = NOT_GIVEN,
        inbound: texml_application_create_params.Inbound | NotGiven = NOT_GIVEN,
        outbound: texml_application_create_params.Outbound | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["get", "post"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        voice_fallback_url: str | NotGiven = NOT_GIVEN,
        voice_method: Literal["get", "post"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TexmlApplicationCreateResponse:
        """
        Creates a TeXML Application.

        Args:
          friendly_name: A user-assigned name to help manage the application.

          voice_url: URL to which Telnyx will deliver your XML Translator webhooks.

          active: Specifies whether the connection can be used.

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          first_command_timeout: Specifies whether calls to phone numbers associated with this connection should
              hangup after timing out.

          first_command_timeout_secs: Specifies how many seconds to wait before timing out a dial command.

          status_callback: URL for Telnyx to send requests to containing information about call progress
              events.

          status_callback_method: HTTP request method Telnyx should use when requesting the status_callback URL.

          tags: Tags associated with the Texml Application.

          voice_fallback_url: URL to which Telnyx will deliver your XML Translator webhooks if we get an error
              response from your voice_url.

          voice_method: HTTP request method Telnyx will use to interact with your XML Translator
              webhooks. Either 'get' or 'post'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/texml_applications",
            body=maybe_transform(
                {
                    "friendly_name": friendly_name,
                    "voice_url": voice_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "dtmf_type": dtmf_type,
                    "first_command_timeout": first_command_timeout,
                    "first_command_timeout_secs": first_command_timeout_secs,
                    "inbound": inbound,
                    "outbound": outbound,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "tags": tags,
                    "voice_fallback_url": voice_fallback_url,
                    "voice_method": voice_method,
                },
                texml_application_create_params.TexmlApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlApplicationCreateResponse,
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
    ) -> TexmlApplicationRetrieveResponse:
        """
        Retrieves the details of an existing TeXML Application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/texml_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlApplicationRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        friendly_name: str,
        voice_url: str,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: AnchorsiteOverride | NotGiven = NOT_GIVEN,
        dtmf_type: DtmfType | NotGiven = NOT_GIVEN,
        first_command_timeout: bool | NotGiven = NOT_GIVEN,
        first_command_timeout_secs: int | NotGiven = NOT_GIVEN,
        inbound: texml_application_update_params.Inbound | NotGiven = NOT_GIVEN,
        outbound: texml_application_update_params.Outbound | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["get", "post"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        voice_fallback_url: str | NotGiven = NOT_GIVEN,
        voice_method: Literal["get", "post"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TexmlApplicationUpdateResponse:
        """
        Updates settings of an existing TeXML Application.

        Args:
          friendly_name: A user-assigned name to help manage the application.

          voice_url: URL to which Telnyx will deliver your XML Translator webhooks.

          active: Specifies whether the connection can be used.

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          first_command_timeout: Specifies whether calls to phone numbers associated with this connection should
              hangup after timing out.

          first_command_timeout_secs: Specifies how many seconds to wait before timing out a dial command.

          status_callback: URL for Telnyx to send requests to containing information about call progress
              events.

          status_callback_method: HTTP request method Telnyx should use when requesting the status_callback URL.

          tags: Tags associated with the Texml Application.

          voice_fallback_url: URL to which Telnyx will deliver your XML Translator webhooks if we get an error
              response from your voice_url.

          voice_method: HTTP request method Telnyx will use to interact with your XML Translator
              webhooks. Either 'get' or 'post'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/texml_applications/{id}",
            body=maybe_transform(
                {
                    "friendly_name": friendly_name,
                    "voice_url": voice_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "dtmf_type": dtmf_type,
                    "first_command_timeout": first_command_timeout,
                    "first_command_timeout_secs": first_command_timeout_secs,
                    "inbound": inbound,
                    "outbound": outbound,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "tags": tags,
                    "voice_fallback_url": voice_fallback_url,
                    "voice_method": voice_method,
                },
                texml_application_update_params.TexmlApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlApplicationUpdateResponse,
        )

    def list(
        self,
        *,
        filter: texml_application_list_params.Filter | NotGiven = NOT_GIVEN,
        page: texml_application_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "friendly_name", "active"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TexmlApplicationListResponse:
        """
        Returns a list of your TeXML Applications.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[outbound_voice_profile_id], filter[friendly_name]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>friendly_name</code>: sorts the result by the
                  <code>friendly_name</code> field in ascending order.
                </li>

                <li>
                  <code>-friendly_name</code>: sorts the result by the
                  <code>friendly_name</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/texml_applications",
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
                    texml_application_list_params.TexmlApplicationListParams,
                ),
            ),
            cast_to=TexmlApplicationListResponse,
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
    ) -> TexmlApplicationDeleteResponse:
        """
        Deletes a TeXML Application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/texml_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlApplicationDeleteResponse,
        )


class AsyncTexmlApplicationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTexmlApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTexmlApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTexmlApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTexmlApplicationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        friendly_name: str,
        voice_url: str,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: AnchorsiteOverride | NotGiven = NOT_GIVEN,
        dtmf_type: DtmfType | NotGiven = NOT_GIVEN,
        first_command_timeout: bool | NotGiven = NOT_GIVEN,
        first_command_timeout_secs: int | NotGiven = NOT_GIVEN,
        inbound: texml_application_create_params.Inbound | NotGiven = NOT_GIVEN,
        outbound: texml_application_create_params.Outbound | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["get", "post"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        voice_fallback_url: str | NotGiven = NOT_GIVEN,
        voice_method: Literal["get", "post"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TexmlApplicationCreateResponse:
        """
        Creates a TeXML Application.

        Args:
          friendly_name: A user-assigned name to help manage the application.

          voice_url: URL to which Telnyx will deliver your XML Translator webhooks.

          active: Specifies whether the connection can be used.

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          first_command_timeout: Specifies whether calls to phone numbers associated with this connection should
              hangup after timing out.

          first_command_timeout_secs: Specifies how many seconds to wait before timing out a dial command.

          status_callback: URL for Telnyx to send requests to containing information about call progress
              events.

          status_callback_method: HTTP request method Telnyx should use when requesting the status_callback URL.

          tags: Tags associated with the Texml Application.

          voice_fallback_url: URL to which Telnyx will deliver your XML Translator webhooks if we get an error
              response from your voice_url.

          voice_method: HTTP request method Telnyx will use to interact with your XML Translator
              webhooks. Either 'get' or 'post'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/texml_applications",
            body=await async_maybe_transform(
                {
                    "friendly_name": friendly_name,
                    "voice_url": voice_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "dtmf_type": dtmf_type,
                    "first_command_timeout": first_command_timeout,
                    "first_command_timeout_secs": first_command_timeout_secs,
                    "inbound": inbound,
                    "outbound": outbound,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "tags": tags,
                    "voice_fallback_url": voice_fallback_url,
                    "voice_method": voice_method,
                },
                texml_application_create_params.TexmlApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlApplicationCreateResponse,
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
    ) -> TexmlApplicationRetrieveResponse:
        """
        Retrieves the details of an existing TeXML Application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/texml_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlApplicationRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        friendly_name: str,
        voice_url: str,
        active: bool | NotGiven = NOT_GIVEN,
        anchorsite_override: AnchorsiteOverride | NotGiven = NOT_GIVEN,
        dtmf_type: DtmfType | NotGiven = NOT_GIVEN,
        first_command_timeout: bool | NotGiven = NOT_GIVEN,
        first_command_timeout_secs: int | NotGiven = NOT_GIVEN,
        inbound: texml_application_update_params.Inbound | NotGiven = NOT_GIVEN,
        outbound: texml_application_update_params.Outbound | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["get", "post"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        voice_fallback_url: str | NotGiven = NOT_GIVEN,
        voice_method: Literal["get", "post"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TexmlApplicationUpdateResponse:
        """
        Updates settings of an existing TeXML Application.

        Args:
          friendly_name: A user-assigned name to help manage the application.

          voice_url: URL to which Telnyx will deliver your XML Translator webhooks.

          active: Specifies whether the connection can be used.

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          dtmf_type: Sets the type of DTMF digits sent from Telnyx to this Connection. Note that DTMF
              digits sent to Telnyx will be accepted in all formats.

          first_command_timeout: Specifies whether calls to phone numbers associated with this connection should
              hangup after timing out.

          first_command_timeout_secs: Specifies how many seconds to wait before timing out a dial command.

          status_callback: URL for Telnyx to send requests to containing information about call progress
              events.

          status_callback_method: HTTP request method Telnyx should use when requesting the status_callback URL.

          tags: Tags associated with the Texml Application.

          voice_fallback_url: URL to which Telnyx will deliver your XML Translator webhooks if we get an error
              response from your voice_url.

          voice_method: HTTP request method Telnyx will use to interact with your XML Translator
              webhooks. Either 'get' or 'post'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/texml_applications/{id}",
            body=await async_maybe_transform(
                {
                    "friendly_name": friendly_name,
                    "voice_url": voice_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "dtmf_type": dtmf_type,
                    "first_command_timeout": first_command_timeout,
                    "first_command_timeout_secs": first_command_timeout_secs,
                    "inbound": inbound,
                    "outbound": outbound,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "tags": tags,
                    "voice_fallback_url": voice_fallback_url,
                    "voice_method": voice_method,
                },
                texml_application_update_params.TexmlApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlApplicationUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: texml_application_list_params.Filter | NotGiven = NOT_GIVEN,
        page: texml_application_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "friendly_name", "active"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TexmlApplicationListResponse:
        """
        Returns a list of your TeXML Applications.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[outbound_voice_profile_id], filter[friendly_name]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>friendly_name</code>: sorts the result by the
                  <code>friendly_name</code> field in ascending order.
                </li>

                <li>
                  <code>-friendly_name</code>: sorts the result by the
                  <code>friendly_name</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/texml_applications",
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
                    texml_application_list_params.TexmlApplicationListParams,
                ),
            ),
            cast_to=TexmlApplicationListResponse,
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
    ) -> TexmlApplicationDeleteResponse:
        """
        Deletes a TeXML Application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/texml_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlApplicationDeleteResponse,
        )


class TexmlApplicationsResourceWithRawResponse:
    def __init__(self, texml_applications: TexmlApplicationsResource) -> None:
        self._texml_applications = texml_applications

        self.create = to_raw_response_wrapper(
            texml_applications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            texml_applications.retrieve,
        )
        self.update = to_raw_response_wrapper(
            texml_applications.update,
        )
        self.list = to_raw_response_wrapper(
            texml_applications.list,
        )
        self.delete = to_raw_response_wrapper(
            texml_applications.delete,
        )


class AsyncTexmlApplicationsResourceWithRawResponse:
    def __init__(self, texml_applications: AsyncTexmlApplicationsResource) -> None:
        self._texml_applications = texml_applications

        self.create = async_to_raw_response_wrapper(
            texml_applications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            texml_applications.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            texml_applications.update,
        )
        self.list = async_to_raw_response_wrapper(
            texml_applications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            texml_applications.delete,
        )


class TexmlApplicationsResourceWithStreamingResponse:
    def __init__(self, texml_applications: TexmlApplicationsResource) -> None:
        self._texml_applications = texml_applications

        self.create = to_streamed_response_wrapper(
            texml_applications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            texml_applications.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            texml_applications.update,
        )
        self.list = to_streamed_response_wrapper(
            texml_applications.list,
        )
        self.delete = to_streamed_response_wrapper(
            texml_applications.delete,
        )


class AsyncTexmlApplicationsResourceWithStreamingResponse:
    def __init__(self, texml_applications: AsyncTexmlApplicationsResource) -> None:
        self._texml_applications = texml_applications

        self.create = async_to_streamed_response_wrapper(
            texml_applications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            texml_applications.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            texml_applications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            texml_applications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            texml_applications.delete,
        )
