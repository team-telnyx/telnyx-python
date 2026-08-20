# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .sub_number_order_regulatory_requirement import SubNumberOrderRegulatoryRequirement

__all__ = ["NumbersSubNumberOrder", "PhoneNumber", "PhoneNumberRegulatoryRequirement"]


class PhoneNumberRegulatoryRequirement(BaseModel):
    field_type: Optional[Literal["textual", "datetime", "address", "document"]] = None

    field_value: Optional[str] = None
    """
    The value of the requirement, this could be an id to a resource or a string
    value.
    """

    record_type: Optional[str] = None

    requirement_id: Optional[str] = None
    """Unique id for a requirement."""

    status: Optional[Literal["approved", "declined", "awaiting-value", "pending-approval"]] = None
    """The status of the regulatory requirement for this phone number."""


class PhoneNumber(BaseModel):
    id: Optional[str] = None

    bundle_id: Optional[str] = None

    country_code: Optional[str] = None

    phone_number: Optional[str] = None

    phone_number_type: Optional[str] = None

    record_type: Optional[str] = None

    regulatory_requirements: Optional[List[PhoneNumberRegulatoryRequirement]] = None

    requirements_met: Optional[bool] = None

    requirements_status: Optional[str] = None

    status: Optional[str] = None


class NumbersSubNumberOrder(BaseModel):
    id: Optional[str] = None

    country_code: Optional[str] = None

    created_at: Optional[datetime] = None
    """An ISO 8901 datetime string denoting when the number order was created."""

    customer_reference: Optional[str] = None
    """A customer reference string for customer look ups."""

    is_block_sub_number_order: Optional[bool] = None
    """True if the sub number order is a block sub number order"""

    order_request_id: Optional[str] = None

    phone_number_type: Optional[Literal["local", "toll_free", "mobile", "national", "shared_cost", "landline"]] = None

    phone_numbers: Optional[List[PhoneNumber]] = None
    """
    The first 50 phone numbers in the sub number order, including their per-number
    regulatory requirement statuses. Only present when
    filter[include_phone_numbers]=true is used.
    """

    phone_numbers_count: Optional[int] = None
    """The count of phone numbers in the number order."""

    record_type: Optional[str] = None

    regulatory_requirements: Optional[List[SubNumberOrderRegulatoryRequirement]] = None

    requirements_met: Optional[bool] = None
    """True if all requirements are met for every phone number, false otherwise."""

    status: Optional[Literal["pending", "success", "failure"]] = None
    """The status of the order."""

    updated_at: Optional[datetime] = None
    """An ISO 8901 datetime string for when the number order was updated."""

    user_id: Optional[str] = None
