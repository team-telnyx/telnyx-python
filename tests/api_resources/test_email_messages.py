# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    MessageEvent,
    EmailMessageBatchResponse,
    EmailMessageRetrieveResponse,
)
from telnyx._utils import parse_datetime
from telnyx.pagination import SyncEmailCursorPagination, AsyncEmailCursorPagination
from telnyx.types.email_inboxes import EmailMessage, EmailMessageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        email_message = client.email_messages.create(
            from_="sender@example.com",
            to=["recipient@example.com"],
        )
        assert_matches_type(EmailMessageResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        email_message = client.email_messages.create(
            from_="sender@example.com",
            to=["recipient@example.com"],
            attachments=[
                {
                    "content": "content",
                    "content_id": "content_id",
                    "content_type": "content_type",
                    "disposition": "disposition",
                    "filename": "filename",
                }
            ],
            bcc=["string"],
            cc=["string"],
            forward_of_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_name="from_name",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            headers={"foo": "string"},
            html_body="html_body",
            ignore_suppression=True,
            in_reply_to_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inline_css=True,
            metadata={"foo": "bar"},
            reply_to="string",
            reply_to_all=True,
            sandbox_mode=True,
            scheduled_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            send_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            subject="Hello from Telnyx",
            tags=["string"],
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_variables={"foo": "bar"},
            text_body="This is a test email.",
            tracking_settings={
                "click_tracking": True,
                "open_tracking": True,
            },
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        )
        assert_matches_type(EmailMessageResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.email_messages.with_raw_response.create(
            from_="sender@example.com",
            to=["recipient@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = response.parse()
        assert_matches_type(EmailMessageResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.email_messages.with_streaming_response.create(
            from_="sender@example.com",
            to=["recipient@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = response.parse()
            assert_matches_type(EmailMessageResponse, email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        email_message = client.email_messages.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailMessageRetrieveResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.email_messages.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = response.parse()
        assert_matches_type(EmailMessageRetrieveResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.email_messages.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = response.parse()
            assert_matches_type(EmailMessageRetrieveResponse, email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        email_message = client.email_messages.list()
        assert_matches_type(SyncEmailCursorPagination[EmailMessage], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        email_message = client.email_messages.list(
            page_cursor="page_cursor",
            page_size=1,
        )
        assert_matches_type(SyncEmailCursorPagination[EmailMessage], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.email_messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = response.parse()
        assert_matches_type(SyncEmailCursorPagination[EmailMessage], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.email_messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = response.parse()
            assert_matches_type(SyncEmailCursorPagination[EmailMessage], email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        email_message = client.email_messages.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert email_message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.email_messages.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = response.parse()
        assert email_message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.email_messages.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = response.parse()
            assert email_message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_messages.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch(self, client: Telnyx) -> None:
        email_message = client.email_messages.batch(
            messages=[
                {
                    "from": "sender@example.com",
                    "to": ["recipient1@example.com"],
                },
                {
                    "from": "sender@example.com",
                    "to": ["recipient2@example.com"],
                },
            ],
        )
        assert_matches_type(EmailMessageBatchResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_with_all_params(self, client: Telnyx) -> None:
        email_message = client.email_messages.batch(
            messages=[
                {
                    "from": "sender@example.com",
                    "to": ["recipient1@example.com"],
                    "attachments": [
                        {
                            "content": "content",
                            "content_id": "content_id",
                            "content_type": "content_type",
                            "disposition": "disposition",
                            "filename": "filename",
                        }
                    ],
                    "bcc": ["string"],
                    "cc": ["string"],
                    "from_name": "from_name",
                    "group_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "headers": {"foo": "string"},
                    "html_body": "html_body",
                    "ignore_suppression": True,
                    "inline_css": True,
                    "metadata": {"foo": "bar"},
                    "reply_to": "string",
                    "sandbox_mode": True,
                    "scheduled_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "send_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "subject": "Hello 1",
                    "tags": ["string"],
                    "template_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "template_variables": {"foo": "bar"},
                    "text_body": "Message 1",
                    "tracking_settings": {
                        "click_tracking": True,
                        "open_tracking": True,
                    },
                },
                {
                    "from": "sender@example.com",
                    "to": ["recipient2@example.com"],
                    "attachments": [
                        {
                            "content": "content",
                            "content_id": "content_id",
                            "content_type": "content_type",
                            "disposition": "disposition",
                            "filename": "filename",
                        }
                    ],
                    "bcc": ["string"],
                    "cc": ["string"],
                    "from_name": "from_name",
                    "group_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "headers": {"foo": "string"},
                    "html_body": "html_body",
                    "ignore_suppression": True,
                    "inline_css": True,
                    "metadata": {"foo": "bar"},
                    "reply_to": "string",
                    "sandbox_mode": True,
                    "scheduled_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "send_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "subject": "Hello 2",
                    "tags": ["string"],
                    "template_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "template_variables": {"foo": "bar"},
                    "text_body": "Message 2",
                    "tracking_settings": {
                        "click_tracking": True,
                        "open_tracking": True,
                    },
                },
            ],
            sandbox_mode=False,
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        )
        assert_matches_type(EmailMessageBatchResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch(self, client: Telnyx) -> None:
        response = client.email_messages.with_raw_response.batch(
            messages=[
                {
                    "from": "sender@example.com",
                    "to": ["recipient1@example.com"],
                },
                {
                    "from": "sender@example.com",
                    "to": ["recipient2@example.com"],
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = response.parse()
        assert_matches_type(EmailMessageBatchResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch(self, client: Telnyx) -> None:
        with client.email_messages.with_streaming_response.batch(
            messages=[
                {
                    "from": "sender@example.com",
                    "to": ["recipient1@example.com"],
                },
                {
                    "from": "sender@example.com",
                    "to": ["recipient2@example.com"],
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = response.parse()
            assert_matches_type(EmailMessageBatchResponse, email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Telnyx) -> None:
        email_message = client.email_messages.delete_all(
            address="dev@stainless.com",
        )
        assert email_message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Telnyx) -> None:
        response = client.email_messages.with_raw_response.delete_all(
            address="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = response.parse()
        assert email_message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Telnyx) -> None:
        with client.email_messages.with_streaming_response.delete_all(
            address="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = response.parse()
            assert email_message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_schedule(self, client: Telnyx) -> None:
        email_message = client.email_messages.delete_schedule(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailMessageResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_schedule(self, client: Telnyx) -> None:
        response = client.email_messages.with_raw_response.delete_schedule(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = response.parse()
        assert_matches_type(EmailMessageResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_schedule(self, client: Telnyx) -> None:
        with client.email_messages.with_streaming_response.delete_schedule(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = response.parse()
            assert_matches_type(EmailMessageResponse, email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_schedule(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.email_messages.with_raw_response.delete_schedule(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_events(self, client: Telnyx) -> None:
        email_message = client.email_messages.retrieve_events(
            email_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncEmailCursorPagination[MessageEvent], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_events_with_all_params(self, client: Telnyx) -> None:
        email_message = client.email_messages.retrieve_events(
            email_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_cursor="page_cursor",
            page_size=1,
        )
        assert_matches_type(SyncEmailCursorPagination[MessageEvent], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_events(self, client: Telnyx) -> None:
        response = client.email_messages.with_raw_response.retrieve_events(
            email_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = response.parse()
        assert_matches_type(SyncEmailCursorPagination[MessageEvent], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_events(self, client: Telnyx) -> None:
        with client.email_messages.with_streaming_response.retrieve_events(
            email_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = response.parse()
            assert_matches_type(SyncEmailCursorPagination[MessageEvent], email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_events(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.email_messages.with_raw_response.retrieve_events(
                email_id="",
            )


class TestAsyncEmailMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.create(
            from_="sender@example.com",
            to=["recipient@example.com"],
        )
        assert_matches_type(EmailMessageResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.create(
            from_="sender@example.com",
            to=["recipient@example.com"],
            attachments=[
                {
                    "content": "content",
                    "content_id": "content_id",
                    "content_type": "content_type",
                    "disposition": "disposition",
                    "filename": "filename",
                }
            ],
            bcc=["string"],
            cc=["string"],
            forward_of_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_name="from_name",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            headers={"foo": "string"},
            html_body="html_body",
            ignore_suppression=True,
            in_reply_to_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inline_css=True,
            metadata={"foo": "bar"},
            reply_to="string",
            reply_to_all=True,
            sandbox_mode=True,
            scheduled_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            send_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            subject="Hello from Telnyx",
            tags=["string"],
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_variables={"foo": "bar"},
            text_body="This is a test email.",
            tracking_settings={
                "click_tracking": True,
                "open_tracking": True,
            },
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        )
        assert_matches_type(EmailMessageResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_messages.with_raw_response.create(
            from_="sender@example.com",
            to=["recipient@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = await response.parse()
        assert_matches_type(EmailMessageResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_messages.with_streaming_response.create(
            from_="sender@example.com",
            to=["recipient@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = await response.parse()
            assert_matches_type(EmailMessageResponse, email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailMessageRetrieveResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_messages.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = await response.parse()
        assert_matches_type(EmailMessageRetrieveResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_messages.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = await response.parse()
            assert_matches_type(EmailMessageRetrieveResponse, email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.list()
        assert_matches_type(AsyncEmailCursorPagination[EmailMessage], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.list(
            page_cursor="page_cursor",
            page_size=1,
        )
        assert_matches_type(AsyncEmailCursorPagination[EmailMessage], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = await response.parse()
        assert_matches_type(AsyncEmailCursorPagination[EmailMessage], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = await response.parse()
            assert_matches_type(AsyncEmailCursorPagination[EmailMessage], email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert email_message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_messages.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = await response.parse()
        assert email_message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_messages.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = await response.parse()
            assert email_message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_messages.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.batch(
            messages=[
                {
                    "from": "sender@example.com",
                    "to": ["recipient1@example.com"],
                },
                {
                    "from": "sender@example.com",
                    "to": ["recipient2@example.com"],
                },
            ],
        )
        assert_matches_type(EmailMessageBatchResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_with_all_params(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.batch(
            messages=[
                {
                    "from": "sender@example.com",
                    "to": ["recipient1@example.com"],
                    "attachments": [
                        {
                            "content": "content",
                            "content_id": "content_id",
                            "content_type": "content_type",
                            "disposition": "disposition",
                            "filename": "filename",
                        }
                    ],
                    "bcc": ["string"],
                    "cc": ["string"],
                    "from_name": "from_name",
                    "group_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "headers": {"foo": "string"},
                    "html_body": "html_body",
                    "ignore_suppression": True,
                    "inline_css": True,
                    "metadata": {"foo": "bar"},
                    "reply_to": "string",
                    "sandbox_mode": True,
                    "scheduled_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "send_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "subject": "Hello 1",
                    "tags": ["string"],
                    "template_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "template_variables": {"foo": "bar"},
                    "text_body": "Message 1",
                    "tracking_settings": {
                        "click_tracking": True,
                        "open_tracking": True,
                    },
                },
                {
                    "from": "sender@example.com",
                    "to": ["recipient2@example.com"],
                    "attachments": [
                        {
                            "content": "content",
                            "content_id": "content_id",
                            "content_type": "content_type",
                            "disposition": "disposition",
                            "filename": "filename",
                        }
                    ],
                    "bcc": ["string"],
                    "cc": ["string"],
                    "from_name": "from_name",
                    "group_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "headers": {"foo": "string"},
                    "html_body": "html_body",
                    "ignore_suppression": True,
                    "inline_css": True,
                    "metadata": {"foo": "bar"},
                    "reply_to": "string",
                    "sandbox_mode": True,
                    "scheduled_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "send_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "subject": "Hello 2",
                    "tags": ["string"],
                    "template_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "template_variables": {"foo": "bar"},
                    "text_body": "Message 2",
                    "tracking_settings": {
                        "click_tracking": True,
                        "open_tracking": True,
                    },
                },
            ],
            sandbox_mode=False,
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        )
        assert_matches_type(EmailMessageBatchResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_messages.with_raw_response.batch(
            messages=[
                {
                    "from": "sender@example.com",
                    "to": ["recipient1@example.com"],
                },
                {
                    "from": "sender@example.com",
                    "to": ["recipient2@example.com"],
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = await response.parse()
        assert_matches_type(EmailMessageBatchResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_messages.with_streaming_response.batch(
            messages=[
                {
                    "from": "sender@example.com",
                    "to": ["recipient1@example.com"],
                },
                {
                    "from": "sender@example.com",
                    "to": ["recipient2@example.com"],
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = await response.parse()
            assert_matches_type(EmailMessageBatchResponse, email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.delete_all(
            address="dev@stainless.com",
        )
        assert email_message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_messages.with_raw_response.delete_all(
            address="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = await response.parse()
        assert email_message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_messages.with_streaming_response.delete_all(
            address="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = await response.parse()
            assert email_message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_schedule(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.delete_schedule(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailMessageResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_schedule(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_messages.with_raw_response.delete_schedule(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = await response.parse()
        assert_matches_type(EmailMessageResponse, email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_schedule(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_messages.with_streaming_response.delete_schedule(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = await response.parse()
            assert_matches_type(EmailMessageResponse, email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_schedule(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.email_messages.with_raw_response.delete_schedule(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.retrieve_events(
            email_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncEmailCursorPagination[MessageEvent], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_events_with_all_params(self, async_client: AsyncTelnyx) -> None:
        email_message = await async_client.email_messages.retrieve_events(
            email_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_cursor="page_cursor",
            page_size=1,
        )
        assert_matches_type(AsyncEmailCursorPagination[MessageEvent], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_messages.with_raw_response.retrieve_events(
            email_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_message = await response.parse()
        assert_matches_type(AsyncEmailCursorPagination[MessageEvent], email_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_messages.with_streaming_response.retrieve_events(
            email_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_message = await response.parse()
            assert_matches_type(AsyncEmailCursorPagination[MessageEvent], email_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.email_messages.with_raw_response.retrieve_events(
                email_id="",
            )
