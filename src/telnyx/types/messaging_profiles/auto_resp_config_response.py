# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .auto_resp_config import AutoRespConfig

__all__ = ["AutoRespConfigResponse"]


class AutoRespConfigResponse(BaseModel):
    data: AutoRespConfig
