# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import advanced_order_create_params, advanced_order_update_params
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

__all__ = ["AdvancedOrdersResource", "AsyncAdvancedOrdersResource"]


class AdvancedOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdvancedOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AdvancedOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvancedOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AdvancedOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        area_code: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        features: List[Literal["sms", "mms", "voice", "fax", "emergency"]] | NotGiven = NOT_GIVEN,
        phone_number_type: Literal["local", "mobile", "toll_free", "shared_cost", "national", "landline"]
        | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        requirement_group_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create Advanced Order

        Args:
          requirement_group_id: The ID of the requirement group to associate with this advanced order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/advanced_orders",
            body=maybe_transform(
                {
                    "area_code": area_code,
                    "comments": comments,
                    "country_code": country_code,
                    "customer_reference": customer_reference,
                    "features": features,
                    "phone_number_type": phone_number_type,
                    "quantity": quantity,
                    "requirement_group_id": requirement_group_id,
                },
                advanced_order_create_params.AdvancedOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve(
        self,
        order_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Advanced Order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return self._get(
            f"/advanced_orders/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update(
        self,
        order_id: str,
        *,
        area_code: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        features: List[Literal["sms", "mms", "voice", "fax", "emergency"]] | NotGiven = NOT_GIVEN,
        phone_number_type: Literal["local", "mobile", "toll_free", "shared_cost", "national", "landline"]
        | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        requirement_group_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Advanced Order

        Args:
          requirement_group_id: The ID of the requirement group to associate with this advanced order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return self._patch(
            f"/advanced_orders/{order_id}",
            body=maybe_transform(
                {
                    "area_code": area_code,
                    "comments": comments,
                    "country_code": country_code,
                    "customer_reference": customer_reference,
                    "features": features,
                    "phone_number_type": phone_number_type,
                    "quantity": quantity,
                    "requirement_group_id": requirement_group_id,
                },
                advanced_order_update_params.AdvancedOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """List Advanced Orders"""
        return self._get(
            "/advanced_orders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAdvancedOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdvancedOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdvancedOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvancedOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAdvancedOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        area_code: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        features: List[Literal["sms", "mms", "voice", "fax", "emergency"]] | NotGiven = NOT_GIVEN,
        phone_number_type: Literal["local", "mobile", "toll_free", "shared_cost", "national", "landline"]
        | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        requirement_group_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create Advanced Order

        Args:
          requirement_group_id: The ID of the requirement group to associate with this advanced order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/advanced_orders",
            body=await async_maybe_transform(
                {
                    "area_code": area_code,
                    "comments": comments,
                    "country_code": country_code,
                    "customer_reference": customer_reference,
                    "features": features,
                    "phone_number_type": phone_number_type,
                    "quantity": quantity,
                    "requirement_group_id": requirement_group_id,
                },
                advanced_order_create_params.AdvancedOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve(
        self,
        order_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Advanced Order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return await self._get(
            f"/advanced_orders/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update(
        self,
        order_id: str,
        *,
        area_code: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        features: List[Literal["sms", "mms", "voice", "fax", "emergency"]] | NotGiven = NOT_GIVEN,
        phone_number_type: Literal["local", "mobile", "toll_free", "shared_cost", "national", "landline"]
        | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        requirement_group_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Advanced Order

        Args:
          requirement_group_id: The ID of the requirement group to associate with this advanced order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return await self._patch(
            f"/advanced_orders/{order_id}",
            body=await async_maybe_transform(
                {
                    "area_code": area_code,
                    "comments": comments,
                    "country_code": country_code,
                    "customer_reference": customer_reference,
                    "features": features,
                    "phone_number_type": phone_number_type,
                    "quantity": quantity,
                    "requirement_group_id": requirement_group_id,
                },
                advanced_order_update_params.AdvancedOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """List Advanced Orders"""
        return await self._get(
            "/advanced_orders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AdvancedOrdersResourceWithRawResponse:
    def __init__(self, advanced_orders: AdvancedOrdersResource) -> None:
        self._advanced_orders = advanced_orders

        self.create = to_raw_response_wrapper(
            advanced_orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            advanced_orders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            advanced_orders.update,
        )
        self.list = to_raw_response_wrapper(
            advanced_orders.list,
        )


class AsyncAdvancedOrdersResourceWithRawResponse:
    def __init__(self, advanced_orders: AsyncAdvancedOrdersResource) -> None:
        self._advanced_orders = advanced_orders

        self.create = async_to_raw_response_wrapper(
            advanced_orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            advanced_orders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            advanced_orders.update,
        )
        self.list = async_to_raw_response_wrapper(
            advanced_orders.list,
        )


class AdvancedOrdersResourceWithStreamingResponse:
    def __init__(self, advanced_orders: AdvancedOrdersResource) -> None:
        self._advanced_orders = advanced_orders

        self.create = to_streamed_response_wrapper(
            advanced_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            advanced_orders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            advanced_orders.update,
        )
        self.list = to_streamed_response_wrapper(
            advanced_orders.list,
        )


class AsyncAdvancedOrdersResourceWithStreamingResponse:
    def __init__(self, advanced_orders: AsyncAdvancedOrdersResource) -> None:
        self._advanced_orders = advanced_orders

        self.create = async_to_streamed_response_wrapper(
            advanced_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            advanced_orders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            advanced_orders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            advanced_orders.list,
        )
