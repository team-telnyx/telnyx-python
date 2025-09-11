# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.texml.accounts.calls import SiprecSiprecSidJsonResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSiprec:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_siprec_sid_json(self, client: Telnyx) -> None:
        siprec = client.texml.accounts.calls.siprec.siprec_sid_json(
            siprec_sid="siprec_sid",
            account_sid="account_sid",
            call_sid="call_sid",
        )
        assert_matches_type(SiprecSiprecSidJsonResponse, siprec, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_siprec_sid_json_with_all_params(self, client: Telnyx) -> None:
        siprec = client.texml.accounts.calls.siprec.siprec_sid_json(
            siprec_sid="siprec_sid",
            account_sid="account_sid",
            call_sid="call_sid",
            status="stopped",
        )
        assert_matches_type(SiprecSiprecSidJsonResponse, siprec, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_siprec_sid_json(self, client: Telnyx) -> None:
        response = client.texml.accounts.calls.siprec.with_raw_response.siprec_sid_json(
            siprec_sid="siprec_sid",
            account_sid="account_sid",
            call_sid="call_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siprec = response.parse()
        assert_matches_type(SiprecSiprecSidJsonResponse, siprec, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_siprec_sid_json(self, client: Telnyx) -> None:
        with client.texml.accounts.calls.siprec.with_streaming_response.siprec_sid_json(
            siprec_sid="siprec_sid",
            account_sid="account_sid",
            call_sid="call_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siprec = response.parse()
            assert_matches_type(SiprecSiprecSidJsonResponse, siprec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_siprec_sid_json(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.calls.siprec.with_raw_response.siprec_sid_json(
                siprec_sid="siprec_sid",
                account_sid="",
                call_sid="call_sid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            client.texml.accounts.calls.siprec.with_raw_response.siprec_sid_json(
                siprec_sid="siprec_sid",
                account_sid="account_sid",
                call_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `siprec_sid` but received ''"):
            client.texml.accounts.calls.siprec.with_raw_response.siprec_sid_json(
                siprec_sid="",
                account_sid="account_sid",
                call_sid="call_sid",
            )


class TestAsyncSiprec:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_siprec_sid_json(self, async_client: AsyncTelnyx) -> None:
        siprec = await async_client.texml.accounts.calls.siprec.siprec_sid_json(
            siprec_sid="siprec_sid",
            account_sid="account_sid",
            call_sid="call_sid",
        )
        assert_matches_type(SiprecSiprecSidJsonResponse, siprec, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_siprec_sid_json_with_all_params(self, async_client: AsyncTelnyx) -> None:
        siprec = await async_client.texml.accounts.calls.siprec.siprec_sid_json(
            siprec_sid="siprec_sid",
            account_sid="account_sid",
            call_sid="call_sid",
            status="stopped",
        )
        assert_matches_type(SiprecSiprecSidJsonResponse, siprec, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_siprec_sid_json(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.calls.siprec.with_raw_response.siprec_sid_json(
            siprec_sid="siprec_sid",
            account_sid="account_sid",
            call_sid="call_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siprec = await response.parse()
        assert_matches_type(SiprecSiprecSidJsonResponse, siprec, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_siprec_sid_json(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.calls.siprec.with_streaming_response.siprec_sid_json(
            siprec_sid="siprec_sid",
            account_sid="account_sid",
            call_sid="call_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siprec = await response.parse()
            assert_matches_type(SiprecSiprecSidJsonResponse, siprec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_siprec_sid_json(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.calls.siprec.with_raw_response.siprec_sid_json(
                siprec_sid="siprec_sid",
                account_sid="",
                call_sid="call_sid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            await async_client.texml.accounts.calls.siprec.with_raw_response.siprec_sid_json(
                siprec_sid="siprec_sid",
                account_sid="account_sid",
                call_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `siprec_sid` but received ''"):
            await async_client.texml.accounts.calls.siprec.with_raw_response.siprec_sid_json(
                siprec_sid="",
                account_sid="account_sid",
                call_sid="call_sid",
            )
