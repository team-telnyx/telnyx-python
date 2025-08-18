# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rcs.rcs import (
    RcsResource,
    AsyncRcsResource,
    RcsResourceWithRawResponse,
    AsyncRcsResourceWithRawResponse,
    RcsResourceWithStreamingResponse,
    AsyncRcsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MessagingResource", "AsyncMessagingResource"]


class MessagingResource(SyncAPIResource):
    @cached_property
    def rcs(self) -> RcsResource:
        return RcsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingResourceWithStreamingResponse(self)


class AsyncMessagingResource(AsyncAPIResource):
    @cached_property
    def rcs(self) -> AsyncRcsResource:
        return AsyncRcsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingResourceWithStreamingResponse(self)


class MessagingResourceWithRawResponse:
    def __init__(self, messaging: MessagingResource) -> None:
        self._messaging = messaging

    @cached_property
    def rcs(self) -> RcsResourceWithRawResponse:
        return RcsResourceWithRawResponse(self._messaging.rcs)


class AsyncMessagingResourceWithRawResponse:
    def __init__(self, messaging: AsyncMessagingResource) -> None:
        self._messaging = messaging

    @cached_property
    def rcs(self) -> AsyncRcsResourceWithRawResponse:
        return AsyncRcsResourceWithRawResponse(self._messaging.rcs)


class MessagingResourceWithStreamingResponse:
    def __init__(self, messaging: MessagingResource) -> None:
        self._messaging = messaging

    @cached_property
    def rcs(self) -> RcsResourceWithStreamingResponse:
        return RcsResourceWithStreamingResponse(self._messaging.rcs)


class AsyncMessagingResourceWithStreamingResponse:
    def __init__(self, messaging: AsyncMessagingResource) -> None:
        self._messaging = messaging

    @cached_property
    def rcs(self) -> AsyncRcsResourceWithStreamingResponse:
        return AsyncRcsResourceWithStreamingResponse(self._messaging.rcs)
