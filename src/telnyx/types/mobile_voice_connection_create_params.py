# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["MobileVoiceConnectionCreateParams", "Inbound", "Outbound"]


class MobileVoiceConnectionCreateParams(TypedDict, total=False):
    active: bool

    connection_name: str

    inbound: Inbound

    outbound: Outbound

    tags: SequenceNotStr[str]

    webhook_api_version: Literal["1", "2"]

    webhook_event_failover_url: Optional[str]

    webhook_event_url: Optional[str]

    webhook_timeout_secs: Optional[int]


class Inbound(TypedDict, total=False):
    channel_limit: int


class Outbound(TypedDict, total=False):
    channel_limit: int

    outbound_voice_profile_id: str
