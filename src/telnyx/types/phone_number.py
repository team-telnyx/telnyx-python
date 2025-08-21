# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.sub_number_order_regulatory_requirement_with_value import SubNumberOrderRegulatoryRequirementWithValue

__all__ = ["PhoneNumber"]


class PhoneNumber(BaseModel):
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

    regulatory_requirements: Optional[List[SubNumberOrderRegulatoryRequirementWithValue]] = None

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
