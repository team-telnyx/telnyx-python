# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.doc_reqs_requirement_type import DocReqsRequirementType

__all__ = ["DocReqsRequirement"]


class DocReqsRequirement(BaseModel):
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

    effective_end_at: Optional[datetime] = None
    """When this version was superseded.

    NULL means this is the active or pending version.
    """

    effective_start_at: Optional[datetime] = None
    """When this version became (or will become) active."""

    locality: Optional[str] = None
    """The locality where this requirement applies"""

    phone_number_type: Optional[Literal["local", "national", "toll_free"]] = None
    """Indicates the phone_number_type this requirement applies to.

    Leave blank if this requirement applies to all number_types.
    """

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    requirement_types: Optional[List[DocReqsRequirementType]] = None
    """Lists the requirement types necessary to fulfill this requirement"""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was last updated."""

    version: Optional[int] = None
    """Version number. Increments with each new version. Defaults to 1."""
