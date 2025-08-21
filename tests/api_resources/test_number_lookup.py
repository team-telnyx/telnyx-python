# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import NumberLookupRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumberLookup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        number_lookup = client.number_lookup.retrieve(
            phone_number="+18665552368",
        )
        assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        number_lookup = client.number_lookup.retrieve(
            phone_number="+18665552368",
            type="carrier",
        )
        assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.number_lookup.with_raw_response.retrieve(
            phone_number="+18665552368",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_lookup = response.parse()
        assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.number_lookup.with_streaming_response.retrieve(
            phone_number="+18665552368",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_lookup = response.parse()
            assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.number_lookup.with_raw_response.retrieve(
                phone_number="",
            )


class TestAsyncNumberLookup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        number_lookup = await async_client.number_lookup.retrieve(
            phone_number="+18665552368",
        )
        assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number_lookup = await async_client.number_lookup.retrieve(
            phone_number="+18665552368",
            type="carrier",
        )
        assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_lookup.with_raw_response.retrieve(
            phone_number="+18665552368",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_lookup = await response.parse()
        assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_lookup.with_streaming_response.retrieve(
            phone_number="+18665552368",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_lookup = await response.parse()
            assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.number_lookup.with_raw_response.retrieve(
                phone_number="",
            )
