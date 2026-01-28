# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.porting_orders import action_requirement_list_params, action_requirement_initiate_params
from ...types.porting_orders.action_requirement_list_response import ActionRequirementListResponse
from ...types.porting_orders.action_requirement_initiate_response import ActionRequirementInitiateResponse

__all__ = ["ActionRequirementsResource", "AsyncActionRequirementsResource"]


class ActionRequirementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionRequirementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActionRequirementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionRequirementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActionRequirementsResourceWithStreamingResponse(self)

    def list(
        self,
        porting_order_id: str,
        *,
        filter: action_requirement_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: action_requirement_list_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[ActionRequirementListResponse]:
        """
        Returns a list of action requirements for a specific porting order.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[id][in][],
              filter[requirement_type_id], filter[action_type], filter[status]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        return self._get_api_list(
            f"/porting_orders/{porting_order_id}/action_requirements",
            page=SyncDefaultFlatPagination[ActionRequirementListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    action_requirement_list_params.ActionRequirementListParams,
                ),
            ),
            model=ActionRequirementListResponse,
        )

    def initiate(
        self,
        id: str,
        *,
        porting_order_id: str,
        params: action_requirement_initiate_params.Params,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRequirementInitiateResponse:
        """
        Initiates a specific action requirement for a porting order.

        Args:
          params: Required information for initiating the action requirement for AU ID
              verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/porting_orders/{porting_order_id}/action_requirements/{id}/initiate",
            body=maybe_transform(
                {"params": params}, action_requirement_initiate_params.ActionRequirementInitiateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRequirementInitiateResponse,
        )


class AsyncActionRequirementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionRequirementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionRequirementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionRequirementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActionRequirementsResourceWithStreamingResponse(self)

    def list(
        self,
        porting_order_id: str,
        *,
        filter: action_requirement_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: action_requirement_list_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ActionRequirementListResponse, AsyncDefaultFlatPagination[ActionRequirementListResponse]]:
        """
        Returns a list of action requirements for a specific porting order.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[id][in][],
              filter[requirement_type_id], filter[action_type], filter[status]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        return self._get_api_list(
            f"/porting_orders/{porting_order_id}/action_requirements",
            page=AsyncDefaultFlatPagination[ActionRequirementListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    action_requirement_list_params.ActionRequirementListParams,
                ),
            ),
            model=ActionRequirementListResponse,
        )

    async def initiate(
        self,
        id: str,
        *,
        porting_order_id: str,
        params: action_requirement_initiate_params.Params,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRequirementInitiateResponse:
        """
        Initiates a specific action requirement for a porting order.

        Args:
          params: Required information for initiating the action requirement for AU ID
              verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/porting_orders/{porting_order_id}/action_requirements/{id}/initiate",
            body=await async_maybe_transform(
                {"params": params}, action_requirement_initiate_params.ActionRequirementInitiateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRequirementInitiateResponse,
        )


class ActionRequirementsResourceWithRawResponse:
    def __init__(self, action_requirements: ActionRequirementsResource) -> None:
        self._action_requirements = action_requirements

        self.list = to_raw_response_wrapper(
            action_requirements.list,
        )
        self.initiate = to_raw_response_wrapper(
            action_requirements.initiate,
        )


class AsyncActionRequirementsResourceWithRawResponse:
    def __init__(self, action_requirements: AsyncActionRequirementsResource) -> None:
        self._action_requirements = action_requirements

        self.list = async_to_raw_response_wrapper(
            action_requirements.list,
        )
        self.initiate = async_to_raw_response_wrapper(
            action_requirements.initiate,
        )


class ActionRequirementsResourceWithStreamingResponse:
    def __init__(self, action_requirements: ActionRequirementsResource) -> None:
        self._action_requirements = action_requirements

        self.list = to_streamed_response_wrapper(
            action_requirements.list,
        )
        self.initiate = to_streamed_response_wrapper(
            action_requirements.initiate,
        )


class AsyncActionRequirementsResourceWithStreamingResponse:
    def __init__(self, action_requirements: AsyncActionRequirementsResource) -> None:
        self._action_requirements = action_requirements

        self.list = async_to_streamed_response_wrapper(
            action_requirements.list,
        )
        self.initiate = async_to_streamed_response_wrapper(
            action_requirements.initiate,
        )
