# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SimCardDataUsageNotificationRetrieveResponse", "Data", "DataThreshold"]


class DataThreshold(BaseModel):
    amount: Optional[str] = None

    unit: Optional[Literal["MB", "GB"]] = None


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    record_type: Optional[str] = None

    sim_card_id: Optional[str] = None
    """The identification UUID of the related SIM card resource."""

    threshold: Optional[DataThreshold] = None
    """Data usage threshold that will trigger the notification."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class SimCardDataUsageNotificationRetrieveResponse(BaseModel):
    data: Optional[Data] = None
    """The SIM card individual data usage notification information."""
