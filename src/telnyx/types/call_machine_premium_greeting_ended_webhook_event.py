# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_machine_premium_greeting_ended import CallMachinePremiumGreetingEnded

__all__ = ["CallMachinePremiumGreetingEndedWebhookEvent"]


class CallMachinePremiumGreetingEndedWebhookEvent(BaseModel):
    data: Optional[CallMachinePremiumGreetingEnded] = None
