# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Clause"]


class Clause(BaseModel):
    """A single attribute/operator/values check.

    A clause matches when the routing context's value for ``attribute``
    satisfies ``operator`` against any of ``values``.
    """

    attribute: str
    """Attribute name from the routing context"""

    operator: Literal["in", "not_in", "starts_with"]
    """Match operator"""

    values: List[str]
