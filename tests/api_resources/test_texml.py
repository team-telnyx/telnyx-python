# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    TexmlSecretsResponse,
    TexmlInitiateAICallResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTexml:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_ai_call(self, client: Telnyx) -> None:
        texml = client.texml.initiate_ai_call(
            connection_id="connection_id",
            ai_assistant_id="ai-assistant-id-123",
            from_="+13120001234",
            to="+13121230000",
        )
        assert_matches_type(TexmlInitiateAICallResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_ai_call_with_all_params(self, client: Telnyx) -> None:
        texml = client.texml.initiate_ai_call(
            connection_id="connection_id",
            ai_assistant_id="ai-assistant-id-123",
            from_="+13120001234",
            to="+13121230000",
            ai_assistant_dynamic_variables={
                "customer_name": "John Doe",
                "account_id": "12345",
            },
            ai_assistant_version="AIAssistantVersion",
            async_amd=True,
            async_amd_status_callback="https://www.example.com/callback",
            async_amd_status_callback_method="GET",
            caller_id="Info",
            conversation_callback="https://www.example.com/conversation-callback",
            conversation_callback_method="GET",
            conversation_callbacks=[
                "https://www.example.com/conversation-callback1",
                "https://www.example.com/conversation-callback2",
            ],
            custom_headers=[
                {
                    "name": "X-Custom-Header",
                    "value": "custom-value",
                }
            ],
            detection_mode="Premium",
            machine_detection="Enable",
            machine_detection_silence_timeout=2000,
            machine_detection_speech_end_threshold=2000,
            machine_detection_speech_threshold=2000,
            machine_detection_timeout=5000,
            passports="Passports",
            preferred_codecs="PCMA,PCMU",
            record=False,
            recording_channels="dual",
            recording_status_callback="https://example.com/recording_status_callback",
            recording_status_callback_event="in-progress completed absent",
            recording_status_callback_method="GET",
            recording_timeout=5,
            recording_track="inbound",
            send_recording_url=False,
            sip_auth_password="1234",
            sip_auth_username="user",
            sip_region="Canada",
            status_callback="https://www.example.com/callback",
            status_callback_event="initiated answered",
            status_callback_method="GET",
            status_callbacks=["https://www.example.com/callback1", "https://www.example.com/callback2"],
            time_limit=3600,
            timeout_seconds=60,
            trim="trim-silence",
        )
        assert_matches_type(TexmlInitiateAICallResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_ai_call(self, client: Telnyx) -> None:
        response = client.texml.with_raw_response.initiate_ai_call(
            connection_id="connection_id",
            ai_assistant_id="ai-assistant-id-123",
            from_="+13120001234",
            to="+13121230000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml = response.parse()
        assert_matches_type(TexmlInitiateAICallResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_ai_call(self, client: Telnyx) -> None:
        with client.texml.with_streaming_response.initiate_ai_call(
            connection_id="connection_id",
            ai_assistant_id="ai-assistant-id-123",
            from_="+13120001234",
            to="+13121230000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml = response.parse()
            assert_matches_type(TexmlInitiateAICallResponse, texml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_initiate_ai_call(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.texml.with_raw_response.initiate_ai_call(
                connection_id="",
                ai_assistant_id="ai-assistant-id-123",
                from_="+13120001234",
                to="+13121230000",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_secrets(self, client: Telnyx) -> None:
        texml = client.texml.secrets(
            name="My Secret Name",
            value="My Secret Value",
        )
        assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_secrets(self, client: Telnyx) -> None:
        response = client.texml.with_raw_response.secrets(
            name="My Secret Name",
            value="My Secret Value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml = response.parse()
        assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_secrets(self, client: Telnyx) -> None:
        with client.texml.with_streaming_response.secrets(
            name="My Secret Name",
            value="My Secret Value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml = response.parse()
            assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTexml:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_ai_call(self, async_client: AsyncTelnyx) -> None:
        texml = await async_client.texml.initiate_ai_call(
            connection_id="connection_id",
            ai_assistant_id="ai-assistant-id-123",
            from_="+13120001234",
            to="+13121230000",
        )
        assert_matches_type(TexmlInitiateAICallResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_ai_call_with_all_params(self, async_client: AsyncTelnyx) -> None:
        texml = await async_client.texml.initiate_ai_call(
            connection_id="connection_id",
            ai_assistant_id="ai-assistant-id-123",
            from_="+13120001234",
            to="+13121230000",
            ai_assistant_dynamic_variables={
                "customer_name": "John Doe",
                "account_id": "12345",
            },
            ai_assistant_version="AIAssistantVersion",
            async_amd=True,
            async_amd_status_callback="https://www.example.com/callback",
            async_amd_status_callback_method="GET",
            caller_id="Info",
            conversation_callback="https://www.example.com/conversation-callback",
            conversation_callback_method="GET",
            conversation_callbacks=[
                "https://www.example.com/conversation-callback1",
                "https://www.example.com/conversation-callback2",
            ],
            custom_headers=[
                {
                    "name": "X-Custom-Header",
                    "value": "custom-value",
                }
            ],
            detection_mode="Premium",
            machine_detection="Enable",
            machine_detection_silence_timeout=2000,
            machine_detection_speech_end_threshold=2000,
            machine_detection_speech_threshold=2000,
            machine_detection_timeout=5000,
            passports="Passports",
            preferred_codecs="PCMA,PCMU",
            record=False,
            recording_channels="dual",
            recording_status_callback="https://example.com/recording_status_callback",
            recording_status_callback_event="in-progress completed absent",
            recording_status_callback_method="GET",
            recording_timeout=5,
            recording_track="inbound",
            send_recording_url=False,
            sip_auth_password="1234",
            sip_auth_username="user",
            sip_region="Canada",
            status_callback="https://www.example.com/callback",
            status_callback_event="initiated answered",
            status_callback_method="GET",
            status_callbacks=["https://www.example.com/callback1", "https://www.example.com/callback2"],
            time_limit=3600,
            timeout_seconds=60,
            trim="trim-silence",
        )
        assert_matches_type(TexmlInitiateAICallResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_ai_call(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.with_raw_response.initiate_ai_call(
            connection_id="connection_id",
            ai_assistant_id="ai-assistant-id-123",
            from_="+13120001234",
            to="+13121230000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml = await response.parse()
        assert_matches_type(TexmlInitiateAICallResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_ai_call(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.with_streaming_response.initiate_ai_call(
            connection_id="connection_id",
            ai_assistant_id="ai-assistant-id-123",
            from_="+13120001234",
            to="+13121230000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml = await response.parse()
            assert_matches_type(TexmlInitiateAICallResponse, texml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_initiate_ai_call(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.texml.with_raw_response.initiate_ai_call(
                connection_id="",
                ai_assistant_id="ai-assistant-id-123",
                from_="+13120001234",
                to="+13121230000",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_secrets(self, async_client: AsyncTelnyx) -> None:
        texml = await async_client.texml.secrets(
            name="My Secret Name",
            value="My Secret Value",
        )
        assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_secrets(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.with_raw_response.secrets(
            name="My Secret Name",
            value="My Secret Value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml = await response.parse()
        assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_secrets(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.with_streaming_response.secrets(
            name="My Secret Name",
            value="My Secret Value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml = await response.parse()
            assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

        assert cast(Any, response.is_closed) is True
