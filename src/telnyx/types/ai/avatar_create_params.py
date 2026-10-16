# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["AvatarCreateParams"]


class AvatarCreateParams(TypedDict, total=False):
    image_file: Required[FileTypes]
    """JPEG, PNG, or WebP image file. The maximum file size is 10 MiB."""

    name: Required[str]
    """Customer-facing name of the custom avatar."""
