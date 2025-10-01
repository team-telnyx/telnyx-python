# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .oauth_client import OAuthClient

__all__ = ["OAuthClientCreateResponse"]


class OAuthClientCreateResponse(BaseModel):
    data: Optional[OAuthClient] = None
