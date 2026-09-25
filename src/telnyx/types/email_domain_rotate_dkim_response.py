# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .dns_record import DNSRecord

__all__ = ["EmailDomainRotateDkimResponse", "Data", "DataDkim", "DataPreviousDkimKey"]


class DataDkim(BaseModel):
    """The new active DKIM key."""

    id: str

    algorithm: Literal["rsa-sha256"]

    key_length: Literal[2048]

    selector: str

    status: Literal["active"]

    version: int
    """Monotonically increasing per-domain key version."""

    activated_at: Optional[datetime] = None


class DataPreviousDkimKey(BaseModel):
    """
    The retired previous key, or null when the domain had no active key before rotation. Retained in a `retiring` state so it can be revoked after the DNS propagation grace period.
    """

    id: str

    selector: str

    status: Literal["retiring", "revoked"]

    version: int


class Data(BaseModel):
    """Result of rotating a domain's DKIM key.

    The new key is active and signing switches to it immediately; the previous key is retired to a `retiring` state (retained, not revoked) so it can be revoked after the DNS propagation grace period. Selectors are fixed, so the DKIM DNS record's TXT value is replaced in place at the shared `<selector>._domainkey.<domain>` host — `old_selector_retained` is false and the returned dns_records carry the new value the customer must publish promptly.
    """

    dkim: DataDkim
    """The new active DKIM key."""

    dns_records: List[DNSRecord]
    """
    The DKIM DNS records the customer must publish, carrying the new key's TXT value
    with verification reset to pending.
    """

    domain: str

    domain_id: str

    old_selector_retained: bool
    """
    False for this service: one selector is fixed per domain, so rotation replaces
    the TXT value at the existing \\__domainkey host. There is no dual-selector
    overlap; publish the replacement TXT promptly because signing switches
    immediately.
    """

    previous_dkim_key: Optional[DataPreviousDkimKey] = None
    """
    The retired previous key, or null when the domain had no active key before
    rotation. Retained in a `retiring` state so it can be revoked after the DNS
    propagation grace period.
    """

    record_type: Literal["email_domain_dkim_rotation"]


class EmailDomainRotateDkimResponse(BaseModel):
    data: Data
    """Result of rotating a domain's DKIM key.

    The new key is active and signing switches to it immediately; the previous key
    is retired to a `retiring` state (retained, not revoked) so it can be revoked
    after the DNS propagation grace period. Selectors are fixed, so the DKIM DNS
    record's TXT value is replaced in place at the shared
    `<selector>._domainkey.<domain>` host — `old_selector_retained` is false and the
    returned dns_records carry the new value the customer must publish promptly.
    """
