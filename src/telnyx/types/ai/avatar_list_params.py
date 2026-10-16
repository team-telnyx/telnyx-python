# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AvatarListParams"]


class AvatarListParams(TypedDict, total=False):
    filter_avatar_type: Annotated["AvatarType", PropertyInfo(alias="filter[avatar_type]")]
    """Return only stock or custom avatars."""

    filter_id: Annotated["AvatarID", PropertyInfo(alias="filter[id]")]
    """Return the avatar with this exact ID."""

    filter_name: Annotated[str, PropertyInfo(alias="filter[name]")]
    """Return avatars whose names contain this value, using case-insensitive matching."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number to retrieve, starting at 1."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of avatars to return per page."""


from .avatar_id import AvatarID
from .avatar_type import AvatarType
