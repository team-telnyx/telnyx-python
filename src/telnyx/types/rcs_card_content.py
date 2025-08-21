# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .rcs_suggestion import RcsSuggestion
from .rcs_content_info import RcsContentInfo

__all__ = ["RcsCardContent", "Media"]


class Media(BaseModel):
    content_info: Optional[RcsContentInfo] = None

    height: Optional[Literal["HEIGHT_UNSPECIFIED", "SHORT", "MEDIUM", "TALL"]] = None
    """The height of the media within a rich card with a vertical layout.

    For a standalone card with horizontal layout, height is not customizable, and
    this field is ignored.
    """


class RcsCardContent(BaseModel):
    description: Optional[str] = None
    """Description of the card (at most 2000 characters)"""

    media: Optional[Media] = None
    """A media file within a rich card."""

    suggestions: Optional[List[RcsSuggestion]] = None
    """List of suggestions to include in the card. Maximum 10 suggestions."""

    title: Optional[str] = None
    """Title of the card (at most 200 characters)"""
