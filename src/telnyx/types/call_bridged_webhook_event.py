# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_bridged import CallBridged

__all__ = ["CallBridgedWebhookEvent"]


class CallBridgedWebhookEvent(BaseModel):
    data: Optional[CallBridged] = None
