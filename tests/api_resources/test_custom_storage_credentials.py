# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    CustomStorageCredentialCreateResponse,
    CustomStorageCredentialUpdateResponse,
    CustomStorageCredentialRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomStorageCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        custom_storage_credential = client.custom_storage_credentials.create(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        )
        assert_matches_type(CustomStorageCredentialCreateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        custom_storage_credential = client.custom_storage_credentials.create(
            connection_id="connection_id",
            backend="gcs",
            configuration={
                "bucket": "example-bucket",
                "credentials": "OPAQUE_CREDENTIALS_TOKEN",
            },
        )
        assert_matches_type(CustomStorageCredentialCreateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.custom_storage_credentials.with_raw_response.create(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_storage_credential = response.parse()
        assert_matches_type(CustomStorageCredentialCreateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.custom_storage_credentials.with_streaming_response.create(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_storage_credential = response.parse()
            assert_matches_type(CustomStorageCredentialCreateResponse, custom_storage_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.custom_storage_credentials.with_raw_response.create(
                connection_id="",
                backend="gcs",
                configuration={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        custom_storage_credential = client.custom_storage_credentials.retrieve(
            "connection_id",
        )
        assert_matches_type(CustomStorageCredentialRetrieveResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.custom_storage_credentials.with_raw_response.retrieve(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_storage_credential = response.parse()
        assert_matches_type(CustomStorageCredentialRetrieveResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.custom_storage_credentials.with_streaming_response.retrieve(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_storage_credential = response.parse()
            assert_matches_type(CustomStorageCredentialRetrieveResponse, custom_storage_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.custom_storage_credentials.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        custom_storage_credential = client.custom_storage_credentials.update(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        )
        assert_matches_type(CustomStorageCredentialUpdateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        custom_storage_credential = client.custom_storage_credentials.update(
            connection_id="connection_id",
            backend="gcs",
            configuration={
                "bucket": "example-bucket",
                "credentials": "OPAQUE_CREDENTIALS_TOKEN",
            },
        )
        assert_matches_type(CustomStorageCredentialUpdateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.custom_storage_credentials.with_raw_response.update(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_storage_credential = response.parse()
        assert_matches_type(CustomStorageCredentialUpdateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.custom_storage_credentials.with_streaming_response.update(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_storage_credential = response.parse()
            assert_matches_type(CustomStorageCredentialUpdateResponse, custom_storage_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.custom_storage_credentials.with_raw_response.update(
                connection_id="",
                backend="gcs",
                configuration={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        custom_storage_credential = client.custom_storage_credentials.delete(
            "connection_id",
        )
        assert custom_storage_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.custom_storage_credentials.with_raw_response.delete(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_storage_credential = response.parse()
        assert custom_storage_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.custom_storage_credentials.with_streaming_response.delete(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_storage_credential = response.parse()
            assert custom_storage_credential is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.custom_storage_credentials.with_raw_response.delete(
                "",
            )


class TestAsyncCustomStorageCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        custom_storage_credential = await async_client.custom_storage_credentials.create(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        )
        assert_matches_type(CustomStorageCredentialCreateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        custom_storage_credential = await async_client.custom_storage_credentials.create(
            connection_id="connection_id",
            backend="gcs",
            configuration={
                "bucket": "example-bucket",
                "credentials": "OPAQUE_CREDENTIALS_TOKEN",
            },
        )
        assert_matches_type(CustomStorageCredentialCreateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.custom_storage_credentials.with_raw_response.create(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_storage_credential = await response.parse()
        assert_matches_type(CustomStorageCredentialCreateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.custom_storage_credentials.with_streaming_response.create(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_storage_credential = await response.parse()
            assert_matches_type(CustomStorageCredentialCreateResponse, custom_storage_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.custom_storage_credentials.with_raw_response.create(
                connection_id="",
                backend="gcs",
                configuration={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        custom_storage_credential = await async_client.custom_storage_credentials.retrieve(
            "connection_id",
        )
        assert_matches_type(CustomStorageCredentialRetrieveResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.custom_storage_credentials.with_raw_response.retrieve(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_storage_credential = await response.parse()
        assert_matches_type(CustomStorageCredentialRetrieveResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.custom_storage_credentials.with_streaming_response.retrieve(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_storage_credential = await response.parse()
            assert_matches_type(CustomStorageCredentialRetrieveResponse, custom_storage_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.custom_storage_credentials.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        custom_storage_credential = await async_client.custom_storage_credentials.update(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        )
        assert_matches_type(CustomStorageCredentialUpdateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        custom_storage_credential = await async_client.custom_storage_credentials.update(
            connection_id="connection_id",
            backend="gcs",
            configuration={
                "bucket": "example-bucket",
                "credentials": "OPAQUE_CREDENTIALS_TOKEN",
            },
        )
        assert_matches_type(CustomStorageCredentialUpdateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.custom_storage_credentials.with_raw_response.update(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_storage_credential = await response.parse()
        assert_matches_type(CustomStorageCredentialUpdateResponse, custom_storage_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.custom_storage_credentials.with_streaming_response.update(
            connection_id="connection_id",
            backend="gcs",
            configuration={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_storage_credential = await response.parse()
            assert_matches_type(CustomStorageCredentialUpdateResponse, custom_storage_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.custom_storage_credentials.with_raw_response.update(
                connection_id="",
                backend="gcs",
                configuration={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        custom_storage_credential = await async_client.custom_storage_credentials.delete(
            "connection_id",
        )
        assert custom_storage_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.custom_storage_credentials.with_raw_response.delete(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_storage_credential = await response.parse()
        assert custom_storage_credential is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.custom_storage_credentials.with_streaming_response.delete(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_storage_credential = await response.parse()
            assert custom_storage_credential is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.custom_storage_credentials.with_raw_response.delete(
                "",
            )
