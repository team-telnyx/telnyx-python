# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AIAssistantJoinParticipantParam"]


class AIAssistantJoinParticipantParam(TypedDict, total=False):
    id: Required[str]
    """The call_control_id of the participant to add to the conversation."""

    role: Required[Literal["user"]]
    """The role of the participant in the conversation."""

    name: str
    """Display name for the participant."""

    on_hangup: Literal["continue_conversation", "end_conversation"]
    """Determines what happens to the conversation when this participant hangs up."""
