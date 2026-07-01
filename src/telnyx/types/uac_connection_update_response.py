# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .uac_connection import UacConnection

__all__ = ["UacConnectionUpdateResponse"]


class UacConnectionUpdateResponse(BaseModel):
    data: Optional[UacConnection] = None
    """
    A UAC (User Agent Client) Connection registers Telnyx to your PBX — the opposite
    of a standard SIP trunk, where the PBX registers to Telnyx. Use UAC when your
    PBX doesn’t support outbound SIP registration or you need Telnyx to maintain the
    registration.
    """
