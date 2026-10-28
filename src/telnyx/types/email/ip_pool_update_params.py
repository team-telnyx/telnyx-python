# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["IPPoolUpdateParams"]


class IPPoolUpdateParams(TypedDict, total=False):
    domain_id: Optional[str]
    """
    Scope the pool to one of the account's email domains, or `null` to remove the
    scope.
    """

    is_default: bool
    """Set or clear the account default flag. An account can have one default pool."""

    name: str
    """
    Pool name: 1-64 characters of lowercase letters, digits, `.`, `_`, and `-`,
    starting and ending with a letter or digit. Must be unique within the account
    and must not start with `dip_`.
    """
