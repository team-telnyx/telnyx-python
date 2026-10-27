# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MetricGenerateMetricsParams"]


class MetricGenerateMetricsParams(TypedDict, total=False):
    agent_id: Required[int]
    """Test agent to suggest metrics for."""

    num_metrics: Required[int]
    """How many metrics to suggest."""

    scenarios: Iterable[int]
    """Scenario IDs to base the suggestions on."""
