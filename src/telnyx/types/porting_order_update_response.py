# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .porting_order import PortingOrder

__all__ = ["PortingOrderUpdateResponse", "Meta"]


class Meta(BaseModel):
    phone_numbers_url: Optional[str] = None
    """Link to list all phone numbers"""


class PortingOrderUpdateResponse(BaseModel):
    data: Optional[PortingOrder] = None

    meta: Optional[Meta] = None
