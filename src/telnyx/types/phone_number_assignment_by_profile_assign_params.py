# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PhoneNumberAssignmentByProfileAssignParams"]


class PhoneNumberAssignmentByProfileAssignParams(TypedDict, total=False):
    messaging_profile_id: Required[Annotated[str, PropertyInfo(alias="messagingProfileId")]]
    """
    The ID of the messaging profile that you want to link to the specified campaign.
    """

    campaign_id: Annotated[str, PropertyInfo(alias="campaignId")]
    """The ID of the campaign you want to link to the specified messaging profile.

    If you supply this ID in the request, do not also include a tcrCampaignId.
    """

    tcr_campaign_id: Annotated[str, PropertyInfo(alias="tcrCampaignId")]
    """
    The TCR ID of the shared campaign you want to link to the specified messaging
    profile (for campaigns not created using Telnyx 10DLC services only). If you
    supply this ID in the request, do not also include a campaignId.
    """
