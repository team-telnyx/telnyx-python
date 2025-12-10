# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    OAuthClient,
    OAuthClientCreateResponse,
    OAuthClientUpdateResponse,
    OAuthClientRetrieveResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuthClients:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        oauth_client = client.oauth_clients.create(
            allowed_grant_types=["client_credentials"],
            allowed_scopes=["admin"],
            client_type="public",
            name="My OAuth client",
        )
        assert_matches_type(OAuthClientCreateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        oauth_client = client.oauth_clients.create(
            allowed_grant_types=["client_credentials"],
            allowed_scopes=["admin"],
            client_type="public",
            name="My OAuth client",
            logo_uri="https://example.com",
            policy_uri="https://example.com",
            redirect_uris=["https://example.com"],
            require_pkce=True,
            tos_uri="https://example.com",
        )
        assert_matches_type(OAuthClientCreateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.oauth_clients.with_raw_response.create(
            allowed_grant_types=["client_credentials"],
            allowed_scopes=["admin"],
            client_type="public",
            name="My OAuth client",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert_matches_type(OAuthClientCreateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.oauth_clients.with_streaming_response.create(
            allowed_grant_types=["client_credentials"],
            allowed_scopes=["admin"],
            client_type="public",
            name="My OAuth client",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert_matches_type(OAuthClientCreateResponse, oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        oauth_client = client.oauth_clients.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OAuthClientRetrieveResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.oauth_clients.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert_matches_type(OAuthClientRetrieveResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.oauth_clients.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert_matches_type(OAuthClientRetrieveResponse, oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.oauth_clients.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        oauth_client = client.oauth_clients.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OAuthClientUpdateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        oauth_client = client.oauth_clients.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_grant_types=["client_credentials"],
            allowed_scopes=["admin"],
            logo_uri="https://example.com",
            name="name",
            policy_uri="https://example.com",
            redirect_uris=["https://example.com"],
            require_pkce=True,
            tos_uri="https://example.com",
        )
        assert_matches_type(OAuthClientUpdateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.oauth_clients.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert_matches_type(OAuthClientUpdateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.oauth_clients.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert_matches_type(OAuthClientUpdateResponse, oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.oauth_clients.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        oauth_client = client.oauth_clients.list()
        assert_matches_type(SyncDefaultFlatPagination[OAuthClient], oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        oauth_client = client.oauth_clients.list(
            filter_allowed_grant_types_contains="client_credentials",
            filter_client_id="filter[client_id]",
            filter_client_type="confidential",
            filter_name="filter[name]",
            filter_name_contains="filter[name][contains]",
            filter_verified=True,
            page_number=1,
            page_size=1,
        )
        assert_matches_type(SyncDefaultFlatPagination[OAuthClient], oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.oauth_clients.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[OAuthClient], oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.oauth_clients.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[OAuthClient], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        oauth_client = client.oauth_clients.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert oauth_client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.oauth_clients.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert oauth_client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.oauth_clients.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert oauth_client is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.oauth_clients.with_raw_response.delete(
                "",
            )


class TestAsyncOAuthClients:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        oauth_client = await async_client.oauth_clients.create(
            allowed_grant_types=["client_credentials"],
            allowed_scopes=["admin"],
            client_type="public",
            name="My OAuth client",
        )
        assert_matches_type(OAuthClientCreateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        oauth_client = await async_client.oauth_clients.create(
            allowed_grant_types=["client_credentials"],
            allowed_scopes=["admin"],
            client_type="public",
            name="My OAuth client",
            logo_uri="https://example.com",
            policy_uri="https://example.com",
            redirect_uris=["https://example.com"],
            require_pkce=True,
            tos_uri="https://example.com",
        )
        assert_matches_type(OAuthClientCreateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth_clients.with_raw_response.create(
            allowed_grant_types=["client_credentials"],
            allowed_scopes=["admin"],
            client_type="public",
            name="My OAuth client",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert_matches_type(OAuthClientCreateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth_clients.with_streaming_response.create(
            allowed_grant_types=["client_credentials"],
            allowed_scopes=["admin"],
            client_type="public",
            name="My OAuth client",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert_matches_type(OAuthClientCreateResponse, oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        oauth_client = await async_client.oauth_clients.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OAuthClientRetrieveResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth_clients.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert_matches_type(OAuthClientRetrieveResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth_clients.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert_matches_type(OAuthClientRetrieveResponse, oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.oauth_clients.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        oauth_client = await async_client.oauth_clients.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OAuthClientUpdateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        oauth_client = await async_client.oauth_clients.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_grant_types=["client_credentials"],
            allowed_scopes=["admin"],
            logo_uri="https://example.com",
            name="name",
            policy_uri="https://example.com",
            redirect_uris=["https://example.com"],
            require_pkce=True,
            tos_uri="https://example.com",
        )
        assert_matches_type(OAuthClientUpdateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth_clients.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert_matches_type(OAuthClientUpdateResponse, oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth_clients.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert_matches_type(OAuthClientUpdateResponse, oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.oauth_clients.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        oauth_client = await async_client.oauth_clients.list()
        assert_matches_type(AsyncDefaultFlatPagination[OAuthClient], oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        oauth_client = await async_client.oauth_clients.list(
            filter_allowed_grant_types_contains="client_credentials",
            filter_client_id="filter[client_id]",
            filter_client_type="confidential",
            filter_name="filter[name]",
            filter_name_contains="filter[name][contains]",
            filter_verified=True,
            page_number=1,
            page_size=1,
        )
        assert_matches_type(AsyncDefaultFlatPagination[OAuthClient], oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth_clients.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[OAuthClient], oauth_client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth_clients.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[OAuthClient], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        oauth_client = await async_client.oauth_clients.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert oauth_client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth_clients.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert oauth_client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth_clients.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert oauth_client is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.oauth_clients.with_raw_response.delete(
                "",
            )
