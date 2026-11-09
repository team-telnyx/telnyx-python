# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import (
    calendar_connection_create_params,
    calendar_connection_update_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .meetings import (
    MeetingsResource,
    AsyncMeetingsResource,
    MeetingsResourceWithRawResponse,
    AsyncMeetingsResourceWithRawResponse,
    MeetingsResourceWithStreamingResponse,
    AsyncMeetingsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.calendar_connection_response import CalendarConnectionResponse
from ...types.calendar_connection_list_response import CalendarConnectionListResponse
from ...types.calendar_connection_create_response import CalendarConnectionCreateResponse
from ...types.calendar_connection_update_response import CalendarConnectionUpdateResponse
from ...types.meeting_session_recording_destination_param import MeetingSessionRecordingDestinationParam

__all__ = ["CalendarConnectionsResource", "AsyncCalendarConnectionsResource"]


class CalendarConnectionsResource(SyncAPIResource):
    """Connect calendars and manage automatic meeting joins."""

    @cached_property
    def meetings(self) -> MeetingsResource:
        """Connect calendars and manage automatic meeting joins."""
        return MeetingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CalendarConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CalendarConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalendarConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CalendarConnectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        platform: Literal["google_calendar", "microsoft_outlook"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionCreateResponse:
        """Start Google Calendar or Microsoft Outlook OAuth.

        Open oauth_url in a browser.
        No connection exists until authorization succeeds. The resulting connection is
        owned by the connecting user.

        Args:
          platform: Calendar provider: Google Calendar or Microsoft Outlook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/calendar_connections",
            body=maybe_transform(
                {"platform": platform}, calendar_connection_create_params.CalendarConnectionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionResponse:
        """
        Retrieve a calendar connection owned by the authenticated connecting user.
        Missing and foreign connections both return 404. Signing secrets are omitted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/calendar_connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionResponse,
        )

    def update(
        self,
        id: str,
        *,
        auto_join_policy: Literal["all_meetings", "external_organizer_excluded", "per_meeting"] | Omit = omit,
        bot_name: Optional[str] | Omit = omit,
        default_assistant: Optional[calendar_connection_update_params.DefaultAssistant] | Omit = omit,
        default_barge_in: Optional[bool] | Omit = omit,
        default_recording: Optional[bool] | Omit = omit,
        default_recording_export: Optional[MeetingSessionRecordingDestinationParam] | Omit = omit,
        default_summarize_on_end: Optional[bool] | Omit = omit,
        default_voice: Optional[str] | Omit = omit,
        default_webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionUpdateResponse:
        """Update policy or defaults for future sessions.

        Supply at least one field.
        Existing sessions retain their configuration. Null clears nullable overrides.
        Assistant, recording, and webhook defaults apply to Google Meet and Teams.
        Assistant defaults require default_barge_in to be false or null and
        default_voice to be null. Recording=true requires a destination; false rejects
        one. A non-null default_webhook_url update returns webhook_secret once; save it
        to verify future session deliveries.

        Args:
          auto_join_policy: all_meetings joins eligible events; external_organizer_excluded requires the
              connected user to be the organizer; per_meeting requires an explicit opt-in.

          bot_name: Bot display name; null clears the override.

          default_assistant: Default assistant for future calendar-scheduled Google Meet and Teams sessions.
              The saved configuration must fit within 8 KiB. Use id, audio_gate,
              dynamic_variables, and leave_on_end; avatar is not accepted. audio_gate defaults
              to full_duplex.

          default_barge_in: Default manual speech interruption. Cannot be true with default_assistant.

          default_recording: Google Meet and Teams recording intent. When null, recording is enabled only if
              a destination is set. True requires default_recording_export; false cannot be
              combined with a destination.

          default_recording_export: Customer-owned Telnyx Storage destination for recording exports. Uses the
              authenticated organization and user; do not supply credentials, region,
              organization ID or object key.

          default_summarize_on_end: Generate a summary when each future session transcript finalizes.

          default_voice: Manual-speech voice; must be null when default_assistant is set.

          default_webhook_url: HTTPS destination for future session webhooks. Null clears the default. A
              non-null update returns webhook_secret once; save it to verify signatures for
              sessions created with this default. Existing sessions retain their original
              signing secret.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/calendar_connections/{id}", id=id),
            body=maybe_transform(
                {
                    "auto_join_policy": auto_join_policy,
                    "bot_name": bot_name,
                    "default_assistant": default_assistant,
                    "default_barge_in": default_barge_in,
                    "default_recording": default_recording,
                    "default_recording_export": default_recording_export,
                    "default_summarize_on_end": default_summarize_on_end,
                    "default_voice": default_voice,
                    "default_webhook_url": default_webhook_url,
                },
                calendar_connection_update_params.CalendarConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionListResponse:
        """List only the authenticated connecting user’s calendar connections.

        Session
        resources created by those connections are shared within the organization.
        """
        return self._get(
            "/calendar_connections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionResponse:
        """
        Disconnect the calendar, cancel future joins, and clear retained calendar
        identity fields. Previously created session records, transcripts, artifacts, and
        Storage objects remain. The response is the updated connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/calendar_connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionResponse,
        )


class AsyncCalendarConnectionsResource(AsyncAPIResource):
    """Connect calendars and manage automatic meeting joins."""

    @cached_property
    def meetings(self) -> AsyncMeetingsResource:
        """Connect calendars and manage automatic meeting joins."""
        return AsyncMeetingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCalendarConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalendarConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalendarConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCalendarConnectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        platform: Literal["google_calendar", "microsoft_outlook"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionCreateResponse:
        """Start Google Calendar or Microsoft Outlook OAuth.

        Open oauth_url in a browser.
        No connection exists until authorization succeeds. The resulting connection is
        owned by the connecting user.

        Args:
          platform: Calendar provider: Google Calendar or Microsoft Outlook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/calendar_connections",
            body=await async_maybe_transform(
                {"platform": platform}, calendar_connection_create_params.CalendarConnectionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionResponse:
        """
        Retrieve a calendar connection owned by the authenticated connecting user.
        Missing and foreign connections both return 404. Signing secrets are omitted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/calendar_connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionResponse,
        )

    async def update(
        self,
        id: str,
        *,
        auto_join_policy: Literal["all_meetings", "external_organizer_excluded", "per_meeting"] | Omit = omit,
        bot_name: Optional[str] | Omit = omit,
        default_assistant: Optional[calendar_connection_update_params.DefaultAssistant] | Omit = omit,
        default_barge_in: Optional[bool] | Omit = omit,
        default_recording: Optional[bool] | Omit = omit,
        default_recording_export: Optional[MeetingSessionRecordingDestinationParam] | Omit = omit,
        default_summarize_on_end: Optional[bool] | Omit = omit,
        default_voice: Optional[str] | Omit = omit,
        default_webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionUpdateResponse:
        """Update policy or defaults for future sessions.

        Supply at least one field.
        Existing sessions retain their configuration. Null clears nullable overrides.
        Assistant, recording, and webhook defaults apply to Google Meet and Teams.
        Assistant defaults require default_barge_in to be false or null and
        default_voice to be null. Recording=true requires a destination; false rejects
        one. A non-null default_webhook_url update returns webhook_secret once; save it
        to verify future session deliveries.

        Args:
          auto_join_policy: all_meetings joins eligible events; external_organizer_excluded requires the
              connected user to be the organizer; per_meeting requires an explicit opt-in.

          bot_name: Bot display name; null clears the override.

          default_assistant: Default assistant for future calendar-scheduled Google Meet and Teams sessions.
              The saved configuration must fit within 8 KiB. Use id, audio_gate,
              dynamic_variables, and leave_on_end; avatar is not accepted. audio_gate defaults
              to full_duplex.

          default_barge_in: Default manual speech interruption. Cannot be true with default_assistant.

          default_recording: Google Meet and Teams recording intent. When null, recording is enabled only if
              a destination is set. True requires default_recording_export; false cannot be
              combined with a destination.

          default_recording_export: Customer-owned Telnyx Storage destination for recording exports. Uses the
              authenticated organization and user; do not supply credentials, region,
              organization ID or object key.

          default_summarize_on_end: Generate a summary when each future session transcript finalizes.

          default_voice: Manual-speech voice; must be null when default_assistant is set.

          default_webhook_url: HTTPS destination for future session webhooks. Null clears the default. A
              non-null update returns webhook_secret once; save it to verify signatures for
              sessions created with this default. Existing sessions retain their original
              signing secret.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/calendar_connections/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "auto_join_policy": auto_join_policy,
                    "bot_name": bot_name,
                    "default_assistant": default_assistant,
                    "default_barge_in": default_barge_in,
                    "default_recording": default_recording,
                    "default_recording_export": default_recording_export,
                    "default_summarize_on_end": default_summarize_on_end,
                    "default_voice": default_voice,
                    "default_webhook_url": default_webhook_url,
                },
                calendar_connection_update_params.CalendarConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionListResponse:
        """List only the authenticated connecting user’s calendar connections.

        Session
        resources created by those connections are shared within the organization.
        """
        return await self._get(
            "/calendar_connections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalendarConnectionResponse:
        """
        Disconnect the calendar, cancel future joins, and clear retained calendar
        identity fields. Previously created session records, transcripts, artifacts, and
        Storage objects remain. The response is the updated connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/calendar_connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalendarConnectionResponse,
        )


class CalendarConnectionsResourceWithRawResponse:
    def __init__(self, calendar_connections: CalendarConnectionsResource) -> None:
        self._calendar_connections = calendar_connections

        self.create = to_raw_response_wrapper(
            calendar_connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            calendar_connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            calendar_connections.update,
        )
        self.list = to_raw_response_wrapper(
            calendar_connections.list,
        )
        self.delete = to_raw_response_wrapper(
            calendar_connections.delete,
        )

    @cached_property
    def meetings(self) -> MeetingsResourceWithRawResponse:
        """Connect calendars and manage automatic meeting joins."""
        return MeetingsResourceWithRawResponse(self._calendar_connections.meetings)


class AsyncCalendarConnectionsResourceWithRawResponse:
    def __init__(self, calendar_connections: AsyncCalendarConnectionsResource) -> None:
        self._calendar_connections = calendar_connections

        self.create = async_to_raw_response_wrapper(
            calendar_connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            calendar_connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            calendar_connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            calendar_connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            calendar_connections.delete,
        )

    @cached_property
    def meetings(self) -> AsyncMeetingsResourceWithRawResponse:
        """Connect calendars and manage automatic meeting joins."""
        return AsyncMeetingsResourceWithRawResponse(self._calendar_connections.meetings)


class CalendarConnectionsResourceWithStreamingResponse:
    def __init__(self, calendar_connections: CalendarConnectionsResource) -> None:
        self._calendar_connections = calendar_connections

        self.create = to_streamed_response_wrapper(
            calendar_connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            calendar_connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            calendar_connections.update,
        )
        self.list = to_streamed_response_wrapper(
            calendar_connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            calendar_connections.delete,
        )

    @cached_property
    def meetings(self) -> MeetingsResourceWithStreamingResponse:
        """Connect calendars and manage automatic meeting joins."""
        return MeetingsResourceWithStreamingResponse(self._calendar_connections.meetings)


class AsyncCalendarConnectionsResourceWithStreamingResponse:
    def __init__(self, calendar_connections: AsyncCalendarConnectionsResource) -> None:
        self._calendar_connections = calendar_connections

        self.create = async_to_streamed_response_wrapper(
            calendar_connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            calendar_connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            calendar_connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            calendar_connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            calendar_connections.delete,
        )

    @cached_property
    def meetings(self) -> AsyncMeetingsResourceWithStreamingResponse:
        """Connect calendars and manage automatic meeting joins."""
        return AsyncMeetingsResourceWithStreamingResponse(self._calendar_connections.meetings)
