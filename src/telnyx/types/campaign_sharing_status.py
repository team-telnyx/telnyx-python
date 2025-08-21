# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CampaignSharingStatus"]


class CampaignSharingStatus(BaseModel):
    downstream_cnp_id: Optional[str] = FieldInfo(alias="downstreamCnpId", default=None)

    shared_date: Optional[str] = FieldInfo(alias="sharedDate", default=None)

    sharing_status: Optional[str] = FieldInfo(alias="sharingStatus", default=None)

    status_date: Optional[str] = FieldInfo(alias="statusDate", default=None)

    upstream_cnp_id: Optional[str] = FieldInfo(alias="upstreamCnpId", default=None)
