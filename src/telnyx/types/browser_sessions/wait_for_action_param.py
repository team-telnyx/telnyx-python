# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "WaitForActionParam",
    "Condition",
    "ConditionUnionMember0",
    "ConditionUnionMember1",
    "ConditionUnionMember2",
    "ConditionKind",
]


class ConditionUnionMember0(TypedDict, total=False):
    kind: Required[Literal["url_pattern"]]

    pattern: Required[str]


class ConditionUnionMember1(TypedDict, total=False):
    kind: Required[Literal["ref"]]

    observation_id: Required[str]

    ref: Required[str]


class ConditionUnionMember2(TypedDict, total=False):
    kind: Required[Literal["text"]]

    text: Required[str]


class ConditionKind(TypedDict, total=False):
    kind: Required[Literal["dom_stable"]]


Condition: TypeAlias = Union[ConditionUnionMember0, ConditionUnionMember1, ConditionUnionMember2, ConditionKind]


class WaitForActionParam(TypedDict, total=False):
    """Wait for a condition before continuing."""

    condition: Required[Condition]

    type: Required[Literal["wait_for"]]

    idempotency_key: str

    include_observation: bool

    timeout_ms: int
