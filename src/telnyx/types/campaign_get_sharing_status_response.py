# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .campaign_sharing_status import CampaignSharingStatus

__all__ = ["CampaignGetSharingStatusResponse"]


class CampaignGetSharingStatusResponse(BaseModel):
    shared_by_me: Optional[CampaignSharingStatus] = FieldInfo(alias="sharedByMe", default=None)

    shared_with_me: Optional[CampaignSharingStatus] = FieldInfo(alias="sharedWithMe", default=None)
