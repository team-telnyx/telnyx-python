# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .insight_template import InsightTemplate
from ..assistants.tests.test_suites.meta import Meta

__all__ = ["InsightListResponse"]


class InsightListResponse(BaseModel):
    data: List[InsightTemplate]

    meta: Meta
