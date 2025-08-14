# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["OutboundCallRecordingParam"]


class OutboundCallRecordingParam(TypedDict, total=False):
    call_recording_caller_phone_numbers: List[str]
    """
    When call_recording_type is 'by_caller_phone_number', only outbound calls using
    one of these numbers will be recorded. Numbers must be specified in E164 format.
    """

    call_recording_channels: Literal["single", "dual"]
    """
    When using 'dual' channels, the final audio file will be a stereo recording with
    the first leg on channel A, and the rest on channel B.
    """

    call_recording_format: Literal["wav", "mp3"]
    """The audio file format for calls being recorded."""

    call_recording_type: Literal["all", "none", "by_caller_phone_number"]
    """Specifies which calls are recorded."""
