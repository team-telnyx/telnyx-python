# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SubNumberOrdersReportRetrieveResponse", "Data", "DataFilters"]


class DataFilters(BaseModel):
    country_code: Optional[str] = None

    created_at_gt: Optional[datetime] = None

    created_at_lt: Optional[datetime] = None

    customer_reference: Optional[str] = None

    order_request_id: Optional[str] = None

    status: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    filters: Optional[DataFilters] = None
    """The filters that were applied to generate this report"""

    order_type: Optional[str] = None
    """The type of order report."""

    status: Optional[Literal["pending", "success", "failed", "expired"]] = None
    """Indicates the completion level of the sub number orders report.

    The report must have a status of 'success' before it can be downloaded.
    """

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

    user_id: Optional[str] = None
    """The ID of the user who created the report."""


class SubNumberOrdersReportRetrieveResponse(BaseModel):
    data: Optional[Data] = None
