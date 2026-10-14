# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .token_key import TokenKey

__all__ = ["TokenKeyResponse"]


class TokenKeyResponse(BaseModel):
    data: TokenKey
