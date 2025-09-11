# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    RequirementGroup,
    RequirementGroupListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequirementGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        requirement_group = client.requirement_groups.create(
            action="ordering",
            country_code="US",
            phone_number_type="local",
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        requirement_group = client.requirement_groups.create(
            action="ordering",
            country_code="US",
            phone_number_type="local",
            customer_reference="My Requirement Group",
            regulatory_requirements=[
                {
                    "field_value": "field_value",
                    "requirement_id": "requirement_id",
                }
            ],
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.requirement_groups.with_raw_response.create(
            action="ordering",
            country_code="US",
            phone_number_type="local",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = response.parse()
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.requirement_groups.with_streaming_response.create(
            action="ordering",
            country_code="US",
            phone_number_type="local",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = response.parse()
            assert_matches_type(RequirementGroup, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        requirement_group = client.requirement_groups.retrieve(
            "id",
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.requirement_groups.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = response.parse()
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.requirement_groups.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = response.parse()
            assert_matches_type(RequirementGroup, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.requirement_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        requirement_group = client.requirement_groups.update(
            id="id",
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        requirement_group = client.requirement_groups.update(
            id="id",
            customer_reference="0002",
            regulatory_requirements=[
                {
                    "field_value": "new requirement value",
                    "requirement_id": "53970723-fbff-4f46-a975-f62be6c1a585",
                }
            ],
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.requirement_groups.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = response.parse()
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.requirement_groups.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = response.parse()
            assert_matches_type(RequirementGroup, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.requirement_groups.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        requirement_group = client.requirement_groups.list()
        assert_matches_type(RequirementGroupListResponse, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        requirement_group = client.requirement_groups.list(
            filter={
                "action": "ordering",
                "country_code": "country_code",
                "customer_reference": "customer_reference",
                "phone_number_type": "local",
                "status": "approved",
            },
        )
        assert_matches_type(RequirementGroupListResponse, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.requirement_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = response.parse()
        assert_matches_type(RequirementGroupListResponse, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.requirement_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = response.parse()
            assert_matches_type(RequirementGroupListResponse, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        requirement_group = client.requirement_groups.delete(
            "id",
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.requirement_groups.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = response.parse()
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.requirement_groups.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = response.parse()
            assert_matches_type(RequirementGroup, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.requirement_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_for_approval(self, client: Telnyx) -> None:
        requirement_group = client.requirement_groups.submit_for_approval(
            "id",
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_for_approval(self, client: Telnyx) -> None:
        response = client.requirement_groups.with_raw_response.submit_for_approval(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = response.parse()
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_for_approval(self, client: Telnyx) -> None:
        with client.requirement_groups.with_streaming_response.submit_for_approval(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = response.parse()
            assert_matches_type(RequirementGroup, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_submit_for_approval(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.requirement_groups.with_raw_response.submit_for_approval(
                "",
            )


class TestAsyncRequirementGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        requirement_group = await async_client.requirement_groups.create(
            action="ordering",
            country_code="US",
            phone_number_type="local",
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        requirement_group = await async_client.requirement_groups.create(
            action="ordering",
            country_code="US",
            phone_number_type="local",
            customer_reference="My Requirement Group",
            regulatory_requirements=[
                {
                    "field_value": "field_value",
                    "requirement_id": "requirement_id",
                }
            ],
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.requirement_groups.with_raw_response.create(
            action="ordering",
            country_code="US",
            phone_number_type="local",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = await response.parse()
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.requirement_groups.with_streaming_response.create(
            action="ordering",
            country_code="US",
            phone_number_type="local",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = await response.parse()
            assert_matches_type(RequirementGroup, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        requirement_group = await async_client.requirement_groups.retrieve(
            "id",
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.requirement_groups.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = await response.parse()
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.requirement_groups.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = await response.parse()
            assert_matches_type(RequirementGroup, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.requirement_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        requirement_group = await async_client.requirement_groups.update(
            id="id",
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        requirement_group = await async_client.requirement_groups.update(
            id="id",
            customer_reference="0002",
            regulatory_requirements=[
                {
                    "field_value": "new requirement value",
                    "requirement_id": "53970723-fbff-4f46-a975-f62be6c1a585",
                }
            ],
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.requirement_groups.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = await response.parse()
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.requirement_groups.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = await response.parse()
            assert_matches_type(RequirementGroup, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.requirement_groups.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        requirement_group = await async_client.requirement_groups.list()
        assert_matches_type(RequirementGroupListResponse, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        requirement_group = await async_client.requirement_groups.list(
            filter={
                "action": "ordering",
                "country_code": "country_code",
                "customer_reference": "customer_reference",
                "phone_number_type": "local",
                "status": "approved",
            },
        )
        assert_matches_type(RequirementGroupListResponse, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.requirement_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = await response.parse()
        assert_matches_type(RequirementGroupListResponse, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.requirement_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = await response.parse()
            assert_matches_type(RequirementGroupListResponse, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        requirement_group = await async_client.requirement_groups.delete(
            "id",
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.requirement_groups.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = await response.parse()
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.requirement_groups.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = await response.parse()
            assert_matches_type(RequirementGroup, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.requirement_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_for_approval(self, async_client: AsyncTelnyx) -> None:
        requirement_group = await async_client.requirement_groups.submit_for_approval(
            "id",
        )
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_for_approval(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.requirement_groups.with_raw_response.submit_for_approval(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        requirement_group = await response.parse()
        assert_matches_type(RequirementGroup, requirement_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_for_approval(self, async_client: AsyncTelnyx) -> None:
        async with async_client.requirement_groups.with_streaming_response.submit_for_approval(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            requirement_group = await response.parse()
            assert_matches_type(RequirementGroup, requirement_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_submit_for_approval(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.requirement_groups.with_raw_response.submit_for_approval(
                "",
            )
