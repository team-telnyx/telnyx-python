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
        """SIM Cards operations"""
        return PurchaseResource(self._client)

    @cached_property
    def register(self) -> RegisterResource:
        """SIM Cards operations"""
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
        """SIM Cards operations"""
        return AsyncPurchaseResource(self._client)

    @cached_property
    def register(self) -> AsyncRegisterResource:
        """SIM Cards operations"""
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
        """SIM Cards operations"""
        return PurchaseResourceWithRawResponse(self._actions.purchase)

    @cached_property
    def register(self) -> RegisterResourceWithRawResponse:
        """SIM Cards operations"""
        return RegisterResourceWithRawResponse(self._actions.register)


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

    @cached_property
    def purchase(self) -> AsyncPurchaseResourceWithRawResponse:
        """SIM Cards operations"""
        return AsyncPurchaseResourceWithRawResponse(self._actions.purchase)

    @cached_property
    def register(self) -> AsyncRegisterResourceWithRawResponse:
        """SIM Cards operations"""
        return AsyncRegisterResourceWithRawResponse(self._actions.register)


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

    @cached_property
    def purchase(self) -> PurchaseResourceWithStreamingResponse:
        """SIM Cards operations"""
        return PurchaseResourceWithStreamingResponse(self._actions.purchase)

    @cached_property
    def register(self) -> RegisterResourceWithStreamingResponse:
        """SIM Cards operations"""
        return RegisterResourceWithStreamingResponse(self._actions.register)


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

    @cached_property
    def purchase(self) -> AsyncPurchaseResourceWithStreamingResponse:
        """SIM Cards operations"""
        return AsyncPurchaseResourceWithStreamingResponse(self._actions.purchase)

    @cached_property
    def register(self) -> AsyncRegisterResourceWithStreamingResponse:
        """SIM Cards operations"""
        return AsyncRegisterResourceWithStreamingResponse(self._actions.register)
