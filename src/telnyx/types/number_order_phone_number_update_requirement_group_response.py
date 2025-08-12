# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["NumberOrderPhoneNumberUpdateRequirementGroupResponse", "Data", "DataRegulatoryRequirement"]


class DataRegulatoryRequirement(BaseModel):
    field_type: Optional[str] = None

    field_value: Optional[str] = None

    requirement_id: Optional[str] = None

    status: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None

    bundle_id: Optional[str] = None

    country_code: Optional[str] = None

    deadline: Optional[datetime] = None

    is_block_number: Optional[bool] = None

    locality: Optional[str] = None

    order_request_id: Optional[str] = None

    phone_number: Optional[str] = None

    phone_number_type: Optional[str] = None

    record_type: Optional[str] = None

    regulatory_requirements: Optional[List[DataRegulatoryRequirement]] = None

    requirements_met: Optional[bool] = None

    requirements_status: Optional[str] = None

    status: Optional[str] = None

    sub_number_order_id: Optional[str] = None


class NumberOrderPhoneNumberUpdateRequirementGroupResponse(BaseModel):
    data: Optional[Data] = None
