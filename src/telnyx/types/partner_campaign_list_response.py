# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .telnyx_downstream_campaign import TelnyxDownstreamCampaign

__all__ = ["PartnerCampaignListResponse"]


class PartnerCampaignListResponse(BaseModel):
    page: Optional[int] = None

    records: Optional[List[TelnyxDownstreamCampaign]] = None

    total_records: Optional[int] = FieldInfo(alias="totalRecords", default=None)
