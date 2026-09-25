# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .email_event_type import EmailEventType

__all__ = ["MessageEvent"]


class MessageEvent(BaseModel):
    """An event on the per-message events endpoint.

    The legacy event_type and additive canonical_event_type are email.-prefixed. The deprecated type preserves the bare stored event name for compatibility.
    """

    canonical_event_type: str
    """Additive canonical outcome name, prefixed with `email.`.

    Gateway rejection is `email.gw_reject`, ambiguous injection timeout is
    `email.injection_timeout`, and MTA expiration is `email.expired`. Unchanged
    outcomes retain their names. Existing stored rows are translated only when
    recorded payload evidence proves the outcome; a legacy failed row is not guessed
    or sharpened.
    """

    event_type: str
    """Legacy customer-visible event name, prefixed with `email.`.

    Gateway rejections render `email.failed`; MTA expirations render
    `email.bounced`. Webhook subscription allowlists match the legacy name.
    """

    occurred_at: datetime

    type: EmailEventType
    """Bare stored event names returned by message history.

    In addition to the normal send and delivery lifecycle, polling can expose
    suppression, scan, and quarantine lifecycle rows. Sharp canonical names
    gw_reject, injection_timeout, and expired distinguish gateway rejection,
    ambiguous injection timeout, and MTA expiration. The failed and bounced names
    remain valid for system/admin failures and hard bounces respectively. Existing
    stored rows retain their original names.
    """

    payload: Optional[Dict[str, object]] = None
