# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = [
    "PhoneNumbersRegulatoryRequirementRetrieveResponse",
    "Data",
    "DataRegionInformation",
    "DataRegulatoryRequirement",
    "DataRegulatoryRequirementAcceptanceCriteria",
]


class DataRegionInformation(BaseModel):
    region_name: Optional[str] = None

    region_type: Optional[str] = None


class DataRegulatoryRequirementAcceptanceCriteria(BaseModel):
    field_type: Optional[str] = None

    field_value: Optional[str] = None

    locality_limit: Optional[str] = None


class DataRegulatoryRequirement(BaseModel):
    id: Optional[str] = None

    acceptance_criteria: Optional[DataRegulatoryRequirementAcceptanceCriteria] = None

    description: Optional[str] = None

    example: Optional[str] = None

    field_type: Optional[str] = None

    label: Optional[str] = None

    record_type: Optional[str] = None


class Data(BaseModel):
    phone_number: Optional[str] = None

    phone_number_type: Optional[str] = None

    record_type: Optional[str] = None

    region_information: Optional[List[DataRegionInformation]] = None

    regulatory_requirements: Optional[List[DataRegulatoryRequirement]] = None


class PhoneNumbersRegulatoryRequirementRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
