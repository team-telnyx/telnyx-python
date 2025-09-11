# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    RoomCompositionListResponse,
    RoomCompositionCreateResponse,
    RoomCompositionRetrieveResponse,
)
from telnyx._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoomCompositions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        room_composition = client.room_compositions.create()
        assert_matches_type(RoomCompositionCreateResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        room_composition = client.room_compositions.create(
            format="mp4",
            resolution="800x600",
            session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777b0",
            video_layout={
                "foo": {
                    "height": 360,
                    "max_columns": 3,
                    "max_rows": 3,
                    "video_sources": ["7b61621f-62e0-4aad-ab11-9fd19e272e73"],
                    "width": 480,
                    "x_pos": 100,
                    "y_pos": 100,
                    "z_pos": 1,
                }
            },
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(RoomCompositionCreateResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.room_compositions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_composition = response.parse()
        assert_matches_type(RoomCompositionCreateResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.room_compositions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_composition = response.parse()
            assert_matches_type(RoomCompositionCreateResponse, room_composition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        room_composition = client.room_compositions.retrieve(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        )
        assert_matches_type(RoomCompositionRetrieveResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.room_compositions.with_raw_response.retrieve(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_composition = response.parse()
        assert_matches_type(RoomCompositionRetrieveResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.room_compositions.with_streaming_response.retrieve(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_composition = response.parse()
            assert_matches_type(RoomCompositionRetrieveResponse, room_composition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_composition_id` but received ''"):
            client.room_compositions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        room_composition = client.room_compositions.list()
        assert_matches_type(RoomCompositionListResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        room_composition = client.room_compositions.list(
            filter={
                "date_created_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "session_id": "92e7d459-bcc5-4386-9f5f-6dd14a82588d",
                "status": "completed",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RoomCompositionListResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.room_compositions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_composition = response.parse()
        assert_matches_type(RoomCompositionListResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.room_compositions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_composition = response.parse()
            assert_matches_type(RoomCompositionListResponse, room_composition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        room_composition = client.room_compositions.delete(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        )
        assert room_composition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.room_compositions.with_raw_response.delete(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_composition = response.parse()
        assert room_composition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.room_compositions.with_streaming_response.delete(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_composition = response.parse()
            assert room_composition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_composition_id` but received ''"):
            client.room_compositions.with_raw_response.delete(
                "",
            )


class TestAsyncRoomCompositions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        room_composition = await async_client.room_compositions.create()
        assert_matches_type(RoomCompositionCreateResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        room_composition = await async_client.room_compositions.create(
            format="mp4",
            resolution="800x600",
            session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777b0",
            video_layout={
                "foo": {
                    "height": 360,
                    "max_columns": 3,
                    "max_rows": 3,
                    "video_sources": ["7b61621f-62e0-4aad-ab11-9fd19e272e73"],
                    "width": 480,
                    "x_pos": 100,
                    "y_pos": 100,
                    "z_pos": 1,
                }
            },
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(RoomCompositionCreateResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.room_compositions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_composition = await response.parse()
        assert_matches_type(RoomCompositionCreateResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.room_compositions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_composition = await response.parse()
            assert_matches_type(RoomCompositionCreateResponse, room_composition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        room_composition = await async_client.room_compositions.retrieve(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        )
        assert_matches_type(RoomCompositionRetrieveResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.room_compositions.with_raw_response.retrieve(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_composition = await response.parse()
        assert_matches_type(RoomCompositionRetrieveResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.room_compositions.with_streaming_response.retrieve(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_composition = await response.parse()
            assert_matches_type(RoomCompositionRetrieveResponse, room_composition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_composition_id` but received ''"):
            await async_client.room_compositions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        room_composition = await async_client.room_compositions.list()
        assert_matches_type(RoomCompositionListResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        room_composition = await async_client.room_compositions.list(
            filter={
                "date_created_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "session_id": "92e7d459-bcc5-4386-9f5f-6dd14a82588d",
                "status": "completed",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RoomCompositionListResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.room_compositions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_composition = await response.parse()
        assert_matches_type(RoomCompositionListResponse, room_composition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.room_compositions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_composition = await response.parse()
            assert_matches_type(RoomCompositionListResponse, room_composition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        room_composition = await async_client.room_compositions.delete(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        )
        assert room_composition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.room_compositions.with_raw_response.delete(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room_composition = await response.parse()
        assert room_composition is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.room_compositions.with_streaming_response.delete(
            "5219b3af-87c6-4c08-9b58-5a533d893e21",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room_composition = await response.parse()
            assert room_composition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_composition_id` but received ''"):
            await async_client.room_compositions.with_raw_response.delete(
                "",
            )
