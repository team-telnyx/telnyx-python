# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.agent_gateways import (
    KeyListResponse,
    KeyCreateResponse,
    AgentGatewayKeyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        key = client.agent_gateways.keys.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        key = client.agent_gateways.keys.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            budget_resets_every="30d",
            expires_in="30d",
            max_budget=20,
            max_parallel_requests=4,
            models=["GLM-5.3-Flash"],
            name="support-agent",
            requests_per_minute=60,
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            tokens_per_minute=1,
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.agent_gateways.keys.with_raw_response.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.agent_gateways.keys.with_streaming_response.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyCreateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.keys.with_raw_response.create(
                instance_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        key = client.agent_gateways.keys.update(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        key = client.agent_gateways.keys.update(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            blocked=True,
            budget_resets_every="30d",
            expires_in="30d",
            max_budget=0,
            max_parallel_requests=1,
            models=["x"],
            name="x",
            requests_per_minute=1,
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tokens_per_minute=1,
        )
        assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.agent_gateways.keys.with_raw_response.update(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.agent_gateways.keys.with_streaming_response.update(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.keys.with_raw_response.update(
                key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.agent_gateways.keys.with_raw_response.update(
                key_id="",
                instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        key = client.agent_gateways.keys.list(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        key = client.agent_gateways.keys.list(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.agent_gateways.keys.with_raw_response.list(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.agent_gateways.keys.with_streaming_response.list(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.keys.with_raw_response.list(
                instance_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        key = client.agent_gateways.keys.delete(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.agent_gateways.keys.with_raw_response.delete(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.agent_gateways.keys.with_streaming_response.delete(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.keys.with_raw_response.delete(
                key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.agent_gateways.keys.with_raw_response.delete(
                key_id="",
                instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            )


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.agent_gateways.keys.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.agent_gateways.keys.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            budget_resets_every="30d",
            expires_in="30d",
            max_budget=20,
            max_parallel_requests=4,
            models=["GLM-5.3-Flash"],
            name="support-agent",
            requests_per_minute=60,
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            tokens_per_minute=1,
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.keys.with_raw_response.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.keys.with_streaming_response.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyCreateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.keys.with_raw_response.create(
                instance_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.agent_gateways.keys.update(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.agent_gateways.keys.update(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            blocked=True,
            budget_resets_every="30d",
            expires_in="30d",
            max_budget=0,
            max_parallel_requests=1,
            models=["x"],
            name="x",
            requests_per_minute=1,
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tokens_per_minute=1,
        )
        assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.keys.with_raw_response.update(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.keys.with_streaming_response.update(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.keys.with_raw_response.update(
                key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.agent_gateways.keys.with_raw_response.update(
                key_id="",
                instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.agent_gateways.keys.list(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.agent_gateways.keys.list(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.keys.with_raw_response.list(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.keys.with_streaming_response.list(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.keys.with_raw_response.list(
                instance_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.agent_gateways.keys.delete(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.keys.with_raw_response.delete(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.keys.with_streaming_response.delete(
            key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(AgentGatewayKeyResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.keys.with_raw_response.delete(
                key_id="5f1c3a0e9b7d4c2a8e6f0b1d3c5a7e9f2b4d6c8a0e1f3a5c7e9b1d3f5a7c9e0b",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.agent_gateways.keys.with_raw_response.delete(
                key_id="",
                instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            )
