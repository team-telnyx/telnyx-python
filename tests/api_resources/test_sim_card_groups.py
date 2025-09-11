# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    SimCardGroupListResponse,
    SimCardGroupCreateResponse,
    SimCardGroupDeleteResponse,
    SimCardGroupUpdateResponse,
    SimCardGroupRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimCardGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        sim_card_group = client.sim_card_groups.create(
            name="My Test Group",
        )
        assert_matches_type(SimCardGroupCreateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        sim_card_group = client.sim_card_groups.create(
            name="My Test Group",
            data_limit={
                "amount": "2048.1",
                "unit": "MB",
            },
        )
        assert_matches_type(SimCardGroupCreateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.sim_card_groups.with_raw_response.create(
            name="My Test Group",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_group = response.parse()
        assert_matches_type(SimCardGroupCreateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.sim_card_groups.with_streaming_response.create(
            name="My Test Group",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_group = response.parse()
            assert_matches_type(SimCardGroupCreateResponse, sim_card_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        sim_card_group = client.sim_card_groups.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGroupRetrieveResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        sim_card_group = client.sim_card_groups.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            include_iccids=True,
        )
        assert_matches_type(SimCardGroupRetrieveResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.sim_card_groups.with_raw_response.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_group = response.parse()
        assert_matches_type(SimCardGroupRetrieveResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.sim_card_groups.with_streaming_response.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_group = response.parse()
            assert_matches_type(SimCardGroupRetrieveResponse, sim_card_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_groups.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        sim_card_group = client.sim_card_groups.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGroupUpdateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        sim_card_group = client.sim_card_groups.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            data_limit={
                "amount": "2048.1",
                "unit": "MB",
            },
            name="My Test Group",
        )
        assert_matches_type(SimCardGroupUpdateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.sim_card_groups.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_group = response.parse()
        assert_matches_type(SimCardGroupUpdateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.sim_card_groups.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_group = response.parse()
            assert_matches_type(SimCardGroupUpdateResponse, sim_card_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_groups.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        sim_card_group = client.sim_card_groups.list()
        assert_matches_type(SimCardGroupListResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        sim_card_group = client.sim_card_groups.list(
            filter_name="My Test Group",
            filter_private_wireless_gateway_id="7606c6d3-ff7c-49c1-943d-68879e9d584d",
            filter_wireless_blocklist_id="0f3f490e-c4d3-4cf5-838a-9970f10ee259",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(SimCardGroupListResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.sim_card_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_group = response.parse()
        assert_matches_type(SimCardGroupListResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.sim_card_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_group = response.parse()
            assert_matches_type(SimCardGroupListResponse, sim_card_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        sim_card_group = client.sim_card_groups.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGroupDeleteResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.sim_card_groups.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_group = response.parse()
        assert_matches_type(SimCardGroupDeleteResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.sim_card_groups.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_group = response.parse()
            assert_matches_type(SimCardGroupDeleteResponse, sim_card_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_groups.with_raw_response.delete(
                "",
            )


class TestAsyncSimCardGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        sim_card_group = await async_client.sim_card_groups.create(
            name="My Test Group",
        )
        assert_matches_type(SimCardGroupCreateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card_group = await async_client.sim_card_groups.create(
            name="My Test Group",
            data_limit={
                "amount": "2048.1",
                "unit": "MB",
            },
        )
        assert_matches_type(SimCardGroupCreateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_groups.with_raw_response.create(
            name="My Test Group",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_group = await response.parse()
        assert_matches_type(SimCardGroupCreateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_groups.with_streaming_response.create(
            name="My Test Group",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_group = await response.parse()
            assert_matches_type(SimCardGroupCreateResponse, sim_card_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        sim_card_group = await async_client.sim_card_groups.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGroupRetrieveResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card_group = await async_client.sim_card_groups.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            include_iccids=True,
        )
        assert_matches_type(SimCardGroupRetrieveResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_groups.with_raw_response.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_group = await response.parse()
        assert_matches_type(SimCardGroupRetrieveResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_groups.with_streaming_response.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_group = await response.parse()
            assert_matches_type(SimCardGroupRetrieveResponse, sim_card_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_groups.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        sim_card_group = await async_client.sim_card_groups.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGroupUpdateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card_group = await async_client.sim_card_groups.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            data_limit={
                "amount": "2048.1",
                "unit": "MB",
            },
            name="My Test Group",
        )
        assert_matches_type(SimCardGroupUpdateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_groups.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_group = await response.parse()
        assert_matches_type(SimCardGroupUpdateResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_groups.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_group = await response.parse()
            assert_matches_type(SimCardGroupUpdateResponse, sim_card_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_groups.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        sim_card_group = await async_client.sim_card_groups.list()
        assert_matches_type(SimCardGroupListResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card_group = await async_client.sim_card_groups.list(
            filter_name="My Test Group",
            filter_private_wireless_gateway_id="7606c6d3-ff7c-49c1-943d-68879e9d584d",
            filter_wireless_blocklist_id="0f3f490e-c4d3-4cf5-838a-9970f10ee259",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(SimCardGroupListResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_group = await response.parse()
        assert_matches_type(SimCardGroupListResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_group = await response.parse()
            assert_matches_type(SimCardGroupListResponse, sim_card_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        sim_card_group = await async_client.sim_card_groups.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGroupDeleteResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_groups.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_group = await response.parse()
        assert_matches_type(SimCardGroupDeleteResponse, sim_card_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_groups.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_group = await response.parse()
            assert_matches_type(SimCardGroupDeleteResponse, sim_card_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_groups.with_raw_response.delete(
                "",
            )
