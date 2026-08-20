# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncEmailBracketCursorPagination, AsyncEmailBracketCursorPagination
from telnyx.types.email_inboxes import (
    EmailDraft,
    EmailDraftResponse,
    EmailMessageResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDrafts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        draft = client.email_inboxes.drafts.create(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        draft = client.email_inboxes.drafts.create(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments=[{"foo": "bar"}],
            bcc=["string"],
            cc=["string"],
            from_email="from_email",
            from_name="from_name",
            headers={"foo": "string"},
            html="html",
            html_body="html_body",
            labels=["important"],
            metadata={"foo": "bar"},
            reply_to="reply_to",
            subject="Quarterly update",
            tags=["string"],
            text="text",
            text_body="Here is the update.",
            to=[
                {
                    "email": "recipient@example.com",
                    "name": "Recipient",
                }
            ],
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.email_inboxes.drafts.with_raw_response.create(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.email_inboxes.drafts.with_streaming_response.create(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(EmailDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.create(
                inbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        draft = client.email_inboxes.drafts.retrieve(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.email_inboxes.drafts.with_raw_response.retrieve(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.email_inboxes.drafts.with_streaming_response.retrieve(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(EmailDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.retrieve(
                draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `draft_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.retrieve(
                draft_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        draft = client.email_inboxes.drafts.update(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        draft = client.email_inboxes.drafts.update(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            subject="Quarterly update (revised)",
            tags=["string"],
            text="text",
            text_body="Updated body.",
            to=["string"],
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.email_inboxes.drafts.with_raw_response.update(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.email_inboxes.drafts.with_streaming_response.update(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(EmailDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.update(
                draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `draft_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.update(
                draft_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        draft = client.email_inboxes.drafts.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncEmailBracketCursorPagination[EmailDraft], draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        draft = client.email_inboxes.drafts.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_status="draft",
            page_after="page[after]",
            page_size=1,
        )
        assert_matches_type(SyncEmailBracketCursorPagination[EmailDraft], draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.email_inboxes.drafts.with_raw_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(SyncEmailBracketCursorPagination[EmailDraft], draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.email_inboxes.drafts.with_streaming_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(SyncEmailBracketCursorPagination[EmailDraft], draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.list(
                inbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        draft = client.email_inboxes.drafts.delete(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.email_inboxes.drafts.with_raw_response.delete(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.email_inboxes.drafts.with_streaming_response.delete(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert draft is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.delete(
                draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `draft_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.delete(
                draft_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch(self, client: Telnyx) -> None:
        draft = client.email_inboxes.drafts.patch(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_with_all_params(self, client: Telnyx) -> None:
        draft = client.email_inboxes.drafts.patch(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            subject="Quarterly update (revised)",
            tags=["string"],
            text="text",
            text_body="Updated body.",
            to=["string"],
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_patch(self, client: Telnyx) -> None:
        response = client.email_inboxes.drafts.with_raw_response.patch(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_patch(self, client: Telnyx) -> None:
        with client.email_inboxes.drafts.with_streaming_response.patch(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(EmailDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_patch(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.patch(
                draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `draft_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.patch(
                draft_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: Telnyx) -> None:
        draft = client.email_inboxes.drafts.send(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailMessageResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Telnyx) -> None:
        response = client.email_inboxes.drafts.with_raw_response.send(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(EmailMessageResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Telnyx) -> None:
        with client.email_inboxes.drafts.with_streaming_response.send(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(EmailMessageResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.send(
                draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `draft_id` but received ''"):
            client.email_inboxes.drafts.with_raw_response.send(
                draft_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncDrafts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        draft = await async_client.email_inboxes.drafts.create(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        draft = await async_client.email_inboxes.drafts.create(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments=[{"foo": "bar"}],
            bcc=["string"],
            cc=["string"],
            from_email="from_email",
            from_name="from_name",
            headers={"foo": "string"},
            html="html",
            html_body="html_body",
            labels=["important"],
            metadata={"foo": "bar"},
            reply_to="reply_to",
            subject="Quarterly update",
            tags=["string"],
            text="text",
            text_body="Here is the update.",
            to=[
                {
                    "email": "recipient@example.com",
                    "name": "Recipient",
                }
            ],
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.drafts.with_raw_response.create(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.drafts.with_streaming_response.create(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(EmailDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.create(
                inbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        draft = await async_client.email_inboxes.drafts.retrieve(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.drafts.with_raw_response.retrieve(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.drafts.with_streaming_response.retrieve(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(EmailDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.retrieve(
                draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `draft_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.retrieve(
                draft_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        draft = await async_client.email_inboxes.drafts.update(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        draft = await async_client.email_inboxes.drafts.update(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            subject="Quarterly update (revised)",
            tags=["string"],
            text="text",
            text_body="Updated body.",
            to=["string"],
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.drafts.with_raw_response.update(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.drafts.with_streaming_response.update(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(EmailDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.update(
                draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `draft_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.update(
                draft_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        draft = await async_client.email_inboxes.drafts.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncEmailBracketCursorPagination[EmailDraft], draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        draft = await async_client.email_inboxes.drafts.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_status="draft",
            page_after="page[after]",
            page_size=1,
        )
        assert_matches_type(AsyncEmailBracketCursorPagination[EmailDraft], draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.drafts.with_raw_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(AsyncEmailBracketCursorPagination[EmailDraft], draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.drafts.with_streaming_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(AsyncEmailBracketCursorPagination[EmailDraft], draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.list(
                inbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        draft = await async_client.email_inboxes.drafts.delete(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.drafts.with_raw_response.delete(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.drafts.with_streaming_response.delete(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert draft is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.delete(
                draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `draft_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.delete(
                draft_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch(self, async_client: AsyncTelnyx) -> None:
        draft = await async_client.email_inboxes.drafts.patch(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_with_all_params(self, async_client: AsyncTelnyx) -> None:
        draft = await async_client.email_inboxes.drafts.patch(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            subject="Quarterly update (revised)",
            tags=["string"],
            text="text",
            text_body="Updated body.",
            to=["string"],
        )
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_patch(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.drafts.with_raw_response.patch(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(EmailDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_patch(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.drafts.with_streaming_response.patch(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(EmailDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_patch(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.patch(
                draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `draft_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.patch(
                draft_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncTelnyx) -> None:
        draft = await async_client.email_inboxes.drafts.send(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailMessageResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.drafts.with_raw_response.send(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(EmailMessageResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.drafts.with_streaming_response.send(
            draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(EmailMessageResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.send(
                draft_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `draft_id` but received ''"):
            await async_client.email_inboxes.drafts.with_raw_response.send(
                draft_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
