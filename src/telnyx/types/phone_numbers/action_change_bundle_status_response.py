# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .phone_number_with_voice_settings import PhoneNumberWithVoiceSettings

__all__ = ["ActionChangeBundleStatusResponse"]


class ActionChangeBundleStatusResponse(BaseModel):
    data: Optional[PhoneNumberWithVoiceSettings] = None
