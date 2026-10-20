# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai import (
    Avatar,
    AvatarResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvatars:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        avatar = client.ai.avatars.create(
            image_file=b"Example data",
            name="Customer portrait",
        )
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.avatars.with_raw_response.create(
            image_file=b"Example data",
            name="Customer portrait",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.avatars.with_streaming_response.create(
            image_file=b"Example data",
            name="Customer portrait",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert_matches_type(AvatarResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        avatar = client.ai.avatars.retrieve(
            "avatar_0123456789abcdef0123456789abcdef",
        )
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.avatars.with_raw_response.retrieve(
            "avatar_0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.avatars.with_streaming_response.retrieve(
            "avatar_0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert_matches_type(AvatarResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `avatar_id` but received ''"):
            client.ai.avatars.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        avatar = client.ai.avatars.update(
            avatar_id="avatar_0123456789abcdef0123456789abcdef",
            name="Updated portrait",
        )
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.avatars.with_raw_response.update(
            avatar_id="avatar_0123456789abcdef0123456789abcdef",
            name="Updated portrait",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.avatars.with_streaming_response.update(
            avatar_id="avatar_0123456789abcdef0123456789abcdef",
            name="Updated portrait",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert_matches_type(AvatarResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `avatar_id` but received ''"):
            client.ai.avatars.with_raw_response.update(
                avatar_id="",
                name="Updated portrait",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        avatar = client.ai.avatars.list()
        assert_matches_type(SyncDefaultFlatPagination[Avatar], avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        avatar = client.ai.avatars.list(
            filter_avatar_type="stock",
            filter_id="avatar_0123456789abcdef0123456789abcdef",
            filter_name="x",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(SyncDefaultFlatPagination[Avatar], avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.avatars.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[Avatar], avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.avatars.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[Avatar], avatar, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAvatars:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        avatar = await async_client.ai.avatars.create(
            image_file=b"Example data",
            name="Customer portrait",
        )
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.avatars.with_raw_response.create(
            image_file=b"Example data",
            name="Customer portrait",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.avatars.with_streaming_response.create(
            image_file=b"Example data",
            name="Customer portrait",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert_matches_type(AvatarResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        avatar = await async_client.ai.avatars.retrieve(
            "avatar_0123456789abcdef0123456789abcdef",
        )
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.avatars.with_raw_response.retrieve(
            "avatar_0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.avatars.with_streaming_response.retrieve(
            "avatar_0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert_matches_type(AvatarResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `avatar_id` but received ''"):
            await async_client.ai.avatars.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        avatar = await async_client.ai.avatars.update(
            avatar_id="avatar_0123456789abcdef0123456789abcdef",
            name="Updated portrait",
        )
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.avatars.with_raw_response.update(
            avatar_id="avatar_0123456789abcdef0123456789abcdef",
            name="Updated portrait",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert_matches_type(AvatarResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.avatars.with_streaming_response.update(
            avatar_id="avatar_0123456789abcdef0123456789abcdef",
            name="Updated portrait",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert_matches_type(AvatarResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `avatar_id` but received ''"):
            await async_client.ai.avatars.with_raw_response.update(
                avatar_id="",
                name="Updated portrait",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        avatar = await async_client.ai.avatars.list()
        assert_matches_type(AsyncDefaultFlatPagination[Avatar], avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        avatar = await async_client.ai.avatars.list(
            filter_avatar_type="stock",
            filter_id="avatar_0123456789abcdef0123456789abcdef",
            filter_name="x",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(AsyncDefaultFlatPagination[Avatar], avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.avatars.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[Avatar], avatar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.avatars.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[Avatar], avatar, path=["response"])

        assert cast(Any, response.is_closed) is True
