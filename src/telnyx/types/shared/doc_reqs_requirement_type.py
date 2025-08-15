# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DocReqsRequirementType", "AcceptanceCriteria"]


class AcceptanceCriteria(BaseModel):
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


class DocReqsRequirementType(BaseModel):
    id: Optional[str] = None
    """Identifies the associated document"""

    acceptance_criteria: Optional[AcceptanceCriteria] = None
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
