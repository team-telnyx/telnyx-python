# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    OAuthCreateGrantResponse,
    OAuthRetrieveJwksResponse,
    OAuthExchangeTokenResponse,
    OAuthRegisterClientResponse,
    OAuthIntrospectTokenResponse,
    OAuthRetrieveConsentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_method_authorize(self, client: Telnyx) -> None:
        oauth = client.oauth.authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
        )
        assert oauth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_method_authorize_with_all_params(self, client: Telnyx) -> None:
        oauth = client.oauth.authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
            code_challenge="code_challenge",
            code_challenge_method="plain",
            scope="scope",
            state="state",
        )
        assert oauth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_raw_response_authorize(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert oauth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_streaming_response_authorize(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.authorize(
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
    def test_method_create_grant(self, client: Telnyx) -> None:
        oauth = client.oauth.create_grant(
            allowed=True,
            consent_token="consent_token",
        )
        assert_matches_type(OAuthCreateGrantResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_grant(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.create_grant(
            allowed=True,
            consent_token="consent_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthCreateGrantResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_grant(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.create_grant(
            allowed=True,
            consent_token="consent_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthCreateGrantResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_exchange_token(self, client: Telnyx) -> None:
        oauth = client.oauth.exchange_token(
            grant_type="client_credentials",
        )
        assert_matches_type(OAuthExchangeTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_exchange_token_with_all_params(self, client: Telnyx) -> None:
        oauth = client.oauth.exchange_token(
            grant_type="client_credentials",
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            code_verifier="code_verifier",
            redirect_uri="https://example.com",
            refresh_token="refresh_token",
            scope="admin",
        )
        assert_matches_type(OAuthExchangeTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_exchange_token(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.exchange_token(
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthExchangeTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_exchange_token(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.exchange_token(
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthExchangeTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_introspect_token(self, client: Telnyx) -> None:
        oauth = client.oauth.introspect_token(
            token="token",
        )
        assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_introspect_token(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.introspect_token(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_introspect_token(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.introspect_token(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_client(self, client: Telnyx) -> None:
        oauth = client.oauth.register_client()
        assert_matches_type(OAuthRegisterClientResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_client_with_all_params(self, client: Telnyx) -> None:
        oauth = client.oauth.register_client(
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
        assert_matches_type(OAuthRegisterClientResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register_client(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.register_client()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthRegisterClientResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register_client(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.register_client() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthRegisterClientResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_consent(self, client: Telnyx) -> None:
        oauth = client.oauth.retrieve_consent(
            "consent_token",
        )
        assert_matches_type(OAuthRetrieveConsentResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_consent(self, client: Telnyx) -> None:
        response = client.oauth.with_raw_response.retrieve_consent(
            "consent_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthRetrieveConsentResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_consent(self, client: Telnyx) -> None:
        with client.oauth.with_streaming_response.retrieve_consent(
            "consent_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthRetrieveConsentResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_consent(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consent_token` but received ''"):
            client.oauth.with_raw_response.retrieve_consent(
                "",
            )

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


class TestAsyncOAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_method_authorize(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
        )
        assert oauth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_method_authorize_with_all_params(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
            code_challenge="code_challenge",
            code_challenge_method="plain",
            scope="scope",
            state="state",
        )
        assert oauth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_raw_response_authorize(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.authorize(
            client_id="client_id",
            redirect_uri="https://example.com",
            response_type="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert oauth is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_streaming_response_authorize(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.authorize(
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
    async def test_method_create_grant(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.create_grant(
            allowed=True,
            consent_token="consent_token",
        )
        assert_matches_type(OAuthCreateGrantResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_grant(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.create_grant(
            allowed=True,
            consent_token="consent_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthCreateGrantResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_grant(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.create_grant(
            allowed=True,
            consent_token="consent_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthCreateGrantResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_exchange_token(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.exchange_token(
            grant_type="client_credentials",
        )
        assert_matches_type(OAuthExchangeTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_exchange_token_with_all_params(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.exchange_token(
            grant_type="client_credentials",
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            code_verifier="code_verifier",
            redirect_uri="https://example.com",
            refresh_token="refresh_token",
            scope="admin",
        )
        assert_matches_type(OAuthExchangeTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_exchange_token(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.exchange_token(
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthExchangeTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_exchange_token(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.exchange_token(
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthExchangeTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_introspect_token(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.introspect_token(
            token="token",
        )
        assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_introspect_token(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.introspect_token(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_introspect_token(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.introspect_token(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_client(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.register_client()
        assert_matches_type(OAuthRegisterClientResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_client_with_all_params(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.register_client(
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
        assert_matches_type(OAuthRegisterClientResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register_client(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.register_client()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthRegisterClientResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register_client(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.register_client() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthRegisterClientResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_consent(self, async_client: AsyncTelnyx) -> None:
        oauth = await async_client.oauth.retrieve_consent(
            "consent_token",
        )
        assert_matches_type(OAuthRetrieveConsentResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_consent(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.oauth.with_raw_response.retrieve_consent(
            "consent_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthRetrieveConsentResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_consent(self, async_client: AsyncTelnyx) -> None:
        async with async_client.oauth.with_streaming_response.retrieve_consent(
            "consent_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthRetrieveConsentResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_consent(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `consent_token` but received ''"):
            await async_client.oauth.with_raw_response.retrieve_consent(
                "",
            )

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
