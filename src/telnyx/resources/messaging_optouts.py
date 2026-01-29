# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import messaging_optout_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
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
        created_at: messaging_optout_list_params.CreatedAt | Omit = omit,
        filter: messaging_optout_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        redaction_enabled: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[MessagingOptoutListResponse]:
        """
        Retrieve a list of opt-out blocks.

        Args:
          created_at:
              Consolidated created_at parameter (deepObject style). Originally:
              created_at[gte], created_at[lte]

          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[messaging_profile_id], filter[from]

          redaction_enabled: If receiving address (+E.164 formatted phone number) should be redacted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/messaging_optouts",
            page=SyncDefaultFlatPagination[MessagingOptoutListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "redaction_enabled": redaction_enabled,
                    },
                    messaging_optout_list_params.MessagingOptoutListParams,
                ),
            ),
            model=MessagingOptoutListResponse,
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

    def list(
        self,
        *,
        created_at: messaging_optout_list_params.CreatedAt | Omit = omit,
        filter: messaging_optout_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        redaction_enabled: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MessagingOptoutListResponse, AsyncDefaultFlatPagination[MessagingOptoutListResponse]]:
        """
        Retrieve a list of opt-out blocks.

        Args:
          created_at:
              Consolidated created_at parameter (deepObject style). Originally:
              created_at[gte], created_at[lte]

          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[messaging_profile_id], filter[from]

          redaction_enabled: If receiving address (+E.164 formatted phone number) should be redacted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/messaging_optouts",
            page=AsyncDefaultFlatPagination[MessagingOptoutListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "redaction_enabled": redaction_enabled,
                    },
                    messaging_optout_list_params.MessagingOptoutListParams,
                ),
            ),
            model=MessagingOptoutListResponse,
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
