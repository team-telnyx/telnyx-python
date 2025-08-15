# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExportPortingOrdersCsvReport", "Filters"]


class Filters(BaseModel):
    created_at_gt: Optional[datetime] = FieldInfo(alias="created_at__gt", default=None)
    """The date and time the porting order was created after."""

    created_at_lt: Optional[datetime] = FieldInfo(alias="created_at__lt", default=None)
    """The date and time the porting order was created before."""

    customer_reference_in: Optional[List[str]] = FieldInfo(alias="customer_reference__in", default=None)
    """The customer reference of the porting orders to include in the report."""

    status_in: Optional[
        List[
            Literal[
                "draft",
                "in-process",
                "submitted",
                "exception",
                "foc-date-confirmed",
                "cancel-pending",
                "ported",
                "cancelled",
            ]
        ]
    ] = FieldInfo(alias="status__in", default=None)
    """The status of the porting orders to include in the report."""


class ExportPortingOrdersCsvReport(BaseModel):
    filters: Filters
    """The filters to apply to the export porting order CSV report."""
