# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["OAuthClientCreateParams"]


class OAuthClientCreateParams(TypedDict, total=False):
    allowed_grant_types: Required[List[Literal["client_credentials", "authorization_code", "refresh_token"]]]
    """List of allowed OAuth grant types"""

    allowed_scopes: Required[SequenceNotStr[str]]
    """List of allowed OAuth scopes"""

    client_type: Required[Literal["public", "confidential"]]
    """OAuth client type"""

    name: Required[str]
    """The name of the OAuth client"""

    logo_uri: str
    """URL of the client logo"""

    policy_uri: str
    """URL of the client's privacy policy"""

    redirect_uris: SequenceNotStr[str]
    """List of redirect URIs (required for authorization_code flow)"""

    require_pkce: bool
    """Whether PKCE (Proof Key for Code Exchange) is required for this client"""

    tos_uri: str
    """URL of the client's terms of service"""
