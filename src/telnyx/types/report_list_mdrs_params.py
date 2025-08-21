# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ReportListMdrsParams"]


class ReportListMdrsParams(TypedDict, total=False):
    id: str
    """Message uuid"""

    cld: str
    """Destination number"""

    cli: str
    """Origination number"""

    direction: Literal["INBOUND", "OUTBOUND"]
    """Direction (inbound or outbound)"""

    end_date: str
    """Pagination end date"""

    message_type: Literal["SMS", "MMS"]
    """Type of message"""

    profile: str
    """Name of the profile"""

    start_date: str
    """Pagination start date"""

    status: Literal["GW_TIMEOUT", "DELIVERED", "DLR_UNCONFIRMED", "DLR_TIMEOUT", "RECEIVED", "GW_REJECT", "FAILED"]
    """Message status"""
