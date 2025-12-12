# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .mobile_voice_connection import MobileVoiceConnection

__all__ = ["MobileVoiceConnectionCreateResponse"]


class MobileVoiceConnectionCreateResponse(BaseModel):
    data: Optional[MobileVoiceConnection] = None
