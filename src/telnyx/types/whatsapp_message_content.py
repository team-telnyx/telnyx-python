# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .whatsapp_media import WhatsappMedia
from .whatsapp_contact import WhatsappContact
from .whatsapp_location import WhatsappLocation
from .whatsapp_reaction import WhatsappReaction
from .whatsapp_interactive import WhatsappInteractive

__all__ = [
    "WhatsappMessageContent",
    "Template",
    "TemplateComponent",
    "TemplateComponentParameter",
    "TemplateLanguage",
    "Text",
]


class TemplateComponentParameter(BaseModel):
    text: Optional[str] = None

    type: Optional[Literal["text", "image", "video", "document", "currency", "date_time"]] = None


class TemplateComponent(BaseModel):
    index: Optional[int] = None
    """Button index (required for button components)"""

    parameters: Optional[List[TemplateComponentParameter]] = None

    sub_type: Optional[Literal["quick_reply", "url"]] = None

    type: Optional[Literal["header", "body", "button"]] = None


class TemplateLanguage(BaseModel):
    """Template language. Required unless template_id is provided."""

    code: str
    """Language code (e.g. en_US)"""

    policy: Optional[str] = None


class Template(BaseModel):
    """Template message object.

    Provide either template_id or name + language to identify the template.
    """

    components: Optional[List[TemplateComponent]] = None
    """Template parameter values for header, body, and button components."""

    language: Optional[TemplateLanguage] = None
    """Template language. Required unless template_id is provided."""

    name: Optional[str] = None
    """Template name as registered with Meta. Required unless template_id is provided."""

    template_id: Optional[str] = None
    """Telnyx template ID (the id field from template list/get responses).

    When provided, name and language are resolved automatically.
    """


class Text(BaseModel):
    """Text message content.

    Can only be sent within a 24-hour customer service window.
    """

    body: str
    """The text message body."""

    preview_url: Optional[bool] = None
    """Whether to show a URL preview in the message."""


class WhatsappMessageContent(BaseModel):
    audio: Optional[WhatsappMedia] = None

    biz_opaque_callback_data: Optional[str] = None
    """custom data to return with status update"""

    contacts: Optional[List[WhatsappContact]] = None

    document: Optional[WhatsappMedia] = None

    image: Optional[WhatsappMedia] = None

    interactive: Optional[WhatsappInteractive] = None

    location: Optional[WhatsappLocation] = None

    reaction: Optional[WhatsappReaction] = None

    sticker: Optional[WhatsappMedia] = None

    template: Optional[Template] = None
    """Template message object.

    Provide either template_id or name + language to identify the template.
    """

    text: Optional[Text] = None
    """Text message content.

    Can only be sent within a 24-hour customer service window.
    """

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
            "text",
        ]
    ] = None

    video: Optional[WhatsappMedia] = None
