# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .action_response import ActionResponse

__all__ = ["ActionCreateResponse"]


class ActionCreateResponse(BaseModel):
    data: Optional[ActionResponse] = None
