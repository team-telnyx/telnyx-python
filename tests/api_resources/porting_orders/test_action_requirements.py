# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.porting_orders import (
    ActionRequirementListResponse,
    ActionRequirementInitiateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActionRequirements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        action_requirement = client.porting_orders.action_requirements.list(
            porting_order_id="porting_order_id",
        )
        assert_matches_type(ActionRequirementListResponse, action_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        action_requirement = client.porting_orders.action_requirements.list(
            porting_order_id="porting_order_id",
            filter={
                "id": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "action_type": "au_id_verification",
                "requirement_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "status": "created",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(ActionRequirementListResponse, action_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.porting_orders.action_requirements.with_raw_response.list(
            porting_order_id="porting_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action_requirement = response.parse()
        assert_matches_type(ActionRequirementListResponse, action_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.porting_orders.action_requirements.with_streaming_response.list(
            porting_order_id="porting_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action_requirement = response.parse()
            assert_matches_type(ActionRequirementListResponse, action_requirement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            client.porting_orders.action_requirements.with_raw_response.list(
                porting_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate(self, client: Telnyx) -> None:
        action_requirement = client.porting_orders.action_requirements.initiate(
            id="id",
            porting_order_id="porting_order_id",
            params={
                "first_name": "John",
                "last_name": "Doe",
            },
        )
        assert_matches_type(ActionRequirementInitiateResponse, action_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate(self, client: Telnyx) -> None:
        response = client.porting_orders.action_requirements.with_raw_response.initiate(
            id="id",
            porting_order_id="porting_order_id",
            params={
                "first_name": "John",
                "last_name": "Doe",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action_requirement = response.parse()
        assert_matches_type(ActionRequirementInitiateResponse, action_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate(self, client: Telnyx) -> None:
        with client.porting_orders.action_requirements.with_streaming_response.initiate(
            id="id",
            porting_order_id="porting_order_id",
            params={
                "first_name": "John",
                "last_name": "Doe",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action_requirement = response.parse()
            assert_matches_type(ActionRequirementInitiateResponse, action_requirement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_initiate(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            client.porting_orders.action_requirements.with_raw_response.initiate(
                id="id",
                porting_order_id="",
                params={
                    "first_name": "John",
                    "last_name": "Doe",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.action_requirements.with_raw_response.initiate(
                id="",
                porting_order_id="porting_order_id",
                params={
                    "first_name": "John",
                    "last_name": "Doe",
                },
            )


class TestAsyncActionRequirements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        action_requirement = await async_client.porting_orders.action_requirements.list(
            porting_order_id="porting_order_id",
        )
        assert_matches_type(ActionRequirementListResponse, action_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action_requirement = await async_client.porting_orders.action_requirements.list(
            porting_order_id="porting_order_id",
            filter={
                "id": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "action_type": "au_id_verification",
                "requirement_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "status": "created",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(ActionRequirementListResponse, action_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.action_requirements.with_raw_response.list(
            porting_order_id="porting_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action_requirement = await response.parse()
        assert_matches_type(ActionRequirementListResponse, action_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.action_requirements.with_streaming_response.list(
            porting_order_id="porting_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action_requirement = await response.parse()
            assert_matches_type(ActionRequirementListResponse, action_requirement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            await async_client.porting_orders.action_requirements.with_raw_response.list(
                porting_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate(self, async_client: AsyncTelnyx) -> None:
        action_requirement = await async_client.porting_orders.action_requirements.initiate(
            id="id",
            porting_order_id="porting_order_id",
            params={
                "first_name": "John",
                "last_name": "Doe",
            },
        )
        assert_matches_type(ActionRequirementInitiateResponse, action_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.action_requirements.with_raw_response.initiate(
            id="id",
            porting_order_id="porting_order_id",
            params={
                "first_name": "John",
                "last_name": "Doe",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action_requirement = await response.parse()
        assert_matches_type(ActionRequirementInitiateResponse, action_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.action_requirements.with_streaming_response.initiate(
            id="id",
            porting_order_id="porting_order_id",
            params={
                "first_name": "John",
                "last_name": "Doe",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action_requirement = await response.parse()
            assert_matches_type(ActionRequirementInitiateResponse, action_requirement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_initiate(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            await async_client.porting_orders.action_requirements.with_raw_response.initiate(
                id="id",
                porting_order_id="",
                params={
                    "first_name": "John",
                    "last_name": "Doe",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.action_requirements.with_raw_response.initiate(
                id="",
                porting_order_id="porting_order_id",
                params={
                    "first_name": "John",
                    "last_name": "Doe",
                },
            )
