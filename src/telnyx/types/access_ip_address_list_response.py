# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .access_ip_address_response import AccessIPAddressResponse
from .pagination_meta_cloudflare_ip_list_sync import PaginationMetaCloudflareIPListSync

__all__ = ["AccessIPAddressListResponse"]


class AccessIPAddressListResponse(BaseModel):
    data: List[AccessIPAddressResponse]

    meta: PaginationMetaCloudflareIPListSync
