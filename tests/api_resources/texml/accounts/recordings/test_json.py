# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.texml import TexmlGetCallRecordingResponseBody

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJson:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_recording_sid_json(self, client: Telnyx) -> None:
        json = client.texml.accounts.recordings.json.delete_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        )
        assert json is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_recording_sid_json(self, client: Telnyx) -> None:
        response = client.texml.accounts.recordings.json.with_raw_response.delete_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        json = response.parse()
        assert json is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_recording_sid_json(self, client: Telnyx) -> None:
        with client.texml.accounts.recordings.json.with_streaming_response.delete_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            json = response.parse()
            assert json is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_recording_sid_json(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.recordings.json.with_raw_response.delete_recording_sid_json(
                recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_sid` but received ''"):
            client.texml.accounts.recordings.json.with_raw_response.delete_recording_sid_json(
                recording_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_recording_sid_json(self, client: Telnyx) -> None:
        json = client.texml.accounts.recordings.json.retrieve_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        )
        assert_matches_type(TexmlGetCallRecordingResponseBody, json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_recording_sid_json(self, client: Telnyx) -> None:
        response = client.texml.accounts.recordings.json.with_raw_response.retrieve_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        json = response.parse()
        assert_matches_type(TexmlGetCallRecordingResponseBody, json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_recording_sid_json(self, client: Telnyx) -> None:
        with client.texml.accounts.recordings.json.with_streaming_response.retrieve_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            json = response.parse()
            assert_matches_type(TexmlGetCallRecordingResponseBody, json, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_recording_sid_json(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.recordings.json.with_raw_response.retrieve_recording_sid_json(
                recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_sid` but received ''"):
            client.texml.accounts.recordings.json.with_raw_response.retrieve_recording_sid_json(
                recording_sid="",
                account_sid="account_sid",
            )


class TestAsyncJson:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_recording_sid_json(self, async_client: AsyncTelnyx) -> None:
        json = await async_client.texml.accounts.recordings.json.delete_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        )
        assert json is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_recording_sid_json(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.recordings.json.with_raw_response.delete_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        json = await response.parse()
        assert json is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_recording_sid_json(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.recordings.json.with_streaming_response.delete_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            json = await response.parse()
            assert json is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_recording_sid_json(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.recordings.json.with_raw_response.delete_recording_sid_json(
                recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_sid` but received ''"):
            await async_client.texml.accounts.recordings.json.with_raw_response.delete_recording_sid_json(
                recording_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_recording_sid_json(self, async_client: AsyncTelnyx) -> None:
        json = await async_client.texml.accounts.recordings.json.retrieve_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        )
        assert_matches_type(TexmlGetCallRecordingResponseBody, json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_recording_sid_json(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.recordings.json.with_raw_response.retrieve_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        json = await response.parse()
        assert_matches_type(TexmlGetCallRecordingResponseBody, json, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_recording_sid_json(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.recordings.json.with_streaming_response.retrieve_recording_sid_json(
            recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            json = await response.parse()
            assert_matches_type(TexmlGetCallRecordingResponseBody, json, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_recording_sid_json(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.recordings.json.with_raw_response.retrieve_recording_sid_json(
                recording_sid="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_sid` but received ''"):
            await async_client.texml.accounts.recordings.json.with_raw_response.retrieve_recording_sid_json(
                recording_sid="",
                account_sid="account_sid",
            )
