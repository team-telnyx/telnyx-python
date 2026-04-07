# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .whatsapp_media_param import WhatsappMediaParam
from .whatsapp_contact_param import WhatsappContactParam
from .whatsapp_location_param import WhatsappLocationParam
from .whatsapp_reaction_param import WhatsappReactionParam
from .whatsapp_interactive_param import WhatsappInteractiveParam

__all__ = [
    "WhatsappMessageContentParam",
    "Template",
    "TemplateComponent",
    "TemplateComponentParameter",
    "TemplateLanguage",
    "Text",
]


class TemplateComponentParameter(TypedDict, total=False):
    text: str

    type: Literal["text", "image", "video", "document", "currency", "date_time"]


class TemplateComponent(TypedDict, total=False):
    index: int
    """Button index (required for button components)"""

    parameters: Iterable[TemplateComponentParameter]

    sub_type: Literal["quick_reply", "url"]

    type: Literal["header", "body", "button"]


class TemplateLanguage(TypedDict, total=False):
    """Template language. Required unless template_id is provided."""

    code: Required[str]
    """Language code (e.g. en_US)"""

    policy: str


class Template(TypedDict, total=False):
    """Template message object.

    Provide either template_id or name + language to identify the template.
    """

    components: Iterable[TemplateComponent]
    """Template parameter values for header, body, and button components."""

    language: TemplateLanguage
    """Template language. Required unless template_id is provided."""

    name: str
    """Template name as registered with Meta. Required unless template_id is provided."""

    template_id: str
    """Telnyx template ID (the id field from template list/get responses).

    When provided, name and language are resolved automatically.
    """


class Text(TypedDict, total=False):
    """Text message content.

    Can only be sent within a 24-hour customer service window.
    """

    body: Required[str]
    """The text message body."""

    preview_url: bool
    """Whether to show a URL preview in the message."""


class WhatsappMessageContentParam(TypedDict, total=False):
    audio: WhatsappMediaParam

    biz_opaque_callback_data: str
    """custom data to return with status update"""

    contacts: Iterable[WhatsappContactParam]

    document: WhatsappMediaParam

    image: WhatsappMediaParam

    interactive: WhatsappInteractiveParam

    location: WhatsappLocationParam

    reaction: WhatsappReactionParam

    sticker: WhatsappMediaParam

    template: Template
    """Template message object.

    Provide either template_id or name + language to identify the template.
    """

    text: Text
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

    video: WhatsappMediaParam
