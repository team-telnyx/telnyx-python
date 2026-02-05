# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_ai_gather_ended import CallAIGatherEnded

__all__ = ["CallAIGatherEndedWebhookEvent"]


class CallAIGatherEndedWebhookEvent(BaseModel):
    data: Optional[CallAIGatherEnded] = None
