# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageSendWithAlphanumericSenderParams"]


class MessageSendWithAlphanumericSenderParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """A valid alphanumeric sender ID on the user's account."""

    messaging_profile_id: Required[str]
    """The messaging profile ID to use."""

    text: Required[str]
    """The message body."""

    to: Required[str]
    """Receiving address (+E.164 formatted phone number)."""

    use_profile_webhooks: bool
    """If true, use the messaging profile's webhook settings."""

    webhook_failover_url: Optional[str]
    """Failover callback URL for delivery status updates."""

    webhook_url: Optional[str]
    """Callback URL for delivery status updates."""
