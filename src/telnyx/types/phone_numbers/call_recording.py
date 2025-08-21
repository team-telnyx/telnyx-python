# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CallRecording"]


class CallRecording(BaseModel):
    inbound_call_recording_channels: Optional[Literal["single", "dual"]] = None
    """
    When using 'dual' channels, final audio file will be stereo recorded with the
    first leg on channel A, and the rest on channel B.
    """

    inbound_call_recording_enabled: Optional[bool] = None
    """When enabled, any inbound call to this number will be recorded."""

    inbound_call_recording_format: Optional[Literal["wav", "mp3"]] = None
    """The audio file format for calls being recorded."""
