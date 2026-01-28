# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import room_list_params, room_create_params, room_update_params, room_retrieve_params
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...types.room import Room
from ..._base_client import AsyncPaginator, make_request_options
from .sessions.sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ...types.room_create_response import RoomCreateResponse
from ...types.room_update_response import RoomUpdateResponse
from ...types.room_retrieve_response import RoomRetrieveResponse

__all__ = ["RoomsResource", "AsyncRoomsResource"]


class RoomsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RoomsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RoomsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoomsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RoomsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        enable_recording: bool | Omit = omit,
        max_participants: int | Omit = omit,
        unique_name: str | Omit = omit,
        webhook_event_failover_url: str | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomCreateResponse:
        """
        Synchronously create a Room.

        Args:
          enable_recording: Enable or disable recording for that room.

          max_participants: The maximum amount of participants allowed in a room. If new participants try to
              join after that limit is reached, their request will be rejected.

          unique_name: The unique (within the Telnyx account scope) name of the room.

          webhook_event_failover_url: The failover URL where webhooks related to this room will be sent if sending to
              the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this room will be sent. Must include a scheme,
              such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/rooms",
            body=maybe_transform(
                {
                    "enable_recording": enable_recording,
                    "max_participants": max_participants,
                    "unique_name": unique_name,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                room_create_params.RoomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomCreateResponse,
        )

    def retrieve(
        self,
        room_id: str,
        *,
        include_sessions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomRetrieveResponse:
        """
        View a room.

        Args:
          include_sessions: To decide if room sessions should be included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return self._get(
            f"/rooms/{room_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_sessions": include_sessions}, room_retrieve_params.RoomRetrieveParams),
            ),
            cast_to=RoomRetrieveResponse,
        )

    def update(
        self,
        room_id: str,
        *,
        enable_recording: bool | Omit = omit,
        max_participants: int | Omit = omit,
        unique_name: str | Omit = omit,
        webhook_event_failover_url: str | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomUpdateResponse:
        """
        Synchronously update a Room.

        Args:
          enable_recording: Enable or disable recording for that room.

          max_participants: The maximum amount of participants allowed in a room. If new participants try to
              join after that limit is reached, their request will be rejected.

          unique_name: The unique (within the Telnyx account scope) name of the room.

          webhook_event_failover_url: The failover URL where webhooks related to this room will be sent if sending to
              the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this room will be sent. Must include a scheme,
              such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return self._patch(
            f"/rooms/{room_id}",
            body=maybe_transform(
                {
                    "enable_recording": enable_recording,
                    "max_participants": max_participants,
                    "unique_name": unique_name,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                room_update_params.RoomUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomUpdateResponse,
        )

    def list(
        self,
        *,
        filter: room_list_params.Filter | Omit = omit,
        include_sessions: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[Room]:
        """
        View a list of rooms.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_created_at][eq], filter[date_created_at][gte],
              filter[date_created_at][lte], filter[date_updated_at][eq],
              filter[date_updated_at][gte], filter[date_updated_at][lte], filter[unique_name]

          include_sessions: To decide if room sessions should be included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/rooms",
            page=SyncDefaultFlatPagination[Room],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_sessions": include_sessions,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    room_list_params.RoomListParams,
                ),
            ),
            model=Room,
        )

    def delete(
        self,
        room_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Synchronously delete a Room.

        Participants from that room will be kicked out,
        they won't be able to join that room anymore, and you won't be charged anymore
        for that room.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/rooms/{room_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRoomsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRoomsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoomsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoomsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRoomsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        enable_recording: bool | Omit = omit,
        max_participants: int | Omit = omit,
        unique_name: str | Omit = omit,
        webhook_event_failover_url: str | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomCreateResponse:
        """
        Synchronously create a Room.

        Args:
          enable_recording: Enable or disable recording for that room.

          max_participants: The maximum amount of participants allowed in a room. If new participants try to
              join after that limit is reached, their request will be rejected.

          unique_name: The unique (within the Telnyx account scope) name of the room.

          webhook_event_failover_url: The failover URL where webhooks related to this room will be sent if sending to
              the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this room will be sent. Must include a scheme,
              such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/rooms",
            body=await async_maybe_transform(
                {
                    "enable_recording": enable_recording,
                    "max_participants": max_participants,
                    "unique_name": unique_name,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                room_create_params.RoomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomCreateResponse,
        )

    async def retrieve(
        self,
        room_id: str,
        *,
        include_sessions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomRetrieveResponse:
        """
        View a room.

        Args:
          include_sessions: To decide if room sessions should be included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return await self._get(
            f"/rooms/{room_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_sessions": include_sessions}, room_retrieve_params.RoomRetrieveParams
                ),
            ),
            cast_to=RoomRetrieveResponse,
        )

    async def update(
        self,
        room_id: str,
        *,
        enable_recording: bool | Omit = omit,
        max_participants: int | Omit = omit,
        unique_name: str | Omit = omit,
        webhook_event_failover_url: str | Omit = omit,
        webhook_event_url: str | Omit = omit,
        webhook_timeout_secs: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomUpdateResponse:
        """
        Synchronously update a Room.

        Args:
          enable_recording: Enable or disable recording for that room.

          max_participants: The maximum amount of participants allowed in a room. If new participants try to
              join after that limit is reached, their request will be rejected.

          unique_name: The unique (within the Telnyx account scope) name of the room.

          webhook_event_failover_url: The failover URL where webhooks related to this room will be sent if sending to
              the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this room will be sent. Must include a scheme,
              such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return await self._patch(
            f"/rooms/{room_id}",
            body=await async_maybe_transform(
                {
                    "enable_recording": enable_recording,
                    "max_participants": max_participants,
                    "unique_name": unique_name,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                room_update_params.RoomUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomUpdateResponse,
        )

    def list(
        self,
        *,
        filter: room_list_params.Filter | Omit = omit,
        include_sessions: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Room, AsyncDefaultFlatPagination[Room]]:
        """
        View a list of rooms.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_created_at][eq], filter[date_created_at][gte],
              filter[date_created_at][lte], filter[date_updated_at][eq],
              filter[date_updated_at][gte], filter[date_updated_at][lte], filter[unique_name]

          include_sessions: To decide if room sessions should be included in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/rooms",
            page=AsyncDefaultFlatPagination[Room],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_sessions": include_sessions,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    room_list_params.RoomListParams,
                ),
            ),
            model=Room,
        )

    async def delete(
        self,
        room_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Synchronously delete a Room.

        Participants from that room will be kicked out,
        they won't be able to join that room anymore, and you won't be charged anymore
        for that room.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/rooms/{room_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RoomsResourceWithRawResponse:
    def __init__(self, rooms: RoomsResource) -> None:
        self._rooms = rooms

        self.create = to_raw_response_wrapper(
            rooms.create,
        )
        self.retrieve = to_raw_response_wrapper(
            rooms.retrieve,
        )
        self.update = to_raw_response_wrapper(
            rooms.update,
        )
        self.list = to_raw_response_wrapper(
            rooms.list,
        )
        self.delete = to_raw_response_wrapper(
            rooms.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._rooms.actions)

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._rooms.sessions)


class AsyncRoomsResourceWithRawResponse:
    def __init__(self, rooms: AsyncRoomsResource) -> None:
        self._rooms = rooms

        self.create = async_to_raw_response_wrapper(
            rooms.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            rooms.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            rooms.update,
        )
        self.list = async_to_raw_response_wrapper(
            rooms.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rooms.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._rooms.actions)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._rooms.sessions)


class RoomsResourceWithStreamingResponse:
    def __init__(self, rooms: RoomsResource) -> None:
        self._rooms = rooms

        self.create = to_streamed_response_wrapper(
            rooms.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            rooms.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            rooms.update,
        )
        self.list = to_streamed_response_wrapper(
            rooms.list,
        )
        self.delete = to_streamed_response_wrapper(
            rooms.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._rooms.actions)

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._rooms.sessions)


class AsyncRoomsResourceWithStreamingResponse:
    def __init__(self, rooms: AsyncRoomsResource) -> None:
        self._rooms = rooms

        self.create = async_to_streamed_response_wrapper(
            rooms.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            rooms.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            rooms.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rooms.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rooms.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._rooms.actions)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._rooms.sessions)
