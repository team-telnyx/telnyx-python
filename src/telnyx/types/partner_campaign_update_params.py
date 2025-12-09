# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PartnerCampaignUpdateParams"]


class PartnerCampaignUpdateParams(TypedDict, total=False):
    webhook_failover_url: Annotated[str, PropertyInfo(alias="webhookFailoverURL")]
    """Webhook failover to which campaign status updates are sent."""

    webhook_url: Annotated[str, PropertyInfo(alias="webhookURL")]
    """Webhook to which campaign status updates are sent."""
