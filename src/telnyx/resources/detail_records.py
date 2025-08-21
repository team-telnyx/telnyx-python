# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import detail_record_list_params
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
from ..types.detail_record_list_response import DetailRecordListResponse

__all__ = ["DetailRecordsResource", "AsyncDetailRecordsResource"]


class DetailRecordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetailRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DetailRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DetailRecordsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: detail_record_list_params.Filter | NotGiven = NOT_GIVEN,
        page: detail_record_list_params.Page | NotGiven = NOT_GIVEN,
        sort: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRecordListResponse:
        """
        Search for any detail record across the Telnyx Platform

        Args:
          filter:
              Filter records on a given record attribute and value. <br/>Example:
              filter[status]=delivered. <br/>Required: filter[record_type] must be specified.

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Specifies the sort order for results. <br/>Example: sort=-created_at

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/detail_records",
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
                    detail_record_list_params.DetailRecordListParams,
                ),
            ),
            cast_to=DetailRecordListResponse,
        )


class AsyncDetailRecordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetailRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDetailRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDetailRecordsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        filter: detail_record_list_params.Filter | NotGiven = NOT_GIVEN,
        page: detail_record_list_params.Page | NotGiven = NOT_GIVEN,
        sort: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRecordListResponse:
        """
        Search for any detail record across the Telnyx Platform

        Args:
          filter:
              Filter records on a given record attribute and value. <br/>Example:
              filter[status]=delivered. <br/>Required: filter[record_type] must be specified.

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Specifies the sort order for results. <br/>Example: sort=-created_at

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/detail_records",
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
                    detail_record_list_params.DetailRecordListParams,
                ),
            ),
            cast_to=DetailRecordListResponse,
        )


class DetailRecordsResourceWithRawResponse:
    def __init__(self, detail_records: DetailRecordsResource) -> None:
        self._detail_records = detail_records

        self.list = to_raw_response_wrapper(
            detail_records.list,
        )


class AsyncDetailRecordsResourceWithRawResponse:
    def __init__(self, detail_records: AsyncDetailRecordsResource) -> None:
        self._detail_records = detail_records

        self.list = async_to_raw_response_wrapper(
            detail_records.list,
        )


class DetailRecordsResourceWithStreamingResponse:
    def __init__(self, detail_records: DetailRecordsResource) -> None:
        self._detail_records = detail_records

        self.list = to_streamed_response_wrapper(
            detail_records.list,
        )


class AsyncDetailRecordsResourceWithStreamingResponse:
    def __init__(self, detail_records: AsyncDetailRecordsResource) -> None:
        self._detail_records = detail_records

        self.list = async_to_streamed_response_wrapper(
            detail_records.list,
        )
