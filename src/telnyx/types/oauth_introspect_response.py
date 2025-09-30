# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["OAuthIntrospectResponse"]


class OAuthIntrospectResponse(BaseModel):
    active: bool
    """Whether the token is active"""

    aud: Optional[str] = None
    """Audience"""

    client_id: Optional[str] = None
    """Client identifier"""

    exp: Optional[int] = None
    """Expiration timestamp"""

    iat: Optional[int] = None
    """Issued at timestamp"""

    iss: Optional[str] = None
    """Issuer"""

    scope: Optional[str] = None
    """Space-separated list of scopes"""
