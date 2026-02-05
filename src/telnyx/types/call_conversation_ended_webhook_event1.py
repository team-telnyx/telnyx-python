# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_conversation_ended import CallConversationEnded

__all__ = ["CallConversationEndedWebhookEvent"]


class CallConversationEndedWebhookEvent(BaseModel):
    data: Optional[CallConversationEnded] = None
