# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .rcs_suggestion_param import RcsSuggestionParam
from .rcs_content_info_param import RcsContentInfoParam

__all__ = ["RcsCardContentParam", "Media"]


class Media(TypedDict, total=False):
    content_info: RcsContentInfoParam

    height: Literal["HEIGHT_UNSPECIFIED", "SHORT", "MEDIUM", "TALL"]
    """The height of the media within a rich card with a vertical layout.

    For a standalone card with horizontal layout, height is not customizable, and
    this field is ignored.
    """


class RcsCardContentParam(TypedDict, total=False):
    description: str
    """Description of the card (at most 2000 characters)"""

    media: Media
    """A media file within a rich card."""

    suggestions: Iterable[RcsSuggestionParam]
    """List of suggestions to include in the card. Maximum 10 suggestions."""

    title: str
    """Title of the card (at most 200 characters)"""
