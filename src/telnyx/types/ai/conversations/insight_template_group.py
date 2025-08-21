# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from .insight_template import InsightTemplate

__all__ = ["InsightTemplateGroup"]


class InsightTemplateGroup(BaseModel):
    id: str

    created_at: datetime

    name: str

    description: Optional[str] = None

    insights: Optional[List[InsightTemplate]] = None

    webhook: Optional[str] = None
