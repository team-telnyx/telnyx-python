# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.porting_orders import (
    AssociatedPhoneNumberListResponse,
    AssociatedPhoneNumberCreateResponse,
    AssociatedPhoneNumberDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssociatedPhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        associated_phone_number = client.porting_orders.associated_phone_numbers.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="keep",
            phone_number_range={},
        )
        assert_matches_type(AssociatedPhoneNumberCreateResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        associated_phone_number = client.porting_orders.associated_phone_numbers.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="keep",
            phone_number_range={
                "end_at": "+441234567899",
                "start_at": "+441234567890",
            },
        )
        assert_matches_type(AssociatedPhoneNumberCreateResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.porting_orders.associated_phone_numbers.with_raw_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="keep",
            phone_number_range={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        associated_phone_number = response.parse()
        assert_matches_type(AssociatedPhoneNumberCreateResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.porting_orders.associated_phone_numbers.with_streaming_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="keep",
            phone_number_range={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            associated_phone_number = response.parse()
            assert_matches_type(AssociatedPhoneNumberCreateResponse, associated_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            client.porting_orders.associated_phone_numbers.with_raw_response.create(
                porting_order_id="",
                action="keep",
                phone_number_range={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        associated_phone_number = client.porting_orders.associated_phone_numbers.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AssociatedPhoneNumberListResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        associated_phone_number = client.porting_orders.associated_phone_numbers.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={
                "action": "keep",
                "phone_number": "+441234567890",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "-created_at"},
        )
        assert_matches_type(AssociatedPhoneNumberListResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.porting_orders.associated_phone_numbers.with_raw_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        associated_phone_number = response.parse()
        assert_matches_type(AssociatedPhoneNumberListResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.porting_orders.associated_phone_numbers.with_streaming_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            associated_phone_number = response.parse()
            assert_matches_type(AssociatedPhoneNumberListResponse, associated_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            client.porting_orders.associated_phone_numbers.with_raw_response.list(
                porting_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        associated_phone_number = client.porting_orders.associated_phone_numbers.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AssociatedPhoneNumberDeleteResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.porting_orders.associated_phone_numbers.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        associated_phone_number = response.parse()
        assert_matches_type(AssociatedPhoneNumberDeleteResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.porting_orders.associated_phone_numbers.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            associated_phone_number = response.parse()
            assert_matches_type(AssociatedPhoneNumberDeleteResponse, associated_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            client.porting_orders.associated_phone_numbers.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                porting_order_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.associated_phone_numbers.with_raw_response.delete(
                id="",
                porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncAssociatedPhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        associated_phone_number = await async_client.porting_orders.associated_phone_numbers.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="keep",
            phone_number_range={},
        )
        assert_matches_type(AssociatedPhoneNumberCreateResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        associated_phone_number = await async_client.porting_orders.associated_phone_numbers.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="keep",
            phone_number_range={
                "end_at": "+441234567899",
                "start_at": "+441234567890",
            },
        )
        assert_matches_type(AssociatedPhoneNumberCreateResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.associated_phone_numbers.with_raw_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="keep",
            phone_number_range={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        associated_phone_number = await response.parse()
        assert_matches_type(AssociatedPhoneNumberCreateResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.associated_phone_numbers.with_streaming_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="keep",
            phone_number_range={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            associated_phone_number = await response.parse()
            assert_matches_type(AssociatedPhoneNumberCreateResponse, associated_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            await async_client.porting_orders.associated_phone_numbers.with_raw_response.create(
                porting_order_id="",
                action="keep",
                phone_number_range={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        associated_phone_number = await async_client.porting_orders.associated_phone_numbers.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AssociatedPhoneNumberListResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        associated_phone_number = await async_client.porting_orders.associated_phone_numbers.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={
                "action": "keep",
                "phone_number": "+441234567890",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "-created_at"},
        )
        assert_matches_type(AssociatedPhoneNumberListResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.associated_phone_numbers.with_raw_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        associated_phone_number = await response.parse()
        assert_matches_type(AssociatedPhoneNumberListResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.associated_phone_numbers.with_streaming_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            associated_phone_number = await response.parse()
            assert_matches_type(AssociatedPhoneNumberListResponse, associated_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            await async_client.porting_orders.associated_phone_numbers.with_raw_response.list(
                porting_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        associated_phone_number = await async_client.porting_orders.associated_phone_numbers.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AssociatedPhoneNumberDeleteResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.associated_phone_numbers.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        associated_phone_number = await response.parse()
        assert_matches_type(AssociatedPhoneNumberDeleteResponse, associated_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.associated_phone_numbers.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            associated_phone_number = await response.parse()
            assert_matches_type(AssociatedPhoneNumberDeleteResponse, associated_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            await async_client.porting_orders.associated_phone_numbers.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                porting_order_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.associated_phone_numbers.with_raw_response.delete(
                id="",
                porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
