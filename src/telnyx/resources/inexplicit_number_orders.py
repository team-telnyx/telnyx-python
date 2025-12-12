# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import inexplicit_number_order_list_params, inexplicit_number_order_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import (
    SyncDefaultFlatPaginationForInexplicitNumberOrders,
    AsyncDefaultFlatPaginationForInexplicitNumberOrders,
)
from .._base_client import AsyncPaginator, make_request_options
from ..types.inexplicit_number_order_response import InexplicitNumberOrderResponse
from ..types.inexplicit_number_order_create_response import InexplicitNumberOrderCreateResponse
from ..types.inexplicit_number_order_retrieve_response import InexplicitNumberOrderRetrieveResponse

__all__ = ["InexplicitNumberOrdersResource", "AsyncInexplicitNumberOrdersResource"]


class InexplicitNumberOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InexplicitNumberOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return InexplicitNumberOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InexplicitNumberOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return InexplicitNumberOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        ordering_groups: Iterable[inexplicit_number_order_create_params.OrderingGroup],
        billing_group_id: str | Omit = omit,
        connection_id: str | Omit = omit,
        customer_reference: str | Omit = omit,
        messaging_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InexplicitNumberOrderCreateResponse:
        """
        Create an inexplicit number order to programmatically purchase phone numbers
        without specifying exact numbers.

        Args:
          ordering_groups: Group(s) of numbers to order. You can have multiple ordering_groups objects
              added to a single request.

          billing_group_id: Billing group id to apply to phone numbers that are purchased

          connection_id: Connection id to apply to phone numbers that are purchased

          customer_reference: Reference label for the customer

          messaging_profile_id: Messaging profile id to apply to phone numbers that are purchased

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/inexplicit_number_orders",
            body=maybe_transform(
                {
                    "ordering_groups": ordering_groups,
                    "billing_group_id": billing_group_id,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "messaging_profile_id": messaging_profile_id,
                },
                inexplicit_number_order_create_params.InexplicitNumberOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InexplicitNumberOrderCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InexplicitNumberOrderRetrieveResponse:
        """
        Get an existing inexplicit number order by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/inexplicit_number_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InexplicitNumberOrderRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse]:
        """
        Get a paginated list of inexplicit number orders.

        Args:
          page_number: The page number to load

          page_size: The size of the page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inexplicit_number_orders",
            page=SyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    inexplicit_number_order_list_params.InexplicitNumberOrderListParams,
                ),
            ),
            model=InexplicitNumberOrderResponse,
        )


class AsyncInexplicitNumberOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInexplicitNumberOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInexplicitNumberOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInexplicitNumberOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncInexplicitNumberOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        ordering_groups: Iterable[inexplicit_number_order_create_params.OrderingGroup],
        billing_group_id: str | Omit = omit,
        connection_id: str | Omit = omit,
        customer_reference: str | Omit = omit,
        messaging_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InexplicitNumberOrderCreateResponse:
        """
        Create an inexplicit number order to programmatically purchase phone numbers
        without specifying exact numbers.

        Args:
          ordering_groups: Group(s) of numbers to order. You can have multiple ordering_groups objects
              added to a single request.

          billing_group_id: Billing group id to apply to phone numbers that are purchased

          connection_id: Connection id to apply to phone numbers that are purchased

          customer_reference: Reference label for the customer

          messaging_profile_id: Messaging profile id to apply to phone numbers that are purchased

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/inexplicit_number_orders",
            body=await async_maybe_transform(
                {
                    "ordering_groups": ordering_groups,
                    "billing_group_id": billing_group_id,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "messaging_profile_id": messaging_profile_id,
                },
                inexplicit_number_order_create_params.InexplicitNumberOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InexplicitNumberOrderCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InexplicitNumberOrderRetrieveResponse:
        """
        Get an existing inexplicit number order by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/inexplicit_number_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InexplicitNumberOrderRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        InexplicitNumberOrderResponse,
        AsyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse],
    ]:
        """
        Get a paginated list of inexplicit number orders.

        Args:
          page_number: The page number to load

          page_size: The size of the page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inexplicit_number_orders",
            page=AsyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    inexplicit_number_order_list_params.InexplicitNumberOrderListParams,
                ),
            ),
            model=InexplicitNumberOrderResponse,
        )


class InexplicitNumberOrdersResourceWithRawResponse:
    def __init__(self, inexplicit_number_orders: InexplicitNumberOrdersResource) -> None:
        self._inexplicit_number_orders = inexplicit_number_orders

        self.create = to_raw_response_wrapper(
            inexplicit_number_orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            inexplicit_number_orders.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inexplicit_number_orders.list,
        )


class AsyncInexplicitNumberOrdersResourceWithRawResponse:
    def __init__(self, inexplicit_number_orders: AsyncInexplicitNumberOrdersResource) -> None:
        self._inexplicit_number_orders = inexplicit_number_orders

        self.create = async_to_raw_response_wrapper(
            inexplicit_number_orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            inexplicit_number_orders.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inexplicit_number_orders.list,
        )


class InexplicitNumberOrdersResourceWithStreamingResponse:
    def __init__(self, inexplicit_number_orders: InexplicitNumberOrdersResource) -> None:
        self._inexplicit_number_orders = inexplicit_number_orders

        self.create = to_streamed_response_wrapper(
            inexplicit_number_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            inexplicit_number_orders.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inexplicit_number_orders.list,
        )


class AsyncInexplicitNumberOrdersResourceWithStreamingResponse:
    def __init__(self, inexplicit_number_orders: AsyncInexplicitNumberOrdersResource) -> None:
        self._inexplicit_number_orders = inexplicit_number_orders

        self.create = async_to_streamed_response_wrapper(
            inexplicit_number_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            inexplicit_number_orders.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inexplicit_number_orders.list,
        )
