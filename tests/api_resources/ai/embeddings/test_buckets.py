# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.embeddings import BucketListResponse, BucketRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuckets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        bucket = client.ai.embeddings.buckets.retrieve(
            "bucket_name",
        )
        assert_matches_type(BucketRetrieveResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.embeddings.buckets.with_raw_response.retrieve(
            "bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert_matches_type(BucketRetrieveResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.embeddings.buckets.with_streaming_response.retrieve(
            "bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert_matches_type(BucketRetrieveResponse, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.ai.embeddings.buckets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        bucket = client.ai.embeddings.buckets.list()
        assert_matches_type(BucketListResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.embeddings.buckets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert_matches_type(BucketListResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.embeddings.buckets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert_matches_type(BucketListResponse, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        bucket = client.ai.embeddings.buckets.delete(
            "bucket_name",
        )
        assert bucket is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.embeddings.buckets.with_raw_response.delete(
            "bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert bucket is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.embeddings.buckets.with_streaming_response.delete(
            "bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert bucket is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.ai.embeddings.buckets.with_raw_response.delete(
                "",
            )


class TestAsyncBuckets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        bucket = await async_client.ai.embeddings.buckets.retrieve(
            "bucket_name",
        )
        assert_matches_type(BucketRetrieveResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.embeddings.buckets.with_raw_response.retrieve(
            "bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert_matches_type(BucketRetrieveResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.embeddings.buckets.with_streaming_response.retrieve(
            "bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert_matches_type(BucketRetrieveResponse, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.ai.embeddings.buckets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        bucket = await async_client.ai.embeddings.buckets.list()
        assert_matches_type(BucketListResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.embeddings.buckets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert_matches_type(BucketListResponse, bucket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.embeddings.buckets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert_matches_type(BucketListResponse, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        bucket = await async_client.ai.embeddings.buckets.delete(
            "bucket_name",
        )
        assert bucket is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.embeddings.buckets.with_raw_response.delete(
            "bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert bucket is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.embeddings.buckets.with_streaming_response.delete(
            "bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert bucket is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.ai.embeddings.buckets.with_raw_response.delete(
                "",
            )
