# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_date
from telnyx.types.rooms import (
    SessionList0Response,
    SessionList1Response,
    SessionRetrieveResponse,
    SessionRetrieveParticipantsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        session = client.rooms.sessions.retrieve(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        session = client.rooms.sessions.retrieve(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            include_participants=True,
        )
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.rooms.sessions.with_raw_response.retrieve(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.rooms.sessions.with_streaming_response.retrieve(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionRetrieveResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            client.rooms.sessions.with_raw_response.retrieve(
                room_session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_0(self, client: Telnyx) -> None:
        session = client.rooms.sessions.list_0()
        assert_matches_type(SessionList0Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_0_with_all_params(self, client: Telnyx) -> None:
        session = client.rooms.sessions.list_0(
            filter={
                "active": True,
                "date_created_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_ended_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_updated_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "room_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            },
            include_participants=True,
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(SessionList0Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_0(self, client: Telnyx) -> None:
        response = client.rooms.sessions.with_raw_response.list_0()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionList0Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_0(self, client: Telnyx) -> None:
        with client.rooms.sessions.with_streaming_response.list_0() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionList0Response, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_1(self, client: Telnyx) -> None:
        session = client.rooms.sessions.list_1(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(SessionList1Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_1_with_all_params(self, client: Telnyx) -> None:
        session = client.rooms.sessions.list_1(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            filter={
                "active": True,
                "date_created_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_ended_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_updated_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
            },
            include_participants=True,
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(SessionList1Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_1(self, client: Telnyx) -> None:
        response = client.rooms.sessions.with_raw_response.list_1(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionList1Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_1(self, client: Telnyx) -> None:
        with client.rooms.sessions.with_streaming_response.list_1(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionList1Response, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_1(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            client.rooms.sessions.with_raw_response.list_1(
                room_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_participants(self, client: Telnyx) -> None:
        session = client.rooms.sessions.retrieve_participants(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(SessionRetrieveParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_participants_with_all_params(self, client: Telnyx) -> None:
        session = client.rooms.sessions.retrieve_participants(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
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
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(SessionRetrieveParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_participants(self, client: Telnyx) -> None:
        response = client.rooms.sessions.with_raw_response.retrieve_participants(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionRetrieveParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_participants(self, client: Telnyx) -> None:
        with client.rooms.sessions.with_streaming_response.retrieve_participants(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionRetrieveParticipantsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_participants(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            client.rooms.sessions.with_raw_response.retrieve_participants(
                room_session_id="",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        session = await async_client.rooms.sessions.retrieve(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        session = await async_client.rooms.sessions.retrieve(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            include_participants=True,
        )
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.sessions.with_raw_response.retrieve(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.sessions.with_streaming_response.retrieve(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionRetrieveResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            await async_client.rooms.sessions.with_raw_response.retrieve(
                room_session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_0(self, async_client: AsyncTelnyx) -> None:
        session = await async_client.rooms.sessions.list_0()
        assert_matches_type(SessionList0Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_0_with_all_params(self, async_client: AsyncTelnyx) -> None:
        session = await async_client.rooms.sessions.list_0(
            filter={
                "active": True,
                "date_created_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_ended_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_updated_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "room_id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            },
            include_participants=True,
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(SessionList0Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_0(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.sessions.with_raw_response.list_0()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionList0Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_0(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.sessions.with_streaming_response.list_0() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionList0Response, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_1(self, async_client: AsyncTelnyx) -> None:
        session = await async_client.rooms.sessions.list_1(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(SessionList1Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_1_with_all_params(self, async_client: AsyncTelnyx) -> None:
        session = await async_client.rooms.sessions.list_1(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            filter={
                "active": True,
                "date_created_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_ended_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
                "date_updated_at": {
                    "eq": parse_date("2021-04-25"),
                    "gte": parse_date("2021-04-25"),
                    "lte": parse_date("2021-04-25"),
                },
            },
            include_participants=True,
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(SessionList1Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_1(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.sessions.with_raw_response.list_1(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionList1Response, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_1(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.sessions.with_streaming_response.list_1(
            room_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionList1Response, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_1(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            await async_client.rooms.sessions.with_raw_response.list_1(
                room_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_participants(self, async_client: AsyncTelnyx) -> None:
        session = await async_client.rooms.sessions.retrieve_participants(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(SessionRetrieveParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_participants_with_all_params(self, async_client: AsyncTelnyx) -> None:
        session = await async_client.rooms.sessions.retrieve_participants(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
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
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(SessionRetrieveParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_participants(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.sessions.with_raw_response.retrieve_participants(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionRetrieveParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_participants(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.sessions.with_streaming_response.retrieve_participants(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionRetrieveParticipantsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_participants(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            await async_client.rooms.sessions.with_raw_response.retrieve_participants(
                room_session_id="",
            )
