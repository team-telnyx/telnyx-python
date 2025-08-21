# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["GlobalIPUsageRetrieveResponse", "Data", "DataGlobalIP", "DataReceived", "DataTransmitted"]


class DataGlobalIP(BaseModel):
    id: Optional[str] = None
    """Global IP ID."""

    ip_address: Optional[str] = None
    """The Global IP address."""


class DataReceived(BaseModel):
    amount: Optional[float] = None
    """The amount of data received."""

    unit: Optional[str] = None
    """The unit of the amount of data received."""


class DataTransmitted(BaseModel):
    amount: Optional[float] = None
    """The amount of data transmitted."""

    unit: Optional[str] = None
    """The unit of the amount of data transmitted."""


class Data(BaseModel):
    global_ip: Optional[DataGlobalIP] = None

    received: Optional[DataReceived] = None

    timestamp: Optional[datetime] = None
    """The timestamp of the metric."""

    transmitted: Optional[DataTransmitted] = None


class GlobalIPUsageRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None
