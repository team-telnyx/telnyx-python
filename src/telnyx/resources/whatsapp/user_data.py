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
from ...types.whatsapp import user_data_update_params
from ...types.whatsapp.user_data_update_response import UserDataUpdateResponse
from ...types.whatsapp.user_data_retrieve_response import UserDataRetrieveResponse

__all__ = ["UserDataResource", "AsyncUserDataResource"]


class UserDataResource(SyncAPIResource):
    """Manage Whatsapp business accounts"""

    @cached_property
    def with_raw_response(self) -> UserDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UserDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return UserDataResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDataRetrieveResponse:
        """Fetch Whatsapp user data"""
        return self._get(
            "/v2/whatsapp/user_data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDataRetrieveResponse,
        )

    def update(
        self,
        *,
        webhook_failover_url: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDataUpdateResponse:
        """
        Update Whatsapp user data

        Args:
          webhook_failover_url: Failover URL to send Whatsapp signup events

          webhook_url: URL to send Whatsapp signup events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v2/whatsapp/user_data",
            body=maybe_transform(
                {
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                user_data_update_params.UserDataUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDataUpdateResponse,
        )


class AsyncUserDataResource(AsyncAPIResource):
    """Manage Whatsapp business accounts"""

    @cached_property
    def with_raw_response(self) -> AsyncUserDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return AsyncUserDataResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDataRetrieveResponse:
        """Fetch Whatsapp user data"""
        return await self._get(
            "/v2/whatsapp/user_data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDataRetrieveResponse,
        )

    async def update(
        self,
        *,
        webhook_failover_url: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDataUpdateResponse:
        """
        Update Whatsapp user data

        Args:
          webhook_failover_url: Failover URL to send Whatsapp signup events

          webhook_url: URL to send Whatsapp signup events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v2/whatsapp/user_data",
            body=await async_maybe_transform(
                {
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                user_data_update_params.UserDataUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDataUpdateResponse,
        )


class UserDataResourceWithRawResponse:
    def __init__(self, user_data: UserDataResource) -> None:
        self._user_data = user_data

        self.retrieve = to_raw_response_wrapper(
            user_data.retrieve,
        )
        self.update = to_raw_response_wrapper(
            user_data.update,
        )


class AsyncUserDataResourceWithRawResponse:
    def __init__(self, user_data: AsyncUserDataResource) -> None:
        self._user_data = user_data

        self.retrieve = async_to_raw_response_wrapper(
            user_data.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            user_data.update,
        )


class UserDataResourceWithStreamingResponse:
    def __init__(self, user_data: UserDataResource) -> None:
        self._user_data = user_data

        self.retrieve = to_streamed_response_wrapper(
            user_data.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            user_data.update,
        )


class AsyncUserDataResourceWithStreamingResponse:
    def __init__(self, user_data: AsyncUserDataResource) -> None:
        self._user_data = user_data

        self.retrieve = async_to_streamed_response_wrapper(
            user_data.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            user_data.update,
        )
