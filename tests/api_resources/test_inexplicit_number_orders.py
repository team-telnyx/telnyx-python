# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    InexplicitNumberOrderResponse,
    InexplicitNumberOrderCreateResponse,
    InexplicitNumberOrderRetrieveResponse,
)
from telnyx.pagination import (
    SyncDefaultFlatPaginationForInexplicitNumberOrders,
    AsyncDefaultFlatPaginationForInexplicitNumberOrders,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInexplicitNumberOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        inexplicit_number_order = client.inexplicit_number_orders.create(
            ordering_groups=[
                {
                    "count_requested": "count_requested",
                    "country_iso": "US",
                    "phone_number_type": "phone_number_type",
                }
            ],
        )
        assert_matches_type(InexplicitNumberOrderCreateResponse, inexplicit_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        inexplicit_number_order = client.inexplicit_number_orders.create(
            ordering_groups=[
                {
                    "count_requested": "count_requested",
                    "country_iso": "US",
                    "phone_number_type": "phone_number_type",
                    "administrative_area": "administrative_area",
                    "exclude_held_numbers": True,
                    "features": ["string"],
                    "locality": "locality",
                    "national_destination_code": "national_destination_code",
                    "phone_number": {
                        "contains": "contains",
                        "ends_with": "ends_with",
                        "starts_with": "starts_with",
                    },
                    "quickship": True,
                    "strategy": "always",
                }
            ],
            billing_group_id="billing_group_id",
            connection_id="connection_id",
            customer_reference="customer_reference",
            messaging_profile_id="messaging_profile_id",
        )
        assert_matches_type(InexplicitNumberOrderCreateResponse, inexplicit_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.inexplicit_number_orders.with_raw_response.create(
            ordering_groups=[
                {
                    "count_requested": "count_requested",
                    "country_iso": "US",
                    "phone_number_type": "phone_number_type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inexplicit_number_order = response.parse()
        assert_matches_type(InexplicitNumberOrderCreateResponse, inexplicit_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.inexplicit_number_orders.with_streaming_response.create(
            ordering_groups=[
                {
                    "count_requested": "count_requested",
                    "country_iso": "US",
                    "phone_number_type": "phone_number_type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inexplicit_number_order = response.parse()
            assert_matches_type(InexplicitNumberOrderCreateResponse, inexplicit_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        inexplicit_number_order = client.inexplicit_number_orders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InexplicitNumberOrderRetrieveResponse, inexplicit_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.inexplicit_number_orders.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inexplicit_number_order = response.parse()
        assert_matches_type(InexplicitNumberOrderRetrieveResponse, inexplicit_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.inexplicit_number_orders.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inexplicit_number_order = response.parse()
            assert_matches_type(InexplicitNumberOrderRetrieveResponse, inexplicit_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.inexplicit_number_orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        inexplicit_number_order = client.inexplicit_number_orders.list()
        assert_matches_type(
            SyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse],
            inexplicit_number_order,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        inexplicit_number_order = client.inexplicit_number_orders.list(
            page_number=1,
            page_size=1,
        )
        assert_matches_type(
            SyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse],
            inexplicit_number_order,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.inexplicit_number_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inexplicit_number_order = response.parse()
        assert_matches_type(
            SyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse],
            inexplicit_number_order,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.inexplicit_number_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inexplicit_number_order = response.parse()
            assert_matches_type(
                SyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse],
                inexplicit_number_order,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncInexplicitNumberOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        inexplicit_number_order = await async_client.inexplicit_number_orders.create(
            ordering_groups=[
                {
                    "count_requested": "count_requested",
                    "country_iso": "US",
                    "phone_number_type": "phone_number_type",
                }
            ],
        )
        assert_matches_type(InexplicitNumberOrderCreateResponse, inexplicit_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        inexplicit_number_order = await async_client.inexplicit_number_orders.create(
            ordering_groups=[
                {
                    "count_requested": "count_requested",
                    "country_iso": "US",
                    "phone_number_type": "phone_number_type",
                    "administrative_area": "administrative_area",
                    "exclude_held_numbers": True,
                    "features": ["string"],
                    "locality": "locality",
                    "national_destination_code": "national_destination_code",
                    "phone_number": {
                        "contains": "contains",
                        "ends_with": "ends_with",
                        "starts_with": "starts_with",
                    },
                    "quickship": True,
                    "strategy": "always",
                }
            ],
            billing_group_id="billing_group_id",
            connection_id="connection_id",
            customer_reference="customer_reference",
            messaging_profile_id="messaging_profile_id",
        )
        assert_matches_type(InexplicitNumberOrderCreateResponse, inexplicit_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.inexplicit_number_orders.with_raw_response.create(
            ordering_groups=[
                {
                    "count_requested": "count_requested",
                    "country_iso": "US",
                    "phone_number_type": "phone_number_type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inexplicit_number_order = await response.parse()
        assert_matches_type(InexplicitNumberOrderCreateResponse, inexplicit_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.inexplicit_number_orders.with_streaming_response.create(
            ordering_groups=[
                {
                    "count_requested": "count_requested",
                    "country_iso": "US",
                    "phone_number_type": "phone_number_type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inexplicit_number_order = await response.parse()
            assert_matches_type(InexplicitNumberOrderCreateResponse, inexplicit_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        inexplicit_number_order = await async_client.inexplicit_number_orders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InexplicitNumberOrderRetrieveResponse, inexplicit_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.inexplicit_number_orders.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inexplicit_number_order = await response.parse()
        assert_matches_type(InexplicitNumberOrderRetrieveResponse, inexplicit_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.inexplicit_number_orders.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inexplicit_number_order = await response.parse()
            assert_matches_type(InexplicitNumberOrderRetrieveResponse, inexplicit_number_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.inexplicit_number_orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        inexplicit_number_order = await async_client.inexplicit_number_orders.list()
        assert_matches_type(
            AsyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse],
            inexplicit_number_order,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        inexplicit_number_order = await async_client.inexplicit_number_orders.list(
            page_number=1,
            page_size=1,
        )
        assert_matches_type(
            AsyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse],
            inexplicit_number_order,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.inexplicit_number_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inexplicit_number_order = await response.parse()
        assert_matches_type(
            AsyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse],
            inexplicit_number_order,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.inexplicit_number_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inexplicit_number_order = await response.parse()
            assert_matches_type(
                AsyncDefaultFlatPaginationForInexplicitNumberOrders[InexplicitNumberOrderResponse],
                inexplicit_number_order,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
