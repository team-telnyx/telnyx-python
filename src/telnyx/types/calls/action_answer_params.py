# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from ..stream_codec import StreamCodec
from ..sip_header_param import SipHeaderParam
from ..custom_sip_header_param import CustomSipHeaderParam
from ..sound_modifications_param import SoundModificationsParam
from ..stream_bidirectional_mode import StreamBidirectionalMode
from ..stream_bidirectional_codec import StreamBidirectionalCodec
from ..stream_bidirectional_target_legs import StreamBidirectionalTargetLegs
from .transcription_start_request_param import TranscriptionStartRequestParam

__all__ = ["ActionAnswerParams"]


class ActionAnswerParams(TypedDict, total=False):
    billing_group_id: str
    """Use this field to set the Billing Group ID for the call.

    Must be a valid and existing Billing Group ID.
    """

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    custom_headers: Iterable[CustomSipHeaderParam]
    """Custom headers to be added to the SIP INVITE response."""

    preferred_codecs: Literal["G722,PCMU,PCMA,G729,OPUS,VP8,H264"]
    """
    The list of comma-separated codecs in a preferred order for the forked media to
    be received.
    """

    record: Literal["record-from-answer"]
    """Start recording automatically after an event. Disabled by default."""

    record_channels: Literal["single", "dual"]
    """
    Defines which channel should be recorded ('single' or 'dual') when `record` is
    specified.
    """

    record_custom_file_name: str
    """The custom recording file name to be used instead of the default `call_leg_id`.

    Telnyx will still add a Unix timestamp suffix.
    """

    record_format: Literal["wav", "mp3"]
    """
    Defines the format of the recording ('wav' or 'mp3') when `record` is specified.
    """

    record_max_length: int
    """
    Defines the maximum length for the recording in seconds when `record` is
    specified. The minimum value is 0. The maximum value is 43200. The default value
    is 0 (infinite).
    """

    record_timeout_secs: int
    """
    The number of seconds that Telnyx will wait for the recording to be stopped if
    silence is detected when `record` is specified. The timer only starts when the
    speech is detected. Please note that call transcription is used to detect
    silence and the related charge will be applied. The minimum value is 0. The
    default value is 0 (infinite).
    """

    record_track: Literal["both", "inbound", "outbound"]
    """The audio track to be recorded.

    Can be either `both`, `inbound` or `outbound`. If only single track is specified
    (`inbound`, `outbound`), `channels` configuration is ignored and it will be
    recorded as mono (single channel).
    """

    record_trim: Literal["trim-silence"]
    """
    When set to `trim-silence`, silence will be removed from the beginning and end
    of the recording.
    """

    send_silence_when_idle: bool
    """Generate silence RTP packets when no transmission available."""

    sip_headers: Iterable[SipHeaderParam]
    """SIP headers to be added to the SIP INVITE response.

    Currently only User-to-User header is supported.
    """

    sound_modifications: SoundModificationsParam
    """Use this field to modify sound effects, for example adjust the pitch."""

    stream_bidirectional_codec: StreamBidirectionalCodec
    """Indicates codec for bidirectional streaming RTP payloads.

    Used only with stream_bidirectional_mode=rtp. Case sensitive.
    """

    stream_bidirectional_mode: StreamBidirectionalMode
    """Configures method of bidirectional streaming (mp3, rtp)."""

    stream_bidirectional_target_legs: StreamBidirectionalTargetLegs
    """Specifies which call legs should receive the bidirectional stream audio."""

    stream_codec: StreamCodec
    """Specifies the codec to be used for the streamed audio.

    When set to 'default' or when transcoding is not possible, the codec from the
    call will be used. Currently, transcoding is only supported between PCMU and
    PCMA codecs.
    """

    stream_track: Literal["inbound_track", "outbound_track", "both_tracks"]
    """Specifies which track should be streamed."""

    stream_url: str
    """The destination WebSocket address where the stream is going to be delivered."""

    transcription: bool
    """Enable transcription upon call answer. The default value is false."""

    transcription_config: TranscriptionStartRequestParam

    webhook_url: str
    """
    Use this field to override the URL for which Telnyx will send subsequent
    webhooks to for this call.
    """

    webhook_url_method: Literal["POST", "GET"]
    """HTTP request type used for `webhook_url`."""
