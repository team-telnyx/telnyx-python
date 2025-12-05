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
from ..._base_client import make_request_options
from ...types.mobile_phone_numbers import messaging_list_params
from ...types.mobile_phone_numbers.messaging_list_response import MessagingListResponse
from ...types.mobile_phone_numbers.messaging_retrieve_response import MessagingRetrieveResponse

__all__ = ["MessagingResource", "AsyncMessagingResource"]


class MessagingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingRetrieveResponse:
        """
        Retrieve a mobile phone number with messaging settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/mobile_phone_numbers/{id}/messaging",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingRetrieveResponse,
        )

    def list(
        self,
        *,
        page: messaging_list_params.Page | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingListResponse:
        """
        List mobile phone numbers with messaging settings

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/mobile_phone_numbers/messaging",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, messaging_list_params.MessagingListParams),
            ),
            cast_to=MessagingListResponse,
        )


class AsyncMessagingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingRetrieveResponse:
        """
        Retrieve a mobile phone number with messaging settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/mobile_phone_numbers/{id}/messaging",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: messaging_list_params.Page | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingListResponse:
        """
        List mobile phone numbers with messaging settings

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/mobile_phone_numbers/messaging",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, messaging_list_params.MessagingListParams),
            ),
            cast_to=MessagingListResponse,
        )


class MessagingResourceWithRawResponse:
    def __init__(self, messaging: MessagingResource) -> None:
        self._messaging = messaging

        self.retrieve = to_raw_response_wrapper(
            messaging.retrieve,
        )
        self.list = to_raw_response_wrapper(
            messaging.list,
        )


class AsyncMessagingResourceWithRawResponse:
    def __init__(self, messaging: AsyncMessagingResource) -> None:
        self._messaging = messaging

        self.retrieve = async_to_raw_response_wrapper(
            messaging.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            messaging.list,
        )


class MessagingResourceWithStreamingResponse:
    def __init__(self, messaging: MessagingResource) -> None:
        self._messaging = messaging

        self.retrieve = to_streamed_response_wrapper(
            messaging.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            messaging.list,
        )


class AsyncMessagingResourceWithStreamingResponse:
    def __init__(self, messaging: AsyncMessagingResource) -> None:
        self._messaging = messaging

        self.retrieve = async_to_streamed_response_wrapper(
            messaging.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            messaging.list,
        )
