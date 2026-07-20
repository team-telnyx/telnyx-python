# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["ConversationInsightRetrieveAggregatesParams", "Metadata"]


class ConversationInsightRetrieveAggregatesParams(TypedDict, total=False):
    created_at: str
    """Filter by creation datetime to scope the aggregation window.

    Supports range operators (e.g., `created_at=gte.2025-01-01T00:00:00Z` for the
    start of the range, `created_at=lt.2025-01-02T00:00:00Z` for the end). To build
    per-day time series (as the portal does for the 'Insights Over Time' chart),
    issue one request per day bounded by `created_at=gte.<day_start>` and
    `created_at=lt.<next_day_start>`.
    """

    group_by: SequenceNotStr[str]
    """Fields to group by (can be comma-separated or multiple parameters).

    Prefix a field with 'metadata.' (e.g. 'metadata.assistant_id') to group by the
    conversation's metadata instead of the insight result.

    Common fields used for over-time charts:

    - `score` — Group by the insight's score value (e.g. for Agent Instruction
      Following, User Satisfaction).
    - `metadata.assistant_id` — Group by the assistant that handled the
      conversation.
    - `metadata.assistant_version_id` — Group by the assistant version, useful for
      comparing performance across versions in the portal's 'Insights Over Time'
      chart.
    - `metadata.telnyx_conversation_channel` — Group by conversation channel
      (phone_call, web_chat, etc.).
    """

    insight_id: str
    """Optional insight ID to filter conversation insights.

    Only insights matching this ID will be included in the aggregation.
    """

    metadata: Metadata

    show: SequenceNotStr[str]
    """Fields to include in the result (can be comma-separated or multiple parameters).

    Supports the same 'metadata.<key>' prefix as group_by. Each returned row will
    contain the grouped field values plus a `record_count` indicating how many
    conversation insights match that combination.
    """


class Metadata(TypedDict, total=False):
    assistant_id: str
    """Filter by assistant ID (e.g., `metadata.assistant_id=eq.<assistant_id>`).

    When provided, only conversation insights for the specified assistant are
    aggregated. Used by the portal to scope the 'Insights Over Time' chart to a
    single assistant.
    """
