# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    CommunityTtsEngine,
    TtsIntegrationListResponse,
    TtsIntegrationRetrieveVoicesResponse,
    TtsIntegrationRetrieveDiscoverableResponse,
    TtsIntegrationRetrieveConformanceRunsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTtsIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.create(
            capabilities={"streamed_audio": True},
            name="acme",
            supported_audio_formats=["linear16"],
            voices_url="https://tts.acme.example/voices",
            websocket_url="wss://tts.acme.example/v1",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.create(
            capabilities={
                "streamed_audio": True,
                "flush_support": True,
                "force_interrupt_support": True,
                "ssml_support": True,
                "voice_settings_schema": {
                    "voice_speed": {},
                    "emotion": {},
                },
            },
            name="acme",
            supported_audio_formats=["linear16"],
            voices_url="https://tts.acme.example/voices",
            websocket_url="wss://tts.acme.example/v1",
            connect_timeout_ms=500,
            contact_email="contact_email",
            data_retention_policy_url="data_retention_policy_url",
            documentation_url="https://tts.acme.example/docs",
            visibility="private",
            voices_api_key_ref="voices_api_key_ref",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.tts_integrations.with_raw_response.create(
            capabilities={"streamed_audio": True},
            name="acme",
            supported_audio_formats=["linear16"],
            voices_url="https://tts.acme.example/voices",
            websocket_url="wss://tts.acme.example/v1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = response.parse()
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.tts_integrations.with_streaming_response.create(
            capabilities={"streamed_audio": True},
            name="acme",
            supported_audio_formats=["linear16"],
            voices_url="https://tts.acme.example/voices",
            websocket_url="wss://tts.acme.example/v1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = response.parse()
            assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.retrieve(
            "id",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.tts_integrations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = response.parse()
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.tts_integrations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = response.parse()
            assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tts_integrations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.update(
            id="id",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.update(
            id="id",
            capabilities={
                "streamed_audio": True,
                "flush_support": True,
                "force_interrupt_support": True,
                "ssml_support": True,
                "voice_settings_schema": {
                    "voice_speed": {},
                    "emotion": {},
                },
            },
            connect_timeout_ms=500,
            contact_email="contact_email",
            data_retention_policy_url="data_retention_policy_url",
            documentation_url="https://",
            supported_audio_formats=["mp3"],
            visibility="public",
            voices_api_key_ref="voices_api_key_ref",
            voices_url="https://",
            websocket_url="wss://",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.tts_integrations.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = response.parse()
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.tts_integrations.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = response.parse()
            assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tts_integrations.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.list()
        assert_matches_type(TtsIntegrationListResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.list(
            page={
                "number": 1,
                "size": 20,
            },
            status="draft",
            visibility="private",
        )
        assert_matches_type(TtsIntegrationListResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.tts_integrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = response.parse()
        assert_matches_type(TtsIntegrationListResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.tts_integrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = response.parse()
            assert_matches_type(TtsIntegrationListResponse, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.delete(
            "id",
        )
        assert tts_integration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.tts_integrations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = response.parse()
        assert tts_integration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.tts_integrations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = response.parse()
            assert tts_integration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tts_integrations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.replace(
            id="id",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.replace(
            id="id",
            capabilities={
                "streamed_audio": True,
                "flush_support": True,
                "force_interrupt_support": True,
                "ssml_support": True,
                "voice_settings_schema": {
                    "voice_speed": {},
                    "emotion": {},
                },
            },
            connect_timeout_ms=500,
            contact_email="voices@acme.example",
            data_retention_policy_url="data_retention_policy_url",
            documentation_url="https://tts.acme.example/docs",
            supported_audio_formats=["mp3"],
            visibility="private",
            voices_api_key_ref="voices_api_key_ref",
            voices_url="https://",
            websocket_url="wss://",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Telnyx) -> None:
        response = client.tts_integrations.with_raw_response.replace(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = response.parse()
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Telnyx) -> None:
        with client.tts_integrations.with_streaming_response.replace(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = response.parse()
            assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tts_integrations.with_raw_response.replace(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_conformance_runs(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.retrieve_conformance_runs(
            id="id",
        )
        assert_matches_type(TtsIntegrationRetrieveConformanceRunsResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_conformance_runs_with_all_params(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.retrieve_conformance_runs(
            id="id",
            page={
                "number": 1,
                "size": 20,
            },
        )
        assert_matches_type(TtsIntegrationRetrieveConformanceRunsResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_conformance_runs(self, client: Telnyx) -> None:
        response = client.tts_integrations.with_raw_response.retrieve_conformance_runs(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = response.parse()
        assert_matches_type(TtsIntegrationRetrieveConformanceRunsResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_conformance_runs(self, client: Telnyx) -> None:
        with client.tts_integrations.with_streaming_response.retrieve_conformance_runs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = response.parse()
            assert_matches_type(TtsIntegrationRetrieveConformanceRunsResponse, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_conformance_runs(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tts_integrations.with_raw_response.retrieve_conformance_runs(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_discoverable(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.retrieve_discoverable()
        assert_matches_type(TtsIntegrationRetrieveDiscoverableResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_discoverable_with_all_params(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.retrieve_discoverable(
            page={
                "number": 1,
                "size": 20,
            },
            status="draft",
            visibility="private",
        )
        assert_matches_type(TtsIntegrationRetrieveDiscoverableResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_discoverable(self, client: Telnyx) -> None:
        response = client.tts_integrations.with_raw_response.retrieve_discoverable()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = response.parse()
        assert_matches_type(TtsIntegrationRetrieveDiscoverableResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_discoverable(self, client: Telnyx) -> None:
        with client.tts_integrations.with_streaming_response.retrieve_discoverable() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = response.parse()
            assert_matches_type(TtsIntegrationRetrieveDiscoverableResponse, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_voices(self, client: Telnyx) -> None:
        tts_integration = client.tts_integrations.retrieve_voices(
            "id",
        )
        assert_matches_type(TtsIntegrationRetrieveVoicesResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_voices(self, client: Telnyx) -> None:
        response = client.tts_integrations.with_raw_response.retrieve_voices(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = response.parse()
        assert_matches_type(TtsIntegrationRetrieveVoicesResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_voices(self, client: Telnyx) -> None:
        with client.tts_integrations.with_streaming_response.retrieve_voices(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = response.parse()
            assert_matches_type(TtsIntegrationRetrieveVoicesResponse, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_voices(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tts_integrations.with_raw_response.retrieve_voices(
                "",
            )


class TestAsyncTtsIntegrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.create(
            capabilities={"streamed_audio": True},
            name="acme",
            supported_audio_formats=["linear16"],
            voices_url="https://tts.acme.example/voices",
            websocket_url="wss://tts.acme.example/v1",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.create(
            capabilities={
                "streamed_audio": True,
                "flush_support": True,
                "force_interrupt_support": True,
                "ssml_support": True,
                "voice_settings_schema": {
                    "voice_speed": {},
                    "emotion": {},
                },
            },
            name="acme",
            supported_audio_formats=["linear16"],
            voices_url="https://tts.acme.example/voices",
            websocket_url="wss://tts.acme.example/v1",
            connect_timeout_ms=500,
            contact_email="contact_email",
            data_retention_policy_url="data_retention_policy_url",
            documentation_url="https://tts.acme.example/docs",
            visibility="private",
            voices_api_key_ref="voices_api_key_ref",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.with_raw_response.create(
            capabilities={"streamed_audio": True},
            name="acme",
            supported_audio_formats=["linear16"],
            voices_url="https://tts.acme.example/voices",
            websocket_url="wss://tts.acme.example/v1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = await response.parse()
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.with_streaming_response.create(
            capabilities={"streamed_audio": True},
            name="acme",
            supported_audio_formats=["linear16"],
            voices_url="https://tts.acme.example/voices",
            websocket_url="wss://tts.acme.example/v1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = await response.parse()
            assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.retrieve(
            "id",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = await response.parse()
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = await response.parse()
            assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tts_integrations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.update(
            id="id",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.update(
            id="id",
            capabilities={
                "streamed_audio": True,
                "flush_support": True,
                "force_interrupt_support": True,
                "ssml_support": True,
                "voice_settings_schema": {
                    "voice_speed": {},
                    "emotion": {},
                },
            },
            connect_timeout_ms=500,
            contact_email="contact_email",
            data_retention_policy_url="data_retention_policy_url",
            documentation_url="https://",
            supported_audio_formats=["mp3"],
            visibility="public",
            voices_api_key_ref="voices_api_key_ref",
            voices_url="https://",
            websocket_url="wss://",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = await response.parse()
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = await response.parse()
            assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tts_integrations.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.list()
        assert_matches_type(TtsIntegrationListResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.list(
            page={
                "number": 1,
                "size": 20,
            },
            status="draft",
            visibility="private",
        )
        assert_matches_type(TtsIntegrationListResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = await response.parse()
        assert_matches_type(TtsIntegrationListResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = await response.parse()
            assert_matches_type(TtsIntegrationListResponse, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.delete(
            "id",
        )
        assert tts_integration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = await response.parse()
        assert tts_integration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = await response.parse()
            assert tts_integration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tts_integrations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.replace(
            id="id",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.replace(
            id="id",
            capabilities={
                "streamed_audio": True,
                "flush_support": True,
                "force_interrupt_support": True,
                "ssml_support": True,
                "voice_settings_schema": {
                    "voice_speed": {},
                    "emotion": {},
                },
            },
            connect_timeout_ms=500,
            contact_email="voices@acme.example",
            data_retention_policy_url="data_retention_policy_url",
            documentation_url="https://tts.acme.example/docs",
            supported_audio_formats=["mp3"],
            visibility="private",
            voices_api_key_ref="voices_api_key_ref",
            voices_url="https://",
            websocket_url="wss://",
        )
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.with_raw_response.replace(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = await response.parse()
        assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.with_streaming_response.replace(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = await response.parse()
            assert_matches_type(CommunityTtsEngine, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tts_integrations.with_raw_response.replace(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_conformance_runs(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.retrieve_conformance_runs(
            id="id",
        )
        assert_matches_type(TtsIntegrationRetrieveConformanceRunsResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_conformance_runs_with_all_params(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.retrieve_conformance_runs(
            id="id",
            page={
                "number": 1,
                "size": 20,
            },
        )
        assert_matches_type(TtsIntegrationRetrieveConformanceRunsResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_conformance_runs(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.with_raw_response.retrieve_conformance_runs(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = await response.parse()
        assert_matches_type(TtsIntegrationRetrieveConformanceRunsResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_conformance_runs(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.with_streaming_response.retrieve_conformance_runs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = await response.parse()
            assert_matches_type(TtsIntegrationRetrieveConformanceRunsResponse, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_conformance_runs(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tts_integrations.with_raw_response.retrieve_conformance_runs(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_discoverable(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.retrieve_discoverable()
        assert_matches_type(TtsIntegrationRetrieveDiscoverableResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_discoverable_with_all_params(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.retrieve_discoverable(
            page={
                "number": 1,
                "size": 20,
            },
            status="draft",
            visibility="private",
        )
        assert_matches_type(TtsIntegrationRetrieveDiscoverableResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_discoverable(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.with_raw_response.retrieve_discoverable()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = await response.parse()
        assert_matches_type(TtsIntegrationRetrieveDiscoverableResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_discoverable(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.with_streaming_response.retrieve_discoverable() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = await response.parse()
            assert_matches_type(TtsIntegrationRetrieveDiscoverableResponse, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_voices(self, async_client: AsyncTelnyx) -> None:
        tts_integration = await async_client.tts_integrations.retrieve_voices(
            "id",
        )
        assert_matches_type(TtsIntegrationRetrieveVoicesResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_voices(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.with_raw_response.retrieve_voices(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tts_integration = await response.parse()
        assert_matches_type(TtsIntegrationRetrieveVoicesResponse, tts_integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_voices(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.with_streaming_response.retrieve_voices(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tts_integration = await response.parse()
            assert_matches_type(TtsIntegrationRetrieveVoicesResponse, tts_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_voices(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tts_integrations.with_raw_response.retrieve_voices(
                "",
            )
