# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    CallDialResponse,
    CallRetrieveStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_dial(self, client: Telnyx) -> None:
        call = client.calls.dial(
            connection_id="7267xxxxxxxxxxxxxx",
            from_="+18005550101",
            to="+18005550100 or sip:username@sip.telnyx.com",
        )
        assert_matches_type(CallDialResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_dial_with_all_params(self, client: Telnyx) -> None:
        call = client.calls.dial(
            connection_id="7267xxxxxxxxxxxxxx",
            from_="+18005550101",
            to="+18005550100 or sip:username@sip.telnyx.com",
            answering_machine_detection="detect",
            answering_machine_detection_config={
                "after_greeting_silence_millis": 1000,
                "between_words_silence_millis": 1000,
                "greeting_duration_millis": 1000,
                "greeting_silence_duration_millis": 2000,
                "greeting_total_analysis_time_millis": 50000,
                "initial_silence_millis": 1000,
                "maximum_number_of_words": 1000,
                "maximum_word_length_millis": 2000,
                "silence_threshold": 512,
                "total_analysis_time_millis": 5000,
            },
            audio_url="http://www.example.com/sounds/greeting.wav",
            billing_group_id="f5586561-8ff0-4291-a0ac-84fe544797bd",
            bridge_intent=True,
            bridge_on_answer=True,
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            conference_config={
                "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "beep_enabled": "on_exit",
                "conference_name": "telnyx-conference",
                "early_media": False,
                "end_conference_on_exit": True,
                "hold": True,
                "hold_audio_url": "http://example.com/message.wav",
                "hold_media_name": "my_media_uploaded_to_media_storage_api",
                "mute": True,
                "soft_end_conference_on_exit": True,
                "start_conference_on_create": False,
                "start_conference_on_enter": True,
                "supervisor_role": "whisper",
                "whisper_call_control_ids": [
                    "v2:Sg1xxxQ_U3ixxxyXT_VDNI3xxxazZdg6Vxxxs4-GNYxxxVaJPOhFMRQ",
                    "v2:qqpb0mmvd-ovhhBr0BUQQn0fld5jIboaaX3-De0DkqXHzbf8d75xkw",
                ],
            },
            custom_headers=[
                {
                    "name": "head_1",
                    "value": "val_1",
                },
                {
                    "name": "head_2",
                    "value": "val_2",
                },
            ],
            dialogflow_config={
                "analyze_sentiment": False,
                "partial_automated_agent_reply": False,
            },
            enable_dialogflow=False,
            from_display_name="Company Name",
            link_to="ilditnZK_eVysupV21KzmzN_sM29ygfauQojpm4BgFtfX5hXAcjotg==",
            media_encryption="SRTP",
            media_name="my_media_uploaded_to_media_storage_api",
            preferred_codecs="G722,PCMU,PCMA,G729,OPUS,VP8,H264",
            record="record-from-answer",
            record_channels="single",
            record_custom_file_name="my_recording_file_name",
            record_format="wav",
            record_max_length=1000,
            record_timeout_secs=100,
            record_track="outbound",
            record_trim="trim-silence",
            send_silence_when_idle=True,
            sip_auth_password="password",
            sip_auth_username="username",
            sip_headers=[
                {
                    "name": "User-to-User",
                    "value": "12345",
                }
            ],
            sip_transport_protocol="TLS",
            sound_modifications={
                "octaves": 0.1,
                "pitch": 0,
                "semitone": -2,
                "track": "both",
            },
            stream_bidirectional_codec="G722",
            stream_bidirectional_mode="rtp",
            stream_bidirectional_sampling_rate=16000,
            stream_bidirectional_target_legs="both",
            stream_codec="PCMA",
            stream_establish_before_call_originate=True,
            stream_track="both_tracks",
            stream_url="wss://www.example.com/websocket",
            supervise_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            supervisor_role="barge",
            time_limit_secs=600,
            timeout_secs=60,
            transcription=True,
            transcription_config={
                "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
                "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
                "transcription_engine": "A",
                "transcription_engine_config": {
                    "enable_speaker_diarization": True,
                    "hints": ["Telnyx"],
                    "interim_results": True,
                    "language": "en",
                    "max_speaker_count": 4,
                    "min_speaker_count": 4,
                    "model": "latest_long",
                    "profanity_filter": True,
                    "speech_context": [
                        {
                            "boost": 1,
                            "phrases": ["Telnyx"],
                        }
                    ],
                    "transcription_engine": "A",
                    "use_enhanced": True,
                },
                "transcription_tracks": "both",
            },
            webhook_url="https://www.example.com/server-b/",
            webhook_url_method="POST",
        )
        assert_matches_type(CallDialResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_dial(self, client: Telnyx) -> None:
        response = client.calls.with_raw_response.dial(
            connection_id="7267xxxxxxxxxxxxxx",
            from_="+18005550101",
            to="+18005550100 or sip:username@sip.telnyx.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallDialResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_dial(self, client: Telnyx) -> None:
        with client.calls.with_streaming_response.dial(
            connection_id="7267xxxxxxxxxxxxxx",
            from_="+18005550101",
            to="+18005550100 or sip:username@sip.telnyx.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallDialResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: Telnyx) -> None:
        call = client.calls.retrieve_status(
            "call_control_id",
        )
        assert_matches_type(CallRetrieveStatusResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: Telnyx) -> None:
        response = client.calls.with_raw_response.retrieve_status(
            "call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallRetrieveStatusResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Telnyx) -> None:
        with client.calls.with_streaming_response.retrieve_status(
            "call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallRetrieveStatusResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.with_raw_response.retrieve_status(
                "",
            )


class TestAsyncCalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_dial(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.calls.dial(
            connection_id="7267xxxxxxxxxxxxxx",
            from_="+18005550101",
            to="+18005550100 or sip:username@sip.telnyx.com",
        )
        assert_matches_type(CallDialResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_dial_with_all_params(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.calls.dial(
            connection_id="7267xxxxxxxxxxxxxx",
            from_="+18005550101",
            to="+18005550100 or sip:username@sip.telnyx.com",
            answering_machine_detection="detect",
            answering_machine_detection_config={
                "after_greeting_silence_millis": 1000,
                "between_words_silence_millis": 1000,
                "greeting_duration_millis": 1000,
                "greeting_silence_duration_millis": 2000,
                "greeting_total_analysis_time_millis": 50000,
                "initial_silence_millis": 1000,
                "maximum_number_of_words": 1000,
                "maximum_word_length_millis": 2000,
                "silence_threshold": 512,
                "total_analysis_time_millis": 5000,
            },
            audio_url="http://www.example.com/sounds/greeting.wav",
            billing_group_id="f5586561-8ff0-4291-a0ac-84fe544797bd",
            bridge_intent=True,
            bridge_on_answer=True,
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            conference_config={
                "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "beep_enabled": "on_exit",
                "conference_name": "telnyx-conference",
                "early_media": False,
                "end_conference_on_exit": True,
                "hold": True,
                "hold_audio_url": "http://example.com/message.wav",
                "hold_media_name": "my_media_uploaded_to_media_storage_api",
                "mute": True,
                "soft_end_conference_on_exit": True,
                "start_conference_on_create": False,
                "start_conference_on_enter": True,
                "supervisor_role": "whisper",
                "whisper_call_control_ids": [
                    "v2:Sg1xxxQ_U3ixxxyXT_VDNI3xxxazZdg6Vxxxs4-GNYxxxVaJPOhFMRQ",
                    "v2:qqpb0mmvd-ovhhBr0BUQQn0fld5jIboaaX3-De0DkqXHzbf8d75xkw",
                ],
            },
            custom_headers=[
                {
                    "name": "head_1",
                    "value": "val_1",
                },
                {
                    "name": "head_2",
                    "value": "val_2",
                },
            ],
            dialogflow_config={
                "analyze_sentiment": False,
                "partial_automated_agent_reply": False,
            },
            enable_dialogflow=False,
            from_display_name="Company Name",
            link_to="ilditnZK_eVysupV21KzmzN_sM29ygfauQojpm4BgFtfX5hXAcjotg==",
            media_encryption="SRTP",
            media_name="my_media_uploaded_to_media_storage_api",
            preferred_codecs="G722,PCMU,PCMA,G729,OPUS,VP8,H264",
            record="record-from-answer",
            record_channels="single",
            record_custom_file_name="my_recording_file_name",
            record_format="wav",
            record_max_length=1000,
            record_timeout_secs=100,
            record_track="outbound",
            record_trim="trim-silence",
            send_silence_when_idle=True,
            sip_auth_password="password",
            sip_auth_username="username",
            sip_headers=[
                {
                    "name": "User-to-User",
                    "value": "12345",
                }
            ],
            sip_transport_protocol="TLS",
            sound_modifications={
                "octaves": 0.1,
                "pitch": 0,
                "semitone": -2,
                "track": "both",
            },
            stream_bidirectional_codec="G722",
            stream_bidirectional_mode="rtp",
            stream_bidirectional_sampling_rate=16000,
            stream_bidirectional_target_legs="both",
            stream_codec="PCMA",
            stream_establish_before_call_originate=True,
            stream_track="both_tracks",
            stream_url="wss://www.example.com/websocket",
            supervise_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            supervisor_role="barge",
            time_limit_secs=600,
            timeout_secs=60,
            transcription=True,
            transcription_config={
                "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
                "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
                "transcription_engine": "A",
                "transcription_engine_config": {
                    "enable_speaker_diarization": True,
                    "hints": ["Telnyx"],
                    "interim_results": True,
                    "language": "en",
                    "max_speaker_count": 4,
                    "min_speaker_count": 4,
                    "model": "latest_long",
                    "profanity_filter": True,
                    "speech_context": [
                        {
                            "boost": 1,
                            "phrases": ["Telnyx"],
                        }
                    ],
                    "transcription_engine": "A",
                    "use_enhanced": True,
                },
                "transcription_tracks": "both",
            },
            webhook_url="https://www.example.com/server-b/",
            webhook_url_method="POST",
        )
        assert_matches_type(CallDialResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_dial(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.with_raw_response.dial(
            connection_id="7267xxxxxxxxxxxxxx",
            from_="+18005550101",
            to="+18005550100 or sip:username@sip.telnyx.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallDialResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_dial(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.with_streaming_response.dial(
            connection_id="7267xxxxxxxxxxxxxx",
            from_="+18005550101",
            to="+18005550100 or sip:username@sip.telnyx.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallDialResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.calls.retrieve_status(
            "call_control_id",
        )
        assert_matches_type(CallRetrieveStatusResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.with_raw_response.retrieve_status(
            "call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallRetrieveStatusResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.with_streaming_response.retrieve_status(
            "call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallRetrieveStatusResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.with_raw_response.retrieve_status(
                "",
            )
