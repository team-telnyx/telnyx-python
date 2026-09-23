# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.noise_suppression_engine_list_response import NoiseSuppressionEngineListResponse

__all__ = ["NoiseSuppressionEnginesResource", "AsyncNoiseSuppressionEnginesResource"]


class NoiseSuppressionEnginesResource(SyncAPIResource):
    """
    Noise suppression engines that can be selected when configuring noise suppression on voice connections.
    """

    @cached_property
    def with_raw_response(self) -> NoiseSuppressionEnginesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NoiseSuppressionEnginesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NoiseSuppressionEnginesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NoiseSuppressionEnginesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NoiseSuppressionEngineListResponse:
        """
        Returns all noise suppression engines available to the authenticated user.
        Engines gated behind a feature flag are included only when the flag is enabled
        for the user's account. Results are not paginated; the number of engines is
        expected to remain small.
        """
        return self._get(
            "/noise_suppression_engines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoiseSuppressionEngineListResponse,
        )


class AsyncNoiseSuppressionEnginesResource(AsyncAPIResource):
    """
    Noise suppression engines that can be selected when configuring noise suppression on voice connections.
    """

    @cached_property
    def with_raw_response(self) -> AsyncNoiseSuppressionEnginesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNoiseSuppressionEnginesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNoiseSuppressionEnginesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNoiseSuppressionEnginesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NoiseSuppressionEngineListResponse:
        """
        Returns all noise suppression engines available to the authenticated user.
        Engines gated behind a feature flag are included only when the flag is enabled
        for the user's account. Results are not paginated; the number of engines is
        expected to remain small.
        """
        return await self._get(
            "/noise_suppression_engines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoiseSuppressionEngineListResponse,
        )


class NoiseSuppressionEnginesResourceWithRawResponse:
    def __init__(self, noise_suppression_engines: NoiseSuppressionEnginesResource) -> None:
        self._noise_suppression_engines = noise_suppression_engines

        self.list = to_raw_response_wrapper(
            noise_suppression_engines.list,
        )


class AsyncNoiseSuppressionEnginesResourceWithRawResponse:
    def __init__(self, noise_suppression_engines: AsyncNoiseSuppressionEnginesResource) -> None:
        self._noise_suppression_engines = noise_suppression_engines

        self.list = async_to_raw_response_wrapper(
            noise_suppression_engines.list,
        )


class NoiseSuppressionEnginesResourceWithStreamingResponse:
    def __init__(self, noise_suppression_engines: NoiseSuppressionEnginesResource) -> None:
        self._noise_suppression_engines = noise_suppression_engines

        self.list = to_streamed_response_wrapper(
            noise_suppression_engines.list,
        )


class AsyncNoiseSuppressionEnginesResourceWithStreamingResponse:
    def __init__(self, noise_suppression_engines: AsyncNoiseSuppressionEnginesResource) -> None:
        self._noise_suppression_engines = noise_suppression_engines

        self.list = async_to_streamed_response_wrapper(
            noise_suppression_engines.list,
        )
