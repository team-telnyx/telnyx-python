# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._models import BaseModel
from .whatsapp_calling_settings_data import WhatsappCallingSettingsData

__all__ = ["CallingSettingUpdateResponse"]


class CallingSettingUpdateResponse(BaseModel):
    data: Optional[WhatsappCallingSettingsData] = None
