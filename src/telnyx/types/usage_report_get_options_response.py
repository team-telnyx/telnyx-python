# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["UsageReportGetOptionsResponse", "Data", "DataRecordType"]


class DataRecordType(BaseModel):
    """
    An object following one of the schemas published in https://developers.telnyx.com/docs/api/v2/detail-records
    """

    product_dimensions: Optional[List[str]] = None
    """Telnyx Product Dimensions"""

    product_metrics: Optional[List[str]] = None
    """Telnyx Product Metrics"""

    record_type: Optional[str] = None
    """Telnyx Product type"""


class Data(BaseModel):
    """
    An object following one of the schemas published in https://developers.telnyx.com/docs/api/v2/detail-records
    """

    product: Optional[str] = None
    """Telnyx Product"""

    product_dimensions: Optional[List[str]] = None
    """Telnyx Product Dimensions"""

    product_metrics: Optional[List[str]] = None
    """Telnyx Product Metrics"""

    record_types: Optional[List[DataRecordType]] = None
    """Subproducts if applicable"""


class UsageReportGetOptionsResponse(BaseModel):
    """
    An object following one of the schemas published in https://developers.telnyx.com/docs/api/v2/detail-records
    """

    data: Optional[List[Data]] = None
    """Collection of product description"""
