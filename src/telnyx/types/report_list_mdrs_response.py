# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReportListMdrsResponse", "Data", "Meta"]


class Data(BaseModel):
    id: Optional[str] = None
    """Id of message detail record"""

    cld: Optional[str] = None
    """The destination number for a call, or the callee"""

    cli: Optional[str] = None
    """The number associated with the person initiating the call, or the caller"""

    cost: Optional[str] = None
    """Final cost. Cost is calculated as rate \\** parts"""

    created_at: Optional[datetime] = None
    """Message sent time"""

    currency: Optional[Literal["AUD", "CAD", "EUR", "GBP", "USD"]] = None
    """Currency of the rate and cost"""

    direction: Optional[str] = None
    """Direction of message - inbound or outbound."""

    message_type: Optional[Literal["SMS", "MMS"]] = None
    """Type of message"""

    parts: Optional[float] = None
    """Number of parts this message has.

    Max number of character is 160. If message contains more characters then that it
    will be broken down in multiple parts
    """

    profile_name: Optional[str] = None
    """Configured profile name.

    New profiles can be created and configured on Telnyx portal
    """

    rate: Optional[str] = None
    """Rate applied to the message"""

    record_type: Optional[str] = None

    status: Optional[
        Literal["GW_TIMEOUT", "DELIVERED", "DLR_UNCONFIRMED", "DLR_TIMEOUT", "RECEIVED", "GW_REJECT", "FAILED"]
    ] = None
    """Message status"""


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class ReportListMdrsResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
