# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import bot_signup_create_params, bot_signup_resend_magic_link_params
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
from ..types.success_response import SuccessResponse

__all__ = ["BotSignupResource", "AsyncBotSignupResource"]


class BotSignupResource(SyncAPIResource):
    """Agentic (bot) signup for Telnyx accounts.

    An AI agent solves a reverse-CAPTCHA challenge designed to be easy for LLMs and hard for humans, registers an account, and signs in by consuming a magic link emailed to the account owner. All endpoints are public and unauthenticated; signup endpoints are additionally gated by the freemium feature flags and per-country availability.
    """

    @cached_property
    def with_raw_response(self) -> BotSignupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BotSignupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BotSignupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BotSignupResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bot_challenge_answer: str,
        bot_challenge_nonce: str,
        privacy_policy_url: str,
        terms_and_conditions_url: str,
        terms_of_service: Literal[True],
        email: str | Omit = omit,
        terms_and_conditions_eu_url: str | Omit = omit,
        terms_of_service_eu: Literal[True] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """Creates a freemium Telnyx account through the agentic signup flow.

        The request
        must carry a valid answer to a previously issued bot challenge
        (`bot_challenge_nonce` and `bot_challenge_answer`), accept the terms of service,
        and echo the exact terms-and-conditions and privacy-policy URLs returned by the
        challenge endpoint. When EU consent enforcement is enabled,
        `terms_of_service_eu` and `terms_and_conditions_eu_url` are also required. On
        success a one-time sign-in (magic) link is emailed to the address provided; if
        the email address belongs to an existing account, a sign-in link is sent instead
        of creating a duplicate account. `email` may only be omitted when
        placeholder-email registration is enabled server-side. This endpoint is public
        and unauthenticated, gated by the freemium feature flags and per-country
        availability, and subject to per-IP and per-domain registration limits.

        Args:
          bot_challenge_answer: Answer to the issued bot challenge.

          bot_challenge_nonce: Nonce from a previously issued bot challenge.

          privacy_policy_url: Must exactly match the privacy-policy URL returned by the challenge endpoint.

          terms_and_conditions_url: Must exactly match the terms-and-conditions URL returned by the challenge
              endpoint.

          terms_of_service: Must be true to accept the terms of service.

          email: Email address for the new account. The magic link is sent here. May only be
              omitted when placeholder-email registration is enabled server-side.

          terms_and_conditions_eu_url: EU terms-and-conditions URL. Required when EU consent enforcement is enabled.

          terms_of_service_eu: EU terms-of-service acceptance. Required when EU consent enforcement is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/bot_signup",
            body=maybe_transform(
                {
                    "bot_challenge_answer": bot_challenge_answer,
                    "bot_challenge_nonce": bot_challenge_nonce,
                    "privacy_policy_url": privacy_policy_url,
                    "terms_and_conditions_url": terms_and_conditions_url,
                    "terms_of_service": terms_of_service,
                    "email": email,
                    "terms_and_conditions_eu_url": terms_and_conditions_eu_url,
                    "terms_of_service_eu": terms_of_service_eu,
                },
                bot_signup_create_params.BotSignupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    def resend_magic_link(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Resends the one-time sign-in (magic) link for an eligible bot signup account.
        Eligibility (account exists, was registered through bot signup, is active, and
        has not exceeded the resend limit or rate window) is evaluated server-side; the
        response is intentionally uniform and does not reveal whether the account exists
        or whether a link was actually sent. This endpoint is public and
        unauthenticated, gated by the freemium feature flags and per-country
        availability.

        Args:
          email: Email address of the bot signup account to resend the magic link to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/bot_signup/resend_magic_link",
            body=maybe_transform({"email": email}, bot_signup_resend_magic_link_params.BotSignupResendMagicLinkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )


class AsyncBotSignupResource(AsyncAPIResource):
    """Agentic (bot) signup for Telnyx accounts.

    An AI agent solves a reverse-CAPTCHA challenge designed to be easy for LLMs and hard for humans, registers an account, and signs in by consuming a magic link emailed to the account owner. All endpoints are public and unauthenticated; signup endpoints are additionally gated by the freemium feature flags and per-country availability.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBotSignupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBotSignupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBotSignupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBotSignupResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bot_challenge_answer: str,
        bot_challenge_nonce: str,
        privacy_policy_url: str,
        terms_and_conditions_url: str,
        terms_of_service: Literal[True],
        email: str | Omit = omit,
        terms_and_conditions_eu_url: str | Omit = omit,
        terms_of_service_eu: Literal[True] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """Creates a freemium Telnyx account through the agentic signup flow.

        The request
        must carry a valid answer to a previously issued bot challenge
        (`bot_challenge_nonce` and `bot_challenge_answer`), accept the terms of service,
        and echo the exact terms-and-conditions and privacy-policy URLs returned by the
        challenge endpoint. When EU consent enforcement is enabled,
        `terms_of_service_eu` and `terms_and_conditions_eu_url` are also required. On
        success a one-time sign-in (magic) link is emailed to the address provided; if
        the email address belongs to an existing account, a sign-in link is sent instead
        of creating a duplicate account. `email` may only be omitted when
        placeholder-email registration is enabled server-side. This endpoint is public
        and unauthenticated, gated by the freemium feature flags and per-country
        availability, and subject to per-IP and per-domain registration limits.

        Args:
          bot_challenge_answer: Answer to the issued bot challenge.

          bot_challenge_nonce: Nonce from a previously issued bot challenge.

          privacy_policy_url: Must exactly match the privacy-policy URL returned by the challenge endpoint.

          terms_and_conditions_url: Must exactly match the terms-and-conditions URL returned by the challenge
              endpoint.

          terms_of_service: Must be true to accept the terms of service.

          email: Email address for the new account. The magic link is sent here. May only be
              omitted when placeholder-email registration is enabled server-side.

          terms_and_conditions_eu_url: EU terms-and-conditions URL. Required when EU consent enforcement is enabled.

          terms_of_service_eu: EU terms-of-service acceptance. Required when EU consent enforcement is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/bot_signup",
            body=await async_maybe_transform(
                {
                    "bot_challenge_answer": bot_challenge_answer,
                    "bot_challenge_nonce": bot_challenge_nonce,
                    "privacy_policy_url": privacy_policy_url,
                    "terms_and_conditions_url": terms_and_conditions_url,
                    "terms_of_service": terms_of_service,
                    "email": email,
                    "terms_and_conditions_eu_url": terms_and_conditions_eu_url,
                    "terms_of_service_eu": terms_of_service_eu,
                },
                bot_signup_create_params.BotSignupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    async def resend_magic_link(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Resends the one-time sign-in (magic) link for an eligible bot signup account.
        Eligibility (account exists, was registered through bot signup, is active, and
        has not exceeded the resend limit or rate window) is evaluated server-side; the
        response is intentionally uniform and does not reveal whether the account exists
        or whether a link was actually sent. This endpoint is public and
        unauthenticated, gated by the freemium feature flags and per-country
        availability.

        Args:
          email: Email address of the bot signup account to resend the magic link to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/bot_signup/resend_magic_link",
            body=await async_maybe_transform(
                {"email": email}, bot_signup_resend_magic_link_params.BotSignupResendMagicLinkParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )


class BotSignupResourceWithRawResponse:
    def __init__(self, bot_signup: BotSignupResource) -> None:
        self._bot_signup = bot_signup

        self.create = to_raw_response_wrapper(
            bot_signup.create,
        )
        self.resend_magic_link = to_raw_response_wrapper(
            bot_signup.resend_magic_link,
        )


class AsyncBotSignupResourceWithRawResponse:
    def __init__(self, bot_signup: AsyncBotSignupResource) -> None:
        self._bot_signup = bot_signup

        self.create = async_to_raw_response_wrapper(
            bot_signup.create,
        )
        self.resend_magic_link = async_to_raw_response_wrapper(
            bot_signup.resend_magic_link,
        )


class BotSignupResourceWithStreamingResponse:
    def __init__(self, bot_signup: BotSignupResource) -> None:
        self._bot_signup = bot_signup

        self.create = to_streamed_response_wrapper(
            bot_signup.create,
        )
        self.resend_magic_link = to_streamed_response_wrapper(
            bot_signup.resend_magic_link,
        )


class AsyncBotSignupResourceWithStreamingResponse:
    def __init__(self, bot_signup: AsyncBotSignupResource) -> None:
        self._bot_signup = bot_signup

        self.create = async_to_streamed_response_wrapper(
            bot_signup.create,
        )
        self.resend_magic_link = async_to_streamed_response_wrapper(
            bot_signup.resend_magic_link,
        )
