# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .voicemail_pref_response import VoicemailPrefResponse

__all__ = ["VoicemailUpdateResponse"]


class VoicemailUpdateResponse(BaseModel):
    data: Optional[VoicemailPrefResponse] = None
