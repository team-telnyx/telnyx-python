# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.storage import CloudfsFilesystemResponseWrapper

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate_meta_token(self, client: Telnyx) -> None:
        action = client.storage.cloudfs.actions.rotate_meta_token(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(CloudfsFilesystemResponseWrapper, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rotate_meta_token(self, client: Telnyx) -> None:
        response = client.storage.cloudfs.actions.with_raw_response.rotate_meta_token(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(CloudfsFilesystemResponseWrapper, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rotate_meta_token(self, client: Telnyx) -> None:
        with client.storage.cloudfs.actions.with_streaming_response.rotate_meta_token(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(CloudfsFilesystemResponseWrapper, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rotate_meta_token(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.storage.cloudfs.actions.with_raw_response.rotate_meta_token(
                id="",
                idempotency_key="Idempotency-Key",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate_meta_token(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.storage.cloudfs.actions.rotate_meta_token(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(CloudfsFilesystemResponseWrapper, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rotate_meta_token(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.cloudfs.actions.with_raw_response.rotate_meta_token(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(CloudfsFilesystemResponseWrapper, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rotate_meta_token(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.cloudfs.actions.with_streaming_response.rotate_meta_token(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(CloudfsFilesystemResponseWrapper, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rotate_meta_token(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.storage.cloudfs.actions.with_raw_response.rotate_meta_token(
                id="",
                idempotency_key="Idempotency-Key",
            )
