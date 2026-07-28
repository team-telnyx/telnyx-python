# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailBlock"]


class EmailBlock(BaseModel):
    """Suppression record.

    Schema fields hidden by the view:
    `account_id`, `bounce_category`, `dsn_code`, `meta`.
    """

    id: str

    created_at: datetime

    reason: Literal["hard_bounce", "spam_complaint", "unsubscribe", "invalid", "manual_block"]

    record_type: Literal["email_block"]
    """View-only discriminator."""

    scope: Literal["account", "domain", "address"]
    """Derived server-side from `domain_id`/`from`; never trusted from the caller."""

    source: Literal["feedback", "manual", "import", "system"]

    status: Literal["active", "expired", "removed"]

    to: str
    """Normalized recipient. (schema: to_address)"""

    updated_at: datetime

    domain_id: Optional[str] = None
    """`null` ⇒ account scope. Stored on the row; exposed here."""

    expires_at: Optional[datetime] = None

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """`null` ⇒ not address-scope. (schema: from_address)"""

    group_id: Optional[str] = None
    """`null` ⇒ global; set ⇒ group-scoped opt-out."""
