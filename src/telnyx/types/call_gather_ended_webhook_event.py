# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_gather_ended import CallGatherEnded

__all__ = ["CallGatherEndedWebhookEvent"]


class CallGatherEndedWebhookEvent(BaseModel):
    data: Optional[CallGatherEnded] = None
