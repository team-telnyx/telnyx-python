# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .porting_order_end_user_admin import PortingOrderEndUserAdmin
from .porting_order_end_user_location import PortingOrderEndUserLocation

__all__ = ["PortingOrderEndUser"]


class PortingOrderEndUser(BaseModel):
    admin: Optional[PortingOrderEndUserAdmin] = None

    location: Optional[PortingOrderEndUserLocation] = None
