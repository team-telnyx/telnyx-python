# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from .porting_loa_configuration import PortingLoaConfiguration

__all__ = ["LoaConfigurationListResponse"]


class LoaConfigurationListResponse(BaseModel):
    data: Optional[List[PortingLoaConfiguration]] = None

    meta: Optional[PaginationMeta] = None
