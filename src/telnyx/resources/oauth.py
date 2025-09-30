# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    oauth_authorize_params,
    oauth_create_grant_params,
    oauth_exchange_token_params,
    oauth_register_client_params,
    oauth_introspect_token_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.oauth_create_grant_response import OAuthCreateGrantResponse
from ..types.oauth_retrieve_jwks_response import OAuthRetrieveJwksResponse
from ..types.oauth_exchange_token_response import OAuthExchangeTokenResponse
from ..types.oauth_register_client_response import OAuthRegisterClientResponse
from ..types.oauth_introspect_token_response import OAuthIntrospectTokenResponse
from ..types.oauth_retrieve_consent_response import OAuthRetrieveConsentResponse

__all__ = ["OAuthResource", "AsyncOAuthResource"]


class OAuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return OAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return OAuthResourceWithStreamingResponse(self)

    def authorize(
        self,
        *,
        client_id: str,
        redirect_uri: str,
        response_type: Literal["code"],
        code_challenge: str | Omit = omit,
        code_challenge_method: Literal["plain", "S256"] | Omit = omit,
        scope: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        OAuth 2.0 authorization endpoint for the authorization code flow

        Args:
          client_id: OAuth client identifier

          redirect_uri: Redirect URI

          response_type: OAuth response type

          code_challenge: PKCE code challenge

          code_challenge_method: PKCE code challenge method

          scope: Space-separated list of requested scopes

          state: State parameter for CSRF protection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/oauth/authorize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_id": client_id,
                        "redirect_uri": redirect_uri,
                        "response_type": response_type,
                        "code_challenge": code_challenge,
                        "code_challenge_method": code_challenge_method,
                        "scope": scope,
                        "state": state,
                    },
                    oauth_authorize_params.OAuthAuthorizeParams,
                ),
            ),
            cast_to=NoneType,
        )

    def create_grant(
        self,
        *,
        allowed: bool,
        consent_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthCreateGrantResponse:
        """
        Create an OAuth authorization grant

        Args:
          allowed: Whether the grant is allowed

          consent_token: Consent token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/oauth/grants",
            body=maybe_transform(
                {
                    "allowed": allowed,
                    "consent_token": consent_token,
                },
                oauth_create_grant_params.OAuthCreateGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthCreateGrantResponse,
        )

    def exchange_token(
        self,
        *,
        grant_type: Literal["client_credentials", "authorization_code", "refresh_token"],
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        code: str | Omit = omit,
        code_verifier: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        refresh_token: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthExchangeTokenResponse:
        """
        Exchange authorization code, client credentials, or refresh token for access
        token

        Args:
          grant_type: OAuth 2.0 grant type

          client_id: OAuth client ID (if not using HTTP Basic auth)

          client_secret: OAuth client secret (if not using HTTP Basic auth)

          code: Authorization code (for authorization_code flow)

          code_verifier: PKCE code verifier (for authorization_code flow)

          redirect_uri: Redirect URI (for authorization_code flow)

          refresh_token: Refresh token (for refresh_token flow)

          scope: Space-separated list of requested scopes (for client_credentials)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/oauth/token",
            body=maybe_transform(
                {
                    "grant_type": grant_type,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code,
                    "code_verifier": code_verifier,
                    "redirect_uri": redirect_uri,
                    "refresh_token": refresh_token,
                    "scope": scope,
                },
                oauth_exchange_token_params.OAuthExchangeTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthExchangeTokenResponse,
        )

    def introspect_token(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthIntrospectTokenResponse:
        """
        Introspect an OAuth access token to check its validity and metadata

        Args:
          token: The token to introspect

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/oauth/introspect",
            body=maybe_transform({"token": token}, oauth_introspect_token_params.OAuthIntrospectTokenParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthIntrospectTokenResponse,
        )

    def register_client(
        self,
        *,
        client_name: str | Omit = omit,
        grant_types: List[Literal["authorization_code", "client_credentials", "refresh_token"]] | Omit = omit,
        logo_uri: str | Omit = omit,
        policy_uri: str | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        response_types: SequenceNotStr[str] | Omit = omit,
        scope: str | Omit = omit,
        token_endpoint_auth_method: Literal["none", "client_secret_basic", "client_secret_post"] | Omit = omit,
        tos_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthRegisterClientResponse:
        """
        Register a new OAuth client dynamically (RFC 7591)

        Args:
          client_name: Human-readable string name of the client to be presented to the end-user

          grant_types: Array of OAuth 2.0 grant type strings that the client may use

          logo_uri: URL of the client logo

          policy_uri: URL of the client's privacy policy

          redirect_uris: Array of redirection URI strings for use in redirect-based flows

          response_types: Array of the OAuth 2.0 response type strings that the client may use

          scope: Space-separated string of scope values that the client may use

          token_endpoint_auth_method: Authentication method for the token endpoint

          tos_uri: URL of the client's terms of service

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/oauth/register",
            body=maybe_transform(
                {
                    "client_name": client_name,
                    "grant_types": grant_types,
                    "logo_uri": logo_uri,
                    "policy_uri": policy_uri,
                    "redirect_uris": redirect_uris,
                    "response_types": response_types,
                    "scope": scope,
                    "token_endpoint_auth_method": token_endpoint_auth_method,
                    "tos_uri": tos_uri,
                },
                oauth_register_client_params.OAuthRegisterClientParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthRegisterClientResponse,
        )

    def retrieve_consent(
        self,
        consent_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthRetrieveConsentResponse:
        """
        Retrieve details about an OAuth consent token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not consent_token:
            raise ValueError(f"Expected a non-empty value for `consent_token` but received {consent_token!r}")
        return self._get(
            f"/oauth/consent/{consent_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthRetrieveConsentResponse,
        )

    def retrieve_jwks(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthRetrieveJwksResponse:
        """Retrieve the JSON Web Key Set for token verification"""
        return self._get(
            "/oauth/jwks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthRetrieveJwksResponse,
        )


class AsyncOAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncOAuthResourceWithStreamingResponse(self)

    async def authorize(
        self,
        *,
        client_id: str,
        redirect_uri: str,
        response_type: Literal["code"],
        code_challenge: str | Omit = omit,
        code_challenge_method: Literal["plain", "S256"] | Omit = omit,
        scope: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        OAuth 2.0 authorization endpoint for the authorization code flow

        Args:
          client_id: OAuth client identifier

          redirect_uri: Redirect URI

          response_type: OAuth response type

          code_challenge: PKCE code challenge

          code_challenge_method: PKCE code challenge method

          scope: Space-separated list of requested scopes

          state: State parameter for CSRF protection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/oauth/authorize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "client_id": client_id,
                        "redirect_uri": redirect_uri,
                        "response_type": response_type,
                        "code_challenge": code_challenge,
                        "code_challenge_method": code_challenge_method,
                        "scope": scope,
                        "state": state,
                    },
                    oauth_authorize_params.OAuthAuthorizeParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def create_grant(
        self,
        *,
        allowed: bool,
        consent_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthCreateGrantResponse:
        """
        Create an OAuth authorization grant

        Args:
          allowed: Whether the grant is allowed

          consent_token: Consent token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/oauth/grants",
            body=await async_maybe_transform(
                {
                    "allowed": allowed,
                    "consent_token": consent_token,
                },
                oauth_create_grant_params.OAuthCreateGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthCreateGrantResponse,
        )

    async def exchange_token(
        self,
        *,
        grant_type: Literal["client_credentials", "authorization_code", "refresh_token"],
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        code: str | Omit = omit,
        code_verifier: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        refresh_token: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthExchangeTokenResponse:
        """
        Exchange authorization code, client credentials, or refresh token for access
        token

        Args:
          grant_type: OAuth 2.0 grant type

          client_id: OAuth client ID (if not using HTTP Basic auth)

          client_secret: OAuth client secret (if not using HTTP Basic auth)

          code: Authorization code (for authorization_code flow)

          code_verifier: PKCE code verifier (for authorization_code flow)

          redirect_uri: Redirect URI (for authorization_code flow)

          refresh_token: Refresh token (for refresh_token flow)

          scope: Space-separated list of requested scopes (for client_credentials)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/oauth/token",
            body=await async_maybe_transform(
                {
                    "grant_type": grant_type,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code,
                    "code_verifier": code_verifier,
                    "redirect_uri": redirect_uri,
                    "refresh_token": refresh_token,
                    "scope": scope,
                },
                oauth_exchange_token_params.OAuthExchangeTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthExchangeTokenResponse,
        )

    async def introspect_token(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthIntrospectTokenResponse:
        """
        Introspect an OAuth access token to check its validity and metadata

        Args:
          token: The token to introspect

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/oauth/introspect",
            body=await async_maybe_transform(
                {"token": token}, oauth_introspect_token_params.OAuthIntrospectTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthIntrospectTokenResponse,
        )

    async def register_client(
        self,
        *,
        client_name: str | Omit = omit,
        grant_types: List[Literal["authorization_code", "client_credentials", "refresh_token"]] | Omit = omit,
        logo_uri: str | Omit = omit,
        policy_uri: str | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        response_types: SequenceNotStr[str] | Omit = omit,
        scope: str | Omit = omit,
        token_endpoint_auth_method: Literal["none", "client_secret_basic", "client_secret_post"] | Omit = omit,
        tos_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthRegisterClientResponse:
        """
        Register a new OAuth client dynamically (RFC 7591)

        Args:
          client_name: Human-readable string name of the client to be presented to the end-user

          grant_types: Array of OAuth 2.0 grant type strings that the client may use

          logo_uri: URL of the client logo

          policy_uri: URL of the client's privacy policy

          redirect_uris: Array of redirection URI strings for use in redirect-based flows

          response_types: Array of the OAuth 2.0 response type strings that the client may use

          scope: Space-separated string of scope values that the client may use

          token_endpoint_auth_method: Authentication method for the token endpoint

          tos_uri: URL of the client's terms of service

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/oauth/register",
            body=await async_maybe_transform(
                {
                    "client_name": client_name,
                    "grant_types": grant_types,
                    "logo_uri": logo_uri,
                    "policy_uri": policy_uri,
                    "redirect_uris": redirect_uris,
                    "response_types": response_types,
                    "scope": scope,
                    "token_endpoint_auth_method": token_endpoint_auth_method,
                    "tos_uri": tos_uri,
                },
                oauth_register_client_params.OAuthRegisterClientParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthRegisterClientResponse,
        )

    async def retrieve_consent(
        self,
        consent_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthRetrieveConsentResponse:
        """
        Retrieve details about an OAuth consent token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not consent_token:
            raise ValueError(f"Expected a non-empty value for `consent_token` but received {consent_token!r}")
        return await self._get(
            f"/oauth/consent/{consent_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthRetrieveConsentResponse,
        )

    async def retrieve_jwks(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthRetrieveJwksResponse:
        """Retrieve the JSON Web Key Set for token verification"""
        return await self._get(
            "/oauth/jwks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthRetrieveJwksResponse,
        )


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.authorize = to_raw_response_wrapper(
            oauth.authorize,
        )
        self.create_grant = to_raw_response_wrapper(
            oauth.create_grant,
        )
        self.exchange_token = to_raw_response_wrapper(
            oauth.exchange_token,
        )
        self.introspect_token = to_raw_response_wrapper(
            oauth.introspect_token,
        )
        self.register_client = to_raw_response_wrapper(
            oauth.register_client,
        )
        self.retrieve_consent = to_raw_response_wrapper(
            oauth.retrieve_consent,
        )
        self.retrieve_jwks = to_raw_response_wrapper(
            oauth.retrieve_jwks,
        )


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.authorize = async_to_raw_response_wrapper(
            oauth.authorize,
        )
        self.create_grant = async_to_raw_response_wrapper(
            oauth.create_grant,
        )
        self.exchange_token = async_to_raw_response_wrapper(
            oauth.exchange_token,
        )
        self.introspect_token = async_to_raw_response_wrapper(
            oauth.introspect_token,
        )
        self.register_client = async_to_raw_response_wrapper(
            oauth.register_client,
        )
        self.retrieve_consent = async_to_raw_response_wrapper(
            oauth.retrieve_consent,
        )
        self.retrieve_jwks = async_to_raw_response_wrapper(
            oauth.retrieve_jwks,
        )


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.authorize = to_streamed_response_wrapper(
            oauth.authorize,
        )
        self.create_grant = to_streamed_response_wrapper(
            oauth.create_grant,
        )
        self.exchange_token = to_streamed_response_wrapper(
            oauth.exchange_token,
        )
        self.introspect_token = to_streamed_response_wrapper(
            oauth.introspect_token,
        )
        self.register_client = to_streamed_response_wrapper(
            oauth.register_client,
        )
        self.retrieve_consent = to_streamed_response_wrapper(
            oauth.retrieve_consent,
        )
        self.retrieve_jwks = to_streamed_response_wrapper(
            oauth.retrieve_jwks,
        )


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.authorize = async_to_streamed_response_wrapper(
            oauth.authorize,
        )
        self.create_grant = async_to_streamed_response_wrapper(
            oauth.create_grant,
        )
        self.exchange_token = async_to_streamed_response_wrapper(
            oauth.exchange_token,
        )
        self.introspect_token = async_to_streamed_response_wrapper(
            oauth.introspect_token,
        )
        self.register_client = async_to_streamed_response_wrapper(
            oauth.register_client,
        )
        self.retrieve_consent = async_to_streamed_response_wrapper(
            oauth.retrieve_consent,
        )
        self.retrieve_jwks = async_to_streamed_response_wrapper(
            oauth.retrieve_jwks,
        )
