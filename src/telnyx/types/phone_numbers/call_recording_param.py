# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CallRecordingParam"]


class CallRecordingParam(TypedDict, total=False):
    inbound_call_recording_channels: Literal["single", "dual"]
    """
    When using 'dual' channels, final audio file will be stereo recorded with the
    first leg on channel A, and the rest on channel B.
    """

    inbound_call_recording_enabled: bool
    """When enabled, any inbound call to this number will be recorded."""

    inbound_call_recording_format: Literal["wav", "mp3"]
    """The audio file format for calls being recorded."""
