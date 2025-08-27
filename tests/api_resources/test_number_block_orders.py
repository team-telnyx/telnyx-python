# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    NumberBlockOrderListResponse,
    NumberBlockOrderCreateResponse,
    NumberBlockOrderRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumberBlockOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        number_block_order = client.number_block_orders.create(
            range=10,
            starting_number="+19705555000",
        )
        assert_matches_type(NumberBlockOrderCreateResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        number_block_order = client.number_block_orders.create(
            range=10,
            starting_number="+19705555000",
            connection_id="346789098765567",
            customer_reference="MY REF 001",
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600",
        )
        assert_matches_type(NumberBlockOrderCreateResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.number_block_orders.with_raw_response.create(
            range=10,
            starting_number="+19705555000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_block_order = response.parse()
        assert_matches_type(NumberBlockOrderCreateResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.number_block_orders.with_streaming_response.create(
            range=10,
            starting_number="+19705555000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_block_order = response.parse()
            assert_matches_type(NumberBlockOrderCreateResponse, number_block_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        number_block_order = client.number_block_orders.retrieve(
            "number_block_order_id",
        )
        assert_matches_type(NumberBlockOrderRetrieveResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.number_block_orders.with_raw_response.retrieve(
            "number_block_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_block_order = response.parse()
        assert_matches_type(NumberBlockOrderRetrieveResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.number_block_orders.with_streaming_response.retrieve(
            "number_block_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_block_order = response.parse()
            assert_matches_type(NumberBlockOrderRetrieveResponse, number_block_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number_block_order_id` but received ''"):
            client.number_block_orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        number_block_order = client.number_block_orders.list()
        assert_matches_type(NumberBlockOrderListResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        number_block_order = client.number_block_orders.list(
            filter={
                "created_at": {
                    "gt": "2018-01-01T00:00:00.000000Z",
                    "lt": "2018-01-01T00:00:00.000000Z",
                },
                "phone_numbers_starting_number": "+19705555000",
                "status": "pending",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(NumberBlockOrderListResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.number_block_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_block_order = response.parse()
        assert_matches_type(NumberBlockOrderListResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.number_block_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_block_order = response.parse()
            assert_matches_type(NumberBlockOrderListResponse, number_block_order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNumberBlockOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        number_block_order = await async_client.number_block_orders.create(
            range=10,
            starting_number="+19705555000",
        )
        assert_matches_type(NumberBlockOrderCreateResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number_block_order = await async_client.number_block_orders.create(
            range=10,
            starting_number="+19705555000",
            connection_id="346789098765567",
            customer_reference="MY REF 001",
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600",
        )
        assert_matches_type(NumberBlockOrderCreateResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_block_orders.with_raw_response.create(
            range=10,
            starting_number="+19705555000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_block_order = await response.parse()
        assert_matches_type(NumberBlockOrderCreateResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_block_orders.with_streaming_response.create(
            range=10,
            starting_number="+19705555000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_block_order = await response.parse()
            assert_matches_type(NumberBlockOrderCreateResponse, number_block_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        number_block_order = await async_client.number_block_orders.retrieve(
            "number_block_order_id",
        )
        assert_matches_type(NumberBlockOrderRetrieveResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_block_orders.with_raw_response.retrieve(
            "number_block_order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_block_order = await response.parse()
        assert_matches_type(NumberBlockOrderRetrieveResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_block_orders.with_streaming_response.retrieve(
            "number_block_order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_block_order = await response.parse()
            assert_matches_type(NumberBlockOrderRetrieveResponse, number_block_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number_block_order_id` but received ''"):
            await async_client.number_block_orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        number_block_order = await async_client.number_block_orders.list()
        assert_matches_type(NumberBlockOrderListResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number_block_order = await async_client.number_block_orders.list(
            filter={
                "created_at": {
                    "gt": "2018-01-01T00:00:00.000000Z",
                    "lt": "2018-01-01T00:00:00.000000Z",
                },
                "phone_numbers_starting_number": "+19705555000",
                "status": "pending",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(NumberBlockOrderListResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_block_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_block_order = await response.parse()
        assert_matches_type(NumberBlockOrderListResponse, number_block_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_block_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_block_order = await response.parse()
            assert_matches_type(NumberBlockOrderListResponse, number_block_order, path=["response"])

        assert cast(Any, response.is_closed) is True
