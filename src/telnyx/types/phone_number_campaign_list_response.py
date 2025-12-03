# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .phone_number_campaign import PhoneNumberCampaign

__all__ = ["PhoneNumberCampaignListResponse"]


class PhoneNumberCampaignListResponse(BaseModel):
    page: int

    records: List[PhoneNumberCampaign]

    total_records: int = FieldInfo(alias="totalRecords")
