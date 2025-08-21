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
from ...types.rooms import action_refresh_client_token_params, action_generate_join_client_token_params
from ..._base_client import make_request_options
from ...types.rooms.action_refresh_client_token_response import ActionRefreshClientTokenResponse
from ...types.rooms.action_generate_join_client_token_response import ActionGenerateJoinClientTokenResponse

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

    def generate_join_client_token(
        self,
        room_id: str,
        *,
        refresh_token_ttl_secs: int | NotGiven = NOT_GIVEN,
        token_ttl_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionGenerateJoinClientTokenResponse:
        """Synchronously create an Client Token to join a Room.

        Client Token is necessary
        to join a Telnyx Room. Client Token will expire after `token_ttl_secs`, a
        Refresh Token is also provided to refresh a Client Token, the Refresh Token
        expires after `refresh_token_ttl_secs`.

        Args:
          refresh_token_ttl_secs: The time to live in seconds of the Refresh Token, after that time the Refresh
              Token is invalid and can't be used to refresh Client Token.

          token_ttl_secs: The time to live in seconds of the Client Token, after that time the Client
              Token is invalid and can't be used to join a Room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return self._post(
            f"/rooms/{room_id}/actions/generate_join_client_token",
            body=maybe_transform(
                {
                    "refresh_token_ttl_secs": refresh_token_ttl_secs,
                    "token_ttl_secs": token_ttl_secs,
                },
                action_generate_join_client_token_params.ActionGenerateJoinClientTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionGenerateJoinClientTokenResponse,
        )

    def refresh_client_token(
        self,
        room_id: str,
        *,
        refresh_token: str,
        token_ttl_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRefreshClientTokenResponse:
        """Synchronously refresh an Client Token to join a Room.

        Client Token is necessary
        to join a Telnyx Room. Client Token will expire after `token_ttl_secs`.

        Args:
          token_ttl_secs: The time to live in seconds of the Client Token, after that time the Client
              Token is invalid and can't be used to join a Room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return self._post(
            f"/rooms/{room_id}/actions/refresh_client_token",
            body=maybe_transform(
                {
                    "refresh_token": refresh_token,
                    "token_ttl_secs": token_ttl_secs,
                },
                action_refresh_client_token_params.ActionRefreshClientTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRefreshClientTokenResponse,
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

    async def generate_join_client_token(
        self,
        room_id: str,
        *,
        refresh_token_ttl_secs: int | NotGiven = NOT_GIVEN,
        token_ttl_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionGenerateJoinClientTokenResponse:
        """Synchronously create an Client Token to join a Room.

        Client Token is necessary
        to join a Telnyx Room. Client Token will expire after `token_ttl_secs`, a
        Refresh Token is also provided to refresh a Client Token, the Refresh Token
        expires after `refresh_token_ttl_secs`.

        Args:
          refresh_token_ttl_secs: The time to live in seconds of the Refresh Token, after that time the Refresh
              Token is invalid and can't be used to refresh Client Token.

          token_ttl_secs: The time to live in seconds of the Client Token, after that time the Client
              Token is invalid and can't be used to join a Room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return await self._post(
            f"/rooms/{room_id}/actions/generate_join_client_token",
            body=await async_maybe_transform(
                {
                    "refresh_token_ttl_secs": refresh_token_ttl_secs,
                    "token_ttl_secs": token_ttl_secs,
                },
                action_generate_join_client_token_params.ActionGenerateJoinClientTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionGenerateJoinClientTokenResponse,
        )

    async def refresh_client_token(
        self,
        room_id: str,
        *,
        refresh_token: str,
        token_ttl_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRefreshClientTokenResponse:
        """Synchronously refresh an Client Token to join a Room.

        Client Token is necessary
        to join a Telnyx Room. Client Token will expire after `token_ttl_secs`.

        Args:
          token_ttl_secs: The time to live in seconds of the Client Token, after that time the Client
              Token is invalid and can't be used to join a Room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return await self._post(
            f"/rooms/{room_id}/actions/refresh_client_token",
            body=await async_maybe_transform(
                {
                    "refresh_token": refresh_token,
                    "token_ttl_secs": token_ttl_secs,
                },
                action_refresh_client_token_params.ActionRefreshClientTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRefreshClientTokenResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.generate_join_client_token = to_raw_response_wrapper(
            actions.generate_join_client_token,
        )
        self.refresh_client_token = to_raw_response_wrapper(
            actions.refresh_client_token,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.generate_join_client_token = async_to_raw_response_wrapper(
            actions.generate_join_client_token,
        )
        self.refresh_client_token = async_to_raw_response_wrapper(
            actions.refresh_client_token,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.generate_join_client_token = to_streamed_response_wrapper(
            actions.generate_join_client_token,
        )
        self.refresh_client_token = to_streamed_response_wrapper(
            actions.refresh_client_token,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.generate_join_client_token = async_to_streamed_response_wrapper(
            actions.generate_join_client_token,
        )
        self.refresh_client_token = async_to_streamed_response_wrapper(
            actions.refresh_client_token,
        )
