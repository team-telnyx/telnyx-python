# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OAuthTokenResponse"]


class OAuthTokenResponse(BaseModel):
    access_token: str
    """The access token"""

    expires_in: int
    """Token lifetime in seconds"""

    token_type: Literal["Bearer"]
    """Token type"""

    refresh_token: Optional[str] = None
    """Refresh token (if applicable)"""

    scope: Optional[str] = None
    """Space-separated list of granted scopes"""
