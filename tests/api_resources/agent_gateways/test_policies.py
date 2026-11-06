# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.agent_gateways import (
    PolicyListResponse,
    AgentGatewayPolicyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        policy = client.agent_gateways.policies.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="baseline",
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        policy = client.agent_gateways.policies.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="baseline",
            base="base",
            description="Mask personal data",
            guardrails={
                "add": ["mask-pii"],
                "remove": ["string"],
            },
            model="model",
            pipeline={
                "hook": "before_request",
                "steps": [
                    {
                        "guardrail": "guardrail",
                        "message": "message",
                        "on_error": "next",
                        "on_fail": "next",
                        "on_pass": "next",
                        "pass_data": True,
                    }
                ],
            },
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.agent_gateways.policies.with_raw_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="baseline",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.agent_gateways.policies.with_streaming_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="baseline",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.policies.with_raw_response.create(
                instance_id="",
                name="baseline",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        policy = client.agent_gateways.policies.retrieve(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.agent_gateways.policies.with_raw_response.retrieve(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.agent_gateways.policies.with_streaming_response.retrieve(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.policies.with_raw_response.retrieve(
                name="strict",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.agent_gateways.policies.with_raw_response.retrieve(
                name="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        policy = client.agent_gateways.policies.update(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        policy = client.agent_gateways.policies.update(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            base="base",
            description="Baseline plus a word check",
            guardrails={
                "add": ["string"],
                "remove": ["string"],
            },
            model="model",
            pipeline={
                "hook": "before_request",
                "steps": [
                    {
                        "guardrail": "guardrail",
                        "message": "message",
                        "on_error": "next",
                        "on_fail": "next",
                        "on_pass": "next",
                        "pass_data": True,
                    }
                ],
            },
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.agent_gateways.policies.with_raw_response.update(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.agent_gateways.policies.with_streaming_response.update(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.policies.with_raw_response.update(
                name="strict",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.agent_gateways.policies.with_raw_response.update(
                name="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        policy = client.agent_gateways.policies.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(PolicyListResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.agent_gateways.policies.with_raw_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyListResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.agent_gateways.policies.with_streaming_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyListResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.policies.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        policy = client.agent_gateways.policies.delete(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.agent_gateways.policies.with_raw_response.delete(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.agent_gateways.policies.with_streaming_response.delete(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.policies.with_raw_response.delete(
                name="strict",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.agent_gateways.policies.with_raw_response.delete(
                name="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        policy = await async_client.agent_gateways.policies.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="baseline",
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        policy = await async_client.agent_gateways.policies.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="baseline",
            base="base",
            description="Mask personal data",
            guardrails={
                "add": ["mask-pii"],
                "remove": ["string"],
            },
            model="model",
            pipeline={
                "hook": "before_request",
                "steps": [
                    {
                        "guardrail": "guardrail",
                        "message": "message",
                        "on_error": "next",
                        "on_fail": "next",
                        "on_pass": "next",
                        "pass_data": True,
                    }
                ],
            },
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.policies.with_raw_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="baseline",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.policies.with_streaming_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="baseline",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.policies.with_raw_response.create(
                instance_id="",
                name="baseline",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        policy = await async_client.agent_gateways.policies.retrieve(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.policies.with_raw_response.retrieve(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.policies.with_streaming_response.retrieve(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.policies.with_raw_response.retrieve(
                name="strict",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.agent_gateways.policies.with_raw_response.retrieve(
                name="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        policy = await async_client.agent_gateways.policies.update(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        policy = await async_client.agent_gateways.policies.update(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            base="base",
            description="Baseline plus a word check",
            guardrails={
                "add": ["string"],
                "remove": ["string"],
            },
            model="model",
            pipeline={
                "hook": "before_request",
                "steps": [
                    {
                        "guardrail": "guardrail",
                        "message": "message",
                        "on_error": "next",
                        "on_fail": "next",
                        "on_pass": "next",
                        "pass_data": True,
                    }
                ],
            },
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.policies.with_raw_response.update(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.policies.with_streaming_response.update(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.policies.with_raw_response.update(
                name="strict",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.agent_gateways.policies.with_raw_response.update(
                name="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        policy = await async_client.agent_gateways.policies.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(PolicyListResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.policies.with_raw_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyListResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.policies.with_streaming_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyListResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.policies.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        policy = await async_client.agent_gateways.policies.delete(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.policies.with_raw_response.delete(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.policies.with_streaming_response.delete(
            name="strict",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(AgentGatewayPolicyResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.policies.with_raw_response.delete(
                name="strict",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.agent_gateways.policies.with_raw_response.delete(
                name="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )
