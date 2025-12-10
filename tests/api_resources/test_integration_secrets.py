# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    IntegrationSecretListResponse,
    IntegrationSecretCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrationSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        integration_secret = client.integration_secrets.create(
            identifier="my_secret",
            type="bearer",
        )
        assert_matches_type(IntegrationSecretCreateResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        integration_secret = client.integration_secrets.create(
            identifier="my_secret",
            type="bearer",
            token="my_secret_value",
            password="password",
            username="username",
        )
        assert_matches_type(IntegrationSecretCreateResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.integration_secrets.with_raw_response.create(
            identifier="my_secret",
            type="bearer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_secret = response.parse()
        assert_matches_type(IntegrationSecretCreateResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.integration_secrets.with_streaming_response.create(
            identifier="my_secret",
            type="bearer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_secret = response.parse()
            assert_matches_type(IntegrationSecretCreateResponse, integration_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        integration_secret = client.integration_secrets.list()
        assert_matches_type(IntegrationSecretListResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        integration_secret = client.integration_secrets.list(
            filter={"type": "bearer"},
            page={
                "number": 1,
                "size": 25,
            },
        )
        assert_matches_type(IntegrationSecretListResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.integration_secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_secret = response.parse()
        assert_matches_type(IntegrationSecretListResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.integration_secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_secret = response.parse()
            assert_matches_type(IntegrationSecretListResponse, integration_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        integration_secret = client.integration_secrets.delete(
            "id",
        )
        assert integration_secret is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.integration_secrets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_secret = response.parse()
        assert integration_secret is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.integration_secrets.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_secret = response.parse()
            assert integration_secret is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.integration_secrets.with_raw_response.delete(
                "",
            )


class TestAsyncIntegrationSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        integration_secret = await async_client.integration_secrets.create(
            identifier="my_secret",
            type="bearer",
        )
        assert_matches_type(IntegrationSecretCreateResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        integration_secret = await async_client.integration_secrets.create(
            identifier="my_secret",
            type="bearer",
            token="my_secret_value",
            password="password",
            username="username",
        )
        assert_matches_type(IntegrationSecretCreateResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.integration_secrets.with_raw_response.create(
            identifier="my_secret",
            type="bearer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_secret = await response.parse()
        assert_matches_type(IntegrationSecretCreateResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.integration_secrets.with_streaming_response.create(
            identifier="my_secret",
            type="bearer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_secret = await response.parse()
            assert_matches_type(IntegrationSecretCreateResponse, integration_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        integration_secret = await async_client.integration_secrets.list()
        assert_matches_type(IntegrationSecretListResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        integration_secret = await async_client.integration_secrets.list(
            filter={"type": "bearer"},
            page={
                "number": 1,
                "size": 25,
            },
        )
        assert_matches_type(IntegrationSecretListResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.integration_secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_secret = await response.parse()
        assert_matches_type(IntegrationSecretListResponse, integration_secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.integration_secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_secret = await response.parse()
            assert_matches_type(IntegrationSecretListResponse, integration_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        integration_secret = await async_client.integration_secrets.delete(
            "id",
        )
        assert integration_secret is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.integration_secrets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_secret = await response.parse()
        assert integration_secret is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.integration_secrets.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_secret = await response.parse()
            assert integration_secret is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.integration_secrets.with_raw_response.delete(
                "",
            )
