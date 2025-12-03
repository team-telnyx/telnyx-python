# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["PortingOrderRetrieveRequirementsResponse", "Data", "DataRequirementType"]


class DataRequirementType(BaseModel):
    id: Optional[str] = None
    """Identifies the requirement type"""

    acceptance_criteria: Optional[Dict[str, object]] = None
    """The acceptance criteria for the requirement type"""

    description: Optional[str] = None
    """A description of the requirement type"""

    example: Optional[str] = None
    """An example of the requirement type"""

    name: Optional[str] = None
    """The name of the requirement type"""

    type: Optional[str] = None
    """The type of the requirement type"""


class Data(BaseModel):
    field_type: Optional[Literal["document", "textual"]] = None
    """Type of value expected on field_value field"""

    field_value: Optional[str] = None
    """Identifies the document that satisfies this requirement"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    requirement_status: Optional[str] = None
    """Status of the requirement"""

    requirement_type: Optional[DataRequirementType] = None
    """Identifies the requirement type that meets this requirement"""


class PortingOrderRetrieveRequirementsResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
