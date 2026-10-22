# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MessageWhatsappParams",
    "WhatsappMessage",
    "WhatsappMessageContact",
    "WhatsappMessageContactAddress",
    "WhatsappMessageContactEmail",
    "WhatsappMessageContactName",
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
    "WhatsappMessageInteractiveActionParametersFlowActionPayload",
    "WhatsappMessageInteractiveActionSection",
    "WhatsappMessageInteractiveActionSectionProductItem",
    "WhatsappMessageInteractiveActionSectionRow",
    "WhatsappMessageInteractiveBody",
    "WhatsappMessageInteractiveFooter",
    "WhatsappMessageInteractiveHeader",
    "WhatsappMessageTemplate",
    "WhatsappMessageTemplateComponent",
    "WhatsappMessageTemplateComponentParameter",
    "WhatsappMessageTemplateComponentParameterAction",
    "WhatsappMessageTemplateLanguage",
    "WhatsappMessageText",
]


class MessageWhatsappParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Phone number in +E.164 format associated with Whatsapp account"""

    to: Required[str]
    """
    Recipient phone number in +E.164 format, or the business-scoped user ID (BSUID)
    of a WhatsApp user who hides their phone number, for example
    `US.13491208655302741918`. Authentication templates cannot be sent to a BSUID.
    """

    whatsapp_message: Required[WhatsappMessage]

    messaging_profile_id: str
    """Messaging profile ID - required if the 'from' number is not SMS-enabled"""

    type: Literal["WHATSAPP"]
    """Message type - must be set to "WHATSAPP" """

    webhook_url: str
    """The URL where webhooks related to this message will be sent."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


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


class WhatsappMessageContactName(TypedDict, total=False):
    formatted_name: Required[str]
    """contact's full name as displayed in the message"""

    first_name: str

    last_name: str

    middle_name: str

    prefix: str

    suffix: str


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

    name: WhatsappMessageContactName

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
    image: "WhatsappMediaParam"

    type: Literal["image", "video"]

    video: "WhatsappMediaParam"


class WhatsappMessageInteractiveActionCard(TypedDict, total=False):
    action: WhatsappMessageInteractiveActionCardAction

    body: WhatsappMessageInteractiveActionCardBody

    card_index: int
    """unique index for each card (0-9)"""

    header: WhatsappMessageInteractiveActionCardHeader

    type: Literal["cta_url"]


class WhatsappMessageInteractiveActionParametersFlowActionPayload(TypedDict, total=False):
    """optional initial screen and data.

    When omitted, the flow opens on its first entry screen. Must be omitted when flow_action is data_exchange
    """

    data: object
    """input data for the first screen. Must be a non-empty object when provided"""

    screen: str
    """ID of the first screen to show"""


class WhatsappMessageInteractiveActionParameters(TypedDict, total=False):
    display_text: str
    """button label text, 20 character maximum"""

    flow_action: Literal["navigate", "data_exchange"]
    """how the flow starts.

    navigate opens the screen in flow_action_payload; data_exchange requests the
    first screen from the business's flow endpoint. Defaults to navigate
    """

    flow_action_payload: WhatsappMessageInteractiveActionParametersFlowActionPayload
    """optional initial screen and data.

    When omitted, the flow opens on its first entry screen. Must be omitted when
    flow_action is data_exchange
    """

    flow_cta: str
    """text of the button that opens the flow, 1-20 characters, no emoji.

    Required for flow messages
    """

    flow_id: str
    """ID of the flow to open. Provide exactly one of flow_id or flow_name"""

    flow_message_version: str
    """flow message version, must be 3. Required for flow messages"""

    flow_name: str
    """name of the flow to open. Provide exactly one of flow_id or flow_name"""

    flow_token: str
    """business-generated identifier for the flow session.

    Returned in the flow response for correlation
    """

    mode: Literal["draft", "published"]
    """use draft to test an unpublished flow. Defaults to published"""

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
    type: Required[Literal["document", "image", "text", "video"]]
    """header type.

    Required when a header is provided; the matching document, image, text, or video
    field must be set
    """

    document: "WhatsappMediaParam"

    image: "WhatsappMediaParam"

    sub_text: str

    text: str
    """header text, 60 character maximum"""

    video: "WhatsappMediaParam"


class WhatsappMessageInteractive(TypedDict, total=False):
    action: WhatsappMessageInteractiveAction

    body: WhatsappMessageInteractiveBody

    footer: WhatsappMessageInteractiveFooter

    header: WhatsappMessageInteractiveHeader

    type: Literal["cta_url", "list", "carousel", "button", "location_request_message", "flow"]


class WhatsappMessageTemplateComponentParameterAction(TypedDict, total=False):
    """Flow button parameters. Used with type action on a flow button component"""

    flow_action_data: object
    """input data for the first screen of the flow"""

    flow_token: str
    """business-generated identifier for the flow session.

    Returned in the flow response for correlation
    """


class WhatsappMessageTemplateComponentParameter(TypedDict, total=False):
    action: WhatsappMessageTemplateComponentParameterAction
    """Flow button parameters. Used with type action on a flow button component"""

    text: str

    type: Literal["text", "image", "video", "document", "currency", "date_time", "action"]


class WhatsappMessageTemplateComponent(TypedDict, total=False):
    index: int
    """Button index (required for button components)"""

    parameters: Iterable[WhatsappMessageTemplateComponentParameter]

    sub_type: Literal["quick_reply", "url", "flow"]

    type: Literal["header", "body", "button"]


class WhatsappMessageTemplateLanguage(TypedDict, total=False):
    """Template language. Required unless template_id is provided."""

    code: Required[str]
    """Language code (e.g. en_US)"""

    policy: str


class WhatsappMessageTemplate(TypedDict, total=False):
    """Template message object.

    Provide either template_id or name + language to identify the template.
    """

    components: Iterable[WhatsappMessageTemplateComponent]
    """Template parameter values for header, body, and button components."""

    language: WhatsappMessageTemplateLanguage
    """Template language. Required unless template_id is provided."""

    name: str
    """Template name as registered with Meta. Required unless template_id is provided."""

    template_id: str
    """Telnyx template ID (the id field from template list/get responses).

    When provided, name and language are resolved automatically.
    """


class WhatsappMessageText(TypedDict, total=False):
    """Text message content.

    Can only be sent within a 24-hour customer service window.
    """

    body: Required[str]
    """The text message body."""

    preview_url: bool
    """Whether to show a URL preview in the message."""


class WhatsappMessage(TypedDict, total=False):
    audio: "WhatsappMediaParam"

    biz_opaque_callback_data: str
    """custom data to return with status update"""

    contacts: Iterable[WhatsappMessageContact]

    document: "WhatsappMediaParam"

    image: "WhatsappMediaParam"

    interactive: WhatsappMessageInteractive

    location: "WhatsappLocationParam"

    reaction: "WhatsappReactionParam"

    sticker: "WhatsappMediaParam"

    template: WhatsappMessageTemplate
    """Template message object.

    Provide either template_id or name + language to identify the template.
    """

    text: WhatsappMessageText
    """Text message content.

    Can only be sent within a 24-hour customer service window.
    """

    type: Literal[
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
        "text",
    ]

    video: "WhatsappMediaParam"


from .whatsapp_media_param import WhatsappMediaParam
from .whatsapp_location_param import WhatsappLocationParam
from .whatsapp_reaction_param import WhatsappReactionParam
