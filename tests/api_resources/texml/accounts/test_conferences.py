# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.texml.accounts import (
    ConferenceUpdateResponse,
    ConferenceRetrieveResponse,
    ConferenceRetrieveRecordingsResponse,
    ConferenceRetrieveConferencesResponse,
    ConferenceRetrieveRecordingsJsonResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        conference = client.texml.accounts.conferences.retrieve(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.texml.accounts.conferences.with_raw_response.retrieve(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = response.parse()
        assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.texml.accounts.conferences.with_streaming_response.retrieve(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = response.parse()
            assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.conferences.with_raw_response.retrieve(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            client.texml.accounts.conferences.with_raw_response.retrieve(
                conference_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        conference = client.texml.accounts.conferences.update(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ConferenceUpdateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        conference = client.texml.accounts.conferences.update(
            conference_sid="conference_sid",
            account_sid="account_sid",
            announce_method="GET",
            announce_url="https://www.example.com/announce.xml",
            status="completed",
        )
        assert_matches_type(ConferenceUpdateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.texml.accounts.conferences.with_raw_response.update(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = response.parse()
        assert_matches_type(ConferenceUpdateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.texml.accounts.conferences.with_streaming_response.update(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = response.parse()
            assert_matches_type(ConferenceUpdateResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.conferences.with_raw_response.update(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            client.texml.accounts.conferences.with_raw_response.update(
                conference_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_conferences(self, client: Telnyx) -> None:
        conference = client.texml.accounts.conferences.retrieve_conferences(
            account_sid="account_sid",
        )
        assert_matches_type(ConferenceRetrieveConferencesResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_conferences_with_all_params(self, client: Telnyx) -> None:
        conference = client.texml.accounts.conferences.retrieve_conferences(
            account_sid="account_sid",
            date_created="DateCreated",
            date_updated="DateUpdated",
            friendly_name="FriendlyName",
            page=0,
            page_size=0,
            page_token="PageToken",
            status="init",
        )
        assert_matches_type(ConferenceRetrieveConferencesResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_conferences(self, client: Telnyx) -> None:
        response = client.texml.accounts.conferences.with_raw_response.retrieve_conferences(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = response.parse()
        assert_matches_type(ConferenceRetrieveConferencesResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_conferences(self, client: Telnyx) -> None:
        with client.texml.accounts.conferences.with_streaming_response.retrieve_conferences(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = response.parse()
            assert_matches_type(ConferenceRetrieveConferencesResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_conferences(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.conferences.with_raw_response.retrieve_conferences(
                account_sid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_recordings(self, client: Telnyx) -> None:
        conference = client.texml.accounts.conferences.retrieve_recordings(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ConferenceRetrieveRecordingsResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_recordings(self, client: Telnyx) -> None:
        response = client.texml.accounts.conferences.with_raw_response.retrieve_recordings(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = response.parse()
        assert_matches_type(ConferenceRetrieveRecordingsResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_recordings(self, client: Telnyx) -> None:
        with client.texml.accounts.conferences.with_streaming_response.retrieve_recordings(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = response.parse()
            assert_matches_type(ConferenceRetrieveRecordingsResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_recordings(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.conferences.with_raw_response.retrieve_recordings(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            client.texml.accounts.conferences.with_raw_response.retrieve_recordings(
                conference_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_recordings_json(self, client: Telnyx) -> None:
        conference = client.texml.accounts.conferences.retrieve_recordings_json(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ConferenceRetrieveRecordingsJsonResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_recordings_json(self, client: Telnyx) -> None:
        response = client.texml.accounts.conferences.with_raw_response.retrieve_recordings_json(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = response.parse()
        assert_matches_type(ConferenceRetrieveRecordingsJsonResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_recordings_json(self, client: Telnyx) -> None:
        with client.texml.accounts.conferences.with_streaming_response.retrieve_recordings_json(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = response.parse()
            assert_matches_type(ConferenceRetrieveRecordingsJsonResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_recordings_json(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.conferences.with_raw_response.retrieve_recordings_json(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            client.texml.accounts.conferences.with_raw_response.retrieve_recordings_json(
                conference_sid="",
                account_sid="account_sid",
            )


class TestAsyncConferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.texml.accounts.conferences.retrieve(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.conferences.with_raw_response.retrieve(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = await response.parse()
        assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.conferences.with_streaming_response.retrieve(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = await response.parse()
            assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.conferences.with_raw_response.retrieve(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            await async_client.texml.accounts.conferences.with_raw_response.retrieve(
                conference_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.texml.accounts.conferences.update(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ConferenceUpdateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.texml.accounts.conferences.update(
            conference_sid="conference_sid",
            account_sid="account_sid",
            announce_method="GET",
            announce_url="https://www.example.com/announce.xml",
            status="completed",
        )
        assert_matches_type(ConferenceUpdateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.conferences.with_raw_response.update(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = await response.parse()
        assert_matches_type(ConferenceUpdateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.conferences.with_streaming_response.update(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = await response.parse()
            assert_matches_type(ConferenceUpdateResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.conferences.with_raw_response.update(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            await async_client.texml.accounts.conferences.with_raw_response.update(
                conference_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_conferences(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.texml.accounts.conferences.retrieve_conferences(
            account_sid="account_sid",
        )
        assert_matches_type(ConferenceRetrieveConferencesResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_conferences_with_all_params(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.texml.accounts.conferences.retrieve_conferences(
            account_sid="account_sid",
            date_created="DateCreated",
            date_updated="DateUpdated",
            friendly_name="FriendlyName",
            page=0,
            page_size=0,
            page_token="PageToken",
            status="init",
        )
        assert_matches_type(ConferenceRetrieveConferencesResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_conferences(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.conferences.with_raw_response.retrieve_conferences(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = await response.parse()
        assert_matches_type(ConferenceRetrieveConferencesResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_conferences(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.conferences.with_streaming_response.retrieve_conferences(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = await response.parse()
            assert_matches_type(ConferenceRetrieveConferencesResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_conferences(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.conferences.with_raw_response.retrieve_conferences(
                account_sid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_recordings(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.texml.accounts.conferences.retrieve_recordings(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ConferenceRetrieveRecordingsResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_recordings(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.conferences.with_raw_response.retrieve_recordings(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = await response.parse()
        assert_matches_type(ConferenceRetrieveRecordingsResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_recordings(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.conferences.with_streaming_response.retrieve_recordings(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = await response.parse()
            assert_matches_type(ConferenceRetrieveRecordingsResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_recordings(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.conferences.with_raw_response.retrieve_recordings(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            await async_client.texml.accounts.conferences.with_raw_response.retrieve_recordings(
                conference_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.texml.accounts.conferences.retrieve_recordings_json(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )
        assert_matches_type(ConferenceRetrieveRecordingsJsonResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.conferences.with_raw_response.retrieve_recordings_json(
            conference_sid="conference_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = await response.parse()
        assert_matches_type(ConferenceRetrieveRecordingsJsonResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.conferences.with_streaming_response.retrieve_recordings_json(
            conference_sid="conference_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = await response.parse()
            assert_matches_type(ConferenceRetrieveRecordingsJsonResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_recordings_json(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.conferences.with_raw_response.retrieve_recordings_json(
                conference_sid="conference_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_sid` but received ''"):
            await async_client.texml.accounts.conferences.with_raw_response.retrieve_recordings_json(
                conference_sid="",
                account_sid="account_sid",
            )
