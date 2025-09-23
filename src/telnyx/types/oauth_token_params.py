# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OAuthTokenParams"]


class OAuthTokenParams(TypedDict, total=False):
    grant_type: Required[Literal["client_credentials", "authorization_code", "refresh_token"]]
    """OAuth 2.0 grant type"""

    client_id: str
    """OAuth client ID (if not using HTTP Basic auth)"""

    client_secret: str
    """OAuth client secret (if not using HTTP Basic auth)"""

    code: str
    """Authorization code (for authorization_code flow)"""

    code_verifier: str
    """PKCE code verifier (for authorization_code flow)"""

    redirect_uri: str
    """Redirect URI (for authorization_code flow)"""

    refresh_token: str
    """Refresh token (for refresh_token flow)"""

    scope: str
    """Space-separated list of requested scopes (for client_credentials)"""
