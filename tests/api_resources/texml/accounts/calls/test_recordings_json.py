# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.texml.accounts.calls import (
    RecordingsJsonRecordingsJsonResponse,
    RecordingsJsonRetrieveRecordingsJsonResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecordingsJson:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_recordings_json(self, client: Telnyx) -> None:
        recordings_json = client.texml.accounts.calls.recordings_json.recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(RecordingsJsonRecordingsJsonResponse, recordings_json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_recordings_json_with_all_params(self, client: Telnyx) -> None:
        recordings_json = client.texml.accounts.calls.recordings_json.recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
            play_beep=False,
            recording_channels="single",
            recording_status_callback="http://webhook.com/callback",
            recording_status_callback_event="in-progress completed absent",
            recording_status_callback_method="GET",
            recording_track="inbound",
            send_recording_url=False,
        )
        assert_matches_type(RecordingsJsonRecordingsJsonResponse, recordings_json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_recordings_json(self, client: Telnyx) -> None:
        response = client.texml.accounts.calls.recordings_json.with_raw_response.recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recordings_json = response.parse()
        assert_matches_type(RecordingsJsonRecordingsJsonResponse, recordings_json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_recordings_json(self, client: Telnyx) -> None:
        with client.texml.accounts.calls.recordings_json.with_streaming_response.recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recordings_json = response.parse()
            assert_matches_type(RecordingsJsonRecordingsJsonResponse, recordings_json, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_recordings_json(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.calls.recordings_json.with_raw_response.recordings_json(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            client.texml.accounts.calls.recordings_json.with_raw_response.recordings_json(
                call_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_recordings_json(self, client: Telnyx) -> None:
        recordings_json = client.texml.accounts.calls.recordings_json.retrieve_recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(RecordingsJsonRetrieveRecordingsJsonResponse, recordings_json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_recordings_json(self, client: Telnyx) -> None:
        response = client.texml.accounts.calls.recordings_json.with_raw_response.retrieve_recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recordings_json = response.parse()
        assert_matches_type(RecordingsJsonRetrieveRecordingsJsonResponse, recordings_json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_recordings_json(self, client: Telnyx) -> None:
        with client.texml.accounts.calls.recordings_json.with_streaming_response.retrieve_recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recordings_json = response.parse()
            assert_matches_type(RecordingsJsonRetrieveRecordingsJsonResponse, recordings_json, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_recordings_json(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.calls.recordings_json.with_raw_response.retrieve_recordings_json(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            client.texml.accounts.calls.recordings_json.with_raw_response.retrieve_recordings_json(
                call_sid="",
                account_sid="account_sid",
            )


class TestAsyncRecordingsJson:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_recordings_json(self, async_client: AsyncTelnyx) -> None:
        recordings_json = await async_client.texml.accounts.calls.recordings_json.recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(RecordingsJsonRecordingsJsonResponse, recordings_json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_recordings_json_with_all_params(self, async_client: AsyncTelnyx) -> None:
        recordings_json = await async_client.texml.accounts.calls.recordings_json.recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
            play_beep=False,
            recording_channels="single",
            recording_status_callback="http://webhook.com/callback",
            recording_status_callback_event="in-progress completed absent",
            recording_status_callback_method="GET",
            recording_track="inbound",
            send_recording_url=False,
        )
        assert_matches_type(RecordingsJsonRecordingsJsonResponse, recordings_json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_recordings_json(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.calls.recordings_json.with_raw_response.recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recordings_json = await response.parse()
        assert_matches_type(RecordingsJsonRecordingsJsonResponse, recordings_json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_recordings_json(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.calls.recordings_json.with_streaming_response.recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recordings_json = await response.parse()
            assert_matches_type(RecordingsJsonRecordingsJsonResponse, recordings_json, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_recordings_json(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.calls.recordings_json.with_raw_response.recordings_json(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            await async_client.texml.accounts.calls.recordings_json.with_raw_response.recordings_json(
                call_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        recordings_json = await async_client.texml.accounts.calls.recordings_json.retrieve_recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(RecordingsJsonRetrieveRecordingsJsonResponse, recordings_json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.calls.recordings_json.with_raw_response.retrieve_recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recordings_json = await response.parse()
        assert_matches_type(RecordingsJsonRetrieveRecordingsJsonResponse, recordings_json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.calls.recordings_json.with_streaming_response.retrieve_recordings_json(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recordings_json = await response.parse()
            assert_matches_type(RecordingsJsonRetrieveRecordingsJsonResponse, recordings_json, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.calls.recordings_json.with_raw_response.retrieve_recordings_json(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            await async_client.texml.accounts.calls.recordings_json.with_raw_response.retrieve_recordings_json(
                call_sid="",
                account_sid="account_sid",
            )
