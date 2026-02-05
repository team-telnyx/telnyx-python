# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_initiated import CallInitiated

__all__ = ["CallInitiatedWebhookEvent"]


class CallInitiatedWebhookEvent(BaseModel):
    data: Optional[CallInitiated] = None
