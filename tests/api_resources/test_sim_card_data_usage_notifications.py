# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    SimCardDataUsageNotificationListResponse,
    SimCardDataUsageNotificationCreateResponse,
    SimCardDataUsageNotificationDeleteResponse,
    SimCardDataUsageNotificationUpdateResponse,
    SimCardDataUsageNotificationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimCardDataUsageNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        sim_card_data_usage_notification = client.sim_card_data_usage_notifications.create(
            sim_card_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            threshold={},
        )
        assert_matches_type(
            SimCardDataUsageNotificationCreateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        sim_card_data_usage_notification = client.sim_card_data_usage_notifications.create(
            sim_card_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            threshold={
                "amount": "2048.1",
                "unit": "MB",
            },
        )
        assert_matches_type(
            SimCardDataUsageNotificationCreateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.sim_card_data_usage_notifications.with_raw_response.create(
            sim_card_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            threshold={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_data_usage_notification = response.parse()
        assert_matches_type(
            SimCardDataUsageNotificationCreateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.sim_card_data_usage_notifications.with_streaming_response.create(
            sim_card_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            threshold={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_data_usage_notification = response.parse()
            assert_matches_type(
                SimCardDataUsageNotificationCreateResponse, sim_card_data_usage_notification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        sim_card_data_usage_notification = client.sim_card_data_usage_notifications.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(
            SimCardDataUsageNotificationRetrieveResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.sim_card_data_usage_notifications.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_data_usage_notification = response.parse()
        assert_matches_type(
            SimCardDataUsageNotificationRetrieveResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.sim_card_data_usage_notifications.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_data_usage_notification = response.parse()
            assert_matches_type(
                SimCardDataUsageNotificationRetrieveResponse, sim_card_data_usage_notification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_data_usage_notifications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        sim_card_data_usage_notification = client.sim_card_data_usage_notifications.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(
            SimCardDataUsageNotificationUpdateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        sim_card_data_usage_notification = client.sim_card_data_usage_notifications.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            sim_card_id="b34c1683-cd85-4493-b9a5-315eb4bc5e19",
            threshold={
                "amount": "2048.0",
                "unit": "MB",
            },
        )
        assert_matches_type(
            SimCardDataUsageNotificationUpdateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.sim_card_data_usage_notifications.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_data_usage_notification = response.parse()
        assert_matches_type(
            SimCardDataUsageNotificationUpdateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.sim_card_data_usage_notifications.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_data_usage_notification = response.parse()
            assert_matches_type(
                SimCardDataUsageNotificationUpdateResponse, sim_card_data_usage_notification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_data_usage_notifications.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        sim_card_data_usage_notification = client.sim_card_data_usage_notifications.list()
        assert_matches_type(
            SimCardDataUsageNotificationListResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        sim_card_data_usage_notification = client.sim_card_data_usage_notifications.list(
            filter_sim_card_id="47a1c2b0-cc7b-4ab1-bb98-b33fb0fc61b9",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(
            SimCardDataUsageNotificationListResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.sim_card_data_usage_notifications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_data_usage_notification = response.parse()
        assert_matches_type(
            SimCardDataUsageNotificationListResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.sim_card_data_usage_notifications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_data_usage_notification = response.parse()
            assert_matches_type(
                SimCardDataUsageNotificationListResponse, sim_card_data_usage_notification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        sim_card_data_usage_notification = client.sim_card_data_usage_notifications.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(
            SimCardDataUsageNotificationDeleteResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.sim_card_data_usage_notifications.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_data_usage_notification = response.parse()
        assert_matches_type(
            SimCardDataUsageNotificationDeleteResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.sim_card_data_usage_notifications.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_data_usage_notification = response.parse()
            assert_matches_type(
                SimCardDataUsageNotificationDeleteResponse, sim_card_data_usage_notification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_data_usage_notifications.with_raw_response.delete(
                "",
            )


class TestAsyncSimCardDataUsageNotifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        sim_card_data_usage_notification = await async_client.sim_card_data_usage_notifications.create(
            sim_card_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            threshold={},
        )
        assert_matches_type(
            SimCardDataUsageNotificationCreateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card_data_usage_notification = await async_client.sim_card_data_usage_notifications.create(
            sim_card_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            threshold={
                "amount": "2048.1",
                "unit": "MB",
            },
        )
        assert_matches_type(
            SimCardDataUsageNotificationCreateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_data_usage_notifications.with_raw_response.create(
            sim_card_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            threshold={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_data_usage_notification = await response.parse()
        assert_matches_type(
            SimCardDataUsageNotificationCreateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_data_usage_notifications.with_streaming_response.create(
            sim_card_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            threshold={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_data_usage_notification = await response.parse()
            assert_matches_type(
                SimCardDataUsageNotificationCreateResponse, sim_card_data_usage_notification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        sim_card_data_usage_notification = await async_client.sim_card_data_usage_notifications.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(
            SimCardDataUsageNotificationRetrieveResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_data_usage_notifications.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_data_usage_notification = await response.parse()
        assert_matches_type(
            SimCardDataUsageNotificationRetrieveResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_data_usage_notifications.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_data_usage_notification = await response.parse()
            assert_matches_type(
                SimCardDataUsageNotificationRetrieveResponse, sim_card_data_usage_notification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_data_usage_notifications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        sim_card_data_usage_notification = await async_client.sim_card_data_usage_notifications.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(
            SimCardDataUsageNotificationUpdateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card_data_usage_notification = await async_client.sim_card_data_usage_notifications.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            sim_card_id="b34c1683-cd85-4493-b9a5-315eb4bc5e19",
            threshold={
                "amount": "2048.0",
                "unit": "MB",
            },
        )
        assert_matches_type(
            SimCardDataUsageNotificationUpdateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_data_usage_notifications.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_data_usage_notification = await response.parse()
        assert_matches_type(
            SimCardDataUsageNotificationUpdateResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_data_usage_notifications.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_data_usage_notification = await response.parse()
            assert_matches_type(
                SimCardDataUsageNotificationUpdateResponse, sim_card_data_usage_notification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_data_usage_notifications.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        sim_card_data_usage_notification = await async_client.sim_card_data_usage_notifications.list()
        assert_matches_type(
            SimCardDataUsageNotificationListResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card_data_usage_notification = await async_client.sim_card_data_usage_notifications.list(
            filter_sim_card_id="47a1c2b0-cc7b-4ab1-bb98-b33fb0fc61b9",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(
            SimCardDataUsageNotificationListResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_data_usage_notifications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_data_usage_notification = await response.parse()
        assert_matches_type(
            SimCardDataUsageNotificationListResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_data_usage_notifications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_data_usage_notification = await response.parse()
            assert_matches_type(
                SimCardDataUsageNotificationListResponse, sim_card_data_usage_notification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        sim_card_data_usage_notification = await async_client.sim_card_data_usage_notifications.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(
            SimCardDataUsageNotificationDeleteResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_data_usage_notifications.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_data_usage_notification = await response.parse()
        assert_matches_type(
            SimCardDataUsageNotificationDeleteResponse, sim_card_data_usage_notification, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_data_usage_notifications.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_data_usage_notification = await response.parse()
            assert_matches_type(
                SimCardDataUsageNotificationDeleteResponse, sim_card_data_usage_notification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_data_usage_notifications.with_raw_response.delete(
                "",
            )
