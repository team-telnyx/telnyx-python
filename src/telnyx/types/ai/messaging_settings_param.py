# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MessagingSettingsParam"]


class MessagingSettingsParam(TypedDict, total=False):
    default_messaging_profile_id: str
    """Default Messaging Profile used for messaging exchanges with your assistant.

    This will be created automatically on assistant creation.
    """

    delivery_status_webhook_url: str
    """
    The URL where webhooks related to delivery statused for assistant messages will
    be sent.
    """
