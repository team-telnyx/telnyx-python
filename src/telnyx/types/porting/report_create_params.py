# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .export_porting_orders_csv_report_param import ExportPortingOrdersCsvReportParam

__all__ = ["ReportCreateParams"]


class ReportCreateParams(TypedDict, total=False):
    params: Required[ExportPortingOrdersCsvReportParam]
    """The parameters for generating a porting orders CSV report."""

    report_type: Required[Literal["export_porting_orders_csv"]]
    """Identifies the type of report"""
