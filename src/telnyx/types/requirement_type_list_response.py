# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .shared.doc_reqs_requirement_type import DocReqsRequirementType

__all__ = ["RequirementTypeListResponse"]


class RequirementTypeListResponse(BaseModel):
    data: Optional[List[DocReqsRequirementType]] = None

    meta: Optional[PaginationMeta] = None
