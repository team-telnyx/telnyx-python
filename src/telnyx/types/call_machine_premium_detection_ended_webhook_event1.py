# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_machine_premium_detection_ended import CallMachinePremiumDetectionEnded

__all__ = ["CallMachinePremiumDetectionEndedWebhookEvent"]


class CallMachinePremiumDetectionEndedWebhookEvent(BaseModel):
    data: Optional[CallMachinePremiumDetectionEnded] = None
