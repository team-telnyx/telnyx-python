# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .funcs import (
    FuncsResource,
    AsyncFuncsResource,
    FuncsResourceWithRawResponse,
    AsyncFuncsResourceWithRawResponse,
    FuncsResourceWithStreamingResponse,
    AsyncFuncsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ComputeResource", "AsyncComputeResource"]


class ComputeResource(SyncAPIResource):
    @cached_property
    def funcs(self) -> FuncsResource:
        return FuncsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ComputeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ComputeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComputeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ComputeResourceWithStreamingResponse(self)


class AsyncComputeResource(AsyncAPIResource):
    @cached_property
    def funcs(self) -> AsyncFuncsResource:
        return AsyncFuncsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncComputeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncComputeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComputeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncComputeResourceWithStreamingResponse(self)


class ComputeResourceWithRawResponse:
    def __init__(self, compute: ComputeResource) -> None:
        self._compute = compute

    @cached_property
    def funcs(self) -> FuncsResourceWithRawResponse:
        return FuncsResourceWithRawResponse(self._compute.funcs)


class AsyncComputeResourceWithRawResponse:
    def __init__(self, compute: AsyncComputeResource) -> None:
        self._compute = compute

    @cached_property
    def funcs(self) -> AsyncFuncsResourceWithRawResponse:
        return AsyncFuncsResourceWithRawResponse(self._compute.funcs)


class ComputeResourceWithStreamingResponse:
    def __init__(self, compute: ComputeResource) -> None:
        self._compute = compute

    @cached_property
    def funcs(self) -> FuncsResourceWithStreamingResponse:
        return FuncsResourceWithStreamingResponse(self._compute.funcs)


class AsyncComputeResourceWithStreamingResponse:
    def __init__(self, compute: AsyncComputeResource) -> None:
        self._compute = compute

    @cached_property
    def funcs(self) -> AsyncFuncsResourceWithStreamingResponse:
        return AsyncFuncsResourceWithStreamingResponse(self._compute.funcs)
