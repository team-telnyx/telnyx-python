# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import sim_card_order_list_params, sim_card_order_create_params
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
from ..types.sim_card_order_list_response import SimCardOrderListResponse
from ..types.sim_card_order_create_response import SimCardOrderCreateResponse
from ..types.sim_card_order_retrieve_response import SimCardOrderRetrieveResponse

__all__ = ["SimCardOrdersResource", "AsyncSimCardOrdersResource"]


class SimCardOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimCardOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SimCardOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimCardOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SimCardOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        address_id: str,
        quantity: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardOrderCreateResponse:
        """
        Creates a new order for SIM cards.

        Args:
          address_id: Uniquely identifies the address for the order.

          quantity: The amount of SIM cards to order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sim_card_orders",
            body=maybe_transform(
                {
                    "address_id": address_id,
                    "quantity": quantity,
                },
                sim_card_order_create_params.SimCardOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardOrderCreateResponse,
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
    ) -> SimCardOrderRetrieveResponse:
        """
        Get a single SIM card order by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sim_card_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardOrderRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: sim_card_order_list_params.Filter | NotGiven = NOT_GIVEN,
        page: sim_card_order_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardOrderListResponse:
        """
        Get all SIM card orders according to filters.

        Args:
          filter: Consolidated filter parameter for SIM card orders (deepObject style).
              Originally: filter[created_at], filter[updated_at], filter[quantity],
              filter[cost.amount], filter[cost.currency], filter[address.id],
              filter[address.street_address], filter[address.extended_address],
              filter[address.locality], filter[address.administrative_area],
              filter[address.country_code], filter[address.postal_code]

          page: Consolidated pagination parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sim_card_orders",
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
                    sim_card_order_list_params.SimCardOrderListParams,
                ),
            ),
            cast_to=SimCardOrderListResponse,
        )


class AsyncSimCardOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimCardOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimCardOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimCardOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSimCardOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        address_id: str,
        quantity: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardOrderCreateResponse:
        """
        Creates a new order for SIM cards.

        Args:
          address_id: Uniquely identifies the address for the order.

          quantity: The amount of SIM cards to order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sim_card_orders",
            body=await async_maybe_transform(
                {
                    "address_id": address_id,
                    "quantity": quantity,
                },
                sim_card_order_create_params.SimCardOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardOrderCreateResponse,
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
    ) -> SimCardOrderRetrieveResponse:
        """
        Get a single SIM card order by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sim_card_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardOrderRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: sim_card_order_list_params.Filter | NotGiven = NOT_GIVEN,
        page: sim_card_order_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardOrderListResponse:
        """
        Get all SIM card orders according to filters.

        Args:
          filter: Consolidated filter parameter for SIM card orders (deepObject style).
              Originally: filter[created_at], filter[updated_at], filter[quantity],
              filter[cost.amount], filter[cost.currency], filter[address.id],
              filter[address.street_address], filter[address.extended_address],
              filter[address.locality], filter[address.administrative_area],
              filter[address.country_code], filter[address.postal_code]

          page: Consolidated pagination parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sim_card_orders",
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
                    sim_card_order_list_params.SimCardOrderListParams,
                ),
            ),
            cast_to=SimCardOrderListResponse,
        )


class SimCardOrdersResourceWithRawResponse:
    def __init__(self, sim_card_orders: SimCardOrdersResource) -> None:
        self._sim_card_orders = sim_card_orders

        self.create = to_raw_response_wrapper(
            sim_card_orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sim_card_orders.retrieve,
        )
        self.list = to_raw_response_wrapper(
            sim_card_orders.list,
        )


class AsyncSimCardOrdersResourceWithRawResponse:
    def __init__(self, sim_card_orders: AsyncSimCardOrdersResource) -> None:
        self._sim_card_orders = sim_card_orders

        self.create = async_to_raw_response_wrapper(
            sim_card_orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sim_card_orders.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            sim_card_orders.list,
        )


class SimCardOrdersResourceWithStreamingResponse:
    def __init__(self, sim_card_orders: SimCardOrdersResource) -> None:
        self._sim_card_orders = sim_card_orders

        self.create = to_streamed_response_wrapper(
            sim_card_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sim_card_orders.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            sim_card_orders.list,
        )


class AsyncSimCardOrdersResourceWithStreamingResponse:
    def __init__(self, sim_card_orders: AsyncSimCardOrdersResource) -> None:
        self._sim_card_orders = sim_card_orders

        self.create = async_to_streamed_response_wrapper(
            sim_card_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sim_card_orders.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            sim_card_orders.list,
        )
