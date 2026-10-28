# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .dedicated_ip import DedicatedIP

__all__ = ["IPPool", "IP"]


class IP(DedicatedIP):
    """A dedicated IP as a member of a pool, with its routing weight in this pool.

    Weight is a positive integer (default 100).
    """

    weight: Optional[int] = None
    """Relative routing weight of this IP within the pool."""


class IPPool(BaseModel):
    """An account-scoped pool of dedicated IPs.

    Mail uses a pool only when the pool is scoped to the sending domain (`domain_id`) or is the account default (`is_default`).
    """

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    domain_id: Optional[str] = None
    """Email domain this pool is scoped to.

    The pool carries that domain's mail. Null when the pool is not domain-scoped.
    """

    ips: Optional[List[IP]] = None
    """Member IPs with their routing weights.

    Populated by Retrieve an IP pool; list, create, and update responses return an
    empty array.
    """

    is_default: Optional[bool] = None
    """Whether this is the account's default pool.

    The default pool carries mail for sending domains that have no domain-scoped
    pool. At most one per account.
    """

    name: Optional[str] = None
    """Pool name, unique within the account."""

    record_type: Optional[Literal["ip_pool"]] = None

    updated_at: Optional[datetime] = None
