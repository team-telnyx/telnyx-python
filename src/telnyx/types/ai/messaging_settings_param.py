# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MessagingSettingsParam"]


class MessagingSettingsParam(TypedDict, total=False):
    conversation_inactivity_minutes: int
    """
    If more than this many minutes have passed since the last message, the assistant
    will start a new conversation instead of continuing the existing one.
    """

    default_messaging_profile_id: str
    """Default Messaging Profile used for messaging exchanges with your assistant.

    This will be created automatically on assistant creation.
    """

    delivery_status_webhook_url: str
    """
    The URL where webhooks related to delivery statused for assistant messages will
    be sent.
    """
