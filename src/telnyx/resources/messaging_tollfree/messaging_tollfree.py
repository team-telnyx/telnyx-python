# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .verification.verification import (
    VerificationResource,
    AsyncVerificationResource,
    VerificationResourceWithRawResponse,
    AsyncVerificationResourceWithRawResponse,
    VerificationResourceWithStreamingResponse,
    AsyncVerificationResourceWithStreamingResponse,
)

__all__ = ["MessagingTollfreeResource", "AsyncMessagingTollfreeResource"]


class MessagingTollfreeResource(SyncAPIResource):
    @cached_property
    def verification(self) -> VerificationResource:
        return VerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> MessagingTollfreeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingTollfreeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingTollfreeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingTollfreeResourceWithStreamingResponse(self)


class AsyncMessagingTollfreeResource(AsyncAPIResource):
    @cached_property
    def verification(self) -> AsyncVerificationResource:
        return AsyncVerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMessagingTollfreeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingTollfreeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingTollfreeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingTollfreeResourceWithStreamingResponse(self)


class MessagingTollfreeResourceWithRawResponse:
    def __init__(self, messaging_tollfree: MessagingTollfreeResource) -> None:
        self._messaging_tollfree = messaging_tollfree

    @cached_property
    def verification(self) -> VerificationResourceWithRawResponse:
        return VerificationResourceWithRawResponse(self._messaging_tollfree.verification)


class AsyncMessagingTollfreeResourceWithRawResponse:
    def __init__(self, messaging_tollfree: AsyncMessagingTollfreeResource) -> None:
        self._messaging_tollfree = messaging_tollfree

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithRawResponse:
        return AsyncVerificationResourceWithRawResponse(self._messaging_tollfree.verification)


class MessagingTollfreeResourceWithStreamingResponse:
    def __init__(self, messaging_tollfree: MessagingTollfreeResource) -> None:
        self._messaging_tollfree = messaging_tollfree

    @cached_property
    def verification(self) -> VerificationResourceWithStreamingResponse:
        return VerificationResourceWithStreamingResponse(self._messaging_tollfree.verification)


class AsyncMessagingTollfreeResourceWithStreamingResponse:
    def __init__(self, messaging_tollfree: AsyncMessagingTollfreeResource) -> None:
        self._messaging_tollfree = messaging_tollfree

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithStreamingResponse:
        return AsyncVerificationResourceWithStreamingResponse(self._messaging_tollfree.verification)
