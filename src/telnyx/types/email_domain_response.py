# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .email_domain import EmailDomain

__all__ = ["EmailDomainResponse"]


class EmailDomainResponse(BaseModel):
    data: EmailDomain
