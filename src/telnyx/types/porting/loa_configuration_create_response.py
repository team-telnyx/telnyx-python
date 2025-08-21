# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .porting_loa_configuration import PortingLoaConfiguration

__all__ = ["LoaConfigurationCreateResponse"]


class LoaConfigurationCreateResponse(BaseModel):
    data: Optional[PortingLoaConfiguration] = None
