# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PartnerCampaignListSharedByMeResponse", "Record"]


class Record(BaseModel):
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


class PartnerCampaignListSharedByMeResponse(BaseModel):
    page: Optional[int] = None

    records: Optional[List[Record]] = None

    total_records: Optional[int] = FieldInfo(alias="totalRecords", default=None)
