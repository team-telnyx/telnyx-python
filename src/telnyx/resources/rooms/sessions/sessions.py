# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
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
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ....types.rooms import (
    session_list_0_params,
    session_list_1_params,
    session_retrieve_params,
    session_retrieve_participants_params,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.room_session import RoomSession
from ....types.shared.room_participant import RoomParticipant
from ....types.rooms.session_retrieve_response import SessionRetrieveResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        room_session_id: str,
        *,
        include_participants: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveResponse:
        """
        View a room session.

        Args:
          include_participants: To decide if room participants should be included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return self._get(
            f"/room_sessions/{room_session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_participants": include_participants}, session_retrieve_params.SessionRetrieveParams
                ),
            ),
            cast_to=SessionRetrieveResponse,
        )

    def list_0(
        self,
        *,
        filter: session_list_0_params.Filter | Omit = omit,
        include_participants: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[RoomSession]:
        """
        View a list of room sessions.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_created_at][eq], filter[date_created_at][gte],
              filter[date_created_at][lte], filter[date_updated_at][eq],
              filter[date_updated_at][gte], filter[date_updated_at][lte],
              filter[date_ended_at][eq], filter[date_ended_at][gte],
              filter[date_ended_at][lte], filter[room_id], filter[active]

          include_participants: To decide if room participants should be included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/room_sessions",
            page=SyncDefaultFlatPagination[RoomSession],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_participants": include_participants,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    session_list_0_params.SessionList0Params,
                ),
            ),
            model=RoomSession,
        )

    def list_1(
        self,
        room_id: str,
        *,
        filter: session_list_1_params.Filter | Omit = omit,
        include_participants: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[RoomSession]:
        """
        View a list of room sessions.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_created_at][eq], filter[date_created_at][gte],
              filter[date_created_at][lte], filter[date_updated_at][eq],
              filter[date_updated_at][gte], filter[date_updated_at][lte],
              filter[date_ended_at][eq], filter[date_ended_at][gte],
              filter[date_ended_at][lte], filter[active]

          include_participants: To decide if room participants should be included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return self._get_api_list(
            f"/rooms/{room_id}/sessions",
            page=SyncDefaultFlatPagination[RoomSession],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_participants": include_participants,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    session_list_1_params.SessionList1Params,
                ),
            ),
            model=RoomSession,
        )

    def retrieve_participants(
        self,
        room_session_id: str,
        *,
        filter: session_retrieve_participants_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[RoomParticipant]:
        """
        View a list of room participants.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_joined_at][eq], filter[date_joined_at][gte],
              filter[date_joined_at][lte], filter[date_updated_at][eq],
              filter[date_updated_at][gte], filter[date_updated_at][lte],
              filter[date_left_at][eq], filter[date_left_at][gte], filter[date_left_at][lte],
              filter[context]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return self._get_api_list(
            f"/room_sessions/{room_session_id}/participants",
            page=SyncDefaultFlatPagination[RoomParticipant],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    session_retrieve_participants_params.SessionRetrieveParticipantsParams,
                ),
            ),
            model=RoomParticipant,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        room_session_id: str,
        *,
        include_participants: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveResponse:
        """
        View a room session.

        Args:
          include_participants: To decide if room participants should be included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return await self._get(
            f"/room_sessions/{room_session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_participants": include_participants}, session_retrieve_params.SessionRetrieveParams
                ),
            ),
            cast_to=SessionRetrieveResponse,
        )

    def list_0(
        self,
        *,
        filter: session_list_0_params.Filter | Omit = omit,
        include_participants: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RoomSession, AsyncDefaultFlatPagination[RoomSession]]:
        """
        View a list of room sessions.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_created_at][eq], filter[date_created_at][gte],
              filter[date_created_at][lte], filter[date_updated_at][eq],
              filter[date_updated_at][gte], filter[date_updated_at][lte],
              filter[date_ended_at][eq], filter[date_ended_at][gte],
              filter[date_ended_at][lte], filter[room_id], filter[active]

          include_participants: To decide if room participants should be included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/room_sessions",
            page=AsyncDefaultFlatPagination[RoomSession],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_participants": include_participants,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    session_list_0_params.SessionList0Params,
                ),
            ),
            model=RoomSession,
        )

    def list_1(
        self,
        room_id: str,
        *,
        filter: session_list_1_params.Filter | Omit = omit,
        include_participants: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RoomSession, AsyncDefaultFlatPagination[RoomSession]]:
        """
        View a list of room sessions.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_created_at][eq], filter[date_created_at][gte],
              filter[date_created_at][lte], filter[date_updated_at][eq],
              filter[date_updated_at][gte], filter[date_updated_at][lte],
              filter[date_ended_at][eq], filter[date_ended_at][gte],
              filter[date_ended_at][lte], filter[active]

          include_participants: To decide if room participants should be included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return self._get_api_list(
            f"/rooms/{room_id}/sessions",
            page=AsyncDefaultFlatPagination[RoomSession],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_participants": include_participants,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    session_list_1_params.SessionList1Params,
                ),
            ),
            model=RoomSession,
        )

    def retrieve_participants(
        self,
        room_session_id: str,
        *,
        filter: session_retrieve_participants_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RoomParticipant, AsyncDefaultFlatPagination[RoomParticipant]]:
        """
        View a list of room participants.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_joined_at][eq], filter[date_joined_at][gte],
              filter[date_joined_at][lte], filter[date_updated_at][eq],
              filter[date_updated_at][gte], filter[date_updated_at][lte],
              filter[date_left_at][eq], filter[date_left_at][gte], filter[date_left_at][lte],
              filter[context]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return self._get_api_list(
            f"/room_sessions/{room_session_id}/participants",
            page=AsyncDefaultFlatPagination[RoomParticipant],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    session_retrieve_participants_params.SessionRetrieveParticipantsParams,
                ),
            ),
            model=RoomParticipant,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.retrieve = to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.list_0 = to_raw_response_wrapper(
            sessions.list_0,
        )
        self.list_1 = to_raw_response_wrapper(
            sessions.list_1,
        )
        self.retrieve_participants = to_raw_response_wrapper(
            sessions.retrieve_participants,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._sessions.actions)


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.retrieve = async_to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.list_0 = async_to_raw_response_wrapper(
            sessions.list_0,
        )
        self.list_1 = async_to_raw_response_wrapper(
            sessions.list_1,
        )
        self.retrieve_participants = async_to_raw_response_wrapper(
            sessions.retrieve_participants,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._sessions.actions)


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.retrieve = to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.list_0 = to_streamed_response_wrapper(
            sessions.list_0,
        )
        self.list_1 = to_streamed_response_wrapper(
            sessions.list_1,
        )
        self.retrieve_participants = to_streamed_response_wrapper(
            sessions.retrieve_participants,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._sessions.actions)


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.retrieve = async_to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.list_0 = async_to_streamed_response_wrapper(
            sessions.list_0,
        )
        self.list_1 = async_to_streamed_response_wrapper(
            sessions.list_1,
        )
        self.retrieve_participants = async_to_streamed_response_wrapper(
            sessions.retrieve_participants,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._sessions.actions)
