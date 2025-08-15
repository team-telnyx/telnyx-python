# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .voicemail_pref_response import VoicemailPrefResponse

__all__ = ["VoicemailCreateResponse"]


class VoicemailCreateResponse(BaseModel):
    data: Optional[VoicemailPrefResponse] = None
