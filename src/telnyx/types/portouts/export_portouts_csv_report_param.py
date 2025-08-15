# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExportPortoutsCsvReportParam", "Filters"]


class Filters(TypedDict, total=False):
    created_at_gt: Annotated[Union[str, datetime], PropertyInfo(alias="created_at__gt", format="iso8601")]
    """The date and time the port-out was created after."""

    created_at_lt: Annotated[Union[str, datetime], PropertyInfo(alias="created_at__lt", format="iso8601")]
    """The date and time the port-out was created before."""

    customer_reference_in: Annotated[List[str], PropertyInfo(alias="customer_reference__in")]
    """The customer reference of the port-outs to include in the report."""

    end_user_name: str
    """The end user name of the port-outs to include in the report."""

    phone_numbers_overlaps: Annotated[List[str], PropertyInfo(alias="phone_numbers__overlaps")]
    """A list of phone numbers that the port-outs phone numbers must overlap with."""

    status_in: Annotated[
        List[Literal["pending", "authorized", "ported", "rejected", "rejected-pending", "canceled"]],
        PropertyInfo(alias="status__in"),
    ]
    """The status of the port-outs to include in the report."""


class ExportPortoutsCsvReportParam(TypedDict, total=False):
    filters: Required[Filters]
    """The filters to apply to the export port-out CSV report."""
