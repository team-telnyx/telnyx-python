# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .serve import Serve
from .clause import Clause
from ...._models import BaseModel

__all__ = ["RuleOutput"]


class RuleOutput(BaseModel):
    """A targeting rule: ``match`` clauses (AND) gate ``serve``.

    An empty ``match`` is a catch-all (always fires).
    """

    serve: Serve
    """What a rule serves when matched.

    Exactly one of:

    - `version_id` — serve a specific version
    - `rollout` — weighted random across versions; weights must sum to less than
      100, with the leftover routing to the main version
    """

    match: Optional[List[Clause]] = None
