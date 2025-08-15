# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .export_portouts_csv_report_param import ExportPortoutsCsvReportParam

__all__ = ["ReportCreateParams"]


class ReportCreateParams(TypedDict, total=False):
    params: Required[ExportPortoutsCsvReportParam]
    """The parameters for generating a port-outs CSV report."""

    report_type: Required[Literal["export_portouts_csv"]]
    """Identifies the type of report"""
