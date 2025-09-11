# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInsights:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_assign(self, client: Telnyx) -> None:
        insight = client.ai.conversations.insight_groups.insights.assign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, insight, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_assign(self, client: Telnyx) -> None:
        response = client.ai.conversations.insight_groups.insights.with_raw_response.assign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(object, insight, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_assign(self, client: Telnyx) -> None:
        with client.ai.conversations.insight_groups.insights.with_streaming_response.assign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(object, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_assign(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.ai.conversations.insight_groups.insights.with_raw_response.assign(
                insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            client.ai.conversations.insight_groups.insights.with_raw_response.assign(
                insight_id="",
                group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_unassign(self, client: Telnyx) -> None:
        insight = client.ai.conversations.insight_groups.insights.delete_unassign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, insight, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_unassign(self, client: Telnyx) -> None:
        response = client.ai.conversations.insight_groups.insights.with_raw_response.delete_unassign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(object, insight, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_unassign(self, client: Telnyx) -> None:
        with client.ai.conversations.insight_groups.insights.with_streaming_response.delete_unassign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(object, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_unassign(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.ai.conversations.insight_groups.insights.with_raw_response.delete_unassign(
                insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            client.ai.conversations.insight_groups.insights.with_raw_response.delete_unassign(
                insight_id="",
                group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncInsights:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_assign(self, async_client: AsyncTelnyx) -> None:
        insight = await async_client.ai.conversations.insight_groups.insights.assign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, insight, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_assign(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.conversations.insight_groups.insights.with_raw_response.assign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(object, insight, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_assign(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.conversations.insight_groups.insights.with_streaming_response.assign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(object, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_assign(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.ai.conversations.insight_groups.insights.with_raw_response.assign(
                insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            await async_client.ai.conversations.insight_groups.insights.with_raw_response.assign(
                insight_id="",
                group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_unassign(self, async_client: AsyncTelnyx) -> None:
        insight = await async_client.ai.conversations.insight_groups.insights.delete_unassign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, insight, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_unassign(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.conversations.insight_groups.insights.with_raw_response.delete_unassign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(object, insight, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_unassign(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.conversations.insight_groups.insights.with_streaming_response.delete_unassign(
            insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(object, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_unassign(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.ai.conversations.insight_groups.insights.with_raw_response.delete_unassign(
                insight_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `insight_id` but received ''"):
            await async_client.ai.conversations.insight_groups.insights.with_raw_response.delete_unassign(
                insight_id="",
                group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
