# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    SimCardOrderListResponse,
    SimCardOrderCreateResponse,
    SimCardOrderRetrieveResponse,
)
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimCardOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        sim_card_order = client.sim_card_orders.create(
            address_id="1293384261075731499",
            quantity=23,
        )
        assert_matches_type(SimCardOrderCreateResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.sim_card_orders.with_raw_response.create(
            address_id="1293384261075731499",
            quantity=23,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_order = response.parse()
        assert_matches_type(SimCardOrderCreateResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.sim_card_orders.with_streaming_response.create(
            address_id="1293384261075731499",
            quantity=23,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_order = response.parse()
            assert_matches_type(SimCardOrderCreateResponse, sim_card_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        sim_card_order = client.sim_card_orders.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardOrderRetrieveResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.sim_card_orders.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_order = response.parse()
        assert_matches_type(SimCardOrderRetrieveResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.sim_card_orders.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_order = response.parse()
            assert_matches_type(SimCardOrderRetrieveResponse, sim_card_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        sim_card_order = client.sim_card_orders.list()
        assert_matches_type(SimCardOrderListResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        sim_card_order = client.sim_card_orders.list(
            filter={
                "address": {
                    "id": "1293384261075731499",
                    "administrative_area": "TX",
                    "country_code": "US",
                    "extended_address": "14th Floor",
                    "locality": "Austin",
                    "postal_code": "78701",
                    "street_address": "600 Congress Avenue",
                },
                "cost": {
                    "amount": "2.53",
                    "currency": "USD",
                },
                "created_at": parse_datetime("2018-02-02T22:25:27.521Z"),
                "quantity": 21,
                "updated_at": parse_datetime("2018-02-02T22:25:27.521Z"),
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(SimCardOrderListResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.sim_card_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_order = response.parse()
        assert_matches_type(SimCardOrderListResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.sim_card_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_order = response.parse()
            assert_matches_type(SimCardOrderListResponse, sim_card_order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimCardOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        sim_card_order = await async_client.sim_card_orders.create(
            address_id="1293384261075731499",
            quantity=23,
        )
        assert_matches_type(SimCardOrderCreateResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_orders.with_raw_response.create(
            address_id="1293384261075731499",
            quantity=23,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_order = await response.parse()
        assert_matches_type(SimCardOrderCreateResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_orders.with_streaming_response.create(
            address_id="1293384261075731499",
            quantity=23,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_order = await response.parse()
            assert_matches_type(SimCardOrderCreateResponse, sim_card_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        sim_card_order = await async_client.sim_card_orders.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardOrderRetrieveResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_orders.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_order = await response.parse()
        assert_matches_type(SimCardOrderRetrieveResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_orders.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_order = await response.parse()
            assert_matches_type(SimCardOrderRetrieveResponse, sim_card_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        sim_card_order = await async_client.sim_card_orders.list()
        assert_matches_type(SimCardOrderListResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card_order = await async_client.sim_card_orders.list(
            filter={
                "address": {
                    "id": "1293384261075731499",
                    "administrative_area": "TX",
                    "country_code": "US",
                    "extended_address": "14th Floor",
                    "locality": "Austin",
                    "postal_code": "78701",
                    "street_address": "600 Congress Avenue",
                },
                "cost": {
                    "amount": "2.53",
                    "currency": "USD",
                },
                "created_at": parse_datetime("2018-02-02T22:25:27.521Z"),
                "quantity": 21,
                "updated_at": parse_datetime("2018-02-02T22:25:27.521Z"),
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(SimCardOrderListResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_order = await response.parse()
        assert_matches_type(SimCardOrderListResponse, sim_card_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_order = await response.parse()
            assert_matches_type(SimCardOrderListResponse, sim_card_order, path=["response"])

        assert cast(Any, response.is_closed) is True
