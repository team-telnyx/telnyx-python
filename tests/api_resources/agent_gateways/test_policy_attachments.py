# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.agent_gateways import (
    PolicyAttachmentListResponse,
    AgentGatewayPolicyAttachmentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicyAttachments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        policy_attachment = client.agent_gateways.policy_attachments.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            policy="strict",
        )
        assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        policy_attachment = client.agent_gateways.policy_attachments.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            policy="strict",
            default=True,
            models=["GLM-5.3*"],
            priority=10,
        )
        assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.agent_gateways.policy_attachments.with_raw_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            policy="strict",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_attachment = response.parse()
        assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.agent_gateways.policy_attachments.with_streaming_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            policy="strict",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_attachment = response.parse()
            assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.policy_attachments.with_raw_response.create(
                instance_id="",
                policy="strict",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        policy_attachment = client.agent_gateways.policy_attachments.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(PolicyAttachmentListResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.agent_gateways.policy_attachments.with_raw_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_attachment = response.parse()
        assert_matches_type(PolicyAttachmentListResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.agent_gateways.policy_attachments.with_streaming_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_attachment = response.parse()
            assert_matches_type(PolicyAttachmentListResponse, policy_attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.policy_attachments.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        policy_attachment = client.agent_gateways.policy_attachments.delete(
            attachment_id="3394712f-2ad5-428a-8a3d-7a08d4b2906d",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.agent_gateways.policy_attachments.with_raw_response.delete(
            attachment_id="3394712f-2ad5-428a-8a3d-7a08d4b2906d",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_attachment = response.parse()
        assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.agent_gateways.policy_attachments.with_streaming_response.delete(
            attachment_id="3394712f-2ad5-428a-8a3d-7a08d4b2906d",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_attachment = response.parse()
            assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.policy_attachments.with_raw_response.delete(
                attachment_id="3394712f-2ad5-428a-8a3d-7a08d4b2906d",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            client.agent_gateways.policy_attachments.with_raw_response.delete(
                attachment_id="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )


class TestAsyncPolicyAttachments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        policy_attachment = await async_client.agent_gateways.policy_attachments.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            policy="strict",
        )
        assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        policy_attachment = await async_client.agent_gateways.policy_attachments.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            policy="strict",
            default=True,
            models=["GLM-5.3*"],
            priority=10,
        )
        assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.policy_attachments.with_raw_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            policy="strict",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_attachment = await response.parse()
        assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.policy_attachments.with_streaming_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            policy="strict",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_attachment = await response.parse()
            assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.policy_attachments.with_raw_response.create(
                instance_id="",
                policy="strict",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        policy_attachment = await async_client.agent_gateways.policy_attachments.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(PolicyAttachmentListResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.policy_attachments.with_raw_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_attachment = await response.parse()
        assert_matches_type(PolicyAttachmentListResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.policy_attachments.with_streaming_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_attachment = await response.parse()
            assert_matches_type(PolicyAttachmentListResponse, policy_attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.policy_attachments.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        policy_attachment = await async_client.agent_gateways.policy_attachments.delete(
            attachment_id="3394712f-2ad5-428a-8a3d-7a08d4b2906d",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.policy_attachments.with_raw_response.delete(
            attachment_id="3394712f-2ad5-428a-8a3d-7a08d4b2906d",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_attachment = await response.parse()
        assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.policy_attachments.with_streaming_response.delete(
            attachment_id="3394712f-2ad5-428a-8a3d-7a08d4b2906d",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_attachment = await response.parse()
            assert_matches_type(AgentGatewayPolicyAttachmentResponse, policy_attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.policy_attachments.with_raw_response.delete(
                attachment_id="3394712f-2ad5-428a-8a3d-7a08d4b2906d",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            await async_client.agent_gateways.policy_attachments.with_raw_response.delete(
                attachment_id="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )
