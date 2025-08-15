# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import messaging_numbers_bulk_update_create_params
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
from ..types.messaging_numbers_bulk_update_create_response import MessagingNumbersBulkUpdateCreateResponse
from ..types.messaging_numbers_bulk_update_retrieve_response import MessagingNumbersBulkUpdateRetrieveResponse

__all__ = ["MessagingNumbersBulkUpdatesResource", "AsyncMessagingNumbersBulkUpdatesResource"]


class MessagingNumbersBulkUpdatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagingNumbersBulkUpdatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingNumbersBulkUpdatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingNumbersBulkUpdatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingNumbersBulkUpdatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        messaging_profile_id: str,
        numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingNumbersBulkUpdateCreateResponse:
        """
        Update the messaging profile of multiple phone numbers

        Args:
          messaging_profile_id:
              Configure the messaging profile these phone numbers are assigned to:

              - Set this field to `""` to unassign each number from their respective messaging
                profile
              - Set this field to a quoted UUID of a messaging profile to assign these numbers
                to that messaging profile

          numbers: The list of phone numbers to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messaging_numbers_bulk_updates",
            body=maybe_transform(
                {
                    "messaging_profile_id": messaging_profile_id,
                    "numbers": numbers,
                },
                messaging_numbers_bulk_update_create_params.MessagingNumbersBulkUpdateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingNumbersBulkUpdateCreateResponse,
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
    ) -> MessagingNumbersBulkUpdateRetrieveResponse:
        """
        Retrieve bulk update status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return self._get(
            f"/messaging_numbers_bulk_updates/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingNumbersBulkUpdateRetrieveResponse,
        )


class AsyncMessagingNumbersBulkUpdatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagingNumbersBulkUpdatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingNumbersBulkUpdatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingNumbersBulkUpdatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingNumbersBulkUpdatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        messaging_profile_id: str,
        numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingNumbersBulkUpdateCreateResponse:
        """
        Update the messaging profile of multiple phone numbers

        Args:
          messaging_profile_id:
              Configure the messaging profile these phone numbers are assigned to:

              - Set this field to `""` to unassign each number from their respective messaging
                profile
              - Set this field to a quoted UUID of a messaging profile to assign these numbers
                to that messaging profile

          numbers: The list of phone numbers to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messaging_numbers_bulk_updates",
            body=await async_maybe_transform(
                {
                    "messaging_profile_id": messaging_profile_id,
                    "numbers": numbers,
                },
                messaging_numbers_bulk_update_create_params.MessagingNumbersBulkUpdateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingNumbersBulkUpdateCreateResponse,
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
    ) -> MessagingNumbersBulkUpdateRetrieveResponse:
        """
        Retrieve bulk update status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return await self._get(
            f"/messaging_numbers_bulk_updates/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingNumbersBulkUpdateRetrieveResponse,
        )


class MessagingNumbersBulkUpdatesResourceWithRawResponse:
    def __init__(self, messaging_numbers_bulk_updates: MessagingNumbersBulkUpdatesResource) -> None:
        self._messaging_numbers_bulk_updates = messaging_numbers_bulk_updates

        self.create = to_raw_response_wrapper(
            messaging_numbers_bulk_updates.create,
        )
        self.retrieve = to_raw_response_wrapper(
            messaging_numbers_bulk_updates.retrieve,
        )


class AsyncMessagingNumbersBulkUpdatesResourceWithRawResponse:
    def __init__(self, messaging_numbers_bulk_updates: AsyncMessagingNumbersBulkUpdatesResource) -> None:
        self._messaging_numbers_bulk_updates = messaging_numbers_bulk_updates

        self.create = async_to_raw_response_wrapper(
            messaging_numbers_bulk_updates.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            messaging_numbers_bulk_updates.retrieve,
        )


class MessagingNumbersBulkUpdatesResourceWithStreamingResponse:
    def __init__(self, messaging_numbers_bulk_updates: MessagingNumbersBulkUpdatesResource) -> None:
        self._messaging_numbers_bulk_updates = messaging_numbers_bulk_updates

        self.create = to_streamed_response_wrapper(
            messaging_numbers_bulk_updates.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            messaging_numbers_bulk_updates.retrieve,
        )


class AsyncMessagingNumbersBulkUpdatesResourceWithStreamingResponse:
    def __init__(self, messaging_numbers_bulk_updates: AsyncMessagingNumbersBulkUpdatesResource) -> None:
        self._messaging_numbers_bulk_updates = messaging_numbers_bulk_updates

        self.create = async_to_streamed_response_wrapper(
            messaging_numbers_bulk_updates.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            messaging_numbers_bulk_updates.retrieve,
        )
