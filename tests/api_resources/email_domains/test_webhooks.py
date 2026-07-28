# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.email_domains import (
    EmailWebhook,
    EmailWebhookResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        webhook = client.email_domains.webhooks.create(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=["email.sent", "email.delivered", "email.bounced"],
            url="https://example.com/webhooks/email",
        )
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.email_domains.webhooks.with_raw_response.create(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=["email.sent", "email.delivered", "email.bounced"],
            url="https://example.com/webhooks/email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.email_domains.webhooks.with_streaming_response.create(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=["email.sent", "email.delivered", "email.bounced"],
            url="https://example.com/webhooks/email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.email_domains.webhooks.with_raw_response.create(
                domain_id="",
                events=["email.sent", "email.delivered", "email.bounced"],
                url="https://example.com/webhooks/email",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        webhook = client.email_domains.webhooks.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.email_domains.webhooks.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.email_domains.webhooks.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.email_domains.webhooks.with_raw_response.retrieve(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                domain_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_domains.webhooks.with_raw_response.retrieve(
                id="",
                domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        webhook = client.email_domains.webhooks.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        webhook = client.email_domains.webhooks.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=["email.sent", "email.delivered", "email.opened"],
            url="https://example.com",
        )
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.email_domains.webhooks.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.email_domains.webhooks.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.email_domains.webhooks.with_raw_response.update(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                domain_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_domains.webhooks.with_raw_response.update(
                id="",
                domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        webhook = client.email_domains.webhooks.list(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncDefaultFlatPagination[EmailWebhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        webhook = client.email_domains.webhooks.list(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_number=1,
            page_size=1,
            sort="created_at",
        )
        assert_matches_type(SyncDefaultFlatPagination[EmailWebhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.email_domains.webhooks.with_raw_response.list(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[EmailWebhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.email_domains.webhooks.with_streaming_response.list(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[EmailWebhook], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.email_domains.webhooks.with_raw_response.list(
                domain_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        webhook = client.email_domains.webhooks.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.email_domains.webhooks.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.email_domains.webhooks.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.email_domains.webhooks.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                domain_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_domains.webhooks.with_raw_response.delete(
                id="",
                domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        webhook = await async_client.email_domains.webhooks.create(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=["email.sent", "email.delivered", "email.bounced"],
            url="https://example.com/webhooks/email",
        )
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_domains.webhooks.with_raw_response.create(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=["email.sent", "email.delivered", "email.bounced"],
            url="https://example.com/webhooks/email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_domains.webhooks.with_streaming_response.create(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=["email.sent", "email.delivered", "email.bounced"],
            url="https://example.com/webhooks/email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.email_domains.webhooks.with_raw_response.create(
                domain_id="",
                events=["email.sent", "email.delivered", "email.bounced"],
                url="https://example.com/webhooks/email",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        webhook = await async_client.email_domains.webhooks.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_domains.webhooks.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_domains.webhooks.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.email_domains.webhooks.with_raw_response.retrieve(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                domain_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_domains.webhooks.with_raw_response.retrieve(
                id="",
                domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        webhook = await async_client.email_domains.webhooks.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        webhook = await async_client.email_domains.webhooks.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=["email.sent", "email.delivered", "email.opened"],
            url="https://example.com",
        )
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_domains.webhooks.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_domains.webhooks.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.email_domains.webhooks.with_raw_response.update(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                domain_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_domains.webhooks.with_raw_response.update(
                id="",
                domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        webhook = await async_client.email_domains.webhooks.list(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncDefaultFlatPagination[EmailWebhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        webhook = await async_client.email_domains.webhooks.list(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_number=1,
            page_size=1,
            sort="created_at",
        )
        assert_matches_type(AsyncDefaultFlatPagination[EmailWebhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_domains.webhooks.with_raw_response.list(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[EmailWebhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_domains.webhooks.with_streaming_response.list(
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[EmailWebhook], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.email_domains.webhooks.with_raw_response.list(
                domain_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        webhook = await async_client.email_domains.webhooks.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_domains.webhooks.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_domains.webhooks.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(EmailWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.email_domains.webhooks.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                domain_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_domains.webhooks.with_raw_response.delete(
                id="",
                domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
