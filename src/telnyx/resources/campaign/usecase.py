# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.campaign import usecase_get_cost_params
from ...types.campaign.usecase_get_cost_response import UsecaseGetCostResponse

__all__ = ["UsecaseResource", "AsyncUsecaseResource"]


class UsecaseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsecaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UsecaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsecaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return UsecaseResourceWithStreamingResponse(self)

    def get_cost(
        self,
        *,
        usecase: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseGetCostResponse:
        """
        Get Campaign Cost

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/campaign/usecase/cost",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"usecase": usecase}, usecase_get_cost_params.UsecaseGetCostParams),
            ),
            cast_to=UsecaseGetCostResponse,
        )


class AsyncUsecaseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsecaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsecaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsecaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncUsecaseResourceWithStreamingResponse(self)

    async def get_cost(
        self,
        *,
        usecase: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseGetCostResponse:
        """
        Get Campaign Cost

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/campaign/usecase/cost",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"usecase": usecase}, usecase_get_cost_params.UsecaseGetCostParams),
            ),
            cast_to=UsecaseGetCostResponse,
        )


class UsecaseResourceWithRawResponse:
    def __init__(self, usecase: UsecaseResource) -> None:
        self._usecase = usecase

        self.get_cost = to_raw_response_wrapper(
            usecase.get_cost,
        )


class AsyncUsecaseResourceWithRawResponse:
    def __init__(self, usecase: AsyncUsecaseResource) -> None:
        self._usecase = usecase

        self.get_cost = async_to_raw_response_wrapper(
            usecase.get_cost,
        )


class UsecaseResourceWithStreamingResponse:
    def __init__(self, usecase: UsecaseResource) -> None:
        self._usecase = usecase

        self.get_cost = to_streamed_response_wrapper(
            usecase.get_cost,
        )


class AsyncUsecaseResourceWithStreamingResponse:
    def __init__(self, usecase: AsyncUsecaseResource) -> None:
        self._usecase = usecase

        self.get_cost = async_to_streamed_response_wrapper(
            usecase.get_cost,
        )
