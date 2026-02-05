# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_ai_gather_message_history_updated import CallAIGatherMessageHistoryUpdated

__all__ = ["CallAIGatherMessageHistoryUpdatedWebhookEvent"]


class CallAIGatherMessageHistoryUpdatedWebhookEvent(BaseModel):
    data: Optional[CallAIGatherMessageHistoryUpdated] = None
