# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PortingOrderDocumentsParam"]


class PortingOrderDocumentsParam(TypedDict, total=False):
    """Can be specified directly or via the `requirement_group_id` parameter."""

    invoice: Optional[str]
    """Returned ID of the submitted Invoice via the Documents endpoint"""

    loa: Optional[str]
    """Returned ID of the submitted LOA via the Documents endpoint"""
