# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OAuthRegisterResponse"]


class OAuthRegisterResponse(BaseModel):
    client_id: str
    """Unique client identifier"""

    client_id_issued_at: int
    """Unix timestamp of when the client ID was issued"""

    client_name: Optional[str] = None
    """Human-readable client name"""

    client_secret: Optional[str] = None
    """Client secret (only for confidential clients)"""

    grant_types: Optional[List[str]] = None
    """Array of allowed grant types"""

    logo_uri: Optional[str] = None
    """URL of the client logo"""

    policy_uri: Optional[str] = None
    """URL of the client's privacy policy"""

    redirect_uris: Optional[List[str]] = None
    """Array of redirection URIs"""

    response_types: Optional[List[str]] = None
    """Array of allowed response types"""

    scope: Optional[str] = None
    """Space-separated scope values"""

    token_endpoint_auth_method: Optional[str] = None
    """Token endpoint authentication method"""

    tos_uri: Optional[str] = None
    """URL of the client's terms of service"""
