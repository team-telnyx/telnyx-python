# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.enterprises import EnterpriseEmailVerificationStatusWrapped

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifyEmail:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        verify_email = client.enterprises.verify_email.create(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.enterprises.verify_email.with_raw_response.create(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_email = response.parse()
        assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.enterprises.verify_email.with_streaming_response.create(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_email = response.parse()
            assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.verify_email.with_raw_response.create(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_confirm(self, client: Telnyx) -> None:
        verify_email = client.enterprises.verify_email.confirm(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            code="482915",
        )
        assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_confirm(self, client: Telnyx) -> None:
        response = client.enterprises.verify_email.with_raw_response.confirm(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            code="482915",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_email = response.parse()
        assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_confirm(self, client: Telnyx) -> None:
        with client.enterprises.verify_email.with_streaming_response.confirm(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            code="482915",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_email = response.parse()
            assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_confirm(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.verify_email.with_raw_response.confirm(
                enterprise_id="",
                code="482915",
            )


class TestAsyncVerifyEmail:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        verify_email = await async_client.enterprises.verify_email.create(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.verify_email.with_raw_response.create(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_email = await response.parse()
        assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.verify_email.with_streaming_response.create(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_email = await response.parse()
            assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.verify_email.with_raw_response.create(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_confirm(self, async_client: AsyncTelnyx) -> None:
        verify_email = await async_client.enterprises.verify_email.confirm(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            code="482915",
        )
        assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.verify_email.with_raw_response.confirm(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            code="482915",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_email = await response.parse()
        assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.verify_email.with_streaming_response.confirm(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            code="482915",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_email = await response.parse()
            assert_matches_type(EnterpriseEmailVerificationStatusWrapped, verify_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_confirm(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.verify_email.with_raw_response.confirm(
                enterprise_id="",
                code="482915",
            )
