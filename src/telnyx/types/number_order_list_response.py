# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["NumberOrderListResponse", "Data", "DataPhoneNumber"]


class DataPhoneNumber(BaseModel):
    id: Optional[str] = None
    """The phone number's ID"""

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class Data(BaseModel):
    id: Optional[str] = None

    billing_group_id: Optional[str] = None
    """Identifies the messaging profile associated with the phone number."""

    connection_id: Optional[str] = None
    """Identifies the connection associated with this phone number."""

    created_at: Optional[datetime] = None
    """An ISO 8901 datetime string denoting when the number order was created."""

    customer_reference: Optional[str] = None
    """A customer reference string for customer look ups."""

    messaging_profile_id: Optional[str] = None
    """Identifies the messaging profile associated with the phone number."""

    phone_numbers: Optional[List[DataPhoneNumber]] = None

    phone_numbers_count: Optional[int] = None
    """The count of phone numbers in the number order."""

    record_type: Optional[str] = None

    requirements_met: Optional[bool] = None
    """True if all requirements are met for every phone number, false otherwise."""

    status: Optional[Literal["pending", "success", "failure"]] = None
    """The status of the order."""

    sub_number_orders_ids: Optional[List[str]] = None

    updated_at: Optional[datetime] = None
    """An ISO 8901 datetime string for when the number order was updated."""


class NumberOrderListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
