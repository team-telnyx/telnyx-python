# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PortingOrderRequirement"]


class PortingOrderRequirement(BaseModel):
    field_type: Optional[Literal["document"]] = None
    """Type of value expected on field_value field"""

    field_value: Optional[str] = None
    """identifies the document that satisfies this requirement"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    requirement_type_id: Optional[str] = None
    """Identifies the requirement type that meets this requirement"""
