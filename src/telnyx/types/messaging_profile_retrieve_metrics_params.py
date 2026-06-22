# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .messaging_metrics_time_frame import MessagingMetricsTimeFrame

__all__ = ["MessagingProfileRetrieveMetricsParams"]


class MessagingProfileRetrieveMetricsParams(TypedDict, total=False):
    time_frame: MessagingMetricsTimeFrame
    """The time frame for metrics."""
