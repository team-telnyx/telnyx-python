# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .ai_assistant_join_participant_param import AIAssistantJoinParticipantParam

__all__ = ["ActionJoinAIAssistantParams"]


class ActionJoinAIAssistantParams(TypedDict, total=False):
    conversation_id: Required[str]
    """The ID of the AI assistant conversation to join."""

    participant: Required[AIAssistantJoinParticipantParam]

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """
