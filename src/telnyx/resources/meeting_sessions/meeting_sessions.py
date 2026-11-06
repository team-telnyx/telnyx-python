# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    meeting_session_list_params,
    meeting_session_create_params,
    meeting_session_update_params,
    meeting_session_retrieve_events_params,
    meeting_session_retrieve_transcript_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .artifacts import (
    ArtifactsResource,
    AsyncArtifactsResource,
    ArtifactsResourceWithRawResponse,
    AsyncArtifactsResourceWithRawResponse,
    ArtifactsResourceWithStreamingResponse,
    AsyncArtifactsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.meeting_session_response import MeetingSessionResponse
from ...types.meeting_session_list_response import MeetingSessionListResponse
from ...types.meeting_session_leave_policy_param import MeetingSessionLeavePolicyParam
from ...types.meeting_session_retrieve_events_response import MeetingSessionRetrieveEventsResponse
from ...types.meeting_session_recording_destination_param import MeetingSessionRecordingDestinationParam
from ...types.meeting_session_retrieve_recordings_response import MeetingSessionRetrieveRecordingsResponse
from ...types.meeting_session_retrieve_transcript_response import MeetingSessionRetrieveTranscriptResponse
from ...types.meeting_session_delete_recording_media_response import MeetingSessionDeleteRecordingMediaResponse

__all__ = ["MeetingSessionsResource", "AsyncMeetingSessionsResource"]


class MeetingSessionsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        """Send real-time speech and chat actions to an active meeting session."""
        return ActionsResource(self._client)

    @cached_property
    def artifacts(self) -> ArtifactsResource:
        """Create and retrieve asynchronous summaries and action-item artifacts."""
        return ArtifactsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MeetingSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MeetingSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeetingSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MeetingSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        meeting_url: str,
        assistant: meeting_session_create_params.Assistant | Omit = omit,
        barge_in: bool | Omit = omit,
        bot_name: str | Omit = omit,
        camera_image: meeting_session_create_params.CameraImage | Omit = omit,
        chat_on_enter: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        join_at: Union[str, datetime] | Omit = omit,
        leave_policy: MeetingSessionLeavePolicyParam | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        recording: bool | Omit = omit,
        recording_export: MeetingSessionRecordingDestinationParam | Omit = omit,
        recording_view: Literal["speaker_view", "gallery_view", "speaker_view_no_sidebar"] | Omit = omit,
        speak_on_enter: str | Omit = omit,
        summarize_on_end: bool | Omit = omit,
        voice: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionResponse:
        """Creates a meeting session and returns 201, or 200 for a replay.

        Use a unique
        `idempotency_key` per intended join and reuse the same key and request on
        retries. Reusing a key with a different join configuration or meeting URL can
        return 409 invalid_state. Always retry with the original request. The session
        can pass through joining and waiting_for_admission before active. Optional
        `camera_image` input is write-only and applies when no assistant avatar takes
        precedence. An ignored URL is not fetched. An effective URL source is resolved
        before bot creation; the source URL and image bytes are not returned in the
        session response. Treat signed URLs as credentials. With
        `assistant.avatar: true`, the assistant is read before the bot is created: an
        assistant without a Telnyx avatar configured is rejected with 400
        `invalid_request` (message prefix `assistant_avatar_not_configured:`), an
        unknown assistant with 400 `invalid_request` (prefix `assistant_not_found:`),
        and a failed lookup with 503 `assistant_lookup_unavailable`; no bot is created
        in any of these cases.

        Args:
          meeting_url: The meeting URL the bot should join.

          assistant: Attach a Telnyx AI Assistant owned by the authenticated account. Supply its ID
              and optional conversation settings. Unknown fields are rejected.

          barge_in: When enabled, a human participant `speech_on` event interrupts and stops the
              current bot audio; it does not bypass admission or initiate speech. Assistant
              sessions reject `barge_in: true`.

          bot_name: Display name for the bot in the meeting. Defaults to "Meeting Bot".

          camera_image: Not supported for Google Meet and Teams joins (422 unsupported_capability).
              Write-only static camera-tile image for this session, not an account or
              participant profile photo. Supply exactly one JPEG source. When effective, the
              image is used as the bot's static camera/video output; presentation varies by
              meeting platform and recording configuration and is not guaranteed in
              recordings. An attached assistant or avatar takes precedence, so this input is
              ignored and a URL source is not fetched.

          chat_on_enter: A message the bot posts to the meeting's chat as soon as it becomes active —
              typically a recording disclosure. Delivered at most once. Independent of
              `speak_on_enter`: both may be set, and the chat message posts first because it
              does not wait for text-to-speech or avatar startup. Rejected with 422
              `unsupported_capability` on platforms without meeting chat. For Google Meet and
              Teams, text must be nonblank, at most 4096 UTF-8 bytes, with no control
              characters except tabs and line breaks. Counts toward the 1000-chat-request
              session limit.

          idempotency_key: Use a unique key per intended join and reuse the same key and request on
              retries. Reusing a key with a different join configuration or meeting URL can
              return 409 invalid_state. Always retry with the original request.

          join_at: Future ISO-8601 join timestamp including timezone. Google Meet and Teams accept
              dates at most three years ahead. Omit for an immediate join. Assistant sessions
              created through this endpoint must join immediately.

          leave_policy: Automatic departure settings for Google Meet and Teams. Omitted fields use the
              default behavior. Set at creation; cannot be changed later. Zoom ignores this
              policy.

          metadata: Arbitrary key-value metadata attached to the session. The serialized JSON
              representation must not exceed 16384 characters at runtime.

          recording: Google Meet and Teams only. Defaults to true when recording_export is supplied
              and false otherwise. True requires recording_export.bucket; false cannot be
              combined with recording_export. Fixed at creation, with no pause/resume action.
              Zoom rejects recording, recording_view, and recording_export with 422
              unsupported_capability; omit these fields for Zoom.

          recording_export: Customer-owned Telnyx Storage destination for recording exports. Uses the
              authenticated organization and user; do not supply credentials, region,
              organization ID or object key.

          recording_view: Recording layout for Google Meet and Teams. Defaults to speaker_view. Accepted
              at creation only; does not enable recording by itself.

          speak_on_enter: Text the bot speaks after joining. Available for sessions without a digital
              avatar. With an AI Assistant, the greeting waits until the assistant is
              connected. Rejected with 400 invalid_request when assistant.avatar is true.

          summarize_on_end: If true, generate a summary artifact when the session ends.

          voice: Session-default voice identifier used for `speak_on_enter` and ordinary speak
              actions. A voice supplied on an individual speak action overrides this default
              for that utterance. With an assistant attached, its conversational voice remains
              configured on the assistant.

          webhook_url: HTTPS endpoint to receive session lifecycle callbacks. Static validation
              requires HTTPS, rejects embedded credentials and blocked hosts, and enforces
              egress policy. Validation makes no network request to the endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/meeting_sessions",
            body=maybe_transform(
                {
                    "meeting_url": meeting_url,
                    "assistant": assistant,
                    "barge_in": barge_in,
                    "bot_name": bot_name,
                    "camera_image": camera_image,
                    "chat_on_enter": chat_on_enter,
                    "idempotency_key": idempotency_key,
                    "join_at": join_at,
                    "leave_policy": leave_policy,
                    "metadata": metadata,
                    "recording": recording,
                    "recording_export": recording_export,
                    "recording_view": recording_view,
                    "speak_on_enter": speak_on_enter,
                    "summarize_on_end": summarize_on_end,
                    "voice": voice,
                    "webhook_url": webhook_url,
                },
                meeting_session_create_params.MeetingSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionResponse,
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
    ) -> MeetingSessionResponse:
        """Retrieves a single meeting session by ID.

        A session that does not exist or that
        belongs to a different account both return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/meeting_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionResponse,
        )

    def update(
        self,
        id: str,
        *,
        bot_name: str | Omit = omit,
        join_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionResponse:
        """Updates mutable properties of a meeting session.

        Only sessions in the scheduled
        state can be updated; any other state returns 409 with the invalid_state error
        code. All request fields are optional, and an empty object is a valid no-op
        update. Calendar-controlled Google Meet and Teams sessions return 409
        calendar_managed; change the event instead. A conflicting pending edit returns
        409 edit_in_progress. On a timeout or 503, read the session and retry the same
        changes.

        Args:
          bot_name: Updated display name for the bot.

          join_at: ISO-8601 timestamp for the bot to join. May be updated to reschedule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/meeting_sessions/{id}", id=id),
            body=maybe_transform(
                {
                    "bot_name": bot_name,
                    "join_at": join_at,
                },
                meeting_session_update_params.MeetingSessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionResponse,
        )

    def list(
        self,
        *,
        status: Literal[
            "scheduled", "joining", "waiting_for_admission", "active", "leaving", "ended", "failed", "admission_denied"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionListResponse:
        """Returns a list of meeting sessions, optionally filtered by status.

        List items
        omit assistant.dynamic_variables and recording_export. Some items include
        remote_state_observed_at; retrieve the individual session for current state.

        Args:
          status: Filter meeting sessions by current status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/meeting_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, meeting_session_list_params.MeetingSessionListParams),
            ),
            cast_to=MeetingSessionListResponse,
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
    ) -> MeetingSessionResponse:
        """Stops a meeting session without deleting its persisted record.

        Scheduled bots
        are cancelled, while bots that are joining or active are asked to leave. The
        persisted meeting session record remains available. A successful response can
        report leaving while departure is pending. Poll until ended, failed, or
        admission_denied. Exported Storage objects are unaffected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/meeting_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionResponse,
        )

    def delete_recording_media(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionDeleteRecordingMediaResponse:
        """
        Irreversibly requests deletion of the aggregate recording media for the session.
        The operation retains the Telnyx-local Meeting session, transcript segments,
        events, artifacts, and usage records. It is separate from
        `DELETE /meeting_sessions/{id}`, which stops or cancels participation without
        deleting the persisted session. A missing/foreign session returns 404; a
        deletion request whose outcome is unknown returns 502. Customer Storage exports
        do not support this operation (422 unsupported_capability); delete the exported
        object through Storage instead. Stopping a session does not delete an exported
        object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/meeting_sessions/{id}/recording_media", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionDeleteRecordingMediaResponse,
        )

    def retrieve_events(
        self,
        id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionRetrieveEventsResponse:
        """Returns stored events ordered by ascending `seq`.

        To continue, pass the last
        returned item's `seq` as `after`. An empty page means no later stored events
        existed at read time; this operation returns no separate next-page cursor.
        Default `limit` is 100 and maximum is 1,000.

        Args:
          after: Return results with a cursor position after this value.

          limit: Maximum number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/meeting_sessions/{id}/events", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    meeting_session_retrieve_events_params.MeetingSessionRetrieveEventsParams,
                ),
            ),
            cast_to=MeetingSessionRetrieveEventsResponse,
        )

    def retrieve_recordings(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionRetrieveRecordingsResponse:
        """Retrieve recording export status.

        Customer Storage exports include
        recording_export with the bucket, region, key and pending/exported/failed
        status, or null when no reference is available. The data array is empty for
        these exports. Download or share the object using the Storage API once its
        status is exported. Zoom recordings and existing Google Meet or Teams recordings
        held by the Meeting service continue returning temporary download links in data
        through this same endpoint and session ID. Those recordings do not require
        Storage setup or migration. Refresh this endpoint when a link expires. Select
        the download method from the returned fields, not the platform alone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/meeting_sessions/{id}/recordings", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionRetrieveRecordingsResponse,
        )

    def retrieve_transcript(
        self,
        id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        wait_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionRetrieveTranscriptResponse:
        """Returns transcript segments ordered by ascending seq.

        Default limit is 100,
        maximum 1000. Continue with after=meta.next_after. On an empty page,
        meta.next_after preserves a positive supplied after cursor, or is null when no
        positive cursor was supplied. wait_seconds holds an empty read for up to 25
        seconds; a timeout still returns 200.

        Args:
          after: Return results with a cursor position after this value.

          limit: Maximum number of results to return per page.

          wait_seconds: Long-poll duration in seconds. The server holds the connection open for up to
              this many seconds, waiting for new or updated results before returning an empty
              response. Set to 0 for an immediate response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/meeting_sessions/{id}/transcript", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "wait_seconds": wait_seconds,
                    },
                    meeting_session_retrieve_transcript_params.MeetingSessionRetrieveTranscriptParams,
                ),
            ),
            cast_to=MeetingSessionRetrieveTranscriptResponse,
        )


class AsyncMeetingSessionsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        """Send real-time speech and chat actions to an active meeting session."""
        return AsyncActionsResource(self._client)

    @cached_property
    def artifacts(self) -> AsyncArtifactsResource:
        """Create and retrieve asynchronous summaries and action-item artifacts."""
        return AsyncArtifactsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMeetingSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeetingSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeetingSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMeetingSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        meeting_url: str,
        assistant: meeting_session_create_params.Assistant | Omit = omit,
        barge_in: bool | Omit = omit,
        bot_name: str | Omit = omit,
        camera_image: meeting_session_create_params.CameraImage | Omit = omit,
        chat_on_enter: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        join_at: Union[str, datetime] | Omit = omit,
        leave_policy: MeetingSessionLeavePolicyParam | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        recording: bool | Omit = omit,
        recording_export: MeetingSessionRecordingDestinationParam | Omit = omit,
        recording_view: Literal["speaker_view", "gallery_view", "speaker_view_no_sidebar"] | Omit = omit,
        speak_on_enter: str | Omit = omit,
        summarize_on_end: bool | Omit = omit,
        voice: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionResponse:
        """Creates a meeting session and returns 201, or 200 for a replay.

        Use a unique
        `idempotency_key` per intended join and reuse the same key and request on
        retries. Reusing a key with a different join configuration or meeting URL can
        return 409 invalid_state. Always retry with the original request. The session
        can pass through joining and waiting_for_admission before active. Optional
        `camera_image` input is write-only and applies when no assistant avatar takes
        precedence. An ignored URL is not fetched. An effective URL source is resolved
        before bot creation; the source URL and image bytes are not returned in the
        session response. Treat signed URLs as credentials. With
        `assistant.avatar: true`, the assistant is read before the bot is created: an
        assistant without a Telnyx avatar configured is rejected with 400
        `invalid_request` (message prefix `assistant_avatar_not_configured:`), an
        unknown assistant with 400 `invalid_request` (prefix `assistant_not_found:`),
        and a failed lookup with 503 `assistant_lookup_unavailable`; no bot is created
        in any of these cases.

        Args:
          meeting_url: The meeting URL the bot should join.

          assistant: Attach a Telnyx AI Assistant owned by the authenticated account. Supply its ID
              and optional conversation settings. Unknown fields are rejected.

          barge_in: When enabled, a human participant `speech_on` event interrupts and stops the
              current bot audio; it does not bypass admission or initiate speech. Assistant
              sessions reject `barge_in: true`.

          bot_name: Display name for the bot in the meeting. Defaults to "Meeting Bot".

          camera_image: Not supported for Google Meet and Teams joins (422 unsupported_capability).
              Write-only static camera-tile image for this session, not an account or
              participant profile photo. Supply exactly one JPEG source. When effective, the
              image is used as the bot's static camera/video output; presentation varies by
              meeting platform and recording configuration and is not guaranteed in
              recordings. An attached assistant or avatar takes precedence, so this input is
              ignored and a URL source is not fetched.

          chat_on_enter: A message the bot posts to the meeting's chat as soon as it becomes active —
              typically a recording disclosure. Delivered at most once. Independent of
              `speak_on_enter`: both may be set, and the chat message posts first because it
              does not wait for text-to-speech or avatar startup. Rejected with 422
              `unsupported_capability` on platforms without meeting chat. For Google Meet and
              Teams, text must be nonblank, at most 4096 UTF-8 bytes, with no control
              characters except tabs and line breaks. Counts toward the 1000-chat-request
              session limit.

          idempotency_key: Use a unique key per intended join and reuse the same key and request on
              retries. Reusing a key with a different join configuration or meeting URL can
              return 409 invalid_state. Always retry with the original request.

          join_at: Future ISO-8601 join timestamp including timezone. Google Meet and Teams accept
              dates at most three years ahead. Omit for an immediate join. Assistant sessions
              created through this endpoint must join immediately.

          leave_policy: Automatic departure settings for Google Meet and Teams. Omitted fields use the
              default behavior. Set at creation; cannot be changed later. Zoom ignores this
              policy.

          metadata: Arbitrary key-value metadata attached to the session. The serialized JSON
              representation must not exceed 16384 characters at runtime.

          recording: Google Meet and Teams only. Defaults to true when recording_export is supplied
              and false otherwise. True requires recording_export.bucket; false cannot be
              combined with recording_export. Fixed at creation, with no pause/resume action.
              Zoom rejects recording, recording_view, and recording_export with 422
              unsupported_capability; omit these fields for Zoom.

          recording_export: Customer-owned Telnyx Storage destination for recording exports. Uses the
              authenticated organization and user; do not supply credentials, region,
              organization ID or object key.

          recording_view: Recording layout for Google Meet and Teams. Defaults to speaker_view. Accepted
              at creation only; does not enable recording by itself.

          speak_on_enter: Text the bot speaks after joining. Available for sessions without a digital
              avatar. With an AI Assistant, the greeting waits until the assistant is
              connected. Rejected with 400 invalid_request when assistant.avatar is true.

          summarize_on_end: If true, generate a summary artifact when the session ends.

          voice: Session-default voice identifier used for `speak_on_enter` and ordinary speak
              actions. A voice supplied on an individual speak action overrides this default
              for that utterance. With an assistant attached, its conversational voice remains
              configured on the assistant.

          webhook_url: HTTPS endpoint to receive session lifecycle callbacks. Static validation
              requires HTTPS, rejects embedded credentials and blocked hosts, and enforces
              egress policy. Validation makes no network request to the endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/meeting_sessions",
            body=await async_maybe_transform(
                {
                    "meeting_url": meeting_url,
                    "assistant": assistant,
                    "barge_in": barge_in,
                    "bot_name": bot_name,
                    "camera_image": camera_image,
                    "chat_on_enter": chat_on_enter,
                    "idempotency_key": idempotency_key,
                    "join_at": join_at,
                    "leave_policy": leave_policy,
                    "metadata": metadata,
                    "recording": recording,
                    "recording_export": recording_export,
                    "recording_view": recording_view,
                    "speak_on_enter": speak_on_enter,
                    "summarize_on_end": summarize_on_end,
                    "voice": voice,
                    "webhook_url": webhook_url,
                },
                meeting_session_create_params.MeetingSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionResponse,
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
    ) -> MeetingSessionResponse:
        """Retrieves a single meeting session by ID.

        A session that does not exist or that
        belongs to a different account both return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/meeting_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionResponse,
        )

    async def update(
        self,
        id: str,
        *,
        bot_name: str | Omit = omit,
        join_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionResponse:
        """Updates mutable properties of a meeting session.

        Only sessions in the scheduled
        state can be updated; any other state returns 409 with the invalid_state error
        code. All request fields are optional, and an empty object is a valid no-op
        update. Calendar-controlled Google Meet and Teams sessions return 409
        calendar_managed; change the event instead. A conflicting pending edit returns
        409 edit_in_progress. On a timeout or 503, read the session and retry the same
        changes.

        Args:
          bot_name: Updated display name for the bot.

          join_at: ISO-8601 timestamp for the bot to join. May be updated to reschedule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/meeting_sessions/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "bot_name": bot_name,
                    "join_at": join_at,
                },
                meeting_session_update_params.MeetingSessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionResponse,
        )

    async def list(
        self,
        *,
        status: Literal[
            "scheduled", "joining", "waiting_for_admission", "active", "leaving", "ended", "failed", "admission_denied"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionListResponse:
        """Returns a list of meeting sessions, optionally filtered by status.

        List items
        omit assistant.dynamic_variables and recording_export. Some items include
        remote_state_observed_at; retrieve the individual session for current state.

        Args:
          status: Filter meeting sessions by current status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/meeting_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"status": status}, meeting_session_list_params.MeetingSessionListParams
                ),
            ),
            cast_to=MeetingSessionListResponse,
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
    ) -> MeetingSessionResponse:
        """Stops a meeting session without deleting its persisted record.

        Scheduled bots
        are cancelled, while bots that are joining or active are asked to leave. The
        persisted meeting session record remains available. A successful response can
        report leaving while departure is pending. Poll until ended, failed, or
        admission_denied. Exported Storage objects are unaffected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/meeting_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionResponse,
        )

    async def delete_recording_media(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionDeleteRecordingMediaResponse:
        """
        Irreversibly requests deletion of the aggregate recording media for the session.
        The operation retains the Telnyx-local Meeting session, transcript segments,
        events, artifacts, and usage records. It is separate from
        `DELETE /meeting_sessions/{id}`, which stops or cancels participation without
        deleting the persisted session. A missing/foreign session returns 404; a
        deletion request whose outcome is unknown returns 502. Customer Storage exports
        do not support this operation (422 unsupported_capability); delete the exported
        object through Storage instead. Stopping a session does not delete an exported
        object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/meeting_sessions/{id}/recording_media", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionDeleteRecordingMediaResponse,
        )

    async def retrieve_events(
        self,
        id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionRetrieveEventsResponse:
        """Returns stored events ordered by ascending `seq`.

        To continue, pass the last
        returned item's `seq` as `after`. An empty page means no later stored events
        existed at read time; this operation returns no separate next-page cursor.
        Default `limit` is 100 and maximum is 1,000.

        Args:
          after: Return results with a cursor position after this value.

          limit: Maximum number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/meeting_sessions/{id}/events", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    meeting_session_retrieve_events_params.MeetingSessionRetrieveEventsParams,
                ),
            ),
            cast_to=MeetingSessionRetrieveEventsResponse,
        )

    async def retrieve_recordings(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionRetrieveRecordingsResponse:
        """Retrieve recording export status.

        Customer Storage exports include
        recording_export with the bucket, region, key and pending/exported/failed
        status, or null when no reference is available. The data array is empty for
        these exports. Download or share the object using the Storage API once its
        status is exported. Zoom recordings and existing Google Meet or Teams recordings
        held by the Meeting service continue returning temporary download links in data
        through this same endpoint and session ID. Those recordings do not require
        Storage setup or migration. Refresh this endpoint when a link expires. Select
        the download method from the returned fields, not the platform alone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/meeting_sessions/{id}/recordings", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionRetrieveRecordingsResponse,
        )

    async def retrieve_transcript(
        self,
        id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        wait_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionRetrieveTranscriptResponse:
        """Returns transcript segments ordered by ascending seq.

        Default limit is 100,
        maximum 1000. Continue with after=meta.next_after. On an empty page,
        meta.next_after preserves a positive supplied after cursor, or is null when no
        positive cursor was supplied. wait_seconds holds an empty read for up to 25
        seconds; a timeout still returns 200.

        Args:
          after: Return results with a cursor position after this value.

          limit: Maximum number of results to return per page.

          wait_seconds: Long-poll duration in seconds. The server holds the connection open for up to
              this many seconds, waiting for new or updated results before returning an empty
              response. Set to 0 for an immediate response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/meeting_sessions/{id}/transcript", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "wait_seconds": wait_seconds,
                    },
                    meeting_session_retrieve_transcript_params.MeetingSessionRetrieveTranscriptParams,
                ),
            ),
            cast_to=MeetingSessionRetrieveTranscriptResponse,
        )


class MeetingSessionsResourceWithRawResponse:
    def __init__(self, meeting_sessions: MeetingSessionsResource) -> None:
        self._meeting_sessions = meeting_sessions

        self.create = to_raw_response_wrapper(
            meeting_sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            meeting_sessions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            meeting_sessions.update,
        )
        self.list = to_raw_response_wrapper(
            meeting_sessions.list,
        )
        self.delete = to_raw_response_wrapper(
            meeting_sessions.delete,
        )
        self.delete_recording_media = to_raw_response_wrapper(
            meeting_sessions.delete_recording_media,
        )
        self.retrieve_events = to_raw_response_wrapper(
            meeting_sessions.retrieve_events,
        )
        self.retrieve_recordings = to_raw_response_wrapper(
            meeting_sessions.retrieve_recordings,
        )
        self.retrieve_transcript = to_raw_response_wrapper(
            meeting_sessions.retrieve_transcript,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """Send real-time speech and chat actions to an active meeting session."""
        return ActionsResourceWithRawResponse(self._meeting_sessions.actions)

    @cached_property
    def artifacts(self) -> ArtifactsResourceWithRawResponse:
        """Create and retrieve asynchronous summaries and action-item artifacts."""
        return ArtifactsResourceWithRawResponse(self._meeting_sessions.artifacts)


class AsyncMeetingSessionsResourceWithRawResponse:
    def __init__(self, meeting_sessions: AsyncMeetingSessionsResource) -> None:
        self._meeting_sessions = meeting_sessions

        self.create = async_to_raw_response_wrapper(
            meeting_sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            meeting_sessions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            meeting_sessions.update,
        )
        self.list = async_to_raw_response_wrapper(
            meeting_sessions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            meeting_sessions.delete,
        )
        self.delete_recording_media = async_to_raw_response_wrapper(
            meeting_sessions.delete_recording_media,
        )
        self.retrieve_events = async_to_raw_response_wrapper(
            meeting_sessions.retrieve_events,
        )
        self.retrieve_recordings = async_to_raw_response_wrapper(
            meeting_sessions.retrieve_recordings,
        )
        self.retrieve_transcript = async_to_raw_response_wrapper(
            meeting_sessions.retrieve_transcript,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """Send real-time speech and chat actions to an active meeting session."""
        return AsyncActionsResourceWithRawResponse(self._meeting_sessions.actions)

    @cached_property
    def artifacts(self) -> AsyncArtifactsResourceWithRawResponse:
        """Create and retrieve asynchronous summaries and action-item artifacts."""
        return AsyncArtifactsResourceWithRawResponse(self._meeting_sessions.artifacts)


class MeetingSessionsResourceWithStreamingResponse:
    def __init__(self, meeting_sessions: MeetingSessionsResource) -> None:
        self._meeting_sessions = meeting_sessions

        self.create = to_streamed_response_wrapper(
            meeting_sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            meeting_sessions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            meeting_sessions.update,
        )
        self.list = to_streamed_response_wrapper(
            meeting_sessions.list,
        )
        self.delete = to_streamed_response_wrapper(
            meeting_sessions.delete,
        )
        self.delete_recording_media = to_streamed_response_wrapper(
            meeting_sessions.delete_recording_media,
        )
        self.retrieve_events = to_streamed_response_wrapper(
            meeting_sessions.retrieve_events,
        )
        self.retrieve_recordings = to_streamed_response_wrapper(
            meeting_sessions.retrieve_recordings,
        )
        self.retrieve_transcript = to_streamed_response_wrapper(
            meeting_sessions.retrieve_transcript,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """Send real-time speech and chat actions to an active meeting session."""
        return ActionsResourceWithStreamingResponse(self._meeting_sessions.actions)

    @cached_property
    def artifacts(self) -> ArtifactsResourceWithStreamingResponse:
        """Create and retrieve asynchronous summaries and action-item artifacts."""
        return ArtifactsResourceWithStreamingResponse(self._meeting_sessions.artifacts)


class AsyncMeetingSessionsResourceWithStreamingResponse:
    def __init__(self, meeting_sessions: AsyncMeetingSessionsResource) -> None:
        self._meeting_sessions = meeting_sessions

        self.create = async_to_streamed_response_wrapper(
            meeting_sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            meeting_sessions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            meeting_sessions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            meeting_sessions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            meeting_sessions.delete,
        )
        self.delete_recording_media = async_to_streamed_response_wrapper(
            meeting_sessions.delete_recording_media,
        )
        self.retrieve_events = async_to_streamed_response_wrapper(
            meeting_sessions.retrieve_events,
        )
        self.retrieve_recordings = async_to_streamed_response_wrapper(
            meeting_sessions.retrieve_recordings,
        )
        self.retrieve_transcript = async_to_streamed_response_wrapper(
            meeting_sessions.retrieve_transcript,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """Send real-time speech and chat actions to an active meeting session."""
        return AsyncActionsResourceWithStreamingResponse(self._meeting_sessions.actions)

    @cached_property
    def artifacts(self) -> AsyncArtifactsResourceWithStreamingResponse:
        """Create and retrieve asynchronous summaries and action-item artifacts."""
        return AsyncArtifactsResourceWithStreamingResponse(self._meeting_sessions.artifacts)
