# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PartnerCampaignListSharedByMeResponse"]


class PartnerCampaignListSharedByMeResponse(BaseModel):
    brand_id: str = FieldInfo(alias="brandId")
    """Alphanumeric identifier of the brand associated with this campaign."""

    campaign_id: str = FieldInfo(alias="campaignId")
    """Alphanumeric identifier assigned by the registry for a campaign.

    This identifier is required by the NetNumber OSR SMS enabling process of 10DLC.
    """

    usecase: str
    """Campaign usecase.

    Must be of defined valid types. Use `/registry/enum/usecase` operation to
    retrieve usecases available for given brand.
    """

    create_date: Optional[str] = FieldInfo(alias="createDate", default=None)
    """Unix timestamp when campaign was created."""

    status: Optional[str] = None
    """Current campaign status.

    Possible values: ACTIVE, EXPIRED. A newly created campaign defaults to ACTIVE
    status.
    """
