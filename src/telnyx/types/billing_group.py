# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingGroup"]


class BillingGroup(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    deleted_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was removed."""

    name: Optional[str] = None
    """A user-specified name for the billing group"""

    organization_id: Optional[str] = None
    """Identifies the organization that owns the resource."""

    record_type: Optional[Literal["billing_group"]] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""
