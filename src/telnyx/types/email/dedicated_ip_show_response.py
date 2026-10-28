# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .dedicated_ip import DedicatedIP

__all__ = ["DedicatedIPShowResponse"]


class DedicatedIPShowResponse(BaseModel):
    data: DedicatedIP
    """A dedicated sending IP address owned by the account."""
