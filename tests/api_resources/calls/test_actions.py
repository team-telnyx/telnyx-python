# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.calls import (
    ActionReferResponse,
    ActionSpeakResponse,
    ActionAnswerResponse,
    ActionBridgeResponse,
    ActionGatherResponse,
    ActionHangupResponse,
    ActionRejectResponse,
    ActionEnqueueResponse,
    ActionSendDtmfResponse,
    ActionTransferResponse,
    ActionLeaveQueueResponse,
    ActionStopGatherResponse,
    ActionStopSiprecResponse,
    ActionSendSipInfoResponse,
    ActionStartSiprecResponse,
    ActionStopForkingResponse,
    ActionStartForkingResponse,
    ActionStopPlaybackResponse,
    ActionGatherUsingAIResponse,
    ActionStartPlaybackResponse,
    ActionStopRecordingResponse,
    ActionStopStreamingResponse,
    ActionPauseRecordingResponse,
    ActionStartRecordingResponse,
    ActionStartStreamingResponse,
    ActionResumeRecordingResponse,
    ActionStopAIAssistantResponse,
    ActionGatherUsingAudioResponse,
    ActionGatherUsingSpeakResponse,
    ActionStartAIAssistantResponse,
    ActionStopTranscriptionResponse,
    ActionUpdateClientStateResponse,
    ActionStartTranscriptionResponse,
    ActionStopNoiseSuppressionResponse,
    ActionSwitchSupervisorRoleResponse,
    ActionStartNoiseSuppressionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_answer(self, client: Telnyx) -> None:
        action = client.calls.actions.answer(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionAnswerResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_answer_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.answer(
            call_control_id="call_control_id",
            billing_group_id="f5586561-8ff0-4291-a0ac-84fe544797bd",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
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
            sip_headers=[
                {
                    "name": "User-to-User",
                    "value": "value",
                }
            ],
            sound_modifications={
                "octaves": 0.1,
                "pitch": 0,
                "semitone": -2,
                "track": "both",
            },
            stream_bidirectional_codec="G722",
            stream_bidirectional_mode="rtp",
            stream_bidirectional_target_legs="both",
            stream_codec="PCMA",
            stream_track="both_tracks",
            stream_url="wss://www.example.com/websocket",
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
        assert_matches_type(ActionAnswerResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_answer(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.answer(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionAnswerResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_answer(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.answer(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionAnswerResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_answer(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.answer(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bridge(self, client: Telnyx) -> None:
        action = client.calls.actions.bridge(
            path_call_control_id="call_control_id",
            body_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        )
        assert_matches_type(ActionBridgeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bridge_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.bridge(
            path_call_control_id="call_control_id",
            body_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            mute_dtmf="opposite",
            park_after_unbridge="self",
            play_ringtone=True,
            queue="support",
            record="record-from-answer",
            record_channels="single",
            record_custom_file_name="my_recording_file_name",
            record_format="wav",
            record_max_length=1000,
            record_timeout_secs=100,
            record_track="outbound",
            record_trim="trim-silence",
            ringtone="pl",
            video_room_context="Alice",
            video_room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(ActionBridgeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bridge(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.bridge(
            path_call_control_id="call_control_id",
            body_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionBridgeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bridge(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.bridge(
            path_call_control_id="call_control_id",
            body_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionBridgeResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_bridge(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_call_control_id` but received ''"):
            client.calls.actions.with_raw_response.bridge(
                path_call_control_id="",
                body_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enqueue(self, client: Telnyx) -> None:
        action = client.calls.actions.enqueue(
            call_control_id="call_control_id",
            queue_name="support",
        )
        assert_matches_type(ActionEnqueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enqueue_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.enqueue(
            call_control_id="call_control_id",
            queue_name="support",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            max_size=20,
            max_wait_time_secs=600,
        )
        assert_matches_type(ActionEnqueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_enqueue(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.enqueue(
            call_control_id="call_control_id",
            queue_name="support",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionEnqueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_enqueue(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.enqueue(
            call_control_id="call_control_id",
            queue_name="support",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionEnqueueResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_enqueue(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.enqueue(
                call_control_id="",
                queue_name="support",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_gather(self, client: Telnyx) -> None:
        action = client.calls.actions.gather(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_gather_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.gather(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            gather_id="my_gather_id",
            initial_timeout_millis=10000,
            inter_digit_timeout_millis=10000,
            maximum_digits=10,
            minimum_digits=1,
            terminating_digit="#",
            timeout_millis=60000,
            valid_digits="123",
        )
        assert_matches_type(ActionGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_gather(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.gather(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_gather(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.gather(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionGatherResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_gather(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.gather(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_gather_using_ai(self, client: Telnyx) -> None:
        action = client.calls.actions.gather_using_ai(
            call_control_id="call_control_id",
            parameters={
                "properties": {
                    "age": {
                        "description": "The age of the customer.",
                        "type": "integer",
                    },
                    "location": {
                        "description": "The location of the customer.",
                        "type": "string",
                    },
                },
                "required": ["age", "location"],
                "type": "object",
            },
        )
        assert_matches_type(ActionGatherUsingAIResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_gather_using_ai_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.gather_using_ai(
            call_control_id="call_control_id",
            parameters={
                "properties": {
                    "age": {
                        "description": "The age of the customer.",
                        "type": "integer",
                    },
                    "location": {
                        "description": "The location of the customer.",
                        "type": "string",
                    },
                },
                "required": ["age", "location"],
                "type": "object",
            },
            assistant={
                "instructions": "You are a friendly voice assistant.",
                "model": "meta-llama/Meta-Llama-3.1-70B-Instruct",
                "openai_api_key_ref": "my_openai_api_key",
                "tools": [
                    {
                        "book_appointment": {
                            "api_key_ref": "my_calcom_api_key",
                            "event_type_id": 0,
                            "attendee_name": "attendee_name",
                            "attendee_timezone": "attendee_timezone",
                        },
                        "type": "book_appointment",
                    }
                ],
            },
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            greeting="Hello, can you tell me your age and where you live?",
            interruption_settings={"enable": True},
            language="en",
            message_history=[
                {
                    "content": "Hello, what's your name?",
                    "role": "assistant",
                },
                {
                    "content": "Hello, I'm John.",
                    "role": "user",
                },
            ],
            send_message_history_updates=True,
            send_partial_results=True,
            transcription={"model": "distil-whisper/distil-large-v2"},
            user_response_timeout_ms=5000,
            voice="Telnyx.KokoroTTS.af",
            voice_settings={"api_key_ref": "my_elevenlabs_api_key"},
        )
        assert_matches_type(ActionGatherUsingAIResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_gather_using_ai(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.gather_using_ai(
            call_control_id="call_control_id",
            parameters={
                "properties": {
                    "age": {
                        "description": "The age of the customer.",
                        "type": "integer",
                    },
                    "location": {
                        "description": "The location of the customer.",
                        "type": "string",
                    },
                },
                "required": ["age", "location"],
                "type": "object",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionGatherUsingAIResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_gather_using_ai(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.gather_using_ai(
            call_control_id="call_control_id",
            parameters={
                "properties": {
                    "age": {
                        "description": "The age of the customer.",
                        "type": "integer",
                    },
                    "location": {
                        "description": "The location of the customer.",
                        "type": "string",
                    },
                },
                "required": ["age", "location"],
                "type": "object",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionGatherUsingAIResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_gather_using_ai(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.gather_using_ai(
                call_control_id="",
                parameters={
                    "properties": {
                        "age": {
                            "description": "The age of the customer.",
                            "type": "integer",
                        },
                        "location": {
                            "description": "The location of the customer.",
                            "type": "string",
                        },
                    },
                    "required": ["age", "location"],
                    "type": "object",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_gather_using_audio(self, client: Telnyx) -> None:
        action = client.calls.actions.gather_using_audio(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionGatherUsingAudioResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_gather_using_audio_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.gather_using_audio(
            call_control_id="call_control_id",
            audio_url="http://example.com/message.wav",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            inter_digit_timeout_millis=10000,
            invalid_audio_url="http://example.com/message.wav",
            invalid_media_name="my_media_uploaded_to_media_storage_api",
            maximum_digits=10,
            maximum_tries=3,
            media_name="my_media_uploaded_to_media_storage_api",
            minimum_digits=1,
            terminating_digit="#",
            timeout_millis=10000,
            valid_digits="123",
        )
        assert_matches_type(ActionGatherUsingAudioResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_gather_using_audio(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.gather_using_audio(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionGatherUsingAudioResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_gather_using_audio(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.gather_using_audio(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionGatherUsingAudioResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_gather_using_audio(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.gather_using_audio(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_gather_using_speak(self, client: Telnyx) -> None:
        action = client.calls.actions.gather_using_speak(
            call_control_id="call_control_id",
            payload="say this on call",
            voice="male",
        )
        assert_matches_type(ActionGatherUsingSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_gather_using_speak_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.gather_using_speak(
            call_control_id="call_control_id",
            payload="say this on call",
            voice="male",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            inter_digit_timeout_millis=10000,
            invalid_payload="say this on call",
            language="arb",
            maximum_digits=10,
            maximum_tries=3,
            minimum_digits=1,
            payload_type="text",
            service_level="premium",
            terminating_digit="#",
            timeout_millis=60000,
            valid_digits="123",
            voice_settings={"api_key_ref": "my_elevenlabs_api_key"},
        )
        assert_matches_type(ActionGatherUsingSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_gather_using_speak(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.gather_using_speak(
            call_control_id="call_control_id",
            payload="say this on call",
            voice="male",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionGatherUsingSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_gather_using_speak(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.gather_using_speak(
            call_control_id="call_control_id",
            payload="say this on call",
            voice="male",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionGatherUsingSpeakResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_gather_using_speak(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.gather_using_speak(
                call_control_id="",
                payload="say this on call",
                voice="male",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_hangup(self, client: Telnyx) -> None:
        action = client.calls.actions.hangup(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionHangupResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_hangup_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.hangup(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionHangupResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_hangup(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.hangup(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionHangupResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_hangup(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.hangup(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionHangupResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_hangup(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.hangup(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_leave_queue(self, client: Telnyx) -> None:
        action = client.calls.actions.leave_queue(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionLeaveQueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_leave_queue_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.leave_queue(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionLeaveQueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_leave_queue(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.leave_queue(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionLeaveQueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_leave_queue(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.leave_queue(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionLeaveQueueResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_leave_queue(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.leave_queue(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_pause_recording(self, client: Telnyx) -> None:
        action = client.calls.actions.pause_recording(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionPauseRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_pause_recording_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.pause_recording(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="6e00ab49-9487-4364-8ad6-23965965afb2",
        )
        assert_matches_type(ActionPauseRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_pause_recording(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.pause_recording(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionPauseRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_pause_recording(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.pause_recording(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionPauseRecordingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_pause_recording(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.pause_recording(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refer(self, client: Telnyx) -> None:
        action = client.calls.actions.refer(
            call_control_id="call_control_id",
            sip_address="sip:username@sip.non-telnyx-address.com",
        )
        assert_matches_type(ActionReferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refer_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.refer(
            call_control_id="call_control_id",
            sip_address="sip:username@sip.non-telnyx-address.com",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
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
            sip_auth_password="sip_auth_password",
            sip_auth_username="sip_auth_username",
            sip_headers=[
                {
                    "name": "User-to-User",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(ActionReferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_refer(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.refer(
            call_control_id="call_control_id",
            sip_address="sip:username@sip.non-telnyx-address.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionReferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_refer(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.refer(
            call_control_id="call_control_id",
            sip_address="sip:username@sip.non-telnyx-address.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionReferResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_refer(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.refer(
                call_control_id="",
                sip_address="sip:username@sip.non-telnyx-address.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reject(self, client: Telnyx) -> None:
        action = client.calls.actions.reject(
            call_control_id="call_control_id",
            cause="USER_BUSY",
        )
        assert_matches_type(ActionRejectResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reject_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.reject(
            call_control_id="call_control_id",
            cause="USER_BUSY",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionRejectResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reject(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.reject(
            call_control_id="call_control_id",
            cause="USER_BUSY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRejectResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reject(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.reject(
            call_control_id="call_control_id",
            cause="USER_BUSY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRejectResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reject(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.reject(
                call_control_id="",
                cause="USER_BUSY",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resume_recording(self, client: Telnyx) -> None:
        action = client.calls.actions.resume_recording(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionResumeRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resume_recording_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.resume_recording(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="6e00ab49-9487-4364-8ad6-23965965afb2",
        )
        assert_matches_type(ActionResumeRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resume_recording(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.resume_recording(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionResumeRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resume_recording(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.resume_recording(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionResumeRecordingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resume_recording(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.resume_recording(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_dtmf(self, client: Telnyx) -> None:
        action = client.calls.actions.send_dtmf(
            call_control_id="call_control_id",
            digits="1www2WABCDw9",
        )
        assert_matches_type(ActionSendDtmfResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_dtmf_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.send_dtmf(
            call_control_id="call_control_id",
            digits="1www2WABCDw9",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            duration_millis=500,
        )
        assert_matches_type(ActionSendDtmfResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_dtmf(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.send_dtmf(
            call_control_id="call_control_id",
            digits="1www2WABCDw9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionSendDtmfResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_dtmf(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.send_dtmf(
            call_control_id="call_control_id",
            digits="1www2WABCDw9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionSendDtmfResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_send_dtmf(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.send_dtmf(
                call_control_id="",
                digits="1www2WABCDw9",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_sip_info(self, client: Telnyx) -> None:
        action = client.calls.actions.send_sip_info(
            call_control_id="call_control_id",
            body='{"key": "value", "numValue": 100}',
            content_type="application/json",
        )
        assert_matches_type(ActionSendSipInfoResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_sip_info_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.send_sip_info(
            call_control_id="call_control_id",
            body='{"key": "value", "numValue": 100}',
            content_type="application/json",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionSendSipInfoResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_sip_info(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.send_sip_info(
            call_control_id="call_control_id",
            body='{"key": "value", "numValue": 100}',
            content_type="application/json",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionSendSipInfoResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_sip_info(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.send_sip_info(
            call_control_id="call_control_id",
            body='{"key": "value", "numValue": 100}',
            content_type="application/json",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionSendSipInfoResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_send_sip_info(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.send_sip_info(
                call_control_id="",
                body='{"key": "value", "numValue": 100}',
                content_type="application/json",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_speak(self, client: Telnyx) -> None:
        action = client.calls.actions.speak(
            call_control_id="call_control_id",
            payload="Say this on the call",
            voice="female",
        )
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_speak_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.speak(
            call_control_id="call_control_id",
            payload="Say this on the call",
            voice="female",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            language="arb",
            payload_type="text",
            service_level="basic",
            stop="current",
            voice_settings={"api_key_ref": "my_elevenlabs_api_key"},
        )
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_speak(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.speak(
            call_control_id="call_control_id",
            payload="Say this on the call",
            voice="female",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_speak(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.speak(
            call_control_id="call_control_id",
            payload="Say this on the call",
            voice="female",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionSpeakResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_speak(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.speak(
                call_control_id="",
                payload="Say this on the call",
                voice="female",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_ai_assistant(self, client: Telnyx) -> None:
        action = client.calls.actions.start_ai_assistant(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_ai_assistant_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.start_ai_assistant(
            call_control_id="call_control_id",
            assistant={
                "id": "id",
                "instructions": "You are a friendly voice assistant.",
                "openai_api_key_ref": "openai_api_key_ref",
            },
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            greeting="Hello, can you tell me your age and where you live?",
            interruption_settings={"enable": True},
            transcription={"model": "distil-whisper/distil-large-v2"},
            voice="Telnyx.KokoroTTS.af",
            voice_settings={"api_key_ref": "my_elevenlabs_api_key"},
        )
        assert_matches_type(ActionStartAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start_ai_assistant(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.start_ai_assistant(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStartAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start_ai_assistant(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.start_ai_assistant(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStartAIAssistantResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_start_ai_assistant(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.start_ai_assistant(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_forking(self, client: Telnyx) -> None:
        action = client.calls.actions.start_forking(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_forking_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.start_forking(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            rx="udp:192.0.2.1:9000",
            stream_type="decrypted",
            tx="udp:192.0.2.1:9001",
        )
        assert_matches_type(ActionStartForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start_forking(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.start_forking(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStartForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start_forking(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.start_forking(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStartForkingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_start_forking(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.start_forking(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_noise_suppression(self, client: Telnyx) -> None:
        action = client.calls.actions.start_noise_suppression(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_noise_suppression_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.start_noise_suppression(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            direction="both",
            noise_suppression_engine="A",
        )
        assert_matches_type(ActionStartNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start_noise_suppression(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.start_noise_suppression(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStartNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start_noise_suppression(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.start_noise_suppression(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStartNoiseSuppressionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_start_noise_suppression(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.start_noise_suppression(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_playback(self, client: Telnyx) -> None:
        action = client.calls.actions.start_playback(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_playback_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.start_playback(
            call_control_id="call_control_id",
            audio_type="wav",
            audio_url="http://www.example.com/sounds/greeting.wav",
            cache_audio=True,
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            loop="infinity",
            media_name="my_media_uploaded_to_media_storage_api",
            overlay=True,
            playback_content="SUQzAwAAAAADf1...",
            stop="current",
            target_legs="self",
        )
        assert_matches_type(ActionStartPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start_playback(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.start_playback(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStartPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start_playback(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.start_playback(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStartPlaybackResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_start_playback(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.start_playback(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_recording(self, client: Telnyx) -> None:
        action = client.calls.actions.start_recording(
            call_control_id="call_control_id",
            channels="single",
            format="wav",
        )
        assert_matches_type(ActionStartRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_recording_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.start_recording(
            call_control_id="call_control_id",
            channels="single",
            format="wav",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            custom_file_name="my_recording_file_name",
            max_length=0,
            play_beep=True,
            recording_track="outbound",
            timeout_secs=0,
            transcription=True,
            transcription_engine="B",
            transcription_language="en-US",
            transcription_max_speaker_count=4,
            transcription_min_speaker_count=4,
            transcription_profanity_filter=True,
            transcription_speaker_diarization=True,
            trim="trim-silence",
        )
        assert_matches_type(ActionStartRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start_recording(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.start_recording(
            call_control_id="call_control_id",
            channels="single",
            format="wav",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStartRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start_recording(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.start_recording(
            call_control_id="call_control_id",
            channels="single",
            format="wav",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStartRecordingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_start_recording(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.start_recording(
                call_control_id="",
                channels="single",
                format="wav",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_siprec(self, client: Telnyx) -> None:
        action = client.calls.actions.start_siprec(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_siprec_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.start_siprec(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            connector_name="my-siprec-connector",
            include_metadata_custom_headers=True,
            secure=True,
            session_timeout_secs=900,
            sip_transport="tcp",
            siprec_track="both_tracks",
        )
        assert_matches_type(ActionStartSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start_siprec(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.start_siprec(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStartSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start_siprec(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.start_siprec(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStartSiprecResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_start_siprec(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.start_siprec(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_streaming(self, client: Telnyx) -> None:
        action = client.calls.actions.start_streaming(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_streaming_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.start_streaming(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            dialogflow_config={
                "analyze_sentiment": False,
                "partial_automated_agent_reply": False,
            },
            enable_dialogflow=False,
            stream_bidirectional_codec="G722",
            stream_bidirectional_mode="rtp",
            stream_bidirectional_target_legs="both",
            stream_codec="PCMA",
            stream_track="both_tracks",
            stream_url="wss://www.example.com/websocket",
        )
        assert_matches_type(ActionStartStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start_streaming(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.start_streaming(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStartStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start_streaming(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.start_streaming(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStartStreamingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_start_streaming(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.start_streaming(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_transcription(self, client: Telnyx) -> None:
        action = client.calls.actions.start_transcription(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_transcription_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.start_transcription(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            transcription_engine="A",
            transcription_engine_config={
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
            transcription_tracks="both",
        )
        assert_matches_type(ActionStartTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start_transcription(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.start_transcription(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStartTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start_transcription(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.start_transcription(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStartTranscriptionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_start_transcription(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.start_transcription(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_ai_assistant(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_ai_assistant(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_ai_assistant_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_ai_assistant(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionStopAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop_ai_assistant(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.stop_ai_assistant(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStopAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop_ai_assistant(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.stop_ai_assistant(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStopAIAssistantResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stop_ai_assistant(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.stop_ai_assistant(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_forking(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_forking(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_forking_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_forking(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            stream_type="decrypted",
        )
        assert_matches_type(ActionStopForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop_forking(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.stop_forking(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStopForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop_forking(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.stop_forking(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStopForkingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stop_forking(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.stop_forking(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_gather(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_gather(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_gather_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_gather(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionStopGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop_gather(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.stop_gather(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStopGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop_gather(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.stop_gather(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStopGatherResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stop_gather(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.stop_gather(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_noise_suppression(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_noise_suppression(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_noise_suppression_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_noise_suppression(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionStopNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop_noise_suppression(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.stop_noise_suppression(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStopNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop_noise_suppression(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.stop_noise_suppression(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStopNoiseSuppressionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stop_noise_suppression(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.stop_noise_suppression(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_playback(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_playback(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_playback_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_playback(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            overlay=False,
            stop="all",
        )
        assert_matches_type(ActionStopPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop_playback(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.stop_playback(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStopPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop_playback(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.stop_playback(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStopPlaybackResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stop_playback(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.stop_playback(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_recording(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_recording(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_recording_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_recording(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="6e00ab49-9487-4364-8ad6-23965965afb2",
        )
        assert_matches_type(ActionStopRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop_recording(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.stop_recording(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStopRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop_recording(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.stop_recording(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStopRecordingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stop_recording(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.stop_recording(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_siprec(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_siprec(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_siprec_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_siprec(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionStopSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop_siprec(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.stop_siprec(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStopSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop_siprec(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.stop_siprec(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStopSiprecResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stop_siprec(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.stop_siprec(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_streaming(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_streaming(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_streaming_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_streaming(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            stream_id="1edb94f9-7ef0-4150-b502-e0ebadfd9491",
        )
        assert_matches_type(ActionStopStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop_streaming(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.stop_streaming(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStopStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop_streaming(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.stop_streaming(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStopStreamingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stop_streaming(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.stop_streaming(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_transcription(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_transcription(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_transcription_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.stop_transcription(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionStopTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop_transcription(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.stop_transcription(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStopTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop_transcription(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.stop_transcription(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStopTranscriptionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stop_transcription(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.stop_transcription(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_switch_supervisor_role(self, client: Telnyx) -> None:
        action = client.calls.actions.switch_supervisor_role(
            call_control_id="call_control_id",
            role="barge",
        )
        assert_matches_type(ActionSwitchSupervisorRoleResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_switch_supervisor_role(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.switch_supervisor_role(
            call_control_id="call_control_id",
            role="barge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionSwitchSupervisorRoleResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_switch_supervisor_role(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.switch_supervisor_role(
            call_control_id="call_control_id",
            role="barge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionSwitchSupervisorRoleResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_switch_supervisor_role(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.switch_supervisor_role(
                call_control_id="",
                role="barge",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_transfer(self, client: Telnyx) -> None:
        action = client.calls.actions.transfer(
            call_control_id="call_control_id",
            to="+18005550100 or sip:username@sip.telnyx.com",
        )
        assert_matches_type(ActionTransferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_transfer_with_all_params(self, client: Telnyx) -> None:
        action = client.calls.actions.transfer(
            call_control_id="call_control_id",
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
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
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
            early_media=True,
            from_="+18005550101",
            from_display_name="Company Name",
            media_encryption="SRTP",
            media_name="my_media_uploaded_to_media_storage_api",
            mute_dtmf="opposite",
            park_after_unbridge="self",
            sip_auth_password="password",
            sip_auth_username="username",
            sip_headers=[
                {
                    "name": "User-to-User",
                    "value": "value",
                }
            ],
            sip_transport_protocol="TLS",
            sound_modifications={
                "octaves": 0.1,
                "pitch": 0,
                "semitone": -2,
                "track": "both",
            },
            target_leg_client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            time_limit_secs=600,
            timeout_secs=60,
            webhook_url="https://www.example.com/server-b/",
            webhook_url_method="POST",
        )
        assert_matches_type(ActionTransferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_transfer(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.transfer(
            call_control_id="call_control_id",
            to="+18005550100 or sip:username@sip.telnyx.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionTransferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_transfer(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.transfer(
            call_control_id="call_control_id",
            to="+18005550100 or sip:username@sip.telnyx.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionTransferResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_transfer(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.transfer(
                call_control_id="",
                to="+18005550100 or sip:username@sip.telnyx.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_client_state(self, client: Telnyx) -> None:
        action = client.calls.actions.update_client_state(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
        )
        assert_matches_type(ActionUpdateClientStateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_client_state(self, client: Telnyx) -> None:
        response = client.calls.actions.with_raw_response.update_client_state(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionUpdateClientStateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_client_state(self, client: Telnyx) -> None:
        with client.calls.actions.with_streaming_response.update_client_state(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionUpdateClientStateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_client_state(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            client.calls.actions.with_raw_response.update_client_state(
                call_control_id="",
                client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_answer(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.answer(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionAnswerResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_answer_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.answer(
            call_control_id="call_control_id",
            billing_group_id="f5586561-8ff0-4291-a0ac-84fe544797bd",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
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
            sip_headers=[
                {
                    "name": "User-to-User",
                    "value": "value",
                }
            ],
            sound_modifications={
                "octaves": 0.1,
                "pitch": 0,
                "semitone": -2,
                "track": "both",
            },
            stream_bidirectional_codec="G722",
            stream_bidirectional_mode="rtp",
            stream_bidirectional_target_legs="both",
            stream_codec="PCMA",
            stream_track="both_tracks",
            stream_url="wss://www.example.com/websocket",
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
        assert_matches_type(ActionAnswerResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_answer(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.answer(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionAnswerResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_answer(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.answer(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionAnswerResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_answer(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.answer(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bridge(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.bridge(
            path_call_control_id="call_control_id",
            body_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        )
        assert_matches_type(ActionBridgeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bridge_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.bridge(
            path_call_control_id="call_control_id",
            body_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            mute_dtmf="opposite",
            park_after_unbridge="self",
            play_ringtone=True,
            queue="support",
            record="record-from-answer",
            record_channels="single",
            record_custom_file_name="my_recording_file_name",
            record_format="wav",
            record_max_length=1000,
            record_timeout_secs=100,
            record_track="outbound",
            record_trim="trim-silence",
            ringtone="pl",
            video_room_context="Alice",
            video_room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(ActionBridgeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bridge(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.bridge(
            path_call_control_id="call_control_id",
            body_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionBridgeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bridge(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.bridge(
            path_call_control_id="call_control_id",
            body_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionBridgeResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_bridge(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.bridge(
                path_call_control_id="",
                body_call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enqueue(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.enqueue(
            call_control_id="call_control_id",
            queue_name="support",
        )
        assert_matches_type(ActionEnqueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enqueue_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.enqueue(
            call_control_id="call_control_id",
            queue_name="support",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            max_size=20,
            max_wait_time_secs=600,
        )
        assert_matches_type(ActionEnqueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_enqueue(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.enqueue(
            call_control_id="call_control_id",
            queue_name="support",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionEnqueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_enqueue(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.enqueue(
            call_control_id="call_control_id",
            queue_name="support",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionEnqueueResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_enqueue(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.enqueue(
                call_control_id="",
                queue_name="support",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_gather(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.gather(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_gather_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.gather(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            gather_id="my_gather_id",
            initial_timeout_millis=10000,
            inter_digit_timeout_millis=10000,
            maximum_digits=10,
            minimum_digits=1,
            terminating_digit="#",
            timeout_millis=60000,
            valid_digits="123",
        )
        assert_matches_type(ActionGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_gather(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.gather(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_gather(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.gather(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionGatherResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_gather(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.gather(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_gather_using_ai(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.gather_using_ai(
            call_control_id="call_control_id",
            parameters={
                "properties": {
                    "age": {
                        "description": "The age of the customer.",
                        "type": "integer",
                    },
                    "location": {
                        "description": "The location of the customer.",
                        "type": "string",
                    },
                },
                "required": ["age", "location"],
                "type": "object",
            },
        )
        assert_matches_type(ActionGatherUsingAIResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_gather_using_ai_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.gather_using_ai(
            call_control_id="call_control_id",
            parameters={
                "properties": {
                    "age": {
                        "description": "The age of the customer.",
                        "type": "integer",
                    },
                    "location": {
                        "description": "The location of the customer.",
                        "type": "string",
                    },
                },
                "required": ["age", "location"],
                "type": "object",
            },
            assistant={
                "instructions": "You are a friendly voice assistant.",
                "model": "meta-llama/Meta-Llama-3.1-70B-Instruct",
                "openai_api_key_ref": "my_openai_api_key",
                "tools": [
                    {
                        "book_appointment": {
                            "api_key_ref": "my_calcom_api_key",
                            "event_type_id": 0,
                            "attendee_name": "attendee_name",
                            "attendee_timezone": "attendee_timezone",
                        },
                        "type": "book_appointment",
                    }
                ],
            },
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            greeting="Hello, can you tell me your age and where you live?",
            interruption_settings={"enable": True},
            language="en",
            message_history=[
                {
                    "content": "Hello, what's your name?",
                    "role": "assistant",
                },
                {
                    "content": "Hello, I'm John.",
                    "role": "user",
                },
            ],
            send_message_history_updates=True,
            send_partial_results=True,
            transcription={"model": "distil-whisper/distil-large-v2"},
            user_response_timeout_ms=5000,
            voice="Telnyx.KokoroTTS.af",
            voice_settings={"api_key_ref": "my_elevenlabs_api_key"},
        )
        assert_matches_type(ActionGatherUsingAIResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_gather_using_ai(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.gather_using_ai(
            call_control_id="call_control_id",
            parameters={
                "properties": {
                    "age": {
                        "description": "The age of the customer.",
                        "type": "integer",
                    },
                    "location": {
                        "description": "The location of the customer.",
                        "type": "string",
                    },
                },
                "required": ["age", "location"],
                "type": "object",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionGatherUsingAIResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_gather_using_ai(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.gather_using_ai(
            call_control_id="call_control_id",
            parameters={
                "properties": {
                    "age": {
                        "description": "The age of the customer.",
                        "type": "integer",
                    },
                    "location": {
                        "description": "The location of the customer.",
                        "type": "string",
                    },
                },
                "required": ["age", "location"],
                "type": "object",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionGatherUsingAIResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_gather_using_ai(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.gather_using_ai(
                call_control_id="",
                parameters={
                    "properties": {
                        "age": {
                            "description": "The age of the customer.",
                            "type": "integer",
                        },
                        "location": {
                            "description": "The location of the customer.",
                            "type": "string",
                        },
                    },
                    "required": ["age", "location"],
                    "type": "object",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_gather_using_audio(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.gather_using_audio(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionGatherUsingAudioResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_gather_using_audio_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.gather_using_audio(
            call_control_id="call_control_id",
            audio_url="http://example.com/message.wav",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            inter_digit_timeout_millis=10000,
            invalid_audio_url="http://example.com/message.wav",
            invalid_media_name="my_media_uploaded_to_media_storage_api",
            maximum_digits=10,
            maximum_tries=3,
            media_name="my_media_uploaded_to_media_storage_api",
            minimum_digits=1,
            terminating_digit="#",
            timeout_millis=10000,
            valid_digits="123",
        )
        assert_matches_type(ActionGatherUsingAudioResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_gather_using_audio(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.gather_using_audio(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionGatherUsingAudioResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_gather_using_audio(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.gather_using_audio(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionGatherUsingAudioResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_gather_using_audio(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.gather_using_audio(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_gather_using_speak(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.gather_using_speak(
            call_control_id="call_control_id",
            payload="say this on call",
            voice="male",
        )
        assert_matches_type(ActionGatherUsingSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_gather_using_speak_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.gather_using_speak(
            call_control_id="call_control_id",
            payload="say this on call",
            voice="male",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            inter_digit_timeout_millis=10000,
            invalid_payload="say this on call",
            language="arb",
            maximum_digits=10,
            maximum_tries=3,
            minimum_digits=1,
            payload_type="text",
            service_level="premium",
            terminating_digit="#",
            timeout_millis=60000,
            valid_digits="123",
            voice_settings={"api_key_ref": "my_elevenlabs_api_key"},
        )
        assert_matches_type(ActionGatherUsingSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_gather_using_speak(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.gather_using_speak(
            call_control_id="call_control_id",
            payload="say this on call",
            voice="male",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionGatherUsingSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_gather_using_speak(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.gather_using_speak(
            call_control_id="call_control_id",
            payload="say this on call",
            voice="male",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionGatherUsingSpeakResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_gather_using_speak(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.gather_using_speak(
                call_control_id="",
                payload="say this on call",
                voice="male",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_hangup(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.hangup(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionHangupResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_hangup_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.hangup(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionHangupResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_hangup(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.hangup(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionHangupResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_hangup(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.hangup(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionHangupResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_hangup(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.hangup(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_leave_queue(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.leave_queue(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionLeaveQueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_leave_queue_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.leave_queue(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionLeaveQueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_leave_queue(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.leave_queue(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionLeaveQueueResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_leave_queue(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.leave_queue(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionLeaveQueueResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_leave_queue(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.leave_queue(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_pause_recording(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.pause_recording(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionPauseRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_pause_recording_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.pause_recording(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="6e00ab49-9487-4364-8ad6-23965965afb2",
        )
        assert_matches_type(ActionPauseRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_pause_recording(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.pause_recording(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionPauseRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_pause_recording(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.pause_recording(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionPauseRecordingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_pause_recording(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.pause_recording(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refer(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.refer(
            call_control_id="call_control_id",
            sip_address="sip:username@sip.non-telnyx-address.com",
        )
        assert_matches_type(ActionReferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refer_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.refer(
            call_control_id="call_control_id",
            sip_address="sip:username@sip.non-telnyx-address.com",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
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
            sip_auth_password="sip_auth_password",
            sip_auth_username="sip_auth_username",
            sip_headers=[
                {
                    "name": "User-to-User",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(ActionReferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_refer(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.refer(
            call_control_id="call_control_id",
            sip_address="sip:username@sip.non-telnyx-address.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionReferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_refer(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.refer(
            call_control_id="call_control_id",
            sip_address="sip:username@sip.non-telnyx-address.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionReferResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_refer(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.refer(
                call_control_id="",
                sip_address="sip:username@sip.non-telnyx-address.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reject(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.reject(
            call_control_id="call_control_id",
            cause="USER_BUSY",
        )
        assert_matches_type(ActionRejectResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reject_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.reject(
            call_control_id="call_control_id",
            cause="USER_BUSY",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionRejectResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reject(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.reject(
            call_control_id="call_control_id",
            cause="USER_BUSY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRejectResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reject(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.reject(
            call_control_id="call_control_id",
            cause="USER_BUSY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRejectResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reject(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.reject(
                call_control_id="",
                cause="USER_BUSY",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resume_recording(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.resume_recording(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionResumeRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resume_recording_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.resume_recording(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="6e00ab49-9487-4364-8ad6-23965965afb2",
        )
        assert_matches_type(ActionResumeRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resume_recording(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.resume_recording(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionResumeRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resume_recording(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.resume_recording(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionResumeRecordingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resume_recording(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.resume_recording(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_dtmf(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.send_dtmf(
            call_control_id="call_control_id",
            digits="1www2WABCDw9",
        )
        assert_matches_type(ActionSendDtmfResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_dtmf_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.send_dtmf(
            call_control_id="call_control_id",
            digits="1www2WABCDw9",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            duration_millis=500,
        )
        assert_matches_type(ActionSendDtmfResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_dtmf(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.send_dtmf(
            call_control_id="call_control_id",
            digits="1www2WABCDw9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionSendDtmfResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_dtmf(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.send_dtmf(
            call_control_id="call_control_id",
            digits="1www2WABCDw9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionSendDtmfResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_send_dtmf(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.send_dtmf(
                call_control_id="",
                digits="1www2WABCDw9",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_sip_info(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.send_sip_info(
            call_control_id="call_control_id",
            body='{"key": "value", "numValue": 100}',
            content_type="application/json",
        )
        assert_matches_type(ActionSendSipInfoResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_sip_info_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.send_sip_info(
            call_control_id="call_control_id",
            body='{"key": "value", "numValue": 100}',
            content_type="application/json",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionSendSipInfoResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_sip_info(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.send_sip_info(
            call_control_id="call_control_id",
            body='{"key": "value", "numValue": 100}',
            content_type="application/json",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionSendSipInfoResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_sip_info(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.send_sip_info(
            call_control_id="call_control_id",
            body='{"key": "value", "numValue": 100}',
            content_type="application/json",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionSendSipInfoResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_send_sip_info(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.send_sip_info(
                call_control_id="",
                body='{"key": "value", "numValue": 100}',
                content_type="application/json",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_speak(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.speak(
            call_control_id="call_control_id",
            payload="Say this on the call",
            voice="female",
        )
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_speak_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.speak(
            call_control_id="call_control_id",
            payload="Say this on the call",
            voice="female",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            language="arb",
            payload_type="text",
            service_level="basic",
            stop="current",
            voice_settings={"api_key_ref": "my_elevenlabs_api_key"},
        )
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_speak(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.speak(
            call_control_id="call_control_id",
            payload="Say this on the call",
            voice="female",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_speak(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.speak(
            call_control_id="call_control_id",
            payload="Say this on the call",
            voice="female",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionSpeakResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_speak(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.speak(
                call_control_id="",
                payload="Say this on the call",
                voice="female",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_ai_assistant(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_ai_assistant(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_ai_assistant_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_ai_assistant(
            call_control_id="call_control_id",
            assistant={
                "id": "id",
                "instructions": "You are a friendly voice assistant.",
                "openai_api_key_ref": "openai_api_key_ref",
            },
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            greeting="Hello, can you tell me your age and where you live?",
            interruption_settings={"enable": True},
            transcription={"model": "distil-whisper/distil-large-v2"},
            voice="Telnyx.KokoroTTS.af",
            voice_settings={"api_key_ref": "my_elevenlabs_api_key"},
        )
        assert_matches_type(ActionStartAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start_ai_assistant(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.start_ai_assistant(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStartAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start_ai_assistant(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.start_ai_assistant(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStartAIAssistantResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_start_ai_assistant(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.start_ai_assistant(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_forking(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_forking(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_forking_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_forking(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            rx="udp:192.0.2.1:9000",
            stream_type="decrypted",
            tx="udp:192.0.2.1:9001",
        )
        assert_matches_type(ActionStartForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start_forking(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.start_forking(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStartForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start_forking(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.start_forking(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStartForkingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_start_forking(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.start_forking(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_noise_suppression(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_noise_suppression(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_noise_suppression_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_noise_suppression(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            direction="both",
            noise_suppression_engine="A",
        )
        assert_matches_type(ActionStartNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start_noise_suppression(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.start_noise_suppression(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStartNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start_noise_suppression(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.start_noise_suppression(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStartNoiseSuppressionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_start_noise_suppression(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.start_noise_suppression(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_playback(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_playback(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_playback_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_playback(
            call_control_id="call_control_id",
            audio_type="wav",
            audio_url="http://www.example.com/sounds/greeting.wav",
            cache_audio=True,
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            loop="infinity",
            media_name="my_media_uploaded_to_media_storage_api",
            overlay=True,
            playback_content="SUQzAwAAAAADf1...",
            stop="current",
            target_legs="self",
        )
        assert_matches_type(ActionStartPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start_playback(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.start_playback(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStartPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start_playback(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.start_playback(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStartPlaybackResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_start_playback(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.start_playback(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_recording(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_recording(
            call_control_id="call_control_id",
            channels="single",
            format="wav",
        )
        assert_matches_type(ActionStartRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_recording_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_recording(
            call_control_id="call_control_id",
            channels="single",
            format="wav",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            custom_file_name="my_recording_file_name",
            max_length=0,
            play_beep=True,
            recording_track="outbound",
            timeout_secs=0,
            transcription=True,
            transcription_engine="B",
            transcription_language="en-US",
            transcription_max_speaker_count=4,
            transcription_min_speaker_count=4,
            transcription_profanity_filter=True,
            transcription_speaker_diarization=True,
            trim="trim-silence",
        )
        assert_matches_type(ActionStartRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start_recording(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.start_recording(
            call_control_id="call_control_id",
            channels="single",
            format="wav",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStartRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start_recording(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.start_recording(
            call_control_id="call_control_id",
            channels="single",
            format="wav",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStartRecordingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_start_recording(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.start_recording(
                call_control_id="",
                channels="single",
                format="wav",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_siprec(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_siprec(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_siprec_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_siprec(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            connector_name="my-siprec-connector",
            include_metadata_custom_headers=True,
            secure=True,
            session_timeout_secs=900,
            sip_transport="tcp",
            siprec_track="both_tracks",
        )
        assert_matches_type(ActionStartSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start_siprec(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.start_siprec(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStartSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start_siprec(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.start_siprec(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStartSiprecResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_start_siprec(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.start_siprec(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_streaming(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_streaming(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_streaming_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_streaming(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            dialogflow_config={
                "analyze_sentiment": False,
                "partial_automated_agent_reply": False,
            },
            enable_dialogflow=False,
            stream_bidirectional_codec="G722",
            stream_bidirectional_mode="rtp",
            stream_bidirectional_target_legs="both",
            stream_codec="PCMA",
            stream_track="both_tracks",
            stream_url="wss://www.example.com/websocket",
        )
        assert_matches_type(ActionStartStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start_streaming(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.start_streaming(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStartStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start_streaming(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.start_streaming(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStartStreamingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_start_streaming(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.start_streaming(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_transcription(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_transcription(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStartTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_transcription_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.start_transcription(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            transcription_engine="A",
            transcription_engine_config={
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
            transcription_tracks="both",
        )
        assert_matches_type(ActionStartTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start_transcription(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.start_transcription(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStartTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start_transcription(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.start_transcription(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStartTranscriptionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_start_transcription(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.start_transcription(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_ai_assistant(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_ai_assistant(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_ai_assistant_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_ai_assistant(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionStopAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop_ai_assistant(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.stop_ai_assistant(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStopAIAssistantResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop_ai_assistant(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.stop_ai_assistant(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStopAIAssistantResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stop_ai_assistant(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.stop_ai_assistant(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_forking(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_forking(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_forking_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_forking(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            stream_type="decrypted",
        )
        assert_matches_type(ActionStopForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop_forking(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.stop_forking(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStopForkingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop_forking(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.stop_forking(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStopForkingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stop_forking(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.stop_forking(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_gather(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_gather(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_gather_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_gather(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionStopGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop_gather(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.stop_gather(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStopGatherResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop_gather(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.stop_gather(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStopGatherResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stop_gather(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.stop_gather(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_noise_suppression(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_noise_suppression(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_noise_suppression_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_noise_suppression(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionStopNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop_noise_suppression(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.stop_noise_suppression(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStopNoiseSuppressionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop_noise_suppression(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.stop_noise_suppression(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStopNoiseSuppressionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stop_noise_suppression(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.stop_noise_suppression(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_playback(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_playback(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_playback_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_playback(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            overlay=False,
            stop="all",
        )
        assert_matches_type(ActionStopPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop_playback(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.stop_playback(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStopPlaybackResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop_playback(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.stop_playback(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStopPlaybackResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stop_playback(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.stop_playback(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_recording(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_recording(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_recording_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_recording(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="6e00ab49-9487-4364-8ad6-23965965afb2",
        )
        assert_matches_type(ActionStopRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop_recording(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.stop_recording(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStopRecordingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop_recording(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.stop_recording(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStopRecordingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stop_recording(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.stop_recording(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_siprec(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_siprec(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_siprec_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_siprec(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionStopSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop_siprec(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.stop_siprec(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStopSiprecResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop_siprec(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.stop_siprec(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStopSiprecResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stop_siprec(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.stop_siprec(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_streaming(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_streaming(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_streaming_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_streaming(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            stream_id="1edb94f9-7ef0-4150-b502-e0ebadfd9491",
        )
        assert_matches_type(ActionStopStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop_streaming(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.stop_streaming(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStopStreamingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop_streaming(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.stop_streaming(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStopStreamingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stop_streaming(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.stop_streaming(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_transcription(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_transcription(
            call_control_id="call_control_id",
        )
        assert_matches_type(ActionStopTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_transcription_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.stop_transcription(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionStopTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop_transcription(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.stop_transcription(
            call_control_id="call_control_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStopTranscriptionResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop_transcription(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.stop_transcription(
            call_control_id="call_control_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStopTranscriptionResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stop_transcription(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.stop_transcription(
                call_control_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_switch_supervisor_role(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.switch_supervisor_role(
            call_control_id="call_control_id",
            role="barge",
        )
        assert_matches_type(ActionSwitchSupervisorRoleResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_switch_supervisor_role(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.switch_supervisor_role(
            call_control_id="call_control_id",
            role="barge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionSwitchSupervisorRoleResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_switch_supervisor_role(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.switch_supervisor_role(
            call_control_id="call_control_id",
            role="barge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionSwitchSupervisorRoleResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_switch_supervisor_role(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.switch_supervisor_role(
                call_control_id="",
                role="barge",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_transfer(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.transfer(
            call_control_id="call_control_id",
            to="+18005550100 or sip:username@sip.telnyx.com",
        )
        assert_matches_type(ActionTransferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_transfer_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.transfer(
            call_control_id="call_control_id",
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
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
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
            early_media=True,
            from_="+18005550101",
            from_display_name="Company Name",
            media_encryption="SRTP",
            media_name="my_media_uploaded_to_media_storage_api",
            mute_dtmf="opposite",
            park_after_unbridge="self",
            sip_auth_password="password",
            sip_auth_username="username",
            sip_headers=[
                {
                    "name": "User-to-User",
                    "value": "value",
                }
            ],
            sip_transport_protocol="TLS",
            sound_modifications={
                "octaves": 0.1,
                "pitch": 0,
                "semitone": -2,
                "track": "both",
            },
            target_leg_client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            time_limit_secs=600,
            timeout_secs=60,
            webhook_url="https://www.example.com/server-b/",
            webhook_url_method="POST",
        )
        assert_matches_type(ActionTransferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_transfer(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.transfer(
            call_control_id="call_control_id",
            to="+18005550100 or sip:username@sip.telnyx.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionTransferResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_transfer(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.transfer(
            call_control_id="call_control_id",
            to="+18005550100 or sip:username@sip.telnyx.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionTransferResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_transfer(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.transfer(
                call_control_id="",
                to="+18005550100 or sip:username@sip.telnyx.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_client_state(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.calls.actions.update_client_state(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
        )
        assert_matches_type(ActionUpdateClientStateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_client_state(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calls.actions.with_raw_response.update_client_state(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionUpdateClientStateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_client_state(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calls.actions.with_streaming_response.update_client_state(
            call_control_id="call_control_id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionUpdateClientStateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_client_state(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_control_id` but received ''"):
            await async_client.calls.actions.with_raw_response.update_client_state(
                call_control_id="",
                client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            )
