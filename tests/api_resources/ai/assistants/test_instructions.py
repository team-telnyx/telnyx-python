# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstructions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enhance(self, client: Telnyx) -> None:
        instruction = client.ai.assistants.instructions.enhance(
            assistant_id="assistant_id",
        )
        assert_matches_type(str, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enhance_with_all_params(self, client: Telnyx) -> None:
        instruction = client.ai.assistants.instructions.enhance(
            assistant_id="assistant_id",
            enhancement_prompt="enhancement_prompt",
            instructions="instructions",
        )
        assert_matches_type(str, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_enhance(self, client: Telnyx) -> None:
        response = client.ai.assistants.instructions.with_raw_response.enhance(
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = response.parse()
        assert_matches_type(str, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_enhance(self, client: Telnyx) -> None:
        with client.ai.assistants.instructions.with_streaming_response.enhance(
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instruction = response.parse()
            assert_matches_type(str, instruction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_enhance(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.instructions.with_raw_response.enhance(
                assistant_id="",
            )


class TestAsyncInstructions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enhance(self, async_client: AsyncTelnyx) -> None:
        instruction = await async_client.ai.assistants.instructions.enhance(
            assistant_id="assistant_id",
        )
        assert_matches_type(str, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enhance_with_all_params(self, async_client: AsyncTelnyx) -> None:
        instruction = await async_client.ai.assistants.instructions.enhance(
            assistant_id="assistant_id",
            enhancement_prompt="enhancement_prompt",
            instructions="instructions",
        )
        assert_matches_type(str, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_enhance(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.instructions.with_raw_response.enhance(
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = await response.parse()
        assert_matches_type(str, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_enhance(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.instructions.with_streaming_response.enhance(
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instruction = await response.parse()
            assert_matches_type(str, instruction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_enhance(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.instructions.with_raw_response.enhance(
                assistant_id="",
            )
