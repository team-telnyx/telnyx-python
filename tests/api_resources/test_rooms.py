# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    RoomListResponse,
    RoomCreateResponse,
    RoomUpdateResponse,
    RoomRetrieveResponse,
)
from telnyx._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRooms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        room = client.rooms.create()
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        room = client.rooms.create(
            enable_recording=True,
            max_participants=10,
            unique_name="My room",
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.rooms.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = response.parse()
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.rooms.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = response.parse()
            assert_matches_type(RoomCreateResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        room = client.rooms.retrieve(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(RoomRetrieveResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        room = client.rooms.retrieve(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            include_sessions=True,
        )
        assert_matches_type(RoomRetrieveResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.rooms.with_raw_response.retrieve(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = response.parse()
        assert_matches_type(RoomRetrieveResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.rooms.with_streaming_response.retrieve(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = response.parse()
            assert_matches_type(RoomRetrieveResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            client.rooms.with_raw_response.retrieve(
                room_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        room = client.rooms.update(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(RoomUpdateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        room = client.rooms.update(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            enable_recording=True,
            max_participants=10,
            unique_name="My room",
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(RoomUpdateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.rooms.with_raw_response.update(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = response.parse()
        assert_matches_type(RoomUpdateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.rooms.with_streaming_response.update(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = response.parse()
            assert_matches_type(RoomUpdateResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            client.rooms.with_raw_response.update(
                room_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        room = client.rooms.list()
        assert_matches_type(RoomListResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        room = client.rooms.list(
            filter={
                "date_created_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_updated_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "unique_name": "my_video_room",
            },
            include_sessions=True,
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RoomListResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.rooms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = response.parse()
        assert_matches_type(RoomListResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.rooms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = response.parse()
            assert_matches_type(RoomListResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        room = client.rooms.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert room is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.rooms.with_raw_response.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = response.parse()
        assert room is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.rooms.with_streaming_response.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = response.parse()
            assert room is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            client.rooms.with_raw_response.delete(
                "",
            )


class TestAsyncRooms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        room = await async_client.rooms.create()
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        room = await async_client.rooms.create(
            enable_recording=True,
            max_participants=10,
            unique_name="My room",
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = await response.parse()
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = await response.parse()
            assert_matches_type(RoomCreateResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        room = await async_client.rooms.retrieve(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(RoomRetrieveResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        room = await async_client.rooms.retrieve(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            include_sessions=True,
        )
        assert_matches_type(RoomRetrieveResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.with_raw_response.retrieve(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = await response.parse()
        assert_matches_type(RoomRetrieveResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.with_streaming_response.retrieve(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = await response.parse()
            assert_matches_type(RoomRetrieveResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            await async_client.rooms.with_raw_response.retrieve(
                room_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        room = await async_client.rooms.update(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(RoomUpdateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        room = await async_client.rooms.update(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            enable_recording=True,
            max_participants=10,
            unique_name="My room",
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(RoomUpdateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.with_raw_response.update(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = await response.parse()
        assert_matches_type(RoomUpdateResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.with_streaming_response.update(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = await response.parse()
            assert_matches_type(RoomUpdateResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            await async_client.rooms.with_raw_response.update(
                room_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        room = await async_client.rooms.list()
        assert_matches_type(RoomListResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        room = await async_client.rooms.list(
            filter={
                "date_created_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_updated_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "unique_name": "my_video_room",
            },
            include_sessions=True,
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RoomListResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = await response.parse()
        assert_matches_type(RoomListResponse, room, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = await response.parse()
            assert_matches_type(RoomListResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        room = await async_client.rooms.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert room is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.with_raw_response.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = await response.parse()
        assert room is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.with_streaming_response.delete(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = await response.parse()
            assert room is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            await async_client.rooms.with_raw_response.delete(
                "",
            )
