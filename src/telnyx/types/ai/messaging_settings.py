# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MessagingSettings"]


class MessagingSettings(BaseModel):
    default_messaging_profile_id: Optional[str] = None
    """Default Messaging Profile used for messaging exchanges with your assistant.

    This will be created automatically on assistant creation.
    """

    delivery_status_webhook_url: Optional[str] = None
    """
    The URL where webhooks related to delivery statused for assistant messages will
    be sent.
    """
