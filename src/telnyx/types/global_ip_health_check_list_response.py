# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .record import Record

__all__ = ["GlobalIPHealthCheckListResponse"]


class GlobalIPHealthCheckListResponse(Record):
    global_ip_id: Optional[str] = None
    """Global IP ID."""

    health_check_params: Optional[Dict[str, object]] = None
    """A Global IP health check params."""

    health_check_type: Optional[str] = None
    """The Global IP health check type."""
