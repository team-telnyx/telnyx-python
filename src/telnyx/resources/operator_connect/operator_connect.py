# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OperatorConnectResource", "AsyncOperatorConnectResource"]


class OperatorConnectResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        """External Connections operations"""
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OperatorConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return OperatorConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperatorConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return OperatorConnectResourceWithStreamingResponse(self)


class AsyncOperatorConnectResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        """External Connections operations"""
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOperatorConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOperatorConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperatorConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncOperatorConnectResourceWithStreamingResponse(self)


class OperatorConnectResourceWithRawResponse:
    def __init__(self, operator_connect: OperatorConnectResource) -> None:
        self._operator_connect = operator_connect

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """External Connections operations"""
        return ActionsResourceWithRawResponse(self._operator_connect.actions)


class AsyncOperatorConnectResourceWithRawResponse:
    def __init__(self, operator_connect: AsyncOperatorConnectResource) -> None:
        self._operator_connect = operator_connect

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """External Connections operations"""
        return AsyncActionsResourceWithRawResponse(self._operator_connect.actions)


class OperatorConnectResourceWithStreamingResponse:
    def __init__(self, operator_connect: OperatorConnectResource) -> None:
        self._operator_connect = operator_connect

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """External Connections operations"""
        return ActionsResourceWithStreamingResponse(self._operator_connect.actions)


class AsyncOperatorConnectResourceWithStreamingResponse:
    def __init__(self, operator_connect: AsyncOperatorConnectResource) -> None:
        self._operator_connect = operator_connect

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """External Connections operations"""
        return AsyncActionsResourceWithStreamingResponse(self._operator_connect.actions)
