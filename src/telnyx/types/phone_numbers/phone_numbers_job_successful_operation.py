# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["PhoneNumbersJobSuccessfulOperation"]


class PhoneNumbersJobSuccessfulOperation(BaseModel):
    id: Optional[str] = None
    """The phone number's ID"""

    phone_number: Optional[str] = None
    """The phone number in e164 format."""
