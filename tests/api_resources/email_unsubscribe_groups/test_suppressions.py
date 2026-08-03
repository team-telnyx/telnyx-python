# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import EmailBlock, EmailBlockResponse
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSuppressions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        suppression = client.email_unsubscribe_groups.suppressions.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            to="to",
        )
        assert_matches_type(EmailBlockResponse, suppression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.email_unsubscribe_groups.suppressions.with_raw_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert_matches_type(EmailBlockResponse, suppression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.email_unsubscribe_groups.suppressions.with_streaming_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert_matches_type(EmailBlockResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_unsubscribe_groups.suppressions.with_raw_response.create(
                id="",
                to="to",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        suppression = client.email_unsubscribe_groups.suppressions.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncDefaultFlatPagination[EmailBlock], suppression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        suppression = client.email_unsubscribe_groups.suppressions.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(SyncDefaultFlatPagination[EmailBlock], suppression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.email_unsubscribe_groups.suppressions.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[EmailBlock], suppression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.email_unsubscribe_groups.suppressions.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[EmailBlock], suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_unsubscribe_groups.suppressions.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        suppression = client.email_unsubscribe_groups.suppressions.delete(
            email="email",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert suppression is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.email_unsubscribe_groups.suppressions.with_raw_response.delete(
            email="email",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert suppression is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.email_unsubscribe_groups.suppressions.with_streaming_response.delete(
            email="email",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert suppression is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_unsubscribe_groups.suppressions.with_raw_response.delete(
                email="email",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email` but received ''"):
            client.email_unsubscribe_groups.suppressions.with_raw_response.delete(
                email="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSuppressions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        suppression = await async_client.email_unsubscribe_groups.suppressions.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            to="to",
        )
        assert_matches_type(EmailBlockResponse, suppression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_unsubscribe_groups.suppressions.with_raw_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert_matches_type(EmailBlockResponse, suppression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_unsubscribe_groups.suppressions.with_streaming_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert_matches_type(EmailBlockResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_unsubscribe_groups.suppressions.with_raw_response.create(
                id="",
                to="to",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        suppression = await async_client.email_unsubscribe_groups.suppressions.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncDefaultFlatPagination[EmailBlock], suppression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        suppression = await async_client.email_unsubscribe_groups.suppressions.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(AsyncDefaultFlatPagination[EmailBlock], suppression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_unsubscribe_groups.suppressions.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[EmailBlock], suppression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_unsubscribe_groups.suppressions.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[EmailBlock], suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_unsubscribe_groups.suppressions.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        suppression = await async_client.email_unsubscribe_groups.suppressions.delete(
            email="email",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert suppression is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_unsubscribe_groups.suppressions.with_raw_response.delete(
            email="email",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert suppression is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_unsubscribe_groups.suppressions.with_streaming_response.delete(
            email="email",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert suppression is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_unsubscribe_groups.suppressions.with_raw_response.delete(
                email="email",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email` but received ''"):
            await async_client.email_unsubscribe_groups.suppressions.with_raw_response.delete(
                email="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
