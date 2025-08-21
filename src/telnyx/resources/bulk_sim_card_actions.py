# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import bulk_sim_card_action_list_params
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
from ..types.bulk_sim_card_action_list_response import BulkSimCardActionListResponse
from ..types.bulk_sim_card_action_retrieve_response import BulkSimCardActionRetrieveResponse

__all__ = ["BulkSimCardActionsResource", "AsyncBulkSimCardActionsResource"]


class BulkSimCardActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkSimCardActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BulkSimCardActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkSimCardActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BulkSimCardActionsResourceWithStreamingResponse(self)

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
    ) -> BulkSimCardActionRetrieveResponse:
        """This API fetches information about a bulk SIM card action.

        A bulk SIM card
        action contains details about a collection of individual SIM card actions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/bulk_sim_card_actions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkSimCardActionRetrieveResponse,
        )

    def list(
        self,
        *,
        filter_action_type: Literal["bulk_set_public_ips"] | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkSimCardActionListResponse:
        """This API lists a paginated collection of bulk SIM card actions.

        A bulk SIM card
        action contains details about a collection of individual SIM card actions.

        Args:
          filter_action_type: Filter by action type.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/bulk_sim_card_actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_action_type": filter_action_type,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    bulk_sim_card_action_list_params.BulkSimCardActionListParams,
                ),
            ),
            cast_to=BulkSimCardActionListResponse,
        )


class AsyncBulkSimCardActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkSimCardActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkSimCardActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkSimCardActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBulkSimCardActionsResourceWithStreamingResponse(self)

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
    ) -> BulkSimCardActionRetrieveResponse:
        """This API fetches information about a bulk SIM card action.

        A bulk SIM card
        action contains details about a collection of individual SIM card actions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/bulk_sim_card_actions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkSimCardActionRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter_action_type: Literal["bulk_set_public_ips"] | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkSimCardActionListResponse:
        """This API lists a paginated collection of bulk SIM card actions.

        A bulk SIM card
        action contains details about a collection of individual SIM card actions.

        Args:
          filter_action_type: Filter by action type.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/bulk_sim_card_actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_action_type": filter_action_type,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    bulk_sim_card_action_list_params.BulkSimCardActionListParams,
                ),
            ),
            cast_to=BulkSimCardActionListResponse,
        )


class BulkSimCardActionsResourceWithRawResponse:
    def __init__(self, bulk_sim_card_actions: BulkSimCardActionsResource) -> None:
        self._bulk_sim_card_actions = bulk_sim_card_actions

        self.retrieve = to_raw_response_wrapper(
            bulk_sim_card_actions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bulk_sim_card_actions.list,
        )


class AsyncBulkSimCardActionsResourceWithRawResponse:
    def __init__(self, bulk_sim_card_actions: AsyncBulkSimCardActionsResource) -> None:
        self._bulk_sim_card_actions = bulk_sim_card_actions

        self.retrieve = async_to_raw_response_wrapper(
            bulk_sim_card_actions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bulk_sim_card_actions.list,
        )


class BulkSimCardActionsResourceWithStreamingResponse:
    def __init__(self, bulk_sim_card_actions: BulkSimCardActionsResource) -> None:
        self._bulk_sim_card_actions = bulk_sim_card_actions

        self.retrieve = to_streamed_response_wrapper(
            bulk_sim_card_actions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bulk_sim_card_actions.list,
        )


class AsyncBulkSimCardActionsResourceWithStreamingResponse:
    def __init__(self, bulk_sim_card_actions: AsyncBulkSimCardActionsResource) -> None:
        self._bulk_sim_card_actions = bulk_sim_card_actions

        self.retrieve = async_to_streamed_response_wrapper(
            bulk_sim_card_actions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bulk_sim_card_actions.list,
        )
