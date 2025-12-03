# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdvancedOrderUpdateRequirementGroupResponse"]


class AdvancedOrderUpdateRequirementGroupResponse(BaseModel):
    id: Optional[str] = None

    area_code: Optional[str] = None

    comments: Optional[str] = None

    country_code: Optional[str] = None

    customer_reference: Optional[str] = None

    features: Optional[List[Literal["sms", "mms", "voice", "fax", "emergency"]]] = None

    orders: Optional[List[str]] = None

    phone_number_type: Optional[
        List[Literal["local", "mobile", "toll_free", "shared_cost", "national", "landline"]]
    ] = None

    quantity: Optional[int] = None

    requirement_group_id: Optional[str] = None
    """The ID of the requirement group associated with this advanced order"""

    status: Optional[List[Literal["pending", "processing", "ordered"]]] = None
