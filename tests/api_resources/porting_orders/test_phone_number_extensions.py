# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.porting_orders import (
    PhoneNumberExtensionListResponse,
    PhoneNumberExtensionCreateResponse,
    PhoneNumberExtensionDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumberExtensions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        phone_number_extension = client.porting_orders.phone_number_extensions.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": 10,
                    "start_at": 1,
                }
            ],
            extension_range={
                "end_at": 10,
                "start_at": 1,
            },
            porting_phone_number_id="f24151b6-3389-41d3-8747-7dd8c681e5e2",
        )
        assert_matches_type(PhoneNumberExtensionCreateResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.porting_orders.phone_number_extensions.with_raw_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": 10,
                    "start_at": 1,
                }
            ],
            extension_range={
                "end_at": 10,
                "start_at": 1,
            },
            porting_phone_number_id="f24151b6-3389-41d3-8747-7dd8c681e5e2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_extension = response.parse()
        assert_matches_type(PhoneNumberExtensionCreateResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.porting_orders.phone_number_extensions.with_streaming_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": 10,
                    "start_at": 1,
                }
            ],
            extension_range={
                "end_at": 10,
                "start_at": 1,
            },
            porting_phone_number_id="f24151b6-3389-41d3-8747-7dd8c681e5e2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_extension = response.parse()
            assert_matches_type(PhoneNumberExtensionCreateResponse, phone_number_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            client.porting_orders.phone_number_extensions.with_raw_response.create(
                porting_order_id="",
                activation_ranges=[
                    {
                        "end_at": 10,
                        "start_at": 1,
                    }
                ],
                extension_range={
                    "end_at": 10,
                    "start_at": 1,
                },
                porting_phone_number_id="f24151b6-3389-41d3-8747-7dd8c681e5e2",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        phone_number_extension = client.porting_orders.phone_number_extensions.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberExtensionListResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        phone_number_extension = client.porting_orders.phone_number_extensions.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={"porting_phone_number_id": "04f8f1b9-310c-4a3c-963e-7dfc54765140"},
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "-created_at"},
        )
        assert_matches_type(PhoneNumberExtensionListResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.porting_orders.phone_number_extensions.with_raw_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_extension = response.parse()
        assert_matches_type(PhoneNumberExtensionListResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.porting_orders.phone_number_extensions.with_streaming_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_extension = response.parse()
            assert_matches_type(PhoneNumberExtensionListResponse, phone_number_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            client.porting_orders.phone_number_extensions.with_raw_response.list(
                porting_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        phone_number_extension = client.porting_orders.phone_number_extensions.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberExtensionDeleteResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.porting_orders.phone_number_extensions.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_extension = response.parse()
        assert_matches_type(PhoneNumberExtensionDeleteResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.porting_orders.phone_number_extensions.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_extension = response.parse()
            assert_matches_type(PhoneNumberExtensionDeleteResponse, phone_number_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            client.porting_orders.phone_number_extensions.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                porting_order_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.phone_number_extensions.with_raw_response.delete(
                id="",
                porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncPhoneNumberExtensions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        phone_number_extension = await async_client.porting_orders.phone_number_extensions.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": 10,
                    "start_at": 1,
                }
            ],
            extension_range={
                "end_at": 10,
                "start_at": 1,
            },
            porting_phone_number_id="f24151b6-3389-41d3-8747-7dd8c681e5e2",
        )
        assert_matches_type(PhoneNumberExtensionCreateResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.phone_number_extensions.with_raw_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": 10,
                    "start_at": 1,
                }
            ],
            extension_range={
                "end_at": 10,
                "start_at": 1,
            },
            porting_phone_number_id="f24151b6-3389-41d3-8747-7dd8c681e5e2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_extension = await response.parse()
        assert_matches_type(PhoneNumberExtensionCreateResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.phone_number_extensions.with_streaming_response.create(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_ranges=[
                {
                    "end_at": 10,
                    "start_at": 1,
                }
            ],
            extension_range={
                "end_at": 10,
                "start_at": 1,
            },
            porting_phone_number_id="f24151b6-3389-41d3-8747-7dd8c681e5e2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_extension = await response.parse()
            assert_matches_type(PhoneNumberExtensionCreateResponse, phone_number_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            await async_client.porting_orders.phone_number_extensions.with_raw_response.create(
                porting_order_id="",
                activation_ranges=[
                    {
                        "end_at": 10,
                        "start_at": 1,
                    }
                ],
                extension_range={
                    "end_at": 10,
                    "start_at": 1,
                },
                porting_phone_number_id="f24151b6-3389-41d3-8747-7dd8c681e5e2",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        phone_number_extension = await async_client.porting_orders.phone_number_extensions.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberExtensionListResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number_extension = await async_client.porting_orders.phone_number_extensions.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={"porting_phone_number_id": "04f8f1b9-310c-4a3c-963e-7dfc54765140"},
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "-created_at"},
        )
        assert_matches_type(PhoneNumberExtensionListResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.phone_number_extensions.with_raw_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_extension = await response.parse()
        assert_matches_type(PhoneNumberExtensionListResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.phone_number_extensions.with_streaming_response.list(
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_extension = await response.parse()
            assert_matches_type(PhoneNumberExtensionListResponse, phone_number_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            await async_client.porting_orders.phone_number_extensions.with_raw_response.list(
                porting_order_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        phone_number_extension = await async_client.porting_orders.phone_number_extensions.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberExtensionDeleteResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.phone_number_extensions.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_extension = await response.parse()
        assert_matches_type(PhoneNumberExtensionDeleteResponse, phone_number_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.phone_number_extensions.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_extension = await response.parse()
            assert_matches_type(PhoneNumberExtensionDeleteResponse, phone_number_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `porting_order_id` but received ''"):
            await async_client.porting_orders.phone_number_extensions.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                porting_order_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.phone_number_extensions.with_raw_response.delete(
                id="",
                porting_order_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
