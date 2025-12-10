# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PhoneNumberCampaign"]


class PhoneNumberCampaign(BaseModel):
    campaign_id: str = FieldInfo(alias="campaignId")
    """
    For shared campaigns, this is the TCR campaign ID, otherwise it is the campaign
    ID
    """

    created_at: str = FieldInfo(alias="createdAt")

    phone_number: str = FieldInfo(alias="phoneNumber")

    updated_at: str = FieldInfo(alias="updatedAt")

    assignment_status: Optional[
        Literal["FAILED_ASSIGNMENT", "PENDING_ASSIGNMENT", "ASSIGNED", "PENDING_UNASSIGNMENT", "FAILED_UNASSIGNMENT"]
    ] = FieldInfo(alias="assignmentStatus", default=None)
    """The assignment status of the number."""

    brand_id: Optional[str] = FieldInfo(alias="brandId", default=None)
    """Brand ID. Empty if the number is associated to a shared campaign."""

    failure_reasons: Optional[str] = FieldInfo(alias="failureReasons", default=None)
    """Extra info about a failure to assign/unassign a number.

    Relevant only if the assignmentStatus is either FAILED_ASSIGNMENT or
    FAILED_UNASSIGNMENT
    """

    tcr_brand_id: Optional[str] = FieldInfo(alias="tcrBrandId", default=None)
    """TCR's alphanumeric ID for the brand."""

    tcr_campaign_id: Optional[str] = FieldInfo(alias="tcrCampaignId", default=None)
    """TCR's alphanumeric ID for the campaign."""

    telnyx_campaign_id: Optional[str] = FieldInfo(alias="telnyxCampaignId", default=None)
    """Campaign ID. Empty if the number is associated to a shared campaign."""
