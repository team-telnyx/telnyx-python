# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["OAuthRegisterParams"]


class OAuthRegisterParams(TypedDict, total=False):
    client_name: str
    """Human-readable string name of the client to be presented to the end-user"""

    grant_types: List[Literal["authorization_code", "client_credentials", "refresh_token"]]
    """Array of OAuth 2.0 grant type strings that the client may use"""

    logo_uri: str
    """URL of the client logo"""

    policy_uri: str
    """URL of the client's privacy policy"""

    redirect_uris: SequenceNotStr[str]
    """Array of redirection URI strings for use in redirect-based flows"""

    response_types: SequenceNotStr[str]
    """Array of the OAuth 2.0 response type strings that the client may use"""

    scope: str
    """Space-separated string of scope values that the client may use"""

    token_endpoint_auth_method: Literal["none", "client_secret_basic", "client_secret_post"]
    """Authentication method for the token endpoint"""

    tos_uri: str
    """URL of the client's terms of service"""
