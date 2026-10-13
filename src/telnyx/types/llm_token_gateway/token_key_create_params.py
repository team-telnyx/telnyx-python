# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TokenKeyCreateParams"]


class TokenKeyCreateParams(TypedDict, total=False):
    name: Required[str]

    token_group_id: Required[str]

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    allowed_models: Optional[SequenceNotStr[str]]

    blocked: bool

    budget_duration: Optional["BudgetDuration"]

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    max_budget: Optional[float]
    """
    USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
    never binary float accounting.
    """

    max_parallel_requests: Optional[int]
    """Optional maximum concurrent reserved/dispatched cache misses across replicas.

    Null means no concurrency cap. Cache hits do not consume slots; unknown usage
    retains its budget hold without a slot.
    """

    required_end_user_id: bool
    """Require a nonempty caller-asserted end-user ID; not proof of identity."""

    rpm_limit: Optional[int]
    """
    Omitted or null defaults to the maximum (6000) (on a blocked key, null is kept
    until the key is unblocked); a value below the minimum (1) or above the maximum
    is rejected with 400 limit_out_of_range; a malformed value (negative, wrong type
    or precision) is 400 invalid_request. Block the key (blocked: true) to deny it;
    blocking is always accepted.
    """

    token_user_id: Optional[str]

    tpm_limit: Optional[int]
    """
    Omitted or null defaults to the maximum (10000000) (on a blocked key, null is
    kept until the key is unblocked); a value below the minimum (1) or above the
    maximum is rejected with 400 limit_out_of_range; a malformed value (negative,
    wrong type or precision) is 400 invalid_request. Block the key (blocked: true)
    to deny it; blocking is always accepted.
    """


from .budget_duration import BudgetDuration
