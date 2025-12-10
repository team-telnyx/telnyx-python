# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .pagination_response import PaginationResponse
from .billing_bundle_summary import BillingBundleSummary

__all__ = ["BillingBundleListResponse"]


class BillingBundleListResponse(BaseModel):
    data: List[BillingBundleSummary]

    meta: PaginationResponse
