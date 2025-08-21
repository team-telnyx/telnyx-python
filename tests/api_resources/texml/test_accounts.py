# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.types.texml import (
    AccountRetrieveRecordingsJsonResponse,
    AccountRetrieveTranscriptionsJsonResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_recordings_json(self, client: Telnyx) -> None:
        account = client.texml.accounts.retrieve_recordings_json(
            account_sid="account_sid",
        )
        assert_matches_type(AccountRetrieveRecordingsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_recordings_json_with_all_params(self, client: Telnyx) -> None:
        account = client.texml.accounts.retrieve_recordings_json(
            account_sid="account_sid",
            date_created=parse_datetime("2019-12-27T18:11:19.117Z"),
            page=0,
            page_size=0,
        )
        assert_matches_type(AccountRetrieveRecordingsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_recordings_json(self, client: Telnyx) -> None:
        response = client.texml.accounts.with_raw_response.retrieve_recordings_json(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveRecordingsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_recordings_json(self, client: Telnyx) -> None:
        with client.texml.accounts.with_streaming_response.retrieve_recordings_json(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveRecordingsJsonResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_recordings_json(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.with_raw_response.retrieve_recordings_json(
                account_sid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_transcriptions_json(self, client: Telnyx) -> None:
        account = client.texml.accounts.retrieve_transcriptions_json(
            account_sid="account_sid",
        )
        assert_matches_type(AccountRetrieveTranscriptionsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_transcriptions_json_with_all_params(self, client: Telnyx) -> None:
        account = client.texml.accounts.retrieve_transcriptions_json(
            account_sid="account_sid",
            page_size=0,
            page_token="PageToken",
        )
        assert_matches_type(AccountRetrieveTranscriptionsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_transcriptions_json(self, client: Telnyx) -> None:
        response = client.texml.accounts.with_raw_response.retrieve_transcriptions_json(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveTranscriptionsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_transcriptions_json(self, client: Telnyx) -> None:
        with client.texml.accounts.with_streaming_response.retrieve_transcriptions_json(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveTranscriptionsJsonResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_transcriptions_json(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.with_raw_response.retrieve_transcriptions_json(
                account_sid="",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        account = await async_client.texml.accounts.retrieve_recordings_json(
            account_sid="account_sid",
        )
        assert_matches_type(AccountRetrieveRecordingsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_recordings_json_with_all_params(self, async_client: AsyncTelnyx) -> None:
        account = await async_client.texml.accounts.retrieve_recordings_json(
            account_sid="account_sid",
            date_created=parse_datetime("2019-12-27T18:11:19.117Z"),
            page=0,
            page_size=0,
        )
        assert_matches_type(AccountRetrieveRecordingsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.with_raw_response.retrieve_recordings_json(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveRecordingsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.with_streaming_response.retrieve_recordings_json(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveRecordingsJsonResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.with_raw_response.retrieve_recordings_json(
                account_sid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_transcriptions_json(self, async_client: AsyncTelnyx) -> None:
        account = await async_client.texml.accounts.retrieve_transcriptions_json(
            account_sid="account_sid",
        )
        assert_matches_type(AccountRetrieveTranscriptionsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_transcriptions_json_with_all_params(self, async_client: AsyncTelnyx) -> None:
        account = await async_client.texml.accounts.retrieve_transcriptions_json(
            account_sid="account_sid",
            page_size=0,
            page_token="PageToken",
        )
        assert_matches_type(AccountRetrieveTranscriptionsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_transcriptions_json(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.with_raw_response.retrieve_transcriptions_json(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveTranscriptionsJsonResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_transcriptions_json(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.with_streaming_response.retrieve_transcriptions_json(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveTranscriptionsJsonResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_transcriptions_json(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.with_raw_response.retrieve_transcriptions_json(
                account_sid="",
            )
