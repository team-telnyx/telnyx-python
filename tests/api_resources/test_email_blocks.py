# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    EmailBlock,
    EmailBlockResponse,
    EmailBlockRetrieveEventsResponse,
)
from telnyx._utils import parse_datetime
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailBlocks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        email_block = client.email_blocks.create(
            to="to",
        )
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        email_block = client.email_blocks.create(
            to="to",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            from_="from",
        )
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.email_blocks.with_raw_response.create(
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = response.parse()
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.email_blocks.with_streaming_response.create(
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = response.parse()
            assert_matches_type(EmailBlockResponse, email_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        email_block = client.email_blocks.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.email_blocks.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = response.parse()
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.email_blocks.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = response.parse()
            assert_matches_type(EmailBlockResponse, email_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_blocks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        email_block = client.email_blocks.list()
        assert_matches_type(SyncDefaultFlatPagination[EmailBlock], email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        email_block = client.email_blocks.list(
            filter_created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_reason="hard_bounce",
            page_after="page[after]",
            page_before="page[before]",
            page_number=1,
            page_size=1,
            sort="created_at",
        )
        assert_matches_type(SyncDefaultFlatPagination[EmailBlock], email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.email_blocks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[EmailBlock], email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.email_blocks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[EmailBlock], email_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        email_block = client.email_blocks.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.email_blocks.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = response.parse()
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.email_blocks.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = response.parse()
            assert_matches_type(EmailBlockResponse, email_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_blocks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_events(self, client: Telnyx) -> None:
        email_block = client.email_blocks.retrieve_events(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailBlockRetrieveEventsResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_events_with_all_params(self, client: Telnyx) -> None:
        email_block = client.email_blocks.retrieve_events(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(EmailBlockRetrieveEventsResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_events(self, client: Telnyx) -> None:
        response = client.email_blocks.with_raw_response.retrieve_events(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = response.parse()
        assert_matches_type(EmailBlockRetrieveEventsResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_events(self, client: Telnyx) -> None:
        with client.email_blocks.with_streaming_response.retrieve_events(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = response.parse()
            assert_matches_type(EmailBlockRetrieveEventsResponse, email_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_events(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_blocks.with_raw_response.retrieve_events(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_export(self, client: Telnyx) -> None:
        email_block = client.email_blocks.retrieve_export()
        assert_matches_type(str, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_export_with_all_params(self, client: Telnyx) -> None:
        email_block = client.email_blocks.retrieve_export(
            filter_created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_reason="hard_bounce",
            page_number=1,
            page_size=1,
            sort="created_at",
        )
        assert_matches_type(str, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_export(self, client: Telnyx) -> None:
        response = client.email_blocks.with_raw_response.retrieve_export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = response.parse()
        assert_matches_type(str, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_export(self, client: Telnyx) -> None:
        with client.email_blocks.with_streaming_response.retrieve_export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = response.parse()
            assert_matches_type(str, email_block, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmailBlocks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        email_block = await async_client.email_blocks.create(
            to="to",
        )
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        email_block = await async_client.email_blocks.create(
            to="to",
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            from_="from",
        )
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_blocks.with_raw_response.create(
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = await response.parse()
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_blocks.with_streaming_response.create(
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = await response.parse()
            assert_matches_type(EmailBlockResponse, email_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        email_block = await async_client.email_blocks.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_blocks.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = await response.parse()
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_blocks.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = await response.parse()
            assert_matches_type(EmailBlockResponse, email_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_blocks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        email_block = await async_client.email_blocks.list()
        assert_matches_type(AsyncDefaultFlatPagination[EmailBlock], email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        email_block = await async_client.email_blocks.list(
            filter_created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_reason="hard_bounce",
            page_after="page[after]",
            page_before="page[before]",
            page_number=1,
            page_size=1,
            sort="created_at",
        )
        assert_matches_type(AsyncDefaultFlatPagination[EmailBlock], email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_blocks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[EmailBlock], email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_blocks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[EmailBlock], email_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        email_block = await async_client.email_blocks.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_blocks.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = await response.parse()
        assert_matches_type(EmailBlockResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_blocks.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = await response.parse()
            assert_matches_type(EmailBlockResponse, email_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_blocks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        email_block = await async_client.email_blocks.retrieve_events(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailBlockRetrieveEventsResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_events_with_all_params(self, async_client: AsyncTelnyx) -> None:
        email_block = await async_client.email_blocks.retrieve_events(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(EmailBlockRetrieveEventsResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_blocks.with_raw_response.retrieve_events(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = await response.parse()
        assert_matches_type(EmailBlockRetrieveEventsResponse, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_blocks.with_streaming_response.retrieve_events(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = await response.parse()
            assert_matches_type(EmailBlockRetrieveEventsResponse, email_block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_blocks.with_raw_response.retrieve_events(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_export(self, async_client: AsyncTelnyx) -> None:
        email_block = await async_client.email_blocks.retrieve_export()
        assert_matches_type(str, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_export_with_all_params(self, async_client: AsyncTelnyx) -> None:
        email_block = await async_client.email_blocks.retrieve_export(
            filter_created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_reason="hard_bounce",
            page_number=1,
            page_size=1,
            sort="created_at",
        )
        assert_matches_type(str, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_export(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_blocks.with_raw_response.retrieve_export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_block = await response.parse()
        assert_matches_type(str, email_block, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_export(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_blocks.with_streaming_response.retrieve_export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_block = await response.parse()
            assert_matches_type(str, email_block, path=["response"])

        assert cast(Any, response.is_closed) is True
