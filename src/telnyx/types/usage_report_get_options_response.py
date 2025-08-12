# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UsageReportGetOptionsResponse", "Data"]


class Data(BaseModel):
    product: Optional[str] = None
    """Telnyx Product"""

    product_dimensions: Optional[List[str]] = None
    """Telnyx Product Dimensions"""

    product_metrics: Optional[List[str]] = None
    """Telnyx Product Metrics"""

    record_types: Optional[List[Literal["custom_storage_credentials"]]] = None
    """Subproducts if applicable"""


class UsageReportGetOptionsResponse(BaseModel):
    data: Optional[List[Data]] = None
    """Collection of product description"""
