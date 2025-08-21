# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .rcs_suggestion_param import RcsSuggestionParam
from .rcs_card_content_param import RcsCardContentParam
from .rcs_content_info_param import RcsContentInfoParam

__all__ = [
    "RcsAgentMessageParam",
    "ContentMessage",
    "ContentMessageRichCard",
    "ContentMessageRichCardCarouselCard",
    "ContentMessageRichCardStandaloneCard",
    "Event",
]


class ContentMessageRichCardCarouselCard(TypedDict, total=False):
    card_contents: Required[Iterable[RcsCardContentParam]]
    """The list of contents for each card in the carousel.

    A carousel can have a minimum of 2 cards and a maximum 10 cards.
    """

    card_width: Required[Literal["CARD_WIDTH_UNSPECIFIED", "SMALL", "MEDIUM"]]
    """The width of the cards in the carousel."""


class ContentMessageRichCardStandaloneCard(TypedDict, total=False):
    card_content: Required[RcsCardContentParam]

    card_orientation: Required[Literal["CARD_ORIENTATION_UNSPECIFIED", "HORIZONTAL", "VERTICAL"]]
    """Orientation of the card."""

    thumbnail_image_alignment: Required[Literal["THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED", "LEFT", "RIGHT"]]
    """Image preview alignment for standalone cards with horizontal layout."""


class ContentMessageRichCard(TypedDict, total=False):
    carousel_card: ContentMessageRichCardCarouselCard
    """Carousel of cards."""

    standalone_card: ContentMessageRichCardStandaloneCard
    """Standalone card"""


class ContentMessage(TypedDict, total=False):
    content_info: RcsContentInfoParam

    rich_card: ContentMessageRichCard

    suggestions: Iterable[RcsSuggestionParam]
    """List of suggested actions and replies"""

    text: str
    """Text (maximum 3072 characters)"""


class Event(TypedDict, total=False):
    event_type: Literal["TYPE_UNSPECIFIED", "IS_TYPING", "READ"]


class RcsAgentMessageParam(TypedDict, total=False):
    content_message: ContentMessage

    event: Event
    """RCS Event to send to the recipient"""

    expire_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Timestamp in UTC of when this message is considered expired"""

    ttl: str
    """Duration in seconds ending with 's'"""
