# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.texml.accounts.calls import StreamStreamingSidJsonResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStreams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_streaming_sid_json(self, client: Telnyx) -> None:
        stream = client.texml.accounts.calls.streams.streaming_sid_json(
            streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
            call_sid="call_sid",
        )
        assert_matches_type(StreamStreamingSidJsonResponse, stream, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_streaming_sid_json_with_all_params(self, client: Telnyx) -> None:
        stream = client.texml.accounts.calls.streams.streaming_sid_json(
            streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
            call_sid="call_sid",
            status="stopped",
        )
        assert_matches_type(StreamStreamingSidJsonResponse, stream, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_streaming_sid_json(self, client: Telnyx) -> None:
        response = client.texml.accounts.calls.streams.with_raw_response.streaming_sid_json(
            streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
            call_sid="call_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(StreamStreamingSidJsonResponse, stream, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_streaming_sid_json(self, client: Telnyx) -> None:
        with client.texml.accounts.calls.streams.with_streaming_response.streaming_sid_json(
            streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
            call_sid="call_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(StreamStreamingSidJsonResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_streaming_sid_json(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.calls.streams.with_raw_response.streaming_sid_json(
                streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
                account_sid="",
                call_sid="call_sid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            client.texml.accounts.calls.streams.with_raw_response.streaming_sid_json(
                streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
                account_sid="account_sid",
                call_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `streaming_sid` but received ''"):
            client.texml.accounts.calls.streams.with_raw_response.streaming_sid_json(
                streaming_sid="",
                account_sid="account_sid",
                call_sid="call_sid",
            )


class TestAsyncStreams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_streaming_sid_json(self, async_client: AsyncTelnyx) -> None:
        stream = await async_client.texml.accounts.calls.streams.streaming_sid_json(
            streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
            call_sid="call_sid",
        )
        assert_matches_type(StreamStreamingSidJsonResponse, stream, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_streaming_sid_json_with_all_params(self, async_client: AsyncTelnyx) -> None:
        stream = await async_client.texml.accounts.calls.streams.streaming_sid_json(
            streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
            call_sid="call_sid",
            status="stopped",
        )
        assert_matches_type(StreamStreamingSidJsonResponse, stream, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_streaming_sid_json(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.calls.streams.with_raw_response.streaming_sid_json(
            streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
            call_sid="call_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(StreamStreamingSidJsonResponse, stream, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_streaming_sid_json(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.calls.streams.with_streaming_response.streaming_sid_json(
            streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
            call_sid="call_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(StreamStreamingSidJsonResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_streaming_sid_json(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.calls.streams.with_raw_response.streaming_sid_json(
                streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
                account_sid="",
                call_sid="call_sid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            await async_client.texml.accounts.calls.streams.with_raw_response.streaming_sid_json(
                streaming_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
                account_sid="account_sid",
                call_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `streaming_sid` but received ''"):
            await async_client.texml.accounts.calls.streams.with_raw_response.streaming_sid_json(
                streaming_sid="",
                account_sid="account_sid",
                call_sid="call_sid",
            )
