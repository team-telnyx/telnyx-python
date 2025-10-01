# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .oauth_grant import OAuthGrant

__all__ = ["OAuthGrantRetrieveResponse"]


class OAuthGrantRetrieveResponse(BaseModel):
    data: Optional[OAuthGrant] = None
