# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .porting_orders_exception_type import PortingOrdersExceptionType

__all__ = ["PortingOrderStatus"]


class PortingOrderStatus(BaseModel):
    details: Optional[List[PortingOrdersExceptionType]] = None
    """A list of 0 or more details about this porting order's status"""

    value: Optional[
        Literal[
            "draft",
            "in-process",
            "submitted",
            "exception",
            "foc-date-confirmed",
            "ported",
            "cancelled",
            "cancel-pending",
        ]
    ] = None
    """The current status of the porting order"""
