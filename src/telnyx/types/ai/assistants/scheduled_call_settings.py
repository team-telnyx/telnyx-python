# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ScheduledCallSettings"]


class ScheduledCallSettings(BaseModel):
    """
    Per-call telephony overrides applied when a scheduled phone-call event
    dispatches. Phone-call events only. New per-call dispatch options should be
    added here rather than as top-level event fields.
    """

    sip_region: Optional[Literal["US", "Europe", "Canada", "Australia", "Middle East"]] = None
    """SIP region passed to Telnyx when initiating an outbound call.

    Values match the Telnyx TeXML `SipRegion` parameter exactly. Telnyx defaults to
    `US` when omitted.
    """
