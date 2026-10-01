# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["WebsocketSettings"]


class WebsocketSettings(BaseModel):
    """
    Streams conversation and telephony events to a WebSocket server you host, and accepts messages injected back into the conversation. Telnyx opens the connection as a client, once per conversation. Delivery is best effort throughout: while the connection is down events are dropped rather than queued, and no socket failure is ever allowed to affect the call. Beta feature.
    """

    auth_ref: Optional[str] = None
    """
    Integration secret identifier whose value Telnyx sends as an
    `Authorization: Bearer <value>` header on the upgrade request. Resolved on every
    connection attempt, so a rotated secret is picked up by the next reconnect.
    """

    enabled: Optional[bool] = None
    """
    Whether Telnyx opens a WebSocket to `url` for each of this assistant's
    conversations. Defaults to `false`.
    """

    url: Optional[str] = None
    """The `ws://` or `wss://` endpoint Telnyx connects to.

    Required when `enabled` is `true`. Must be externally reachable — localhost,
    private IP ranges and `.local` domains are rejected.
    """
