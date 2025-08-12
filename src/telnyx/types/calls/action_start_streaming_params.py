# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..stream_codec import StreamCodec
from ..dialogflow_config_param import DialogflowConfigParam
from ..stream_bidirectional_mode import StreamBidirectionalMode
from ..stream_bidirectional_codec import StreamBidirectionalCodec
from ..stream_bidirectional_target_legs import StreamBidirectionalTargetLegs

__all__ = ["ActionStartStreamingParams"]


class ActionStartStreamingParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    dialogflow_config: DialogflowConfigParam

    enable_dialogflow: bool
    """Enables Dialogflow for the current call. The default value is false."""

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
