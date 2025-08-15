# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import numbers_feature_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.numbers_feature_create_response import NumbersFeatureCreateResponse

__all__ = ["NumbersFeaturesResource", "AsyncNumbersFeaturesResource"]


class NumbersFeaturesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NumbersFeaturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NumbersFeaturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumbersFeaturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NumbersFeaturesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumbersFeatureCreateResponse:
        """
        Retrieve the features for a list of numbers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/numbers_features",
            body=maybe_transform(
                {"phone_numbers": phone_numbers}, numbers_feature_create_params.NumbersFeatureCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumbersFeatureCreateResponse,
        )


class AsyncNumbersFeaturesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNumbersFeaturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumbersFeaturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumbersFeaturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNumbersFeaturesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumbersFeatureCreateResponse:
        """
        Retrieve the features for a list of numbers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/numbers_features",
            body=await async_maybe_transform(
                {"phone_numbers": phone_numbers}, numbers_feature_create_params.NumbersFeatureCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumbersFeatureCreateResponse,
        )


class NumbersFeaturesResourceWithRawResponse:
    def __init__(self, numbers_features: NumbersFeaturesResource) -> None:
        self._numbers_features = numbers_features

        self.create = to_raw_response_wrapper(
            numbers_features.create,
        )


class AsyncNumbersFeaturesResourceWithRawResponse:
    def __init__(self, numbers_features: AsyncNumbersFeaturesResource) -> None:
        self._numbers_features = numbers_features

        self.create = async_to_raw_response_wrapper(
            numbers_features.create,
        )


class NumbersFeaturesResourceWithStreamingResponse:
    def __init__(self, numbers_features: NumbersFeaturesResource) -> None:
        self._numbers_features = numbers_features

        self.create = to_streamed_response_wrapper(
            numbers_features.create,
        )


class AsyncNumbersFeaturesResourceWithStreamingResponse:
    def __init__(self, numbers_features: AsyncNumbersFeaturesResource) -> None:
        self._numbers_features = numbers_features

        self.create = async_to_streamed_response_wrapper(
            numbers_features.create,
        )
