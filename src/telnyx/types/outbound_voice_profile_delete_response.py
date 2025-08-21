# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .outbound_voice_profile import OutboundVoiceProfile

__all__ = ["OutboundVoiceProfileDeleteResponse"]


class OutboundVoiceProfileDeleteResponse(BaseModel):
    data: Optional[OutboundVoiceProfile] = None
