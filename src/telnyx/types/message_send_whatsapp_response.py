# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .whatsapp_media import WhatsappMedia

__all__ = [
    "MessageSendWhatsappResponse",
    "Data",
    "DataBody",
    "DataBodyContact",
    "DataBodyContactAddress",
    "DataBodyContactEmail",
    "DataBodyContactOrg",
    "DataBodyContactPhone",
    "DataBodyContactURL",
    "DataBodyInteractive",
    "DataBodyInteractiveAction",
    "DataBodyInteractiveActionButton",
    "DataBodyInteractiveActionButtonReply",
    "DataBodyInteractiveActionCard",
    "DataBodyInteractiveActionCardAction",
    "DataBodyInteractiveActionCardBody",
    "DataBodyInteractiveActionCardHeader",
    "DataBodyInteractiveActionParameters",
    "DataBodyInteractiveActionSection",
    "DataBodyInteractiveActionSectionProductItem",
    "DataBodyInteractiveActionSectionRow",
    "DataBodyInteractiveBody",
    "DataBodyInteractiveFooter",
    "DataBodyInteractiveHeader",
    "DataBodyLocation",
    "DataBodyReaction",
    "DataFrom",
    "DataTo",
]


class DataBodyContactAddress(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    country_code: Optional[str] = None

    state: Optional[str] = None

    street: Optional[str] = None

    type: Optional[str] = None

    zip: Optional[str] = None


class DataBodyContactEmail(BaseModel):
    email: Optional[str] = None

    type: Optional[str] = None


class DataBodyContactOrg(BaseModel):
    company: Optional[str] = None

    department: Optional[str] = None

    title: Optional[str] = None


class DataBodyContactPhone(BaseModel):
    phone: Optional[str] = None

    type: Optional[str] = None

    wa_id: Optional[str] = None


class DataBodyContactURL(BaseModel):
    type: Optional[str] = None

    url: Optional[str] = None


class DataBodyContact(BaseModel):
    addresses: Optional[List[DataBodyContactAddress]] = None

    birthday: Optional[str] = None

    emails: Optional[List[DataBodyContactEmail]] = None

    name: Optional[str] = None

    org: Optional[DataBodyContactOrg] = None

    phones: Optional[List[DataBodyContactPhone]] = None

    urls: Optional[List[DataBodyContactURL]] = None


class DataBodyInteractiveActionButtonReply(BaseModel):
    id: Optional[str] = None
    """unique identifier for each button, 256 character maximum"""

    title: Optional[str] = None
    """button label, 20 character maximum"""


class DataBodyInteractiveActionButton(BaseModel):
    reply: Optional[DataBodyInteractiveActionButtonReply] = None

    type: Optional[Literal["reply"]] = None


class DataBodyInteractiveActionCardAction(BaseModel):
    catalog_id: Optional[str] = None
    """the unique ID of the catalog"""

    product_retailer_id: Optional[str] = None
    """the unique retailer ID of the product"""


class DataBodyInteractiveActionCardBody(BaseModel):
    text: Optional[str] = None
    """160 character maximum, up to 2 line breaks"""


class DataBodyInteractiveActionCardHeader(BaseModel):
    image: Optional[WhatsappMedia] = None

    type: Optional[Literal["image", "video"]] = None

    video: Optional[WhatsappMedia] = None


class DataBodyInteractiveActionCard(BaseModel):
    action: Optional[DataBodyInteractiveActionCardAction] = None

    body: Optional[DataBodyInteractiveActionCardBody] = None

    card_index: Optional[int] = None
    """unique index for each card (0-9)"""

    header: Optional[DataBodyInteractiveActionCardHeader] = None

    type: Optional[Literal["cta_url"]] = None


class DataBodyInteractiveActionParameters(BaseModel):
    display_text: Optional[str] = None
    """button label text, 20 character maximum"""

    url: Optional[str] = None
    """button URL to load when tapped by the user"""


class DataBodyInteractiveActionSectionProductItem(BaseModel):
    product_retailer_id: Optional[str] = None


class DataBodyInteractiveActionSectionRow(BaseModel):
    id: Optional[str] = None
    """arbitrary string identifying the row, 200 character maximum"""

    description: Optional[str] = None
    """row description, 72 character maximum"""

    title: Optional[str] = None
    """row title, 24 character maximum"""


class DataBodyInteractiveActionSection(BaseModel):
    product_items: Optional[List[DataBodyInteractiveActionSectionProductItem]] = None

    rows: Optional[List[DataBodyInteractiveActionSectionRow]] = None

    title: Optional[str] = None
    """section title, 24 character maximum"""


class DataBodyInteractiveAction(BaseModel):
    button: Optional[str] = None

    buttons: Optional[List[DataBodyInteractiveActionButton]] = None

    cards: Optional[List[DataBodyInteractiveActionCard]] = None

    catalog_id: Optional[str] = None

    mode: Optional[str] = None

    name: Optional[str] = None

    parameters: Optional[DataBodyInteractiveActionParameters] = None

    product_retailer_id: Optional[str] = None

    sections: Optional[List[DataBodyInteractiveActionSection]] = None


class DataBodyInteractiveBody(BaseModel):
    text: Optional[str] = None
    """body text, 1024 character maximum"""


class DataBodyInteractiveFooter(BaseModel):
    text: Optional[str] = None
    """footer text, 60 character maximum"""


class DataBodyInteractiveHeader(BaseModel):
    document: Optional[WhatsappMedia] = None

    image: Optional[WhatsappMedia] = None

    sub_text: Optional[str] = None

    text: Optional[str] = None
    """header text, 60 character maximum"""

    video: Optional[WhatsappMedia] = None


class DataBodyInteractive(BaseModel):
    action: Optional[DataBodyInteractiveAction] = None

    body: Optional[DataBodyInteractiveBody] = None

    footer: Optional[DataBodyInteractiveFooter] = None

    header: Optional[DataBodyInteractiveHeader] = None

    type: Optional[Literal["cta_url", "list", "carousel", "button", "location_request_message"]] = None


class DataBodyLocation(BaseModel):
    address: Optional[str] = None

    latitude: Optional[str] = None

    longitude: Optional[str] = None

    name: Optional[str] = None


class DataBodyReaction(BaseModel):
    emoji: Optional[str] = None

    message_id: Optional[str] = None


class DataBody(BaseModel):
    audio: Optional[WhatsappMedia] = None

    biz_opaque_callback_data: Optional[str] = None
    """custom data to return with status update"""

    contacts: Optional[List[DataBodyContact]] = None

    document: Optional[WhatsappMedia] = None

    image: Optional[WhatsappMedia] = None

    interactive: Optional[DataBodyInteractive] = None

    location: Optional[DataBodyLocation] = None

    reaction: Optional[DataBodyReaction] = None

    sticker: Optional[WhatsappMedia] = None

    type: Optional[
        Literal[
            "audio",
            "document",
            "image",
            "sticker",
            "video",
            "interactive",
            "location",
            "template",
            "reaction",
            "contacts",
        ]
    ] = None

    video: Optional[WhatsappMedia] = None


class DataFrom(BaseModel):
    carrier: Optional[str] = None
    """The carrier of the sender."""

    line_type: Optional[Literal["Wireline", "Wireless", "VoWiFi", "VoIP", "Pre-Paid Wireless", ""]] = None
    """The line-type of the sender."""

    phone_number: Optional[str] = None
    """
    Sending address (+E.164 formatted phone number, alphanumeric sender ID, or short
    code).
    """

    status: Optional[Literal["received", "delivered"]] = None


class DataTo(BaseModel):
    carrier: Optional[str] = None

    line_type: Optional[str] = None

    phone_number: Optional[str] = None

    status: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None
    """message ID"""

    body: Optional[DataBody] = None

    direction: Optional[str] = None

    encoding: Optional[str] = None

    from_: Optional[DataFrom] = FieldInfo(alias="from", default=None)

    messaging_profile_id: Optional[str] = None

    organization_id: Optional[str] = None

    received_at: Optional[datetime] = None

    record_type: Optional[str] = None

    to: Optional[List[DataTo]] = None

    type: Optional[str] = None


class MessageSendWhatsappResponse(BaseModel):
    data: Optional[Data] = None
