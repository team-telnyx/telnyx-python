# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.storage.buckets import (
    SslCertificateCreateResponse,
    SslCertificateDeleteResponse,
    SslCertificateRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSslCertificate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        ssl_certificate = client.storage.buckets.ssl_certificate.create(
            bucket_name="",
        )
        assert_matches_type(SslCertificateCreateResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        ssl_certificate = client.storage.buckets.ssl_certificate.create(
            bucket_name="",
            certificate=b"raw file contents",
            private_key=b"raw file contents",
        )
        assert_matches_type(SslCertificateCreateResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.storage.buckets.ssl_certificate.with_raw_response.create(
            bucket_name="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssl_certificate = response.parse()
        assert_matches_type(SslCertificateCreateResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.storage.buckets.ssl_certificate.with_streaming_response.create(
            bucket_name="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssl_certificate = response.parse()
            assert_matches_type(SslCertificateCreateResponse, ssl_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.buckets.ssl_certificate.with_raw_response.create(
                bucket_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        ssl_certificate = client.storage.buckets.ssl_certificate.retrieve(
            "bucketName",
        )
        assert_matches_type(SslCertificateRetrieveResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.storage.buckets.ssl_certificate.with_raw_response.retrieve(
            "bucketName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssl_certificate = response.parse()
        assert_matches_type(SslCertificateRetrieveResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.storage.buckets.ssl_certificate.with_streaming_response.retrieve(
            "bucketName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssl_certificate = response.parse()
            assert_matches_type(SslCertificateRetrieveResponse, ssl_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.buckets.ssl_certificate.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        ssl_certificate = client.storage.buckets.ssl_certificate.delete(
            "bucketName",
        )
        assert_matches_type(SslCertificateDeleteResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.storage.buckets.ssl_certificate.with_raw_response.delete(
            "bucketName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssl_certificate = response.parse()
        assert_matches_type(SslCertificateDeleteResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.storage.buckets.ssl_certificate.with_streaming_response.delete(
            "bucketName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssl_certificate = response.parse()
            assert_matches_type(SslCertificateDeleteResponse, ssl_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.storage.buckets.ssl_certificate.with_raw_response.delete(
                "",
            )


class TestAsyncSslCertificate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        ssl_certificate = await async_client.storage.buckets.ssl_certificate.create(
            bucket_name="",
        )
        assert_matches_type(SslCertificateCreateResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        ssl_certificate = await async_client.storage.buckets.ssl_certificate.create(
            bucket_name="",
            certificate=b"raw file contents",
            private_key=b"raw file contents",
        )
        assert_matches_type(SslCertificateCreateResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.buckets.ssl_certificate.with_raw_response.create(
            bucket_name="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssl_certificate = await response.parse()
        assert_matches_type(SslCertificateCreateResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.buckets.ssl_certificate.with_streaming_response.create(
            bucket_name="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssl_certificate = await response.parse()
            assert_matches_type(SslCertificateCreateResponse, ssl_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.buckets.ssl_certificate.with_raw_response.create(
                bucket_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        ssl_certificate = await async_client.storage.buckets.ssl_certificate.retrieve(
            "bucketName",
        )
        assert_matches_type(SslCertificateRetrieveResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.buckets.ssl_certificate.with_raw_response.retrieve(
            "bucketName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssl_certificate = await response.parse()
        assert_matches_type(SslCertificateRetrieveResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.buckets.ssl_certificate.with_streaming_response.retrieve(
            "bucketName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssl_certificate = await response.parse()
            assert_matches_type(SslCertificateRetrieveResponse, ssl_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.buckets.ssl_certificate.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        ssl_certificate = await async_client.storage.buckets.ssl_certificate.delete(
            "bucketName",
        )
        assert_matches_type(SslCertificateDeleteResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.buckets.ssl_certificate.with_raw_response.delete(
            "bucketName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ssl_certificate = await response.parse()
        assert_matches_type(SslCertificateDeleteResponse, ssl_certificate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.buckets.ssl_certificate.with_streaming_response.delete(
            "bucketName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ssl_certificate = await response.parse()
            assert_matches_type(SslCertificateDeleteResponse, ssl_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.storage.buckets.ssl_certificate.with_raw_response.delete(
                "",
            )
