# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_ai_gather_partial_results import CallAIGatherPartialResults

__all__ = ["CallAIGatherPartialResultsWebhookEvent"]


class CallAIGatherPartialResultsWebhookEvent(BaseModel):
    data: Optional[CallAIGatherPartialResults] = None
