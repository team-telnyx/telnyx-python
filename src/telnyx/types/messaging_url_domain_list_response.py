# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["MessagingURLDomainListResponse", "Data", "Meta"]


class Data(BaseModel):
    id: Optional[str] = None

    record_type: Optional[str] = None

    url_domain: Optional[str] = None

    use_case: Optional[str] = None


class Meta(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int


class MessagingURLDomainListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
