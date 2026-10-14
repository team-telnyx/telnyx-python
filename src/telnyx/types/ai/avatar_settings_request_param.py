# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AvatarSettingsRequestParam"]


class AvatarSettingsRequestParam(TypedDict, total=False):
    """**Beta:** Configuration for the Telnyx open-source avatar provider.

    Use one of the six stock avatars or an organization-owned custom avatar returned by the Avatars API. Supported backgrounds are office, studio, and reception.
    """

    avatar_id: Required["AvatarIDParam"]
    """The Telnyx stock avatar or organization-owned custom avatar to render."""

    background_id: Required[Literal["office", "studio", "reception"]]
    """The background to render."""

    model: Required[Literal["foxtrot-1"]]
    """Required avatar model identifier, separate from `avatar_id`.

    The supported value is `foxtrot-1`. Omission, null, and unsupported model
    identifiers are rejected.
    """

    provider: Required[Literal["telnyx"]]
    """Selects the Telnyx open-source avatar provider."""


from .avatar_id_param import AvatarIDParam
