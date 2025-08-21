# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .sub_number_order_regulatory_requirement import SubNumberOrderRegulatoryRequirement

__all__ = ["SubNumberOrder"]


class SubNumberOrder(BaseModel):
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
