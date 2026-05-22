# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserDataUpdateParams"]


class UserDataUpdateParams(TypedDict, total=False):
    webhook_failover_url: str
    """Failover URL to send Whatsapp signup events"""

    webhook_url: str
    """URL to send Whatsapp signup events"""
