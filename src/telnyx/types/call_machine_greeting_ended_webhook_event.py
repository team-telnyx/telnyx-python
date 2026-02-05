# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_machine_greeting_ended import CallMachineGreetingEnded

__all__ = ["CallMachineGreetingEndedWebhookEvent"]


class CallMachineGreetingEndedWebhookEvent(BaseModel):
    data: Optional[CallMachineGreetingEnded] = None
