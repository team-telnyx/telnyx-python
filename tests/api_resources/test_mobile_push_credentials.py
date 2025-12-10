# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    PushCredentialResponse,
    MobilePushCredentialListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMobilePushCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Telnyx) -> None:
        mobile_push_credential = client.mobile_push_credentials.create(
            alias="LucyIosCredential",
            certificate="-----BEGIN CERTIFICATE----- MIIGVDCCBTKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END CERTIFICATE-----",
            private_key="-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END RSA PRIVATE KEY-----",
            type="ios",
        )
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Telnyx) -> None:
        response = client.mobile_push_credentials.with_raw_response.create(
            alias="LucyIosCredential",
            certificate="-----BEGIN CERTIFICATE----- MIIGVDCCBTKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END CERTIFICATE-----",
            private_key="-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END RSA PRIVATE KEY-----",
            type="ios",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_push_credential = response.parse()
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Telnyx) -> None:
        with client.mobile_push_credentials.with_streaming_response.create(
            alias="LucyIosCredential",
            certificate="-----BEGIN CERTIFICATE----- MIIGVDCCBTKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END CERTIFICATE-----",
            private_key="-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END RSA PRIVATE KEY-----",
            type="ios",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_push_credential = response.parse()
            assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Telnyx) -> None:
        mobile_push_credential = client.mobile_push_credentials.create(
            alias="LucyAndroidCredential",
            project_account_json_file={
                "private_key": "bar",
                "client_email": "bar",
            },
            type="android",
        )
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Telnyx) -> None:
        response = client.mobile_push_credentials.with_raw_response.create(
            alias="LucyAndroidCredential",
            project_account_json_file={
                "private_key": "bar",
                "client_email": "bar",
            },
            type="android",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_push_credential = response.parse()
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Telnyx) -> None:
        with client.mobile_push_credentials.with_streaming_response.create(
            alias="LucyAndroidCredential",
            project_account_json_file={
                "private_key": "bar",
                "client_email": "bar",
            },
            type="android",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_push_credential = response.parse()
            assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        mobile_push_credential = client.mobile_push_credentials.retrieve(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        )
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.mobile_push_credentials.with_raw_response.retrieve(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_push_credential = response.parse()
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.mobile_push_credentials.with_streaming_response.retrieve(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_push_credential = response.parse()
            assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `push_credential_id` but received ''"):
            client.mobile_push_credentials.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        mobile_push_credential = client.mobile_push_credentials.list()
        assert_matches_type(MobilePushCredentialListResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        mobile_push_credential = client.mobile_push_credentials.list(
            filter={
                "alias": "LucyCredential",
                "type": "ios",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MobilePushCredentialListResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.mobile_push_credentials.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_push_credential = response.parse()
        assert_matches_type(MobilePushCredentialListResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.mobile_push_credentials.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_push_credential = response.parse()
            assert_matches_type(MobilePushCredentialListResponse, mobile_push_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        mobile_push_credential = client.mobile_push_credentials.delete(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        )
        assert mobile_push_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.mobile_push_credentials.with_raw_response.delete(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_push_credential = response.parse()
        assert mobile_push_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.mobile_push_credentials.with_streaming_response.delete(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_push_credential = response.parse()
            assert mobile_push_credential is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `push_credential_id` but received ''"):
            client.mobile_push_credentials.with_raw_response.delete(
                "",
            )


class TestAsyncMobilePushCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        mobile_push_credential = await async_client.mobile_push_credentials.create(
            alias="LucyIosCredential",
            certificate="-----BEGIN CERTIFICATE----- MIIGVDCCBTKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END CERTIFICATE-----",
            private_key="-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END RSA PRIVATE KEY-----",
            type="ios",
        )
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_push_credentials.with_raw_response.create(
            alias="LucyIosCredential",
            certificate="-----BEGIN CERTIFICATE----- MIIGVDCCBTKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END CERTIFICATE-----",
            private_key="-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END RSA PRIVATE KEY-----",
            type="ios",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_push_credential = await response.parse()
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_push_credentials.with_streaming_response.create(
            alias="LucyIosCredential",
            certificate="-----BEGIN CERTIFICATE----- MIIGVDCCBTKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END CERTIFICATE-----",
            private_key="-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END RSA PRIVATE KEY-----",
            type="ios",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_push_credential = await response.parse()
            assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        mobile_push_credential = await async_client.mobile_push_credentials.create(
            alias="LucyAndroidCredential",
            project_account_json_file={
                "private_key": "bar",
                "client_email": "bar",
            },
            type="android",
        )
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_push_credentials.with_raw_response.create(
            alias="LucyAndroidCredential",
            project_account_json_file={
                "private_key": "bar",
                "client_email": "bar",
            },
            type="android",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_push_credential = await response.parse()
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_push_credentials.with_streaming_response.create(
            alias="LucyAndroidCredential",
            project_account_json_file={
                "private_key": "bar",
                "client_email": "bar",
            },
            type="android",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_push_credential = await response.parse()
            assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        mobile_push_credential = await async_client.mobile_push_credentials.retrieve(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        )
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_push_credentials.with_raw_response.retrieve(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_push_credential = await response.parse()
        assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_push_credentials.with_streaming_response.retrieve(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_push_credential = await response.parse()
            assert_matches_type(PushCredentialResponse, mobile_push_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `push_credential_id` but received ''"):
            await async_client.mobile_push_credentials.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        mobile_push_credential = await async_client.mobile_push_credentials.list()
        assert_matches_type(MobilePushCredentialListResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mobile_push_credential = await async_client.mobile_push_credentials.list(
            filter={
                "alias": "LucyCredential",
                "type": "ios",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MobilePushCredentialListResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_push_credentials.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_push_credential = await response.parse()
        assert_matches_type(MobilePushCredentialListResponse, mobile_push_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_push_credentials.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_push_credential = await response.parse()
            assert_matches_type(MobilePushCredentialListResponse, mobile_push_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        mobile_push_credential = await async_client.mobile_push_credentials.delete(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        )
        assert mobile_push_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_push_credentials.with_raw_response.delete(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_push_credential = await response.parse()
        assert mobile_push_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_push_credentials.with_streaming_response.delete(
            "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_push_credential = await response.parse()
            assert mobile_push_credential is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `push_credential_id` but received ''"):
            await async_client.mobile_push_credentials.with_raw_response.delete(
                "",
            )
