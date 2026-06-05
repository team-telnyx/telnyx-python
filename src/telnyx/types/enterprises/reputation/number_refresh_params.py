# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["NumberRefreshParams"]


class NumberRefreshParams(TypedDict, total=False):
    phone_numbers: Required[SequenceNotStr[str]]
    """Phone numbers to refresh reputation data for.

    1–100 numbers per request, each in E.164 format. Reputation refreshes are
    subject to per-enterprise rate limits.
    """
