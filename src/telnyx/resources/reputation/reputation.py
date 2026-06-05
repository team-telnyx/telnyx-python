# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .numbers import (
    NumbersResource,
    AsyncNumbersResource,
    NumbersResourceWithRawResponse,
    AsyncNumbersResourceWithRawResponse,
    NumbersResourceWithStreamingResponse,
    AsyncNumbersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ReputationResource", "AsyncReputationResource"]


class ReputationResource(SyncAPIResource):
    @cached_property
    def numbers(self) -> NumbersResource:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return NumbersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReputationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ReputationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReputationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ReputationResourceWithStreamingResponse(self)


class AsyncReputationResource(AsyncAPIResource):
    @cached_property
    def numbers(self) -> AsyncNumbersResource:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncNumbersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReputationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReputationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReputationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncReputationResourceWithStreamingResponse(self)


class ReputationResourceWithRawResponse:
    def __init__(self, reputation: ReputationResource) -> None:
        self._reputation = reputation

    @cached_property
    def numbers(self) -> NumbersResourceWithRawResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return NumbersResourceWithRawResponse(self._reputation.numbers)


class AsyncReputationResourceWithRawResponse:
    def __init__(self, reputation: AsyncReputationResource) -> None:
        self._reputation = reputation

    @cached_property
    def numbers(self) -> AsyncNumbersResourceWithRawResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncNumbersResourceWithRawResponse(self._reputation.numbers)


class ReputationResourceWithStreamingResponse:
    def __init__(self, reputation: ReputationResource) -> None:
        self._reputation = reputation

    @cached_property
    def numbers(self) -> NumbersResourceWithStreamingResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return NumbersResourceWithStreamingResponse(self._reputation.numbers)


class AsyncReputationResourceWithStreamingResponse:
    def __init__(self, reputation: AsyncReputationResource) -> None:
        self._reputation = reputation

    @cached_property
    def numbers(self) -> AsyncNumbersResourceWithStreamingResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncNumbersResourceWithStreamingResponse(self._reputation.numbers)
