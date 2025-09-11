# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import RoomParticipantListResponse, RoomParticipantRetrieveResponse
from telnyx._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoomParticipants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        room_participant = client.room_participants.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(RoomParticipantRetrieveResponse, room_participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.room_participants.with_raw_response.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_participant = response.parse()
        assert_matches_type(RoomParticipantRetrieveResponse, room_participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.room_participants.with_streaming_response.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_participant = response.parse()
            assert_matches_type(RoomParticipantRetrieveResponse, room_participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_participant_id` but received ''"):
            client.room_participants.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        room_participant = client.room_participants.list()
        assert_matches_type(RoomParticipantListResponse, room_participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        room_participant = client.room_participants.list(
            filter={
                "context": "Alice",
                "date_joined_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_left_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_updated_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "session_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RoomParticipantListResponse, room_participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.room_participants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_participant = response.parse()
        assert_matches_type(RoomParticipantListResponse, room_participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.room_participants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_participant = response.parse()
            assert_matches_type(RoomParticipantListResponse, room_participant, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoomParticipants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        room_participant = await async_client.room_participants.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(RoomParticipantRetrieveResponse, room_participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.room_participants.with_raw_response.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_participant = await response.parse()
        assert_matches_type(RoomParticipantRetrieveResponse, room_participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.room_participants.with_streaming_response.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_participant = await response.parse()
            assert_matches_type(RoomParticipantRetrieveResponse, room_participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_participant_id` but received ''"):
            await async_client.room_participants.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        room_participant = await async_client.room_participants.list()
        assert_matches_type(RoomParticipantListResponse, room_participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        room_participant = await async_client.room_participants.list(
            filter={
                "context": "Alice",
                "date_joined_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_left_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_updated_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "session_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RoomParticipantListResponse, room_participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.room_participants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_participant = await response.parse()
        assert_matches_type(RoomParticipantListResponse, room_participant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.room_participants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_participant = await response.parse()
            assert_matches_type(RoomParticipantListResponse, room_participant, path=["response"])

        assert cast(Any, response.is_closed) is True
