# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.tests.test_framework.v1 import (
    TestAgent,
    AiagentListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAiagents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        aiagent = client.ai.tests.test_framework.v1.aiagents.create(
            agent_name="Support Bot Under Test",
            assistant_id="e1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6",
        )
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        aiagent = client.ai.tests.test_framework.v1.aiagents.create(
            agent_name="Support Bot Under Test",
            assistant_id="e1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6",
            auto_fetch_calls_enabled=True,
            auto_sync_prompt_enabled=True,
            auto_update_dropoff_nodes=False,
            auto_update_topic_nodes=False,
            contact_number="contact_number",
            description="Evaluates the support assistant against generated callers.",
            inbound=False,
            language="en",
            llm_max_tokens=512,
            llm_model="openai/gpt-oss-120b",
            llm_system_prompt="llm_system_prompt",
            llm_temperature=0.7,
            outbound_auto_call=False,
            sip_endpoint="",
        )
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.aiagents.with_raw_response.create(
            agent_name="Support Bot Under Test",
            assistant_id="e1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aiagent = response.parse()
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.aiagents.with_streaming_response.create(
            agent_name="Support Bot Under Test",
            assistant_id="e1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aiagent = response.parse()
            assert_matches_type(TestAgent, aiagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        aiagent = client.ai.tests.test_framework.v1.aiagents.retrieve(
            0,
        )
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.aiagents.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aiagent = response.parse()
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.aiagents.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aiagent = response.parse()
            assert_matches_type(TestAgent, aiagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        aiagent = client.ai.tests.test_framework.v1.aiagents.update(
            id=0,
        )
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        aiagent = client.ai.tests.test_framework.v1.aiagents.update(
            id=0,
            agent_name="Support Bot Under Test - renamed",
            assistant_id="assistant_id",
            auto_fetch_calls_enabled=True,
            auto_sync_prompt_enabled=True,
            auto_update_dropoff_nodes=True,
            auto_update_topic_nodes=True,
            contact_number="contact_number",
            description="description",
            inbound=True,
            language="language",
            llm_max_tokens=256,
            llm_model="llm_model",
            llm_system_prompt="llm_system_prompt",
            llm_temperature=0.5,
            outbound_auto_call=True,
            sip_endpoint="sip_endpoint",
        )
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.aiagents.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aiagent = response.parse()
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.aiagents.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aiagent = response.parse()
            assert_matches_type(TestAgent, aiagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        aiagent = client.ai.tests.test_framework.v1.aiagents.list()
        assert_matches_type(AiagentListResponse, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        aiagent = client.ai.tests.test_framework.v1.aiagents.list(
            page=1,
            page_size=1,
        )
        assert_matches_type(AiagentListResponse, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.aiagents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aiagent = response.parse()
        assert_matches_type(AiagentListResponse, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.aiagents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aiagent = response.parse()
            assert_matches_type(AiagentListResponse, aiagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        aiagent = client.ai.tests.test_framework.v1.aiagents.delete(
            0,
        )
        assert_matches_type(object, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.aiagents.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aiagent = response.parse()
        assert_matches_type(object, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.aiagents.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aiagent = response.parse()
            assert_matches_type(object, aiagent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAiagents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        aiagent = await async_client.ai.tests.test_framework.v1.aiagents.create(
            agent_name="Support Bot Under Test",
            assistant_id="e1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6",
        )
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        aiagent = await async_client.ai.tests.test_framework.v1.aiagents.create(
            agent_name="Support Bot Under Test",
            assistant_id="e1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6",
            auto_fetch_calls_enabled=True,
            auto_sync_prompt_enabled=True,
            auto_update_dropoff_nodes=False,
            auto_update_topic_nodes=False,
            contact_number="contact_number",
            description="Evaluates the support assistant against generated callers.",
            inbound=False,
            language="en",
            llm_max_tokens=512,
            llm_model="openai/gpt-oss-120b",
            llm_system_prompt="llm_system_prompt",
            llm_temperature=0.7,
            outbound_auto_call=False,
            sip_endpoint="",
        )
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.aiagents.with_raw_response.create(
            agent_name="Support Bot Under Test",
            assistant_id="e1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aiagent = await response.parse()
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.aiagents.with_streaming_response.create(
            agent_name="Support Bot Under Test",
            assistant_id="e1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aiagent = await response.parse()
            assert_matches_type(TestAgent, aiagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        aiagent = await async_client.ai.tests.test_framework.v1.aiagents.retrieve(
            0,
        )
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.aiagents.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aiagent = await response.parse()
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.aiagents.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aiagent = await response.parse()
            assert_matches_type(TestAgent, aiagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        aiagent = await async_client.ai.tests.test_framework.v1.aiagents.update(
            id=0,
        )
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        aiagent = await async_client.ai.tests.test_framework.v1.aiagents.update(
            id=0,
            agent_name="Support Bot Under Test - renamed",
            assistant_id="assistant_id",
            auto_fetch_calls_enabled=True,
            auto_sync_prompt_enabled=True,
            auto_update_dropoff_nodes=True,
            auto_update_topic_nodes=True,
            contact_number="contact_number",
            description="description",
            inbound=True,
            language="language",
            llm_max_tokens=256,
            llm_model="llm_model",
            llm_system_prompt="llm_system_prompt",
            llm_temperature=0.5,
            outbound_auto_call=True,
            sip_endpoint="sip_endpoint",
        )
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.aiagents.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aiagent = await response.parse()
        assert_matches_type(TestAgent, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.aiagents.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aiagent = await response.parse()
            assert_matches_type(TestAgent, aiagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        aiagent = await async_client.ai.tests.test_framework.v1.aiagents.list()
        assert_matches_type(AiagentListResponse, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        aiagent = await async_client.ai.tests.test_framework.v1.aiagents.list(
            page=1,
            page_size=1,
        )
        assert_matches_type(AiagentListResponse, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.aiagents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aiagent = await response.parse()
        assert_matches_type(AiagentListResponse, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.aiagents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aiagent = await response.parse()
            assert_matches_type(AiagentListResponse, aiagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        aiagent = await async_client.ai.tests.test_framework.v1.aiagents.delete(
            0,
        )
        assert_matches_type(object, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.aiagents.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aiagent = await response.parse()
        assert_matches_type(object, aiagent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.aiagents.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aiagent = await response.parse()
            assert_matches_type(object, aiagent, path=["response"])

        assert cast(Any, response.is_closed) is True
