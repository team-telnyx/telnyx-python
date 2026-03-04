# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["StreamClientEvent"]


class StreamClientEvent(BaseModel):
    """Client-to-server frame containing text to synthesize."""

    text: str
    """Text to convert to speech.

    Send `" "` (single space) as an initial handshake with optional
    `voice_settings`. Subsequent messages contain the actual text to synthesize.
    """

    force: Optional[bool] = None
    """When `true`, stops the current synthesis worker and starts a new one.

    Used to interrupt speech mid-stream and begin synthesizing new text.
    """

    voice_settings: Optional[Dict[str, object]] = None
    """Provider-specific voice settings sent with the initial handshake.

    Contents vary by provider — e.g. `{"speed": 1.2}` for Minimax,
    `{"voice_speed": 1.5}` for Telnyx.
    """
