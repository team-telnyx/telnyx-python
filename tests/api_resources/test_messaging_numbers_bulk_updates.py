# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    MessagingNumbersBulkUpdateCreateResponse,
    MessagingNumbersBulkUpdateRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessagingNumbersBulkUpdates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        messaging_numbers_bulk_update = client.messaging_numbers_bulk_updates.create(
            messaging_profile_id="00000000-0000-0000-0000-000000000000",
            numbers=["+18880000000", "+18880000001", "+18880000002"],
        )
        assert_matches_type(MessagingNumbersBulkUpdateCreateResponse, messaging_numbers_bulk_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.messaging_numbers_bulk_updates.with_raw_response.create(
            messaging_profile_id="00000000-0000-0000-0000-000000000000",
            numbers=["+18880000000", "+18880000001", "+18880000002"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_numbers_bulk_update = response.parse()
        assert_matches_type(MessagingNumbersBulkUpdateCreateResponse, messaging_numbers_bulk_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.messaging_numbers_bulk_updates.with_streaming_response.create(
            messaging_profile_id="00000000-0000-0000-0000-000000000000",
            numbers=["+18880000000", "+18880000001", "+18880000002"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_numbers_bulk_update = response.parse()
            assert_matches_type(
                MessagingNumbersBulkUpdateCreateResponse, messaging_numbers_bulk_update, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        messaging_numbers_bulk_update = client.messaging_numbers_bulk_updates.retrieve(
            "order_id",
        )
        assert_matches_type(
            MessagingNumbersBulkUpdateRetrieveResponse, messaging_numbers_bulk_update, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.messaging_numbers_bulk_updates.with_raw_response.retrieve(
            "order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_numbers_bulk_update = response.parse()
        assert_matches_type(
            MessagingNumbersBulkUpdateRetrieveResponse, messaging_numbers_bulk_update, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.messaging_numbers_bulk_updates.with_streaming_response.retrieve(
            "order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_numbers_bulk_update = response.parse()
            assert_matches_type(
                MessagingNumbersBulkUpdateRetrieveResponse, messaging_numbers_bulk_update, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.messaging_numbers_bulk_updates.with_raw_response.retrieve(
                "",
            )


class TestAsyncMessagingNumbersBulkUpdates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        messaging_numbers_bulk_update = await async_client.messaging_numbers_bulk_updates.create(
            messaging_profile_id="00000000-0000-0000-0000-000000000000",
            numbers=["+18880000000", "+18880000001", "+18880000002"],
        )
        assert_matches_type(MessagingNumbersBulkUpdateCreateResponse, messaging_numbers_bulk_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_numbers_bulk_updates.with_raw_response.create(
            messaging_profile_id="00000000-0000-0000-0000-000000000000",
            numbers=["+18880000000", "+18880000001", "+18880000002"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_numbers_bulk_update = await response.parse()
        assert_matches_type(MessagingNumbersBulkUpdateCreateResponse, messaging_numbers_bulk_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_numbers_bulk_updates.with_streaming_response.create(
            messaging_profile_id="00000000-0000-0000-0000-000000000000",
            numbers=["+18880000000", "+18880000001", "+18880000002"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_numbers_bulk_update = await response.parse()
            assert_matches_type(
                MessagingNumbersBulkUpdateCreateResponse, messaging_numbers_bulk_update, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        messaging_numbers_bulk_update = await async_client.messaging_numbers_bulk_updates.retrieve(
            "order_id",
        )
        assert_matches_type(
            MessagingNumbersBulkUpdateRetrieveResponse, messaging_numbers_bulk_update, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_numbers_bulk_updates.with_raw_response.retrieve(
            "order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_numbers_bulk_update = await response.parse()
        assert_matches_type(
            MessagingNumbersBulkUpdateRetrieveResponse, messaging_numbers_bulk_update, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_numbers_bulk_updates.with_streaming_response.retrieve(
            "order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_numbers_bulk_update = await response.parse()
            assert_matches_type(
                MessagingNumbersBulkUpdateRetrieveResponse, messaging_numbers_bulk_update, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.messaging_numbers_bulk_updates.with_raw_response.retrieve(
                "",
            )
