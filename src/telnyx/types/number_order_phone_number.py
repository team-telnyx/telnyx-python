# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.sub_number_order_regulatory_requirement_with_value import SubNumberOrderRegulatoryRequirementWithValue

__all__ = ["NumberOrderPhoneNumber"]


class NumberOrderPhoneNumber(BaseModel):
    id: Optional[str] = None

    bundle_id: Optional[str] = None

    country_code: Optional[str] = None

    deadline: Optional[datetime] = None

    is_block_number: Optional[bool] = None

    locality: Optional[str] = None

    order_request_id: Optional[str] = None

    phone_number: Optional[str] = None

    phone_number_type: Optional[Literal["local", "toll_free", "mobile", "national", "shared_cost", "landline"]] = None

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
    """Status of requirements (if applicable)"""

    status: Optional[Literal["pending", "success", "failure"]] = None
    """The status of the phone number in the order."""

    sub_number_order_id: Optional[str] = None
