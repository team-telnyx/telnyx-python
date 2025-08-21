# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .customer_service_record import CustomerServiceRecord

__all__ = ["CustomerServiceRecordRetrieveResponse"]


class CustomerServiceRecordRetrieveResponse(BaseModel):
    data: Optional[CustomerServiceRecord] = None
