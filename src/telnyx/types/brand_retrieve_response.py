# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .telnyx_brand import TelnyxBrand

__all__ = ["BrandRetrieveResponse"]


class BrandRetrieveResponse(TelnyxBrand):
    assigned_campaigns_count: Optional[float] = FieldInfo(alias="assignedCampaignsCount", default=None)
    """Number of campaigns associated with the brand"""
