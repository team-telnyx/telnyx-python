# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import room_composition_list_params, room_composition_create_params
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
from ..types.video_region_param import VideoRegionParam
from ..types.room_composition_list_response import RoomCompositionListResponse
from ..types.room_composition_create_response import RoomCompositionCreateResponse
from ..types.room_composition_retrieve_response import RoomCompositionRetrieveResponse

__all__ = ["RoomCompositionsResource", "AsyncRoomCompositionsResource"]


class RoomCompositionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoomCompositionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RoomCompositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoomCompositionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RoomCompositionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        format: Optional[str] | NotGiven = NOT_GIVEN,
        resolution: Optional[str] | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        video_layout: Dict[str, VideoRegionParam] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_event_url: str | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomCompositionCreateResponse:
        """
        Asynchronously create a room composition.

        Args:
          format: The desired format of the room composition.

          resolution: The desired resolution (width/height in pixels) of the resulting video of the
              room composition. Both width and height are required to be between 16 and 1280;
              and width _ height should not exceed 1280 _ 720

          session_id: id of the room session associated with the room composition.

          video_layout: Describes the video layout of the room composition in terms of regions.

          webhook_event_failover_url: The failover URL where webhooks related to this room composition will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this room composition will be sent. Must
              include a scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/room_compositions",
            body=maybe_transform(
                {
                    "format": format,
                    "resolution": resolution,
                    "session_id": session_id,
                    "video_layout": video_layout,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                room_composition_create_params.RoomCompositionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomCompositionCreateResponse,
        )

    def retrieve(
        self,
        room_composition_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomCompositionRetrieveResponse:
        """
        View a room composition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_composition_id:
            raise ValueError(
                f"Expected a non-empty value for `room_composition_id` but received {room_composition_id!r}"
            )
        return self._get(
            f"/room_compositions/{room_composition_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomCompositionRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: room_composition_list_params.Filter | NotGiven = NOT_GIVEN,
        page: room_composition_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomCompositionListResponse:
        """
        View a list of room compositions.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_created_at][eq], filter[date_created_at][gte],
              filter[date_created_at][lte], filter[session_id], filter[status]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/room_compositions",
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
                    room_composition_list_params.RoomCompositionListParams,
                ),
            ),
            cast_to=RoomCompositionListResponse,
        )

    def delete(
        self,
        room_composition_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Synchronously delete a room composition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_composition_id:
            raise ValueError(
                f"Expected a non-empty value for `room_composition_id` but received {room_composition_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/room_compositions/{room_composition_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRoomCompositionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoomCompositionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoomCompositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoomCompositionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRoomCompositionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        format: Optional[str] | NotGiven = NOT_GIVEN,
        resolution: Optional[str] | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        video_layout: Dict[str, VideoRegionParam] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_event_url: str | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomCompositionCreateResponse:
        """
        Asynchronously create a room composition.

        Args:
          format: The desired format of the room composition.

          resolution: The desired resolution (width/height in pixels) of the resulting video of the
              room composition. Both width and height are required to be between 16 and 1280;
              and width _ height should not exceed 1280 _ 720

          session_id: id of the room session associated with the room composition.

          video_layout: Describes the video layout of the room composition in terms of regions.

          webhook_event_failover_url: The failover URL where webhooks related to this room composition will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this room composition will be sent. Must
              include a scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/room_compositions",
            body=await async_maybe_transform(
                {
                    "format": format,
                    "resolution": resolution,
                    "session_id": session_id,
                    "video_layout": video_layout,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                room_composition_create_params.RoomCompositionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomCompositionCreateResponse,
        )

    async def retrieve(
        self,
        room_composition_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomCompositionRetrieveResponse:
        """
        View a room composition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_composition_id:
            raise ValueError(
                f"Expected a non-empty value for `room_composition_id` but received {room_composition_id!r}"
            )
        return await self._get(
            f"/room_compositions/{room_composition_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomCompositionRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: room_composition_list_params.Filter | NotGiven = NOT_GIVEN,
        page: room_composition_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoomCompositionListResponse:
        """
        View a list of room compositions.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[date_created_at][eq], filter[date_created_at][gte],
              filter[date_created_at][lte], filter[session_id], filter[status]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/room_compositions",
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
                    room_composition_list_params.RoomCompositionListParams,
                ),
            ),
            cast_to=RoomCompositionListResponse,
        )

    async def delete(
        self,
        room_composition_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Synchronously delete a room composition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_composition_id:
            raise ValueError(
                f"Expected a non-empty value for `room_composition_id` but received {room_composition_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/room_compositions/{room_composition_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RoomCompositionsResourceWithRawResponse:
    def __init__(self, room_compositions: RoomCompositionsResource) -> None:
        self._room_compositions = room_compositions

        self.create = to_raw_response_wrapper(
            room_compositions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            room_compositions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            room_compositions.list,
        )
        self.delete = to_raw_response_wrapper(
            room_compositions.delete,
        )


class AsyncRoomCompositionsResourceWithRawResponse:
    def __init__(self, room_compositions: AsyncRoomCompositionsResource) -> None:
        self._room_compositions = room_compositions

        self.create = async_to_raw_response_wrapper(
            room_compositions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            room_compositions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            room_compositions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            room_compositions.delete,
        )


class RoomCompositionsResourceWithStreamingResponse:
    def __init__(self, room_compositions: RoomCompositionsResource) -> None:
        self._room_compositions = room_compositions

        self.create = to_streamed_response_wrapper(
            room_compositions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            room_compositions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            room_compositions.list,
        )
        self.delete = to_streamed_response_wrapper(
            room_compositions.delete,
        )


class AsyncRoomCompositionsResourceWithStreamingResponse:
    def __init__(self, room_compositions: AsyncRoomCompositionsResource) -> None:
        self._room_compositions = room_compositions

        self.create = async_to_streamed_response_wrapper(
            room_compositions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            room_compositions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            room_compositions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            room_compositions.delete,
        )
