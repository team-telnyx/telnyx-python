# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionStartConversationRelayResponse", "Data"]


class Data(BaseModel):
    conversation_relay_id: Optional[str] = None
    """The ID of the Conversation Relay session created by the command."""

    result: Optional[str] = None


class ActionStartConversationRelayResponse(BaseModel):
    data: Optional[Data] = None
