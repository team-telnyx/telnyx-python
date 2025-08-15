# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    sub_number_order_list_params,
    sub_number_order_update_params,
    sub_number_order_retrieve_params,
    sub_number_order_update_requirement_group_params,
)
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
from ..types.sub_number_order_list_response import SubNumberOrderListResponse
from ..types.sub_number_order_cancel_response import SubNumberOrderCancelResponse
from ..types.sub_number_order_update_response import SubNumberOrderUpdateResponse
from ..types.sub_number_order_retrieve_response import SubNumberOrderRetrieveResponse
from ..types.update_regulatory_requirement_param import UpdateRegulatoryRequirementParam
from ..types.sub_number_order_update_requirement_group_response import SubNumberOrderUpdateRequirementGroupResponse

__all__ = ["SubNumberOrdersResource", "AsyncSubNumberOrdersResource"]


class SubNumberOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubNumberOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SubNumberOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubNumberOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SubNumberOrdersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        sub_number_order_id: str,
        *,
        filter: sub_number_order_retrieve_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrderRetrieveResponse:
        """
        Get an existing sub number order.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[include_phone_numbers]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sub_number_order_id:
            raise ValueError(
                f"Expected a non-empty value for `sub_number_order_id` but received {sub_number_order_id!r}"
            )
        return self._get(
            f"/sub_number_orders/{sub_number_order_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"filter": filter}, sub_number_order_retrieve_params.SubNumberOrderRetrieveParams
                ),
            ),
            cast_to=SubNumberOrderRetrieveResponse,
        )

    def update(
        self,
        sub_number_order_id: str,
        *,
        regulatory_requirements: Iterable[UpdateRegulatoryRequirementParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrderUpdateResponse:
        """
        Updates a sub number order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sub_number_order_id:
            raise ValueError(
                f"Expected a non-empty value for `sub_number_order_id` but received {sub_number_order_id!r}"
            )
        return self._patch(
            f"/sub_number_orders/{sub_number_order_id}",
            body=maybe_transform(
                {"regulatory_requirements": regulatory_requirements},
                sub_number_order_update_params.SubNumberOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrderUpdateResponse,
        )

    def list(
        self,
        *,
        filter: sub_number_order_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrderListResponse:
        """
        Get a paginated list of sub number orders.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[order_request_id], filter[country_code], filter[phone_number_type],
              filter[phone_numbers_count]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sub_number_orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"filter": filter}, sub_number_order_list_params.SubNumberOrderListParams),
            ),
            cast_to=SubNumberOrderListResponse,
        )

    def cancel(
        self,
        sub_number_order_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrderCancelResponse:
        """
        Allows you to cancel a sub number order in 'pending' status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sub_number_order_id:
            raise ValueError(
                f"Expected a non-empty value for `sub_number_order_id` but received {sub_number_order_id!r}"
            )
        return self._patch(
            f"/sub_number_orders/{sub_number_order_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrderCancelResponse,
        )

    def update_requirement_group(
        self,
        id: str,
        *,
        requirement_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrderUpdateRequirementGroupResponse:
        """
        Update requirement group for a sub number order

        Args:
          requirement_group_id: The ID of the requirement group to associate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/sub_number_orders/{id}/requirement_group",
            body=maybe_transform(
                {"requirement_group_id": requirement_group_id},
                sub_number_order_update_requirement_group_params.SubNumberOrderUpdateRequirementGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrderUpdateRequirementGroupResponse,
        )


class AsyncSubNumberOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubNumberOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubNumberOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubNumberOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSubNumberOrdersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        sub_number_order_id: str,
        *,
        filter: sub_number_order_retrieve_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrderRetrieveResponse:
        """
        Get an existing sub number order.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[include_phone_numbers]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sub_number_order_id:
            raise ValueError(
                f"Expected a non-empty value for `sub_number_order_id` but received {sub_number_order_id!r}"
            )
        return await self._get(
            f"/sub_number_orders/{sub_number_order_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter}, sub_number_order_retrieve_params.SubNumberOrderRetrieveParams
                ),
            ),
            cast_to=SubNumberOrderRetrieveResponse,
        )

    async def update(
        self,
        sub_number_order_id: str,
        *,
        regulatory_requirements: Iterable[UpdateRegulatoryRequirementParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrderUpdateResponse:
        """
        Updates a sub number order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sub_number_order_id:
            raise ValueError(
                f"Expected a non-empty value for `sub_number_order_id` but received {sub_number_order_id!r}"
            )
        return await self._patch(
            f"/sub_number_orders/{sub_number_order_id}",
            body=await async_maybe_transform(
                {"regulatory_requirements": regulatory_requirements},
                sub_number_order_update_params.SubNumberOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrderUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: sub_number_order_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrderListResponse:
        """
        Get a paginated list of sub number orders.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[order_request_id], filter[country_code], filter[phone_number_type],
              filter[phone_numbers_count]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sub_number_orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter}, sub_number_order_list_params.SubNumberOrderListParams
                ),
            ),
            cast_to=SubNumberOrderListResponse,
        )

    async def cancel(
        self,
        sub_number_order_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrderCancelResponse:
        """
        Allows you to cancel a sub number order in 'pending' status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sub_number_order_id:
            raise ValueError(
                f"Expected a non-empty value for `sub_number_order_id` but received {sub_number_order_id!r}"
            )
        return await self._patch(
            f"/sub_number_orders/{sub_number_order_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrderCancelResponse,
        )

    async def update_requirement_group(
        self,
        id: str,
        *,
        requirement_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrderUpdateRequirementGroupResponse:
        """
        Update requirement group for a sub number order

        Args:
          requirement_group_id: The ID of the requirement group to associate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/sub_number_orders/{id}/requirement_group",
            body=await async_maybe_transform(
                {"requirement_group_id": requirement_group_id},
                sub_number_order_update_requirement_group_params.SubNumberOrderUpdateRequirementGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrderUpdateRequirementGroupResponse,
        )


class SubNumberOrdersResourceWithRawResponse:
    def __init__(self, sub_number_orders: SubNumberOrdersResource) -> None:
        self._sub_number_orders = sub_number_orders

        self.retrieve = to_raw_response_wrapper(
            sub_number_orders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sub_number_orders.update,
        )
        self.list = to_raw_response_wrapper(
            sub_number_orders.list,
        )
        self.cancel = to_raw_response_wrapper(
            sub_number_orders.cancel,
        )
        self.update_requirement_group = to_raw_response_wrapper(
            sub_number_orders.update_requirement_group,
        )


class AsyncSubNumberOrdersResourceWithRawResponse:
    def __init__(self, sub_number_orders: AsyncSubNumberOrdersResource) -> None:
        self._sub_number_orders = sub_number_orders

        self.retrieve = async_to_raw_response_wrapper(
            sub_number_orders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sub_number_orders.update,
        )
        self.list = async_to_raw_response_wrapper(
            sub_number_orders.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            sub_number_orders.cancel,
        )
        self.update_requirement_group = async_to_raw_response_wrapper(
            sub_number_orders.update_requirement_group,
        )


class SubNumberOrdersResourceWithStreamingResponse:
    def __init__(self, sub_number_orders: SubNumberOrdersResource) -> None:
        self._sub_number_orders = sub_number_orders

        self.retrieve = to_streamed_response_wrapper(
            sub_number_orders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sub_number_orders.update,
        )
        self.list = to_streamed_response_wrapper(
            sub_number_orders.list,
        )
        self.cancel = to_streamed_response_wrapper(
            sub_number_orders.cancel,
        )
        self.update_requirement_group = to_streamed_response_wrapper(
            sub_number_orders.update_requirement_group,
        )


class AsyncSubNumberOrdersResourceWithStreamingResponse:
    def __init__(self, sub_number_orders: AsyncSubNumberOrdersResource) -> None:
        self._sub_number_orders = sub_number_orders

        self.retrieve = async_to_streamed_response_wrapper(
            sub_number_orders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sub_number_orders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sub_number_orders.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            sub_number_orders.cancel,
        )
        self.update_requirement_group = async_to_streamed_response_wrapper(
            sub_number_orders.update_requirement_group,
        )
