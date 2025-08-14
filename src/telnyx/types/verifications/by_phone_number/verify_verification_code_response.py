# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["VerifyVerificationCodeResponse", "Data"]


class Data(BaseModel):
    phone_number: str
    """+E164 formatted phone number."""

    response_code: Literal["accepted", "rejected"]
    """Identifies if the verification code has been accepted or rejected."""


class VerifyVerificationCodeResponse(BaseModel):
    data: Data
