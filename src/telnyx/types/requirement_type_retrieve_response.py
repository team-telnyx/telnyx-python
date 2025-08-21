# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.doc_reqs_requirement_type import DocReqsRequirementType

__all__ = ["RequirementTypeRetrieveResponse"]


class RequirementTypeRetrieveResponse(BaseModel):
    data: Optional[DocReqsRequirementType] = None
