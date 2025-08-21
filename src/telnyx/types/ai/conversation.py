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
    own.
    """

    name: Optional[str] = None
