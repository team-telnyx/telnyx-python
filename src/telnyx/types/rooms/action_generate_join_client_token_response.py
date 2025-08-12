# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ActionGenerateJoinClientTokenResponse", "Data"]


class Data(BaseModel):
    token: Optional[str] = None

    refresh_token: Optional[str] = None

    refresh_token_expires_at: Optional[datetime] = None
    """ISO 8601 timestamp when the refresh token expires."""

    token_expires_at: Optional[datetime] = None
    """ISO 8601 timestamp when the token expires."""


class ActionGenerateJoinClientTokenResponse(BaseModel):
    data: Optional[Data] = None
