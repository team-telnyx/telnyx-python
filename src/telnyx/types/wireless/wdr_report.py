# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WdrReport"]


class WdrReport(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    end_time: Optional[str] = None
    """ISO 8601 formatted date-time indicating the end time."""

    record_type: Optional[str] = None

    report_url: Optional[str] = None
    """The URL where the report content, when generated, will be published to."""

    start_time: Optional[str] = None
    """ISO 8601 formatted date-time indicating the start time."""

    status: Optional[Literal["pending", "complete", "failed", "deleted"]] = None
    """Indicates the status of the report, which is updated asynchronously."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""
