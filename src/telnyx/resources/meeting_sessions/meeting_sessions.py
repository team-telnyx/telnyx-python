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
from ...types.meeting_session_retrieve_events_response import MeetingSessionRetrieveEventsResponse
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
        avatar: meeting_session_create_params.Avatar | Omit = omit,
        barge_in: bool | Omit = omit,
        bot_name: str | Omit = omit,
        camera_image: meeting_session_create_params.CameraImage | Omit = omit,
        idempotency_key: str | Omit = omit,
        join_at: Union[str, datetime] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
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
        """Creates a new meeting session.

        When an idempotency_key is supplied in the
        request body, replay lookup is scoped to the authenticated account and compares
        only the key; the request payload is not fingerprinted or compared. If a session
        with that key already exists for the account, the existing session is replayed
        (200); otherwise a new session is created (201). Supports bring-your-own-key
        (BYOK) configuration. The session may enter asynchronous states (e.g. joining,
        waiting_for_admission) before becoming active. Optional `camera_image` input is
        write-only and applies only when no Avatar or Assistant webpage output takes
        precedence. An ignored URL is not fetched. An effective URL source is resolved
        before bot creation; neither the source URL nor image bytes are persisted,
        returned, or logged. Treat signed URLs as credentials.

        Args:
          meeting_url: The meeting URL the bot should join.

          assistant: Request options for attaching a voice assistant to the session. Routing fields
              (`call_control_connection_id`, `from`, and `loopback_sip_uri`) are used only to
              establish the assistant call leg and are omitted from response objects.
              `audio_gate` is returned with `id` in the assistant response object.

          avatar: Request options for attaching a bring-your-own-key avatar to the session.

          barge_in: When enabled, a human participant `speech_on` event interrupts and stops the
              current bot audio; it does not bypass admission or initiate speech. Assistant
              sessions reject `barge_in: true`.

          bot_name: Display name for the bot in the meeting. Defaults to "Meeting Bot".

          camera_image: Write-only static camera-tile image for this session, not a native account or
              participant profile photo. Supply exactly one JPEG source. When effective, the
              image is used as the bot's static camera/video output; presentation varies by
              meeting platform and recording configuration and is not guaranteed in
              recordings. An effective Avatar or Assistant webpage output takes precedence, so
              this input is ignored and a URL source is not fetched.

          idempotency_key: Client-supplied idempotency key to safely retry creation requests without
              duplicating sessions. Lookup is scoped to the authenticated account and compares
              the key only; the request payload is not fingerprinted or compared.

          join_at: ISO-8601 timestamp in the future at which the bot should join. If omitted, the
              bot joins immediately.

          metadata: Arbitrary key-value metadata attached to the session. The serialized JSON
              representation must not exceed 16384 characters at runtime.

          speak_on_enter: Text the bot speaks when it enters the meeting.

          summarize_on_end: If true, generate a summary artifact when the session ends.

          voice: Session-default voice identifier used for `speak_on_enter` and ordinary speak
              actions. A voice supplied on an individual speak action overrides this default
              for that utterance.

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
                    "avatar": avatar,
                    "barge_in": barge_in,
                    "bot_name": bot_name,
                    "camera_image": camera_image,
                    "idempotency_key": idempotency_key,
                    "join_at": join_at,
                    "metadata": metadata,
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
        update.

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
        """
        Returns a list of meeting sessions, optionally filtered by status.

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
        persisted meeting session record remains available.

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
        **Not yet available in production** — this route is not currently routed on
        api.telnyx.com and returns a generic 404; it is documented ahead of rollout.
        Irreversibly requests deletion of provider-hosted aggregate recording media
        under the provider contract. The operation retains the Telnyx-local Meeting
        session, transcript segments, events, artifacts, and usage records. It is
        separate from `DELETE /meeting_sessions/{id}`, which stops or cancels
        participation without deleting the persisted session. A missing/foreign session
        returns 404; provider deletion failures return 502.

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
        """
        Returns recordings for a meeting session.

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
        """Returns transcript segments ordered by ascending `seq`.

        Default `limit` is 100
        and maximum is 1,000. Continue with `after=meta.next_after`. A long-poll timeout
        returns 200 with empty `data` and `meta.next_after: null`; retain the cursor
        supplied to that request because null is not a replacement cursor.

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
        avatar: meeting_session_create_params.Avatar | Omit = omit,
        barge_in: bool | Omit = omit,
        bot_name: str | Omit = omit,
        camera_image: meeting_session_create_params.CameraImage | Omit = omit,
        idempotency_key: str | Omit = omit,
        join_at: Union[str, datetime] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
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
        """Creates a new meeting session.

        When an idempotency_key is supplied in the
        request body, replay lookup is scoped to the authenticated account and compares
        only the key; the request payload is not fingerprinted or compared. If a session
        with that key already exists for the account, the existing session is replayed
        (200); otherwise a new session is created (201). Supports bring-your-own-key
        (BYOK) configuration. The session may enter asynchronous states (e.g. joining,
        waiting_for_admission) before becoming active. Optional `camera_image` input is
        write-only and applies only when no Avatar or Assistant webpage output takes
        precedence. An ignored URL is not fetched. An effective URL source is resolved
        before bot creation; neither the source URL nor image bytes are persisted,
        returned, or logged. Treat signed URLs as credentials.

        Args:
          meeting_url: The meeting URL the bot should join.

          assistant: Request options for attaching a voice assistant to the session. Routing fields
              (`call_control_connection_id`, `from`, and `loopback_sip_uri`) are used only to
              establish the assistant call leg and are omitted from response objects.
              `audio_gate` is returned with `id` in the assistant response object.

          avatar: Request options for attaching a bring-your-own-key avatar to the session.

          barge_in: When enabled, a human participant `speech_on` event interrupts and stops the
              current bot audio; it does not bypass admission or initiate speech. Assistant
              sessions reject `barge_in: true`.

          bot_name: Display name for the bot in the meeting. Defaults to "Meeting Bot".

          camera_image: Write-only static camera-tile image for this session, not a native account or
              participant profile photo. Supply exactly one JPEG source. When effective, the
              image is used as the bot's static camera/video output; presentation varies by
              meeting platform and recording configuration and is not guaranteed in
              recordings. An effective Avatar or Assistant webpage output takes precedence, so
              this input is ignored and a URL source is not fetched.

          idempotency_key: Client-supplied idempotency key to safely retry creation requests without
              duplicating sessions. Lookup is scoped to the authenticated account and compares
              the key only; the request payload is not fingerprinted or compared.

          join_at: ISO-8601 timestamp in the future at which the bot should join. If omitted, the
              bot joins immediately.

          metadata: Arbitrary key-value metadata attached to the session. The serialized JSON
              representation must not exceed 16384 characters at runtime.

          speak_on_enter: Text the bot speaks when it enters the meeting.

          summarize_on_end: If true, generate a summary artifact when the session ends.

          voice: Session-default voice identifier used for `speak_on_enter` and ordinary speak
              actions. A voice supplied on an individual speak action overrides this default
              for that utterance.

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
                    "avatar": avatar,
                    "barge_in": barge_in,
                    "bot_name": bot_name,
                    "camera_image": camera_image,
                    "idempotency_key": idempotency_key,
                    "join_at": join_at,
                    "metadata": metadata,
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
        update.

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
        """
        Returns a list of meeting sessions, optionally filtered by status.

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
        persisted meeting session record remains available.

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
        **Not yet available in production** — this route is not currently routed on
        api.telnyx.com and returns a generic 404; it is documented ahead of rollout.
        Irreversibly requests deletion of provider-hosted aggregate recording media
        under the provider contract. The operation retains the Telnyx-local Meeting
        session, transcript segments, events, artifacts, and usage records. It is
        separate from `DELETE /meeting_sessions/{id}`, which stops or cancels
        participation without deleting the persisted session. A missing/foreign session
        returns 404; provider deletion failures return 502.

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
        """
        Returns recordings for a meeting session.

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
        """Returns transcript segments ordered by ascending `seq`.

        Default `limit` is 100
        and maximum is 1,000. Continue with `after=meta.next_after`. A long-poll timeout
        returns 200 with empty `data` and `meta.next_after: null`; retain the cursor
        supplied to that request because null is not a replacement cursor.

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
