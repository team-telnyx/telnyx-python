# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.list_retrieve_all_response import ListRetrieveAllResponse
from ..types.list_retrieve_by_zone_response import ListRetrieveByZoneResponse

__all__ = ["ListResource", "AsyncListResource"]


class ListResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ListResourceWithStreamingResponse(self)

    def retrieve_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListRetrieveAllResponse:
        """Retrieve a list of all phone numbers using Channel Billing, grouped by Zone."""
        return self._get(
            "/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListRetrieveAllResponse,
        )

    def retrieve_by_zone(
        self,
        channel_zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListRetrieveByZoneResponse:
        """
        Retrieve a list of phone numbers using Channel Billing for a specific Zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_zone_id:
            raise ValueError(f"Expected a non-empty value for `channel_zone_id` but received {channel_zone_id!r}")
        return self._get(
            f"/list/{channel_zone_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListRetrieveByZoneResponse,
        )


class AsyncListResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncListResourceWithStreamingResponse(self)

    async def retrieve_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListRetrieveAllResponse:
        """Retrieve a list of all phone numbers using Channel Billing, grouped by Zone."""
        return await self._get(
            "/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListRetrieveAllResponse,
        )

    async def retrieve_by_zone(
        self,
        channel_zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListRetrieveByZoneResponse:
        """
        Retrieve a list of phone numbers using Channel Billing for a specific Zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_zone_id:
            raise ValueError(f"Expected a non-empty value for `channel_zone_id` but received {channel_zone_id!r}")
        return await self._get(
            f"/list/{channel_zone_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListRetrieveByZoneResponse,
        )


class ListResourceWithRawResponse:
    def __init__(self, list: ListResource) -> None:
        self._list = list

        self.retrieve_all = to_raw_response_wrapper(
            list.retrieve_all,
        )
        self.retrieve_by_zone = to_raw_response_wrapper(
            list.retrieve_by_zone,
        )


class AsyncListResourceWithRawResponse:
    def __init__(self, list: AsyncListResource) -> None:
        self._list = list

        self.retrieve_all = async_to_raw_response_wrapper(
            list.retrieve_all,
        )
        self.retrieve_by_zone = async_to_raw_response_wrapper(
            list.retrieve_by_zone,
        )


class ListResourceWithStreamingResponse:
    def __init__(self, list: ListResource) -> None:
        self._list = list

        self.retrieve_all = to_streamed_response_wrapper(
            list.retrieve_all,
        )
        self.retrieve_by_zone = to_streamed_response_wrapper(
            list.retrieve_by_zone,
        )


class AsyncListResourceWithStreamingResponse:
    def __init__(self, list: AsyncListResource) -> None:
        self._list = list

        self.retrieve_all = async_to_streamed_response_wrapper(
            list.retrieve_all,
        )
        self.retrieve_by_zone = async_to_streamed_response_wrapper(
            list.retrieve_by_zone,
        )
