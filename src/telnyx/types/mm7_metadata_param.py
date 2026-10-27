# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Mm7MetadataParam"]


class Mm7MetadataParam(TypedDict, total=False):
    """MM7 settings for inbound messages"""

    mm7_failover_webhook_url: str
    """Failover webhook URL to receive inbound MM7 traffic"""

    mm7_webhook_url: str
    """Webhook URL to receive inbound MM7 traffic"""
