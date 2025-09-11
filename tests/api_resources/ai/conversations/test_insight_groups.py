# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.conversations import (
    InsightTemplateGroupDetail,
    InsightGroupRetrieveInsightGroupsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInsightGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        insight_group = client.ai.conversations.insight_groups.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.conversations.insight_groups.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_group = response.parse()
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.conversations.insight_groups.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_group = response.parse()
            assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.ai.conversations.insight_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        insight_group = client.ai.conversations.insight_groups.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        insight_group = client.ai.conversations.insight_groups.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
            webhook="webhook",
        )
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.conversations.insight_groups.with_raw_response.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_group = response.parse()
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.conversations.insight_groups.with_streaming_response.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_group = response.parse()
            assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.ai.conversations.insight_groups.with_raw_response.update(
                group_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        insight_group = client.ai.conversations.insight_groups.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.conversations.insight_groups.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_group = response.parse()
        assert_matches_type(object, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.conversations.insight_groups.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_group = response.parse()
            assert_matches_type(object, insight_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.ai.conversations.insight_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_insight_groups(self, client: Telnyx) -> None:
        insight_group = client.ai.conversations.insight_groups.insight_groups(
            name="name",
        )
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_insight_groups_with_all_params(self, client: Telnyx) -> None:
        insight_group = client.ai.conversations.insight_groups.insight_groups(
            name="name",
            description="description",
            webhook="webhook",
        )
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_insight_groups(self, client: Telnyx) -> None:
        response = client.ai.conversations.insight_groups.with_raw_response.insight_groups(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_group = response.parse()
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_insight_groups(self, client: Telnyx) -> None:
        with client.ai.conversations.insight_groups.with_streaming_response.insight_groups(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_group = response.parse()
            assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_insight_groups(self, client: Telnyx) -> None:
        insight_group = client.ai.conversations.insight_groups.retrieve_insight_groups()
        assert_matches_type(InsightGroupRetrieveInsightGroupsResponse, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_insight_groups_with_all_params(self, client: Telnyx) -> None:
        insight_group = client.ai.conversations.insight_groups.retrieve_insight_groups(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(InsightGroupRetrieveInsightGroupsResponse, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_insight_groups(self, client: Telnyx) -> None:
        response = client.ai.conversations.insight_groups.with_raw_response.retrieve_insight_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_group = response.parse()
        assert_matches_type(InsightGroupRetrieveInsightGroupsResponse, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_insight_groups(self, client: Telnyx) -> None:
        with client.ai.conversations.insight_groups.with_streaming_response.retrieve_insight_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_group = response.parse()
            assert_matches_type(InsightGroupRetrieveInsightGroupsResponse, insight_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInsightGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        insight_group = await async_client.ai.conversations.insight_groups.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.conversations.insight_groups.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_group = await response.parse()
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.conversations.insight_groups.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_group = await response.parse()
            assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.ai.conversations.insight_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        insight_group = await async_client.ai.conversations.insight_groups.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        insight_group = await async_client.ai.conversations.insight_groups.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
            webhook="webhook",
        )
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.conversations.insight_groups.with_raw_response.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_group = await response.parse()
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.conversations.insight_groups.with_streaming_response.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_group = await response.parse()
            assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.ai.conversations.insight_groups.with_raw_response.update(
                group_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        insight_group = await async_client.ai.conversations.insight_groups.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.conversations.insight_groups.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_group = await response.parse()
        assert_matches_type(object, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.conversations.insight_groups.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_group = await response.parse()
            assert_matches_type(object, insight_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.ai.conversations.insight_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_insight_groups(self, async_client: AsyncTelnyx) -> None:
        insight_group = await async_client.ai.conversations.insight_groups.insight_groups(
            name="name",
        )
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_insight_groups_with_all_params(self, async_client: AsyncTelnyx) -> None:
        insight_group = await async_client.ai.conversations.insight_groups.insight_groups(
            name="name",
            description="description",
            webhook="webhook",
        )
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_insight_groups(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.conversations.insight_groups.with_raw_response.insight_groups(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_group = await response.parse()
        assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_insight_groups(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.conversations.insight_groups.with_streaming_response.insight_groups(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_group = await response.parse()
            assert_matches_type(InsightTemplateGroupDetail, insight_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_insight_groups(self, async_client: AsyncTelnyx) -> None:
        insight_group = await async_client.ai.conversations.insight_groups.retrieve_insight_groups()
        assert_matches_type(InsightGroupRetrieveInsightGroupsResponse, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_insight_groups_with_all_params(self, async_client: AsyncTelnyx) -> None:
        insight_group = await async_client.ai.conversations.insight_groups.retrieve_insight_groups(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(InsightGroupRetrieveInsightGroupsResponse, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_insight_groups(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.conversations.insight_groups.with_raw_response.retrieve_insight_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_group = await response.parse()
        assert_matches_type(InsightGroupRetrieveInsightGroupsResponse, insight_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_insight_groups(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.ai.conversations.insight_groups.with_streaming_response.retrieve_insight_groups()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_group = await response.parse()
            assert_matches_type(InsightGroupRetrieveInsightGroupsResponse, insight_group, path=["response"])

        assert cast(Any, response.is_closed) is True
