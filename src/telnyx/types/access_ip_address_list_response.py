# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .access_ip_address_response import AccessIPAddressResponse

__all__ = ["AccessIPAddressListResponse", "Meta"]


class Meta(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int


class AccessIPAddressListResponse(BaseModel):
    data: List[AccessIPAddressResponse]

    meta: Meta
