# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .whatsapp_message_content_param import WhatsappMessageContentParam

__all__ = ["MessageSendWhatsappParams"]


class MessageSendWhatsappParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Phone number in +E.164 format associated with Whatsapp account"""

    to: Required[str]
    """Phone number in +E.164 format"""

    whatsapp_message: Required[WhatsappMessageContentParam]

    messaging_profile_id: str
    """Messaging profile ID - required if the 'from' number is not SMS-enabled"""

    type: Literal["WHATSAPP"]
    """Message type - must be set to "WHATSAPP" """

    webhook_url: str
    """The URL where webhooks related to this message will be sent."""
