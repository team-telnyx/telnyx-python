# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PhoneNumberAssignmentByProfileAssignResponse",
    "AssignProfileToCampaignResponse",
    "SettingsDataErrorMessage",
]


class AssignProfileToCampaignResponse(BaseModel):
    messaging_profile_id: str = FieldInfo(alias="messagingProfileId")
    """
    The ID of the messaging profile that you want to link to the specified campaign.
    """

    task_id: str = FieldInfo(alias="taskId")
    """The ID of the task associated with assigning a messaging profile to a campaign."""

    campaign_id: Optional[str] = FieldInfo(alias="campaignId", default=None)
    """The ID of the campaign you want to link to the specified messaging profile.

    If you supply this ID in the request, do not also include a tcrCampaignId.
    """

    tcr_campaign_id: Optional[str] = FieldInfo(alias="tcrCampaignId", default=None)
    """
    The TCR ID of the shared campaign you want to link to the specified messaging
    profile (for campaigns not created using Telnyx 10DLC services only). If you
    supply this ID in the request, do not also include a campaignId.
    """


class SettingsDataErrorMessage(BaseModel):
    message: str


PhoneNumberAssignmentByProfileAssignResponse: TypeAlias = Union[
    AssignProfileToCampaignResponse, SettingsDataErrorMessage
]
