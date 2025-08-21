# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .fqdn_connection import FqdnConnection

__all__ = ["FqdnConnectionUpdateResponse"]


class FqdnConnectionUpdateResponse(BaseModel):
    data: Optional[FqdnConnection] = None
