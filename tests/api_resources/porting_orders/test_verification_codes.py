# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.porting_orders import (
    VerificationCodeListResponse,
    VerificationCodeVerifyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerificationCodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        verification_code = client.porting_orders.verification_codes.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VerificationCodeListResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        verification_code = client.porting_orders.verification_codes.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={"verified": True},
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(VerificationCodeListResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.porting_orders.verification_codes.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_code = response.parse()
        assert_matches_type(VerificationCodeListResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.porting_orders.verification_codes.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_code = response.parse()
            assert_matches_type(VerificationCodeListResponse, verification_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.verification_codes.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: Telnyx) -> None:
        verification_code = client.porting_orders.verification_codes.send(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert verification_code is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Telnyx) -> None:
        verification_code = client.porting_orders.verification_codes.send(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_numbers=["+61424000001", "+61424000002"],
            verification_method="sms",
        )
        assert verification_code is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Telnyx) -> None:
        response = client.porting_orders.verification_codes.with_raw_response.send(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_code = response.parse()
        assert verification_code is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Telnyx) -> None:
        with client.porting_orders.verification_codes.with_streaming_response.send(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_code = response.parse()
            assert verification_code is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_send(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.verification_codes.with_raw_response.send(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify(self, client: Telnyx) -> None:
        verification_code = client.porting_orders.verification_codes.verify(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VerificationCodeVerifyResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify_with_all_params(self, client: Telnyx) -> None:
        verification_code = client.porting_orders.verification_codes.verify(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            verification_codes=[
                {
                    "code": "12345",
                    "phone_number": "+61424000001",
                },
                {
                    "code": "54321",
                    "phone_number": "+61424000002",
                },
            ],
        )
        assert_matches_type(VerificationCodeVerifyResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: Telnyx) -> None:
        response = client.porting_orders.verification_codes.with_raw_response.verify(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_code = response.parse()
        assert_matches_type(VerificationCodeVerifyResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: Telnyx) -> None:
        with client.porting_orders.verification_codes.with_streaming_response.verify(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_code = response.parse()
            assert_matches_type(VerificationCodeVerifyResponse, verification_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_verify(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.verification_codes.with_raw_response.verify(
                id="",
            )


class TestAsyncVerificationCodes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        verification_code = await async_client.porting_orders.verification_codes.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VerificationCodeListResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        verification_code = await async_client.porting_orders.verification_codes.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={"verified": True},
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(VerificationCodeListResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.verification_codes.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_code = await response.parse()
        assert_matches_type(VerificationCodeListResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.verification_codes.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_code = await response.parse()
            assert_matches_type(VerificationCodeListResponse, verification_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.verification_codes.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncTelnyx) -> None:
        verification_code = await async_client.porting_orders.verification_codes.send(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert verification_code is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncTelnyx) -> None:
        verification_code = await async_client.porting_orders.verification_codes.send(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_numbers=["+61424000001", "+61424000002"],
            verification_method="sms",
        )
        assert verification_code is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.verification_codes.with_raw_response.send(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_code = await response.parse()
        assert verification_code is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.verification_codes.with_streaming_response.send(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_code = await response.parse()
            assert verification_code is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.verification_codes.with_raw_response.send(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncTelnyx) -> None:
        verification_code = await async_client.porting_orders.verification_codes.verify(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VerificationCodeVerifyResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify_with_all_params(self, async_client: AsyncTelnyx) -> None:
        verification_code = await async_client.porting_orders.verification_codes.verify(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            verification_codes=[
                {
                    "code": "12345",
                    "phone_number": "+61424000001",
                },
                {
                    "code": "54321",
                    "phone_number": "+61424000002",
                },
            ],
        )
        assert_matches_type(VerificationCodeVerifyResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.verification_codes.with_raw_response.verify(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_code = await response.parse()
        assert_matches_type(VerificationCodeVerifyResponse, verification_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.verification_codes.with_streaming_response.verify(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_code = await response.parse()
            assert_matches_type(VerificationCodeVerifyResponse, verification_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_verify(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.verification_codes.with_raw_response.verify(
                id="",
            )
