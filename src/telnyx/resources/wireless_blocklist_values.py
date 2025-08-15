# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import wireless_blocklist_value_list_params
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
from ..types.wireless_blocklist_value_list_response import WirelessBlocklistValueListResponse

__all__ = ["WirelessBlocklistValuesResource", "AsyncWirelessBlocklistValuesResource"]


class WirelessBlocklistValuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WirelessBlocklistValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return WirelessBlocklistValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WirelessBlocklistValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return WirelessBlocklistValuesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        type: Literal["country", "mcc", "plmn"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WirelessBlocklistValueListResponse:
        """
        Retrieve all wireless blocklist values for a given blocklist type.

        Args:
          type: The Wireless Blocklist type for which to list possible values (e.g., `country`,
              `mcc`, `plmn`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/wireless_blocklist_values",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"type": type}, wireless_blocklist_value_list_params.WirelessBlocklistValueListParams
                ),
            ),
            cast_to=WirelessBlocklistValueListResponse,
        )


class AsyncWirelessBlocklistValuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWirelessBlocklistValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWirelessBlocklistValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWirelessBlocklistValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncWirelessBlocklistValuesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        type: Literal["country", "mcc", "plmn"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WirelessBlocklistValueListResponse:
        """
        Retrieve all wireless blocklist values for a given blocklist type.

        Args:
          type: The Wireless Blocklist type for which to list possible values (e.g., `country`,
              `mcc`, `plmn`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/wireless_blocklist_values",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, wireless_blocklist_value_list_params.WirelessBlocklistValueListParams
                ),
            ),
            cast_to=WirelessBlocklistValueListResponse,
        )


class WirelessBlocklistValuesResourceWithRawResponse:
    def __init__(self, wireless_blocklist_values: WirelessBlocklistValuesResource) -> None:
        self._wireless_blocklist_values = wireless_blocklist_values

        self.list = to_raw_response_wrapper(
            wireless_blocklist_values.list,
        )


class AsyncWirelessBlocklistValuesResourceWithRawResponse:
    def __init__(self, wireless_blocklist_values: AsyncWirelessBlocklistValuesResource) -> None:
        self._wireless_blocklist_values = wireless_blocklist_values

        self.list = async_to_raw_response_wrapper(
            wireless_blocklist_values.list,
        )


class WirelessBlocklistValuesResourceWithStreamingResponse:
    def __init__(self, wireless_blocklist_values: WirelessBlocklistValuesResource) -> None:
        self._wireless_blocklist_values = wireless_blocklist_values

        self.list = to_streamed_response_wrapper(
            wireless_blocklist_values.list,
        )


class AsyncWirelessBlocklistValuesResourceWithStreamingResponse:
    def __init__(self, wireless_blocklist_values: AsyncWirelessBlocklistValuesResource) -> None:
        self._wireless_blocklist_values = wireless_blocklist_values

        self.list = async_to_streamed_response_wrapper(
            wireless_blocklist_values.list,
        )
