# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .doc_reqs_requirement import DocReqsRequirement

__all__ = ["RequirementRetrieveResponse"]


class RequirementRetrieveResponse(BaseModel):
    data: Optional[DocReqsRequirement] = None
