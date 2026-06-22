# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WhatsappTemplateCarouselComponentParam", "Card"]


class Card(TypedDict, total=False):
    components: Iterable[Dict[str, object]]


class WhatsappTemplateCarouselComponentParam(TypedDict, total=False):
    """Carousel component for multi-card templates.

    Each card can contain its own header, body, and buttons.
    """

    cards: Required[Iterable[Card]]
    """Array of card objects, each with its own components."""

    type: Required[Literal["CAROUSEL"]]
