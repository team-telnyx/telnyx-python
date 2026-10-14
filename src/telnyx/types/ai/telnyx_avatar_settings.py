# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from ..._models import BaseModel
from .avatar_id import AvatarID

__all__ = ["TelnyxAvatarSettings"]


class TelnyxAvatarSettings(BaseModel):
    """**Beta:** Configuration for the Telnyx open-source avatar provider.

    Use one of the six stock avatars or an organization-owned custom avatar returned by the Avatars API. Supported backgrounds are office, studio, and reception.
    """

    avatar_id: AvatarID
    """The Telnyx stock avatar or organization-owned custom avatar to render."""

    background_id: Literal["office", "studio", "reception"]
    """The background to render."""

    model: Literal["foxtrot-1"]
    """Required avatar model identifier, separate from `avatar_id`.

    The supported value is `foxtrot-1`. Omission, null, and unsupported model
    identifiers are rejected.
    """

    provider: Literal["telnyx"]
    """Selects the Telnyx open-source avatar provider."""
