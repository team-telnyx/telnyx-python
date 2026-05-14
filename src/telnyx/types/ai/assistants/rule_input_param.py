# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .serve_param import ServeParam
from .clause_param import ClauseParam

__all__ = ["RuleInputParam"]


class RuleInputParam(TypedDict, total=False):
    """A targeting rule: ``match`` clauses (AND) gate ``serve``.

    An empty ``match`` is a catch-all (always fires).
    """

    serve: Required[ServeParam]
    """What a rule serves when matched.

    Exactly one of:

    - `version_id` — serve a specific version
    - `rollout` — weighted random across versions; weights must sum to less than
      100, with the leftover routing to the main version
    """

    match: Iterable[ClauseParam]
