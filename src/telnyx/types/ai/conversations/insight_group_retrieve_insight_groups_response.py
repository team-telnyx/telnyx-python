# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .insight_template_group import InsightTemplateGroup
from ..assistants.tests.test_suites.meta import Meta

__all__ = ["InsightGroupRetrieveInsightGroupsResponse"]


class InsightGroupRetrieveInsightGroupsResponse(BaseModel):
    data: List[InsightTemplateGroup]

    meta: Meta
