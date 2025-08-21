# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import room_participant_list_params
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
from ..types.room_participant_list_response import RoomParticipantListResponse
from ..types.room_participant_retrieve_response import RoomParticipantRetrieveResponse

__all__ = ["RoomParticipantsResource", "AsyncRoomParticipantsResource"]


class RoomParticipantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoomParticipantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RoomParticipantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoomParticipantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RoomParticipantsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        room_participant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomParticipantRetrieveResponse:
        """
        View a room participant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_participant_id:
            raise ValueError(
                f"Expected a non-empty value for `room_participant_id` but received {room_participant_id!r}"
            )
        return self._get(
            f"/room_participants/{room_participant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomParticipantRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: room_participant_list_params.Filter | NotGiven = NOT_GIVEN,
        page: room_participant_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomParticipantListResponse:
        """
        View a list of room participants.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_joined_at][eq], filter[date_joined_at][gte],
              filter[date_joined_at][lte], filter[date_updated_at][eq],
              filter[date_updated_at][gte], filter[date_updated_at][lte],
              filter[date_left_at][eq], filter[date_left_at][gte], filter[date_left_at][lte],
              filter[context], filter[session_id]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/room_participants",
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
                    room_participant_list_params.RoomParticipantListParams,
                ),
            ),
            cast_to=RoomParticipantListResponse,
        )


class AsyncRoomParticipantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoomParticipantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoomParticipantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoomParticipantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRoomParticipantsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        room_participant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomParticipantRetrieveResponse:
        """
        View a room participant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_participant_id:
            raise ValueError(
                f"Expected a non-empty value for `room_participant_id` but received {room_participant_id!r}"
            )
        return await self._get(
            f"/room_participants/{room_participant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomParticipantRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: room_participant_list_params.Filter | NotGiven = NOT_GIVEN,
        page: room_participant_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomParticipantListResponse:
        """
        View a list of room participants.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_joined_at][eq], filter[date_joined_at][gte],
              filter[date_joined_at][lte], filter[date_updated_at][eq],
              filter[date_updated_at][gte], filter[date_updated_at][lte],
              filter[date_left_at][eq], filter[date_left_at][gte], filter[date_left_at][lte],
              filter[context], filter[session_id]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/room_participants",
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
                    room_participant_list_params.RoomParticipantListParams,
                ),
            ),
            cast_to=RoomParticipantListResponse,
        )


class RoomParticipantsResourceWithRawResponse:
    def __init__(self, room_participants: RoomParticipantsResource) -> None:
        self._room_participants = room_participants

        self.retrieve = to_raw_response_wrapper(
            room_participants.retrieve,
        )
        self.list = to_raw_response_wrapper(
            room_participants.list,
        )


class AsyncRoomParticipantsResourceWithRawResponse:
    def __init__(self, room_participants: AsyncRoomParticipantsResource) -> None:
        self._room_participants = room_participants

        self.retrieve = async_to_raw_response_wrapper(
            room_participants.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            room_participants.list,
        )


class RoomParticipantsResourceWithStreamingResponse:
    def __init__(self, room_participants: RoomParticipantsResource) -> None:
        self._room_participants = room_participants

        self.retrieve = to_streamed_response_wrapper(
            room_participants.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            room_participants.list,
        )


class AsyncRoomParticipantsResourceWithStreamingResponse:
    def __init__(self, room_participants: AsyncRoomParticipantsResource) -> None:
        self._room_participants = room_participants

        self.retrieve = async_to_streamed_response_wrapper(
            room_participants.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            room_participants.list,
        )
