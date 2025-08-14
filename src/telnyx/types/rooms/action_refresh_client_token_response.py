# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ActionRefreshClientTokenResponse", "Data"]


class Data(BaseModel):
    token: Optional[str] = None

    token_expires_at: Optional[datetime] = None
    """ISO 8601 timestamp when the token expires."""


class ActionRefreshClientTokenResponse(BaseModel):
    data: Optional[Data] = None
