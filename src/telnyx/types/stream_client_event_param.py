# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["StreamClientEventParam"]


class StreamClientEventParam(TypedDict, total=False):
    """Client-to-server frame containing text to synthesize."""

    text: Required[str]
    """Text to convert to speech.

    Send `" "` (single space) as an initial handshake with optional
    `voice_settings`. Subsequent messages contain the actual text to synthesize.
    """

    force: bool
    """When `true`, stops the current synthesis worker and starts a new one.

    Used to interrupt speech mid-stream and begin synthesizing new text.
    """

    voice_settings: Dict[str, object]
    """Provider-specific voice settings sent with the initial handshake.

    Contents vary by provider — e.g. `{"speed": 1.2}` for Minimax,
    `{"voice_speed": 1.5}` for Telnyx.
    """
