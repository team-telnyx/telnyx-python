# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .avatar_id import AvatarID
from .avatar_type import AvatarType

__all__ = ["Avatar"]


class Avatar(BaseModel):
    id: AvatarID
    """Stable identifier returned by the Avatars API.

    Discover available stock IDs with GET /v2/ai/avatars and
    filter[avatar_type]=stock rather than maintaining a fixed list. Custom avatar
    IDs use the `avatar_` prefix and must belong to the authenticated organization.
    The service validates that the selected avatar is available.
    """

    avatar_type: AvatarType
    """
    Whether the avatar is provided by Telnyx or was uploaded by the authenticated
    organization.
    """

    hosted: Literal[True]
    """Indicates that avatar rendering runs on Telnyx-operated infrastructure."""

    image_url: str
    """HTTPS image URL suitable for an avatar selection thumbnail.

    If the URL expires, list or retrieve the avatar again to refresh it.
    """

    name: str
    """Customer-facing avatar name."""

    provider: Literal["telnyx"]
    """Avatar provider. The first release supports Telnyx avatars."""

    content_type: Optional[Literal["image/jpeg", "image/png", "image/webp"]] = None
    """MIME type of a custom avatar image."""

    created_at: Optional[datetime] = None
    """Time when the custom avatar was created."""

    height_px: Optional[int] = None
    """Decoded height of a custom avatar image."""

    image_url_expires_at: Optional[datetime] = None
    """Expiration time of `image_url`. Omitted when the URL does not expire."""

    size_bytes: Optional[int] = None
    """Size of a custom avatar image in bytes."""

    suggested_voice_id: Optional[str] = None
    """Optional recommended Telnyx text-to-speech voice for this avatar.

    An omitted field or empty string means no recommendation is available. Custom
    avatars have no suggested voice. It is informational and selecting the avatar
    does not automatically change the AI Assistant's configured voice.
    """

    updated_at: Optional[datetime] = None
    """Time when the custom avatar was last updated."""

    width_px: Optional[int] = None
    """Decoded width of a custom avatar image."""
