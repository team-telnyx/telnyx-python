# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    NumberOrderListResponse,
    NumberOrderCreateResponse,
    NumberOrderUpdateResponse,
    NumberOrderRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumberOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        number_order = client.number_orders.create()
        assert_matches_type(NumberOrderCreateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        number_order = client.number_orders.create(
            billing_group_id="abc85f64-5717-4562-b3fc-2c9600",
            connection_id="346789098765567",
            customer_reference="MY REF 001",
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600",
            phone_numbers=[
                {
                    "phone_number": "+19705555098",
                    "bundle_id": "bc8e4d67-33a0-4cbb-af74-7b58f05bd494",
                    "requirement_group_id": "dbbd94ee-9079-488f-80ba-f566b247fd7",
                },
                {
                    "phone_number": "+492111609539",
                    "bundle_id": "bc8e4d67-33a0-4cbb-af74-7b58f05bd494",
                    "requirement_group_id": "dbbd94ee-9079-488f-80ba-f566b247fd79",
                },
            ],
        )
        assert_matches_type(NumberOrderCreateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.number_orders.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order = response.parse()
        assert_matches_type(NumberOrderCreateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.number_orders.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order = response.parse()
            assert_matches_type(NumberOrderCreateResponse, number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        number_order = client.number_orders.retrieve(
            "number_order_id",
        )
        assert_matches_type(NumberOrderRetrieveResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.number_orders.with_raw_response.retrieve(
            "number_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order = response.parse()
        assert_matches_type(NumberOrderRetrieveResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.number_orders.with_streaming_response.retrieve(
            "number_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order = response.parse()
            assert_matches_type(NumberOrderRetrieveResponse, number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number_order_id` but received ''"):
            client.number_orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        number_order = client.number_orders.update(
            number_order_id="number_order_id",
        )
        assert_matches_type(NumberOrderUpdateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        number_order = client.number_orders.update(
            number_order_id="number_order_id",
            customer_reference="MY REF 001",
            regulatory_requirements=[
                {
                    "field_value": "45f45a04-b4be-4592-95b1-9306b9db2b21",
                    "requirement_id": "8ffb3622-7c6b-4ccc-b65f-7a3dc0099576",
                }
            ],
        )
        assert_matches_type(NumberOrderUpdateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.number_orders.with_raw_response.update(
            number_order_id="number_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order = response.parse()
        assert_matches_type(NumberOrderUpdateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.number_orders.with_streaming_response.update(
            number_order_id="number_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order = response.parse()
            assert_matches_type(NumberOrderUpdateResponse, number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number_order_id` but received ''"):
            client.number_orders.with_raw_response.update(
                number_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        number_order = client.number_orders.list()
        assert_matches_type(NumberOrderListResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        number_order = client.number_orders.list(
            filter={
                "created_at": {
                    "gt": "gt",
                    "lt": "lt",
                },
                "customer_reference": "customer_reference",
                "phone_numbers_count": "phone_numbers_count",
                "requirements_met": True,
                "status": "status",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(NumberOrderListResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.number_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order = response.parse()
        assert_matches_type(NumberOrderListResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.number_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order = response.parse()
            assert_matches_type(NumberOrderListResponse, number_order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNumberOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        number_order = await async_client.number_orders.create()
        assert_matches_type(NumberOrderCreateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number_order = await async_client.number_orders.create(
            billing_group_id="abc85f64-5717-4562-b3fc-2c9600",
            connection_id="346789098765567",
            customer_reference="MY REF 001",
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600",
            phone_numbers=[
                {
                    "phone_number": "+19705555098",
                    "bundle_id": "bc8e4d67-33a0-4cbb-af74-7b58f05bd494",
                    "requirement_group_id": "dbbd94ee-9079-488f-80ba-f566b247fd7",
                },
                {
                    "phone_number": "+492111609539",
                    "bundle_id": "bc8e4d67-33a0-4cbb-af74-7b58f05bd494",
                    "requirement_group_id": "dbbd94ee-9079-488f-80ba-f566b247fd79",
                },
            ],
        )
        assert_matches_type(NumberOrderCreateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_orders.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order = await response.parse()
        assert_matches_type(NumberOrderCreateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_orders.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order = await response.parse()
            assert_matches_type(NumberOrderCreateResponse, number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        number_order = await async_client.number_orders.retrieve(
            "number_order_id",
        )
        assert_matches_type(NumberOrderRetrieveResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_orders.with_raw_response.retrieve(
            "number_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order = await response.parse()
        assert_matches_type(NumberOrderRetrieveResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_orders.with_streaming_response.retrieve(
            "number_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order = await response.parse()
            assert_matches_type(NumberOrderRetrieveResponse, number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number_order_id` but received ''"):
            await async_client.number_orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        number_order = await async_client.number_orders.update(
            number_order_id="number_order_id",
        )
        assert_matches_type(NumberOrderUpdateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number_order = await async_client.number_orders.update(
            number_order_id="number_order_id",
            customer_reference="MY REF 001",
            regulatory_requirements=[
                {
                    "field_value": "45f45a04-b4be-4592-95b1-9306b9db2b21",
                    "requirement_id": "8ffb3622-7c6b-4ccc-b65f-7a3dc0099576",
                }
            ],
        )
        assert_matches_type(NumberOrderUpdateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_orders.with_raw_response.update(
            number_order_id="number_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order = await response.parse()
        assert_matches_type(NumberOrderUpdateResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_orders.with_streaming_response.update(
            number_order_id="number_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order = await response.parse()
            assert_matches_type(NumberOrderUpdateResponse, number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number_order_id` but received ''"):
            await async_client.number_orders.with_raw_response.update(
                number_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        number_order = await async_client.number_orders.list()
        assert_matches_type(NumberOrderListResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number_order = await async_client.number_orders.list(
            filter={
                "created_at": {
                    "gt": "gt",
                    "lt": "lt",
                },
                "customer_reference": "customer_reference",
                "phone_numbers_count": "phone_numbers_count",
                "requirements_met": True,
                "status": "status",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(NumberOrderListResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order = await response.parse()
        assert_matches_type(NumberOrderListResponse, number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order = await response.parse()
            assert_matches_type(NumberOrderListResponse, number_order, path=["response"])

        assert cast(Any, response.is_closed) is True
