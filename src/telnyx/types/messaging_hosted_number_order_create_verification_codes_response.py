# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessagingHostedNumberOrderCreateVerificationCodesResponse", "Data"]


class Data(BaseModel):
    """Verification code result response"""

    phone_number: str
    """Phone number for which the verification code was created"""

    error: Optional[str] = None
    """Error message describing why the verification code creation failed"""

    type: Optional[Literal["sms", "call", "flashcall"]] = None
    """Type of verification method used"""

    verification_code_id: Optional[str] = None
    """Unique identifier for the verification code"""


class MessagingHostedNumberOrderCreateVerificationCodesResponse(BaseModel):
    data: List[Data]
