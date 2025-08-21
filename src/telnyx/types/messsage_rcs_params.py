# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .rcs_agent_message_param import RcsAgentMessageParam

__all__ = ["MesssageRcsParams", "MmsFallback", "SMSFallback"]


class MesssageRcsParams(TypedDict, total=False):
    agent_id: Required[str]
    """RCS Agent ID"""

    agent_message: Required[RcsAgentMessageParam]

    messaging_profile_id: Required[str]
    """A valid messaging profile ID"""

    to: Required[str]
    """Phone number in +E.164 format"""

    mms_fallback: MmsFallback

    sms_fallback: SMSFallback

    type: Literal["RCS"]
    """Message type - must be set to "RCS" """

    webhook_url: str
    """The URL where webhooks related to this message will be sent."""


_MmsFallbackReservedKeywords = TypedDict(
    "_MmsFallbackReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MmsFallback(_MmsFallbackReservedKeywords, total=False):
    media_urls: List[str]
    """List of media URLs"""

    subject: str
    """Subject of the message"""

    text: str
    """Text"""


_SMSFallbackReservedKeywords = TypedDict(
    "_SMSFallbackReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class SMSFallback(_SMSFallbackReservedKeywords, total=False):
    text: str
    """Text (maximum 3072 characters)"""
