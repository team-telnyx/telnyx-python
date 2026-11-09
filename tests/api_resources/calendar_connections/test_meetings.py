# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.types.calendar_connections import (
    MeetingListResponse,
    MeetingUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMeetings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        meeting = client.calendar_connections.meetings.update(
            meeting_id="meeting_id",
            id="id",
            bot_will_join=False,
        )
        assert_matches_type(MeetingUpdateResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.calendar_connections.meetings.with_raw_response.update(
            meeting_id="meeting_id",
            id="id",
            bot_will_join=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingUpdateResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.calendar_connections.meetings.with_streaming_response.update(
            meeting_id="meeting_id",
            id="id",
            bot_will_join=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingUpdateResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calendar_connections.meetings.with_raw_response.update(
                meeting_id="meeting_id",
                id="",
                bot_will_join=False,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.calendar_connections.meetings.with_raw_response.update(
                meeting_id="",
                id="id",
                bot_will_join=False,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        meeting = client.calendar_connections.meetings.list(
            id="id",
        )
        assert_matches_type(MeetingListResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        meeting = client.calendar_connections.meetings.list(
            id="id",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MeetingListResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.calendar_connections.meetings.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingListResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.calendar_connections.meetings.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingListResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calendar_connections.meetings.with_raw_response.list(
                id="",
            )


class TestAsyncMeetings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        meeting = await async_client.calendar_connections.meetings.update(
            meeting_id="meeting_id",
            id="id",
            bot_will_join=False,
        )
        assert_matches_type(MeetingUpdateResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calendar_connections.meetings.with_raw_response.update(
            meeting_id="meeting_id",
            id="id",
            bot_will_join=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingUpdateResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calendar_connections.meetings.with_streaming_response.update(
            meeting_id="meeting_id",
            id="id",
            bot_will_join=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingUpdateResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calendar_connections.meetings.with_raw_response.update(
                meeting_id="meeting_id",
                id="",
                bot_will_join=False,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.calendar_connections.meetings.with_raw_response.update(
                meeting_id="",
                id="id",
                bot_will_join=False,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        meeting = await async_client.calendar_connections.meetings.list(
            id="id",
        )
        assert_matches_type(MeetingListResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        meeting = await async_client.calendar_connections.meetings.list(
            id="id",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MeetingListResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calendar_connections.meetings.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingListResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calendar_connections.meetings.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingListResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calendar_connections.meetings.with_raw_response.list(
                id="",
            )
