# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._models import BaseModel
from .waba_settings import WabaSettings

__all__ = ["SettingRetrieveResponse"]


class SettingRetrieveResponse(BaseModel):
    data: Optional[WabaSettings] = None
