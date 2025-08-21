# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "SubNumberOrderUpdateRequirementGroupResponse",
    "Data",
    "DataPhoneNumber",
    "DataPhoneNumberRegulatoryRequirement",
    "DataRegulatoryRequirement",
]


class DataPhoneNumberRegulatoryRequirement(BaseModel):
    field_type: Optional[str] = None

    field_value: Optional[str] = None

    requirement_id: Optional[str] = None

    status: Optional[str] = None


class DataPhoneNumber(BaseModel):
    id: Optional[str] = None

    bundle_id: Optional[str] = None

    country_code: Optional[str] = None

    phone_number: Optional[str] = None

    phone_number_type: Optional[str] = None

    record_type: Optional[str] = None

    regulatory_requirements: Optional[List[DataPhoneNumberRegulatoryRequirement]] = None

    requirements_met: Optional[bool] = None

    requirements_status: Optional[str] = None

    status: Optional[str] = None


class DataRegulatoryRequirement(BaseModel):
    field_type: Optional[str] = None

    record_type: Optional[str] = None

    requirement_id: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None

    country_code: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_reference: Optional[str] = None

    is_block_sub_number_order: Optional[bool] = None

    order_request_id: Optional[str] = None

    phone_number_type: Optional[str] = None

    phone_numbers: Optional[List[DataPhoneNumber]] = None

    phone_numbers_count: Optional[int] = None

    record_type: Optional[str] = None

    regulatory_requirements: Optional[List[DataRegulatoryRequirement]] = None

    requirements_met: Optional[bool] = None

    status: Optional[str] = None

    updated_at: Optional[datetime] = None


class SubNumberOrderUpdateRequirementGroupResponse(BaseModel):
    data: Optional[Data] = None
