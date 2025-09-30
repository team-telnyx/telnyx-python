# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["OAuthCreateGrantResponse"]


class OAuthCreateGrantResponse(BaseModel):
    redirect_uri: str
    """Redirect URI with authorization code or error"""
