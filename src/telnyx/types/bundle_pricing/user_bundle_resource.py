# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["UserBundleResource"]


class UserBundleResource(BaseModel):
    id: str
    """Resource's ID."""

    created_at: date
    """Date the resource was created."""

    resource: str
    """The resource itself (usually a phone number)."""

    resource_type: str
    """The type of the resource (usually 'number')."""

    updated_at: Optional[date] = None
    """Date the resource was last updated."""
