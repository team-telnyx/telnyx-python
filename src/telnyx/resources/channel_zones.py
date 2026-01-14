# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import channel_zone_list_params, channel_zone_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.channel_zone_list_response import ChannelZoneListResponse
from ..types.channel_zone_update_response import ChannelZoneUpdateResponse

__all__ = ["ChannelZonesResource", "AsyncChannelZonesResource"]


class ChannelZonesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChannelZonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ChannelZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelZonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ChannelZonesResourceWithStreamingResponse(self)

    def update(
        self,
        channel_zone_id: str,
        *,
        channels: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelZoneUpdateResponse:
        """Update the number of Voice Channels for the Non-US Zones.

        This allows your
        account to handle multiple simultaneous inbound calls to Non-US numbers. Use
        this endpoint to increase or decrease your capacity based on expected call
        volume.

        Args:
          channels: The number of reserved channels

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_zone_id:
            raise ValueError(f"Expected a non-empty value for `channel_zone_id` but received {channel_zone_id!r}")
        return self._put(
            f"/channel_zones/{channel_zone_id}",
            body=maybe_transform({"channels": channels}, channel_zone_update_params.ChannelZoneUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelZoneUpdateResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[ChannelZoneListResponse]:
        """Returns the non-US voice channels for your account.

        voice channels allow you to
        use Channel Billing for calls to your Telnyx phone numbers. Please check the
        <a href="https://support.telnyx.com/en/articles/8428806-global-channel-billing">Telnyx
        Support Articles</a> section for full information and examples of how to utilize
        Channel Billing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/channel_zones",
            page=SyncDefaultFlatPagination[ChannelZoneListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    channel_zone_list_params.ChannelZoneListParams,
                ),
            ),
            model=ChannelZoneListResponse,
        )


class AsyncChannelZonesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChannelZonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelZonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncChannelZonesResourceWithStreamingResponse(self)

    async def update(
        self,
        channel_zone_id: str,
        *,
        channels: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelZoneUpdateResponse:
        """Update the number of Voice Channels for the Non-US Zones.

        This allows your
        account to handle multiple simultaneous inbound calls to Non-US numbers. Use
        this endpoint to increase or decrease your capacity based on expected call
        volume.

        Args:
          channels: The number of reserved channels

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_zone_id:
            raise ValueError(f"Expected a non-empty value for `channel_zone_id` but received {channel_zone_id!r}")
        return await self._put(
            f"/channel_zones/{channel_zone_id}",
            body=await async_maybe_transform(
                {"channels": channels}, channel_zone_update_params.ChannelZoneUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelZoneUpdateResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ChannelZoneListResponse, AsyncDefaultFlatPagination[ChannelZoneListResponse]]:
        """Returns the non-US voice channels for your account.

        voice channels allow you to
        use Channel Billing for calls to your Telnyx phone numbers. Please check the
        <a href="https://support.telnyx.com/en/articles/8428806-global-channel-billing">Telnyx
        Support Articles</a> section for full information and examples of how to utilize
        Channel Billing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/channel_zones",
            page=AsyncDefaultFlatPagination[ChannelZoneListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    channel_zone_list_params.ChannelZoneListParams,
                ),
            ),
            model=ChannelZoneListResponse,
        )


class ChannelZonesResourceWithRawResponse:
    def __init__(self, channel_zones: ChannelZonesResource) -> None:
        self._channel_zones = channel_zones

        self.update = to_raw_response_wrapper(
            channel_zones.update,
        )
        self.list = to_raw_response_wrapper(
            channel_zones.list,
        )


class AsyncChannelZonesResourceWithRawResponse:
    def __init__(self, channel_zones: AsyncChannelZonesResource) -> None:
        self._channel_zones = channel_zones

        self.update = async_to_raw_response_wrapper(
            channel_zones.update,
        )
        self.list = async_to_raw_response_wrapper(
            channel_zones.list,
        )


class ChannelZonesResourceWithStreamingResponse:
    def __init__(self, channel_zones: ChannelZonesResource) -> None:
        self._channel_zones = channel_zones

        self.update = to_streamed_response_wrapper(
            channel_zones.update,
        )
        self.list = to_streamed_response_wrapper(
            channel_zones.list,
        )


class AsyncChannelZonesResourceWithStreamingResponse:
    def __init__(self, channel_zones: AsyncChannelZonesResource) -> None:
        self._channel_zones = channel_zones

        self.update = async_to_streamed_response_wrapper(
            channel_zones.update,
        )
        self.list = async_to_streamed_response_wrapper(
            channel_zones.list,
        )
