# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["OsrResource", "AsyncOsrResource"]


class OsrResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OsrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return OsrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OsrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return OsrResourceWithStreamingResponse(self)

    def get_attributes(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get My Osr Campaign Attributes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._get(
            f"/campaign/{campaign_id}/osr/attributes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOsrResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOsrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOsrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOsrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncOsrResourceWithStreamingResponse(self)

    async def get_attributes(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get My Osr Campaign Attributes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._get(
            f"/campaign/{campaign_id}/osr/attributes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OsrResourceWithRawResponse:
    def __init__(self, osr: OsrResource) -> None:
        self._osr = osr

        self.get_attributes = to_raw_response_wrapper(
            osr.get_attributes,
        )


class AsyncOsrResourceWithRawResponse:
    def __init__(self, osr: AsyncOsrResource) -> None:
        self._osr = osr

        self.get_attributes = async_to_raw_response_wrapper(
            osr.get_attributes,
        )


class OsrResourceWithStreamingResponse:
    def __init__(self, osr: OsrResource) -> None:
        self._osr = osr

        self.get_attributes = to_streamed_response_wrapper(
            osr.get_attributes,
        )


class AsyncOsrResourceWithStreamingResponse:
    def __init__(self, osr: AsyncOsrResource) -> None:
        self._osr = osr

        self.get_attributes = async_to_streamed_response_wrapper(
            osr.get_attributes,
        )
