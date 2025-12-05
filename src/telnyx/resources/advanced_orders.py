# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import advanced_order_create_params, advanced_order_update_requirement_group_params
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
from .._base_client import make_request_options
from ..types.advanced_order_list_response import AdvancedOrderListResponse
from ..types.advanced_order_create_response import AdvancedOrderCreateResponse
from ..types.advanced_order_retrieve_response import AdvancedOrderRetrieveResponse
from ..types.advanced_order_update_requirement_group_response import AdvancedOrderUpdateRequirementGroupResponse

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
        area_code: str | Omit = omit,
        comments: str | Omit = omit,
        country_code: str | Omit = omit,
        customer_reference: str | Omit = omit,
        features: List[Literal["sms", "mms", "voice", "fax", "emergency"]] | Omit = omit,
        phone_number_type: Literal["local", "mobile", "toll_free", "shared_cost", "national", "landline"] | Omit = omit,
        quantity: int | Omit = omit,
        requirement_group_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedOrderCreateResponse:
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
            cast_to=AdvancedOrderCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedOrderRetrieveResponse:
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
            cast_to=AdvancedOrderRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedOrderListResponse:
        """List Advanced Orders"""
        return self._get(
            "/advanced_orders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdvancedOrderListResponse,
        )

    def update_requirement_group(
        self,
        advanced_order_id: str,
        *,
        area_code: str | Omit = omit,
        comments: str | Omit = omit,
        country_code: str | Omit = omit,
        customer_reference: str | Omit = omit,
        features: List[Literal["sms", "mms", "voice", "fax", "emergency"]] | Omit = omit,
        phone_number_type: Literal["local", "mobile", "toll_free", "shared_cost", "national", "landline"] | Omit = omit,
        quantity: int | Omit = omit,
        requirement_group_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedOrderUpdateRequirementGroupResponse:
        """
        Update Advanced Order

        Args:
          requirement_group_id: The ID of the requirement group to associate with this advanced order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not advanced_order_id:
            raise ValueError(f"Expected a non-empty value for `advanced_order_id` but received {advanced_order_id!r}")
        return self._patch(
            f"/advanced_orders/{advanced_order_id}/requirement_group",
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
                advanced_order_update_requirement_group_params.AdvancedOrderUpdateRequirementGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdvancedOrderUpdateRequirementGroupResponse,
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
        area_code: str | Omit = omit,
        comments: str | Omit = omit,
        country_code: str | Omit = omit,
        customer_reference: str | Omit = omit,
        features: List[Literal["sms", "mms", "voice", "fax", "emergency"]] | Omit = omit,
        phone_number_type: Literal["local", "mobile", "toll_free", "shared_cost", "national", "landline"] | Omit = omit,
        quantity: int | Omit = omit,
        requirement_group_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedOrderCreateResponse:
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
            cast_to=AdvancedOrderCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedOrderRetrieveResponse:
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
            cast_to=AdvancedOrderRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedOrderListResponse:
        """List Advanced Orders"""
        return await self._get(
            "/advanced_orders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdvancedOrderListResponse,
        )

    async def update_requirement_group(
        self,
        advanced_order_id: str,
        *,
        area_code: str | Omit = omit,
        comments: str | Omit = omit,
        country_code: str | Omit = omit,
        customer_reference: str | Omit = omit,
        features: List[Literal["sms", "mms", "voice", "fax", "emergency"]] | Omit = omit,
        phone_number_type: Literal["local", "mobile", "toll_free", "shared_cost", "national", "landline"] | Omit = omit,
        quantity: int | Omit = omit,
        requirement_group_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedOrderUpdateRequirementGroupResponse:
        """
        Update Advanced Order

        Args:
          requirement_group_id: The ID of the requirement group to associate with this advanced order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not advanced_order_id:
            raise ValueError(f"Expected a non-empty value for `advanced_order_id` but received {advanced_order_id!r}")
        return await self._patch(
            f"/advanced_orders/{advanced_order_id}/requirement_group",
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
                advanced_order_update_requirement_group_params.AdvancedOrderUpdateRequirementGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdvancedOrderUpdateRequirementGroupResponse,
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
        self.list = to_raw_response_wrapper(
            advanced_orders.list,
        )
        self.update_requirement_group = to_raw_response_wrapper(
            advanced_orders.update_requirement_group,
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
        self.list = async_to_raw_response_wrapper(
            advanced_orders.list,
        )
        self.update_requirement_group = async_to_raw_response_wrapper(
            advanced_orders.update_requirement_group,
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
        self.list = to_streamed_response_wrapper(
            advanced_orders.list,
        )
        self.update_requirement_group = to_streamed_response_wrapper(
            advanced_orders.update_requirement_group,
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
        self.list = async_to_streamed_response_wrapper(
            advanced_orders.list,
        )
        self.update_requirement_group = async_to_streamed_response_wrapper(
            advanced_orders.update_requirement_group,
        )
