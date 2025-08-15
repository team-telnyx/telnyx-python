# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RegionListResponse", "Data"]


class Data(BaseModel):
    code: Optional[str] = None
    """A code for the region."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    name: Optional[str] = None
    """A name for the region."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    supported_interfaces: Optional[List[str]] = None
    """List of interface types supported in this region."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class RegionListResponse(BaseModel):
    data: Optional[List[Data]] = None
