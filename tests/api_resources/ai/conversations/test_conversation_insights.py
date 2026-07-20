# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.conversations import (
    ConversationInsightRetrieveAggregatesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversationInsights:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_aggregates(self, client: Telnyx) -> None:
        conversation_insight = client.ai.conversations.conversation_insights.retrieve_aggregates()
        assert_matches_type(ConversationInsightRetrieveAggregatesResponse, conversation_insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_aggregates_with_all_params(self, client: Telnyx) -> None:
        conversation_insight = client.ai.conversations.conversation_insights.retrieve_aggregates(
            created_at="created_at",
            group_by=["string"],
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"assistant_id": "assistant_id"},
            show=["string"],
        )
        assert_matches_type(ConversationInsightRetrieveAggregatesResponse, conversation_insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_aggregates(self, client: Telnyx) -> None:
        response = client.ai.conversations.conversation_insights.with_raw_response.retrieve_aggregates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_insight = response.parse()
        assert_matches_type(ConversationInsightRetrieveAggregatesResponse, conversation_insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_aggregates(self, client: Telnyx) -> None:
        with client.ai.conversations.conversation_insights.with_streaming_response.retrieve_aggregates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_insight = response.parse()
            assert_matches_type(ConversationInsightRetrieveAggregatesResponse, conversation_insight, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConversationInsights:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_aggregates(self, async_client: AsyncTelnyx) -> None:
        conversation_insight = await async_client.ai.conversations.conversation_insights.retrieve_aggregates()
        assert_matches_type(ConversationInsightRetrieveAggregatesResponse, conversation_insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_aggregates_with_all_params(self, async_client: AsyncTelnyx) -> None:
        conversation_insight = await async_client.ai.conversations.conversation_insights.retrieve_aggregates(
            created_at="created_at",
            group_by=["string"],
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"assistant_id": "assistant_id"},
            show=["string"],
        )
        assert_matches_type(ConversationInsightRetrieveAggregatesResponse, conversation_insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_aggregates(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.conversations.conversation_insights.with_raw_response.retrieve_aggregates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_insight = await response.parse()
        assert_matches_type(ConversationInsightRetrieveAggregatesResponse, conversation_insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_aggregates(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.ai.conversations.conversation_insights.with_streaming_response.retrieve_aggregates()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_insight = await response.parse()
            assert_matches_type(ConversationInsightRetrieveAggregatesResponse, conversation_insight, path=["response"])

        assert cast(Any, response.is_closed) is True
