# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    CalendarConnectionResponse,
    CalendarConnectionListResponse,
    CalendarConnectionCreateResponse,
    CalendarConnectionUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalendarConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        calendar_connection = client.calendar_connections.create(
            platform="google_calendar",
        )
        assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.calendar_connections.with_raw_response.create(
            platform="google_calendar",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.calendar_connections.with_streaming_response.create(
            platform="google_calendar",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        calendar_connection = client.calendar_connections.retrieve(
            "id",
        )
        assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.calendar_connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.calendar_connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calendar_connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        calendar_connection = client.calendar_connections.update(
            id="id",
        )
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        calendar_connection = client.calendar_connections.update(
            id="id",
            auto_join_policy="all_meetings",
            bot_name="x",
            default_assistant={
                "id": "x",
                "audio_gate": "half_duplex",
                "dynamic_variables": {"foo": "string"},
                "leave_on_end": True,
            },
            default_barge_in=True,
            default_recording=True,
            default_recording_export={
                "bucket": "meeting-recordings",
                "prefix": "prefix",
            },
            default_summarize_on_end=True,
            default_voice="x",
            default_webhook_url="https://example.com/meeting-events",
        )
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.calendar_connections.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.calendar_connections.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calendar_connections.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        calendar_connection = client.calendar_connections.list()
        assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.calendar_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.calendar_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        calendar_connection = client.calendar_connections.delete(
            "id",
        )
        assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.calendar_connections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = response.parse()
        assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.calendar_connections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = response.parse()
            assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calendar_connections.with_raw_response.delete(
                "",
            )


class TestAsyncCalendarConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        calendar_connection = await async_client.calendar_connections.create(
            platform="google_calendar",
        )
        assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calendar_connections.with_raw_response.create(
            platform="google_calendar",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calendar_connections.with_streaming_response.create(
            platform="google_calendar",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionCreateResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        calendar_connection = await async_client.calendar_connections.retrieve(
            "id",
        )
        assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calendar_connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calendar_connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calendar_connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        calendar_connection = await async_client.calendar_connections.update(
            id="id",
        )
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        calendar_connection = await async_client.calendar_connections.update(
            id="id",
            auto_join_policy="all_meetings",
            bot_name="x",
            default_assistant={
                "id": "x",
                "audio_gate": "half_duplex",
                "dynamic_variables": {"foo": "string"},
                "leave_on_end": True,
            },
            default_barge_in=True,
            default_recording=True,
            default_recording_export={
                "bucket": "meeting-recordings",
                "prefix": "prefix",
            },
            default_summarize_on_end=True,
            default_voice="x",
            default_webhook_url="https://example.com/meeting-events",
        )
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calendar_connections.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calendar_connections.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionUpdateResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calendar_connections.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        calendar_connection = await async_client.calendar_connections.list()
        assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calendar_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calendar_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionListResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        calendar_connection = await async_client.calendar_connections.delete(
            "id",
        )
        assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.calendar_connections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar_connection = await response.parse()
        assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.calendar_connections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar_connection = await response.parse()
            assert_matches_type(CalendarConnectionResponse, calendar_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calendar_connections.with_raw_response.delete(
                "",
            )
