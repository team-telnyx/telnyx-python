# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.whatsapp import SignupListResponse, SignupRetrieveStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSignup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        signup = client.whatsapp.signup.list()
        assert_matches_type(SyncDefaultFlatPagination[SignupListResponse], signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        signup = client.whatsapp.signup.list(
            filter_created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_customer_id="filter[customer_id]",
            filter_waba_id="filter[waba_id]",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultFlatPagination[SignupListResponse], signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.whatsapp.signup.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signup = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[SignupListResponse], signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.whatsapp.signup.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signup = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[SignupListResponse], signup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: Telnyx) -> None:
        signup = client.whatsapp.signup.retrieve_status(
            "id",
        )
        assert_matches_type(SignupRetrieveStatusResponse, signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: Telnyx) -> None:
        response = client.whatsapp.signup.with_raw_response.retrieve_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signup = response.parse()
        assert_matches_type(SignupRetrieveStatusResponse, signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Telnyx) -> None:
        with client.whatsapp.signup.with_streaming_response.retrieve_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signup = response.parse()
            assert_matches_type(SignupRetrieveStatusResponse, signup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.whatsapp.signup.with_raw_response.retrieve_status(
                "",
            )


class TestAsyncSignup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        signup = await async_client.whatsapp.signup.list()
        assert_matches_type(AsyncDefaultFlatPagination[SignupListResponse], signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        signup = await async_client.whatsapp.signup.list(
            filter_created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_customer_id="filter[customer_id]",
            filter_waba_id="filter[waba_id]",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultFlatPagination[SignupListResponse], signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.signup.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signup = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[SignupListResponse], signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.signup.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signup = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[SignupListResponse], signup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        signup = await async_client.whatsapp.signup.retrieve_status(
            "id",
        )
        assert_matches_type(SignupRetrieveStatusResponse, signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.signup.with_raw_response.retrieve_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signup = await response.parse()
        assert_matches_type(SignupRetrieveStatusResponse, signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.signup.with_streaming_response.retrieve_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signup = await response.parse()
            assert_matches_type(SignupRetrieveStatusResponse, signup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.whatsapp.signup.with_raw_response.retrieve_status(
                "",
            )
