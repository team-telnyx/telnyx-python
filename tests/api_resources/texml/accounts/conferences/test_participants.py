# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.texml.accounts.conferences import (
    ParticipantUpdateResponse,
    ParticipantRetrieveResponse,
    ParticipantParticipantsResponse,
    ParticipantRetrieveParticipantsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParticipants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        participant = client.texml.accounts.conferences.participants.retrieve(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )
        assert_matches_type(ParticipantRetrieveResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.texml.accounts.conferences.participants.with_raw_response.retrieve(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantRetrieveResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.texml.accounts.conferences.participants.with_streaming_response.retrieve(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantRetrieveResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.conferences.participants.with_raw_response.retrieve(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="",
                conference_sid="conference_sid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            client.texml.accounts.conferences.participants.with_raw_response.retrieve(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="account_sid",
                conference_sid="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `call_sid_or_participant_label` but received ''"
        ):
            client.texml.accounts.conferences.participants.with_raw_response.retrieve(
                call_sid_or_participant_label="",
                account_sid="account_sid",
                conference_sid="conference_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        participant = client.texml.accounts.conferences.participants.update(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )
        assert_matches_type(ParticipantUpdateResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        participant = client.texml.accounts.conferences.participants.update(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
            announce_method="GET",
            announce_url="https://www.example.com/announce.xml",
            beep_on_exit=False,
            call_sid_to_coach="v3:9X2vxPDFY2RHSJ1EdMS0RHRksMTg7ldNxdjWbVr9zBjbGjGsSe-aiQ",
            coaching=False,
            end_conference_on_exit=False,
            hold=True,
            hold_method="POST",
            hold_url="HoldUrl",
            muted=True,
            wait_url="https://www.example.com/wait_music.mp3",
        )
        assert_matches_type(ParticipantUpdateResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.texml.accounts.conferences.participants.with_raw_response.update(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantUpdateResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.texml.accounts.conferences.participants.with_streaming_response.update(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantUpdateResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.conferences.participants.with_raw_response.update(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="",
                conference_sid="conference_sid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            client.texml.accounts.conferences.participants.with_raw_response.update(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="account_sid",
                conference_sid="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `call_sid_or_participant_label` but received ''"
        ):
            client.texml.accounts.conferences.participants.with_raw_response.update(
                call_sid_or_participant_label="",
                account_sid="account_sid",
                conference_sid="conference_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        participant = client.texml.accounts.conferences.participants.delete(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )
        assert participant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.texml.accounts.conferences.participants.with_raw_response.delete(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert participant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.texml.accounts.conferences.participants.with_streaming_response.delete(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert participant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.conferences.participants.with_raw_response.delete(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="",
                conference_sid="conference_sid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            client.texml.accounts.conferences.participants.with_raw_response.delete(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="account_sid",
                conference_sid="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `call_sid_or_participant_label` but received ''"
        ):
            client.texml.accounts.conferences.participants.with_raw_response.delete(
                call_sid_or_participant_label="",
                account_sid="account_sid",
                conference_sid="conference_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_participants(self, client: Telnyx) -> None:
        participant = client.texml.accounts.conferences.participants.participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ParticipantParticipantsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_participants_with_all_params(self, client: Telnyx) -> None:
        participant = client.texml.accounts.conferences.participants.participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
            amd_status_callback="https://www.example.com/amd_result",
            amd_status_callback_method="GET",
            beep="onExit",
            caller_id="Info",
            call_sid_to_coach="v3:9X2vxPDFY2RHSJ1EdMS0RHRksMTg7ldNxdjWbVr9zBjbGjGsSe-aiQ",
            cancel_playback_on_detect_message_end=False,
            cancel_playback_on_machine_detection=False,
            coaching=False,
            conference_record="record-from-start",
            conference_recording_status_callback="https://example.com/conference_recording_status_callback",
            conference_recording_status_callback_event="in-progress completed failed absent",
            conference_recording_status_callback_method="GET",
            conference_recording_timeout=5,
            conference_status_callback="https://example.com/conference_status_callback",
            conference_status_callback_event="start end join leave",
            conference_status_callback_method="GET",
            conference_trim="trim-silence",
            early_media=True,
            end_conference_on_exit=True,
            from_="+12065550200",
            machine_detection="Enable",
            machine_detection_silence_timeout=2000,
            machine_detection_speech_end_threshold=2000,
            machine_detection_speech_threshold=2000,
            machine_detection_timeout=1000,
            max_participants=30,
            muted=True,
            preferred_codecs="PCMA,PCMU",
            record=False,
            recording_channels="dual",
            recording_status_callback="https://example.com/recording_status_callback",
            recording_status_callback_event="in-progress completed absent",
            recording_status_callback_method="GET",
            recording_track="inbound",
            sip_auth_password="1234",
            sip_auth_username="user",
            start_conference_on_enter=False,
            status_callback="https://www.example.com/callback",
            status_callback_event="answered completed",
            status_callback_method="GET",
            time_limit=30,
            timeout_seconds=30,
            to="+12065550100",
            trim="trim-silence",
            wait_url="https://www.example.com/wait_music.mp3",
        )
        assert_matches_type(ParticipantParticipantsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_participants(self, client: Telnyx) -> None:
        response = client.texml.accounts.conferences.participants.with_raw_response.participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantParticipantsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_participants(self, client: Telnyx) -> None:
        with client.texml.accounts.conferences.participants.with_streaming_response.participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantParticipantsResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_participants(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.conferences.participants.with_raw_response.participants(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            client.texml.accounts.conferences.participants.with_raw_response.participants(
                conference_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_participants(self, client: Telnyx) -> None:
        participant = client.texml.accounts.conferences.participants.retrieve_participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ParticipantRetrieveParticipantsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_participants(self, client: Telnyx) -> None:
        response = client.texml.accounts.conferences.participants.with_raw_response.retrieve_participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantRetrieveParticipantsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_participants(self, client: Telnyx) -> None:
        with client.texml.accounts.conferences.participants.with_streaming_response.retrieve_participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantRetrieveParticipantsResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_participants(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.conferences.participants.with_raw_response.retrieve_participants(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            client.texml.accounts.conferences.participants.with_raw_response.retrieve_participants(
                conference_sid="",
                account_sid="account_sid",
            )


class TestAsyncParticipants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        participant = await async_client.texml.accounts.conferences.participants.retrieve(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )
        assert_matches_type(ParticipantRetrieveResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.conferences.participants.with_raw_response.retrieve(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantRetrieveResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.conferences.participants.with_streaming_response.retrieve(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantRetrieveResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.conferences.participants.with_raw_response.retrieve(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="",
                conference_sid="conference_sid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            await async_client.texml.accounts.conferences.participants.with_raw_response.retrieve(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="account_sid",
                conference_sid="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `call_sid_or_participant_label` but received ''"
        ):
            await async_client.texml.accounts.conferences.participants.with_raw_response.retrieve(
                call_sid_or_participant_label="",
                account_sid="account_sid",
                conference_sid="conference_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        participant = await async_client.texml.accounts.conferences.participants.update(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )
        assert_matches_type(ParticipantUpdateResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        participant = await async_client.texml.accounts.conferences.participants.update(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
            announce_method="GET",
            announce_url="https://www.example.com/announce.xml",
            beep_on_exit=False,
            call_sid_to_coach="v3:9X2vxPDFY2RHSJ1EdMS0RHRksMTg7ldNxdjWbVr9zBjbGjGsSe-aiQ",
            coaching=False,
            end_conference_on_exit=False,
            hold=True,
            hold_method="POST",
            hold_url="HoldUrl",
            muted=True,
            wait_url="https://www.example.com/wait_music.mp3",
        )
        assert_matches_type(ParticipantUpdateResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.conferences.participants.with_raw_response.update(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantUpdateResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.conferences.participants.with_streaming_response.update(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantUpdateResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.conferences.participants.with_raw_response.update(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="",
                conference_sid="conference_sid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            await async_client.texml.accounts.conferences.participants.with_raw_response.update(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="account_sid",
                conference_sid="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `call_sid_or_participant_label` but received ''"
        ):
            await async_client.texml.accounts.conferences.participants.with_raw_response.update(
                call_sid_or_participant_label="",
                account_sid="account_sid",
                conference_sid="conference_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        participant = await async_client.texml.accounts.conferences.participants.delete(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )
        assert participant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.conferences.participants.with_raw_response.delete(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert participant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.conferences.participants.with_streaming_response.delete(
            call_sid_or_participant_label="call_sid_or_participant_label",
            account_sid="account_sid",
            conference_sid="conference_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert participant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.conferences.participants.with_raw_response.delete(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="",
                conference_sid="conference_sid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            await async_client.texml.accounts.conferences.participants.with_raw_response.delete(
                call_sid_or_participant_label="call_sid_or_participant_label",
                account_sid="account_sid",
                conference_sid="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `call_sid_or_participant_label` but received ''"
        ):
            await async_client.texml.accounts.conferences.participants.with_raw_response.delete(
                call_sid_or_participant_label="",
                account_sid="account_sid",
                conference_sid="conference_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_participants(self, async_client: AsyncTelnyx) -> None:
        participant = await async_client.texml.accounts.conferences.participants.participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ParticipantParticipantsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_participants_with_all_params(self, async_client: AsyncTelnyx) -> None:
        participant = await async_client.texml.accounts.conferences.participants.participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
            amd_status_callback="https://www.example.com/amd_result",
            amd_status_callback_method="GET",
            beep="onExit",
            caller_id="Info",
            call_sid_to_coach="v3:9X2vxPDFY2RHSJ1EdMS0RHRksMTg7ldNxdjWbVr9zBjbGjGsSe-aiQ",
            cancel_playback_on_detect_message_end=False,
            cancel_playback_on_machine_detection=False,
            coaching=False,
            conference_record="record-from-start",
            conference_recording_status_callback="https://example.com/conference_recording_status_callback",
            conference_recording_status_callback_event="in-progress completed failed absent",
            conference_recording_status_callback_method="GET",
            conference_recording_timeout=5,
            conference_status_callback="https://example.com/conference_status_callback",
            conference_status_callback_event="start end join leave",
            conference_status_callback_method="GET",
            conference_trim="trim-silence",
            early_media=True,
            end_conference_on_exit=True,
            from_="+12065550200",
            machine_detection="Enable",
            machine_detection_silence_timeout=2000,
            machine_detection_speech_end_threshold=2000,
            machine_detection_speech_threshold=2000,
            machine_detection_timeout=1000,
            max_participants=30,
            muted=True,
            preferred_codecs="PCMA,PCMU",
            record=False,
            recording_channels="dual",
            recording_status_callback="https://example.com/recording_status_callback",
            recording_status_callback_event="in-progress completed absent",
            recording_status_callback_method="GET",
            recording_track="inbound",
            sip_auth_password="1234",
            sip_auth_username="user",
            start_conference_on_enter=False,
            status_callback="https://www.example.com/callback",
            status_callback_event="answered completed",
            status_callback_method="GET",
            time_limit=30,
            timeout_seconds=30,
            to="+12065550100",
            trim="trim-silence",
            wait_url="https://www.example.com/wait_music.mp3",
        )
        assert_matches_type(ParticipantParticipantsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_participants(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.conferences.participants.with_raw_response.participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantParticipantsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_participants(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.conferences.participants.with_streaming_response.participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantParticipantsResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_participants(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.conferences.participants.with_raw_response.participants(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            await async_client.texml.accounts.conferences.participants.with_raw_response.participants(
                conference_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_participants(self, async_client: AsyncTelnyx) -> None:
        participant = await async_client.texml.accounts.conferences.participants.retrieve_participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ParticipantRetrieveParticipantsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_participants(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.conferences.participants.with_raw_response.retrieve_participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantRetrieveParticipantsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_participants(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.conferences.participants.with_streaming_response.retrieve_participants(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantRetrieveParticipantsResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_participants(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.conferences.participants.with_raw_response.retrieve_participants(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            await async_client.texml.accounts.conferences.participants.with_raw_response.retrieve_participants(
                conference_sid="",
                account_sid="account_sid",
            )
