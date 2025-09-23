# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.types.legacy.reporting.batch_detail_records import (
    MessagingListResponse,
    MessagingCreateResponse,
    MessagingDeleteResponse,
    MessagingRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessaging:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        messaging = client.legacy.reporting.batch_detail_records.messaging.create(
            end_time=parse_datetime("2024-02-12T23:59:59Z"),
            start_time=parse_datetime("2024-02-01T00:00:00Z"),
        )
        assert_matches_type(MessagingCreateResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        messaging = client.legacy.reporting.batch_detail_records.messaging.create(
            end_time=parse_datetime("2024-02-12T23:59:59Z"),
            start_time=parse_datetime("2024-02-01T00:00:00Z"),
            connections=[123, 456],
            directions=[1, 2],
            filters=[
                {
                    "billing_group": "adfaa016-f921-4b6c-97bb-e4c1dad231c5",
                    "cld": "+13129457420",
                    "cld_filter": "contains",
                    "cli": "+13129457420",
                    "cli_filter": "contains",
                    "filter_type": "and",
                    "tags_list": "tag1",
                }
            ],
            include_message_body=True,
            managed_accounts=["f47ac10b-58cc-4372-a567-0e02b2c3d479", "6ba7b810-9dad-11d1-80b4-00c04fd430c8"],
            profiles=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "7d4e3f8a-9b2c-4e1d-8f5a-1a2b3c4d5e6f"],
            record_types=[1, 2],
            report_name="My MDR Report",
            select_all_managed_accounts=False,
            timezone="UTC",
        )
        assert_matches_type(MessagingCreateResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.legacy.reporting.batch_detail_records.messaging.with_raw_response.create(
            end_time=parse_datetime("2024-02-12T23:59:59Z"),
            start_time=parse_datetime("2024-02-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging = response.parse()
        assert_matches_type(MessagingCreateResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.legacy.reporting.batch_detail_records.messaging.with_streaming_response.create(
            end_time=parse_datetime("2024-02-12T23:59:59Z"),
            start_time=parse_datetime("2024-02-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging = response.parse()
            assert_matches_type(MessagingCreateResponse, messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        messaging = client.legacy.reporting.batch_detail_records.messaging.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingRetrieveResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.legacy.reporting.batch_detail_records.messaging.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging = response.parse()
        assert_matches_type(MessagingRetrieveResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.legacy.reporting.batch_detail_records.messaging.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging = response.parse()
            assert_matches_type(MessagingRetrieveResponse, messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.legacy.reporting.batch_detail_records.messaging.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        messaging = client.legacy.reporting.batch_detail_records.messaging.list()
        assert_matches_type(MessagingListResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.legacy.reporting.batch_detail_records.messaging.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging = response.parse()
        assert_matches_type(MessagingListResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.legacy.reporting.batch_detail_records.messaging.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging = response.parse()
            assert_matches_type(MessagingListResponse, messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        messaging = client.legacy.reporting.batch_detail_records.messaging.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingDeleteResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.legacy.reporting.batch_detail_records.messaging.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging = response.parse()
        assert_matches_type(MessagingDeleteResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.legacy.reporting.batch_detail_records.messaging.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging = response.parse()
            assert_matches_type(MessagingDeleteResponse, messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.legacy.reporting.batch_detail_records.messaging.with_raw_response.delete(
                "",
            )


class TestAsyncMessaging:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        messaging = await async_client.legacy.reporting.batch_detail_records.messaging.create(
            end_time=parse_datetime("2024-02-12T23:59:59Z"),
            start_time=parse_datetime("2024-02-01T00:00:00Z"),
        )
        assert_matches_type(MessagingCreateResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging = await async_client.legacy.reporting.batch_detail_records.messaging.create(
            end_time=parse_datetime("2024-02-12T23:59:59Z"),
            start_time=parse_datetime("2024-02-01T00:00:00Z"),
            connections=[123, 456],
            directions=[1, 2],
            filters=[
                {
                    "billing_group": "adfaa016-f921-4b6c-97bb-e4c1dad231c5",
                    "cld": "+13129457420",
                    "cld_filter": "contains",
                    "cli": "+13129457420",
                    "cli_filter": "contains",
                    "filter_type": "and",
                    "tags_list": "tag1",
                }
            ],
            include_message_body=True,
            managed_accounts=["f47ac10b-58cc-4372-a567-0e02b2c3d479", "6ba7b810-9dad-11d1-80b4-00c04fd430c8"],
            profiles=["3fa85f64-5717-4562-b3fc-2c963f66afa6", "7d4e3f8a-9b2c-4e1d-8f5a-1a2b3c4d5e6f"],
            record_types=[1, 2],
            report_name="My MDR Report",
            select_all_managed_accounts=False,
            timezone="UTC",
        )
        assert_matches_type(MessagingCreateResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.legacy.reporting.batch_detail_records.messaging.with_raw_response.create(
            end_time=parse_datetime("2024-02-12T23:59:59Z"),
            start_time=parse_datetime("2024-02-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging = await response.parse()
        assert_matches_type(MessagingCreateResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.legacy.reporting.batch_detail_records.messaging.with_streaming_response.create(
            end_time=parse_datetime("2024-02-12T23:59:59Z"),
            start_time=parse_datetime("2024-02-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging = await response.parse()
            assert_matches_type(MessagingCreateResponse, messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        messaging = await async_client.legacy.reporting.batch_detail_records.messaging.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingRetrieveResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.legacy.reporting.batch_detail_records.messaging.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging = await response.parse()
        assert_matches_type(MessagingRetrieveResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.legacy.reporting.batch_detail_records.messaging.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging = await response.parse()
            assert_matches_type(MessagingRetrieveResponse, messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.legacy.reporting.batch_detail_records.messaging.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        messaging = await async_client.legacy.reporting.batch_detail_records.messaging.list()
        assert_matches_type(MessagingListResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.legacy.reporting.batch_detail_records.messaging.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging = await response.parse()
        assert_matches_type(MessagingListResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.legacy.reporting.batch_detail_records.messaging.with_streaming_response.list()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging = await response.parse()
            assert_matches_type(MessagingListResponse, messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        messaging = await async_client.legacy.reporting.batch_detail_records.messaging.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingDeleteResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.legacy.reporting.batch_detail_records.messaging.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging = await response.parse()
        assert_matches_type(MessagingDeleteResponse, messaging, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.legacy.reporting.batch_detail_records.messaging.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging = await response.parse()
            assert_matches_type(MessagingDeleteResponse, messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.legacy.reporting.batch_detail_records.messaging.with_raw_response.delete(
                "",
            )
