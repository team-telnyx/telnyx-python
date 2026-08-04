# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .email_domain_verification import EmailDomainVerification

__all__ = ["EmailDomainRetrieveHealthResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier for the email domain"""

    checked_at: datetime
    """Timestamp of the last health check"""

    record_type: Literal["email_domain_health"]
    """Record type discriminator"""

    status: Literal["pending", "verifying", "verified", "failed", "degraded", "suspended"]
    """Current domain status"""

    usable_for_inbound: bool
    """Whether the domain is usable for receiving inbound email"""

    usable_for_sending: bool
    """Whether the domain is usable for sending email"""

    verification: EmailDomainVerification


class EmailDomainRetrieveHealthResponse(BaseModel):
    data: Data
