# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .spend import (
    SpendResource,
    AsyncSpendResource,
    SpendResourceWithRawResponse,
    AsyncSpendResourceWithRawResponse,
    SpendResourceWithStreamingResponse,
    AsyncSpendResourceWithStreamingResponse,
)
from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .token_keys import (
    TokenKeysResource,
    AsyncTokenKeysResource,
    TokenKeysResourceWithRawResponse,
    AsyncTokenKeysResourceWithRawResponse,
    TokenKeysResourceWithStreamingResponse,
    AsyncTokenKeysResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .token_groups import (
    TokenGroupsResource,
    AsyncTokenGroupsResource,
    TokenGroupsResourceWithRawResponse,
    AsyncTokenGroupsResourceWithRawResponse,
    TokenGroupsResourceWithStreamingResponse,
    AsyncTokenGroupsResourceWithStreamingResponse,
)

__all__ = ["LlmTokenGatewayResource", "AsyncLlmTokenGatewayResource"]


class LlmTokenGatewayResource(SyncAPIResource):
    @cached_property
    def usage(self) -> UsageResource:
        """Manage and report AI Gateway usage."""
        return UsageResource(self._client)

    @cached_property
    def spend(self) -> SpendResource:
        """Manage and report AI Gateway usage."""
        return SpendResource(self._client)

    @cached_property
    def token_groups(self) -> TokenGroupsResource:
        """Manage and report AI Gateway usage."""
        return TokenGroupsResource(self._client)

    @cached_property
    def token_keys(self) -> TokenKeysResource:
        """Manage and report AI Gateway usage."""
        return TokenKeysResource(self._client)

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
        """Manage and report AI Gateway usage."""
        return AsyncUsageResource(self._client)

    @cached_property
    def spend(self) -> AsyncSpendResource:
        """Manage and report AI Gateway usage."""
        return AsyncSpendResource(self._client)

    @cached_property
    def token_groups(self) -> AsyncTokenGroupsResource:
        """Manage and report AI Gateway usage."""
        return AsyncTokenGroupsResource(self._client)

    @cached_property
    def token_keys(self) -> AsyncTokenKeysResource:
        """Manage and report AI Gateway usage."""
        return AsyncTokenKeysResource(self._client)

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
        """Manage and report AI Gateway usage."""
        return UsageResourceWithRawResponse(self._llm_token_gateway.usage)

    @cached_property
    def spend(self) -> SpendResourceWithRawResponse:
        """Manage and report AI Gateway usage."""
        return SpendResourceWithRawResponse(self._llm_token_gateway.spend)

    @cached_property
    def token_groups(self) -> TokenGroupsResourceWithRawResponse:
        """Manage and report AI Gateway usage."""
        return TokenGroupsResourceWithRawResponse(self._llm_token_gateway.token_groups)

    @cached_property
    def token_keys(self) -> TokenKeysResourceWithRawResponse:
        """Manage and report AI Gateway usage."""
        return TokenKeysResourceWithRawResponse(self._llm_token_gateway.token_keys)


class AsyncLlmTokenGatewayResourceWithRawResponse:
    def __init__(self, llm_token_gateway: AsyncLlmTokenGatewayResource) -> None:
        self._llm_token_gateway = llm_token_gateway

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        """Manage and report AI Gateway usage."""
        return AsyncUsageResourceWithRawResponse(self._llm_token_gateway.usage)

    @cached_property
    def spend(self) -> AsyncSpendResourceWithRawResponse:
        """Manage and report AI Gateway usage."""
        return AsyncSpendResourceWithRawResponse(self._llm_token_gateway.spend)

    @cached_property
    def token_groups(self) -> AsyncTokenGroupsResourceWithRawResponse:
        """Manage and report AI Gateway usage."""
        return AsyncTokenGroupsResourceWithRawResponse(self._llm_token_gateway.token_groups)

    @cached_property
    def token_keys(self) -> AsyncTokenKeysResourceWithRawResponse:
        """Manage and report AI Gateway usage."""
        return AsyncTokenKeysResourceWithRawResponse(self._llm_token_gateway.token_keys)


class LlmTokenGatewayResourceWithStreamingResponse:
    def __init__(self, llm_token_gateway: LlmTokenGatewayResource) -> None:
        self._llm_token_gateway = llm_token_gateway

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        """Manage and report AI Gateway usage."""
        return UsageResourceWithStreamingResponse(self._llm_token_gateway.usage)

    @cached_property
    def spend(self) -> SpendResourceWithStreamingResponse:
        """Manage and report AI Gateway usage."""
        return SpendResourceWithStreamingResponse(self._llm_token_gateway.spend)

    @cached_property
    def token_groups(self) -> TokenGroupsResourceWithStreamingResponse:
        """Manage and report AI Gateway usage."""
        return TokenGroupsResourceWithStreamingResponse(self._llm_token_gateway.token_groups)

    @cached_property
    def token_keys(self) -> TokenKeysResourceWithStreamingResponse:
        """Manage and report AI Gateway usage."""
        return TokenKeysResourceWithStreamingResponse(self._llm_token_gateway.token_keys)


class AsyncLlmTokenGatewayResourceWithStreamingResponse:
    def __init__(self, llm_token_gateway: AsyncLlmTokenGatewayResource) -> None:
        self._llm_token_gateway = llm_token_gateway

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        """Manage and report AI Gateway usage."""
        return AsyncUsageResourceWithStreamingResponse(self._llm_token_gateway.usage)

    @cached_property
    def spend(self) -> AsyncSpendResourceWithStreamingResponse:
        """Manage and report AI Gateway usage."""
        return AsyncSpendResourceWithStreamingResponse(self._llm_token_gateway.spend)

    @cached_property
    def token_groups(self) -> AsyncTokenGroupsResourceWithStreamingResponse:
        """Manage and report AI Gateway usage."""
        return AsyncTokenGroupsResourceWithStreamingResponse(self._llm_token_gateway.token_groups)

    @cached_property
    def token_keys(self) -> AsyncTokenKeysResourceWithStreamingResponse:
        """Manage and report AI Gateway usage."""
        return AsyncTokenKeysResourceWithStreamingResponse(self._llm_token_gateway.token_keys)
