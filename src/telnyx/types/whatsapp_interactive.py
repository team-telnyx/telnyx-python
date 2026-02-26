# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .whatsapp_media import WhatsappMedia

__all__ = [
    "WhatsappInteractive",
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


class ActionButtonReply(BaseModel):
    id: Optional[str] = None
    """unique identifier for each button, 256 character maximum"""

    title: Optional[str] = None
    """button label, 20 character maximum"""


class ActionButton(BaseModel):
    reply: Optional[ActionButtonReply] = None

    type: Optional[Literal["reply"]] = None


class ActionCardAction(BaseModel):
    catalog_id: Optional[str] = None
    """the unique ID of the catalog"""

    product_retailer_id: Optional[str] = None
    """the unique retailer ID of the product"""


class ActionCardBody(BaseModel):
    text: Optional[str] = None
    """160 character maximum, up to 2 line breaks"""


class ActionCardHeader(BaseModel):
    image: Optional[WhatsappMedia] = None

    type: Optional[Literal["image", "video"]] = None

    video: Optional[WhatsappMedia] = None


class ActionCard(BaseModel):
    action: Optional[ActionCardAction] = None

    body: Optional[ActionCardBody] = None

    card_index: Optional[int] = None
    """unique index for each card (0-9)"""

    header: Optional[ActionCardHeader] = None

    type: Optional[Literal["cta_url"]] = None


class ActionParameters(BaseModel):
    display_text: Optional[str] = None
    """button label text, 20 character maximum"""

    url: Optional[str] = None
    """button URL to load when tapped by the user"""


class ActionSectionProductItem(BaseModel):
    product_retailer_id: Optional[str] = None


class ActionSectionRow(BaseModel):
    id: Optional[str] = None
    """arbitrary string identifying the row, 200 character maximum"""

    description: Optional[str] = None
    """row description, 72 character maximum"""

    title: Optional[str] = None
    """row title, 24 character maximum"""


class ActionSection(BaseModel):
    product_items: Optional[List[ActionSectionProductItem]] = None

    rows: Optional[List[ActionSectionRow]] = None

    title: Optional[str] = None
    """section title, 24 character maximum"""


class Action(BaseModel):
    button: Optional[str] = None

    buttons: Optional[List[ActionButton]] = None

    cards: Optional[List[ActionCard]] = None

    catalog_id: Optional[str] = None

    mode: Optional[str] = None

    name: Optional[str] = None

    parameters: Optional[ActionParameters] = None

    product_retailer_id: Optional[str] = None

    sections: Optional[List[ActionSection]] = None


class Body(BaseModel):
    text: Optional[str] = None
    """body text, 1024 character maximum"""


class Footer(BaseModel):
    text: Optional[str] = None
    """footer text, 60 character maximum"""


class Header(BaseModel):
    document: Optional[WhatsappMedia] = None

    image: Optional[WhatsappMedia] = None

    sub_text: Optional[str] = None

    text: Optional[str] = None
    """header text, 60 character maximum"""

    video: Optional[WhatsappMedia] = None


class WhatsappInteractive(BaseModel):
    action: Optional[Action] = None

    body: Optional[Body] = None

    footer: Optional[Footer] = None

    header: Optional[Header] = None

    type: Optional[Literal["cta_url", "list", "carousel", "button", "location_request_message"]] = None
