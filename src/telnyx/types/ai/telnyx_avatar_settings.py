# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TelnyxAvatarSettings"]


class TelnyxAvatarSettings(BaseModel):
    """**Beta:** Configuration for the Telnyx open-source avatar provider.

    The launch catalog supports six avatars and office, studio, or reception backgrounds.
    """

    avatar_id: Literal["elena", "ben", "jordan", "lin", "avery", "raphael"]
    """The Telnyx avatar to render."""

    background_id: Literal["office", "studio", "reception"]
    """The background to render."""

    model: Literal["foxtrot-1"]
    """Required avatar model identifier, separate from `avatar_id`.

    The supported value is `foxtrot-1`. Omission, null, and unsupported model
    identifiers are rejected.
    """

    provider: Literal["telnyx"]
    """Selects the Telnyx open-source avatar provider."""
