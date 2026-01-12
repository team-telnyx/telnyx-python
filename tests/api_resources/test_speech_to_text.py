# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeechToText:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_transcribe(self, client: Telnyx) -> None:
        speech_to_text = client.speech_to_text.transcribe(
            input_format="mp3",
            transcription_engine="Azure",
        )
        assert speech_to_text is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_transcribe_with_all_params(self, client: Telnyx) -> None:
        speech_to_text = client.speech_to_text.transcribe(
            input_format="mp3",
            transcription_engine="Azure",
            interim_results=True,
            language="language",
            model="fast",
        )
        assert speech_to_text is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_transcribe(self, client: Telnyx) -> None:
        response = client.speech_to_text.with_raw_response.transcribe(
            input_format="mp3",
            transcription_engine="Azure",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech_to_text = response.parse()
        assert speech_to_text is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_transcribe(self, client: Telnyx) -> None:
        with client.speech_to_text.with_streaming_response.transcribe(
            input_format="mp3",
            transcription_engine="Azure",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech_to_text = response.parse()
            assert speech_to_text is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSpeechToText:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_transcribe(self, async_client: AsyncTelnyx) -> None:
        speech_to_text = await async_client.speech_to_text.transcribe(
            input_format="mp3",
            transcription_engine="Azure",
        )
        assert speech_to_text is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_transcribe_with_all_params(self, async_client: AsyncTelnyx) -> None:
        speech_to_text = await async_client.speech_to_text.transcribe(
            input_format="mp3",
            transcription_engine="Azure",
            interim_results=True,
            language="language",
            model="fast",
        )
        assert speech_to_text is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_transcribe(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.speech_to_text.with_raw_response.transcribe(
            input_format="mp3",
            transcription_engine="Azure",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech_to_text = await response.parse()
        assert speech_to_text is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_transcribe(self, async_client: AsyncTelnyx) -> None:
        async with async_client.speech_to_text.with_streaming_response.transcribe(
            input_format="mp3",
            transcription_engine="Azure",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech_to_text = await response.parse()
            assert speech_to_text is None

        assert cast(Any, response.is_closed) is True
