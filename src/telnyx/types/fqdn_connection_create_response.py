# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .fqdn_connection import FqdnConnection

__all__ = ["FqdnConnectionCreateResponse"]


class FqdnConnectionCreateResponse(BaseModel):
    data: Optional[FqdnConnection] = None
