# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import bot_challenge_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.bot_challenge_create_response import BotChallengeCreateResponse

__all__ = ["BotChallengeResource", "AsyncBotChallengeResource"]


class BotChallengeResource(SyncAPIResource):
    """Agentic (bot) signup for Telnyx accounts.

    An AI agent solves a reverse-CAPTCHA challenge designed to be easy for LLMs and hard for humans, registers an account, and signs in by consuming a magic link emailed to the account owner. All endpoints are public and unauthenticated; signup endpoints are additionally gated by the freemium feature flags and per-country availability.
    """

    @cached_property
    def with_raw_response(self) -> BotChallengeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BotChallengeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BotChallengeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BotChallengeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        llm_model_name: str | Omit = omit,
        llm_parameter_count: str | Omit = omit,
        llm_quantization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotChallengeCreateResponse:
        """Generates a reverse-CAPTCHA challenge used to gate the bot signup flow.

        A random
        active problem is selected from the pool; math problems are returned obfuscated
        (case randomization, symbol injection, spacing noise) with an unobfuscated
        rounding instruction appended, while string and binary problems are returned
        as-is. The response contains a single-use nonce, the problem text, and the
        current terms-and-conditions and privacy-policy URLs, which must be echoed back
        on the signup request. Challenges expire after a short window (10 minutes by
        default) and can only be answered once. This endpoint is public and
        unauthenticated.

        Args:
          llm_model_name: Name of the LLM the client is using.

          llm_parameter_count: Parameter count of the client LLM.

          llm_quantization: Quantization of the client LLM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/bot_challenge",
            body=maybe_transform(
                {
                    "llm_model_name": llm_model_name,
                    "llm_parameter_count": llm_parameter_count,
                    "llm_quantization": llm_quantization,
                },
                bot_challenge_create_params.BotChallengeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BotChallengeCreateResponse,
        )


class AsyncBotChallengeResource(AsyncAPIResource):
    """Agentic (bot) signup for Telnyx accounts.

    An AI agent solves a reverse-CAPTCHA challenge designed to be easy for LLMs and hard for humans, registers an account, and signs in by consuming a magic link emailed to the account owner. All endpoints are public and unauthenticated; signup endpoints are additionally gated by the freemium feature flags and per-country availability.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBotChallengeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBotChallengeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBotChallengeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBotChallengeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        llm_model_name: str | Omit = omit,
        llm_parameter_count: str | Omit = omit,
        llm_quantization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotChallengeCreateResponse:
        """Generates a reverse-CAPTCHA challenge used to gate the bot signup flow.

        A random
        active problem is selected from the pool; math problems are returned obfuscated
        (case randomization, symbol injection, spacing noise) with an unobfuscated
        rounding instruction appended, while string and binary problems are returned
        as-is. The response contains a single-use nonce, the problem text, and the
        current terms-and-conditions and privacy-policy URLs, which must be echoed back
        on the signup request. Challenges expire after a short window (10 minutes by
        default) and can only be answered once. This endpoint is public and
        unauthenticated.

        Args:
          llm_model_name: Name of the LLM the client is using.

          llm_parameter_count: Parameter count of the client LLM.

          llm_quantization: Quantization of the client LLM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/bot_challenge",
            body=await async_maybe_transform(
                {
                    "llm_model_name": llm_model_name,
                    "llm_parameter_count": llm_parameter_count,
                    "llm_quantization": llm_quantization,
                },
                bot_challenge_create_params.BotChallengeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BotChallengeCreateResponse,
        )


class BotChallengeResourceWithRawResponse:
    def __init__(self, bot_challenge: BotChallengeResource) -> None:
        self._bot_challenge = bot_challenge

        self.create = to_raw_response_wrapper(
            bot_challenge.create,
        )


class AsyncBotChallengeResourceWithRawResponse:
    def __init__(self, bot_challenge: AsyncBotChallengeResource) -> None:
        self._bot_challenge = bot_challenge

        self.create = async_to_raw_response_wrapper(
            bot_challenge.create,
        )


class BotChallengeResourceWithStreamingResponse:
    def __init__(self, bot_challenge: BotChallengeResource) -> None:
        self._bot_challenge = bot_challenge

        self.create = to_streamed_response_wrapper(
            bot_challenge.create,
        )


class AsyncBotChallengeResourceWithStreamingResponse:
    def __init__(self, bot_challenge: AsyncBotChallengeResource) -> None:
        self._bot_challenge = bot_challenge

        self.create = async_to_streamed_response_wrapper(
            bot_challenge.create,
        )
