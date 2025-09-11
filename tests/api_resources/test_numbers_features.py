# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import NumbersFeatureCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumbersFeatures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        numbers_feature = client.numbers_features.create(
            phone_numbers=["string"],
        )
        assert_matches_type(NumbersFeatureCreateResponse, numbers_feature, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.numbers_features.with_raw_response.create(
            phone_numbers=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        numbers_feature = response.parse()
        assert_matches_type(NumbersFeatureCreateResponse, numbers_feature, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.numbers_features.with_streaming_response.create(
            phone_numbers=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            numbers_feature = response.parse()
            assert_matches_type(NumbersFeatureCreateResponse, numbers_feature, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNumbersFeatures:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        numbers_feature = await async_client.numbers_features.create(
            phone_numbers=["string"],
        )
        assert_matches_type(NumbersFeatureCreateResponse, numbers_feature, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.numbers_features.with_raw_response.create(
            phone_numbers=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        numbers_feature = await response.parse()
        assert_matches_type(NumbersFeatureCreateResponse, numbers_feature, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.numbers_features.with_streaming_response.create(
            phone_numbers=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            numbers_feature = await response.parse()
            assert_matches_type(NumbersFeatureCreateResponse, numbers_feature, path=["response"])

        assert cast(Any, response.is_closed) is True
