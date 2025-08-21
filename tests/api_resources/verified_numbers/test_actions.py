# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import VerifiedNumberDataWrapper

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_verification_code(self, client: Telnyx) -> None:
        action = client.verified_numbers.actions.submit_verification_code(
            phone_number="+15551234567",
            verification_code="123456",
        )
        assert_matches_type(VerifiedNumberDataWrapper, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_verification_code(self, client: Telnyx) -> None:
        response = client.verified_numbers.actions.with_raw_response.submit_verification_code(
            phone_number="+15551234567",
            verification_code="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(VerifiedNumberDataWrapper, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_verification_code(self, client: Telnyx) -> None:
        with client.verified_numbers.actions.with_streaming_response.submit_verification_code(
            phone_number="+15551234567",
            verification_code="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(VerifiedNumberDataWrapper, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_submit_verification_code(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.verified_numbers.actions.with_raw_response.submit_verification_code(
                phone_number="",
                verification_code="123456",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_verification_code(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.verified_numbers.actions.submit_verification_code(
            phone_number="+15551234567",
            verification_code="123456",
        )
        assert_matches_type(VerifiedNumberDataWrapper, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_verification_code(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verified_numbers.actions.with_raw_response.submit_verification_code(
            phone_number="+15551234567",
            verification_code="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(VerifiedNumberDataWrapper, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_verification_code(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verified_numbers.actions.with_streaming_response.submit_verification_code(
            phone_number="+15551234567",
            verification_code="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(VerifiedNumberDataWrapper, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_submit_verification_code(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.verified_numbers.actions.with_raw_response.submit_verification_code(
                phone_number="",
                verification_code="123456",
            )
