# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NumberBlockOrder"]


class NumberBlockOrder(BaseModel):
    id: Optional[str] = None

    connection_id: Optional[str] = None
    """Identifies the connection associated to all numbers in the phone number block."""

    created_at: Optional[datetime] = None
    """An ISO 8901 datetime string denoting when the number order was created."""

    customer_reference: Optional[str] = None
    """A customer reference string for customer look ups."""

    messaging_profile_id: Optional[str] = None
    """
    Identifies the messaging profile associated to all numbers in the phone number
    block.
    """

    phone_numbers_count: Optional[int] = None
    """The count of phone numbers in the number order."""

    range: Optional[int] = None
    """The phone number range included in the block."""

    record_type: Optional[str] = None

    requirements_met: Optional[bool] = None
    """True if all requirements are met for every phone number, false otherwise."""

    starting_number: Optional[str] = None
    """Starting phone number block"""

    status: Optional[Literal["pending", "success", "failure"]] = None
    """The status of the order."""

    updated_at: Optional[datetime] = None
    """An ISO 8901 datetime string for when the number order was updated."""
