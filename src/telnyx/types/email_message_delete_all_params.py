# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmailMessageDeleteAllParams"]


class EmailMessageDeleteAllParams(TypedDict, total=False):
    address: Required[str]
    """Sender or recipient address to delete.

    Matching is trimmed and case-insensitive.
    """
