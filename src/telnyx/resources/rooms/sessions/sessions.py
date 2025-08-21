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
from ....types.rooms import (
    session_list_0_params,
    session_list_1_params,
    session_retrieve_params,
    session_retrieve_participants_params,
)
from ...._base_client import make_request_options
from ....types.rooms.session_list_0_response import SessionList0Response
from ....types.rooms.session_list_1_response import SessionList1Response
from ....types.rooms.session_retrieve_response import SessionRetrieveResponse
from ....types.rooms.session_retrieve_participants_response import SessionRetrieveParticipantsResponse

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
        include_participants: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        filter: session_list_0_params.Filter | NotGiven = NOT_GIVEN,
        include_participants: bool | NotGiven = NOT_GIVEN,
        page: session_list_0_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionList0Response:
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

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/room_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_participants": include_participants,
                        "page": page,
                    },
                    session_list_0_params.SessionList0Params,
                ),
            ),
            cast_to=SessionList0Response,
        )

    def list_1(
        self,
        room_id: str,
        *,
        filter: session_list_1_params.Filter | NotGiven = NOT_GIVEN,
        include_participants: bool | NotGiven = NOT_GIVEN,
        page: session_list_1_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionList1Response:
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

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return self._get(
            f"/rooms/{room_id}/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_participants": include_participants,
                        "page": page,
                    },
                    session_list_1_params.SessionList1Params,
                ),
            ),
            cast_to=SessionList1Response,
        )

    def retrieve_participants(
        self,
        room_session_id: str,
        *,
        filter: session_retrieve_participants_params.Filter | NotGiven = NOT_GIVEN,
        page: session_retrieve_participants_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionRetrieveParticipantsResponse:
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

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return self._get(
            f"/room_sessions/{room_session_id}/participants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    session_retrieve_participants_params.SessionRetrieveParticipantsParams,
                ),
            ),
            cast_to=SessionRetrieveParticipantsResponse,
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
        include_participants: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def list_0(
        self,
        *,
        filter: session_list_0_params.Filter | NotGiven = NOT_GIVEN,
        include_participants: bool | NotGiven = NOT_GIVEN,
        page: session_list_0_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionList0Response:
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

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/room_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "include_participants": include_participants,
                        "page": page,
                    },
                    session_list_0_params.SessionList0Params,
                ),
            ),
            cast_to=SessionList0Response,
        )

    async def list_1(
        self,
        room_id: str,
        *,
        filter: session_list_1_params.Filter | NotGiven = NOT_GIVEN,
        include_participants: bool | NotGiven = NOT_GIVEN,
        page: session_list_1_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionList1Response:
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

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return await self._get(
            f"/rooms/{room_id}/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "include_participants": include_participants,
                        "page": page,
                    },
                    session_list_1_params.SessionList1Params,
                ),
            ),
            cast_to=SessionList1Response,
        )

    async def retrieve_participants(
        self,
        room_session_id: str,
        *,
        filter: session_retrieve_participants_params.Filter | NotGiven = NOT_GIVEN,
        page: session_retrieve_participants_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionRetrieveParticipantsResponse:
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

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_session_id:
            raise ValueError(f"Expected a non-empty value for `room_session_id` but received {room_session_id!r}")
        return await self._get(
            f"/room_sessions/{room_session_id}/participants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    session_retrieve_participants_params.SessionRetrieveParticipantsParams,
                ),
            ),
            cast_to=SessionRetrieveParticipantsResponse,
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
