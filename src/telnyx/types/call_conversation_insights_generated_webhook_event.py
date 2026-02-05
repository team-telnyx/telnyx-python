# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_conversation_insights_generated import CallConversationInsightsGenerated

__all__ = ["CallConversationInsightsGeneratedWebhookEvent"]


class CallConversationInsightsGeneratedWebhookEvent(BaseModel):
    data: Optional[CallConversationInsightsGenerated] = None
