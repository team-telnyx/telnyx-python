# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .billing_group import BillingGroup

__all__ = ["BillingGroupRetrieveResponse"]


class BillingGroupRetrieveResponse(BaseModel):
    data: Optional[BillingGroup] = None
