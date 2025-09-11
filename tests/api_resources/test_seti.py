# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import SetiRetrieveBlackBoxTestResultsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeti:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_black_box_test_results(self, client: Telnyx) -> None:
        seti = client.seti.retrieve_black_box_test_results()
        assert_matches_type(SetiRetrieveBlackBoxTestResultsResponse, seti, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_black_box_test_results_with_all_params(self, client: Telnyx) -> None:
        seti = client.seti.retrieve_black_box_test_results(
            filter={"product": "product"},
        )
        assert_matches_type(SetiRetrieveBlackBoxTestResultsResponse, seti, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_black_box_test_results(self, client: Telnyx) -> None:
        response = client.seti.with_raw_response.retrieve_black_box_test_results()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seti = response.parse()
        assert_matches_type(SetiRetrieveBlackBoxTestResultsResponse, seti, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_black_box_test_results(self, client: Telnyx) -> None:
        with client.seti.with_streaming_response.retrieve_black_box_test_results() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seti = response.parse()
            assert_matches_type(SetiRetrieveBlackBoxTestResultsResponse, seti, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSeti:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_black_box_test_results(self, async_client: AsyncTelnyx) -> None:
        seti = await async_client.seti.retrieve_black_box_test_results()
        assert_matches_type(SetiRetrieveBlackBoxTestResultsResponse, seti, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_black_box_test_results_with_all_params(self, async_client: AsyncTelnyx) -> None:
        seti = await async_client.seti.retrieve_black_box_test_results(
            filter={"product": "product"},
        )
        assert_matches_type(SetiRetrieveBlackBoxTestResultsResponse, seti, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_black_box_test_results(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.seti.with_raw_response.retrieve_black_box_test_results()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seti = await response.parse()
        assert_matches_type(SetiRetrieveBlackBoxTestResultsResponse, seti, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_black_box_test_results(self, async_client: AsyncTelnyx) -> None:
        async with async_client.seti.with_streaming_response.retrieve_black_box_test_results() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seti = await response.parse()
            assert_matches_type(SetiRetrieveBlackBoxTestResultsResponse, seti, path=["response"])

        assert cast(Any, response.is_closed) is True
