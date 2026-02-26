# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .whatsapp_media import WhatsappMedia
from .whatsapp_contact import WhatsappContact
from .whatsapp_location import WhatsappLocation
from .whatsapp_reaction import WhatsappReaction
from .whatsapp_interactive import WhatsappInteractive

__all__ = ["WhatsappMessageContent"]


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
