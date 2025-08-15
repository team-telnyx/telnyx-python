# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExportPortingOrdersCsvReportParam", "Filters"]


class Filters(TypedDict, total=False):
    created_at_gt: Annotated[Union[str, datetime], PropertyInfo(alias="created_at__gt", format="iso8601")]
    """The date and time the porting order was created after."""

    created_at_lt: Annotated[Union[str, datetime], PropertyInfo(alias="created_at__lt", format="iso8601")]
    """The date and time the porting order was created before."""

    customer_reference_in: Annotated[List[str], PropertyInfo(alias="customer_reference__in")]
    """The customer reference of the porting orders to include in the report."""

    status_in: Annotated[
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
        ],
        PropertyInfo(alias="status__in"),
    ]
    """The status of the porting orders to include in the report."""


class ExportPortingOrdersCsvReportParam(TypedDict, total=False):
    filters: Required[Filters]
    """The filters to apply to the export porting order CSV report."""
