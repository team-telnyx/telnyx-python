# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.rooms.sessions import action_kick_params, action_mute_params, action_unmute_params
from ....types.rooms.sessions.action_end_response import ActionEndResponse
from ....types.rooms.sessions.action_kick_response import ActionKickResponse
from ....types.rooms.sessions.action_mute_response import ActionMuteResponse
from ....types.rooms.sessions.action_unmute_response import ActionUnmuteResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
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

    def end(
        self,
        room_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionEndResponse:
        """
        Note: this will also kick all participants currently present in the room

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return self._post(
            f"/room_sessions/{room_session_id}/actions/end",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEndResponse,
        )

    def kick(
        self,
        room_session_id: str,
        *,
        exclude: List[str] | NotGiven = NOT_GIVEN,
        participants: Union[Literal["all"], List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionKickResponse:
        """
        Kick participants from a room session.

        Args:
          exclude: List of participant id to exclude from the action.

          participants: Either a list of participant id to perform the action on, or the keyword "all"
              to perform the action on all participant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return self._post(
            f"/room_sessions/{room_session_id}/actions/kick",
            body=maybe_transform(
                {
                    "exclude": exclude,
                    "participants": participants,
                },
                action_kick_params.ActionKickParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionKickResponse,
        )

    def mute(
        self,
        room_session_id: str,
        *,
        exclude: List[str] | NotGiven = NOT_GIVEN,
        participants: Union[Literal["all"], List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionMuteResponse:
        """
        Mute participants in room session.

        Args:
          exclude: List of participant id to exclude from the action.

          participants: Either a list of participant id to perform the action on, or the keyword "all"
              to perform the action on all participant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return self._post(
            f"/room_sessions/{room_session_id}/actions/mute",
            body=maybe_transform(
                {
                    "exclude": exclude,
                    "participants": participants,
                },
                action_mute_params.ActionMuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionMuteResponse,
        )

    def unmute(
        self,
        room_session_id: str,
        *,
        exclude: List[str] | NotGiven = NOT_GIVEN,
        participants: Union[Literal["all"], List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionUnmuteResponse:
        """
        Unmute participants in room session.

        Args:
          exclude: List of participant id to exclude from the action.

          participants: Either a list of participant id to perform the action on, or the keyword "all"
              to perform the action on all participant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return self._post(
            f"/room_sessions/{room_session_id}/actions/unmute",
            body=maybe_transform(
                {
                    "exclude": exclude,
                    "participants": participants,
                },
                action_unmute_params.ActionUnmuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUnmuteResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
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

    async def end(
        self,
        room_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionEndResponse:
        """
        Note: this will also kick all participants currently present in the room

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return await self._post(
            f"/room_sessions/{room_session_id}/actions/end",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEndResponse,
        )

    async def kick(
        self,
        room_session_id: str,
        *,
        exclude: List[str] | NotGiven = NOT_GIVEN,
        participants: Union[Literal["all"], List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionKickResponse:
        """
        Kick participants from a room session.

        Args:
          exclude: List of participant id to exclude from the action.

          participants: Either a list of participant id to perform the action on, or the keyword "all"
              to perform the action on all participant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return await self._post(
            f"/room_sessions/{room_session_id}/actions/kick",
            body=await async_maybe_transform(
                {
                    "exclude": exclude,
                    "participants": participants,
                },
                action_kick_params.ActionKickParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionKickResponse,
        )

    async def mute(
        self,
        room_session_id: str,
        *,
        exclude: List[str] | NotGiven = NOT_GIVEN,
        participants: Union[Literal["all"], List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionMuteResponse:
        """
        Mute participants in room session.

        Args:
          exclude: List of participant id to exclude from the action.

          participants: Either a list of participant id to perform the action on, or the keyword "all"
              to perform the action on all participant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return await self._post(
            f"/room_sessions/{room_session_id}/actions/mute",
            body=await async_maybe_transform(
                {
                    "exclude": exclude,
                    "participants": participants,
                },
                action_mute_params.ActionMuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionMuteResponse,
        )

    async def unmute(
        self,
        room_session_id: str,
        *,
        exclude: List[str] | NotGiven = NOT_GIVEN,
        participants: Union[Literal["all"], List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionUnmuteResponse:
        """
        Unmute participants in room session.

        Args:
          exclude: List of participant id to exclude from the action.

          participants: Either a list of participant id to perform the action on, or the keyword "all"
              to perform the action on all participant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return await self._post(
            f"/room_sessions/{room_session_id}/actions/unmute",
            body=await async_maybe_transform(
                {
                    "exclude": exclude,
                    "participants": participants,
                },
                action_unmute_params.ActionUnmuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUnmuteResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.end = to_raw_response_wrapper(
            actions.end,
        )
        self.kick = to_raw_response_wrapper(
            actions.kick,
        )
        self.mute = to_raw_response_wrapper(
            actions.mute,
        )
        self.unmute = to_raw_response_wrapper(
            actions.unmute,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.end = async_to_raw_response_wrapper(
            actions.end,
        )
        self.kick = async_to_raw_response_wrapper(
            actions.kick,
        )
        self.mute = async_to_raw_response_wrapper(
            actions.mute,
        )
        self.unmute = async_to_raw_response_wrapper(
            actions.unmute,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.end = to_streamed_response_wrapper(
            actions.end,
        )
        self.kick = to_streamed_response_wrapper(
            actions.kick,
        )
        self.mute = to_streamed_response_wrapper(
            actions.mute,
        )
        self.unmute = to_streamed_response_wrapper(
            actions.unmute,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.end = async_to_streamed_response_wrapper(
            actions.end,
        )
        self.kick = async_to_streamed_response_wrapper(
            actions.kick,
        )
        self.mute = async_to_streamed_response_wrapper(
            actions.mute,
        )
        self.unmute = async_to_streamed_response_wrapper(
            actions.unmute,
        )
