# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ClauseParam"]


class ClauseParam(TypedDict, total=False):
    """A single attribute/operator/values check.

    A clause matches when the routing context's value for ``attribute``
    satisfies ``operator`` against any of ``values``.
    """

    attribute: Required[str]
    """Attribute name from the routing context"""

    operator: Required[Literal["in", "not_in", "starts_with"]]
    """Match operator"""

    values: Required[SequenceNotStr[str]]
