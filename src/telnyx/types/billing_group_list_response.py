# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .billing_group import BillingGroup
from .pagination_meta import PaginationMeta

__all__ = ["BillingGroupListResponse"]


class BillingGroupListResponse(BaseModel):
    data: Optional[List[BillingGroup]] = None

    meta: Optional[PaginationMeta] = None
