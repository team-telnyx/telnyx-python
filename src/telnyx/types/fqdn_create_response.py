# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .fqdn import Fqdn
from .._models import BaseModel

__all__ = ["FqdnCreateResponse"]


class FqdnCreateResponse(BaseModel):
    data: Optional[Fqdn] = None
