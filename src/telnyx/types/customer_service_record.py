# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CustomerServiceRecord", "Result", "ResultAddress", "ResultAdmin"]


class ResultAddress(BaseModel):
    administrative_area: Optional[str] = None
    """The state of the address"""

    full_address: Optional[str] = None
    """The full address"""

    locality: Optional[str] = None
    """The city of the address"""

    postal_code: Optional[str] = None
    """The zip code of the address"""

    street_address: Optional[str] = None
    """The street address"""


class ResultAdmin(BaseModel):
    account_number: Optional[str] = None
    """The account number of the customer service record."""

    authorized_person_name: Optional[str] = None
    """The authorized person name of the customer service record."""

    billing_phone_number: Optional[str] = None
    """The billing phone number of the customer service record."""

    name: Optional[str] = None
    """The name of the customer service record."""


class Result(BaseModel):
    address: Optional[ResultAddress] = None
    """The address of the customer service record"""

    admin: Optional[ResultAdmin] = None
    """The admin of the customer service record."""

    associated_phone_numbers: Optional[List[str]] = None
    """The associated phone numbers of the customer service record."""

    carrier_name: Optional[str] = None
    """The name of the carrier that the customer service record is for."""


class CustomerServiceRecord(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies this customer service record"""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    error_message: Optional[str] = None
    """The error message in case status is `failed`.

    This field would be null in case of `pending` or `completed` status.
    """

    phone_number: Optional[str] = None
    """The phone number of the customer service record."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    result: Optional[Result] = None
    """The result of the CSR request.

    This field would be null in case of `pending` or `failed` status.
    """

    status: Optional[Literal["pending", "completed", "failed"]] = None
    """The status of the customer service record"""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""
