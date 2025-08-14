# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .insight_template import InsightTemplate

__all__ = ["InsightTemplateDetail"]


class InsightTemplateDetail(BaseModel):
    data: InsightTemplate
