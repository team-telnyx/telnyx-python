# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    MeetingSessionResponse,
    MeetingSessionListResponse,
    MeetingSessionRetrieveEventsResponse,
    MeetingSessionRetrieveRecordingsResponse,
    MeetingSessionRetrieveTranscriptResponse,
    MeetingSessionDeleteRecordingMediaResponse,
)
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMeetingSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.create(
            meeting_url="https://zoom.us/j/1234567890",
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.create(
            meeting_url="https://zoom.us/j/1234567890",
            assistant={
                "id": "asst_fake-uuid-1234",
                "call_control_connection_id": "conn-fake-abcdef",
                "from": "+12025550199",
                "loopback_sip_uri": "sip:loopback@example.invalid",
                "audio_gate": "half_duplex",
            },
            avatar={
                "api_key": "fake_avatar_api_key_do_not_use",
                "avatar_id": "avatar_fake-001",
                "provider": "anam",
            },
            barge_in=True,
            bot_name="Notetaker",
            camera_image={
                "base64_data": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/wAALCAACAAIBAREA/8QAFAABAAAAAAAAAAAAAAAAAAAACP/EAB4QAAAEBwAAAAAAAAAAAAAAAAAEBgcCFic1RVNi/9oACAEBAAA/AH8hGJbWR09TxKW4vhC2qHgf/9k=",
                "format": "jpeg",
            },
            idempotency_key="x",
            join_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "bar"},
            speak_on_enter="x",
            summarize_on_end=True,
            voice="x",
            webhook_url="https://example.com",
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.meeting_sessions.with_raw_response.create(
            meeting_url="https://zoom.us/j/1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = response.parse()
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.meeting_sessions.with_streaming_response.create(
            meeting_url="https://zoom.us/j/1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = response.parse()
            assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.retrieve(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.meeting_sessions.with_raw_response.retrieve(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = response.parse()
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.meeting_sessions.with_streaming_response.retrieve(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = response.parse()
            assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.update(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.update(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            bot_name="x",
            join_at=parse_datetime("2026-08-05T17:00:00Z"),
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.meeting_sessions.with_raw_response.update(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = response.parse()
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.meeting_sessions.with_streaming_response.update(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = response.parse()
            assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.list()
        assert_matches_type(MeetingSessionListResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.list(
            status="scheduled",
        )
        assert_matches_type(MeetingSessionListResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.meeting_sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = response.parse()
        assert_matches_type(MeetingSessionListResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.meeting_sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = response.parse()
            assert_matches_type(MeetingSessionListResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.delete(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.meeting_sessions.with_raw_response.delete(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = response.parse()
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.meeting_sessions.with_streaming_response.delete(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = response.parse()
            assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_recording_media(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.delete_recording_media(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionDeleteRecordingMediaResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_recording_media(self, client: Telnyx) -> None:
        response = client.meeting_sessions.with_raw_response.delete_recording_media(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = response.parse()
        assert_matches_type(MeetingSessionDeleteRecordingMediaResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_recording_media(self, client: Telnyx) -> None:
        with client.meeting_sessions.with_streaming_response.delete_recording_media(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = response.parse()
            assert_matches_type(MeetingSessionDeleteRecordingMediaResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_recording_media(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.with_raw_response.delete_recording_media(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_events(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.retrieve_events(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionRetrieveEventsResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_events_with_all_params(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.retrieve_events(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            after=0,
            limit=1,
        )
        assert_matches_type(MeetingSessionRetrieveEventsResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_events(self, client: Telnyx) -> None:
        response = client.meeting_sessions.with_raw_response.retrieve_events(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = response.parse()
        assert_matches_type(MeetingSessionRetrieveEventsResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_events(self, client: Telnyx) -> None:
        with client.meeting_sessions.with_streaming_response.retrieve_events(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = response.parse()
            assert_matches_type(MeetingSessionRetrieveEventsResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_events(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.with_raw_response.retrieve_events(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_recordings(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.retrieve_recordings(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionRetrieveRecordingsResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_recordings(self, client: Telnyx) -> None:
        response = client.meeting_sessions.with_raw_response.retrieve_recordings(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = response.parse()
        assert_matches_type(MeetingSessionRetrieveRecordingsResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_recordings(self, client: Telnyx) -> None:
        with client.meeting_sessions.with_streaming_response.retrieve_recordings(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = response.parse()
            assert_matches_type(MeetingSessionRetrieveRecordingsResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_recordings(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.with_raw_response.retrieve_recordings(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_transcript(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.retrieve_transcript(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionRetrieveTranscriptResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_transcript_with_all_params(self, client: Telnyx) -> None:
        meeting_session = client.meeting_sessions.retrieve_transcript(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            after=0,
            limit=1,
            wait_seconds=0,
        )
        assert_matches_type(MeetingSessionRetrieveTranscriptResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_transcript(self, client: Telnyx) -> None:
        response = client.meeting_sessions.with_raw_response.retrieve_transcript(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = response.parse()
        assert_matches_type(MeetingSessionRetrieveTranscriptResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_transcript(self, client: Telnyx) -> None:
        with client.meeting_sessions.with_streaming_response.retrieve_transcript(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = response.parse()
            assert_matches_type(MeetingSessionRetrieveTranscriptResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_transcript(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.with_raw_response.retrieve_transcript(
                id="",
            )


class TestAsyncMeetingSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.create(
            meeting_url="https://zoom.us/j/1234567890",
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.create(
            meeting_url="https://zoom.us/j/1234567890",
            assistant={
                "id": "asst_fake-uuid-1234",
                "call_control_connection_id": "conn-fake-abcdef",
                "from": "+12025550199",
                "loopback_sip_uri": "sip:loopback@example.invalid",
                "audio_gate": "half_duplex",
            },
            avatar={
                "api_key": "fake_avatar_api_key_do_not_use",
                "avatar_id": "avatar_fake-001",
                "provider": "anam",
            },
            barge_in=True,
            bot_name="Notetaker",
            camera_image={
                "base64_data": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/wAALCAACAAIBAREA/8QAFAABAAAAAAAAAAAAAAAAAAAACP/EAB4QAAAEBwAAAAAAAAAAAAAAAAAEBgcCFic1RVNi/9oACAEBAAA/AH8hGJbWR09TxKW4vhC2qHgf/9k=",
                "format": "jpeg",
            },
            idempotency_key="x",
            join_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "bar"},
            speak_on_enter="x",
            summarize_on_end=True,
            voice="x",
            webhook_url="https://example.com",
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.with_raw_response.create(
            meeting_url="https://zoom.us/j/1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = await response.parse()
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.with_streaming_response.create(
            meeting_url="https://zoom.us/j/1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = await response.parse()
            assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.retrieve(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.with_raw_response.retrieve(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = await response.parse()
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.with_streaming_response.retrieve(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = await response.parse()
            assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.update(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.update(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            bot_name="x",
            join_at=parse_datetime("2026-08-05T17:00:00Z"),
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.with_raw_response.update(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = await response.parse()
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.with_streaming_response.update(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = await response.parse()
            assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.list()
        assert_matches_type(MeetingSessionListResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.list(
            status="scheduled",
        )
        assert_matches_type(MeetingSessionListResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = await response.parse()
        assert_matches_type(MeetingSessionListResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = await response.parse()
            assert_matches_type(MeetingSessionListResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.delete(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.with_raw_response.delete(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = await response.parse()
        assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.with_streaming_response.delete(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = await response.parse()
            assert_matches_type(MeetingSessionResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_recording_media(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.delete_recording_media(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionDeleteRecordingMediaResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_recording_media(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.with_raw_response.delete_recording_media(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = await response.parse()
        assert_matches_type(MeetingSessionDeleteRecordingMediaResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_recording_media(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.with_streaming_response.delete_recording_media(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = await response.parse()
            assert_matches_type(MeetingSessionDeleteRecordingMediaResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_recording_media(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.with_raw_response.delete_recording_media(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.retrieve_events(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionRetrieveEventsResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_events_with_all_params(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.retrieve_events(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            after=0,
            limit=1,
        )
        assert_matches_type(MeetingSessionRetrieveEventsResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.with_raw_response.retrieve_events(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = await response.parse()
        assert_matches_type(MeetingSessionRetrieveEventsResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.with_streaming_response.retrieve_events(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = await response.parse()
            assert_matches_type(MeetingSessionRetrieveEventsResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.with_raw_response.retrieve_events(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_recordings(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.retrieve_recordings(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionRetrieveRecordingsResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_recordings(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.with_raw_response.retrieve_recordings(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = await response.parse()
        assert_matches_type(MeetingSessionRetrieveRecordingsResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_recordings(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.with_streaming_response.retrieve_recordings(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = await response.parse()
            assert_matches_type(MeetingSessionRetrieveRecordingsResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_recordings(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.with_raw_response.retrieve_recordings(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_transcript(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.retrieve_transcript(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionRetrieveTranscriptResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_transcript_with_all_params(self, async_client: AsyncTelnyx) -> None:
        meeting_session = await async_client.meeting_sessions.retrieve_transcript(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            after=0,
            limit=1,
            wait_seconds=0,
        )
        assert_matches_type(MeetingSessionRetrieveTranscriptResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_transcript(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.with_raw_response.retrieve_transcript(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting_session = await response.parse()
        assert_matches_type(MeetingSessionRetrieveTranscriptResponse, meeting_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_transcript(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.with_streaming_response.retrieve_transcript(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting_session = await response.parse()
            assert_matches_type(MeetingSessionRetrieveTranscriptResponse, meeting_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_transcript(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.with_raw_response.retrieve_transcript(
                id="",
            )
