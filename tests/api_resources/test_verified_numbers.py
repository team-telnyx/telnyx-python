# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    VerifiedNumberDataWrapper,
    VerifiedNumberListResponse,
    VerifiedNumberCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifiedNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        verified_number = client.verified_numbers.create(
            phone_number="+15551234567",
            verification_method="sms",
        )
        assert_matches_type(VerifiedNumberCreateResponse, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.verified_numbers.with_raw_response.create(
            phone_number="+15551234567",
            verification_method="sms",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_number = response.parse()
        assert_matches_type(VerifiedNumberCreateResponse, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.verified_numbers.with_streaming_response.create(
            phone_number="+15551234567",
            verification_method="sms",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_number = response.parse()
            assert_matches_type(VerifiedNumberCreateResponse, verified_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        verified_number = client.verified_numbers.retrieve(
            "+15551234567",
        )
        assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.verified_numbers.with_raw_response.retrieve(
            "+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_number = response.parse()
        assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.verified_numbers.with_streaming_response.retrieve(
            "+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_number = response.parse()
            assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.verified_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        verified_number = client.verified_numbers.list()
        assert_matches_type(VerifiedNumberListResponse, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        verified_number = client.verified_numbers.list(
            page={
                "number": 0,
                "size": 0,
            },
        )
        assert_matches_type(VerifiedNumberListResponse, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.verified_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_number = response.parse()
        assert_matches_type(VerifiedNumberListResponse, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.verified_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_number = response.parse()
            assert_matches_type(VerifiedNumberListResponse, verified_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        verified_number = client.verified_numbers.delete(
            "+15551234567",
        )
        assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.verified_numbers.with_raw_response.delete(
            "+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_number = response.parse()
        assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.verified_numbers.with_streaming_response.delete(
            "+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_number = response.parse()
            assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.verified_numbers.with_raw_response.delete(
                "",
            )


class TestAsyncVerifiedNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        verified_number = await async_client.verified_numbers.create(
            phone_number="+15551234567",
            verification_method="sms",
        )
        assert_matches_type(VerifiedNumberCreateResponse, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verified_numbers.with_raw_response.create(
            phone_number="+15551234567",
            verification_method="sms",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_number = await response.parse()
        assert_matches_type(VerifiedNumberCreateResponse, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verified_numbers.with_streaming_response.create(
            phone_number="+15551234567",
            verification_method="sms",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_number = await response.parse()
            assert_matches_type(VerifiedNumberCreateResponse, verified_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        verified_number = await async_client.verified_numbers.retrieve(
            "+15551234567",
        )
        assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verified_numbers.with_raw_response.retrieve(
            "+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_number = await response.parse()
        assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verified_numbers.with_streaming_response.retrieve(
            "+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_number = await response.parse()
            assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.verified_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        verified_number = await async_client.verified_numbers.list()
        assert_matches_type(VerifiedNumberListResponse, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        verified_number = await async_client.verified_numbers.list(
            page={
                "number": 0,
                "size": 0,
            },
        )
        assert_matches_type(VerifiedNumberListResponse, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verified_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_number = await response.parse()
        assert_matches_type(VerifiedNumberListResponse, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verified_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_number = await response.parse()
            assert_matches_type(VerifiedNumberListResponse, verified_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        verified_number = await async_client.verified_numbers.delete(
            "+15551234567",
        )
        assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verified_numbers.with_raw_response.delete(
            "+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_number = await response.parse()
        assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verified_numbers.with_streaming_response.delete(
            "+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_number = await response.parse()
            assert_matches_type(VerifiedNumberDataWrapper, verified_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.verified_numbers.with_raw_response.delete(
                "",
            )
