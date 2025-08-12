# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import WebhookDeliveryListResponse, WebhookDeliveryRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhookDeliveries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        webhook_delivery = client.webhook_deliveries.retrieve(
            "C9C0797E-901D-4349-A33C-C2C8F31A92C2",
        )
        assert_matches_type(WebhookDeliveryRetrieveResponse, webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.webhook_deliveries.with_raw_response.retrieve(
            "C9C0797E-901D-4349-A33C-C2C8F31A92C2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_delivery = response.parse()
        assert_matches_type(WebhookDeliveryRetrieveResponse, webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.webhook_deliveries.with_streaming_response.retrieve(
            "C9C0797E-901D-4349-A33C-C2C8F31A92C2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_delivery = response.parse()
            assert_matches_type(WebhookDeliveryRetrieveResponse, webhook_delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhook_deliveries.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        webhook_delivery = client.webhook_deliveries.list()
        assert_matches_type(WebhookDeliveryListResponse, webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        webhook_delivery = client.webhook_deliveries.list(
            filter={
                "attempts": {"contains": "https://fallback.example.com/webhooks"},
                "event_type": "call_initiated,call.initiated",
                "finished_at": {
                    "gte": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "started_at": {
                    "gte": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "status": {"eq": "delivered"},
                "webhook": {"contains": "call.initiated"},
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(WebhookDeliveryListResponse, webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.webhook_deliveries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_delivery = response.parse()
        assert_matches_type(WebhookDeliveryListResponse, webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.webhook_deliveries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_delivery = response.parse()
            assert_matches_type(WebhookDeliveryListResponse, webhook_delivery, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhookDeliveries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        webhook_delivery = await async_client.webhook_deliveries.retrieve(
            "C9C0797E-901D-4349-A33C-C2C8F31A92C2",
        )
        assert_matches_type(WebhookDeliveryRetrieveResponse, webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.webhook_deliveries.with_raw_response.retrieve(
            "C9C0797E-901D-4349-A33C-C2C8F31A92C2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_delivery = await response.parse()
        assert_matches_type(WebhookDeliveryRetrieveResponse, webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.webhook_deliveries.with_streaming_response.retrieve(
            "C9C0797E-901D-4349-A33C-C2C8F31A92C2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_delivery = await response.parse()
            assert_matches_type(WebhookDeliveryRetrieveResponse, webhook_delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhook_deliveries.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        webhook_delivery = await async_client.webhook_deliveries.list()
        assert_matches_type(WebhookDeliveryListResponse, webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        webhook_delivery = await async_client.webhook_deliveries.list(
            filter={
                "attempts": {"contains": "https://fallback.example.com/webhooks"},
                "event_type": "call_initiated,call.initiated",
                "finished_at": {
                    "gte": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "started_at": {
                    "gte": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "status": {"eq": "delivered"},
                "webhook": {"contains": "call.initiated"},
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(WebhookDeliveryListResponse, webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.webhook_deliveries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_delivery = await response.parse()
        assert_matches_type(WebhookDeliveryListResponse, webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.webhook_deliveries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_delivery = await response.parse()
            assert_matches_type(WebhookDeliveryListResponse, webhook_delivery, path=["response"])

        assert cast(Any, response.is_closed) is True
