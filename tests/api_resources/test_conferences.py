# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    ConferenceListResponse,
    ConferenceCreateResponse,
    ConferenceRetrieveResponse,
    ConferenceListParticipantsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        conference = client.conferences.create(
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            name="Business",
        )
        assert_matches_type(ConferenceCreateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        conference = client.conferences.create(
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            name="Business",
            beep_enabled="always",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            comfort_noise=False,
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            duration_minutes=5,
            hold_audio_url="http://www.example.com/audio.wav",
            hold_media_name="my_media_uploaded_to_media_storage_api",
            max_participants=250,
            start_conference_on_create=False,
        )
        assert_matches_type(ConferenceCreateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.conferences.with_raw_response.create(
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            name="Business",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = response.parse()
        assert_matches_type(ConferenceCreateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.conferences.with_streaming_response.create(
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            name="Business",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = response.parse()
            assert_matches_type(ConferenceCreateResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        conference = client.conferences.retrieve(
            "id",
        )
        assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.conferences.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = response.parse()
        assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.conferences.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = response.parse()
            assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conferences.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        conference = client.conferences.list()
        assert_matches_type(ConferenceListResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        conference = client.conferences.list(
            filter={
                "application_name": {"contains": "contains"},
                "application_session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "connection_id": "connection_id",
                "failed": False,
                "from": "+12025550142",
                "leg_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "occurred_at": {
                    "eq": "2019-03-29T11:10:00Z",
                    "gt": "2019-03-29T11:10:00Z",
                    "gte": "2019-03-29T11:10:00Z",
                    "lt": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "outbound_outbound_voice_profile_id": "outbound.outbound_voice_profile_id",
                "product": "texml",
                "status": "init",
                "to": "+12025550142",
                "type": "webhook",
            },
            page={
                "after": "after",
                "before": "before",
                "limit": 1,
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ConferenceListResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.conferences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = response.parse()
        assert_matches_type(ConferenceListResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.conferences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = response.parse()
            assert_matches_type(ConferenceListResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_participants(self, client: Telnyx) -> None:
        conference = client.conferences.list_participants(
            conference_id="conference_id",
        )
        assert_matches_type(ConferenceListParticipantsResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_participants_with_all_params(self, client: Telnyx) -> None:
        conference = client.conferences.list_participants(
            conference_id="conference_id",
            filter={
                "muted": True,
                "on_hold": True,
                "whispering": True,
            },
            page={
                "after": "after",
                "before": "before",
                "limit": 1,
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ConferenceListParticipantsResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_participants(self, client: Telnyx) -> None:
        response = client.conferences.with_raw_response.list_participants(
            conference_id="conference_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = response.parse()
        assert_matches_type(ConferenceListParticipantsResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_participants(self, client: Telnyx) -> None:
        with client.conferences.with_streaming_response.list_participants(
            conference_id="conference_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = response.parse()
            assert_matches_type(ConferenceListParticipantsResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_participants(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_id` but received ''"):
            client.conferences.with_raw_response.list_participants(
                conference_id="",
            )


class TestAsyncConferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.conferences.create(
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            name="Business",
        )
        assert_matches_type(ConferenceCreateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.conferences.create(
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            name="Business",
            beep_enabled="always",
            client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
            comfort_noise=False,
            command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
            duration_minutes=5,
            hold_audio_url="http://www.example.com/audio.wav",
            hold_media_name="my_media_uploaded_to_media_storage_api",
            max_participants=250,
            start_conference_on_create=False,
        )
        assert_matches_type(ConferenceCreateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.with_raw_response.create(
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            name="Business",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = await response.parse()
        assert_matches_type(ConferenceCreateResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.with_streaming_response.create(
            call_control_id="v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg",
            name="Business",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = await response.parse()
            assert_matches_type(ConferenceCreateResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.conferences.retrieve(
            "id",
        )
        assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = await response.parse()
        assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = await response.parse()
            assert_matches_type(ConferenceRetrieveResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conferences.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.conferences.list()
        assert_matches_type(ConferenceListResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.conferences.list(
            filter={
                "application_name": {"contains": "contains"},
                "application_session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "connection_id": "connection_id",
                "failed": False,
                "from": "+12025550142",
                "leg_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "occurred_at": {
                    "eq": "2019-03-29T11:10:00Z",
                    "gt": "2019-03-29T11:10:00Z",
                    "gte": "2019-03-29T11:10:00Z",
                    "lt": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "outbound_outbound_voice_profile_id": "outbound.outbound_voice_profile_id",
                "product": "texml",
                "status": "init",
                "to": "+12025550142",
                "type": "webhook",
            },
            page={
                "after": "after",
                "before": "before",
                "limit": 1,
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ConferenceListResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = await response.parse()
        assert_matches_type(ConferenceListResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = await response.parse()
            assert_matches_type(ConferenceListResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_participants(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.conferences.list_participants(
            conference_id="conference_id",
        )
        assert_matches_type(ConferenceListParticipantsResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_participants_with_all_params(self, async_client: AsyncTelnyx) -> None:
        conference = await async_client.conferences.list_participants(
            conference_id="conference_id",
            filter={
                "muted": True,
                "on_hold": True,
                "whispering": True,
            },
            page={
                "after": "after",
                "before": "before",
                "limit": 1,
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ConferenceListParticipantsResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_participants(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.conferences.with_raw_response.list_participants(
            conference_id="conference_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conference = await response.parse()
        assert_matches_type(ConferenceListParticipantsResponse, conference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_participants(self, async_client: AsyncTelnyx) -> None:
        async with async_client.conferences.with_streaming_response.list_participants(
            conference_id="conference_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conference = await response.parse()
            assert_matches_type(ConferenceListParticipantsResponse, conference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_participants(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conference_id` but received ''"):
            await async_client.conferences.with_raw_response.list_participants(
                conference_id="",
            )
