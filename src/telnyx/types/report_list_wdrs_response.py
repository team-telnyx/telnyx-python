# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReportListWdrsResponse", "Cost", "DownlinkData", "Rate", "UplinkData"]


class Cost(BaseModel):
    amount: Optional[str] = None
    """Final cost. Cost is calculated as rate \\** unit"""

    currency: Optional[Literal["AUD", "CAD", "EUR", "GBP", "USD"]] = None
    """Currency of the rate and cost"""


class DownlinkData(BaseModel):
    amount: Optional[float] = None
    """Downlink data"""

    unit: Optional[Literal["B", "KB", "MB"]] = None
    """Transmission unit"""


class Rate(BaseModel):
    amount: Optional[str] = None
    """Rate from which cost is calculated"""

    currency: Optional[Literal["AUD", "CAD", "EUR", "GBP", "USD"]] = None
    """Currency of the rate and cost"""


class UplinkData(BaseModel):
    amount: Optional[float] = None
    """Uplink data"""

    unit: Optional[Literal["B", "KB", "MB"]] = None
    """Transmission unit"""


class ReportListWdrsResponse(BaseModel):
    id: Optional[str] = None
    """WDR id"""

    cost: Optional[Cost] = None

    created_at: Optional[datetime] = None
    """Record created time"""

    downlink_data: Optional[DownlinkData] = None

    duration_seconds: Optional[float] = None
    """Session duration in seconds."""

    imsi: Optional[str] = None
    """International mobile subscriber identity."""

    mcc: Optional[str] = None
    """Mobile country code."""

    mnc: Optional[str] = None
    """Mobile network code."""

    phone_number: Optional[str] = None
    """Phone number"""

    rate: Optional[Rate] = None

    record_type: Optional[str] = None

    sim_card_id: Optional[str] = None
    """Sim card unique identifier"""

    sim_group_id: Optional[str] = None
    """Sim group unique identifier"""

    sim_group_name: Optional[str] = None
    """Defined sim group name"""

    uplink_data: Optional[UplinkData] = None
