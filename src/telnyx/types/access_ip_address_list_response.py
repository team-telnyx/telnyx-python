# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .access_ip_address_response import AccessIPAddressResponse

__all__ = ["AccessIPAddressListResponse"]


class AccessIPAddressListResponse(BaseModel):
    data: List[AccessIPAddressResponse]

    meta: PaginationMeta
