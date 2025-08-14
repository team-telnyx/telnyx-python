# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NumberOrderRetrieveResponse", "Data", "DataPhoneNumber", "DataPhoneNumberRegulatoryRequirement"]


class DataPhoneNumberRegulatoryRequirement(BaseModel):
    field_type: Optional[Literal["textual", "datetime", "address", "document"]] = None

    field_value: Optional[str] = None
    """
    The value of the requirement, this could be an id to a resource or a string
    value.
    """

    record_type: Optional[str] = None

    requirement_id: Optional[str] = None
    """Unique id for a requirement."""


class DataPhoneNumber(BaseModel):
    id: Optional[str] = None

    bundle_id: Optional[str] = None

    country_code: Optional[str] = None
    """Country code of the phone number"""

    country_iso_alpha2: Optional[str] = None
    """The ISO 3166-1 alpha-2 country code of the phone number."""

    phone_number: Optional[str] = None

    phone_number_type: Optional[Literal["local", "mobile", "national", "shared_cost", "toll_free"]] = None
    """Phone number type"""

    record_type: Optional[str] = None

    regulatory_requirements: Optional[List[DataPhoneNumberRegulatoryRequirement]] = None

    requirements_met: Optional[bool] = None
    """True if all requirements are met for a phone number, false otherwise."""

    requirements_status: Optional[
        Literal[
            "pending",
            "approved",
            "cancelled",
            "deleted",
            "requirement-info-exception",
            "requirement-info-pending",
            "requirement-info-under-review",
        ]
    ] = None
    """Status of document requirements (if applicable)"""

    status: Optional[Literal["pending", "success", "failure"]] = None
    """The status of the phone number in the order."""


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


class NumberOrderRetrieveResponse(BaseModel):
    data: Optional[Data] = None
