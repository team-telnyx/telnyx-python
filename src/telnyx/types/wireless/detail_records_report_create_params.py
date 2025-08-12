# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DetailRecordsReportCreateParams"]


class DetailRecordsReportCreateParams(TypedDict, total=False):
    end_time: str
    """ISO 8601 formatted date-time indicating the end time."""

    start_time: str
    """ISO 8601 formatted date-time indicating the start time."""
