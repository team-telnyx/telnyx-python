# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .fqdn_authentication import FqdnAuthentication

__all__ = ["FqdnAuthenticationPatchAllResponse"]


class FqdnAuthenticationPatchAllResponse(BaseModel):
    data: Optional[FqdnAuthentication] = None
