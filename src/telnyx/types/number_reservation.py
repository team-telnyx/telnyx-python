# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .reserved_phone_number import ReservedPhoneNumber

__all__ = ["NumberReservation"]


class NumberReservation(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None
    """An ISO 8901 datetime string denoting when the numbers reservation was created."""

    customer_reference: Optional[str] = None
    """A customer reference string for customer look ups."""

    phone_numbers: Optional[List[ReservedPhoneNumber]] = None

    record_type: Optional[str] = None

    status: Optional[Literal["pending", "success", "failure"]] = None
    """The status of the entire reservation."""

    updated_at: Optional[datetime] = None
    """An ISO 8901 datetime string for when the number reservation was updated."""
