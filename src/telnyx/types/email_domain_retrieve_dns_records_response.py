# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel
from .dns_record import DNSRecord

__all__ = ["EmailDomainRetrieveDNSRecordsResponse"]


class EmailDomainRetrieveDNSRecordsResponse(BaseModel):
    data: List[DNSRecord]
