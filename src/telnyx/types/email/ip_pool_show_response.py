# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ip_pool import IPPool
from ..._models import BaseModel

__all__ = ["IPPoolShowResponse"]


class IPPoolShowResponse(BaseModel):
    data: IPPool
    """An account-scoped pool of dedicated IPs.

    Mail uses a pool only when the pool is scoped to the sending domain
    (`domain_id`) or is the account default (`is_default`).
    """
