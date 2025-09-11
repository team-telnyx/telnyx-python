# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.porting_orders import (
    PhoneNumberBlockListResponse,
    PhoneNumberBlockCreateResponse,
    PhoneNumberBlockDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumberBlocks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        phone_number_block = client.porting_orders.phone_number_blocks.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": "+4930244999910",
                    "start_at": "+4930244999901",
                }
            ],
            phone_number_range={
                "end_at": "+4930244999910",
                "start_at": "+4930244999901",
            },
        )
        assert_matches_type(PhoneNumberBlockCreateResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.porting_orders.phone_number_blocks.with_raw_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": "+4930244999910",
                    "start_at": "+4930244999901",
                }
            ],
            phone_number_range={
                "end_at": "+4930244999910",
                "start_at": "+4930244999901",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_block = response.parse()
        assert_matches_type(PhoneNumberBlockCreateResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.porting_orders.phone_number_blocks.with_streaming_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": "+4930244999910",
                    "start_at": "+4930244999901",
                }
            ],
            phone_number_range={
                "end_at": "+4930244999910",
                "start_at": "+4930244999901",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_block = response.parse()
            assert_matches_type(PhoneNumberBlockCreateResponse, phone_number_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            client.porting_orders.phone_number_blocks.with_raw_response.create(
                porting_order_id="",
                activation_ranges=[
                    {
                        "end_at": "+4930244999910",
                        "start_at": "+4930244999901",
                    }
                ],
                phone_number_range={
                    "end_at": "+4930244999910",
                    "start_at": "+4930244999901",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        phone_number_block = client.porting_orders.phone_number_blocks.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberBlockListResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        phone_number_block = client.porting_orders.phone_number_blocks.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={
                "activation_status": "Active",
                "phone_number": ["+12003151212"],
                "portability_status": "confirmed",
                "porting_order_id": ["f3575e15-32ce-400e-a4c0-dd78800c20b0"],
                "status": "in-process",
                "support_key": "sr_a12345",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "-created_at"},
        )
        assert_matches_type(PhoneNumberBlockListResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.porting_orders.phone_number_blocks.with_raw_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_block = response.parse()
        assert_matches_type(PhoneNumberBlockListResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.porting_orders.phone_number_blocks.with_streaming_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_block = response.parse()
            assert_matches_type(PhoneNumberBlockListResponse, phone_number_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            client.porting_orders.phone_number_blocks.with_raw_response.list(
                porting_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        phone_number_block = client.porting_orders.phone_number_blocks.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberBlockDeleteResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.porting_orders.phone_number_blocks.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_block = response.parse()
        assert_matches_type(PhoneNumberBlockDeleteResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.porting_orders.phone_number_blocks.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_block = response.parse()
            assert_matches_type(PhoneNumberBlockDeleteResponse, phone_number_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            client.porting_orders.phone_number_blocks.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                porting_order_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.phone_number_blocks.with_raw_response.delete(
                id="",
                porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncPhoneNumberBlocks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        phone_number_block = await async_client.porting_orders.phone_number_blocks.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": "+4930244999910",
                    "start_at": "+4930244999901",
                }
            ],
            phone_number_range={
                "end_at": "+4930244999910",
                "start_at": "+4930244999901",
            },
        )
        assert_matches_type(PhoneNumberBlockCreateResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.phone_number_blocks.with_raw_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": "+4930244999910",
                    "start_at": "+4930244999901",
                }
            ],
            phone_number_range={
                "end_at": "+4930244999910",
                "start_at": "+4930244999901",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_block = await response.parse()
        assert_matches_type(PhoneNumberBlockCreateResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.phone_number_blocks.with_streaming_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": "+4930244999910",
                    "start_at": "+4930244999901",
                }
            ],
            phone_number_range={
                "end_at": "+4930244999910",
                "start_at": "+4930244999901",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_block = await response.parse()
            assert_matches_type(PhoneNumberBlockCreateResponse, phone_number_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            await async_client.porting_orders.phone_number_blocks.with_raw_response.create(
                porting_order_id="",
                activation_ranges=[
                    {
                        "end_at": "+4930244999910",
                        "start_at": "+4930244999901",
                    }
                ],
                phone_number_range={
                    "end_at": "+4930244999910",
                    "start_at": "+4930244999901",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        phone_number_block = await async_client.porting_orders.phone_number_blocks.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberBlockListResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number_block = await async_client.porting_orders.phone_number_blocks.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={
                "activation_status": "Active",
                "phone_number": ["+12003151212"],
                "portability_status": "confirmed",
                "porting_order_id": ["f3575e15-32ce-400e-a4c0-dd78800c20b0"],
                "status": "in-process",
                "support_key": "sr_a12345",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "-created_at"},
        )
        assert_matches_type(PhoneNumberBlockListResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.phone_number_blocks.with_raw_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_block = await response.parse()
        assert_matches_type(PhoneNumberBlockListResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.phone_number_blocks.with_streaming_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_block = await response.parse()
            assert_matches_type(PhoneNumberBlockListResponse, phone_number_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            await async_client.porting_orders.phone_number_blocks.with_raw_response.list(
                porting_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        phone_number_block = await async_client.porting_orders.phone_number_blocks.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberBlockDeleteResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.phone_number_blocks.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_block = await response.parse()
        assert_matches_type(PhoneNumberBlockDeleteResponse, phone_number_block, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.phone_number_blocks.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_block = await response.parse()
            assert_matches_type(PhoneNumberBlockDeleteResponse, phone_number_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            await async_client.porting_orders.phone_number_blocks.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                porting_order_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.phone_number_blocks.with_raw_response.delete(
                id="",
                porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
