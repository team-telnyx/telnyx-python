# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from .porting_associated_phone_number import PortingAssociatedPhoneNumber

__all__ = ["AssociatedPhoneNumberListResponse"]


class AssociatedPhoneNumberListResponse(BaseModel):
    data: Optional[List[PortingAssociatedPhoneNumber]] = None

    meta: Optional[PaginationMeta] = None
