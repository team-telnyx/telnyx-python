# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["Mm7Metadata"]


class Mm7Metadata(BaseModel):
    """MM7 settings for inbound messages"""

    mm7_failover_webhook_url: Optional[str] = None
    """Failover webhook URL to receive inbound MM7 traffic"""

    mm7_webhook_url: Optional[str] = None
    """Webhook URL to receive inbound MM7 traffic"""
