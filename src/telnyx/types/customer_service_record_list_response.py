# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .customer_service_record import CustomerServiceRecord

__all__ = ["CustomerServiceRecordListResponse"]


class CustomerServiceRecordListResponse(BaseModel):
    data: Optional[List[CustomerServiceRecord]] = None

    meta: Optional[PaginationMeta] = None
