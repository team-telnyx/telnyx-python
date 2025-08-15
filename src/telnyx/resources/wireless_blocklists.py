# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import wireless_blocklist_list_params, wireless_blocklist_create_params, wireless_blocklist_update_params
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
from ..types.wireless_blocklist_list_response import WirelessBlocklistListResponse
from ..types.wireless_blocklist_create_response import WirelessBlocklistCreateResponse
from ..types.wireless_blocklist_delete_response import WirelessBlocklistDeleteResponse
from ..types.wireless_blocklist_update_response import WirelessBlocklistUpdateResponse
from ..types.wireless_blocklist_retrieve_response import WirelessBlocklistRetrieveResponse

__all__ = ["WirelessBlocklistsResource", "AsyncWirelessBlocklistsResource"]


class WirelessBlocklistsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WirelessBlocklistsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return WirelessBlocklistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WirelessBlocklistsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return WirelessBlocklistsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: Literal["country", "mcc", "plmn"],
        values: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WirelessBlocklistCreateResponse:
        """
        Create a Wireless Blocklist to prevent SIMs from connecting to certain networks.

        Args:
          name: The name of the Wireless Blocklist.

          type: The type of wireless blocklist.

          values: Values to block. The values here depend on the `type` of Wireless Blocklist.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/wireless_blocklists",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "values": values,
                },
                wireless_blocklist_create_params.WirelessBlocklistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WirelessBlocklistCreateResponse,
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
    ) -> WirelessBlocklistRetrieveResponse:
        """
        Retrieve information about a Wireless Blocklist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/wireless_blocklists/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WirelessBlocklistRetrieveResponse,
        )

    def update(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        type: Literal["country", "mcc", "plmn"] | NotGiven = NOT_GIVEN,
        values: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WirelessBlocklistUpdateResponse:
        """
        Update a Wireless Blocklist.

        Args:
          name: The name of the Wireless Blocklist.

          type: The type of wireless blocklist.

          values: Values to block. The values here depend on the `type` of Wireless Blocklist.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/wireless_blocklists",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "values": values,
                },
                wireless_blocklist_update_params.WirelessBlocklistUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WirelessBlocklistUpdateResponse,
        )

    def list(
        self,
        *,
        filter_name: str | NotGiven = NOT_GIVEN,
        filter_type: str | NotGiven = NOT_GIVEN,
        filter_values: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WirelessBlocklistListResponse:
        """
        Get all Wireless Blocklists belonging to the user.

        Args:
          filter_name: The name of the Wireless Blocklist.

          filter_type: When the Private Wireless Gateway was last updated.

          filter_values: Values to filter on (inclusive).

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/wireless_blocklists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_name": filter_name,
                        "filter_type": filter_type,
                        "filter_values": filter_values,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    wireless_blocklist_list_params.WirelessBlocklistListParams,
                ),
            ),
            cast_to=WirelessBlocklistListResponse,
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
    ) -> WirelessBlocklistDeleteResponse:
        """
        Deletes the Wireless Blocklist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/wireless_blocklists/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WirelessBlocklistDeleteResponse,
        )


class AsyncWirelessBlocklistsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWirelessBlocklistsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWirelessBlocklistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWirelessBlocklistsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncWirelessBlocklistsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: Literal["country", "mcc", "plmn"],
        values: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WirelessBlocklistCreateResponse:
        """
        Create a Wireless Blocklist to prevent SIMs from connecting to certain networks.

        Args:
          name: The name of the Wireless Blocklist.

          type: The type of wireless blocklist.

          values: Values to block. The values here depend on the `type` of Wireless Blocklist.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/wireless_blocklists",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "values": values,
                },
                wireless_blocklist_create_params.WirelessBlocklistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WirelessBlocklistCreateResponse,
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
    ) -> WirelessBlocklistRetrieveResponse:
        """
        Retrieve information about a Wireless Blocklist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/wireless_blocklists/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WirelessBlocklistRetrieveResponse,
        )

    async def update(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        type: Literal["country", "mcc", "plmn"] | NotGiven = NOT_GIVEN,
        values: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WirelessBlocklistUpdateResponse:
        """
        Update a Wireless Blocklist.

        Args:
          name: The name of the Wireless Blocklist.

          type: The type of wireless blocklist.

          values: Values to block. The values here depend on the `type` of Wireless Blocklist.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/wireless_blocklists",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "values": values,
                },
                wireless_blocklist_update_params.WirelessBlocklistUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WirelessBlocklistUpdateResponse,
        )

    async def list(
        self,
        *,
        filter_name: str | NotGiven = NOT_GIVEN,
        filter_type: str | NotGiven = NOT_GIVEN,
        filter_values: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WirelessBlocklistListResponse:
        """
        Get all Wireless Blocklists belonging to the user.

        Args:
          filter_name: The name of the Wireless Blocklist.

          filter_type: When the Private Wireless Gateway was last updated.

          filter_values: Values to filter on (inclusive).

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/wireless_blocklists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_name": filter_name,
                        "filter_type": filter_type,
                        "filter_values": filter_values,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    wireless_blocklist_list_params.WirelessBlocklistListParams,
                ),
            ),
            cast_to=WirelessBlocklistListResponse,
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
    ) -> WirelessBlocklistDeleteResponse:
        """
        Deletes the Wireless Blocklist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/wireless_blocklists/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WirelessBlocklistDeleteResponse,
        )


class WirelessBlocklistsResourceWithRawResponse:
    def __init__(self, wireless_blocklists: WirelessBlocklistsResource) -> None:
        self._wireless_blocklists = wireless_blocklists

        self.create = to_raw_response_wrapper(
            wireless_blocklists.create,
        )
        self.retrieve = to_raw_response_wrapper(
            wireless_blocklists.retrieve,
        )
        self.update = to_raw_response_wrapper(
            wireless_blocklists.update,
        )
        self.list = to_raw_response_wrapper(
            wireless_blocklists.list,
        )
        self.delete = to_raw_response_wrapper(
            wireless_blocklists.delete,
        )


class AsyncWirelessBlocklistsResourceWithRawResponse:
    def __init__(self, wireless_blocklists: AsyncWirelessBlocklistsResource) -> None:
        self._wireless_blocklists = wireless_blocklists

        self.create = async_to_raw_response_wrapper(
            wireless_blocklists.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            wireless_blocklists.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            wireless_blocklists.update,
        )
        self.list = async_to_raw_response_wrapper(
            wireless_blocklists.list,
        )
        self.delete = async_to_raw_response_wrapper(
            wireless_blocklists.delete,
        )


class WirelessBlocklistsResourceWithStreamingResponse:
    def __init__(self, wireless_blocklists: WirelessBlocklistsResource) -> None:
        self._wireless_blocklists = wireless_blocklists

        self.create = to_streamed_response_wrapper(
            wireless_blocklists.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            wireless_blocklists.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            wireless_blocklists.update,
        )
        self.list = to_streamed_response_wrapper(
            wireless_blocklists.list,
        )
        self.delete = to_streamed_response_wrapper(
            wireless_blocklists.delete,
        )


class AsyncWirelessBlocklistsResourceWithStreamingResponse:
    def __init__(self, wireless_blocklists: AsyncWirelessBlocklistsResource) -> None:
        self._wireless_blocklists = wireless_blocklists

        self.create = async_to_streamed_response_wrapper(
            wireless_blocklists.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            wireless_blocklists.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            wireless_blocklists.update,
        )
        self.list = async_to_streamed_response_wrapper(
            wireless_blocklists.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            wireless_blocklists.delete,
        )
