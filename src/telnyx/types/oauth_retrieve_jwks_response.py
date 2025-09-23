# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OAuthRetrieveJwksResponse", "Key"]


class Key(BaseModel):
    alg: Optional[str] = None
    """Algorithm"""

    kid: Optional[str] = None
    """Key ID"""

    kty: Optional[str] = None
    """Key type"""

    use: Optional[str] = None
    """Key use"""


class OAuthRetrieveJwksResponse(BaseModel):
    keys: Optional[List[Key]] = None
