# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import access_ip_range_list_params, access_ip_range_create_params
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
from ..types.access_ip_range import AccessIPRange
from ..types.access_ip_range_list_response import AccessIPRangeListResponse

__all__ = ["AccessIPRangesResource", "AsyncAccessIPRangesResource"]


class AccessIPRangesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessIPRangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AccessIPRangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessIPRangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AccessIPRangesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        cidr_block: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessIPRange:
        """
        Create new Access IP Range

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/access_ip_ranges",
            body=maybe_transform(
                {
                    "cidr_block": cidr_block,
                    "description": description,
                },
                access_ip_range_create_params.AccessIPRangeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessIPRange,
        )

    def list(
        self,
        *,
        filter: access_ip_range_list_params.Filter | NotGiven = NOT_GIVEN,
        page: access_ip_range_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessIPRangeListResponse:
        """
        List all Access IP Ranges

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[cidr_block], filter[cidr_block][startswith],
              filter[cidr_block][endswith], filter[cidr_block][contains], filter[created_at].
              Supports complex bracket operations for dynamic filtering.

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/access_ip_ranges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    access_ip_range_list_params.AccessIPRangeListParams,
                ),
            ),
            cast_to=AccessIPRangeListResponse,
        )

    def delete(
        self,
        access_ip_range_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessIPRange:
        """
        Delete access IP ranges

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not access_ip_range_id:
            raise ValueError(f"Expected a non-empty value for `access_ip_range_id` but received {access_ip_range_id!r}")
        return self._delete(
            f"/access_ip_ranges/{access_ip_range_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessIPRange,
        )


class AsyncAccessIPRangesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessIPRangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessIPRangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessIPRangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAccessIPRangesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        cidr_block: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessIPRange:
        """
        Create new Access IP Range

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/access_ip_ranges",
            body=await async_maybe_transform(
                {
                    "cidr_block": cidr_block,
                    "description": description,
                },
                access_ip_range_create_params.AccessIPRangeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessIPRange,
        )

    async def list(
        self,
        *,
        filter: access_ip_range_list_params.Filter | NotGiven = NOT_GIVEN,
        page: access_ip_range_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessIPRangeListResponse:
        """
        List all Access IP Ranges

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[cidr_block], filter[cidr_block][startswith],
              filter[cidr_block][endswith], filter[cidr_block][contains], filter[created_at].
              Supports complex bracket operations for dynamic filtering.

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/access_ip_ranges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    access_ip_range_list_params.AccessIPRangeListParams,
                ),
            ),
            cast_to=AccessIPRangeListResponse,
        )

    async def delete(
        self,
        access_ip_range_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessIPRange:
        """
        Delete access IP ranges

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not access_ip_range_id:
            raise ValueError(f"Expected a non-empty value for `access_ip_range_id` but received {access_ip_range_id!r}")
        return await self._delete(
            f"/access_ip_ranges/{access_ip_range_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessIPRange,
        )


class AccessIPRangesResourceWithRawResponse:
    def __init__(self, access_ip_ranges: AccessIPRangesResource) -> None:
        self._access_ip_ranges = access_ip_ranges

        self.create = to_raw_response_wrapper(
            access_ip_ranges.create,
        )
        self.list = to_raw_response_wrapper(
            access_ip_ranges.list,
        )
        self.delete = to_raw_response_wrapper(
            access_ip_ranges.delete,
        )


class AsyncAccessIPRangesResourceWithRawResponse:
    def __init__(self, access_ip_ranges: AsyncAccessIPRangesResource) -> None:
        self._access_ip_ranges = access_ip_ranges

        self.create = async_to_raw_response_wrapper(
            access_ip_ranges.create,
        )
        self.list = async_to_raw_response_wrapper(
            access_ip_ranges.list,
        )
        self.delete = async_to_raw_response_wrapper(
            access_ip_ranges.delete,
        )


class AccessIPRangesResourceWithStreamingResponse:
    def __init__(self, access_ip_ranges: AccessIPRangesResource) -> None:
        self._access_ip_ranges = access_ip_ranges

        self.create = to_streamed_response_wrapper(
            access_ip_ranges.create,
        )
        self.list = to_streamed_response_wrapper(
            access_ip_ranges.list,
        )
        self.delete = to_streamed_response_wrapper(
            access_ip_ranges.delete,
        )


class AsyncAccessIPRangesResourceWithStreamingResponse:
    def __init__(self, access_ip_ranges: AsyncAccessIPRangesResource) -> None:
        self._access_ip_ranges = access_ip_ranges

        self.create = async_to_streamed_response_wrapper(
            access_ip_ranges.create,
        )
        self.list = async_to_streamed_response_wrapper(
            access_ip_ranges.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            access_ip_ranges.delete,
        )
