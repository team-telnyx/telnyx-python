# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    ShortCodeListResponse,
    ShortCodeUpdateResponse,
    ShortCodeRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShortCodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        short_code = client.short_codes.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ShortCodeRetrieveResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.short_codes.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        short_code = response.parse()
        assert_matches_type(ShortCodeRetrieveResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.short_codes.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            short_code = response.parse()
            assert_matches_type(ShortCodeRetrieveResponse, short_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.short_codes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        short_code = client.short_codes.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
        )
        assert_matches_type(ShortCodeUpdateResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.short_codes.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        short_code = response.parse()
        assert_matches_type(ShortCodeUpdateResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.short_codes.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            short_code = response.parse()
            assert_matches_type(ShortCodeUpdateResponse, short_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.short_codes.with_raw_response.update(
                id="",
                messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        short_code = client.short_codes.list()
        assert_matches_type(ShortCodeListResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        short_code = client.short_codes.list(
            filter={"messaging_profile_id": "messaging_profile_id"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ShortCodeListResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.short_codes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        short_code = response.parse()
        assert_matches_type(ShortCodeListResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.short_codes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            short_code = response.parse()
            assert_matches_type(ShortCodeListResponse, short_code, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShortCodes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        short_code = await async_client.short_codes.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ShortCodeRetrieveResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.short_codes.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        short_code = await response.parse()
        assert_matches_type(ShortCodeRetrieveResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.short_codes.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            short_code = await response.parse()
            assert_matches_type(ShortCodeRetrieveResponse, short_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.short_codes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        short_code = await async_client.short_codes.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
        )
        assert_matches_type(ShortCodeUpdateResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.short_codes.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        short_code = await response.parse()
        assert_matches_type(ShortCodeUpdateResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.short_codes.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            short_code = await response.parse()
            assert_matches_type(ShortCodeUpdateResponse, short_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.short_codes.with_raw_response.update(
                id="",
                messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        short_code = await async_client.short_codes.list()
        assert_matches_type(ShortCodeListResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        short_code = await async_client.short_codes.list(
            filter={"messaging_profile_id": "messaging_profile_id"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ShortCodeListResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.short_codes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        short_code = await response.parse()
        assert_matches_type(ShortCodeListResponse, short_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.short_codes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            short_code = await response.parse()
            assert_matches_type(ShortCodeListResponse, short_code, path=["response"])

        assert cast(Any, response.is_closed) is True
