# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..porting_orders_activation_job import PortingOrdersActivationJob

__all__ = ["ActivationJobUpdateResponse"]


class ActivationJobUpdateResponse(BaseModel):
    data: Optional[PortingOrdersActivationJob] = None
