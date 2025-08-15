# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import porting_phone_number_list_params
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
from ..types.porting_phone_number_list_response import PortingPhoneNumberListResponse

__all__ = ["PortingPhoneNumbersResource", "AsyncPortingPhoneNumbersResource"]


class PortingPhoneNumbersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortingPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PortingPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortingPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PortingPhoneNumbersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: porting_phone_number_list_params.Filter | NotGiven = NOT_GIVEN,
        page: porting_phone_number_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingPhoneNumberListResponse:
        """
        Returns a list of your porting phone numbers.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[porting_order_status]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/porting_phone_numbers",
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
                    porting_phone_number_list_params.PortingPhoneNumberListParams,
                ),
            ),
            cast_to=PortingPhoneNumberListResponse,
        )


class AsyncPortingPhoneNumbersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortingPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortingPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortingPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPortingPhoneNumbersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        filter: porting_phone_number_list_params.Filter | NotGiven = NOT_GIVEN,
        page: porting_phone_number_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingPhoneNumberListResponse:
        """
        Returns a list of your porting phone numbers.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[porting_order_status]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/porting_phone_numbers",
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
                    porting_phone_number_list_params.PortingPhoneNumberListParams,
                ),
            ),
            cast_to=PortingPhoneNumberListResponse,
        )


class PortingPhoneNumbersResourceWithRawResponse:
    def __init__(self, porting_phone_numbers: PortingPhoneNumbersResource) -> None:
        self._porting_phone_numbers = porting_phone_numbers

        self.list = to_raw_response_wrapper(
            porting_phone_numbers.list,
        )


class AsyncPortingPhoneNumbersResourceWithRawResponse:
    def __init__(self, porting_phone_numbers: AsyncPortingPhoneNumbersResource) -> None:
        self._porting_phone_numbers = porting_phone_numbers

        self.list = async_to_raw_response_wrapper(
            porting_phone_numbers.list,
        )


class PortingPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, porting_phone_numbers: PortingPhoneNumbersResource) -> None:
        self._porting_phone_numbers = porting_phone_numbers

        self.list = to_streamed_response_wrapper(
            porting_phone_numbers.list,
        )


class AsyncPortingPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, porting_phone_numbers: AsyncPortingPhoneNumbersResource) -> None:
        self._porting_phone_numbers = porting_phone_numbers

        self.list = async_to_streamed_response_wrapper(
            porting_phone_numbers.list,
        )
