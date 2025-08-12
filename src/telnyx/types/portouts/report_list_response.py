# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta

__all__ = ["ReportListResponse", "Data", "DataParams", "DataParamsFilters"]


class DataParamsFilters(BaseModel):
    created_at_gt: Optional[datetime] = FieldInfo(alias="created_at__gt", default=None)
    """The date and time the port-out was created after."""

    created_at_lt: Optional[datetime] = FieldInfo(alias="created_at__lt", default=None)
    """The date and time the port-out was created before."""

    customer_reference_in: Optional[List[str]] = FieldInfo(alias="customer_reference__in", default=None)
    """The customer reference of the port-outs to include in the report."""

    end_user_name: Optional[str] = None
    """The end user name of the port-outs to include in the report."""

    phone_numbers_overlaps: Optional[List[str]] = FieldInfo(alias="phone_numbers__overlaps", default=None)
    """A list of phone numbers that the port-outs phone numbers must overlap with."""

    status_in: Optional[
        List[Literal["pending", "authorized", "ported", "rejected", "rejected-pending", "canceled"]]
    ] = FieldInfo(alias="status__in", default=None)
    """The status of the port-outs to include in the report."""


class DataParams(BaseModel):
    filters: DataParamsFilters
    """The filters to apply to the export port-out CSV report."""


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the report."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    document_id: Optional[str] = None
    """Identifies the document that was uploaded when report was generated.

    This field is only populated when the report is under completed status.
    """

    params: Optional[DataParams] = None
    """The parameters for generating a port-outs CSV report."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    report_type: Optional[Literal["export_portouts_csv"]] = None
    """Identifies the type of report"""

    status: Optional[Literal["pending", "completed"]] = None
    """The current status of the report generation."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class ReportListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
