# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AnthropicResource", "AsyncAnthropicResource"]


class AnthropicResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AnthropicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AnthropicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnthropicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AnthropicResourceWithStreamingResponse(self)


class AsyncAnthropicResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnthropicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnthropicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnthropicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAnthropicResourceWithStreamingResponse(self)


class AnthropicResourceWithRawResponse:
    def __init__(self, anthropic: AnthropicResource) -> None:
        self._anthropic = anthropic

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self._anthropic.v1)


class AsyncAnthropicResourceWithRawResponse:
    def __init__(self, anthropic: AsyncAnthropicResource) -> None:
        self._anthropic = anthropic

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self._anthropic.v1)


class AnthropicResourceWithStreamingResponse:
    def __init__(self, anthropic: AnthropicResource) -> None:
        self._anthropic = anthropic

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self._anthropic.v1)


class AsyncAnthropicResourceWithStreamingResponse:
    def __init__(self, anthropic: AsyncAnthropicResource) -> None:
        self._anthropic = anthropic

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self._anthropic.v1)
