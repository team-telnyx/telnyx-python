# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CanaryDeployResponse", "Rule", "RuleServe", "RuleServeRollout", "RuleMatch"]


class RuleServeRollout(BaseModel):
    """One slot in a percentage rollout."""

    version_id: str

    weight: float


class RuleServe(BaseModel):
    """What a rule serves when matched.

    Exactly one of:
    - ``version_id`` — serve a specific version
    - ``rollout`` — weighted random across versions; weights must sum to
      less than 100, with the leftover routing to the main version
    """

    rollout: Optional[List[RuleServeRollout]] = None

    version_id: Optional[str] = None


class RuleMatch(BaseModel):
    """A single attribute/operator/values check.

    A clause matches when the routing context's value for ``attribute``
    satisfies ``operator`` against any of ``values``.
    """

    attribute: str
    """Attribute name from the routing context"""

    operator: Literal["in", "not_in", "starts_with"]
    """Match operator"""

    values: List[str]


class Rule(BaseModel):
    """A targeting rule: ``match`` clauses (AND) gate ``serve``.

    An empty ``match`` is a catch-all (always fires).
    """

    serve: RuleServe
    """What a rule serves when matched.

    Exactly one of:

    - `version_id` — serve a specific version
    - `rollout` — weighted random across versions; weights must sum to less than
      100, with the leftover routing to the main version
    """

    match: Optional[List[RuleMatch]] = None


class CanaryDeployResponse(BaseModel):
    """Response shape.

    Always carries ``rules`` (canonical).
    """

    assistant_id: str

    created_at: datetime

    rules: List[Rule]

    updated_at: datetime
