# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import room_recording_list_params, room_recording_delete_bulk_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.room_recording_list_response import RoomRecordingListResponse
from ..types.room_recording_retrieve_response import RoomRecordingRetrieveResponse
from ..types.room_recording_delete_bulk_response import RoomRecordingDeleteBulkResponse

__all__ = ["RoomRecordingsResource", "AsyncRoomRecordingsResource"]


class RoomRecordingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoomRecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RoomRecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoomRecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RoomRecordingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        room_recording_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomRecordingRetrieveResponse:
        """
        View a room recording.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_recording_id:
            raise ValueError(f"Expected a non-empty value for `room_recording_id` but received {room_recording_id!r}")
        return self._get(
            f"/room_recordings/{room_recording_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomRecordingRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: room_recording_list_params.Filter | NotGiven = NOT_GIVEN,
        page: room_recording_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomRecordingListResponse:
        """
        View a list of room recordings.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_ended_at][eq], filter[date_ended_at][gte],
              filter[date_ended_at][lte], filter[date_started_at][eq],
              filter[date_started_at][gte], filter[date_started_at][lte], filter[room_id],
              filter[participant_id], filter[session_id], filter[status], filter[type],
              filter[duration_secs]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/room_recordings",
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
                    room_recording_list_params.RoomRecordingListParams,
                ),
            ),
            cast_to=RoomRecordingListResponse,
        )

    def delete(
        self,
        room_recording_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Synchronously delete a Room Recording.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_recording_id:
            raise ValueError(f"Expected a non-empty value for `room_recording_id` but received {room_recording_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/room_recordings/{room_recording_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_bulk(
        self,
        *,
        filter: room_recording_delete_bulk_params.Filter | NotGiven = NOT_GIVEN,
        page: room_recording_delete_bulk_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomRecordingDeleteBulkResponse:
        """
        Delete several room recordings in a bulk.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_ended_at][eq], filter[date_ended_at][gte],
              filter[date_ended_at][lte], filter[date_started_at][eq],
              filter[date_started_at][gte], filter[date_started_at][lte], filter[room_id],
              filter[participant_id], filter[session_id], filter[status], filter[type],
              filter[duration_secs]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/room_recordings",
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
                    room_recording_delete_bulk_params.RoomRecordingDeleteBulkParams,
                ),
            ),
            cast_to=RoomRecordingDeleteBulkResponse,
        )


class AsyncRoomRecordingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoomRecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoomRecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoomRecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRoomRecordingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        room_recording_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomRecordingRetrieveResponse:
        """
        View a room recording.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_recording_id:
            raise ValueError(f"Expected a non-empty value for `room_recording_id` but received {room_recording_id!r}")
        return await self._get(
            f"/room_recordings/{room_recording_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomRecordingRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: room_recording_list_params.Filter | NotGiven = NOT_GIVEN,
        page: room_recording_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomRecordingListResponse:
        """
        View a list of room recordings.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_ended_at][eq], filter[date_ended_at][gte],
              filter[date_ended_at][lte], filter[date_started_at][eq],
              filter[date_started_at][gte], filter[date_started_at][lte], filter[room_id],
              filter[participant_id], filter[session_id], filter[status], filter[type],
              filter[duration_secs]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/room_recordings",
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
                    room_recording_list_params.RoomRecordingListParams,
                ),
            ),
            cast_to=RoomRecordingListResponse,
        )

    async def delete(
        self,
        room_recording_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Synchronously delete a Room Recording.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_recording_id:
            raise ValueError(f"Expected a non-empty value for `room_recording_id` but received {room_recording_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/room_recordings/{room_recording_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_bulk(
        self,
        *,
        filter: room_recording_delete_bulk_params.Filter | NotGiven = NOT_GIVEN,
        page: room_recording_delete_bulk_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomRecordingDeleteBulkResponse:
        """
        Delete several room recordings in a bulk.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_ended_at][eq], filter[date_ended_at][gte],
              filter[date_ended_at][lte], filter[date_started_at][eq],
              filter[date_started_at][gte], filter[date_started_at][lte], filter[room_id],
              filter[participant_id], filter[session_id], filter[status], filter[type],
              filter[duration_secs]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/room_recordings",
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
                    room_recording_delete_bulk_params.RoomRecordingDeleteBulkParams,
                ),
            ),
            cast_to=RoomRecordingDeleteBulkResponse,
        )


class RoomRecordingsResourceWithRawResponse:
    def __init__(self, room_recordings: RoomRecordingsResource) -> None:
        self._room_recordings = room_recordings

        self.retrieve = to_raw_response_wrapper(
            room_recordings.retrieve,
        )
        self.list = to_raw_response_wrapper(
            room_recordings.list,
        )
        self.delete = to_raw_response_wrapper(
            room_recordings.delete,
        )
        self.delete_bulk = to_raw_response_wrapper(
            room_recordings.delete_bulk,
        )


class AsyncRoomRecordingsResourceWithRawResponse:
    def __init__(self, room_recordings: AsyncRoomRecordingsResource) -> None:
        self._room_recordings = room_recordings

        self.retrieve = async_to_raw_response_wrapper(
            room_recordings.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            room_recordings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            room_recordings.delete,
        )
        self.delete_bulk = async_to_raw_response_wrapper(
            room_recordings.delete_bulk,
        )


class RoomRecordingsResourceWithStreamingResponse:
    def __init__(self, room_recordings: RoomRecordingsResource) -> None:
        self._room_recordings = room_recordings

        self.retrieve = to_streamed_response_wrapper(
            room_recordings.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            room_recordings.list,
        )
        self.delete = to_streamed_response_wrapper(
            room_recordings.delete,
        )
        self.delete_bulk = to_streamed_response_wrapper(
            room_recordings.delete_bulk,
        )


class AsyncRoomRecordingsResourceWithStreamingResponse:
    def __init__(self, room_recordings: AsyncRoomRecordingsResource) -> None:
        self._room_recordings = room_recordings

        self.retrieve = async_to_streamed_response_wrapper(
            room_recordings.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            room_recordings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            room_recordings.delete,
        )
        self.delete_bulk = async_to_streamed_response_wrapper(
            room_recordings.delete_bulk,
        )
