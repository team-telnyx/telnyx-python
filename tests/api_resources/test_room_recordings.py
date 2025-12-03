# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    RoomRecordingListResponse,
    RoomRecordingRetrieveResponse,
    RoomRecordingDeleteBulkResponse,
)
from telnyx._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoomRecordings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        room_recording = client.room_recordings.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(RoomRecordingRetrieveResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.room_recordings.with_raw_response.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_recording = response.parse()
        assert_matches_type(RoomRecordingRetrieveResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.room_recordings.with_streaming_response.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_recording = response.parse()
            assert_matches_type(RoomRecordingRetrieveResponse, room_recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_recording_id` but received ''"):
            client.room_recordings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        room_recording = client.room_recordings.list()
        assert_matches_type(RoomRecordingListResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        room_recording = client.room_recordings.list(
            filter={
                "date_ended_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_started_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "duration_secs": 20,
                "participant_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "room_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "session_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "status": "completed",
                "type": "audio",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RoomRecordingListResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.room_recordings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_recording = response.parse()
        assert_matches_type(RoomRecordingListResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.room_recordings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_recording = response.parse()
            assert_matches_type(RoomRecordingListResponse, room_recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        room_recording = client.room_recordings.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert room_recording is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.room_recordings.with_raw_response.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_recording = response.parse()
        assert room_recording is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.room_recordings.with_streaming_response.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_recording = response.parse()
            assert room_recording is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_recording_id` but received ''"):
            client.room_recordings.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_bulk(self, client: Telnyx) -> None:
        room_recording = client.room_recordings.delete_bulk()
        assert_matches_type(RoomRecordingDeleteBulkResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_bulk_with_all_params(self, client: Telnyx) -> None:
        room_recording = client.room_recordings.delete_bulk(
            filter={
                "date_ended_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_started_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "duration_secs": 20,
                "participant_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "room_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "session_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "status": "completed",
                "type": "audio",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RoomRecordingDeleteBulkResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_bulk(self, client: Telnyx) -> None:
        response = client.room_recordings.with_raw_response.delete_bulk()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_recording = response.parse()
        assert_matches_type(RoomRecordingDeleteBulkResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_bulk(self, client: Telnyx) -> None:
        with client.room_recordings.with_streaming_response.delete_bulk() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_recording = response.parse()
            assert_matches_type(RoomRecordingDeleteBulkResponse, room_recording, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoomRecordings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        room_recording = await async_client.room_recordings.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(RoomRecordingRetrieveResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.room_recordings.with_raw_response.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_recording = await response.parse()
        assert_matches_type(RoomRecordingRetrieveResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.room_recordings.with_streaming_response.retrieve(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_recording = await response.parse()
            assert_matches_type(RoomRecordingRetrieveResponse, room_recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_recording_id` but received ''"):
            await async_client.room_recordings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        room_recording = await async_client.room_recordings.list()
        assert_matches_type(RoomRecordingListResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        room_recording = await async_client.room_recordings.list(
            filter={
                "date_ended_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_started_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "duration_secs": 20,
                "participant_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "room_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "session_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "status": "completed",
                "type": "audio",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RoomRecordingListResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.room_recordings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_recording = await response.parse()
        assert_matches_type(RoomRecordingListResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.room_recordings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_recording = await response.parse()
            assert_matches_type(RoomRecordingListResponse, room_recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        room_recording = await async_client.room_recordings.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert room_recording is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.room_recordings.with_raw_response.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_recording = await response.parse()
        assert room_recording is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.room_recordings.with_streaming_response.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_recording = await response.parse()
            assert room_recording is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_recording_id` but received ''"):
            await async_client.room_recordings.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_bulk(self, async_client: AsyncTelnyx) -> None:
        room_recording = await async_client.room_recordings.delete_bulk()
        assert_matches_type(RoomRecordingDeleteBulkResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_bulk_with_all_params(self, async_client: AsyncTelnyx) -> None:
        room_recording = await async_client.room_recordings.delete_bulk(
            filter={
                "date_ended_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_started_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "duration_secs": 20,
                "participant_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "room_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "session_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
                "status": "completed",
                "type": "audio",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RoomRecordingDeleteBulkResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_bulk(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.room_recordings.with_raw_response.delete_bulk()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_recording = await response.parse()
        assert_matches_type(RoomRecordingDeleteBulkResponse, room_recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_bulk(self, async_client: AsyncTelnyx) -> None:
        async with async_client.room_recordings.with_streaming_response.delete_bulk() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_recording = await response.parse()
            assert_matches_type(RoomRecordingDeleteBulkResponse, room_recording, path=["response"])

        assert cast(Any, response.is_closed) is True
