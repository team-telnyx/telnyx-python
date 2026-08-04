# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import EmailValidationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailValidations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        email_validation = client.email_validations.create(
            email="user@example.com",
        )
        assert_matches_type(EmailValidationCreateResponse, email_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        email_validation = client.email_validations.create(
            email="user@example.com",
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        )
        assert_matches_type(EmailValidationCreateResponse, email_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.email_validations.with_raw_response.create(
            email="user@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_validation = response.parse()
        assert_matches_type(EmailValidationCreateResponse, email_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.email_validations.with_streaming_response.create(
            email="user@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_validation = response.parse()
            assert_matches_type(EmailValidationCreateResponse, email_validation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmailValidations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        email_validation = await async_client.email_validations.create(
            email="user@example.com",
        )
        assert_matches_type(EmailValidationCreateResponse, email_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        email_validation = await async_client.email_validations.create(
            email="user@example.com",
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        )
        assert_matches_type(EmailValidationCreateResponse, email_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_validations.with_raw_response.create(
            email="user@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_validation = await response.parse()
        assert_matches_type(EmailValidationCreateResponse, email_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_validations.with_streaming_response.create(
            email="user@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_validation = await response.parse()
            assert_matches_type(EmailValidationCreateResponse, email_validation, path=["response"])

        assert cast(Any, response.is_closed) is True
