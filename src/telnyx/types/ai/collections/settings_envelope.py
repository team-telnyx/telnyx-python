# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._models import BaseModel
from .retrieval_settings_wrapper import RetrievalSettingsWrapper

__all__ = ["SettingsEnvelope"]


class SettingsEnvelope(BaseModel):
    data: Optional[RetrievalSettingsWrapper] = None
