# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .budget_duration import BudgetDuration

__all__ = ["TokenKey"]


class TokenKey(BaseModel):
    id: str

    allowed_models: Optional[List[str]] = None

    blocked: bool

    budget_duration: Optional[BudgetDuration] = None

    budget_started_at: Optional[datetime] = None

    created_at: datetime

    expires_at: Optional[datetime] = None

    max_budget: Optional[float] = None
    """
    USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
    never binary float accounting.
    """

    name: str

    record_type: Literal["token_key"]

    required_end_user_id: bool
    """Require a nonempty caller-asserted end-user ID; not proof of identity."""

    reserved_spend: float
    """
    USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
    never binary float accounting.
    """

    resets_at: Optional[datetime] = None

    rpm_limit: Optional[int] = None
    """
    Stored key limit; set to the maximum when the key was written without one (on a
    blocked key, null is kept until the key is unblocked).
    """

    spend: float
    """
    USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
    never binary float accounting.
    """

    token_group_id: str

    token_user_id: Optional[str] = None

    tpm_limit: Optional[int] = None
    """
    Stored key limit; set to the maximum when the key was written without one (on a
    blocked key, null is kept until the key is unblocked).
    """

    updated_at: datetime

    version: int

    max_parallel_requests: Optional[int] = None
    """Optional maximum concurrent reserved/dispatched cache misses across replicas.

    Null means no concurrency cap. Cache hits do not consume slots; unknown usage
    retains its budget hold without a slot.
    """

    provisioning: Optional[Literal["ready", "pending", "unavailable", "inactive", "unsupported", "unknown"]] = None
    """Provisioning state of the key's current policy.

    `pending`: retry readiness with bounded backoff (treat `unknown` the same).
    `inactive` and `unsupported` are terminal until the key, group, user or catalog
    changes. `unavailable` means provisioning is stuck and is retried slowly;
    surface it. Absent while the gateway runs in compatibility mode.
    """
