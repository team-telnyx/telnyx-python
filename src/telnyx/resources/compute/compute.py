# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .funcs.funcs import (
    FuncsResource,
    AsyncFuncsResource,
    FuncsResourceWithRawResponse,
    AsyncFuncsResourceWithRawResponse,
    FuncsResourceWithStreamingResponse,
    AsyncFuncsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.compute_retrieve_response import ComputeRetrieveResponse

__all__ = ["ComputeResource", "AsyncComputeResource"]


class ComputeResource(SyncAPIResource):
    """Inspect Stateful Actor types"""

    @cached_property
    def funcs(self) -> FuncsResource:
        """Manage Edge Compute functions"""
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

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComputeRetrieveResponse:
        """Retrieve one account-scoped Stateful Actor type.

        owner_function_id identifies
        the function that owns and ships the actor class; other functions may reference
        the same actor type through actor bindings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/compute/actors/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComputeRetrieveResponse,
        )


class AsyncComputeResource(AsyncAPIResource):
    """Inspect Stateful Actor types"""

    @cached_property
    def funcs(self) -> AsyncFuncsResource:
        """Manage Edge Compute functions"""
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

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComputeRetrieveResponse:
        """Retrieve one account-scoped Stateful Actor type.

        owner_function_id identifies
        the function that owns and ships the actor class; other functions may reference
        the same actor type through actor bindings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/compute/actors/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComputeRetrieveResponse,
        )


class ComputeResourceWithRawResponse:
    def __init__(self, compute: ComputeResource) -> None:
        self._compute = compute

        self.retrieve = to_raw_response_wrapper(
            compute.retrieve,
        )

    @cached_property
    def funcs(self) -> FuncsResourceWithRawResponse:
        """Manage Edge Compute functions"""
        return FuncsResourceWithRawResponse(self._compute.funcs)


class AsyncComputeResourceWithRawResponse:
    def __init__(self, compute: AsyncComputeResource) -> None:
        self._compute = compute

        self.retrieve = async_to_raw_response_wrapper(
            compute.retrieve,
        )

    @cached_property
    def funcs(self) -> AsyncFuncsResourceWithRawResponse:
        """Manage Edge Compute functions"""
        return AsyncFuncsResourceWithRawResponse(self._compute.funcs)


class ComputeResourceWithStreamingResponse:
    def __init__(self, compute: ComputeResource) -> None:
        self._compute = compute

        self.retrieve = to_streamed_response_wrapper(
            compute.retrieve,
        )

    @cached_property
    def funcs(self) -> FuncsResourceWithStreamingResponse:
        """Manage Edge Compute functions"""
        return FuncsResourceWithStreamingResponse(self._compute.funcs)


class AsyncComputeResourceWithStreamingResponse:
    def __init__(self, compute: AsyncComputeResource) -> None:
        self._compute = compute

        self.retrieve = async_to_streamed_response_wrapper(
            compute.retrieve,
        )

    @cached_property
    def funcs(self) -> AsyncFuncsResourceWithStreamingResponse:
        """Manage Edge Compute functions"""
        return AsyncFuncsResourceWithStreamingResponse(self._compute.funcs)
