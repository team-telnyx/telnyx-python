# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["CommunityTtsEngineCapabilities"]


class CommunityTtsEngineCapabilities(BaseModel):
    """What the engine supports. An unknown key is rejected."""

    streamed_audio: bool
    """Required.

    `true` when the engine sends audio in small frames as it synthesizes; `false`
    when it sends one frame per sentence.
    """

    flush_support: Optional[bool] = None
    """The engine speaks the buffered text when a frame carries `"flush": true`."""

    force_interrupt_support: Optional[bool] = None
    """The engine supports a restart of the current speech (barge-in)."""

    ssml_support: Optional[bool] = None
    """The engine accepts SSML in the text."""

    voice_settings_schema: Optional[Dict[str, object]] = None
    """
    The settings callers can pass to the engine in `voice_settings`, one entry per
    setting: `{"type": "number" | "integer", "min", "max"}`, `{"type": "boolean"}`,
    `{"type": "string"}` (at most 1000 characters) or
    `{"type": "enum", "values": [...]}`, each with an optional `default`. A caller's
    settings are checked against it before Telnyx connects to the engine: an
    undeclared setting, a value of the wrong type, or a value out of bounds is
    refused. An engine that declares none receives the settings as sent.
    """
