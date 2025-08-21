# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReportListWdrsResponse", "Data", "DataCost", "DataDownlinkData", "DataRate", "DataUplinkData", "Meta"]


class DataCost(BaseModel):
    amount: Optional[str] = None
    """Final cost. Cost is calculated as rate \\** unit"""

    currency: Optional[Literal["AUD", "CAD", "EUR", "GBP", "USD"]] = None
    """Currency of the rate and cost"""


class DataDownlinkData(BaseModel):
    amount: Optional[float] = None
    """Downlink data"""

    unit: Optional[Literal["B", "KB", "MB"]] = None
    """Transmission unit"""


class DataRate(BaseModel):
    amount: Optional[str] = None
    """Rate from which cost is calculated"""

    currency: Optional[Literal["AUD", "CAD", "EUR", "GBP", "USD"]] = None
    """Currency of the rate and cost"""


class DataUplinkData(BaseModel):
    amount: Optional[float] = None
    """Uplink data"""

    unit: Optional[Literal["B", "KB", "MB"]] = None
    """Transmission unit"""


class Data(BaseModel):
    id: Optional[str] = None
    """WDR id"""

    cost: Optional[DataCost] = None

    created_at: Optional[datetime] = None
    """Record created time"""

    downlink_data: Optional[DataDownlinkData] = None

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

    rate: Optional[DataRate] = None

    record_type: Optional[str] = None

    sim_card_id: Optional[str] = None
    """Sim card unique identifier"""

    sim_group_id: Optional[str] = None
    """Sim group unique identifier"""

    sim_group_name: Optional[str] = None
    """Defined sim group name"""

    uplink_data: Optional[DataUplinkData] = None


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class ReportListWdrsResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
