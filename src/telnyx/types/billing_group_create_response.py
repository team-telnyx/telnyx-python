# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .billing_group import BillingGroup

__all__ = ["BillingGroupCreateResponse"]


class BillingGroupCreateResponse(BaseModel):
    data: Optional[BillingGroup] = None
