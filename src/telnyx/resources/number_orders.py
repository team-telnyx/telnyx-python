# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import number_order_list_params, number_order_create_params, number_order_update_params
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
from ..types.number_order_list_response import NumberOrderListResponse
from ..types.number_order_create_response import NumberOrderCreateResponse
from ..types.number_order_update_response import NumberOrderUpdateResponse
from ..types.number_order_retrieve_response import NumberOrderRetrieveResponse
from ..types.update_regulatory_requirement_param import UpdateRegulatoryRequirementParam

__all__ = ["NumberOrdersResource", "AsyncNumberOrdersResource"]


class NumberOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NumberOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NumberOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumberOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NumberOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        billing_group_id: str | NotGiven = NOT_GIVEN,
        connection_id: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        messaging_profile_id: str | NotGiven = NOT_GIVEN,
        phone_numbers: Iterable[number_order_create_params.PhoneNumber] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderCreateResponse:
        """
        Creates a phone number order.

        Args:
          billing_group_id: Identifies the billing group associated with the phone number.

          connection_id: Identifies the connection associated with this phone number.

          customer_reference: A customer reference string for customer look ups.

          messaging_profile_id: Identifies the messaging profile associated with the phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/number_orders",
            body=maybe_transform(
                {
                    "billing_group_id": billing_group_id,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "messaging_profile_id": messaging_profile_id,
                    "phone_numbers": phone_numbers,
                },
                number_order_create_params.NumberOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderCreateResponse,
        )

    def retrieve(
        self,
        number_order_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderRetrieveResponse:
        """
        Get an existing phone number order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_order_id:
            raise ValueError(f"Expected a non-empty value for `number_order_id` but received {number_order_id!r}")
        return self._get(
            f"/number_orders/{number_order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderRetrieveResponse,
        )

    def update(
        self,
        number_order_id: str,
        *,
        customer_reference: str | NotGiven = NOT_GIVEN,
        regulatory_requirements: Iterable[UpdateRegulatoryRequirementParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderUpdateResponse:
        """
        Updates a phone number order.

        Args:
          customer_reference: A customer reference string for customer look ups.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_order_id:
            raise ValueError(f"Expected a non-empty value for `number_order_id` but received {number_order_id!r}")
        return self._patch(
            f"/number_orders/{number_order_id}",
            body=maybe_transform(
                {
                    "customer_reference": customer_reference,
                    "regulatory_requirements": regulatory_requirements,
                },
                number_order_update_params.NumberOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderUpdateResponse,
        )

    def list(
        self,
        *,
        filter: number_order_list_params.Filter | NotGiven = NOT_GIVEN,
        page: number_order_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderListResponse:
        """
        Get a paginated list of number orders.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[created_at], filter[phone_numbers_count], filter[customer_reference],
              filter[requirements_met]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/number_orders",
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
                    number_order_list_params.NumberOrderListParams,
                ),
            ),
            cast_to=NumberOrderListResponse,
        )


class AsyncNumberOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNumberOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumberOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumberOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNumberOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        billing_group_id: str | NotGiven = NOT_GIVEN,
        connection_id: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        messaging_profile_id: str | NotGiven = NOT_GIVEN,
        phone_numbers: Iterable[number_order_create_params.PhoneNumber] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderCreateResponse:
        """
        Creates a phone number order.

        Args:
          billing_group_id: Identifies the billing group associated with the phone number.

          connection_id: Identifies the connection associated with this phone number.

          customer_reference: A customer reference string for customer look ups.

          messaging_profile_id: Identifies the messaging profile associated with the phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/number_orders",
            body=await async_maybe_transform(
                {
                    "billing_group_id": billing_group_id,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "messaging_profile_id": messaging_profile_id,
                    "phone_numbers": phone_numbers,
                },
                number_order_create_params.NumberOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderCreateResponse,
        )

    async def retrieve(
        self,
        number_order_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderRetrieveResponse:
        """
        Get an existing phone number order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_order_id:
            raise ValueError(f"Expected a non-empty value for `number_order_id` but received {number_order_id!r}")
        return await self._get(
            f"/number_orders/{number_order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderRetrieveResponse,
        )

    async def update(
        self,
        number_order_id: str,
        *,
        customer_reference: str | NotGiven = NOT_GIVEN,
        regulatory_requirements: Iterable[UpdateRegulatoryRequirementParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderUpdateResponse:
        """
        Updates a phone number order.

        Args:
          customer_reference: A customer reference string for customer look ups.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_order_id:
            raise ValueError(f"Expected a non-empty value for `number_order_id` but received {number_order_id!r}")
        return await self._patch(
            f"/number_orders/{number_order_id}",
            body=await async_maybe_transform(
                {
                    "customer_reference": customer_reference,
                    "regulatory_requirements": regulatory_requirements,
                },
                number_order_update_params.NumberOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: number_order_list_params.Filter | NotGiven = NOT_GIVEN,
        page: number_order_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderListResponse:
        """
        Get a paginated list of number orders.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[created_at], filter[phone_numbers_count], filter[customer_reference],
              filter[requirements_met]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/number_orders",
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
                    number_order_list_params.NumberOrderListParams,
                ),
            ),
            cast_to=NumberOrderListResponse,
        )


class NumberOrdersResourceWithRawResponse:
    def __init__(self, number_orders: NumberOrdersResource) -> None:
        self._number_orders = number_orders

        self.create = to_raw_response_wrapper(
            number_orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            number_orders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            number_orders.update,
        )
        self.list = to_raw_response_wrapper(
            number_orders.list,
        )


class AsyncNumberOrdersResourceWithRawResponse:
    def __init__(self, number_orders: AsyncNumberOrdersResource) -> None:
        self._number_orders = number_orders

        self.create = async_to_raw_response_wrapper(
            number_orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            number_orders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            number_orders.update,
        )
        self.list = async_to_raw_response_wrapper(
            number_orders.list,
        )


class NumberOrdersResourceWithStreamingResponse:
    def __init__(self, number_orders: NumberOrdersResource) -> None:
        self._number_orders = number_orders

        self.create = to_streamed_response_wrapper(
            number_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            number_orders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            number_orders.update,
        )
        self.list = to_streamed_response_wrapper(
            number_orders.list,
        )


class AsyncNumberOrdersResourceWithStreamingResponse:
    def __init__(self, number_orders: AsyncNumberOrdersResource) -> None:
        self._number_orders = number_orders

        self.create = async_to_streamed_response_wrapper(
            number_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            number_orders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            number_orders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            number_orders.list,
        )
