# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.conferences import (
    ActionHoldResponse,
    ActionJoinResponse,
    ActionMuteResponse,
    ActionPlayResponse,
    ActionStopResponse,
    ActionLeaveResponse,
    ActionSpeakResponse,
    ActionUnholdResponse,
    ActionUnmuteResponse,
    ActionUpdateResponse,
    ActionRecordStopResponse,
    ActionRecordPauseResponse,
    ActionRecordStartResponse,
    ActionRecordResumeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        action = client.conferences.actions.update(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            supervisor_role="whisper",
        )
        assert_matches_type(ActionUpdateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.update(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            supervisor_role="whisper",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            whisper_call_control_ids=[
                "v2:Sg1xxxQ_U3ixxxyXT_VDNI3xxxazZdg6Vxxxs4-GNYxxxVaJPOhFMRQ",
                "v2:qqpb0mmvd-ovhhBr0BUQQn0fld5jIboaaX3-De0DkqXHzbf8d75xkw",
            ],
        )
        assert_matches_type(ActionUpdateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.update(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            supervisor_role="whisper",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionUpdateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.update(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            supervisor_role="whisper",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionUpdateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.update(
                id="",
                call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
                supervisor_role="whisper",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_hold(self, client: Telnyx) -> None:
        action = client.conferences.actions.hold(
            id="id",
        )
        assert_matches_type(ActionHoldResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_hold_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.hold(
            id="id",
            audio_url="http://example.com/message.wav",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
            media_name="my_media_uploaded_to_media_storage_api",
        )
        assert_matches_type(ActionHoldResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_hold(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.hold(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionHoldResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_hold(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.hold(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionHoldResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_hold(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.hold(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_join(self, client: Telnyx) -> None:
        action = client.conferences.actions.join(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        )
        assert_matches_type(ActionJoinResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_join_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.join(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            beep_enabled="always",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            end_conference_on_exit=True,
            hold=True,
            hold_audio_url="http://www.example.com/audio.wav",
            hold_media_name="my_media_uploaded_to_media_storage_api",
            mute=True,
            soft_end_conference_on_exit=True,
            start_conference_on_enter=True,
            supervisor_role="whisper",
            whisper_call_control_ids=[
                "v2:Sg1xxxQ_U3ixxxyXT_VDNI3xxxazZdg6Vxxxs4-GNYxxxVaJPOhFMRQ",
                "v2:qqpb0mmvd-ovhhBr0BUQQn0fld5jIboaaX3-De0DkqXHzbf8d75xkw",
            ],
        )
        assert_matches_type(ActionJoinResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_join(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.join(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionJoinResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_join(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.join(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionJoinResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_join(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.join(
                id="",
                call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_leave(self, client: Telnyx) -> None:
        action = client.conferences.actions.leave(
            id="id",
            call_control_id="c46e06d7-b78f-4b13-96b6-c576af9640ff",
        )
        assert_matches_type(ActionLeaveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_leave_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.leave(
            id="id",
            call_control_id="c46e06d7-b78f-4b13-96b6-c576af9640ff",
            beep_enabled="never",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionLeaveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_leave(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.leave(
            id="id",
            call_control_id="c46e06d7-b78f-4b13-96b6-c576af9640ff",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionLeaveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_leave(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.leave(
            id="id",
            call_control_id="c46e06d7-b78f-4b13-96b6-c576af9640ff",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionLeaveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_leave(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.leave(
                id="",
                call_control_id="c46e06d7-b78f-4b13-96b6-c576af9640ff",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_mute(self, client: Telnyx) -> None:
        action = client.conferences.actions.mute(
            id="id",
        )
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_mute_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.mute(
            id="id",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
        )
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_mute(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.mute(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_mute(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.mute(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionMuteResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_mute(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.mute(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_play(self, client: Telnyx) -> None:
        action = client.conferences.actions.play(
            id="id",
        )
        assert_matches_type(ActionPlayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_play_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.play(
            id="id",
            audio_url="http://www.example.com/sounds/greeting.wav",
            call_control_ids=["string"],
            loop="infinity",
            media_name="my_media_uploaded_to_media_storage_api",
        )
        assert_matches_type(ActionPlayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_play(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.play(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionPlayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_play(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.play(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionPlayResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_play(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.play(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_record_pause(self, client: Telnyx) -> None:
        action = client.conferences.actions.record_pause(
            id="id",
        )
        assert_matches_type(ActionRecordPauseResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_record_pause_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.record_pause(
            id="id",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionRecordPauseResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_record_pause(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.record_pause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRecordPauseResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_record_pause(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.record_pause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRecordPauseResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_record_pause(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.record_pause(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_record_resume(self, client: Telnyx) -> None:
        action = client.conferences.actions.record_resume(
            id="id",
        )
        assert_matches_type(ActionRecordResumeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_record_resume_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.record_resume(
            id="id",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionRecordResumeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_record_resume(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.record_resume(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRecordResumeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_record_resume(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.record_resume(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRecordResumeResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_record_resume(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.record_resume(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_record_start(self, client: Telnyx) -> None:
        action = client.conferences.actions.record_start(
            id="id",
            format="wav",
        )
        assert_matches_type(ActionRecordStartResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_record_start_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.record_start(
            id="id",
            format="wav",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            custom_file_name="my_recording_file_name",
            play_beep=True,
            trim="trim-silence",
        )
        assert_matches_type(ActionRecordStartResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_record_start(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.record_start(
            id="id",
            format="wav",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRecordStartResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_record_start(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.record_start(
            id="id",
            format="wav",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRecordStartResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_record_start(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.record_start(
                id="",
                format="wav",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_record_stop(self, client: Telnyx) -> None:
        action = client.conferences.actions.record_stop(
            id="id",
        )
        assert_matches_type(ActionRecordStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_record_stop_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.record_stop(
            id="id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="6e00ab49-9487-4364-8ad6-23965965afb2",
        )
        assert_matches_type(ActionRecordStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_record_stop(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.record_stop(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRecordStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_record_stop(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.record_stop(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRecordStopResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_record_stop(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.record_stop(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_speak(self, client: Telnyx) -> None:
        action = client.conferences.actions.speak(
            id="id",
            payload="Say this to participants",
            voice="female",
        )
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_speak_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.speak(
            id="id",
            payload="Say this to participants",
            voice="female",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            language="en-US",
            payload_type="text",
            voice_settings={"api_key_ref": "my_elevenlabs_api_key"},
        )
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_speak(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.speak(
            id="id",
            payload="Say this to participants",
            voice="female",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_speak(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.speak(
            id="id",
            payload="Say this to participants",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.speak(
                id="",
                payload="Say this to participants",
                voice="female",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop(self, client: Telnyx) -> None:
        action = client.conferences.actions.stop(
            id="id",
        )
        assert_matches_type(ActionStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.stop(
            id="id",
            call_control_ids=["string"],
        )
        assert_matches_type(ActionStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.stop(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.stop(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionStopResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stop(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.stop(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unhold(self, client: Telnyx) -> None:
        action = client.conferences.actions.unhold(
            id="id",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
        )
        assert_matches_type(ActionUnholdResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unhold(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.unhold(
            id="id",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionUnholdResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unhold(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.unhold(
            id="id",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionUnholdResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unhold(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.unhold(
                id="",
                call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unmute(self, client: Telnyx) -> None:
        action = client.conferences.actions.unmute(
            id="id",
        )
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unmute_with_all_params(self, client: Telnyx) -> None:
        action = client.conferences.actions.unmute(
            id="id",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
        )
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unmute(self, client: Telnyx) -> None:
        response = client.conferences.actions.with_raw_response.unmute(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unmute(self, client: Telnyx) -> None:
        with client.conferences.actions.with_streaming_response.unmute(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionUnmuteResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unmute(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.actions.with_raw_response.unmute(
                id="",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.update(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            supervisor_role="whisper",
        )
        assert_matches_type(ActionUpdateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.update(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            supervisor_role="whisper",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            whisper_call_control_ids=[
                "v2:Sg1xxxQ_U3ixxxyXT_VDNI3xxxazZdg6Vxxxs4-GNYxxxVaJPOhFMRQ",
                "v2:qqpb0mmvd-ovhhBr0BUQQn0fld5jIboaaX3-De0DkqXHzbf8d75xkw",
            ],
        )
        assert_matches_type(ActionUpdateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.update(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            supervisor_role="whisper",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionUpdateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.update(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            supervisor_role="whisper",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionUpdateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.update(
                id="",
                call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
                supervisor_role="whisper",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_hold(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.hold(
            id="id",
        )
        assert_matches_type(ActionHoldResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_hold_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.hold(
            id="id",
            audio_url="http://example.com/message.wav",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
            media_name="my_media_uploaded_to_media_storage_api",
        )
        assert_matches_type(ActionHoldResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_hold(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.hold(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionHoldResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_hold(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.hold(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionHoldResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_hold(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.hold(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_join(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.join(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        )
        assert_matches_type(ActionJoinResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_join_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.join(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            beep_enabled="always",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            end_conference_on_exit=True,
            hold=True,
            hold_audio_url="http://www.example.com/audio.wav",
            hold_media_name="my_media_uploaded_to_media_storage_api",
            mute=True,
            soft_end_conference_on_exit=True,
            start_conference_on_enter=True,
            supervisor_role="whisper",
            whisper_call_control_ids=[
                "v2:Sg1xxxQ_U3ixxxyXT_VDNI3xxxazZdg6Vxxxs4-GNYxxxVaJPOhFMRQ",
                "v2:qqpb0mmvd-ovhhBr0BUQQn0fld5jIboaaX3-De0DkqXHzbf8d75xkw",
            ],
        )
        assert_matches_type(ActionJoinResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_join(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.join(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionJoinResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_join(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.join(
            id="id",
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionJoinResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_join(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.join(
                id="",
                call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_leave(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.leave(
            id="id",
            call_control_id="c46e06d7-b78f-4b13-96b6-c576af9640ff",
        )
        assert_matches_type(ActionLeaveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_leave_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.leave(
            id="id",
            call_control_id="c46e06d7-b78f-4b13-96b6-c576af9640ff",
            beep_enabled="never",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionLeaveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_leave(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.leave(
            id="id",
            call_control_id="c46e06d7-b78f-4b13-96b6-c576af9640ff",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionLeaveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_leave(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.leave(
            id="id",
            call_control_id="c46e06d7-b78f-4b13-96b6-c576af9640ff",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionLeaveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_leave(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.leave(
                id="",
                call_control_id="c46e06d7-b78f-4b13-96b6-c576af9640ff",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_mute(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.mute(
            id="id",
        )
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_mute_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.mute(
            id="id",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
        )
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_mute(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.mute(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_mute(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.mute(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionMuteResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_mute(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.mute(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_play(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.play(
            id="id",
        )
        assert_matches_type(ActionPlayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_play_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.play(
            id="id",
            audio_url="http://www.example.com/sounds/greeting.wav",
            call_control_ids=["string"],
            loop="infinity",
            media_name="my_media_uploaded_to_media_storage_api",
        )
        assert_matches_type(ActionPlayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_play(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.play(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionPlayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_play(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.play(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionPlayResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_play(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.play(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_record_pause(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.record_pause(
            id="id",
        )
        assert_matches_type(ActionRecordPauseResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_record_pause_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.record_pause(
            id="id",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionRecordPauseResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_record_pause(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.record_pause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRecordPauseResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_record_pause(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.record_pause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRecordPauseResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_record_pause(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.record_pause(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_record_resume(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.record_resume(
            id="id",
        )
        assert_matches_type(ActionRecordResumeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_record_resume_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.record_resume(
            id="id",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="891510ac-f3e4-11e8-af5b-de00688a4901",
        )
        assert_matches_type(ActionRecordResumeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_record_resume(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.record_resume(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRecordResumeResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_record_resume(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.record_resume(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRecordResumeResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_record_resume(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.record_resume(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_record_start(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.record_start(
            id="id",
            format="wav",
        )
        assert_matches_type(ActionRecordStartResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_record_start_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.record_start(
            id="id",
            format="wav",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            custom_file_name="my_recording_file_name",
            play_beep=True,
            trim="trim-silence",
        )
        assert_matches_type(ActionRecordStartResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_record_start(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.record_start(
            id="id",
            format="wav",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRecordStartResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_record_start(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.record_start(
            id="id",
            format="wav",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRecordStartResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_record_start(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.record_start(
                id="",
                format="wav",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_record_stop(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.record_stop(
            id="id",
        )
        assert_matches_type(ActionRecordStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_record_stop_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.record_stop(
            id="id",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            recording_id="6e00ab49-9487-4364-8ad6-23965965afb2",
        )
        assert_matches_type(ActionRecordStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_record_stop(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.record_stop(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRecordStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_record_stop(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.record_stop(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRecordStopResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_record_stop(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.record_stop(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_speak(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.speak(
            id="id",
            payload="Say this to participants",
            voice="female",
        )
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_speak_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.speak(
            id="id",
            payload="Say this to participants",
            voice="female",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            language="en-US",
            payload_type="text",
            voice_settings={"api_key_ref": "my_elevenlabs_api_key"},
        )
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_speak(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.speak(
            id="id",
            payload="Say this to participants",
            voice="female",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionSpeakResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_speak(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.speak(
            id="id",
            payload="Say this to participants",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.speak(
                id="",
                payload="Say this to participants",
                voice="female",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.stop(
            id="id",
        )
        assert_matches_type(ActionStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.stop(
            id="id",
            call_control_ids=["string"],
        )
        assert_matches_type(ActionStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.stop(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionStopResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.stop(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionStopResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stop(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.stop(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unhold(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.unhold(
            id="id",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
        )
        assert_matches_type(ActionUnholdResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unhold(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.unhold(
            id="id",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionUnholdResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unhold(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.unhold(
            id="id",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionUnholdResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unhold(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.unhold(
                id="",
                call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unmute(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.unmute(
            id="id",
        )
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unmute_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.conferences.actions.unmute(
            id="id",
            call_control_ids=["v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg"],
        )
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unmute(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.actions.with_raw_response.unmute(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unmute(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.actions.with_streaming_response.unmute(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionUnmuteResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unmute(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.actions.with_raw_response.unmute(
                id="",
            )
