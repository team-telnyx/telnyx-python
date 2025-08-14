# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "RegulatoryRequirementRetrieveResponse",
    "Data",
    "DataRegulatoryRequirement",
    "DataRegulatoryRequirementAcceptanceCriteria",
]


class DataRegulatoryRequirementAcceptanceCriteria(BaseModel):
    acceptable_characters: Optional[str] = None

    acceptable_values: Optional[List[str]] = None

    case_sensitive: Optional[str] = None

    locality_limit: Optional[str] = None

    max_length: Optional[str] = None

    min_length: Optional[str] = None

    regex: Optional[str] = None

    time_limit: Optional[str] = None


class DataRegulatoryRequirement(BaseModel):
    id: Optional[str] = None

    acceptance_criteria: Optional[DataRegulatoryRequirementAcceptanceCriteria] = None

    description: Optional[str] = None

    example: Optional[str] = None

    field_type: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    action: Optional[str] = None

    country_code: Optional[str] = None

    phone_number_type: Optional[str] = None

    regulatory_requirements: Optional[List[DataRegulatoryRequirement]] = None


class RegulatoryRequirementRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None
