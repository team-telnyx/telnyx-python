# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InsightSettingsParam"]


class InsightSettingsParam(TypedDict, total=False):
    insight_group_id: str
    """Reference to an Insight Group.

    Insights in this group will be run automatically for all the assistant's
    conversations.
    """
