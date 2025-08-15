# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReservedPhoneNumber"]


class ReservedPhoneNumber(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None
    """
    An ISO 8901 datetime string denoting when the individual number reservation was
    created.
    """

    expired_at: Optional[datetime] = None
    """
    An ISO 8901 datetime string for when the individual number reservation is going
    to expire
    """

    phone_number: Optional[str] = None

    record_type: Optional[str] = None

    status: Optional[Literal["pending", "success", "failure"]] = None
    """The status of the phone number's reservation."""

    updated_at: Optional[datetime] = None
    """
    An ISO 8901 datetime string for when the the individual number reservation was
    updated.
    """
