# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["LlmTokenGatewayResource", "AsyncLlmTokenGatewayResource"]


class LlmTokenGatewayResource(SyncAPIResource):
    @cached_property
    def usage(self) -> UsageResource:
        """Manage and report AI Gateway traffic."""
        return UsageResource(self._client)

    @cached_property
    def with_raw_response(self) -> LlmTokenGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return LlmTokenGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlmTokenGatewayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return LlmTokenGatewayResourceWithStreamingResponse(self)


class AsyncLlmTokenGatewayResource(AsyncAPIResource):
    @cached_property
    def usage(self) -> AsyncUsageResource:
        """Manage and report AI Gateway traffic."""
        return AsyncUsageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLlmTokenGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLlmTokenGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlmTokenGatewayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncLlmTokenGatewayResourceWithStreamingResponse(self)


class LlmTokenGatewayResourceWithRawResponse:
    def __init__(self, llm_token_gateway: LlmTokenGatewayResource) -> None:
        self._llm_token_gateway = llm_token_gateway

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        """Manage and report AI Gateway traffic."""
        return UsageResourceWithRawResponse(self._llm_token_gateway.usage)


class AsyncLlmTokenGatewayResourceWithRawResponse:
    def __init__(self, llm_token_gateway: AsyncLlmTokenGatewayResource) -> None:
        self._llm_token_gateway = llm_token_gateway

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        """Manage and report AI Gateway traffic."""
        return AsyncUsageResourceWithRawResponse(self._llm_token_gateway.usage)


class LlmTokenGatewayResourceWithStreamingResponse:
    def __init__(self, llm_token_gateway: LlmTokenGatewayResource) -> None:
        self._llm_token_gateway = llm_token_gateway

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        """Manage and report AI Gateway traffic."""
        return UsageResourceWithStreamingResponse(self._llm_token_gateway.usage)


class AsyncLlmTokenGatewayResourceWithStreamingResponse:
    def __init__(self, llm_token_gateway: AsyncLlmTokenGatewayResource) -> None:
        self._llm_token_gateway = llm_token_gateway

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        """Manage and report AI Gateway traffic."""
        return AsyncUsageResourceWithStreamingResponse(self._llm_token_gateway.usage)
