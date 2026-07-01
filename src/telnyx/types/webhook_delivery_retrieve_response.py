# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .webhook_delivery import WebhookDelivery

__all__ = ["WebhookDeliveryRetrieveResponse"]


class WebhookDeliveryRetrieveResponse(BaseModel):
    data: Optional[WebhookDelivery] = None
    """Record of all attempts to deliver a webhook."""
