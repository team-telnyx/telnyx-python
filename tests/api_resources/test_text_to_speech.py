# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    TextToSpeechGenerateResponse,
    TextToSpeechListVoicesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTextToSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate(self, client: Telnyx) -> None:
        text_to_speech = client.text_to_speech.generate()
        assert_matches_type(TextToSpeechGenerateResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_with_all_params(self, client: Telnyx) -> None:
        text_to_speech = client.text_to_speech.generate(
            aws={
                "language_code": "language_code",
                "lexicon_names": ["string"],
                "output_format": "output_format",
                "sample_rate": "sample_rate",
                "text_type": "text",
            },
            azure={
                "api_key": "api_key",
                "deployment_id": "deployment_id",
                "effect": "effect",
                "gender": "gender",
                "language_code": "language_code",
                "output_format": "output_format",
                "region": "region",
                "text_type": "text",
            },
            disable_cache=True,
            elevenlabs={
                "api_key": "api_key",
                "language_code": "language_code",
                "voice_settings": {"foo": "bar"},
            },
            inworld={"foo": "bar"},
            language="language",
            minimax={
                "language_boost": "language_boost",
                "pitch": 0,
                "response_format": "response_format",
                "speed": 0,
                "vol": 0,
            },
            output_type="binary_output",
            provider="aws",
            resemble={
                "api_key": "api_key",
                "format": "format",
                "precision": "precision",
                "sample_rate": "sample_rate",
            },
            rime={
                "response_format": "response_format",
                "sampling_rate": 0,
                "voice_speed": 0,
            },
            telnyx={
                "response_format": "response_format",
                "sampling_rate": 0,
                "temperature": 0,
                "voice_speed": 0,
            },
            text="text",
            text_type="text",
            voice="voice",
            voice_settings={"foo": "bar"},
        )
        assert_matches_type(TextToSpeechGenerateResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate(self, client: Telnyx) -> None:
        response = client.text_to_speech.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = response.parse()
        assert_matches_type(TextToSpeechGenerateResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate(self, client: Telnyx) -> None:
        with client.text_to_speech.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = response.parse()
            assert_matches_type(TextToSpeechGenerateResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_voices(self, client: Telnyx) -> None:
        text_to_speech = client.text_to_speech.list_voices()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_voices_with_all_params(self, client: Telnyx) -> None:
        text_to_speech = client.text_to_speech.list_voices(
            api_key="api_key",
            provider="aws",
        )
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_voices(self, client: Telnyx) -> None:
        response = client.text_to_speech.with_raw_response.list_voices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = response.parse()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_voices(self, client: Telnyx) -> None:
        with client.text_to_speech.with_streaming_response.list_voices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = response.parse()
            assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream(self, client: Telnyx) -> None:
        text_to_speech = client.text_to_speech.stream()
        assert text_to_speech is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_with_all_params(self, client: Telnyx) -> None:
        text_to_speech = client.text_to_speech.stream(
            audio_format="pcm",
            disable_cache=True,
            model_id="model_id",
            provider="aws",
            socket_id="socket_id",
            voice="voice",
            voice_id="voice_id",
        )
        assert text_to_speech is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream(self, client: Telnyx) -> None:
        response = client.text_to_speech.with_raw_response.stream()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = response.parse()
        assert text_to_speech is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream(self, client: Telnyx) -> None:
        with client.text_to_speech.with_streaming_response.stream() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = response.parse()
            assert text_to_speech is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTextToSpeech:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate(self, async_client: AsyncTelnyx) -> None:
        text_to_speech = await async_client.text_to_speech.generate()
        assert_matches_type(TextToSpeechGenerateResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncTelnyx) -> None:
        text_to_speech = await async_client.text_to_speech.generate(
            aws={
                "language_code": "language_code",
                "lexicon_names": ["string"],
                "output_format": "output_format",
                "sample_rate": "sample_rate",
                "text_type": "text",
            },
            azure={
                "api_key": "api_key",
                "deployment_id": "deployment_id",
                "effect": "effect",
                "gender": "gender",
                "language_code": "language_code",
                "output_format": "output_format",
                "region": "region",
                "text_type": "text",
            },
            disable_cache=True,
            elevenlabs={
                "api_key": "api_key",
                "language_code": "language_code",
                "voice_settings": {"foo": "bar"},
            },
            inworld={"foo": "bar"},
            language="language",
            minimax={
                "language_boost": "language_boost",
                "pitch": 0,
                "response_format": "response_format",
                "speed": 0,
                "vol": 0,
            },
            output_type="binary_output",
            provider="aws",
            resemble={
                "api_key": "api_key",
                "format": "format",
                "precision": "precision",
                "sample_rate": "sample_rate",
            },
            rime={
                "response_format": "response_format",
                "sampling_rate": 0,
                "voice_speed": 0,
            },
            telnyx={
                "response_format": "response_format",
                "sampling_rate": 0,
                "temperature": 0,
                "voice_speed": 0,
            },
            text="text",
            text_type="text",
            voice="voice",
            voice_settings={"foo": "bar"},
        )
        assert_matches_type(TextToSpeechGenerateResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.text_to_speech.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = await response.parse()
        assert_matches_type(TextToSpeechGenerateResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncTelnyx) -> None:
        async with async_client.text_to_speech.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = await response.parse()
            assert_matches_type(TextToSpeechGenerateResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_voices(self, async_client: AsyncTelnyx) -> None:
        text_to_speech = await async_client.text_to_speech.list_voices()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_voices_with_all_params(self, async_client: AsyncTelnyx) -> None:
        text_to_speech = await async_client.text_to_speech.list_voices(
            api_key="api_key",
            provider="aws",
        )
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_voices(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.text_to_speech.with_raw_response.list_voices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = await response.parse()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_voices(self, async_client: AsyncTelnyx) -> None:
        async with async_client.text_to_speech.with_streaming_response.list_voices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = await response.parse()
            assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream(self, async_client: AsyncTelnyx) -> None:
        text_to_speech = await async_client.text_to_speech.stream()
        assert text_to_speech is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncTelnyx) -> None:
        text_to_speech = await async_client.text_to_speech.stream(
            audio_format="pcm",
            disable_cache=True,
            model_id="model_id",
            provider="aws",
            socket_id="socket_id",
            voice="voice",
            voice_id="voice_id",
        )
        assert text_to_speech is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.text_to_speech.with_raw_response.stream()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = await response.parse()
        assert text_to_speech is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncTelnyx) -> None:
        async with async_client.text_to_speech.with_streaming_response.stream() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = await response.parse()
            assert text_to_speech is None

        assert cast(Any, response.is_closed) is True
