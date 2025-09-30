# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OAuthRetrieveAuthorizeParams"]


class OAuthRetrieveAuthorizeParams(TypedDict, total=False):
    client_id: Required[str]
    """OAuth client identifier"""

    redirect_uri: Required[str]
    """Redirect URI"""

    response_type: Required[Literal["code"]]
    """OAuth response type"""

    code_challenge: str
    """PKCE code challenge"""

    code_challenge_method: Literal["plain", "S256"]
    """PKCE code challenge method"""

    scope: str
    """Space-separated list of requested scopes"""

    state: str
    """State parameter for CSRF protection"""
