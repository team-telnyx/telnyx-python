# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.types.ai.assistants import (
    ScheduledEventResponse,
    ScheduledEventListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScheduledEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        scheduled_event = client.ai.assistants.scheduled_events.create(
            assistant_id="assistant_id",
            scheduled_at_fixed_datetime=parse_datetime("2025-04-15T13:07:28.764Z"),
            telnyx_agent_target="telnyx_agent_target",
            telnyx_conversation_channel="phone_call",
            telnyx_end_user_target="telnyx_end_user_target",
        )
        assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        scheduled_event = client.ai.assistants.scheduled_events.create(
            assistant_id="assistant_id",
            scheduled_at_fixed_datetime=parse_datetime("2025-04-15T13:07:28.764Z"),
            telnyx_agent_target="telnyx_agent_target",
            telnyx_conversation_channel="phone_call",
            telnyx_end_user_target="telnyx_end_user_target",
            conversation_metadata={"foo": "string"},
            text="text",
        )
        assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.assistants.scheduled_events.with_raw_response.create(
            assistant_id="assistant_id",
            scheduled_at_fixed_datetime=parse_datetime("2025-04-15T13:07:28.764Z"),
            telnyx_agent_target="telnyx_agent_target",
            telnyx_conversation_channel="phone_call",
            telnyx_end_user_target="telnyx_end_user_target",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_event = response.parse()
        assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.assistants.scheduled_events.with_streaming_response.create(
            assistant_id="assistant_id",
            scheduled_at_fixed_datetime=parse_datetime("2025-04-15T13:07:28.764Z"),
            telnyx_agent_target="telnyx_agent_target",
            telnyx_conversation_channel="phone_call",
            telnyx_end_user_target="telnyx_end_user_target",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_event = response.parse()
            assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.scheduled_events.with_raw_response.create(
                assistant_id="",
                scheduled_at_fixed_datetime=parse_datetime("2025-04-15T13:07:28.764Z"),
                telnyx_agent_target="telnyx_agent_target",
                telnyx_conversation_channel="phone_call",
                telnyx_end_user_target="telnyx_end_user_target",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        scheduled_event = client.ai.assistants.scheduled_events.retrieve(
            event_id="event_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.assistants.scheduled_events.with_raw_response.retrieve(
            event_id="event_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_event = response.parse()
        assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.assistants.scheduled_events.with_streaming_response.retrieve(
            event_id="event_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_event = response.parse()
            assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.scheduled_events.with_raw_response.retrieve(
                event_id="event_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.ai.assistants.scheduled_events.with_raw_response.retrieve(
                event_id="",
                assistant_id="assistant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        scheduled_event = client.ai.assistants.scheduled_events.list(
            assistant_id="assistant_id",
        )
        assert_matches_type(ScheduledEventListResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        scheduled_event = client.ai.assistants.scheduled_events.list(
            assistant_id="assistant_id",
            conversation_channel="phone_call",
            from_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            page={
                "number": 1,
                "size": 1,
            },
            to_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ScheduledEventListResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.assistants.scheduled_events.with_raw_response.list(
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_event = response.parse()
        assert_matches_type(ScheduledEventListResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.assistants.scheduled_events.with_streaming_response.list(
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_event = response.parse()
            assert_matches_type(ScheduledEventListResponse, scheduled_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.scheduled_events.with_raw_response.list(
                assistant_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        scheduled_event = client.ai.assistants.scheduled_events.delete(
            event_id="event_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(object, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.assistants.scheduled_events.with_raw_response.delete(
            event_id="event_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_event = response.parse()
        assert_matches_type(object, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.assistants.scheduled_events.with_streaming_response.delete(
            event_id="event_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_event = response.parse()
            assert_matches_type(object, scheduled_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.scheduled_events.with_raw_response.delete(
                event_id="event_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.ai.assistants.scheduled_events.with_raw_response.delete(
                event_id="",
                assistant_id="assistant_id",
            )


class TestAsyncScheduledEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        scheduled_event = await async_client.ai.assistants.scheduled_events.create(
            assistant_id="assistant_id",
            scheduled_at_fixed_datetime=parse_datetime("2025-04-15T13:07:28.764Z"),
            telnyx_agent_target="telnyx_agent_target",
            telnyx_conversation_channel="phone_call",
            telnyx_end_user_target="telnyx_end_user_target",
        )
        assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        scheduled_event = await async_client.ai.assistants.scheduled_events.create(
            assistant_id="assistant_id",
            scheduled_at_fixed_datetime=parse_datetime("2025-04-15T13:07:28.764Z"),
            telnyx_agent_target="telnyx_agent_target",
            telnyx_conversation_channel="phone_call",
            telnyx_end_user_target="telnyx_end_user_target",
            conversation_metadata={"foo": "string"},
            text="text",
        )
        assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.scheduled_events.with_raw_response.create(
            assistant_id="assistant_id",
            scheduled_at_fixed_datetime=parse_datetime("2025-04-15T13:07:28.764Z"),
            telnyx_agent_target="telnyx_agent_target",
            telnyx_conversation_channel="phone_call",
            telnyx_end_user_target="telnyx_end_user_target",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_event = await response.parse()
        assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.scheduled_events.with_streaming_response.create(
            assistant_id="assistant_id",
            scheduled_at_fixed_datetime=parse_datetime("2025-04-15T13:07:28.764Z"),
            telnyx_agent_target="telnyx_agent_target",
            telnyx_conversation_channel="phone_call",
            telnyx_end_user_target="telnyx_end_user_target",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_event = await response.parse()
            assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.scheduled_events.with_raw_response.create(
                assistant_id="",
                scheduled_at_fixed_datetime=parse_datetime("2025-04-15T13:07:28.764Z"),
                telnyx_agent_target="telnyx_agent_target",
                telnyx_conversation_channel="phone_call",
                telnyx_end_user_target="telnyx_end_user_target",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        scheduled_event = await async_client.ai.assistants.scheduled_events.retrieve(
            event_id="event_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.scheduled_events.with_raw_response.retrieve(
            event_id="event_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_event = await response.parse()
        assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.scheduled_events.with_streaming_response.retrieve(
            event_id="event_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_event = await response.parse()
            assert_matches_type(ScheduledEventResponse, scheduled_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.scheduled_events.with_raw_response.retrieve(
                event_id="event_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.ai.assistants.scheduled_events.with_raw_response.retrieve(
                event_id="",
                assistant_id="assistant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        scheduled_event = await async_client.ai.assistants.scheduled_events.list(
            assistant_id="assistant_id",
        )
        assert_matches_type(ScheduledEventListResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        scheduled_event = await async_client.ai.assistants.scheduled_events.list(
            assistant_id="assistant_id",
            conversation_channel="phone_call",
            from_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            page={
                "number": 1,
                "size": 1,
            },
            to_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ScheduledEventListResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.scheduled_events.with_raw_response.list(
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_event = await response.parse()
        assert_matches_type(ScheduledEventListResponse, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.scheduled_events.with_streaming_response.list(
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_event = await response.parse()
            assert_matches_type(ScheduledEventListResponse, scheduled_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.scheduled_events.with_raw_response.list(
                assistant_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        scheduled_event = await async_client.ai.assistants.scheduled_events.delete(
            event_id="event_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(object, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.scheduled_events.with_raw_response.delete(
            event_id="event_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_event = await response.parse()
        assert_matches_type(object, scheduled_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.scheduled_events.with_streaming_response.delete(
            event_id="event_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_event = await response.parse()
            assert_matches_type(object, scheduled_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.scheduled_events.with_raw_response.delete(
                event_id="event_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.ai.assistants.scheduled_events.with_raw_response.delete(
                event_id="",
                assistant_id="assistant_id",
            )
