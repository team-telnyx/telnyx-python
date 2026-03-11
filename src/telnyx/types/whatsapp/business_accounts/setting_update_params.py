# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    name: str

    timezone: str
    """IANA timezone identifier"""

    webhook_enabled: bool
    """Enable/disable receiving Whatsapp events"""

    webhook_events: SequenceNotStr[str]

    webhook_failover_url: str
    """Failover URL to send Whatsapp events"""

    webhook_url: str
    """URL to send Whatsapp events"""
