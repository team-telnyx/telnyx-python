# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .outbound_voice_profile import OutboundVoiceProfile

__all__ = ["OutboundVoiceProfileListResponse"]


class OutboundVoiceProfileListResponse(BaseModel):
    data: Optional[List[OutboundVoiceProfile]] = None

    meta: Optional[PaginationMeta] = None
