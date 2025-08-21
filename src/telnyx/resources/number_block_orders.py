# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import number_block_order_list_params, number_block_order_create_params
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
from ..types.number_block_order_list_response import NumberBlockOrderListResponse
from ..types.number_block_order_create_response import NumberBlockOrderCreateResponse
from ..types.number_block_order_retrieve_response import NumberBlockOrderRetrieveResponse

__all__ = ["NumberBlockOrdersResource", "AsyncNumberBlockOrdersResource"]


class NumberBlockOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NumberBlockOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NumberBlockOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumberBlockOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NumberBlockOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        range: int,
        starting_number: str,
        connection_id: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        messaging_profile_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberBlockOrderCreateResponse:
        """
        Creates a phone number block order.

        Args:
          range: The phone number range included in the block.

          starting_number: Starting phone number block

          connection_id: Identifies the connection associated with this phone number.

          customer_reference: A customer reference string for customer look ups.

          messaging_profile_id: Identifies the messaging profile associated with the phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/number_block_orders",
            body=maybe_transform(
                {
                    "range": range,
                    "starting_number": starting_number,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "messaging_profile_id": messaging_profile_id,
                },
                number_block_order_create_params.NumberBlockOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberBlockOrderCreateResponse,
        )

    def retrieve(
        self,
        number_block_order_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberBlockOrderRetrieveResponse:
        """
        Get an existing phone number block order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_block_order_id:
            raise ValueError(
                f"Expected a non-empty value for `number_block_order_id` but received {number_block_order_id!r}"
            )
        return self._get(
            f"/number_block_orders/{number_block_order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberBlockOrderRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: number_block_order_list_params.Filter | NotGiven = NOT_GIVEN,
        page: number_block_order_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberBlockOrderListResponse:
        """
        Get a paginated list of number block orders.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[created_at], filter[phone_numbers.starting_number]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/number_block_orders",
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
                    number_block_order_list_params.NumberBlockOrderListParams,
                ),
            ),
            cast_to=NumberBlockOrderListResponse,
        )


class AsyncNumberBlockOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNumberBlockOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumberBlockOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumberBlockOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNumberBlockOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        range: int,
        starting_number: str,
        connection_id: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        messaging_profile_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberBlockOrderCreateResponse:
        """
        Creates a phone number block order.

        Args:
          range: The phone number range included in the block.

          starting_number: Starting phone number block

          connection_id: Identifies the connection associated with this phone number.

          customer_reference: A customer reference string for customer look ups.

          messaging_profile_id: Identifies the messaging profile associated with the phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/number_block_orders",
            body=await async_maybe_transform(
                {
                    "range": range,
                    "starting_number": starting_number,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "messaging_profile_id": messaging_profile_id,
                },
                number_block_order_create_params.NumberBlockOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberBlockOrderCreateResponse,
        )

    async def retrieve(
        self,
        number_block_order_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberBlockOrderRetrieveResponse:
        """
        Get an existing phone number block order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_block_order_id:
            raise ValueError(
                f"Expected a non-empty value for `number_block_order_id` but received {number_block_order_id!r}"
            )
        return await self._get(
            f"/number_block_orders/{number_block_order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberBlockOrderRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: number_block_order_list_params.Filter | NotGiven = NOT_GIVEN,
        page: number_block_order_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberBlockOrderListResponse:
        """
        Get a paginated list of number block orders.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[created_at], filter[phone_numbers.starting_number]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/number_block_orders",
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
                    number_block_order_list_params.NumberBlockOrderListParams,
                ),
            ),
            cast_to=NumberBlockOrderListResponse,
        )


class NumberBlockOrdersResourceWithRawResponse:
    def __init__(self, number_block_orders: NumberBlockOrdersResource) -> None:
        self._number_block_orders = number_block_orders

        self.create = to_raw_response_wrapper(
            number_block_orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            number_block_orders.retrieve,
        )
        self.list = to_raw_response_wrapper(
            number_block_orders.list,
        )


class AsyncNumberBlockOrdersResourceWithRawResponse:
    def __init__(self, number_block_orders: AsyncNumberBlockOrdersResource) -> None:
        self._number_block_orders = number_block_orders

        self.create = async_to_raw_response_wrapper(
            number_block_orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            number_block_orders.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            number_block_orders.list,
        )


class NumberBlockOrdersResourceWithStreamingResponse:
    def __init__(self, number_block_orders: NumberBlockOrdersResource) -> None:
        self._number_block_orders = number_block_orders

        self.create = to_streamed_response_wrapper(
            number_block_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            number_block_orders.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            number_block_orders.list,
        )


class AsyncNumberBlockOrdersResourceWithStreamingResponse:
    def __init__(self, number_block_orders: AsyncNumberBlockOrdersResource) -> None:
        self._number_block_orders = number_block_orders

        self.create = async_to_streamed_response_wrapper(
            number_block_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            number_block_orders.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            number_block_orders.list,
        )
