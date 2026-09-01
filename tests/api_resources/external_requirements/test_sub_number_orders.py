# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.external_requirements import (
    SubNumberOrderUpdateResponse,
    SubNumberOrderRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubNumberOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        sub_number_order = client.external_requirements.sub_number_orders.retrieve(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.external_requirements.sub_number_orders.with_raw_response.retrieve(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = response.parse()
        assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.external_requirements.sub_number_orders.with_streaming_response.retrieve(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = response.parse()
            assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `regulatory_requirement_id` but received ''"
        ):
            client.external_requirements.sub_number_orders.with_raw_response.retrieve(
                sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                regulatory_requirement_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_number_order_id` but received ''"):
            client.external_requirements.sub_number_orders.with_raw_response.retrieve(
                sub_number_order_id="",
                regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        sub_number_order = client.external_requirements.sub_number_orders.update(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement={
                "first_name": "Jane",
                "last_name": "Doe",
            },
        )
        assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.external_requirements.sub_number_orders.with_raw_response.update(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement={
                "first_name": "Jane",
                "last_name": "Doe",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = response.parse()
        assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.external_requirements.sub_number_orders.with_streaming_response.update(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement={
                "first_name": "Jane",
                "last_name": "Doe",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = response.parse()
            assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `regulatory_requirement_id` but received ''"
        ):
            client.external_requirements.sub_number_orders.with_raw_response.update(
                sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                regulatory_requirement_id="",
                requirement={
                    "first_name": "Jane",
                    "last_name": "Doe",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_number_order_id` but received ''"):
            client.external_requirements.sub_number_orders.with_raw_response.update(
                sub_number_order_id="",
                regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                requirement={
                    "first_name": "Jane",
                    "last_name": "Doe",
                },
            )


class TestAsyncSubNumberOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        sub_number_order = await async_client.external_requirements.sub_number_orders.retrieve(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_requirements.sub_number_orders.with_raw_response.retrieve(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = await response.parse()
        assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_requirements.sub_number_orders.with_streaming_response.retrieve(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = await response.parse()
            assert_matches_type(SubNumberOrderRetrieveResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `regulatory_requirement_id` but received ''"
        ):
            await async_client.external_requirements.sub_number_orders.with_raw_response.retrieve(
                sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                regulatory_requirement_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_number_order_id` but received ''"):
            await async_client.external_requirements.sub_number_orders.with_raw_response.retrieve(
                sub_number_order_id="",
                regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        sub_number_order = await async_client.external_requirements.sub_number_orders.update(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement={
                "first_name": "Jane",
                "last_name": "Doe",
            },
        )
        assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_requirements.sub_number_orders.with_raw_response.update(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement={
                "first_name": "Jane",
                "last_name": "Doe",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_order = await response.parse()
        assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_requirements.sub_number_orders.with_streaming_response.update(
            sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement={
                "first_name": "Jane",
                "last_name": "Doe",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_order = await response.parse()
            assert_matches_type(SubNumberOrderUpdateResponse, sub_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `regulatory_requirement_id` but received ''"
        ):
            await async_client.external_requirements.sub_number_orders.with_raw_response.update(
                sub_number_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                regulatory_requirement_id="",
                requirement={
                    "first_name": "Jane",
                    "last_name": "Doe",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_number_order_id` but received ''"):
            await async_client.external_requirements.sub_number_orders.with_raw_response.update(
                sub_number_order_id="",
                regulatory_requirement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                requirement={
                    "first_name": "Jane",
                    "last_name": "Doe",
                },
            )
