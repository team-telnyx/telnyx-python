# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    SubNumberOrderListResponse,
    SubNumberOrderCancelResponse,
    SubNumberOrderUpdateResponse,
    SubNumberOrderRetrieveResponse,
    SubNumberOrderUpdateRequirementGroupResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubNumberOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        sub_number_order = client.sub_number_orders.retrieve(
            sub_number_order_id="sub_number_order_id",
        )
        assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        sub_number_order = client.sub_number_orders.retrieve(
            sub_number_order_id="sub_number_order_id",
            filter={"include_phone_numbers": True},
        )
        assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.sub_number_orders.with_raw_response.retrieve(
            sub_number_order_id="sub_number_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = response.parse()
        assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.sub_number_orders.with_streaming_response.retrieve(
            sub_number_order_id="sub_number_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = response.parse()
            assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_number_order_id` but received ''"):
            client.sub_number_orders.with_raw_response.retrieve(
                sub_number_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        sub_number_order = client.sub_number_orders.update(
            sub_number_order_id="sub_number_order_id",
        )
        assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        sub_number_order = client.sub_number_orders.update(
            sub_number_order_id="sub_number_order_id",
            regulatory_requirements=[
                {
                    "field_value": "45f45a04-b4be-4592-95b1-9306b9db2b21",
                    "requirement_id": "8ffb3622-7c6b-4ccc-b65f-7a3dc0099576",
                }
            ],
        )
        assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.sub_number_orders.with_raw_response.update(
            sub_number_order_id="sub_number_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = response.parse()
        assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.sub_number_orders.with_streaming_response.update(
            sub_number_order_id="sub_number_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = response.parse()
            assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_number_order_id` but received ''"):
            client.sub_number_orders.with_raw_response.update(
                sub_number_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        sub_number_order = client.sub_number_orders.list()
        assert_matches_type(SubNumberOrderListResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        sub_number_order = client.sub_number_orders.list(
            filter={
                "country_code": "US",
                "order_request_id": "12ade33a-21c0-473b-b055-b3c836e1c293",
                "phone_number_type": "local",
                "phone_numbers_count": 1,
                "status": "status",
            },
        )
        assert_matches_type(SubNumberOrderListResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.sub_number_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = response.parse()
        assert_matches_type(SubNumberOrderListResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.sub_number_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = response.parse()
            assert_matches_type(SubNumberOrderListResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Telnyx) -> None:
        sub_number_order = client.sub_number_orders.cancel(
            "sub_number_order_id",
        )
        assert_matches_type(SubNumberOrderCancelResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Telnyx) -> None:
        response = client.sub_number_orders.with_raw_response.cancel(
            "sub_number_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = response.parse()
        assert_matches_type(SubNumberOrderCancelResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Telnyx) -> None:
        with client.sub_number_orders.with_streaming_response.cancel(
            "sub_number_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = response.parse()
            assert_matches_type(SubNumberOrderCancelResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_number_order_id` but received ''"):
            client.sub_number_orders.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_requirement_group(self, client: Telnyx) -> None:
        sub_number_order = client.sub_number_orders.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="a4b201f9-8646-4e54-a7d2-b2e403eeaf8c",
        )
        assert_matches_type(SubNumberOrderUpdateRequirementGroupResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_requirement_group(self, client: Telnyx) -> None:
        response = client.sub_number_orders.with_raw_response.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="a4b201f9-8646-4e54-a7d2-b2e403eeaf8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = response.parse()
        assert_matches_type(SubNumberOrderUpdateRequirementGroupResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_requirement_group(self, client: Telnyx) -> None:
        with client.sub_number_orders.with_streaming_response.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="a4b201f9-8646-4e54-a7d2-b2e403eeaf8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = response.parse()
            assert_matches_type(SubNumberOrderUpdateRequirementGroupResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_requirement_group(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sub_number_orders.with_raw_response.update_requirement_group(
                id="",
                requirement_group_id="a4b201f9-8646-4e54-a7d2-b2e403eeaf8c",
            )


class TestAsyncSubNumberOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        sub_number_order = await async_client.sub_number_orders.retrieve(
            sub_number_order_id="sub_number_order_id",
        )
        assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sub_number_order = await async_client.sub_number_orders.retrieve(
            sub_number_order_id="sub_number_order_id",
            filter={"include_phone_numbers": True},
        )
        assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sub_number_orders.with_raw_response.retrieve(
            sub_number_order_id="sub_number_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = await response.parse()
        assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sub_number_orders.with_streaming_response.retrieve(
            sub_number_order_id="sub_number_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = await response.parse()
            assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_number_order_id` but received ''"):
            await async_client.sub_number_orders.with_raw_response.retrieve(
                sub_number_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        sub_number_order = await async_client.sub_number_orders.update(
            sub_number_order_id="sub_number_order_id",
        )
        assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sub_number_order = await async_client.sub_number_orders.update(
            sub_number_order_id="sub_number_order_id",
            regulatory_requirements=[
                {
                    "field_value": "45f45a04-b4be-4592-95b1-9306b9db2b21",
                    "requirement_id": "8ffb3622-7c6b-4ccc-b65f-7a3dc0099576",
                }
            ],
        )
        assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sub_number_orders.with_raw_response.update(
            sub_number_order_id="sub_number_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = await response.parse()
        assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sub_number_orders.with_streaming_response.update(
            sub_number_order_id="sub_number_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = await response.parse()
            assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_number_order_id` but received ''"):
            await async_client.sub_number_orders.with_raw_response.update(
                sub_number_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        sub_number_order = await async_client.sub_number_orders.list()
        assert_matches_type(SubNumberOrderListResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sub_number_order = await async_client.sub_number_orders.list(
            filter={
                "country_code": "US",
                "order_request_id": "12ade33a-21c0-473b-b055-b3c836e1c293",
                "phone_number_type": "local",
                "phone_numbers_count": 1,
                "status": "status",
            },
        )
        assert_matches_type(SubNumberOrderListResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sub_number_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = await response.parse()
        assert_matches_type(SubNumberOrderListResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sub_number_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = await response.parse()
            assert_matches_type(SubNumberOrderListResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncTelnyx) -> None:
        sub_number_order = await async_client.sub_number_orders.cancel(
            "sub_number_order_id",
        )
        assert_matches_type(SubNumberOrderCancelResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sub_number_orders.with_raw_response.cancel(
            "sub_number_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = await response.parse()
        assert_matches_type(SubNumberOrderCancelResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sub_number_orders.with_streaming_response.cancel(
            "sub_number_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = await response.parse()
            assert_matches_type(SubNumberOrderCancelResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_number_order_id` but received ''"):
            await async_client.sub_number_orders.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_requirement_group(self, async_client: AsyncTelnyx) -> None:
        sub_number_order = await async_client.sub_number_orders.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="a4b201f9-8646-4e54-a7d2-b2e403eeaf8c",
        )
        assert_matches_type(SubNumberOrderUpdateRequirementGroupResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_requirement_group(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sub_number_orders.with_raw_response.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="a4b201f9-8646-4e54-a7d2-b2e403eeaf8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = await response.parse()
        assert_matches_type(SubNumberOrderUpdateRequirementGroupResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_requirement_group(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sub_number_orders.with_streaming_response.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="a4b201f9-8646-4e54-a7d2-b2e403eeaf8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = await response.parse()
            assert_matches_type(SubNumberOrderUpdateRequirementGroupResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_requirement_group(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sub_number_orders.with_raw_response.update_requirement_group(
                id="",
                requirement_group_id="a4b201f9-8646-4e54-a7d2-b2e403eeaf8c",
            )
