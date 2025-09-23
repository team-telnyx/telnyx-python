# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    oauth_token_params,
    oauth_grants_params,
    oauth_register_params,
    oauth_introspect_params,
    oauth_retrieve_authorize_params,
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
from ..types.oauth_token_response import OAuthTokenResponse
from ..types.oauth_grants_response import OAuthGrantsResponse
from ..types.oauth_register_response import OAuthRegisterResponse
from ..types.oauth_retrieve_response import OAuthRetrieveResponse
from ..types.oauth_introspect_response import OAuthIntrospectResponse
from ..types.oauth_retrieve_jwks_response import OAuthRetrieveJwksResponse

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

    def retrieve(
        self,
        consent_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthRetrieveResponse:
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
            cast_to=OAuthRetrieveResponse,
        )

    def grants(
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
    ) -> OAuthGrantsResponse:
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
                oauth_grants_params.OAuthGrantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthGrantsResponse,
        )

    def introspect(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthIntrospectResponse:
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
            body=maybe_transform({"token": token}, oauth_introspect_params.OAuthIntrospectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthIntrospectResponse,
        )

    def register(
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
    ) -> OAuthRegisterResponse:
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
                oauth_register_params.OAuthRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthRegisterResponse,
        )

    def retrieve_authorize(
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
                    oauth_retrieve_authorize_params.OAuthRetrieveAuthorizeParams,
                ),
            ),
            cast_to=NoneType,
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

    def token(
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
    ) -> OAuthTokenResponse:
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
                oauth_token_params.OAuthTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthTokenResponse,
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

    async def retrieve(
        self,
        consent_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthRetrieveResponse:
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
            cast_to=OAuthRetrieveResponse,
        )

    async def grants(
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
    ) -> OAuthGrantsResponse:
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
                oauth_grants_params.OAuthGrantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthGrantsResponse,
        )

    async def introspect(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthIntrospectResponse:
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
            body=await async_maybe_transform({"token": token}, oauth_introspect_params.OAuthIntrospectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthIntrospectResponse,
        )

    async def register(
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
    ) -> OAuthRegisterResponse:
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
                oauth_register_params.OAuthRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthRegisterResponse,
        )

    async def retrieve_authorize(
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
                    oauth_retrieve_authorize_params.OAuthRetrieveAuthorizeParams,
                ),
            ),
            cast_to=NoneType,
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

    async def token(
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
    ) -> OAuthTokenResponse:
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
                oauth_token_params.OAuthTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthTokenResponse,
        )


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.retrieve = to_raw_response_wrapper(
            oauth.retrieve,
        )
        self.grants = to_raw_response_wrapper(
            oauth.grants,
        )
        self.introspect = to_raw_response_wrapper(
            oauth.introspect,
        )
        self.register = to_raw_response_wrapper(
            oauth.register,
        )
        self.retrieve_authorize = to_raw_response_wrapper(
            oauth.retrieve_authorize,
        )
        self.retrieve_jwks = to_raw_response_wrapper(
            oauth.retrieve_jwks,
        )
        self.token = to_raw_response_wrapper(
            oauth.token,
        )


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.retrieve = async_to_raw_response_wrapper(
            oauth.retrieve,
        )
        self.grants = async_to_raw_response_wrapper(
            oauth.grants,
        )
        self.introspect = async_to_raw_response_wrapper(
            oauth.introspect,
        )
        self.register = async_to_raw_response_wrapper(
            oauth.register,
        )
        self.retrieve_authorize = async_to_raw_response_wrapper(
            oauth.retrieve_authorize,
        )
        self.retrieve_jwks = async_to_raw_response_wrapper(
            oauth.retrieve_jwks,
        )
        self.token = async_to_raw_response_wrapper(
            oauth.token,
        )


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.retrieve = to_streamed_response_wrapper(
            oauth.retrieve,
        )
        self.grants = to_streamed_response_wrapper(
            oauth.grants,
        )
        self.introspect = to_streamed_response_wrapper(
            oauth.introspect,
        )
        self.register = to_streamed_response_wrapper(
            oauth.register,
        )
        self.retrieve_authorize = to_streamed_response_wrapper(
            oauth.retrieve_authorize,
        )
        self.retrieve_jwks = to_streamed_response_wrapper(
            oauth.retrieve_jwks,
        )
        self.token = to_streamed_response_wrapper(
            oauth.token,
        )


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.retrieve = async_to_streamed_response_wrapper(
            oauth.retrieve,
        )
        self.grants = async_to_streamed_response_wrapper(
            oauth.grants,
        )
        self.introspect = async_to_streamed_response_wrapper(
            oauth.introspect,
        )
        self.register = async_to_streamed_response_wrapper(
            oauth.register,
        )
        self.retrieve_authorize = async_to_streamed_response_wrapper(
            oauth.retrieve_authorize,
        )
        self.retrieve_jwks = async_to_streamed_response_wrapper(
            oauth.retrieve_jwks,
        )
        self.token = async_to_streamed_response_wrapper(
            oauth.token,
        )
