# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.types.storage.buckets import (
    UsageGetAPIUsageResponse,
    UsageGetBucketUsageResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_api_usage(self, client: Telnyx) -> None:
        usage = client.storage.buckets.usage.get_api_usage(
            bucket_name="",
            filter={
                "end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(UsageGetAPIUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_api_usage(self, client: Telnyx) -> None:
        response = client.storage.buckets.usage.with_raw_response.get_api_usage(
            bucket_name="",
            filter={
                "end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetAPIUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_api_usage(self, client: Telnyx) -> None:
        with client.storage.buckets.usage.with_streaming_response.get_api_usage(
            bucket_name="",
            filter={
                "end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetAPIUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_api_usage(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.buckets.usage.with_raw_response.get_api_usage(
                bucket_name="",
                filter={
                    "end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_bucket_usage(self, client: Telnyx) -> None:
        usage = client.storage.buckets.usage.get_bucket_usage(
            "bucketName",
        )
        assert_matches_type(UsageGetBucketUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_bucket_usage(self, client: Telnyx) -> None:
        response = client.storage.buckets.usage.with_raw_response.get_bucket_usage(
            "bucketName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetBucketUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_bucket_usage(self, client: Telnyx) -> None:
        with client.storage.buckets.usage.with_streaming_response.get_bucket_usage(
            "bucketName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetBucketUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_bucket_usage(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.buckets.usage.with_raw_response.get_bucket_usage(
                "",
            )


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_api_usage(self, async_client: AsyncTelnyx) -> None:
        usage = await async_client.storage.buckets.usage.get_api_usage(
            bucket_name="",
            filter={
                "end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(UsageGetAPIUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_api_usage(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.buckets.usage.with_raw_response.get_api_usage(
            bucket_name="",
            filter={
                "end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetAPIUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_api_usage(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.buckets.usage.with_streaming_response.get_api_usage(
            bucket_name="",
            filter={
                "end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetAPIUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_api_usage(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.buckets.usage.with_raw_response.get_api_usage(
                bucket_name="",
                filter={
                    "end_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "start_time": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_bucket_usage(self, async_client: AsyncTelnyx) -> None:
        usage = await async_client.storage.buckets.usage.get_bucket_usage(
            "bucketName",
        )
        assert_matches_type(UsageGetBucketUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_bucket_usage(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.buckets.usage.with_raw_response.get_bucket_usage(
            "bucketName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetBucketUsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_bucket_usage(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.buckets.usage.with_streaming_response.get_bucket_usage(
            "bucketName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetBucketUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_bucket_usage(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.buckets.usage.with_raw_response.get_bucket_usage(
                "",
            )
