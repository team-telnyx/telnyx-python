# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AvatarSettingsRequestParam"]


class AvatarSettingsRequestParam(TypedDict, total=False):
    """**Beta:** Configuration for the Telnyx open-source avatar provider.

    The launch catalog supports six avatars and office, studio, or reception backgrounds.
    """

    avatar_id: Required[Literal["elena", "ben", "jordan", "lin", "avery", "raphael"]]
    """The Telnyx avatar to render."""

    background_id: Required[Literal["office", "studio", "reception"]]
    """The background to render."""

    model: Required[Literal["foxtrot-1"]]
    """Required avatar model identifier, separate from `avatar_id`.

    The supported value is `foxtrot-1`. Omission, null, and unsupported model
    identifiers are rejected.
    """

    provider: Required[Literal["telnyx"]]
    """Selects the Telnyx open-source avatar provider."""
