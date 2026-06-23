# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .network import Network
from .._models import BaseModel

__all__ = ["NetworkDeleteResponse"]


class NetworkDeleteResponse(BaseModel):
    data: Optional[Network] = None
