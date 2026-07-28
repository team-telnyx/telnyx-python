# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .email_webhook import EmailWebhook

__all__ = ["EmailWebhookResponse"]


class EmailWebhookResponse(BaseModel):
    data: EmailWebhook
