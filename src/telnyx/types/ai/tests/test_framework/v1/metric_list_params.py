# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MetricListParams"]


class MetricListParams(TypedDict, total=False):
    agent_id: int
    """Filter metrics attached to the specified test agent."""

    assistant_id: str
    """Filter metrics attached to the specified Telnyx assistant."""
