# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .dns_record import DNSRecord
from .email_domain_type import EmailDomainType
from .email_dmarc_policy import EmailDmarcPolicy
from .email_domain_status import EmailDomainStatus
from .domains_tracking_settings import DomainsTrackingSettings
from .email_domain_verification import EmailDomainVerification

__all__ = ["EmailDomain", "Dkim", "Inbound", "Reputation"]


class Dkim(BaseModel):
    active: bool

    algorithm: Optional[Literal["rsa-sha256"]] = None

    key_length: Optional[Literal[2048]] = None

    rotated_at: Optional[datetime] = None

    selector: Optional[str] = None


class Inbound(BaseModel):
    catch_all: bool

    enabled: bool

    mx_required: bool


class Reputation(BaseModel):
    """Sender reputation for this domain (present on all domain responses)."""

    band: Optional[str] = None
    """Reputation band, e.g. good/warn/poor."""

    breakdown: Optional[Dict[str, object]] = None

    computed_at: Optional[datetime] = None


class EmailDomain(BaseModel):
    id: str

    created_at: datetime

    dkim: Dkim

    dmarc_policy: Optional[EmailDmarcPolicy] = None
    """DMARC policy for a sending domain.

    Drives the recommended \\__dmarc.<domain> TXT record. DMARC is advisory and never
    blocks sending. When omitted or null, the domain uses the advisory default
    (v=DMARC1; p=none; rua=mailto:dmarc@telnyx.com).
    """

    dns_records: List[DNSRecord]

    domain: str

    inbound: Inbound

    record_type: Literal["email_domain"]

    status: EmailDomainStatus

    tracking: DomainsTrackingSettings

    type: EmailDomainType
    """Domain type.

    `custom` domains are account-owned (BYOD). `shared` domains are Telnyx-managed,
    visible to and usable by ALL accounts for sending, but read-only: only the
    owning (system) account may modify, verify, or delete them; other accounts
    receive 403 (code 10008).
    """

    updated_at: datetime

    usable_for_inbound: bool

    usable_for_sending: bool

    verification: EmailDomainVerification

    reputation: Optional[Reputation] = None
    """Sender reputation for this domain (present on all domain responses)."""

    verified_at: Optional[datetime] = None
