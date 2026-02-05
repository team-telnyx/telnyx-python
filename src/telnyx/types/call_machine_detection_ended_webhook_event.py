# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_machine_detection_ended import CallMachineDetectionEnded

__all__ = ["CallMachineDetectionEndedWebhookEvent"]


class CallMachineDetectionEndedWebhookEvent(BaseModel):
    data: Optional[CallMachineDetectionEnded] = None
