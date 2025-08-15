# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from ..porting_orders_activation_job import PortingOrdersActivationJob

__all__ = ["ActivationJobListResponse"]


class ActivationJobListResponse(BaseModel):
    data: Optional[List[PortingOrdersActivationJob]] = None

    meta: Optional[PaginationMeta] = None
