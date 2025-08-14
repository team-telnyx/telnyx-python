# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai import AudioTranscribeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudio:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_transcribe(self, client: Telnyx) -> None:
        audio = client.ai.audio.transcribe(
            model="distil-whisper/distil-large-v2",
        )
        assert_matches_type(AudioTranscribeResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_transcribe_with_all_params(self, client: Telnyx) -> None:
        audio = client.ai.audio.transcribe(
            model="distil-whisper/distil-large-v2",
            file=b"raw file contents",
            file_url="https://example.com/file.mp3",
            response_format="json",
            timestamp_granularities="segment",
        )
        assert_matches_type(AudioTranscribeResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_transcribe(self, client: Telnyx) -> None:
        response = client.ai.audio.with_raw_response.transcribe(
            model="distil-whisper/distil-large-v2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = response.parse()
        assert_matches_type(AudioTranscribeResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_transcribe(self, client: Telnyx) -> None:
        with client.ai.audio.with_streaming_response.transcribe(
            model="distil-whisper/distil-large-v2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = response.parse()
            assert_matches_type(AudioTranscribeResponse, audio, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAudio:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_transcribe(self, async_client: AsyncTelnyx) -> None:
        audio = await async_client.ai.audio.transcribe(
            model="distil-whisper/distil-large-v2",
        )
        assert_matches_type(AudioTranscribeResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_transcribe_with_all_params(self, async_client: AsyncTelnyx) -> None:
        audio = await async_client.ai.audio.transcribe(
            model="distil-whisper/distil-large-v2",
            file=b"raw file contents",
            file_url="https://example.com/file.mp3",
            response_format="json",
            timestamp_granularities="segment",
        )
        assert_matches_type(AudioTranscribeResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_transcribe(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.audio.with_raw_response.transcribe(
            model="distil-whisper/distil-large-v2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = await response.parse()
        assert_matches_type(AudioTranscribeResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_transcribe(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.audio.with_streaming_response.transcribe(
            model="distil-whisper/distil-large-v2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = await response.parse()
            assert_matches_type(AudioTranscribeResponse, audio, path=["response"])

        assert cast(Any, response.is_closed) is True
