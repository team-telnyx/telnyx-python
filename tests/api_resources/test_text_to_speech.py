# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    TextToSpeechListVoicesResponse,
)
from telnyx._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTextToSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_generate_speech(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/text-to-speech/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        text_to_speech = client.text_to_speech.generate_speech(
            text="text",
            voice="voice",
        )
        assert text_to_speech.is_closed
        assert text_to_speech.json() == {"foo": "bar"}
        assert cast(Any, text_to_speech.is_closed) is True
        assert isinstance(text_to_speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_generate_speech(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/text-to-speech/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        text_to_speech = client.text_to_speech.with_raw_response.generate_speech(
            text="text",
            voice="voice",
        )

        assert text_to_speech.is_closed is True
        assert text_to_speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert text_to_speech.json() == {"foo": "bar"}
        assert isinstance(text_to_speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_generate_speech(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/text-to-speech/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.text_to_speech.with_streaming_response.generate_speech(
            text="text",
            voice="voice",
        ) as text_to_speech:
            assert not text_to_speech.is_closed
            assert text_to_speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert text_to_speech.json() == {"foo": "bar"}
            assert cast(Any, text_to_speech.is_closed) is True
            assert isinstance(text_to_speech, StreamedBinaryAPIResponse)

        assert cast(Any, text_to_speech.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_voices(self, client: Telnyx) -> None:
        text_to_speech = client.text_to_speech.list_voices()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_voices_with_all_params(self, client: Telnyx) -> None:
        text_to_speech = client.text_to_speech.list_voices(
            elevenlabs_api_key_ref="elevenlabs_api_key_ref",
            provider="aws",
        )
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_voices(self, client: Telnyx) -> None:
        response = client.text_to_speech.with_raw_response.list_voices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = response.parse()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_voices(self, client: Telnyx) -> None:
        with client.text_to_speech.with_streaming_response.list_voices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = response.parse()
            assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTextToSpeech:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_generate_speech(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/text-to-speech/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        text_to_speech = await async_client.text_to_speech.generate_speech(
            text="text",
            voice="voice",
        )
        assert text_to_speech.is_closed
        assert await text_to_speech.json() == {"foo": "bar"}
        assert cast(Any, text_to_speech.is_closed) is True
        assert isinstance(text_to_speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_generate_speech(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/text-to-speech/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        text_to_speech = await async_client.text_to_speech.with_raw_response.generate_speech(
            text="text",
            voice="voice",
        )

        assert text_to_speech.is_closed is True
        assert text_to_speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await text_to_speech.json() == {"foo": "bar"}
        assert isinstance(text_to_speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_generate_speech(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/text-to-speech/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.text_to_speech.with_streaming_response.generate_speech(
            text="text",
            voice="voice",
        ) as text_to_speech:
            assert not text_to_speech.is_closed
            assert text_to_speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await text_to_speech.json() == {"foo": "bar"}
            assert cast(Any, text_to_speech.is_closed) is True
            assert isinstance(text_to_speech, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, text_to_speech.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_voices(self, async_client: AsyncTelnyx) -> None:
        text_to_speech = await async_client.text_to_speech.list_voices()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_voices_with_all_params(self, async_client: AsyncTelnyx) -> None:
        text_to_speech = await async_client.text_to_speech.list_voices(
            elevenlabs_api_key_ref="elevenlabs_api_key_ref",
            provider="aws",
        )
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_voices(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.text_to_speech.with_raw_response.list_voices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = await response.parse()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_voices(self, async_client: AsyncTelnyx) -> None:
        async with async_client.text_to_speech.with_streaming_response.list_voices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = await response.parse()
            assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True
