# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessagingHostedNumberOrderValidateCodesResponse", "Data", "DataPhoneNumber"]


class DataPhoneNumber(BaseModel):
    phone_number: str

    status: Literal["verified", "rejected", "already_verified"]


class Data(BaseModel):
    order_id: str

    phone_numbers: List[DataPhoneNumber]


class MessagingHostedNumberOrderValidateCodesResponse(BaseModel):
    data: Optional[Data] = None
