# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.whatsapp import (
    HostedSignupListResponse,
    HostedSignupCreateResponse,
    HostedSignupRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHostedSignups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        hosted_signup = client.whatsapp.hosted_signups.create(
            app_id="123456789012345",
        )
        assert_matches_type(HostedSignupCreateResponse, hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        hosted_signup = client.whatsapp.hosted_signups.create(
            app_id="123456789012345",
            expires_at=parse_datetime("2026-07-09T12:00:00Z"),
            signup_type="coexistence",
        )
        assert_matches_type(HostedSignupCreateResponse, hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.whatsapp.hosted_signups.with_raw_response.create(
            app_id="123456789012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hosted_signup = response.parse()
        assert_matches_type(HostedSignupCreateResponse, hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.whatsapp.hosted_signups.with_streaming_response.create(
            app_id="123456789012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hosted_signup = response.parse()
            assert_matches_type(HostedSignupCreateResponse, hosted_signup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        hosted_signup = client.whatsapp.hosted_signups.retrieve(
            "id",
        )
        assert_matches_type(HostedSignupRetrieveResponse, hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.whatsapp.hosted_signups.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hosted_signup = response.parse()
        assert_matches_type(HostedSignupRetrieveResponse, hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.whatsapp.hosted_signups.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hosted_signup = response.parse()
            assert_matches_type(HostedSignupRetrieveResponse, hosted_signup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.whatsapp.hosted_signups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        hosted_signup = client.whatsapp.hosted_signups.list()
        assert_matches_type(SyncDefaultFlatPagination[HostedSignupListResponse], hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        hosted_signup = client.whatsapp.hosted_signups.list(
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultFlatPagination[HostedSignupListResponse], hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.whatsapp.hosted_signups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hosted_signup = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[HostedSignupListResponse], hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.whatsapp.hosted_signups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hosted_signup = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[HostedSignupListResponse], hosted_signup, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHostedSignups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        hosted_signup = await async_client.whatsapp.hosted_signups.create(
            app_id="123456789012345",
        )
        assert_matches_type(HostedSignupCreateResponse, hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        hosted_signup = await async_client.whatsapp.hosted_signups.create(
            app_id="123456789012345",
            expires_at=parse_datetime("2026-07-09T12:00:00Z"),
            signup_type="coexistence",
        )
        assert_matches_type(HostedSignupCreateResponse, hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.hosted_signups.with_raw_response.create(
            app_id="123456789012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hosted_signup = await response.parse()
        assert_matches_type(HostedSignupCreateResponse, hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.hosted_signups.with_streaming_response.create(
            app_id="123456789012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hosted_signup = await response.parse()
            assert_matches_type(HostedSignupCreateResponse, hosted_signup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        hosted_signup = await async_client.whatsapp.hosted_signups.retrieve(
            "id",
        )
        assert_matches_type(HostedSignupRetrieveResponse, hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.hosted_signups.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hosted_signup = await response.parse()
        assert_matches_type(HostedSignupRetrieveResponse, hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.hosted_signups.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hosted_signup = await response.parse()
            assert_matches_type(HostedSignupRetrieveResponse, hosted_signup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.whatsapp.hosted_signups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        hosted_signup = await async_client.whatsapp.hosted_signups.list()
        assert_matches_type(AsyncDefaultFlatPagination[HostedSignupListResponse], hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        hosted_signup = await async_client.whatsapp.hosted_signups.list(
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultFlatPagination[HostedSignupListResponse], hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.hosted_signups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hosted_signup = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[HostedSignupListResponse], hosted_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.hosted_signups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hosted_signup = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[HostedSignupListResponse], hosted_signup, path=["response"])

        assert cast(Any, response.is_closed) is True
