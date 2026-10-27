# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AiagentListParams"]


class AiagentListParams(TypedDict, total=False):
    page: int
    """Page number (1-based)."""

    page_size: int
    """Number of results per page."""
