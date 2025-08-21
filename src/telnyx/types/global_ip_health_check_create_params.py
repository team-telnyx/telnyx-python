# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["GlobalIPHealthCheckCreateParams"]


class GlobalIPHealthCheckCreateParams(TypedDict, total=False):
    global_ip_id: str
    """Global IP ID."""

    health_check_params: Dict[str, object]
    """A Global IP health check params."""

    health_check_type: str
    """The Global IP health check type."""
