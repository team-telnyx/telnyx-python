# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .entity_type import EntityType
from .brand_identity_status import BrandIdentityStatus

__all__ = ["BrandListResponse", "Record"]


class Record(BaseModel):
    assigned_campaings_count: Optional[int] = FieldInfo(alias="assignedCampaingsCount", default=None)
    """Number of campaigns associated with the brand"""

    brand_id: Optional[str] = FieldInfo(alias="brandId", default=None)
    """Unique identifier assigned to the brand."""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """(Required for Non-profit/private/public) Legal company name."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """Date and time that the brand was created at."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display or marketing name of the brand."""

    email: Optional[str] = None
    """Valid email address of brand support contact."""

    entity_type: Optional[EntityType] = FieldInfo(alias="entityType", default=None)
    """Entity type behind the brand. This is the form of business establishment."""

    failure_reasons: Optional[str] = FieldInfo(alias="failureReasons", default=None)
    """Failure reasons for brand"""

    identity_status: Optional[BrandIdentityStatus] = FieldInfo(alias="identityStatus", default=None)
    """The verification status of an active brand"""

    status: Optional[Literal["OK", "REGISTRATION_PENDING", "REGISTRATION_FAILED"]] = None
    """Status of the brand"""

    tcr_brand_id: Optional[str] = FieldInfo(alias="tcrBrandId", default=None)
    """Unique identifier assigned to the brand by the registry."""

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """Date and time that the brand was last updated at."""

    website: Optional[str] = None
    """Brand website URL."""


class BrandListResponse(BaseModel):
    page: Optional[int] = None

    records: Optional[List[Record]] = None

    total_records: Optional[int] = FieldInfo(alias="totalRecords", default=None)
