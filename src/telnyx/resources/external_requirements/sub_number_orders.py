# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.external_requirements import sub_number_order_update_params
from ...types.external_requirements.sub_number_order_update_response import SubNumberOrderUpdateResponse
from ...types.external_requirements.sub_number_order_retrieve_response import SubNumberOrderRetrieveResponse

__all__ = ["SubNumberOrdersResource", "AsyncSubNumberOrdersResource"]


class SubNumberOrdersResource(SyncAPIResource):
    """Requirement Groups"""

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
        regulatory_requirement_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubNumberOrderRetrieveResponse:
        """
        Returns the input fields an action requirement needs and the current requirement
        action for a sub number order. Action requirements are fulfilled by an external
        step rather than by uploading documents. Australia mobile ID verification is
        currently the only action requirement. Once a verification link has been
        generated, it is returned in `requirement_action.value`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not regulatory_requirement_id:
            raise ValueError(
                f"Expected a non-empty value for `regulatory_requirement_id` but received {regulatory_requirement_id!r}"
            )
        if not sub_number_order_id:
            raise ValueError(
                f"Expected a non-empty value for `sub_number_order_id` but received {sub_number_order_id!r}"
            )
        return self._get(
            path_template(
                "/external_requirements/{regulatory_requirement_id}/sub_number_orders/{sub_number_order_id}",
                regulatory_requirement_id=regulatory_requirement_id,
                sub_number_order_id=sub_number_order_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrderRetrieveResponse,
        )

    def update(
        self,
        sub_number_order_id: str,
        *,
        regulatory_requirement_id: str,
        requirement: sub_number_order_update_params.Requirement,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubNumberOrderUpdateResponse:
        """
        Submits the end user's details to the external verification provider and returns
        the requirement action. Australia mobile ID verification is currently the only
        action requirement. It generates a unique Onfido verification link, returned in
        `requirement_action.value`, which you share with the end user. The end user's
        `first_name` and `last_name` must be nested inside a `requirement` object;
        sending them at the top level is rejected.

        Args:
          requirement: The end user's identity details for the action requirement. Australia mobile ID
              verification is currently the only action requirement. It requires `first_name`
              and `last_name`, the same fields the corresponding GET lists in
              `fields_required`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not regulatory_requirement_id:
            raise ValueError(
                f"Expected a non-empty value for `regulatory_requirement_id` but received {regulatory_requirement_id!r}"
            )
        if not sub_number_order_id:
            raise ValueError(
                f"Expected a non-empty value for `sub_number_order_id` but received {sub_number_order_id!r}"
            )
        return self._post(
            path_template(
                "/external_requirements/{regulatory_requirement_id}/sub_number_orders/{sub_number_order_id}",
                regulatory_requirement_id=regulatory_requirement_id,
                sub_number_order_id=sub_number_order_id,
            ),
            body=maybe_transform(
                {"requirement": requirement}, sub_number_order_update_params.SubNumberOrderUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrderUpdateResponse,
        )


class AsyncSubNumberOrdersResource(AsyncAPIResource):
    """Requirement Groups"""

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
        regulatory_requirement_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubNumberOrderRetrieveResponse:
        """
        Returns the input fields an action requirement needs and the current requirement
        action for a sub number order. Action requirements are fulfilled by an external
        step rather than by uploading documents. Australia mobile ID verification is
        currently the only action requirement. Once a verification link has been
        generated, it is returned in `requirement_action.value`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not regulatory_requirement_id:
            raise ValueError(
                f"Expected a non-empty value for `regulatory_requirement_id` but received {regulatory_requirement_id!r}"
            )
        if not sub_number_order_id:
            raise ValueError(
                f"Expected a non-empty value for `sub_number_order_id` but received {sub_number_order_id!r}"
            )
        return await self._get(
            path_template(
                "/external_requirements/{regulatory_requirement_id}/sub_number_orders/{sub_number_order_id}",
                regulatory_requirement_id=regulatory_requirement_id,
                sub_number_order_id=sub_number_order_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrderRetrieveResponse,
        )

    async def update(
        self,
        sub_number_order_id: str,
        *,
        regulatory_requirement_id: str,
        requirement: sub_number_order_update_params.Requirement,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubNumberOrderUpdateResponse:
        """
        Submits the end user's details to the external verification provider and returns
        the requirement action. Australia mobile ID verification is currently the only
        action requirement. It generates a unique Onfido verification link, returned in
        `requirement_action.value`, which you share with the end user. The end user's
        `first_name` and `last_name` must be nested inside a `requirement` object;
        sending them at the top level is rejected.

        Args:
          requirement: The end user's identity details for the action requirement. Australia mobile ID
              verification is currently the only action requirement. It requires `first_name`
              and `last_name`, the same fields the corresponding GET lists in
              `fields_required`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not regulatory_requirement_id:
            raise ValueError(
                f"Expected a non-empty value for `regulatory_requirement_id` but received {regulatory_requirement_id!r}"
            )
        if not sub_number_order_id:
            raise ValueError(
                f"Expected a non-empty value for `sub_number_order_id` but received {sub_number_order_id!r}"
            )
        return await self._post(
            path_template(
                "/external_requirements/{regulatory_requirement_id}/sub_number_orders/{sub_number_order_id}",
                regulatory_requirement_id=regulatory_requirement_id,
                sub_number_order_id=sub_number_order_id,
            ),
            body=await async_maybe_transform(
                {"requirement": requirement}, sub_number_order_update_params.SubNumberOrderUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrderUpdateResponse,
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


class AsyncSubNumberOrdersResourceWithRawResponse:
    def __init__(self, sub_number_orders: AsyncSubNumberOrdersResource) -> None:
        self._sub_number_orders = sub_number_orders

        self.retrieve = async_to_raw_response_wrapper(
            sub_number_orders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sub_number_orders.update,
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


class AsyncSubNumberOrdersResourceWithStreamingResponse:
    def __init__(self, sub_number_orders: AsyncSubNumberOrdersResource) -> None:
        self._sub_number_orders = sub_number_orders

        self.retrieve = async_to_streamed_response_wrapper(
            sub_number_orders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sub_number_orders.update,
        )
