# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import inbound_channel_update_params
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
from ..types.inbound_channel_list_response import InboundChannelListResponse
from ..types.inbound_channel_update_response import InboundChannelUpdateResponse

__all__ = ["InboundChannelsResource", "AsyncInboundChannelsResource"]


class InboundChannelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return InboundChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return InboundChannelsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        channels: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundChannelUpdateResponse:
        """Update the number of Voice Channels for the US Zone.

        This allows your account to
        handle multiple simultaneous inbound calls to US numbers. Use this endpoint to
        increase or decrease your capacity based on expected call volume.

        Args:
          channels: The new number of concurrent channels for the account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/inbound_channels",
            body=maybe_transform({"channels": channels}, inbound_channel_update_params.InboundChannelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundChannelUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundChannelListResponse:
        """Returns the US Zone voice channels for your account.

        voice channels allows you
        to use Channel Billing for calls to your Telnyx phone numbers. Please check the
        <a href="https://support.telnyx.com/en/articles/8428806-global-channel-billing">Telnyx
        Support Articles</a> section for full information and examples of how to utilize
        Channel Billing.
        """
        return self._get(
            "/inbound_channels",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundChannelListResponse,
        )


class AsyncInboundChannelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncInboundChannelsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        channels: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundChannelUpdateResponse:
        """Update the number of Voice Channels for the US Zone.

        This allows your account to
        handle multiple simultaneous inbound calls to US numbers. Use this endpoint to
        increase or decrease your capacity based on expected call volume.

        Args:
          channels: The new number of concurrent channels for the account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/inbound_channels",
            body=await async_maybe_transform(
                {"channels": channels}, inbound_channel_update_params.InboundChannelUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundChannelUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundChannelListResponse:
        """Returns the US Zone voice channels for your account.

        voice channels allows you
        to use Channel Billing for calls to your Telnyx phone numbers. Please check the
        <a href="https://support.telnyx.com/en/articles/8428806-global-channel-billing">Telnyx
        Support Articles</a> section for full information and examples of how to utilize
        Channel Billing.
        """
        return await self._get(
            "/inbound_channels",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundChannelListResponse,
        )


class InboundChannelsResourceWithRawResponse:
    def __init__(self, inbound_channels: InboundChannelsResource) -> None:
        self._inbound_channels = inbound_channels

        self.update = to_raw_response_wrapper(
            inbound_channels.update,
        )
        self.list = to_raw_response_wrapper(
            inbound_channels.list,
        )


class AsyncInboundChannelsResourceWithRawResponse:
    def __init__(self, inbound_channels: AsyncInboundChannelsResource) -> None:
        self._inbound_channels = inbound_channels

        self.update = async_to_raw_response_wrapper(
            inbound_channels.update,
        )
        self.list = async_to_raw_response_wrapper(
            inbound_channels.list,
        )


class InboundChannelsResourceWithStreamingResponse:
    def __init__(self, inbound_channels: InboundChannelsResource) -> None:
        self._inbound_channels = inbound_channels

        self.update = to_streamed_response_wrapper(
            inbound_channels.update,
        )
        self.list = to_streamed_response_wrapper(
            inbound_channels.list,
        )


class AsyncInboundChannelsResourceWithStreamingResponse:
    def __init__(self, inbound_channels: AsyncInboundChannelsResource) -> None:
        self._inbound_channels = inbound_channels

        self.update = async_to_streamed_response_wrapper(
            inbound_channels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            inbound_channels.list,
        )
