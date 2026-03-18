# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionJoinAIAssistantParams", "Participant"]


class ActionJoinAIAssistantParams(TypedDict, total=False):
    conversation_id: Required[str]
    """The ID of the AI assistant conversation to join."""

    participant: Required[Participant]

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """


class Participant(TypedDict, total=False):
    id: Required[str]
    """The call_control_id of the participant to add to the conversation."""

    role: Required[Literal["user"]]
    """The role of the participant in the conversation."""

    name: str
    """Display name for the participant."""

    on_hangup: Literal["continue_conversation", "end_conversation"]
    """Determines what happens to the conversation when this participant hangs up."""
