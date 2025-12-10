# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from .porting_phone_number_block import PortingPhoneNumberBlock

__all__ = ["PhoneNumberBlockListResponse"]


class PhoneNumberBlockListResponse(BaseModel):
    data: Optional[List[PortingPhoneNumberBlock]] = None

    meta: Optional[PaginationMeta] = None
