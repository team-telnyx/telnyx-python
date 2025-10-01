# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OAuthClient"]


class OAuthClient(BaseModel):
    client_id: str
    """OAuth client identifier"""

    client_type: Literal["public", "confidential"]
    """OAuth client type"""

    created_at: datetime
    """Timestamp when the client was created"""

    name: str
    """Human-readable name for the OAuth client"""

    org_id: str
    """Organization ID that owns this OAuth client"""

    record_type: Literal["oauth_client"]
    """Record type identifier"""

    require_pkce: bool
    """Whether PKCE (Proof Key for Code Exchange) is required for this client"""

    updated_at: datetime
    """Timestamp when the client was last updated"""

    user_id: str
    """User ID that created this OAuth client"""

    allowed_grant_types: Optional[List[Literal["client_credentials", "authorization_code", "refresh_token"]]] = None
    """List of allowed OAuth grant types"""

    allowed_scopes: Optional[List[str]] = None
    """List of allowed OAuth scopes"""

    client_secret: Optional[str] = None
    """Client secret (only included when available, for confidential clients)"""

    logo_uri: Optional[str] = None
    """URL of the client logo"""

    policy_uri: Optional[str] = None
    """URL of the client's privacy policy"""

    redirect_uris: Optional[List[str]] = None
    """List of allowed redirect URIs"""

    tos_uri: Optional[str] = None
    """URL of the client's terms of service"""
