# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import CommunityTtsEngine
from telnyx.types.tts_integrations import CommunityTtsConformanceRun

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disable(self, client: Telnyx) -> None:
        action = client.tts_integrations.actions.disable(
            "id",
        )
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disable(self, client: Telnyx) -> None:
        response = client.tts_integrations.actions.with_raw_response.disable(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disable(self, client: Telnyx) -> None:
        with client.tts_integrations.actions.with_streaming_response.disable(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(CommunityTtsEngine, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disable(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tts_integrations.actions.with_raw_response.disable(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enable(self, client: Telnyx) -> None:
        action = client.tts_integrations.actions.enable(
            "id",
        )
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_enable(self, client: Telnyx) -> None:
        response = client.tts_integrations.actions.with_raw_response.enable(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_enable(self, client: Telnyx) -> None:
        with client.tts_integrations.actions.with_streaming_response.enable(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(CommunityTtsEngine, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_enable(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tts_integrations.actions.with_raw_response.enable(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refresh_voices(self, client: Telnyx) -> None:
        action = client.tts_integrations.actions.refresh_voices(
            "id",
        )
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_refresh_voices(self, client: Telnyx) -> None:
        response = client.tts_integrations.actions.with_raw_response.refresh_voices(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_refresh_voices(self, client: Telnyx) -> None:
        with client.tts_integrations.actions.with_streaming_response.refresh_voices(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(CommunityTtsEngine, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_refresh_voices(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tts_integrations.actions.with_raw_response.refresh_voices(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_review(self, client: Telnyx) -> None:
        action = client.tts_integrations.actions.request_review(
            "id",
        )
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_review(self, client: Telnyx) -> None:
        response = client.tts_integrations.actions.with_raw_response.request_review(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_review(self, client: Telnyx) -> None:
        with client.tts_integrations.actions.with_streaming_response.request_review(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(CommunityTtsEngine, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_request_review(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tts_integrations.actions.with_raw_response.request_review(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_connection(self, client: Telnyx) -> None:
        action = client.tts_integrations.actions.test_connection(
            id="id",
            api_key_ref="acme-engine-key",
        )
        assert_matches_type(CommunityTtsConformanceRun, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_connection_with_all_params(self, client: Telnyx) -> None:
        action = client.tts_integrations.actions.test_connection(
            id="id",
            api_key_ref="acme-engine-key",
            voice_id="alpha",
        )
        assert_matches_type(CommunityTtsConformanceRun, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test_connection(self, client: Telnyx) -> None:
        response = client.tts_integrations.actions.with_raw_response.test_connection(
            id="id",
            api_key_ref="acme-engine-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(CommunityTtsConformanceRun, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test_connection(self, client: Telnyx) -> None:
        with client.tts_integrations.actions.with_streaming_response.test_connection(
            id="id",
            api_key_ref="acme-engine-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(CommunityTtsConformanceRun, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test_connection(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tts_integrations.actions.with_raw_response.test_connection(
                id="",
                api_key_ref="acme-engine-key",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disable(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.tts_integrations.actions.disable(
            "id",
        )
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.actions.with_raw_response.disable(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.actions.with_streaming_response.disable(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(CommunityTtsEngine, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disable(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tts_integrations.actions.with_raw_response.disable(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enable(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.tts_integrations.actions.enable(
            "id",
        )
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.actions.with_raw_response.enable(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.actions.with_streaming_response.enable(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(CommunityTtsEngine, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_enable(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tts_integrations.actions.with_raw_response.enable(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refresh_voices(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.tts_integrations.actions.refresh_voices(
            "id",
        )
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_refresh_voices(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.actions.with_raw_response.refresh_voices(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_refresh_voices(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.actions.with_streaming_response.refresh_voices(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(CommunityTtsEngine, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_refresh_voices(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tts_integrations.actions.with_raw_response.refresh_voices(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_review(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.tts_integrations.actions.request_review(
            "id",
        )
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_review(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.actions.with_raw_response.request_review(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(CommunityTtsEngine, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_review(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.actions.with_streaming_response.request_review(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(CommunityTtsEngine, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_request_review(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tts_integrations.actions.with_raw_response.request_review(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_connection(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.tts_integrations.actions.test_connection(
            id="id",
            api_key_ref="acme-engine-key",
        )
        assert_matches_type(CommunityTtsConformanceRun, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_connection_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.tts_integrations.actions.test_connection(
            id="id",
            api_key_ref="acme-engine-key",
            voice_id="alpha",
        )
        assert_matches_type(CommunityTtsConformanceRun, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test_connection(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tts_integrations.actions.with_raw_response.test_connection(
            id="id",
            api_key_ref="acme-engine-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(CommunityTtsConformanceRun, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test_connection(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tts_integrations.actions.with_streaming_response.test_connection(
            id="id",
            api_key_ref="acme-engine-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(CommunityTtsConformanceRun, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test_connection(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tts_integrations.actions.with_raw_response.test_connection(
                id="",
                api_key_ref="acme-engine-key",
            )
