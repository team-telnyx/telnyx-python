# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["ImportCreateParams"]


class ImportCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The CSV file (Plug.Upload). Missing/non-upload → 400."""

    block_ttl_days: int
    """TTL for imported `manual_block` rows; other reasons get `expires_at: null`.

    Invalid/missing → falls back to 30.
    """
