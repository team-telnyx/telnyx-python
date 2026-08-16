# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.meeting_sessions import action_speak_params, action_send_chat_params
from ...types.meeting_sessions.action_accepted_response import ActionAcceptedResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    """Send real-time speech and chat actions to an active meeting session."""

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

    def send_chat(
        self,
        id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionAcceptedResponse:
        """
        Sends a chat message into a meeting session.

        Args:
          text: Chat message text to send in the meeting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/meeting_sessions/{id}/actions/send_chat", id=id),
            body=maybe_transform({"text": text}, action_send_chat_params.ActionSendChatParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAcceptedResponse,
        )

    def speak(
        self,
        id: str,
        *,
        text: str,
        interrupt: bool | Omit = omit,
        voice: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionAcceptedResponse:
        """
        Sends audio / text-to-speech into a meeting session.

        Args:
          text: Text for the bot to speak.

          interrupt: If true, interrupt any currently playing audio to speak this text immediately.

          voice: Voice identifier to use for this utterance. When supplied, it overrides the
              session-default voice configured at creation; otherwise the speak action uses
              that session default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/meeting_sessions/{id}/actions/speak", id=id),
            body=maybe_transform(
                {
                    "text": text,
                    "interrupt": interrupt,
                    "voice": voice,
                },
                action_speak_params.ActionSpeakParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAcceptedResponse,
        )

    def stop_speaking(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionAcceptedResponse:
        """
        Stops any active text-to-speech playback in a meeting session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/meeting_sessions/{id}/actions/stop_speaking", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAcceptedResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    """Send real-time speech and chat actions to an active meeting session."""

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

    async def send_chat(
        self,
        id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionAcceptedResponse:
        """
        Sends a chat message into a meeting session.

        Args:
          text: Chat message text to send in the meeting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/meeting_sessions/{id}/actions/send_chat", id=id),
            body=await async_maybe_transform({"text": text}, action_send_chat_params.ActionSendChatParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAcceptedResponse,
        )

    async def speak(
        self,
        id: str,
        *,
        text: str,
        interrupt: bool | Omit = omit,
        voice: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionAcceptedResponse:
        """
        Sends audio / text-to-speech into a meeting session.

        Args:
          text: Text for the bot to speak.

          interrupt: If true, interrupt any currently playing audio to speak this text immediately.

          voice: Voice identifier to use for this utterance. When supplied, it overrides the
              session-default voice configured at creation; otherwise the speak action uses
              that session default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/meeting_sessions/{id}/actions/speak", id=id),
            body=await async_maybe_transform(
                {
                    "text": text,
                    "interrupt": interrupt,
                    "voice": voice,
                },
                action_speak_params.ActionSpeakParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAcceptedResponse,
        )

    async def stop_speaking(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionAcceptedResponse:
        """
        Stops any active text-to-speech playback in a meeting session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/meeting_sessions/{id}/actions/stop_speaking", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAcceptedResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.send_chat = to_raw_response_wrapper(
            actions.send_chat,
        )
        self.speak = to_raw_response_wrapper(
            actions.speak,
        )
        self.stop_speaking = to_raw_response_wrapper(
            actions.stop_speaking,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.send_chat = async_to_raw_response_wrapper(
            actions.send_chat,
        )
        self.speak = async_to_raw_response_wrapper(
            actions.speak,
        )
        self.stop_speaking = async_to_raw_response_wrapper(
            actions.stop_speaking,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.send_chat = to_streamed_response_wrapper(
            actions.send_chat,
        )
        self.speak = to_streamed_response_wrapper(
            actions.speak,
        )
        self.stop_speaking = to_streamed_response_wrapper(
            actions.stop_speaking,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.send_chat = async_to_streamed_response_wrapper(
            actions.send_chat,
        )
        self.speak = async_to_streamed_response_wrapper(
            actions.speak,
        )
        self.stop_speaking = async_to_streamed_response_wrapper(
            actions.stop_speaking,
        )
