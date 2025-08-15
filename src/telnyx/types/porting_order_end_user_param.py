# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .porting_order_end_user_admin_param import PortingOrderEndUserAdminParam
from .porting_order_end_user_location_param import PortingOrderEndUserLocationParam

__all__ = ["PortingOrderEndUserParam"]


class PortingOrderEndUserParam(TypedDict, total=False):
    admin: PortingOrderEndUserAdminParam

    location: PortingOrderEndUserLocationParam
