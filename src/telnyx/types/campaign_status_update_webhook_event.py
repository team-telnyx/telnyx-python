# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

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

    is_t_mobile_registered: Optional[bool] = FieldInfo(alias="isTMobileRegistered", default=None)
    """Indicates whether the campaign is registered with T-Mobile."""
