# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from datetime import datetime

from ...._models import BaseModel
from .rule_output import RuleOutput

__all__ = ["CanaryDeployResponse"]


class CanaryDeployResponse(BaseModel):
    """Response shape.

    Always carries ``rules`` (canonical).
    """

    assistant_id: str

    created_at: datetime

    rules: List[RuleOutput]

    updated_at: datetime
