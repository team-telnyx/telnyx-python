# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .porting_loa_configuration import PortingLoaConfiguration

__all__ = ["LoaConfigurationUpdateResponse"]


class LoaConfigurationUpdateResponse(BaseModel):
    data: Optional[PortingLoaConfiguration] = None
