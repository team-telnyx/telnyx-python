# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .whatsapp_media_param import WhatsappMediaParam

__all__ = [
    "WhatsappInteractiveParam",
    "Action",
    "ActionButton",
    "ActionButtonReply",
    "ActionCard",
    "ActionCardAction",
    "ActionCardBody",
    "ActionCardHeader",
    "ActionParameters",
    "ActionSection",
    "ActionSectionProductItem",
    "ActionSectionRow",
    "Body",
    "Footer",
    "Header",
]


class ActionButtonReply(TypedDict, total=False):
    id: str
    """unique identifier for each button, 256 character maximum"""

    title: str
    """button label, 20 character maximum"""


class ActionButton(TypedDict, total=False):
    reply: ActionButtonReply

    type: Literal["reply"]


class ActionCardAction(TypedDict, total=False):
    catalog_id: str
    """the unique ID of the catalog"""

    product_retailer_id: str
    """the unique retailer ID of the product"""


class ActionCardBody(TypedDict, total=False):
    text: str
    """160 character maximum, up to 2 line breaks"""


class ActionCardHeader(TypedDict, total=False):
    image: WhatsappMediaParam

    type: Literal["image", "video"]

    video: WhatsappMediaParam


class ActionCard(TypedDict, total=False):
    action: ActionCardAction

    body: ActionCardBody

    card_index: int
    """unique index for each card (0-9)"""

    header: ActionCardHeader

    type: Literal["cta_url"]


class ActionParameters(TypedDict, total=False):
    display_text: str
    """button label text, 20 character maximum"""

    url: str
    """button URL to load when tapped by the user"""


class ActionSectionProductItem(TypedDict, total=False):
    product_retailer_id: str


class ActionSectionRow(TypedDict, total=False):
    id: str
    """arbitrary string identifying the row, 200 character maximum"""

    description: str
    """row description, 72 character maximum"""

    title: str
    """row title, 24 character maximum"""


class ActionSection(TypedDict, total=False):
    product_items: Iterable[ActionSectionProductItem]

    rows: Iterable[ActionSectionRow]

    title: str
    """section title, 24 character maximum"""


class Action(TypedDict, total=False):
    button: str

    buttons: Iterable[ActionButton]

    cards: Iterable[ActionCard]

    catalog_id: str

    mode: str

    name: str

    parameters: ActionParameters

    product_retailer_id: str

    sections: Iterable[ActionSection]


class Body(TypedDict, total=False):
    text: str
    """body text, 1024 character maximum"""


class Footer(TypedDict, total=False):
    text: str
    """footer text, 60 character maximum"""


class Header(TypedDict, total=False):
    document: WhatsappMediaParam

    image: WhatsappMediaParam

    sub_text: str

    text: str
    """header text, 60 character maximum"""

    video: WhatsappMediaParam


class WhatsappInteractiveParam(TypedDict, total=False):
    action: Action

    body: Body

    footer: Footer

    header: Header

    type: Literal["cta_url", "list", "carousel", "button", "location_request_message"]
