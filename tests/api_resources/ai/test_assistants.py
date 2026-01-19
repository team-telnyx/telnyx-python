# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai import (
    AssistantsList,
    InferenceEmbedding,
    AssistantChatResponse,
    AssistantDeleteResponse,
    AssistantSendSMSResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssistants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.create(
            instructions="instructions",
            model="model",
            name="name",
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.create(
            instructions="instructions",
            model="model",
            name="name",
            description="description",
            dynamic_variables={"foo": "bar"},
            dynamic_variables_webhook_url="dynamic_variables_webhook_url",
            enabled_features=["telephony"],
            greeting="greeting",
            insight_settings={"insight_group_id": "insight_group_id"},
            llm_api_key_ref="llm_api_key_ref",
            messaging_settings={
                "conversation_inactivity_minutes": 1,
                "default_messaging_profile_id": "default_messaging_profile_id",
                "delivery_status_webhook_url": "delivery_status_webhook_url",
            },
            privacy_settings={"data_retention": True},
            telephony_settings={
                "default_texml_app_id": "default_texml_app_id",
                "noise_suppression": "krisp",
                "noise_suppression_config": {
                    "attenuation_limit": 0,
                    "mode": "advanced",
                },
                "supports_unauthenticated_web_calls": True,
                "time_limit_secs": 30,
                "user_idle_timeout_secs": 30,
                "voicemail_detection": {
                    "on_voicemail_detected": {
                        "action": "stop_assistant",
                        "voicemail_message": {
                            "message": "message",
                            "prompt": "prompt",
                            "type": "prompt",
                        },
                    }
                },
            },
            tools=[
                {
                    "type": "webhook",
                    "webhook": {
                        "description": "description",
                        "name": "name",
                        "url": "https://example.com/api/v1/function",
                        "async": True,
                        "body_parameters": {
                            "properties": {
                                "age": "bar",
                                "location": "bar",
                            },
                            "required": ["age", "location"],
                            "type": "object",
                        },
                        "headers": [
                            {
                                "name": "name",
                                "value": "value",
                            }
                        ],
                        "method": "GET",
                        "path_parameters": {
                            "properties": {"id": "bar"},
                            "required": ["id"],
                            "type": "object",
                        },
                        "query_parameters": {
                            "properties": {"page": "bar"},
                            "required": ["page"],
                            "type": "object",
                        },
                        "timeout_ms": 500,
                    },
                }
            ],
            transcription={
                "language": "language",
                "model": "deepgram/flux",
                "region": "region",
                "settings": {
                    "eager_eot_threshold": 0.3,
                    "eot_threshold": 0,
                    "eot_timeout_ms": 0,
                    "numerals": True,
                    "smart_format": True,
                },
            },
            voice_settings={
                "voice": "voice",
                "api_key_ref": "api_key_ref",
                "background_audio": {
                    "type": "predefined_media",
                    "value": "silence",
                },
                "similarity_boost": 0,
                "speed": 0,
                "style": 0,
                "temperature": 0,
                "use_speaker_boost": True,
                "voice_speed": 0,
            },
            widget_settings={
                "agent_thinking_text": "agent_thinking_text",
                "audio_visualizer_config": {
                    "color": "verdant",
                    "preset": "preset",
                },
                "default_state": "expanded",
                "give_feedback_url": "give_feedback_url",
                "logo_icon_url": "logo_icon_url",
                "position": "fixed",
                "report_issue_url": "report_issue_url",
                "speak_to_interrupt_text": "speak_to_interrupt_text",
                "start_call_text": "start_call_text",
                "theme": "light",
                "view_history_url": "view_history_url",
            },
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.assistants.with_raw_response.create(
            instructions="instructions",
            model="model",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.assistants.with_streaming_response.create(
            instructions="instructions",
            model="model",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(InferenceEmbedding, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.retrieve(
            assistant_id="assistant_id",
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.retrieve(
            assistant_id="assistant_id",
            call_control_id="call_control_id",
            fetch_dynamic_variables_from_webhook=True,
            from_="from",
            to="to",
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.assistants.with_raw_response.retrieve(
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.assistants.with_streaming_response.retrieve(
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(InferenceEmbedding, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.with_raw_response.retrieve(
                assistant_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.update(
            assistant_id="assistant_id",
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.update(
            assistant_id="assistant_id",
            description="description",
            dynamic_variables={"foo": "bar"},
            dynamic_variables_webhook_url="dynamic_variables_webhook_url",
            enabled_features=["telephony"],
            greeting="greeting",
            insight_settings={"insight_group_id": "insight_group_id"},
            instructions="instructions",
            llm_api_key_ref="llm_api_key_ref",
            messaging_settings={
                "conversation_inactivity_minutes": 1,
                "default_messaging_profile_id": "default_messaging_profile_id",
                "delivery_status_webhook_url": "delivery_status_webhook_url",
            },
            model="model",
            name="name",
            privacy_settings={"data_retention": True},
            promote_to_main=True,
            telephony_settings={
                "default_texml_app_id": "default_texml_app_id",
                "noise_suppression": "krisp",
                "noise_suppression_config": {
                    "attenuation_limit": 0,
                    "mode": "advanced",
                },
                "supports_unauthenticated_web_calls": True,
                "time_limit_secs": 30,
                "user_idle_timeout_secs": 30,
                "voicemail_detection": {
                    "on_voicemail_detected": {
                        "action": "stop_assistant",
                        "voicemail_message": {
                            "message": "message",
                            "prompt": "prompt",
                            "type": "prompt",
                        },
                    }
                },
            },
            tools=[
                {
                    "type": "webhook",
                    "webhook": {
                        "description": "description",
                        "name": "name",
                        "url": "https://example.com/api/v1/function",
                        "async": True,
                        "body_parameters": {
                            "properties": {
                                "age": "bar",
                                "location": "bar",
                            },
                            "required": ["age", "location"],
                            "type": "object",
                        },
                        "headers": [
                            {
                                "name": "name",
                                "value": "value",
                            }
                        ],
                        "method": "GET",
                        "path_parameters": {
                            "properties": {"id": "bar"},
                            "required": ["id"],
                            "type": "object",
                        },
                        "query_parameters": {
                            "properties": {"page": "bar"},
                            "required": ["page"],
                            "type": "object",
                        },
                        "timeout_ms": 500,
                    },
                }
            ],
            transcription={
                "language": "language",
                "model": "deepgram/flux",
                "region": "region",
                "settings": {
                    "eager_eot_threshold": 0.3,
                    "eot_threshold": 0,
                    "eot_timeout_ms": 0,
                    "numerals": True,
                    "smart_format": True,
                },
            },
            voice_settings={
                "voice": "voice",
                "api_key_ref": "api_key_ref",
                "background_audio": {
                    "type": "predefined_media",
                    "value": "silence",
                },
                "similarity_boost": 0,
                "speed": 0,
                "style": 0,
                "temperature": 0,
                "use_speaker_boost": True,
                "voice_speed": 0,
            },
            widget_settings={
                "agent_thinking_text": "agent_thinking_text",
                "audio_visualizer_config": {
                    "color": "verdant",
                    "preset": "preset",
                },
                "default_state": "expanded",
                "give_feedback_url": "give_feedback_url",
                "logo_icon_url": "logo_icon_url",
                "position": "fixed",
                "report_issue_url": "report_issue_url",
                "speak_to_interrupt_text": "speak_to_interrupt_text",
                "start_call_text": "start_call_text",
                "theme": "light",
                "view_history_url": "view_history_url",
            },
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.assistants.with_raw_response.update(
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.assistants.with_streaming_response.update(
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(InferenceEmbedding, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.with_raw_response.update(
                assistant_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.list()
        assert_matches_type(AssistantsList, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.assistants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantsList, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.assistants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(AssistantsList, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.delete(
            "assistant_id",
        )
        assert_matches_type(AssistantDeleteResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.assistants.with_raw_response.delete(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantDeleteResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.assistants.with_streaming_response.delete(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(AssistantDeleteResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_chat(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.chat(
            assistant_id="assistant_id",
            content="Tell me a joke about cats",
            conversation_id="42b20469-1215-4a9a-8964-c36f66b406f4",
        )
        assert_matches_type(AssistantChatResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_chat_with_all_params(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.chat(
            assistant_id="assistant_id",
            content="Tell me a joke about cats",
            conversation_id="42b20469-1215-4a9a-8964-c36f66b406f4",
            name="Charlie",
        )
        assert_matches_type(AssistantChatResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_chat(self, client: Telnyx) -> None:
        response = client.ai.assistants.with_raw_response.chat(
            assistant_id="assistant_id",
            content="Tell me a joke about cats",
            conversation_id="42b20469-1215-4a9a-8964-c36f66b406f4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantChatResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_chat(self, client: Telnyx) -> None:
        with client.ai.assistants.with_streaming_response.chat(
            assistant_id="assistant_id",
            content="Tell me a joke about cats",
            conversation_id="42b20469-1215-4a9a-8964-c36f66b406f4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(AssistantChatResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_chat(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.with_raw_response.chat(
                assistant_id="",
                content="Tell me a joke about cats",
                conversation_id="42b20469-1215-4a9a-8964-c36f66b406f4",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.clone(
            "assistant_id",
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: Telnyx) -> None:
        response = client.ai.assistants.with_raw_response.clone(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: Telnyx) -> None:
        with client.ai.assistants.with_streaming_response.clone(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(InferenceEmbedding, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_clone(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.with_raw_response.clone(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_texml(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.get_texml(
            "assistant_id",
        )
        assert_matches_type(str, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_texml(self, client: Telnyx) -> None:
        response = client.ai.assistants.with_raw_response.get_texml(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(str, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_texml(self, client: Telnyx) -> None:
        with client.ai.assistants.with_streaming_response.get_texml(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(str, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_texml(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.with_raw_response.get_texml(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_imports(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.imports(
            api_key_ref="api_key_ref",
            provider="elevenlabs",
        )
        assert_matches_type(AssistantsList, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_imports_with_all_params(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.imports(
            api_key_ref="api_key_ref",
            provider="elevenlabs",
            import_ids=["string"],
        )
        assert_matches_type(AssistantsList, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_imports(self, client: Telnyx) -> None:
        response = client.ai.assistants.with_raw_response.imports(
            api_key_ref="api_key_ref",
            provider="elevenlabs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantsList, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_imports(self, client: Telnyx) -> None:
        with client.ai.assistants.with_streaming_response.imports(
            api_key_ref="api_key_ref",
            provider="elevenlabs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(AssistantsList, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_sms(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.send_sms(
            assistant_id="assistant_id",
            from_="from",
            to="to",
        )
        assert_matches_type(AssistantSendSMSResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_sms_with_all_params(self, client: Telnyx) -> None:
        assistant = client.ai.assistants.send_sms(
            assistant_id="assistant_id",
            from_="from",
            to="to",
            conversation_metadata={"foo": "string"},
            should_create_conversation=True,
            text="text",
        )
        assert_matches_type(AssistantSendSMSResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_sms(self, client: Telnyx) -> None:
        response = client.ai.assistants.with_raw_response.send_sms(
            assistant_id="assistant_id",
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantSendSMSResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_sms(self, client: Telnyx) -> None:
        with client.ai.assistants.with_streaming_response.send_sms(
            assistant_id="assistant_id",
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(AssistantSendSMSResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_send_sms(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.with_raw_response.send_sms(
                assistant_id="",
                from_="from",
                to="to",
            )


class TestAsyncAssistants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.create(
            instructions="instructions",
            model="model",
            name="name",
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.create(
            instructions="instructions",
            model="model",
            name="name",
            description="description",
            dynamic_variables={"foo": "bar"},
            dynamic_variables_webhook_url="dynamic_variables_webhook_url",
            enabled_features=["telephony"],
            greeting="greeting",
            insight_settings={"insight_group_id": "insight_group_id"},
            llm_api_key_ref="llm_api_key_ref",
            messaging_settings={
                "conversation_inactivity_minutes": 1,
                "default_messaging_profile_id": "default_messaging_profile_id",
                "delivery_status_webhook_url": "delivery_status_webhook_url",
            },
            privacy_settings={"data_retention": True},
            telephony_settings={
                "default_texml_app_id": "default_texml_app_id",
                "noise_suppression": "krisp",
                "noise_suppression_config": {
                    "attenuation_limit": 0,
                    "mode": "advanced",
                },
                "supports_unauthenticated_web_calls": True,
                "time_limit_secs": 30,
                "user_idle_timeout_secs": 30,
                "voicemail_detection": {
                    "on_voicemail_detected": {
                        "action": "stop_assistant",
                        "voicemail_message": {
                            "message": "message",
                            "prompt": "prompt",
                            "type": "prompt",
                        },
                    }
                },
            },
            tools=[
                {
                    "type": "webhook",
                    "webhook": {
                        "description": "description",
                        "name": "name",
                        "url": "https://example.com/api/v1/function",
                        "async": True,
                        "body_parameters": {
                            "properties": {
                                "age": "bar",
                                "location": "bar",
                            },
                            "required": ["age", "location"],
                            "type": "object",
                        },
                        "headers": [
                            {
                                "name": "name",
                                "value": "value",
                            }
                        ],
                        "method": "GET",
                        "path_parameters": {
                            "properties": {"id": "bar"},
                            "required": ["id"],
                            "type": "object",
                        },
                        "query_parameters": {
                            "properties": {"page": "bar"},
                            "required": ["page"],
                            "type": "object",
                        },
                        "timeout_ms": 500,
                    },
                }
            ],
            transcription={
                "language": "language",
                "model": "deepgram/flux",
                "region": "region",
                "settings": {
                    "eager_eot_threshold": 0.3,
                    "eot_threshold": 0,
                    "eot_timeout_ms": 0,
                    "numerals": True,
                    "smart_format": True,
                },
            },
            voice_settings={
                "voice": "voice",
                "api_key_ref": "api_key_ref",
                "background_audio": {
                    "type": "predefined_media",
                    "value": "silence",
                },
                "similarity_boost": 0,
                "speed": 0,
                "style": 0,
                "temperature": 0,
                "use_speaker_boost": True,
                "voice_speed": 0,
            },
            widget_settings={
                "agent_thinking_text": "agent_thinking_text",
                "audio_visualizer_config": {
                    "color": "verdant",
                    "preset": "preset",
                },
                "default_state": "expanded",
                "give_feedback_url": "give_feedback_url",
                "logo_icon_url": "logo_icon_url",
                "position": "fixed",
                "report_issue_url": "report_issue_url",
                "speak_to_interrupt_text": "speak_to_interrupt_text",
                "start_call_text": "start_call_text",
                "theme": "light",
                "view_history_url": "view_history_url",
            },
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.with_raw_response.create(
            instructions="instructions",
            model="model",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.with_streaming_response.create(
            instructions="instructions",
            model="model",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(InferenceEmbedding, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.retrieve(
            assistant_id="assistant_id",
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.retrieve(
            assistant_id="assistant_id",
            call_control_id="call_control_id",
            fetch_dynamic_variables_from_webhook=True,
            from_="from",
            to="to",
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.with_raw_response.retrieve(
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.with_streaming_response.retrieve(
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(InferenceEmbedding, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.with_raw_response.retrieve(
                assistant_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.update(
            assistant_id="assistant_id",
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.update(
            assistant_id="assistant_id",
            description="description",
            dynamic_variables={"foo": "bar"},
            dynamic_variables_webhook_url="dynamic_variables_webhook_url",
            enabled_features=["telephony"],
            greeting="greeting",
            insight_settings={"insight_group_id": "insight_group_id"},
            instructions="instructions",
            llm_api_key_ref="llm_api_key_ref",
            messaging_settings={
                "conversation_inactivity_minutes": 1,
                "default_messaging_profile_id": "default_messaging_profile_id",
                "delivery_status_webhook_url": "delivery_status_webhook_url",
            },
            model="model",
            name="name",
            privacy_settings={"data_retention": True},
            promote_to_main=True,
            telephony_settings={
                "default_texml_app_id": "default_texml_app_id",
                "noise_suppression": "krisp",
                "noise_suppression_config": {
                    "attenuation_limit": 0,
                    "mode": "advanced",
                },
                "supports_unauthenticated_web_calls": True,
                "time_limit_secs": 30,
                "user_idle_timeout_secs": 30,
                "voicemail_detection": {
                    "on_voicemail_detected": {
                        "action": "stop_assistant",
                        "voicemail_message": {
                            "message": "message",
                            "prompt": "prompt",
                            "type": "prompt",
                        },
                    }
                },
            },
            tools=[
                {
                    "type": "webhook",
                    "webhook": {
                        "description": "description",
                        "name": "name",
                        "url": "https://example.com/api/v1/function",
                        "async": True,
                        "body_parameters": {
                            "properties": {
                                "age": "bar",
                                "location": "bar",
                            },
                            "required": ["age", "location"],
                            "type": "object",
                        },
                        "headers": [
                            {
                                "name": "name",
                                "value": "value",
                            }
                        ],
                        "method": "GET",
                        "path_parameters": {
                            "properties": {"id": "bar"},
                            "required": ["id"],
                            "type": "object",
                        },
                        "query_parameters": {
                            "properties": {"page": "bar"},
                            "required": ["page"],
                            "type": "object",
                        },
                        "timeout_ms": 500,
                    },
                }
            ],
            transcription={
                "language": "language",
                "model": "deepgram/flux",
                "region": "region",
                "settings": {
                    "eager_eot_threshold": 0.3,
                    "eot_threshold": 0,
                    "eot_timeout_ms": 0,
                    "numerals": True,
                    "smart_format": True,
                },
            },
            voice_settings={
                "voice": "voice",
                "api_key_ref": "api_key_ref",
                "background_audio": {
                    "type": "predefined_media",
                    "value": "silence",
                },
                "similarity_boost": 0,
                "speed": 0,
                "style": 0,
                "temperature": 0,
                "use_speaker_boost": True,
                "voice_speed": 0,
            },
            widget_settings={
                "agent_thinking_text": "agent_thinking_text",
                "audio_visualizer_config": {
                    "color": "verdant",
                    "preset": "preset",
                },
                "default_state": "expanded",
                "give_feedback_url": "give_feedback_url",
                "logo_icon_url": "logo_icon_url",
                "position": "fixed",
                "report_issue_url": "report_issue_url",
                "speak_to_interrupt_text": "speak_to_interrupt_text",
                "start_call_text": "start_call_text",
                "theme": "light",
                "view_history_url": "view_history_url",
            },
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.with_raw_response.update(
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.with_streaming_response.update(
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(InferenceEmbedding, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.with_raw_response.update(
                assistant_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.list()
        assert_matches_type(AssistantsList, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(AssistantsList, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(AssistantsList, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.delete(
            "assistant_id",
        )
        assert_matches_type(AssistantDeleteResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.with_raw_response.delete(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(AssistantDeleteResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.with_streaming_response.delete(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(AssistantDeleteResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_chat(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.chat(
            assistant_id="assistant_id",
            content="Tell me a joke about cats",
            conversation_id="42b20469-1215-4a9a-8964-c36f66b406f4",
        )
        assert_matches_type(AssistantChatResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.chat(
            assistant_id="assistant_id",
            content="Tell me a joke about cats",
            conversation_id="42b20469-1215-4a9a-8964-c36f66b406f4",
            name="Charlie",
        )
        assert_matches_type(AssistantChatResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.with_raw_response.chat(
            assistant_id="assistant_id",
            content="Tell me a joke about cats",
            conversation_id="42b20469-1215-4a9a-8964-c36f66b406f4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(AssistantChatResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.with_streaming_response.chat(
            assistant_id="assistant_id",
            content="Tell me a joke about cats",
            conversation_id="42b20469-1215-4a9a-8964-c36f66b406f4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(AssistantChatResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_chat(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.with_raw_response.chat(
                assistant_id="",
                content="Tell me a joke about cats",
                conversation_id="42b20469-1215-4a9a-8964-c36f66b406f4",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.clone(
            "assistant_id",
        )
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.with_raw_response.clone(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(InferenceEmbedding, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.with_streaming_response.clone(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(InferenceEmbedding, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_clone(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.with_raw_response.clone(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_texml(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.get_texml(
            "assistant_id",
        )
        assert_matches_type(str, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_texml(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.with_raw_response.get_texml(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(str, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_texml(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.with_streaming_response.get_texml(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(str, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_texml(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.with_raw_response.get_texml(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_imports(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.imports(
            api_key_ref="api_key_ref",
            provider="elevenlabs",
        )
        assert_matches_type(AssistantsList, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_imports_with_all_params(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.imports(
            api_key_ref="api_key_ref",
            provider="elevenlabs",
            import_ids=["string"],
        )
        assert_matches_type(AssistantsList, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_imports(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.with_raw_response.imports(
            api_key_ref="api_key_ref",
            provider="elevenlabs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(AssistantsList, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_imports(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.with_streaming_response.imports(
            api_key_ref="api_key_ref",
            provider="elevenlabs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(AssistantsList, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_sms(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.send_sms(
            assistant_id="assistant_id",
            from_="from",
            to="to",
        )
        assert_matches_type(AssistantSendSMSResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_sms_with_all_params(self, async_client: AsyncTelnyx) -> None:
        assistant = await async_client.ai.assistants.send_sms(
            assistant_id="assistant_id",
            from_="from",
            to="to",
            conversation_metadata={"foo": "string"},
            should_create_conversation=True,
            text="text",
        )
        assert_matches_type(AssistantSendSMSResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_sms(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.with_raw_response.send_sms(
            assistant_id="assistant_id",
            from_="from",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(AssistantSendSMSResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_sms(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.with_streaming_response.send_sms(
            assistant_id="assistant_id",
            from_="from",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(AssistantSendSMSResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_send_sms(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.with_raw_response.send_sms(
                assistant_id="",
                from_="from",
                to="to",
            )
