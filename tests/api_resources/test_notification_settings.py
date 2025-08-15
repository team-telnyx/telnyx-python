# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    NotificationSettingListResponse,
    NotificationSettingCreateResponse,
    NotificationSettingDeleteResponse,
    NotificationSettingRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotificationSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        notification_setting = client.notification_settings.create()
        assert_matches_type(NotificationSettingCreateResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        notification_setting = client.notification_settings.create(
            notification_channel_id="12455643-3cf1-4683-ad23-1cd32f7d5e0a",
            notification_event_condition_id="70c7c5cb-dce2-4124-accb-870d39dbe852",
            notification_profile_id="12455643-3cf1-4683-ad23-1cd32f7d5e0a",
            parameters=[
                {
                    "name": "phone_number",
                    "value": "+13125550000",
                }
            ],
        )
        assert_matches_type(NotificationSettingCreateResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.notification_settings.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_setting = response.parse()
        assert_matches_type(NotificationSettingCreateResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.notification_settings.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_setting = response.parse()
            assert_matches_type(NotificationSettingCreateResponse, notification_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        notification_setting = client.notification_settings.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NotificationSettingRetrieveResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.notification_settings.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_setting = response.parse()
        assert_matches_type(NotificationSettingRetrieveResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.notification_settings.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_setting = response.parse()
            assert_matches_type(NotificationSettingRetrieveResponse, notification_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notification_settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        notification_setting = client.notification_settings.list()
        assert_matches_type(NotificationSettingListResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        notification_setting = client.notification_settings.list(
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
        assert_matches_type(NotificationSettingListResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.notification_settings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_setting = response.parse()
        assert_matches_type(NotificationSettingListResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.notification_settings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_setting = response.parse()
            assert_matches_type(NotificationSettingListResponse, notification_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        notification_setting = client.notification_settings.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NotificationSettingDeleteResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.notification_settings.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_setting = response.parse()
        assert_matches_type(NotificationSettingDeleteResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.notification_settings.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_setting = response.parse()
            assert_matches_type(NotificationSettingDeleteResponse, notification_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notification_settings.with_raw_response.delete(
                "",
            )


class TestAsyncNotificationSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        notification_setting = await async_client.notification_settings.create()
        assert_matches_type(NotificationSettingCreateResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        notification_setting = await async_client.notification_settings.create(
            notification_channel_id="12455643-3cf1-4683-ad23-1cd32f7d5e0a",
            notification_event_condition_id="70c7c5cb-dce2-4124-accb-870d39dbe852",
            notification_profile_id="12455643-3cf1-4683-ad23-1cd32f7d5e0a",
            parameters=[
                {
                    "name": "phone_number",
                    "value": "+13125550000",
                }
            ],
        )
        assert_matches_type(NotificationSettingCreateResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.notification_settings.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_setting = await response.parse()
        assert_matches_type(NotificationSettingCreateResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.notification_settings.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_setting = await response.parse()
            assert_matches_type(NotificationSettingCreateResponse, notification_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        notification_setting = await async_client.notification_settings.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NotificationSettingRetrieveResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.notification_settings.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_setting = await response.parse()
        assert_matches_type(NotificationSettingRetrieveResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.notification_settings.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_setting = await response.parse()
            assert_matches_type(NotificationSettingRetrieveResponse, notification_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notification_settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        notification_setting = await async_client.notification_settings.list()
        assert_matches_type(NotificationSettingListResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        notification_setting = await async_client.notification_settings.list(
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
        assert_matches_type(NotificationSettingListResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.notification_settings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_setting = await response.parse()
        assert_matches_type(NotificationSettingListResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.notification_settings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_setting = await response.parse()
            assert_matches_type(NotificationSettingListResponse, notification_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        notification_setting = await async_client.notification_settings.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NotificationSettingDeleteResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.notification_settings.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification_setting = await response.parse()
        assert_matches_type(NotificationSettingDeleteResponse, notification_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.notification_settings.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification_setting = await response.parse()
            assert_matches_type(NotificationSettingDeleteResponse, notification_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notification_settings.with_raw_response.delete(
                "",
            )
