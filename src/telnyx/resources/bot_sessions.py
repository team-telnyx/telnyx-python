# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import bot_session_list_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.bot_session_list_response import BotSessionListResponse

__all__ = ["BotSessionsResource", "AsyncBotSessionsResource"]


class BotSessionsResource(SyncAPIResource):
    """Agentic (bot) signup for Telnyx accounts.

    An AI agent solves a reverse-CAPTCHA challenge designed to be easy for LLMs and hard for humans, registers an account, and signs in by consuming a magic link emailed to the account owner. All endpoints are public and unauthenticated; signup endpoints are additionally gated by the freemium feature flags and per-country availability.
    """

    @cached_property
    def with_raw_response(self) -> BotSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BotSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BotSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BotSessionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        email: str,
        portal_redirect_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotSessionListResponse:
        """
        Consumes the one-time portal redirect (magic link) token emailed during bot
        signup and returns an API session. The token is a UUIDv7 that encodes its
        creation time; it expires after a configurable validity window (15 minutes by
        default) and is cleared on first use. Although the action creates a session, the
        route uses the GET verb because it is opened from an email link. On first use
        the account is also initialized. For bot signup (freemium) accounts the response
        is a minimal envelope containing only the `api_v2_token`; accounts that are
        permitted to use magic links but are not freemium accounts may instead receive
        an extended session payload when additional steps (such as two-factor
        authentication or identity verification) are required. This endpoint is public;
        the magic link token in the query string is the credential.

        Args:
          email: Email address associated with the magic link token.

          portal_redirect_token: Single-use portal redirect (magic link) token, a UUIDv7 sent to the account
              owner's email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/bot_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email": email,
                        "portal_redirect_token": portal_redirect_token,
                    },
                    bot_session_list_params.BotSessionListParams,
                ),
            ),
            cast_to=BotSessionListResponse,
        )


class AsyncBotSessionsResource(AsyncAPIResource):
    """Agentic (bot) signup for Telnyx accounts.

    An AI agent solves a reverse-CAPTCHA challenge designed to be easy for LLMs and hard for humans, registers an account, and signs in by consuming a magic link emailed to the account owner. All endpoints are public and unauthenticated; signup endpoints are additionally gated by the freemium feature flags and per-country availability.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBotSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBotSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBotSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBotSessionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        email: str,
        portal_redirect_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotSessionListResponse:
        """
        Consumes the one-time portal redirect (magic link) token emailed during bot
        signup and returns an API session. The token is a UUIDv7 that encodes its
        creation time; it expires after a configurable validity window (15 minutes by
        default) and is cleared on first use. Although the action creates a session, the
        route uses the GET verb because it is opened from an email link. On first use
        the account is also initialized. For bot signup (freemium) accounts the response
        is a minimal envelope containing only the `api_v2_token`; accounts that are
        permitted to use magic links but are not freemium accounts may instead receive
        an extended session payload when additional steps (such as two-factor
        authentication or identity verification) are required. This endpoint is public;
        the magic link token in the query string is the credential.

        Args:
          email: Email address associated with the magic link token.

          portal_redirect_token: Single-use portal redirect (magic link) token, a UUIDv7 sent to the account
              owner's email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/bot_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email": email,
                        "portal_redirect_token": portal_redirect_token,
                    },
                    bot_session_list_params.BotSessionListParams,
                ),
            ),
            cast_to=BotSessionListResponse,
        )


class BotSessionsResourceWithRawResponse:
    def __init__(self, bot_sessions: BotSessionsResource) -> None:
        self._bot_sessions = bot_sessions

        self.list = to_raw_response_wrapper(
            bot_sessions.list,
        )


class AsyncBotSessionsResourceWithRawResponse:
    def __init__(self, bot_sessions: AsyncBotSessionsResource) -> None:
        self._bot_sessions = bot_sessions

        self.list = async_to_raw_response_wrapper(
            bot_sessions.list,
        )


class BotSessionsResourceWithStreamingResponse:
    def __init__(self, bot_sessions: BotSessionsResource) -> None:
        self._bot_sessions = bot_sessions

        self.list = to_streamed_response_wrapper(
            bot_sessions.list,
        )


class AsyncBotSessionsResourceWithStreamingResponse:
    def __init__(self, bot_sessions: AsyncBotSessionsResource) -> None:
        self._bot_sessions = bot_sessions

        self.list = async_to_streamed_response_wrapper(
            bot_sessions.list,
        )
