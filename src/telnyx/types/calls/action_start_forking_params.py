# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ActionStartForkingParams"]


class ActionStartForkingParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    rx: str
    """
    The network target, <udp:ip_address:port>, where the call's incoming RTP media
    packets should be forwarded.
    """

    stream_type: Literal["decrypted"]
    """Optionally specify a media type to stream.

    If `decrypted` selected, Telnyx will decrypt incoming SIP media before forking
    to the target. `rx` and `tx` are required fields if `decrypted` selected.
    """

    tx: str
    """
    The network target, <udp:ip_address:port>, where the call's outgoing RTP media
    packets should be forwarded.
    """
