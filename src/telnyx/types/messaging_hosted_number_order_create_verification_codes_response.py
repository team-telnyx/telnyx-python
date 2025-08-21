# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "MessagingHostedNumberOrderCreateVerificationCodesResponse",
    "Data",
    "DataVerificationCodeSuccess",
    "DataVerificationCodeError",
]


class DataVerificationCodeSuccess(BaseModel):
    phone_number: str
    """Phone number for which the verification code was created"""

    type: Literal["sms", "call", "flashcall"]
    """Type of verification method used"""

    verification_code_id: str
    """Unique identifier for the verification code"""


class DataVerificationCodeError(BaseModel):
    error: str
    """Error message describing why the verification code creation failed"""

    phone_number: str
    """Phone number for which the verification code creation failed"""


Data: TypeAlias = Union[DataVerificationCodeSuccess, DataVerificationCodeError]


class MessagingHostedNumberOrderCreateVerificationCodesResponse(BaseModel):
    data: List[Data]
