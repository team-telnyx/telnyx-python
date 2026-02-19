# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.ai.missions.runs import (
    EventLogResponse,
    EventListResponse,
    EventGetEventDetailsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        event = client.ai.missions.runs.events.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncDefaultFlatPagination[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        event = client.ai.missions.runs.events.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="agent_id",
            page_number=1,
            page_size=1,
            step_id="step_id",
            type="type",
        )
        assert_matches_type(SyncDefaultFlatPagination[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.events.with_raw_response.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.missions.runs.events.with_streaming_response.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[EventListResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.events.with_raw_response.list(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.events.with_raw_response.list(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_event_details(self, client: Telnyx) -> None:
        event = client.ai.missions.runs.events.get_event_details(
            event_id="event_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EventGetEventDetailsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_event_details(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.events.with_raw_response.get_event_details(
            event_id="event_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventGetEventDetailsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_event_details(self, client: Telnyx) -> None:
        with client.ai.missions.runs.events.with_streaming_response.get_event_details(
            event_id="event_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventGetEventDetailsResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_event_details(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.events.with_raw_response.get_event_details(
                event_id="event_id",
                mission_id="",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.events.with_raw_response.get_event_details(
                event_id="event_id",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.ai.missions.runs.events.with_raw_response.get_event_details(
                event_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_log(self, client: Telnyx) -> None:
        event = client.ai.missions.runs.events.log(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
            type="status_change",
        )
        assert_matches_type(EventLogResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_log_with_all_params(self, client: Telnyx) -> None:
        event = client.ai.missions.runs.events.log(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
            type="status_change",
            agent_id="agent_id",
            idempotency_key="idempotency_key",
            payload={"foo": "bar"},
            step_id="step_id",
        )
        assert_matches_type(EventLogResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_log(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.events.with_raw_response.log(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
            type="status_change",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventLogResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_log(self, client: Telnyx) -> None:
        with client.ai.missions.runs.events.with_streaming_response.log(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
            type="status_change",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventLogResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_log(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.events.with_raw_response.log(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
                summary="summary",
                type="status_change",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.events.with_raw_response.log(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                summary="summary",
                type="status_change",
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        event = await async_client.ai.missions.runs.events.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncDefaultFlatPagination[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        event = await async_client.ai.missions.runs.events.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="agent_id",
            page_number=1,
            page_size=1,
            step_id="step_id",
            type="type",
        )
        assert_matches_type(AsyncDefaultFlatPagination[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.events.with_raw_response.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.events.with_streaming_response.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[EventListResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.events.with_raw_response.list(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.events.with_raw_response.list(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_event_details(self, async_client: AsyncTelnyx) -> None:
        event = await async_client.ai.missions.runs.events.get_event_details(
            event_id="event_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EventGetEventDetailsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_event_details(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.events.with_raw_response.get_event_details(
            event_id="event_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventGetEventDetailsResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_event_details(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.events.with_streaming_response.get_event_details(
            event_id="event_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventGetEventDetailsResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_event_details(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.events.with_raw_response.get_event_details(
                event_id="event_id",
                mission_id="",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.events.with_raw_response.get_event_details(
                event_id="event_id",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.ai.missions.runs.events.with_raw_response.get_event_details(
                event_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_log(self, async_client: AsyncTelnyx) -> None:
        event = await async_client.ai.missions.runs.events.log(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
            type="status_change",
        )
        assert_matches_type(EventLogResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_log_with_all_params(self, async_client: AsyncTelnyx) -> None:
        event = await async_client.ai.missions.runs.events.log(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
            type="status_change",
            agent_id="agent_id",
            idempotency_key="idempotency_key",
            payload={"foo": "bar"},
            step_id="step_id",
        )
        assert_matches_type(EventLogResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_log(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.events.with_raw_response.log(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
            type="status_change",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventLogResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_log(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.events.with_streaming_response.log(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
            type="status_change",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventLogResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_log(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.events.with_raw_response.log(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
                summary="summary",
                type="status_change",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.events.with_raw_response.log(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                summary="summary",
                type="status_change",
            )
