# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..porting_orders_activation_job import PortingOrdersActivationJob

__all__ = ["ActionActivateResponse"]


class ActionActivateResponse(BaseModel):
    data: Optional[PortingOrdersActivationJob] = None
