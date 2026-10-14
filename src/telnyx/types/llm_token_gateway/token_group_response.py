# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .token_group import TokenGroup

__all__ = ["TokenGroupResponse"]


class TokenGroupResponse(BaseModel):
    data: TokenGroup
