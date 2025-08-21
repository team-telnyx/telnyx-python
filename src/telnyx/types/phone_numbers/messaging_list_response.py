# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from ..shared.phone_number_with_messaging_settings import PhoneNumberWithMessagingSettings

__all__ = ["MessagingListResponse"]


class MessagingListResponse(BaseModel):
    data: Optional[List[PhoneNumberWithMessagingSettings]] = None

    meta: Optional[PaginationMeta] = None
