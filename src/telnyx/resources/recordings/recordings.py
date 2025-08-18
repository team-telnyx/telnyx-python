# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import recording_list_params
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
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
from ..._base_client import make_request_options
from ...types.recording_list_response import RecordingListResponse
from ...types.recording_delete_response import RecordingDeleteResponse
from ...types.recording_retrieve_response import RecordingRetrieveResponse

__all__ = ["RecordingsResource", "AsyncRecordingsResource"]


class RecordingsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RecordingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        recording_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingRetrieveResponse:
        """
        Retrieves the details of an existing call recording.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not recording_id:
            raise ValueError(f"Expected a non-empty value for `recording_id` but received {recording_id!r}")
        return self._get(
            f"/recordings/{recording_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: recording_list_params.Filter | NotGiven = NOT_GIVEN,
        page: recording_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingListResponse:
        """
        Returns a list of your call recordings.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[conference_id], filter[created_at][gte], filter[created_at][lte],
              filter[call_leg_id], filter[call_session_id], filter[from], filter[to],
              filter[connection_id]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/recordings",
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
                    recording_list_params.RecordingListParams,
                ),
            ),
            cast_to=RecordingListResponse,
        )

    def delete(
        self,
        recording_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingDeleteResponse:
        """
        Permanently deletes a call recording.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not recording_id:
            raise ValueError(f"Expected a non-empty value for `recording_id` but received {recording_id!r}")
        return self._delete(
            f"/recordings/{recording_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingDeleteResponse,
        )


class AsyncRecordingsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRecordingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        recording_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingRetrieveResponse:
        """
        Retrieves the details of an existing call recording.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not recording_id:
            raise ValueError(f"Expected a non-empty value for `recording_id` but received {recording_id!r}")
        return await self._get(
            f"/recordings/{recording_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: recording_list_params.Filter | NotGiven = NOT_GIVEN,
        page: recording_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingListResponse:
        """
        Returns a list of your call recordings.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[conference_id], filter[created_at][gte], filter[created_at][lte],
              filter[call_leg_id], filter[call_session_id], filter[from], filter[to],
              filter[connection_id]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/recordings",
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
                    recording_list_params.RecordingListParams,
                ),
            ),
            cast_to=RecordingListResponse,
        )

    async def delete(
        self,
        recording_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingDeleteResponse:
        """
        Permanently deletes a call recording.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not recording_id:
            raise ValueError(f"Expected a non-empty value for `recording_id` but received {recording_id!r}")
        return await self._delete(
            f"/recordings/{recording_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingDeleteResponse,
        )


class RecordingsResourceWithRawResponse:
    def __init__(self, recordings: RecordingsResource) -> None:
        self._recordings = recordings

        self.retrieve = to_raw_response_wrapper(
            recordings.retrieve,
        )
        self.list = to_raw_response_wrapper(
            recordings.list,
        )
        self.delete = to_raw_response_wrapper(
            recordings.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._recordings.actions)


class AsyncRecordingsResourceWithRawResponse:
    def __init__(self, recordings: AsyncRecordingsResource) -> None:
        self._recordings = recordings

        self.retrieve = async_to_raw_response_wrapper(
            recordings.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            recordings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            recordings.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._recordings.actions)


class RecordingsResourceWithStreamingResponse:
    def __init__(self, recordings: RecordingsResource) -> None:
        self._recordings = recordings

        self.retrieve = to_streamed_response_wrapper(
            recordings.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            recordings.list,
        )
        self.delete = to_streamed_response_wrapper(
            recordings.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._recordings.actions)


class AsyncRecordingsResourceWithStreamingResponse:
    def __init__(self, recordings: AsyncRecordingsResource) -> None:
        self._recordings = recordings

        self.retrieve = async_to_streamed_response_wrapper(
            recordings.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            recordings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            recordings.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._recordings.actions)
