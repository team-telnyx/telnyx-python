# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .insight_template_group import InsightTemplateGroup

__all__ = ["InsightTemplateGroupDetail"]


class InsightTemplateGroupDetail(BaseModel):
    data: InsightTemplateGroup
