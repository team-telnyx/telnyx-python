# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from .porting_phone_number_extension import PortingPhoneNumberExtension

__all__ = ["PhoneNumberExtensionListResponse"]


class PhoneNumberExtensionListResponse(BaseModel):
    data: Optional[List[PortingPhoneNumberExtension]] = None

    meta: Optional[PaginationMeta] = None
