# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ReportListMdrsParams"]


class ReportListMdrsParams(TypedDict, total=False):
    id: str
    """Filter results by identifier."""

    cld: str
    """Filter results by cld."""

    cli: str
    """Filter results by cli."""

    direction: Literal["INBOUND", "OUTBOUND"]
    """Filter results by direction."""

    end_date: str
    """Pagination end date"""

    message_type: Literal["SMS", "MMS"]
    """Filter results by message type."""

    profile: str
    """Filter results by profile."""

    start_date: str
    """Pagination start date"""

    status: Literal["GW_TIMEOUT", "DELIVERED", "DLR_UNCONFIRMED", "DLR_TIMEOUT", "RECEIVED", "GW_REJECT", "FAILED"]
    """Filter results by status."""
