# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubNumberOrdersReportCreateParams"]


class SubNumberOrdersReportCreateParams(TypedDict, total=False):
    country_code: str
    """Filter by country code"""

    created_at_gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter for orders created after this date"""

    created_at_lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter for orders created before this date"""

    customer_reference: str
    """Filter by customer reference"""

    order_request_id: str
    """Filter by specific order request ID"""

    status: Literal["pending", "success", "failure"]
    """Filter by order status"""
