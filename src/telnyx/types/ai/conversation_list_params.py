# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConversationListParams"]


class ConversationListParams(TypedDict, total=False):
    id: str
    """Filter by conversation ID (e.g. id=eq.123)"""

    created_at: str
    """Filter by creation datetime (e.g., `created_at=gte.2025-01-01`)"""

    last_message_at: str
    """Filter by last message datetime (e.g., `last_message_at=lte.2025-06-01`)"""

    limit: int
    """Limit the number of returned conversations (e.g., `limit=10`)"""

    metadata_assistant_id: Annotated[str, PropertyInfo(alias="metadata->assistant_id")]
    """Filter by assistant ID (e.g., `metadata->assistant_id=eq.assistant-123`)"""

    metadata_call_control_id: Annotated[str, PropertyInfo(alias="metadata->call_control_id")]
    """Filter by call control ID (e.g., `metadata->call_control_id=eq.v3:123`)"""

    metadata_telnyx_agent_target: Annotated[str, PropertyInfo(alias="metadata->telnyx_agent_target")]
    """
    Filter by the phone number, SIP URI, or other identifier for the agent (e.g.,
    `metadata->telnyx_agent_target=eq.+13128675309`)
    """

    metadata_telnyx_conversation_channel: Annotated[str, PropertyInfo(alias="metadata->telnyx_conversation_channel")]
    """
    Filter by conversation channel (e.g.,
    `metadata->telnyx_conversation_channel=eq.phone_call`)
    """

    metadata_telnyx_end_user_target: Annotated[str, PropertyInfo(alias="metadata->telnyx_end_user_target")]
    """
    Filter by the phone number, SIP URI, or other identifier for the end user (e.g.,
    `metadata->telnyx_end_user_target=eq.+13128675309`)
    """

    name: str
    """Filter by conversation Name (e.g. `name=like.Voice%`)"""

    or_: Annotated[str, PropertyInfo(alias="or")]
    """
    Apply OR conditions using PostgREST syntax (e.g.,
    `or=(created_at.gte.2025-04-01,last_message_at.gte.2025-04-01)`)
    """

    order: str
    """
    Order the results by specific fields (e.g., `order=created_at.desc` or
    `order=last_message_at.asc`)
    """
