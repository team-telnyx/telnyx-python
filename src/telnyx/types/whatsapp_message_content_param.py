# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .whatsapp_media_param import WhatsappMediaParam
from .whatsapp_contact_param import WhatsappContactParam
from .whatsapp_location_param import WhatsappLocationParam
from .whatsapp_reaction_param import WhatsappReactionParam
from .whatsapp_interactive_param import WhatsappInteractiveParam

__all__ = ["WhatsappMessageContentParam"]


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

    type: Literal[
        "audio", "document", "image", "sticker", "video", "interactive", "location", "template", "reaction", "contacts"
    ]

    video: WhatsappMediaParam
