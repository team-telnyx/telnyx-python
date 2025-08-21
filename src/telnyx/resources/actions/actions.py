# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .purchase import (
    PurchaseResource,
    AsyncPurchaseResource,
    PurchaseResourceWithRawResponse,
    AsyncPurchaseResourceWithRawResponse,
    PurchaseResourceWithStreamingResponse,
    AsyncPurchaseResourceWithStreamingResponse,
)
from .register import (
    RegisterResource,
    AsyncRegisterResource,
    RegisterResourceWithRawResponse,
    AsyncRegisterResourceWithRawResponse,
    RegisterResourceWithStreamingResponse,
    AsyncRegisterResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def purchase(self) -> PurchaseResource:
        return PurchaseResource(self._client)

    @cached_property
    def register(self) -> RegisterResource:
        return RegisterResource(self._client)

    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def purchase(self) -> AsyncPurchaseResource:
        return AsyncPurchaseResource(self._client)

    @cached_property
    def register(self) -> AsyncRegisterResource:
        return AsyncRegisterResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

    @cached_property
    def purchase(self) -> PurchaseResourceWithRawResponse:
        return PurchaseResourceWithRawResponse(self._actions.purchase)

    @cached_property
    def register(self) -> RegisterResourceWithRawResponse:
        return RegisterResourceWithRawResponse(self._actions.register)


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

    @cached_property
    def purchase(self) -> AsyncPurchaseResourceWithRawResponse:
        return AsyncPurchaseResourceWithRawResponse(self._actions.purchase)

    @cached_property
    def register(self) -> AsyncRegisterResourceWithRawResponse:
        return AsyncRegisterResourceWithRawResponse(self._actions.register)


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

    @cached_property
    def purchase(self) -> PurchaseResourceWithStreamingResponse:
        return PurchaseResourceWithStreamingResponse(self._actions.purchase)

    @cached_property
    def register(self) -> RegisterResourceWithStreamingResponse:
        return RegisterResourceWithStreamingResponse(self._actions.register)


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

    @cached_property
    def purchase(self) -> AsyncPurchaseResourceWithStreamingResponse:
        return AsyncPurchaseResourceWithStreamingResponse(self._actions.purchase)

    @cached_property
    def register(self) -> AsyncRegisterResourceWithStreamingResponse:
        return AsyncRegisterResourceWithStreamingResponse(self._actions.register)
