# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    MessageSendResponse,
    MessageRetrieveResponse,
    MessageScheduleResponse,
    MessageSendGroupMmsResponse,
    MessageSendLongCodeResponse,
    MessageSendShortCodeResponse,
    MessageSendNumberPoolResponse,
    MessageCancelScheduledResponse,
)
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        message = client.messages.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.messages.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.messages.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel_scheduled(self, client: Telnyx) -> None:
        message = client.messages.cancel_scheduled(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageCancelScheduledResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel_scheduled(self, client: Telnyx) -> None:
        response = client.messages.with_raw_response.cancel_scheduled(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageCancelScheduledResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel_scheduled(self, client: Telnyx) -> None:
        with client.messages.with_streaming_response.cancel_scheduled(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageCancelScheduledResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel_scheduled(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messages.with_raw_response.cancel_scheduled(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_schedule(self, client: Telnyx) -> None:
        message = client.messages.schedule(
            to="+18445550001",
        )
        assert_matches_type(MessageScheduleResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_schedule_with_all_params(self, client: Telnyx) -> None:
        message = client.messages.schedule(
            to="+18445550001",
            auto_detect=True,
            from_="+18445550001",
            media_urls=["string"],
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            send_at=parse_datetime("2019-01-23T18:30:00Z"),
            subject="From Telnyx!",
            text="Hello, World!",
            type="SMS",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageScheduleResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_schedule(self, client: Telnyx) -> None:
        response = client.messages.with_raw_response.schedule(
            to="+18445550001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageScheduleResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_schedule(self, client: Telnyx) -> None:
        with client.messages.with_streaming_response.schedule(
            to="+18445550001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageScheduleResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: Telnyx) -> None:
        message = client.messages.send(
            to="+18445550001",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Telnyx) -> None:
        message = client.messages.send(
            to="+18445550001",
            auto_detect=True,
            from_="+18445550001",
            media_urls=["http://example.com"],
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            send_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            subject="From Telnyx!",
            text="Hello, World!",
            type="MMS",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Telnyx) -> None:
        response = client.messages.with_raw_response.send(
            to="+18445550001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Telnyx) -> None:
        with client.messages.with_streaming_response.send(
            to="+18445550001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_group_mms(self, client: Telnyx) -> None:
        message = client.messages.send_group_mms(
            from_="+13125551234",
            to=["+18655551234", "+14155551234"],
        )
        assert_matches_type(MessageSendGroupMmsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_group_mms_with_all_params(self, client: Telnyx) -> None:
        message = client.messages.send_group_mms(
            from_="+13125551234",
            to=["+18655551234", "+14155551234"],
            media_urls=["http://example.com"],
            subject="From Telnyx!",
            text="Hello, World!",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageSendGroupMmsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_group_mms(self, client: Telnyx) -> None:
        response = client.messages.with_raw_response.send_group_mms(
            from_="+13125551234",
            to=["+18655551234", "+14155551234"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSendGroupMmsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_group_mms(self, client: Telnyx) -> None:
        with client.messages.with_streaming_response.send_group_mms(
            from_="+13125551234",
            to=["+18655551234", "+14155551234"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSendGroupMmsResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_long_code(self, client: Telnyx) -> None:
        message = client.messages.send_long_code(
            from_="+18445550001",
            to="+13125550002",
        )
        assert_matches_type(MessageSendLongCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_long_code_with_all_params(self, client: Telnyx) -> None:
        message = client.messages.send_long_code(
            from_="+18445550001",
            to="+13125550002",
            auto_detect=True,
            media_urls=["http://example.com"],
            subject="From Telnyx!",
            text="Hello, World!",
            type="MMS",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageSendLongCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_long_code(self, client: Telnyx) -> None:
        response = client.messages.with_raw_response.send_long_code(
            from_="+18445550001",
            to="+13125550002",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSendLongCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_long_code(self, client: Telnyx) -> None:
        with client.messages.with_streaming_response.send_long_code(
            from_="+18445550001",
            to="+13125550002",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSendLongCodeResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_number_pool(self, client: Telnyx) -> None:
        message = client.messages.send_number_pool(
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            to="to",
        )
        assert_matches_type(MessageSendNumberPoolResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_number_pool_with_all_params(self, client: Telnyx) -> None:
        message = client.messages.send_number_pool(
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            to="to",
            auto_detect=True,
            media_urls=["http://example.com"],
            subject="From Telnyx!",
            text="Hello, World!",
            type="MMS",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageSendNumberPoolResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_number_pool(self, client: Telnyx) -> None:
        response = client.messages.with_raw_response.send_number_pool(
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSendNumberPoolResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_number_pool(self, client: Telnyx) -> None:
        with client.messages.with_streaming_response.send_number_pool(
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSendNumberPoolResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_short_code(self, client: Telnyx) -> None:
        message = client.messages.send_short_code(
            from_="+18445550001",
            to="+18445550001",
        )
        assert_matches_type(MessageSendShortCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_short_code_with_all_params(self, client: Telnyx) -> None:
        message = client.messages.send_short_code(
            from_="+18445550001",
            to="+18445550001",
            auto_detect=True,
            media_urls=["http://example.com"],
            subject="From Telnyx!",
            text="Hello, World!",
            type="MMS",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageSendShortCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_short_code(self, client: Telnyx) -> None:
        response = client.messages.with_raw_response.send_short_code(
            from_="+18445550001",
            to="+18445550001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSendShortCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_short_code(self, client: Telnyx) -> None:
        with client.messages.with_streaming_response.send_short_code(
            from_="+18445550001",
            to="+18445550001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSendShortCodeResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messages.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messages.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel_scheduled(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.cancel_scheduled(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageCancelScheduledResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel_scheduled(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messages.with_raw_response.cancel_scheduled(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageCancelScheduledResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_scheduled(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messages.with_streaming_response.cancel_scheduled(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageCancelScheduledResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel_scheduled(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messages.with_raw_response.cancel_scheduled(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_schedule(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.schedule(
            to="+18445550001",
        )
        assert_matches_type(MessageScheduleResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_schedule_with_all_params(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.schedule(
            to="+18445550001",
            auto_detect=True,
            from_="+18445550001",
            media_urls=["string"],
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            send_at=parse_datetime("2019-01-23T18:30:00Z"),
            subject="From Telnyx!",
            text="Hello, World!",
            type="SMS",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageScheduleResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_schedule(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messages.with_raw_response.schedule(
            to="+18445550001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageScheduleResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_schedule(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messages.with_streaming_response.schedule(
            to="+18445550001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageScheduleResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.send(
            to="+18445550001",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.send(
            to="+18445550001",
            auto_detect=True,
            from_="+18445550001",
            media_urls=["http://example.com"],
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            send_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            subject="From Telnyx!",
            text="Hello, World!",
            type="MMS",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messages.with_raw_response.send(
            to="+18445550001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messages.with_streaming_response.send(
            to="+18445550001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_group_mms(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.send_group_mms(
            from_="+13125551234",
            to=["+18655551234", "+14155551234"],
        )
        assert_matches_type(MessageSendGroupMmsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_group_mms_with_all_params(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.send_group_mms(
            from_="+13125551234",
            to=["+18655551234", "+14155551234"],
            media_urls=["http://example.com"],
            subject="From Telnyx!",
            text="Hello, World!",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageSendGroupMmsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_group_mms(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messages.with_raw_response.send_group_mms(
            from_="+13125551234",
            to=["+18655551234", "+14155551234"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSendGroupMmsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_group_mms(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messages.with_streaming_response.send_group_mms(
            from_="+13125551234",
            to=["+18655551234", "+14155551234"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSendGroupMmsResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_long_code(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.send_long_code(
            from_="+18445550001",
            to="+13125550002",
        )
        assert_matches_type(MessageSendLongCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_long_code_with_all_params(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.send_long_code(
            from_="+18445550001",
            to="+13125550002",
            auto_detect=True,
            media_urls=["http://example.com"],
            subject="From Telnyx!",
            text="Hello, World!",
            type="MMS",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageSendLongCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_long_code(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messages.with_raw_response.send_long_code(
            from_="+18445550001",
            to="+13125550002",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSendLongCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_long_code(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messages.with_streaming_response.send_long_code(
            from_="+18445550001",
            to="+13125550002",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSendLongCodeResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_number_pool(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.send_number_pool(
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            to="to",
        )
        assert_matches_type(MessageSendNumberPoolResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_number_pool_with_all_params(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.send_number_pool(
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            to="to",
            auto_detect=True,
            media_urls=["http://example.com"],
            subject="From Telnyx!",
            text="Hello, World!",
            type="MMS",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageSendNumberPoolResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_number_pool(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messages.with_raw_response.send_number_pool(
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSendNumberPoolResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_number_pool(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messages.with_streaming_response.send_number_pool(
            messaging_profile_id="abc85f64-5717-4562-b3fc-2c9600000000",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSendNumberPoolResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_short_code(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.send_short_code(
            from_="+18445550001",
            to="+18445550001",
        )
        assert_matches_type(MessageSendShortCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_short_code_with_all_params(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.messages.send_short_code(
            from_="+18445550001",
            to="+18445550001",
            auto_detect=True,
            media_urls=["http://example.com"],
            subject="From Telnyx!",
            text="Hello, World!",
            type="MMS",
            use_profile_webhooks=True,
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="http://example.com/webhooks",
        )
        assert_matches_type(MessageSendShortCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_short_code(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messages.with_raw_response.send_short_code(
            from_="+18445550001",
            to="+18445550001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSendShortCodeResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_short_code(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messages.with_streaming_response.send_short_code(
            from_="+18445550001",
            to="+18445550001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSendShortCodeResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True
