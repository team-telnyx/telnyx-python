# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["BotSessionListResponse", "Data"]


class Data(BaseModel):
    api_v2_token: str
    """API v2 session token for the signed-in user.

    Use it as a bearer token on authenticated endpoints.
    """


class BotSessionListResponse(BaseModel):
    data: Data
