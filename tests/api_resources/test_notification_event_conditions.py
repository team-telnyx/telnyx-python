# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import NotificationEventConditionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotificationEventConditions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        notification_event_condition = client.notification_event_conditions.list()
        assert_matches_type(NotificationEventConditionListResponse, notification_event_condition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        notification_event_condition = client.notification_event_conditions.list(
            filter={
                "associated_record_type": {"eq": "phone_number"},
                "channel_type_id": {"eq": "webhook"},
                "notification_channel": {"eq": "12455643-3cf1-4683-ad23-1cd32f7d5e0a"},
                "notification_event_condition_id": {"eq": "12455643-3cf1-4683-ad23-1cd32f7d5e0a"},
                "notification_profile_id": {"eq": "12455643-3cf1-4683-ad23-1cd32f7d5e0a"},
                "status": {"eq": "enable-received"},
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(NotificationEventConditionListResponse, notification_event_condition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.notification_event_conditions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_event_condition = response.parse()
        assert_matches_type(NotificationEventConditionListResponse, notification_event_condition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.notification_event_conditions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_event_condition = response.parse()
            assert_matches_type(NotificationEventConditionListResponse, notification_event_condition, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotificationEventConditions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        notification_event_condition = await async_client.notification_event_conditions.list()
        assert_matches_type(NotificationEventConditionListResponse, notification_event_condition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        notification_event_condition = await async_client.notification_event_conditions.list(
            filter={
                "associated_record_type": {"eq": "phone_number"},
                "channel_type_id": {"eq": "webhook"},
                "notification_channel": {"eq": "12455643-3cf1-4683-ad23-1cd32f7d5e0a"},
                "notification_event_condition_id": {"eq": "12455643-3cf1-4683-ad23-1cd32f7d5e0a"},
                "notification_profile_id": {"eq": "12455643-3cf1-4683-ad23-1cd32f7d5e0a"},
                "status": {"eq": "enable-received"},
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(NotificationEventConditionListResponse, notification_event_condition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.notification_event_conditions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_event_condition = await response.parse()
        assert_matches_type(NotificationEventConditionListResponse, notification_event_condition, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.notification_event_conditions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_event_condition = await response.parse()
            assert_matches_type(NotificationEventConditionListResponse, notification_event_condition, path=["response"])

        assert cast(Any, response.is_closed) is True
