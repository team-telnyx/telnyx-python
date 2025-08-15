# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .fqdn import Fqdn
from .._models import BaseModel

__all__ = ["FqdnDeleteResponse"]


class FqdnDeleteResponse(BaseModel):
    data: Optional[Fqdn] = None
