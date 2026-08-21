# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import InboundMessage
from telnyx._utils import parse_datetime
from telnyx.pagination import SyncEmailBracketCursorPagination, AsyncEmailBracketCursorPagination
from telnyx.types.email_inboxes import (
    EmailDraftResponse,
    MessageUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        message = client.email_inboxes.messages.update(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            read_at=True,
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.email_inboxes.messages.with_raw_response.update(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            read_at=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.email_inboxes.messages.with_streaming_response.update(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            read_at=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.messages.with_raw_response.update(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
                read_at=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.email_inboxes.messages.with_raw_response.update(
                message_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                read_at=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        message = client.email_inboxes.messages.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncEmailBracketCursorPagination[InboundMessage], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        message = client.email_inboxes.messages.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_from="filter[from]",
            filter_label="filter[label]",
            filter_read=True,
            filter_received_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_received_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_search="filter[search]",
            filter_subject="filter[subject]",
            filter_unread=True,
            page_after="page[after]",
            page_size=1,
        )
        assert_matches_type(SyncEmailBracketCursorPagination[InboundMessage], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.email_inboxes.messages.with_raw_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncEmailBracketCursorPagination[InboundMessage], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.email_inboxes.messages.with_streaming_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncEmailBracketCursorPagination[InboundMessage], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.messages.with_raw_response.list(
                inbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_drafts(self, client: Telnyx) -> None:
        message = client.email_inboxes.messages.drafts(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailDraftResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_drafts_with_all_params(self, client: Telnyx) -> None:
        message = client.email_inboxes.messages.drafts(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments=[{"foo": "bar"}],
            bcc=["string"],
            cc=["string"],
            from_email="from_email",
            from_name="from_name",
            headers={"foo": "string"},
            html="html",
            html_body="html_body",
            labels=["string"],
            metadata={"foo": "bar"},
            reply_to="reply_to",
            subject="subject",
            tags=["string"],
            text="text",
            text_body="Thanks for the update — I will review today.",
            to=["string"],
        )
        assert_matches_type(EmailDraftResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_drafts(self, client: Telnyx) -> None:
        response = client.email_inboxes.messages.with_raw_response.drafts(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(EmailDraftResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_drafts(self, client: Telnyx) -> None:
        with client.email_inboxes.messages.with_streaming_response.drafts(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(EmailDraftResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_drafts(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.messages.with_raw_response.drafts(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.email_inboxes.messages.with_raw_response.drafts(
                message_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.email_inboxes.messages.update(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            read_at=True,
        )
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.messages.with_raw_response.update(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            read_at=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageUpdateResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.messages.with_streaming_response.update(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            read_at=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageUpdateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.messages.with_raw_response.update(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
                read_at=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.email_inboxes.messages.with_raw_response.update(
                message_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                read_at=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.email_inboxes.messages.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncEmailBracketCursorPagination[InboundMessage], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.email_inboxes.messages.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_from="filter[from]",
            filter_label="filter[label]",
            filter_read=True,
            filter_received_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_received_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_search="filter[search]",
            filter_subject="filter[subject]",
            filter_unread=True,
            page_after="page[after]",
            page_size=1,
        )
        assert_matches_type(AsyncEmailBracketCursorPagination[InboundMessage], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.messages.with_raw_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncEmailBracketCursorPagination[InboundMessage], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.messages.with_streaming_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncEmailBracketCursorPagination[InboundMessage], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.messages.with_raw_response.list(
                inbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_drafts(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.email_inboxes.messages.drafts(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailDraftResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_drafts_with_all_params(self, async_client: AsyncTelnyx) -> None:
        message = await async_client.email_inboxes.messages.drafts(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments=[{"foo": "bar"}],
            bcc=["string"],
            cc=["string"],
            from_email="from_email",
            from_name="from_name",
            headers={"foo": "string"},
            html="html",
            html_body="html_body",
            labels=["string"],
            metadata={"foo": "bar"},
            reply_to="reply_to",
            subject="subject",
            tags=["string"],
            text="text",
            text_body="Thanks for the update — I will review today.",
            to=["string"],
        )
        assert_matches_type(EmailDraftResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_drafts(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.messages.with_raw_response.drafts(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(EmailDraftResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_drafts(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.messages.with_streaming_response.drafts(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(EmailDraftResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_drafts(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.messages.with_raw_response.drafts(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.email_inboxes.messages.with_raw_response.drafts(
                message_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
