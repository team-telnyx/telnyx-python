# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CampaignStatusUpdateWebhookEvent"]


class CampaignStatusUpdateWebhookEvent(BaseModel):
    brand_id: Optional[str] = FieldInfo(alias="brandId", default=None)
    """Brand ID associated with the campaign."""

    campaign_id: Optional[str] = FieldInfo(alias="campaignId", default=None)
    """The ID of the campaign."""

    create_date: Optional[str] = FieldInfo(alias="createDate", default=None)
    """Unix timestamp when campaign was created."""

    csp_id: Optional[str] = FieldInfo(alias="cspId", default=None)
    """Alphanumeric identifier of the CSP associated with this campaign."""

    description: Optional[str] = None
    """Description of the event."""

    is_t_mobile_registered: Optional[bool] = FieldInfo(alias="isTMobileRegistered", default=None)
    """Indicates whether the campaign is registered with T-Mobile."""

    status: Optional[Literal["ACCEPTED", "REJECTED", "DORMANT", "success", "failed"]] = None
    """The status of the campaign."""

    type: Optional[
        Literal[
            "TELNYX_EVENT",
            "REGISTRATION",
            "MNO_REVIEW",
            "TELNYX_REVIEW",
            "NUMBER_POOL_PROVISIONED",
            "NUMBER_POOL_DEPROVISIONED",
            "TCR_EVENT",
            "VERIFIED",
        ]
    ] = None
