# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.storage import BucketCreatePresignedURLResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuckets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_presigned_url(self, client: Telnyx) -> None:
        bucket = client.storage.buckets.create_presigned_url(
            object_name="",
            bucket_name="",
        )
        assert_matches_type(BucketCreatePresignedURLResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_presigned_url_with_all_params(self, client: Telnyx) -> None:
        bucket = client.storage.buckets.create_presigned_url(
            object_name="",
            bucket_name="",
            ttl=1,
        )
        assert_matches_type(BucketCreatePresignedURLResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_presigned_url(self, client: Telnyx) -> None:
        response = client.storage.buckets.with_raw_response.create_presigned_url(
            object_name="",
            bucket_name="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert_matches_type(BucketCreatePresignedURLResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_presigned_url(self, client: Telnyx) -> None:
        with client.storage.buckets.with_streaming_response.create_presigned_url(
            object_name="",
            bucket_name="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert_matches_type(BucketCreatePresignedURLResponse, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_presigned_url(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.buckets.with_raw_response.create_presigned_url(
                object_name="",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.storage.buckets.with_raw_response.create_presigned_url(
                object_name="",
                bucket_name="",
            )


class TestAsyncBuckets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_presigned_url(self, async_client: AsyncTelnyx) -> None:
        bucket = await async_client.storage.buckets.create_presigned_url(
            object_name="",
            bucket_name="",
        )
        assert_matches_type(BucketCreatePresignedURLResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_presigned_url_with_all_params(self, async_client: AsyncTelnyx) -> None:
        bucket = await async_client.storage.buckets.create_presigned_url(
            object_name="",
            bucket_name="",
            ttl=1,
        )
        assert_matches_type(BucketCreatePresignedURLResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_presigned_url(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.buckets.with_raw_response.create_presigned_url(
            object_name="",
            bucket_name="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert_matches_type(BucketCreatePresignedURLResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_presigned_url(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.buckets.with_streaming_response.create_presigned_url(
            object_name="",
            bucket_name="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert_matches_type(BucketCreatePresignedURLResponse, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_presigned_url(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.buckets.with_raw_response.create_presigned_url(
                object_name="",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.storage.buckets.with_raw_response.create_presigned_url(
                object_name="",
                bucket_name="",
            )
