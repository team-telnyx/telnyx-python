# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MessagingURLDomainListResponse"]


class MessagingURLDomainListResponse(BaseModel):
    id: Optional[str] = None

    record_type: Optional[str] = None

    url_domain: Optional[str] = None

    use_case: Optional[str] = None
