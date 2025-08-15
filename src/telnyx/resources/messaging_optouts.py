# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import messaging_optout_list_params
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
from ..types.messaging_optout_list_response import MessagingOptoutListResponse

__all__ = ["MessagingOptoutsResource", "AsyncMessagingOptoutsResource"]


class MessagingOptoutsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagingOptoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingOptoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingOptoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingOptoutsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        created_at: messaging_optout_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        filter: messaging_optout_list_params.Filter | NotGiven = NOT_GIVEN,
        page: messaging_optout_list_params.Page | NotGiven = NOT_GIVEN,
        redaction_enabled: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingOptoutListResponse:
        """
        Retrieve a list of opt-out blocks.

        Args:
          created_at:
              Consolidated created_at parameter (deepObject style). Originally:
              created_at[gte], created_at[lte]

          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[messaging_profile_id], filter[from]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          redaction_enabled: If receiving address (+E.164 formatted phone number) should be redacted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/messaging_optouts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "filter": filter,
                        "page": page,
                        "redaction_enabled": redaction_enabled,
                    },
                    messaging_optout_list_params.MessagingOptoutListParams,
                ),
            ),
            cast_to=MessagingOptoutListResponse,
        )


class AsyncMessagingOptoutsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagingOptoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingOptoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingOptoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingOptoutsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        created_at: messaging_optout_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        filter: messaging_optout_list_params.Filter | NotGiven = NOT_GIVEN,
        page: messaging_optout_list_params.Page | NotGiven = NOT_GIVEN,
        redaction_enabled: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingOptoutListResponse:
        """
        Retrieve a list of opt-out blocks.

        Args:
          created_at:
              Consolidated created_at parameter (deepObject style). Originally:
              created_at[gte], created_at[lte]

          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[messaging_profile_id], filter[from]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          redaction_enabled: If receiving address (+E.164 formatted phone number) should be redacted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/messaging_optouts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_at": created_at,
                        "filter": filter,
                        "page": page,
                        "redaction_enabled": redaction_enabled,
                    },
                    messaging_optout_list_params.MessagingOptoutListParams,
                ),
            ),
            cast_to=MessagingOptoutListResponse,
        )


class MessagingOptoutsResourceWithRawResponse:
    def __init__(self, messaging_optouts: MessagingOptoutsResource) -> None:
        self._messaging_optouts = messaging_optouts

        self.list = to_raw_response_wrapper(
            messaging_optouts.list,
        )


class AsyncMessagingOptoutsResourceWithRawResponse:
    def __init__(self, messaging_optouts: AsyncMessagingOptoutsResource) -> None:
        self._messaging_optouts = messaging_optouts

        self.list = async_to_raw_response_wrapper(
            messaging_optouts.list,
        )


class MessagingOptoutsResourceWithStreamingResponse:
    def __init__(self, messaging_optouts: MessagingOptoutsResource) -> None:
        self._messaging_optouts = messaging_optouts

        self.list = to_streamed_response_wrapper(
            messaging_optouts.list,
        )


class AsyncMessagingOptoutsResourceWithStreamingResponse:
    def __init__(self, messaging_optouts: AsyncMessagingOptoutsResource) -> None:
        self._messaging_optouts = messaging_optouts

        self.list = async_to_streamed_response_wrapper(
            messaging_optouts.list,
        )
