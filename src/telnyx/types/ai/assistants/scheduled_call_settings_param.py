# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ScheduledCallSettingsParam"]


class ScheduledCallSettingsParam(TypedDict, total=False):
    """
    Per-call telephony overrides applied when a scheduled phone-call event
    dispatches. Phone-call events only. New per-call dispatch options should be
    added here rather than as top-level event fields.
    """

    sip_region: Literal["US", "Europe", "Canada", "Australia", "Middle East"]
    """SIP region passed to Telnyx when initiating an outbound call.

    Values match the Telnyx TeXML `SipRegion` parameter exactly. Telnyx defaults to
    `US` when omitted.
    """
