# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["CanaryDeployCreateParams", "Rule", "RuleServe", "RuleServeRollout", "RuleMatch"]


class CanaryDeployCreateParams(TypedDict, total=False):
    rules: Iterable[Rule]


class RuleServeRollout(TypedDict, total=False):
    """One slot in a percentage rollout."""

    version_id: Required[str]

    weight: Required[float]


class RuleServe(TypedDict, total=False):
    """What a rule serves when matched.

    Exactly one of:
    - ``version_id`` — serve a specific version
    - ``rollout`` — weighted random across versions; weights must sum to
      less than 100, with the leftover routing to the main version
    """

    rollout: Iterable[RuleServeRollout]

    version_id: str


class RuleMatch(TypedDict, total=False):
    """A single attribute/operator/values check.

    A clause matches when the routing context's value for ``attribute``
    satisfies ``operator`` against any of ``values``.
    """

    attribute: Required[str]
    """Attribute name from the routing context"""

    operator: Required[Literal["in", "not_in", "starts_with"]]
    """Match operator"""

    values: Required[SequenceNotStr[str]]


class Rule(TypedDict, total=False):
    """A targeting rule: ``match`` clauses (AND) gate ``serve``.

    An empty ``match`` is a catch-all (always fires).
    """

    serve: Required[RuleServe]
    """What a rule serves when matched.

    Exactly one of:

    - `version_id` — serve a specific version
    - `rollout` — weighted random across versions; weights must sum to less than
      100, with the leftover routing to the main version
    """

    match: Iterable[RuleMatch]
