# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Conversation"]


class Conversation(BaseModel):
    id: str

    created_at: datetime
    """The datetime the conversation was created."""

    last_message_at: datetime
    """The datetime of the latest message in the conversation."""

    metadata: Dict[str, str]
    """Metadata associated with the conversation.

    Telnyx provides several pieces of metadata, but customers can also add their
    own. The reserved field `ai_disabled` (boolean) can be set to `true` to prevent
    AI-generated responses on this conversation. When `ai_disabled` is `true`, calls
    to the chat endpoint will return a 400 error. Set to `false` or remove the field
    to re-enable AI responses. This is useful when a human agent needs to take over
    the conversation mid-stream (e.g., a technician stepping in while AI was
    messaging a resident).
    """

    name: Optional[str] = None
