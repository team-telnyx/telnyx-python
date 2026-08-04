# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.email_inboxes import (
    FilterAddResponse,
    FilterListResponse,
    FilterReplaceResponse,
    FilterDeleteAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFilters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        filter = client.email_inboxes.filters.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FilterListResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.email_inboxes.filters.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FilterListResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.email_inboxes.filters.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(FilterListResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.filters.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Telnyx) -> None:
        filter = client.email_inboxes.filters.add(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["@spam.example"],
            type="blocklist",
        )
        assert_matches_type(FilterAddResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Telnyx) -> None:
        response = client.email_inboxes.filters.with_raw_response.add(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["@spam.example"],
            type="blocklist",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FilterAddResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Telnyx) -> None:
        with client.email_inboxes.filters.with_streaming_response.add(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["@spam.example"],
            type="blocklist",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(FilterAddResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.filters.with_raw_response.add(
                inbox_id="",
                entries=["@spam.example"],
                type="blocklist",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Telnyx) -> None:
        filter = client.email_inboxes.filters.delete_all(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["former-partner@example.com"],
            type="allowlist",
        )
        assert_matches_type(FilterDeleteAllResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Telnyx) -> None:
        response = client.email_inboxes.filters.with_raw_response.delete_all(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["former-partner@example.com"],
            type="allowlist",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FilterDeleteAllResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Telnyx) -> None:
        with client.email_inboxes.filters.with_streaming_response.delete_all(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["former-partner@example.com"],
            type="allowlist",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(FilterDeleteAllResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_all(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.filters.with_raw_response.delete_all(
                inbox_id="",
                entries=["former-partner@example.com"],
                type="allowlist",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Telnyx) -> None:
        filter = client.email_inboxes.filters.replace(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FilterReplaceResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Telnyx) -> None:
        filter = client.email_inboxes.filters.replace(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowlist=["trusted@example.com", "@partner.example"],
            blocklist=["@spam.example"],
        )
        assert_matches_type(FilterReplaceResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Telnyx) -> None:
        response = client.email_inboxes.filters.with_raw_response.replace(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FilterReplaceResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Telnyx) -> None:
        with client.email_inboxes.filters.with_streaming_response.replace(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(FilterReplaceResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.email_inboxes.filters.with_raw_response.replace(
                inbox_id="",
            )


class TestAsyncFilters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        filter = await async_client.email_inboxes.filters.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FilterListResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.filters.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FilterListResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.filters.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(FilterListResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.filters.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncTelnyx) -> None:
        filter = await async_client.email_inboxes.filters.add(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["@spam.example"],
            type="blocklist",
        )
        assert_matches_type(FilterAddResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.filters.with_raw_response.add(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["@spam.example"],
            type="blocklist",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FilterAddResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.filters.with_streaming_response.add(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["@spam.example"],
            type="blocklist",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(FilterAddResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.filters.with_raw_response.add(
                inbox_id="",
                entries=["@spam.example"],
                type="blocklist",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncTelnyx) -> None:
        filter = await async_client.email_inboxes.filters.delete_all(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["former-partner@example.com"],
            type="allowlist",
        )
        assert_matches_type(FilterDeleteAllResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.filters.with_raw_response.delete_all(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["former-partner@example.com"],
            type="allowlist",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FilterDeleteAllResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.filters.with_streaming_response.delete_all(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entries=["former-partner@example.com"],
            type="allowlist",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(FilterDeleteAllResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.filters.with_raw_response.delete_all(
                inbox_id="",
                entries=["former-partner@example.com"],
                type="allowlist",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncTelnyx) -> None:
        filter = await async_client.email_inboxes.filters.replace(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FilterReplaceResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncTelnyx) -> None:
        filter = await async_client.email_inboxes.filters.replace(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowlist=["trusted@example.com", "@partner.example"],
            blocklist=["@spam.example"],
        )
        assert_matches_type(FilterReplaceResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_inboxes.filters.with_raw_response.replace(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FilterReplaceResponse, filter, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_inboxes.filters.with_streaming_response.replace(
            inbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(FilterReplaceResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.email_inboxes.filters.with_raw_response.replace(
                inbox_id="",
            )
