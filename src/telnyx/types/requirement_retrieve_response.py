# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RequirementRetrieveResponse", "Data", "DataRequirementsType", "DataRequirementsTypeAcceptanceCriteria"]


class DataRequirementsTypeAcceptanceCriteria(BaseModel):
    acceptable_characters: Optional[str] = None
    """Specifies the allowed characters as a string"""

    acceptable_values: Optional[List[str]] = None
    """Specifies the list of strictly possible values for the requirement.

    Ignored when empty
    """

    locality_limit: Optional[str] = None
    """Specifies geography-based acceptance criteria"""

    max_length: Optional[int] = None
    """Maximum length allowed for the value"""

    min_length: Optional[int] = None
    """Minimum length allowed for the value"""

    time_limit: Optional[str] = None
    """Specifies time-based acceptance criteria"""


class DataRequirementsType(BaseModel):
    id: Optional[str] = None
    """Identifies the associated document"""

    acceptance_criteria: Optional[DataRequirementsTypeAcceptanceCriteria] = None
    """Specifies objective criteria for acceptance"""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    description: Optional[str] = None
    """Describes the requirement type"""

    example: Optional[str] = None
    """Provides one or more examples of acceptable documents"""

    name: Optional[str] = None
    """A short descriptive name for this requirement_type"""

    record_type: Optional[str] = None
    """Identifies the type of the resource"""

    type: Optional[Literal["document", "address", "textual"]] = None
    """Defines the type of this requirement type"""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was last updated."""


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the associated document"""

    action: Optional[Literal["both", "branded_calling", "ordering", "porting"]] = None
    """
    Indicates whether this requirement applies to branded_calling, ordering,
    porting, or both ordering and porting
    """

    country_code: Optional[str] = None
    """
    The 2-character (ISO 3166-1 alpha-2) country code where this requirement applies
    """

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    locality: Optional[str] = None
    """The locality where this requirement applies"""

    phone_number_type: Optional[Literal["local", "national", "toll_free"]] = None
    """Indicates the phone_number_type this requirement applies to.

    Leave blank if this requirement applies to all number_types.
    """

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    requirements_types: Optional[List[DataRequirementsType]] = None
    """Lists the requirement types necessary to fulfill this requirement"""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was last updated."""


class RequirementRetrieveResponse(BaseModel):
    data: Optional[Data] = None
