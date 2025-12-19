# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .whatsapp_media_param import WhatsappMediaParam

__all__ = [
    "MessageSendWhatsappParams",
    "WhatsappMessage",
    "WhatsappMessageContact",
    "WhatsappMessageContactAddress",
    "WhatsappMessageContactEmail",
    "WhatsappMessageContactOrg",
    "WhatsappMessageContactPhone",
    "WhatsappMessageContactURL",
    "WhatsappMessageInteractive",
    "WhatsappMessageInteractiveAction",
    "WhatsappMessageInteractiveActionButton",
    "WhatsappMessageInteractiveActionButtonReply",
    "WhatsappMessageInteractiveActionCard",
    "WhatsappMessageInteractiveActionCardAction",
    "WhatsappMessageInteractiveActionCardBody",
    "WhatsappMessageInteractiveActionCardHeader",
    "WhatsappMessageInteractiveActionParameters",
    "WhatsappMessageInteractiveActionSection",
    "WhatsappMessageInteractiveActionSectionProductItem",
    "WhatsappMessageInteractiveActionSectionRow",
    "WhatsappMessageInteractiveBody",
    "WhatsappMessageInteractiveFooter",
    "WhatsappMessageInteractiveHeader",
    "WhatsappMessageLocation",
    "WhatsappMessageReaction",
]


class MessageSendWhatsappParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Phone number in +E.164 format associated with Whatsapp account"""

    to: Required[str]
    """Phone number in +E.164 format"""

    whatsapp_message: Required[WhatsappMessage]

    type: Literal["WHATSAPP"]
    """Message type - must be set to "WHATSAPP" """

    webhook_url: str
    """The URL where webhooks related to this message will be sent."""


class WhatsappMessageContactAddress(TypedDict, total=False):
    city: str

    country: str

    country_code: str

    state: str

    street: str

    type: str

    zip: str


class WhatsappMessageContactEmail(TypedDict, total=False):
    email: str

    type: str


class WhatsappMessageContactOrg(TypedDict, total=False):
    company: str

    department: str

    title: str


class WhatsappMessageContactPhone(TypedDict, total=False):
    phone: str

    type: str

    wa_id: str


class WhatsappMessageContactURL(TypedDict, total=False):
    type: str

    url: str


class WhatsappMessageContact(TypedDict, total=False):
    addresses: Iterable[WhatsappMessageContactAddress]

    birthday: str

    emails: Iterable[WhatsappMessageContactEmail]

    name: str

    org: WhatsappMessageContactOrg

    phones: Iterable[WhatsappMessageContactPhone]

    urls: Iterable[WhatsappMessageContactURL]


class WhatsappMessageInteractiveActionButtonReply(TypedDict, total=False):
    id: str
    """unique identifier for each button, 256 character maximum"""

    title: str
    """button label, 20 character maximum"""


class WhatsappMessageInteractiveActionButton(TypedDict, total=False):
    reply: WhatsappMessageInteractiveActionButtonReply

    type: Literal["reply"]


class WhatsappMessageInteractiveActionCardAction(TypedDict, total=False):
    catalog_id: str
    """the unique ID of the catalog"""

    product_retailer_id: str
    """the unique retailer ID of the product"""


class WhatsappMessageInteractiveActionCardBody(TypedDict, total=False):
    text: str
    """160 character maximum, up to 2 line breaks"""


class WhatsappMessageInteractiveActionCardHeader(TypedDict, total=False):
    image: WhatsappMediaParam

    type: Literal["image", "video"]

    video: WhatsappMediaParam


class WhatsappMessageInteractiveActionCard(TypedDict, total=False):
    action: WhatsappMessageInteractiveActionCardAction

    body: WhatsappMessageInteractiveActionCardBody

    card_index: int
    """unique index for each card (0-9)"""

    header: WhatsappMessageInteractiveActionCardHeader

    type: Literal["cta_url"]


class WhatsappMessageInteractiveActionParameters(TypedDict, total=False):
    display_text: str
    """button label text, 20 character maximum"""

    url: str
    """button URL to load when tapped by the user"""


class WhatsappMessageInteractiveActionSectionProductItem(TypedDict, total=False):
    product_retailer_id: str


class WhatsappMessageInteractiveActionSectionRow(TypedDict, total=False):
    id: str
    """arbitrary string identifying the row, 200 character maximum"""

    description: str
    """row description, 72 character maximum"""

    title: str
    """row title, 24 character maximum"""


class WhatsappMessageInteractiveActionSection(TypedDict, total=False):
    product_items: Iterable[WhatsappMessageInteractiveActionSectionProductItem]

    rows: Iterable[WhatsappMessageInteractiveActionSectionRow]

    title: str
    """section title, 24 character maximum"""


class WhatsappMessageInteractiveAction(TypedDict, total=False):
    button: str

    buttons: Iterable[WhatsappMessageInteractiveActionButton]

    cards: Iterable[WhatsappMessageInteractiveActionCard]

    catalog_id: str

    mode: str

    name: str

    parameters: WhatsappMessageInteractiveActionParameters

    product_retailer_id: str

    sections: Iterable[WhatsappMessageInteractiveActionSection]


class WhatsappMessageInteractiveBody(TypedDict, total=False):
    text: str
    """body text, 1024 character maximum"""


class WhatsappMessageInteractiveFooter(TypedDict, total=False):
    text: str
    """footer text, 60 character maximum"""


class WhatsappMessageInteractiveHeader(TypedDict, total=False):
    document: WhatsappMediaParam

    image: WhatsappMediaParam

    sub_text: str

    text: str
    """header text, 60 character maximum"""

    video: WhatsappMediaParam


class WhatsappMessageInteractive(TypedDict, total=False):
    action: WhatsappMessageInteractiveAction

    body: WhatsappMessageInteractiveBody

    footer: WhatsappMessageInteractiveFooter

    header: WhatsappMessageInteractiveHeader

    type: Literal["cta_url", "list", "carousel", "button", "location_request_message"]


class WhatsappMessageLocation(TypedDict, total=False):
    address: str

    latitude: str

    longitude: str

    name: str


class WhatsappMessageReaction(TypedDict, total=False):
    emoji: str

    message_id: str


class WhatsappMessage(TypedDict, total=False):
    audio: WhatsappMediaParam

    biz_opaque_callback_data: str
    """custom data to return with status update"""

    contacts: Iterable[WhatsappMessageContact]

    document: WhatsappMediaParam

    image: WhatsappMediaParam

    interactive: WhatsappMessageInteractive

    location: WhatsappMessageLocation

    reaction: WhatsappMessageReaction

    sticker: WhatsappMediaParam

    type: Literal[
        "audio", "document", "image", "sticker", "video", "interactive", "location", "template", "reaction", "contacts"
    ]

    video: WhatsappMediaParam
