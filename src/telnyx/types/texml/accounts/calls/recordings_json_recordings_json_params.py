# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["RecordingsJsonRecordingsJsonParams"]


class RecordingsJsonRecordingsJsonParams(TypedDict, total=False):
    account_sid: Required[str]

    play_beep: Annotated[bool, PropertyInfo(alias="PlayBeep")]
    """Whether to play a beep when recording is started."""

    recording_channels: Annotated[Literal["single", "dual"], PropertyInfo(alias="RecordingChannels")]
    """
    When `dual`, final audio file has the first leg on channel A, and the rest on
    channel B. `single` mixes both tracks into a single channel.
    """

    recording_status_callback: Annotated[str, PropertyInfo(alias="RecordingStatusCallback")]
    """Url where status callbacks will be sent."""

    recording_status_callback_event: Annotated[str, PropertyInfo(alias="RecordingStatusCallbackEvent")]
    """
    The changes to the recording's state that should generate a call to
    `RecoridngStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
    Separate multiple values with a space. Defaults to `completed`.
    """

    recording_status_callback_method: Annotated[
        Literal["GET", "POST"], PropertyInfo(alias="RecordingStatusCallbackMethod")
    ]
    """HTTP method used to send status callbacks."""

    recording_track: Annotated[Literal["inbound", "outbound", "both"], PropertyInfo(alias="RecordingTrack")]
    """The audio track to record for the call. The default is `both`."""

    send_recording_url: Annotated[bool, PropertyInfo(alias="SendRecordingUrl")]
    """Whether to send RecordingUrl in webhooks."""
