# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.email_inboxes import (
    ThreadRetrieveResponse,
    InboundThreadListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        thread = client.email_inboxes.threads.retrieve(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ThreadRetrieveResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        thread = client.email_inboxes.threads.retrieve(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_after="page[after]",
            page_size=1,
        )
        assert_matches_type(ThreadRetrieveResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.email_inboxes.threads.with_raw_response.retrieve(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadRetrieveResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.email_inboxes.threads.with_streaming_response.retrieve(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadRetrieveResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.threads.with_raw_response.retrieve(
                thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.email_inboxes.threads.with_raw_response.retrieve(
                thread_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        thread = client.email_inboxes.threads.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InboundThreadListResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        thread = client.email_inboxes.threads.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_label="filter[label]",
            page_after="page[after]",
            page_size=1,
        )
        assert_matches_type(InboundThreadListResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.email_inboxes.threads.with_raw_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(InboundThreadListResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.email_inboxes.threads.with_streaming_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(InboundThreadListResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.threads.with_raw_response.list(
                inbox_id="",
            )


class TestAsyncThreads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        thread = await async_client.email_inboxes.threads.retrieve(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ThreadRetrieveResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        thread = await async_client.email_inboxes.threads.retrieve(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_after="page[after]",
            page_size=1,
        )
        assert_matches_type(ThreadRetrieveResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.threads.with_raw_response.retrieve(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(ThreadRetrieveResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.threads.with_streaming_response.retrieve(
            thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadRetrieveResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.threads.with_raw_response.retrieve(
                thread_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.email_inboxes.threads.with_raw_response.retrieve(
                thread_id="",
                inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        thread = await async_client.email_inboxes.threads.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InboundThreadListResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        thread = await async_client.email_inboxes.threads.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_label="filter[label]",
            page_after="page[after]",
            page_size=1,
        )
        assert_matches_type(InboundThreadListResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.threads.with_raw_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(InboundThreadListResponse, thread, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.threads.with_streaming_response.list(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(InboundThreadListResponse, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.threads.with_raw_response.list(
                inbox_id="",
            )
