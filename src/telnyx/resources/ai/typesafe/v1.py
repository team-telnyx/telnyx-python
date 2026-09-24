# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.typesafe import v1_systemone_params
from ....types.ai.typesafe.v1_systemone_response import V1SystemoneResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    """
    Beta API for evaluating shared context with typed questions and structured answers using Flash or Pro.
    """

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def systemone(
        self,
        *,
        questions: Dict[str, v1_systemone_params.Questions],
        state: Union[str, Dict[str, object], Iterable[object]],
        model: Literal["telnyx/decision-flash", "telnyx/decision-pro"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1SystemoneResponse:
        """
        **Beta API.** Choose telnyx/decision-flash for the lowest cost and latency, or
        telnyx/decision-pro for decisions that require long context, including inputs
        beyond Jev’s 32k per-decision limit. Omitted model defaults to
        telnyx/decision-flash.

        Evaluate shared context using named choice, noul (yes/no), and score questions.
        Returns TypeSafe System One-compatible answer shapes, the selected public model
        alias, and token usage. See the
        [decision model guide](https://developers.telnyx.com/docs/inference/decision-models)
        for examples and compatibility limits.

        The supported request subset requires instructions for every question, string
        descriptions for criteria (or null for choice descriptions), 1–64 questions, and
        2–64 options for choice and score questions. The model field accepts only
        telnyx/decision-flash or telnyx/decision-pro. Unsupported model values and
        unknown fields are rejected. The endpoint is synchronous and does not stream.

        Use the TypeSafe Python SDK with base_url set to
        https://api.telnyx.com/v2/ai/typesafe and a Telnyx API key. The SDK appends
        /v1/systemone; explicitly set model to a supported Telnyx alias because its own
        default model is not supported. Compatibility covers this operation and the
        documented request subset; it does not include TypeSafe model listing. Scores
        describe relative preference, not calibrated correctness.

        Args:
          questions: Between 1 and 64 named questions. Each key identifies the corresponding answer.

          state: Shared context evaluated by every question.

          model: Public model alias. telnyx/decision-flash offers the lowest cost and latency;
              telnyx/decision-pro supports decisions that require long context, including
              inputs beyond Jev’s 32k per-decision limit. Applies to every question in the
              request. Other values are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/typesafe/v1/systemone",
            body=maybe_transform(
                {
                    "questions": questions,
                    "state": state,
                    "model": model,
                },
                v1_systemone_params.V1SystemoneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1SystemoneResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    """
    Beta API for evaluating shared context with typed questions and structured answers using Flash or Pro.
    """

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def systemone(
        self,
        *,
        questions: Dict[str, v1_systemone_params.Questions],
        state: Union[str, Dict[str, object], Iterable[object]],
        model: Literal["telnyx/decision-flash", "telnyx/decision-pro"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1SystemoneResponse:
        """
        **Beta API.** Choose telnyx/decision-flash for the lowest cost and latency, or
        telnyx/decision-pro for decisions that require long context, including inputs
        beyond Jev’s 32k per-decision limit. Omitted model defaults to
        telnyx/decision-flash.

        Evaluate shared context using named choice, noul (yes/no), and score questions.
        Returns TypeSafe System One-compatible answer shapes, the selected public model
        alias, and token usage. See the
        [decision model guide](https://developers.telnyx.com/docs/inference/decision-models)
        for examples and compatibility limits.

        The supported request subset requires instructions for every question, string
        descriptions for criteria (or null for choice descriptions), 1–64 questions, and
        2–64 options for choice and score questions. The model field accepts only
        telnyx/decision-flash or telnyx/decision-pro. Unsupported model values and
        unknown fields are rejected. The endpoint is synchronous and does not stream.

        Use the TypeSafe Python SDK with base_url set to
        https://api.telnyx.com/v2/ai/typesafe and a Telnyx API key. The SDK appends
        /v1/systemone; explicitly set model to a supported Telnyx alias because its own
        default model is not supported. Compatibility covers this operation and the
        documented request subset; it does not include TypeSafe model listing. Scores
        describe relative preference, not calibrated correctness.

        Args:
          questions: Between 1 and 64 named questions. Each key identifies the corresponding answer.

          state: Shared context evaluated by every question.

          model: Public model alias. telnyx/decision-flash offers the lowest cost and latency;
              telnyx/decision-pro supports decisions that require long context, including
              inputs beyond Jev’s 32k per-decision limit. Applies to every question in the
              request. Other values are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/typesafe/v1/systemone",
            body=await async_maybe_transform(
                {
                    "questions": questions,
                    "state": state,
                    "model": model,
                },
                v1_systemone_params.V1SystemoneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1SystemoneResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.systemone = to_raw_response_wrapper(
            v1.systemone,
        )


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.systemone = async_to_raw_response_wrapper(
            v1.systemone,
        )


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.systemone = to_streamed_response_wrapper(
            v1.systemone,
        )


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.systemone = async_to_streamed_response_wrapper(
            v1.systemone,
        )
