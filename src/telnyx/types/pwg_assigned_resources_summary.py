# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PwgAssignedResourcesSummary"]


class PwgAssignedResourcesSummary(BaseModel):
    count: Optional[int] = None
    """The current count of a resource type assigned to the Private Wireless Gateway."""

    record_type: Optional[str] = None
    """The type of the resource assigned to the Private Wireless Gateway."""
