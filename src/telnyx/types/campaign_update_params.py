# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CampaignUpdateParams"]


class CampaignUpdateParams(TypedDict, total=False):
    auto_renewal: Annotated[bool, PropertyInfo(alias="autoRenewal")]
    """Help message of the campaign."""

    help_message: Annotated[str, PropertyInfo(alias="helpMessage")]
    """Help message of the campaign."""

    message_flow: Annotated[str, PropertyInfo(alias="messageFlow")]
    """Message flow description."""

    reseller_id: Annotated[str, PropertyInfo(alias="resellerId")]
    """
    Alphanumeric identifier of the reseller that you want to associate with this
    campaign.
    """

    sample1: str
    """Message sample. Some campaign tiers require 1 or more message samples."""

    sample2: str
    """Message sample. Some campaign tiers require 2 or more message samples."""

    sample3: str
    """Message sample. Some campaign tiers require 3 or more message samples."""

    sample4: str
    """Message sample. Some campaign tiers require 4 or more message samples."""

    sample5: str
    """Message sample. Some campaign tiers require 5 or more message samples."""

    webhook_failover_url: Annotated[str, PropertyInfo(alias="webhookFailoverURL")]
    """Webhook failover to which campaign status updates are sent."""

    webhook_url: Annotated[str, PropertyInfo(alias="webhookURL")]
    """Webhook to which campaign status updates are sent."""
