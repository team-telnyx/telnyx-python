# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CampaignSuspendedEvent"]


class CampaignSuspendedEvent(BaseModel):
    campaign_id: Optional[str] = FieldInfo(alias="campaignId", default=None)
    """The ID of the campaign."""

    description: Optional[str] = None
    """Description of the event."""

    status: Optional[Literal["DORMANT"]] = None
    """The status of the campaign."""

    type: Optional[Literal["TELNYX_EVENT"]] = None
