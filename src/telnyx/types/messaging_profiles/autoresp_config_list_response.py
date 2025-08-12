# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from .auto_resp_config import AutoRespConfig

__all__ = ["AutorespConfigListResponse"]


class AutorespConfigListResponse(BaseModel):
    data: List[AutoRespConfig]

    meta: PaginationMeta
