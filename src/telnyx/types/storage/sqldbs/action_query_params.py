# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ActionQueryParams"]


class ActionQueryParams(TypedDict, total=False):
    sql: Required[str]
    """The SQL to run.

    Use positional `?` placeholders and supply the values in `params` rather than
    interpolating them into this string.
    """

    params: SequenceNotStr[Union[str, float, bool, None]]
    """Positional bind parameters, in placeholder order.

    Each value is a string, a number, a boolean, or null; booleans are cast to
    `1`/`0`. The count must match the number of `?` placeholders exactly — a
    mismatch is rejected with 422 rather than binding null for the ones you left
    out. (Not enforced for multi-statement scripts or named parameters, where the
    placeholder count is not the number bound.)
    """
