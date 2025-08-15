# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import available_phone_number_list_params
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
from ..types.available_phone_number_list_response import AvailablePhoneNumberListResponse

__all__ = ["AvailablePhoneNumbersResource", "AsyncAvailablePhoneNumbersResource"]


class AvailablePhoneNumbersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailablePhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AvailablePhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailablePhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AvailablePhoneNumbersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: available_phone_number_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvailablePhoneNumberListResponse:
        """
        List available phone numbers

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number], filter[locality], filter[administrative_area],
              filter[country_code], filter[national_destination_code], filter[rate_center],
              filter[phone_number_type], filter[features], filter[limit], filter[best_effort],
              filter[quickship], filter[reservable], filter[exclude_held_numbers]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/available_phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"filter": filter}, available_phone_number_list_params.AvailablePhoneNumberListParams
                ),
            ),
            cast_to=AvailablePhoneNumberListResponse,
        )


class AsyncAvailablePhoneNumbersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvailablePhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvailablePhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailablePhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAvailablePhoneNumbersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        filter: available_phone_number_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AvailablePhoneNumberListResponse:
        """
        List available phone numbers

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number], filter[locality], filter[administrative_area],
              filter[country_code], filter[national_destination_code], filter[rate_center],
              filter[phone_number_type], filter[features], filter[limit], filter[best_effort],
              filter[quickship], filter[reservable], filter[exclude_held_numbers]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/available_phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter}, available_phone_number_list_params.AvailablePhoneNumberListParams
                ),
            ),
            cast_to=AvailablePhoneNumberListResponse,
        )


class AvailablePhoneNumbersResourceWithRawResponse:
    def __init__(self, available_phone_numbers: AvailablePhoneNumbersResource) -> None:
        self._available_phone_numbers = available_phone_numbers

        self.list = to_raw_response_wrapper(
            available_phone_numbers.list,
        )


class AsyncAvailablePhoneNumbersResourceWithRawResponse:
    def __init__(self, available_phone_numbers: AsyncAvailablePhoneNumbersResource) -> None:
        self._available_phone_numbers = available_phone_numbers

        self.list = async_to_raw_response_wrapper(
            available_phone_numbers.list,
        )


class AvailablePhoneNumbersResourceWithStreamingResponse:
    def __init__(self, available_phone_numbers: AvailablePhoneNumbersResource) -> None:
        self._available_phone_numbers = available_phone_numbers

        self.list = to_streamed_response_wrapper(
            available_phone_numbers.list,
        )


class AsyncAvailablePhoneNumbersResourceWithStreamingResponse:
    def __init__(self, available_phone_numbers: AsyncAvailablePhoneNumbersResource) -> None:
        self._available_phone_numbers = available_phone_numbers

        self.list = async_to_streamed_response_wrapper(
            available_phone_numbers.list,
        )
