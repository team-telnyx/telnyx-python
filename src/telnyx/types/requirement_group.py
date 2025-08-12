# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RequirementGroup", "RegulatoryRequirement"]


class RegulatoryRequirement(BaseModel):
    created_at: Optional[datetime] = None

    expires_at: Optional[datetime] = None

    field_type: Optional[str] = None

    field_value: Optional[str] = None

    requirement_id: Optional[str] = None

    status: Optional[Literal["approved", "unapproved", "pending-approval", "declined"]] = None

    updated_at: Optional[datetime] = None


class RequirementGroup(BaseModel):
    id: Optional[str] = None

    action: Optional[str] = None

    country_code: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_reference: Optional[str] = None

    phone_number_type: Optional[str] = None

    record_type: Optional[str] = None

    regulatory_requirements: Optional[List[RegulatoryRequirement]] = None

    status: Optional[Literal["approved", "unapproved", "pending-approval", "declined"]] = None

    updated_at: Optional[datetime] = None
