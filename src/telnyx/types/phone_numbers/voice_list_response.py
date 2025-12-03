# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from .phone_number_with_voice_settings import PhoneNumberWithVoiceSettings

__all__ = ["VoiceListResponse"]


class VoiceListResponse(BaseModel):
    data: Optional[List[PhoneNumberWithVoiceSettings]] = None

    meta: Optional[PaginationMeta] = None
