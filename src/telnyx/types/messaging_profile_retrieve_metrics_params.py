# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MessagingProfileRetrieveMetricsParams"]


class MessagingProfileRetrieveMetricsParams(TypedDict, total=False):
    time_frame: Literal["1h", "3h", "24h", "3d", "7d", "30d"]
    """The time frame for metrics."""
