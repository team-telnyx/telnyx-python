# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserRequirement"]


class UserRequirement(BaseModel):
    created_at: Optional[datetime] = None

    expires_at: Optional[datetime] = None

    field_type: Optional[str] = None

    field_value: Optional[str] = None

    requirement_id: Optional[str] = None

    status: Optional[Literal["approved", "unapproved", "pending-approval", "declined", "expired"]] = None

    updated_at: Optional[datetime] = None
