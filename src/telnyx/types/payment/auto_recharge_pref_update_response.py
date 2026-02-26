# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .auto_recharge_pref import AutoRechargePref

__all__ = ["AutoRechargePrefUpdateResponse"]


class AutoRechargePrefUpdateResponse(BaseModel):
    data: Optional[AutoRechargePref] = None
