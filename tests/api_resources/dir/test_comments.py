# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.dir import DirComment, CommentCreateResponse
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        comment = client.dir.comments.create(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            content="Re-uploaded the certificate. New document_id: 89450109-ee35-411c-b5bb-14f1d806fca2.",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        comment = client.dir.comments.create(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            content="Re-uploaded the certificate. New document_id: 89450109-ee35-411c-b5bb-14f1d806fca2.",
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.dir.comments.with_raw_response.create(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            content="Re-uploaded the certificate. New document_id: 89450109-ee35-411c-b5bb-14f1d806fca2.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.dir.comments.with_streaming_response.create(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            content="Re-uploaded the certificate. New document_id: 89450109-ee35-411c-b5bb-14f1d806fca2.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.comments.with_raw_response.create(
                dir_id="",
                content="Re-uploaded the certificate. New document_id: 89450109-ee35-411c-b5bb-14f1d806fca2.",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        comment = client.dir.comments.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(SyncDefaultFlatPagination[DirComment], comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        comment = client.dir.comments.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            comment_type="vetting_comment",
            page_number=1,
            page_size=20,
        )
        assert_matches_type(SyncDefaultFlatPagination[DirComment], comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.dir.comments.with_raw_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[DirComment], comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.dir.comments.with_streaming_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[DirComment], comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.comments.with_raw_response.list(
                dir_id="",
            )


class TestAsyncComments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        comment = await async_client.dir.comments.create(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            content="Re-uploaded the certificate. New document_id: 89450109-ee35-411c-b5bb-14f1d806fca2.",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        comment = await async_client.dir.comments.create(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            content="Re-uploaded the certificate. New document_id: 89450109-ee35-411c-b5bb-14f1d806fca2.",
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.comments.with_raw_response.create(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            content="Re-uploaded the certificate. New document_id: 89450109-ee35-411c-b5bb-14f1d806fca2.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.comments.with_streaming_response.create(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            content="Re-uploaded the certificate. New document_id: 89450109-ee35-411c-b5bb-14f1d806fca2.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.comments.with_raw_response.create(
                dir_id="",
                content="Re-uploaded the certificate. New document_id: 89450109-ee35-411c-b5bb-14f1d806fca2.",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        comment = await async_client.dir.comments.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(AsyncDefaultFlatPagination[DirComment], comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        comment = await async_client.dir.comments.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            comment_type="vetting_comment",
            page_number=1,
            page_size=20,
        )
        assert_matches_type(AsyncDefaultFlatPagination[DirComment], comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.comments.with_raw_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[DirComment], comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.comments.with_streaming_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[DirComment], comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.comments.with_raw_response.list(
                dir_id="",
            )
