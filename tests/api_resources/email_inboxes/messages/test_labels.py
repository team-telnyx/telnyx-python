# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.email_inboxes.messages import (
    LabelCreateResponse,
    LabelDeleteAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLabels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        label = client.email_inboxes.messages.labels.create(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam", "urgent"],
        )
        assert_matches_type(LabelCreateResponse, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.email_inboxes.messages.labels.with_raw_response.create(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam", "urgent"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(LabelCreateResponse, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.email_inboxes.messages.labels.with_streaming_response.create(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam", "urgent"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(LabelCreateResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.messages.labels.with_raw_response.create(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
                labels=["spam", "urgent"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.email_inboxes.messages.labels.with_raw_response.create(
                message_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                labels=["spam", "urgent"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Telnyx) -> None:
        label = client.email_inboxes.messages.labels.delete_all(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam"],
        )
        assert_matches_type(LabelDeleteAllResponse, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Telnyx) -> None:
        response = client.email_inboxes.messages.labels.with_raw_response.delete_all(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(LabelDeleteAllResponse, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Telnyx) -> None:
        with client.email_inboxes.messages.labels.with_streaming_response.delete_all(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(LabelDeleteAllResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_all(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.messages.labels.with_raw_response.delete_all(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
                labels=["spam"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.email_inboxes.messages.labels.with_raw_response.delete_all(
                message_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                labels=["spam"],
            )


class TestAsyncLabels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        label = await async_client.email_inboxes.messages.labels.create(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam", "urgent"],
        )
        assert_matches_type(LabelCreateResponse, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.messages.labels.with_raw_response.create(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam", "urgent"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(LabelCreateResponse, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.messages.labels.with_streaming_response.create(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam", "urgent"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(LabelCreateResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.messages.labels.with_raw_response.create(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
                labels=["spam", "urgent"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.email_inboxes.messages.labels.with_raw_response.create(
                message_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                labels=["spam", "urgent"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncTelnyx) -> None:
        label = await async_client.email_inboxes.messages.labels.delete_all(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam"],
        )
        assert_matches_type(LabelDeleteAllResponse, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.messages.labels.with_raw_response.delete_all(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(LabelDeleteAllResponse, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.messages.labels.with_streaming_response.delete_all(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            labels=["spam"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(LabelDeleteAllResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.messages.labels.with_raw_response.delete_all(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
                labels=["spam"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.email_inboxes.messages.labels.with_raw_response.delete_all(
                message_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                labels=["spam"],
            )
