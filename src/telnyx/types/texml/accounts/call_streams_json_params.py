# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallStreamsJsonParams"]


class CallStreamsJsonParams(TypedDict, total=False):
    account_sid: Required[str]

    bidirectional_codec: Annotated[Literal["PCMU", "PCMA", "G722"], PropertyInfo(alias="BidirectionalCodec")]
    """Indicates codec for bidirectional streaming RTP payloads.

    Used only with stream_bidirectional_mode=rtp. Case sensitive.
    """

    bidirectional_mode: Annotated[Literal["mp3", "rtp"], PropertyInfo(alias="BidirectionalMode")]
    """Configures method of bidirectional streaming (mp3, rtp)."""

    name: Annotated[str, PropertyInfo(alias="Name")]
    """The user specified name of Stream."""

    status_callback: Annotated[str, PropertyInfo(alias="StatusCallback")]
    """Url where status callbacks will be sent."""

    status_callback_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="StatusCallbackMethod")]
    """HTTP method used to send status callbacks."""

    track: Annotated[Literal["inbound_track", "outbound_track", "both_tracks"], PropertyInfo(alias="Track")]
    """Tracks to be included in the stream"""

    url: Annotated[str, PropertyInfo(alias="Url")]
    """The destination WebSocket address where the stream is going to be delivered."""
