# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .rcs_suggestion import RcsSuggestion
from .rcs_card_content import RcsCardContent
from .rcs_content_info import RcsContentInfo

__all__ = [
    "RcsAgentMessage",
    "ContentMessage",
    "ContentMessageRichCard",
    "ContentMessageRichCardCarouselCard",
    "ContentMessageRichCardStandaloneCard",
    "Event",
]


class ContentMessageRichCardCarouselCard(BaseModel):
    card_contents: List[RcsCardContent]
    """The list of contents for each card in the carousel.

    A carousel can have a minimum of 2 cards and a maximum 10 cards.
    """

    card_width: Literal["CARD_WIDTH_UNSPECIFIED", "SMALL", "MEDIUM"]
    """The width of the cards in the carousel."""


class ContentMessageRichCardStandaloneCard(BaseModel):
    card_content: RcsCardContent

    card_orientation: Literal["CARD_ORIENTATION_UNSPECIFIED", "HORIZONTAL", "VERTICAL"]
    """Orientation of the card."""

    thumbnail_image_alignment: Literal["THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED", "LEFT", "RIGHT"]
    """Image preview alignment for standalone cards with horizontal layout."""


class ContentMessageRichCard(BaseModel):
    carousel_card: Optional[ContentMessageRichCardCarouselCard] = None
    """Carousel of cards."""

    standalone_card: Optional[ContentMessageRichCardStandaloneCard] = None
    """Standalone card"""


class ContentMessage(BaseModel):
    content_info: Optional[RcsContentInfo] = None

    rich_card: Optional[ContentMessageRichCard] = None

    suggestions: Optional[List[RcsSuggestion]] = None
    """List of suggested actions and replies"""

    text: Optional[str] = None
    """Text (maximum 3072 characters)"""


class Event(BaseModel):
    event_type: Optional[Literal["TYPE_UNSPECIFIED", "IS_TYPING", "READ"]] = None


class RcsAgentMessage(BaseModel):
    content_message: Optional[ContentMessage] = None

    event: Optional[Event] = None
    """RCS Event to send to the recipient"""

    expire_time: Optional[datetime] = None
    """Timestamp in UTC of when this message is considered expired"""

    ttl: Optional[str] = None
    """Duration in seconds ending with 's'"""
