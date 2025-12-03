# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PhoneNumberCampaignUpdateParams"]


class PhoneNumberCampaignUpdateParams(TypedDict, total=False):
    campaign_id: Required[Annotated[str, PropertyInfo(alias="campaignId")]]
    """The ID of the campaign you want to link to the specified phone number."""

    body_phone_number: Required[Annotated[str, PropertyInfo(alias="phoneNumber")]]
    """The phone number you want to link to a specified campaign."""
