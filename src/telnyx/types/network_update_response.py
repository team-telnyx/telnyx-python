# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .network import Network
from .._models import BaseModel

__all__ = ["NetworkUpdateResponse"]


class NetworkUpdateResponse(BaseModel):
    data: Optional[Network] = None
