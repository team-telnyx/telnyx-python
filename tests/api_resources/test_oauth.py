# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    OAuthTokenResponse,
    OAuthGrantsResponse,
    OAuthRegisterResponse,
    OAuthRetrieveResponse,
    OAuthIntrospectResponse,
    OAuthRetrieveJwksResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        oauth = client.oauth.retrieve(
            "consent_token",
        )
        assert_matches_type(OAuthRetrieveResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.retrieve(
            "consent_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthRetrieveResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.retrieve(
            "consent_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthRetrieveResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consent_token` but received ''"):
            client.oauth.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_grants(self, client: Telnyx) -> None:
        oauth = client.oauth.grants(
            allowed=True,
            consent_token="consent_token",
        )
        assert_matches_type(OAuthGrantsResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_grants(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.grants(
            allowed=True,
            consent_token="consent_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthGrantsResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_grants(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.grants(
            allowed=True,
            consent_token="consent_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthGrantsResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_introspect(self, client: Telnyx) -> None:
        oauth = client.oauth.introspect(
            token="token",
        )
        assert_matches_type(OAuthIntrospectResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_introspect(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.introspect(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthIntrospectResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_introspect(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.introspect(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthIntrospectResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register(self, client: Telnyx) -> None:
        oauth = client.oauth.register()
        assert_matches_type(OAuthRegisterResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_with_all_params(self, client: Telnyx) -> None:
        oauth = client.oauth.register(
            client_name="My OAuth Application",
            grant_types=["authorization_code"],
            logo_uri="https://example.com",
            policy_uri="https://example.com",
            redirect_uris=["https://example.com/callback"],
            response_types=["string"],
            scope="admin",
            token_endpoint_auth_method="none",
            tos_uri="https://example.com",
        )
        assert_matches_type(OAuthRegisterResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.register()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthRegisterResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.register() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthRegisterResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_authorize(self, client: Telnyx) -> None:
        oauth = client.oauth.retrieve_authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
        )
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_authorize_with_all_params(self, client: Telnyx) -> None:
        oauth = client.oauth.retrieve_authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
            code_challenge="code_challenge",
            code_challenge_method="plain",
            scope="scope",
            state="state",
        )
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_authorize(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.retrieve_authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_authorize(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.retrieve_authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert oauth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_jwks(self, client: Telnyx) -> None:
        oauth = client.oauth.retrieve_jwks()
        assert_matches_type(OAuthRetrieveJwksResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_jwks(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.retrieve_jwks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthRetrieveJwksResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_jwks(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.retrieve_jwks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthRetrieveJwksResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_token(self, client: Telnyx) -> None:
        oauth = client.oauth.token(
            grant_type="client_credentials",
        )
        assert_matches_type(OAuthTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_token_with_all_params(self, client: Telnyx) -> None:
        oauth = client.oauth.token(
            grant_type="client_credentials",
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            code_verifier="code_verifier",
            redirect_uri="https://example.com",
            refresh_token="refresh_token",
            scope="admin",
        )
        assert_matches_type(OAuthTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_token(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.token(
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_token(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.token(
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.retrieve(
            "consent_token",
        )
        assert_matches_type(OAuthRetrieveResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.retrieve(
            "consent_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthRetrieveResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.retrieve(
            "consent_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthRetrieveResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consent_token` but received ''"):
            await async_client.oauth.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_grants(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.grants(
            allowed=True,
            consent_token="consent_token",
        )
        assert_matches_type(OAuthGrantsResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_grants(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.grants(
            allowed=True,
            consent_token="consent_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthGrantsResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_grants(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.grants(
            allowed=True,
            consent_token="consent_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthGrantsResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_introspect(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.introspect(
            token="token",
        )
        assert_matches_type(OAuthIntrospectResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_introspect(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.introspect(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthIntrospectResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_introspect(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.introspect(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthIntrospectResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.register()
        assert_matches_type(OAuthRegisterResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.register(
            client_name="My OAuth Application",
            grant_types=["authorization_code"],
            logo_uri="https://example.com",
            policy_uri="https://example.com",
            redirect_uris=["https://example.com/callback"],
            response_types=["string"],
            scope="admin",
            token_endpoint_auth_method="none",
            tos_uri="https://example.com",
        )
        assert_matches_type(OAuthRegisterResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.register()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthRegisterResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.register() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthRegisterResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_authorize(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.retrieve_authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
        )
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_authorize_with_all_params(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.retrieve_authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
            code_challenge="code_challenge",
            code_challenge_method="plain",
            scope="scope",
            state="state",
        )
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_authorize(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.retrieve_authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_authorize(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.retrieve_authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert oauth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_jwks(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.retrieve_jwks()
        assert_matches_type(OAuthRetrieveJwksResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_jwks(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.retrieve_jwks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthRetrieveJwksResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_jwks(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.retrieve_jwks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthRetrieveJwksResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_token(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.token(
            grant_type="client_credentials",
        )
        assert_matches_type(OAuthTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_token_with_all_params(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.token(
            grant_type="client_credentials",
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            code_verifier="code_verifier",
            redirect_uri="https://example.com",
            refresh_token="refresh_token",
            scope="admin",
        )
        assert_matches_type(OAuthTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_token(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.token(
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_token(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.token(
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True
