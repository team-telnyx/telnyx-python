# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.verifications import ByPhoneNumberListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestByPhoneNumber:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        by_phone_number = client.verifications.by_phone_number.list(
            "+13035551234",
        )
        assert_matches_type(ByPhoneNumberListResponse, by_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.verifications.by_phone_number.with_raw_response.list(
            "+13035551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_phone_number = response.parse()
        assert_matches_type(ByPhoneNumberListResponse, by_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.verifications.by_phone_number.with_streaming_response.list(
            "+13035551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_phone_number = response.parse()
            assert_matches_type(ByPhoneNumberListResponse, by_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.verifications.by_phone_number.with_raw_response.list(
                "",
            )


class TestAsyncByPhoneNumber:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        by_phone_number = await async_client.verifications.by_phone_number.list(
            "+13035551234",
        )
        assert_matches_type(ByPhoneNumberListResponse, by_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verifications.by_phone_number.with_raw_response.list(
            "+13035551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_phone_number = await response.parse()
        assert_matches_type(ByPhoneNumberListResponse, by_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verifications.by_phone_number.with_streaming_response.list(
            "+13035551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_phone_number = await response.parse()
            assert_matches_type(ByPhoneNumberListResponse, by_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.verifications.by_phone_number.with_raw_response.list(
                "",
            )
