# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OutboundCallRecording"]


class OutboundCallRecording(BaseModel):
    call_recording_caller_phone_numbers: Optional[List[str]] = None
    """
    When call_recording_type is 'by_caller_phone_number', only outbound calls using
    one of these numbers will be recorded. Numbers must be specified in E164 format.
    """

    call_recording_channels: Optional[Literal["single", "dual"]] = None
    """
    When using 'dual' channels, the final audio file will be a stereo recording with
    the first leg on channel A, and the rest on channel B.
    """

    call_recording_format: Optional[Literal["wav", "mp3"]] = None
    """The audio file format for calls being recorded."""

    call_recording_type: Optional[Literal["all", "none", "by_caller_phone_number"]] = None
    """Specifies which calls are recorded."""
