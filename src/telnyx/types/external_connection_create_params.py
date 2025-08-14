# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalConnectionCreateParams", "Outbound", "Inbound"]


class ExternalConnectionCreateParams(TypedDict, total=False):
    external_sip_connection: Required[Literal["zoom"]]
    """The service that will be consuming this connection."""

    outbound: Required[Outbound]

    active: bool
    """Specifies whether the connection can be used."""

    inbound: Inbound

    tags: List[str]
    """Tags associated with the connection."""

    webhook_event_failover_url: Optional[str]
    """
    The failover URL where webhooks related to this connection will be sent if
    sending to the primary URL fails. Must include a scheme, such as 'https'.
    """

    webhook_event_url: str
    """The URL where webhooks related to this connection will be sent.

    Must include a scheme, such as 'https'.
    """

    webhook_timeout_secs: Optional[int]
    """Specifies how many seconds to wait before timing out a webhook."""


class Outbound(TypedDict, total=False):
    channel_limit: int
    """
    When set, this will limit the number of concurrent outbound calls to phone
    numbers associated with this connection.
    """

    outbound_voice_profile_id: str
    """Identifies the associated outbound voice profile."""


class Inbound(TypedDict, total=False):
    channel_limit: int
    """
    When set, this will limit the number of concurrent inbound calls to phone
    numbers associated with this connection.
    """
