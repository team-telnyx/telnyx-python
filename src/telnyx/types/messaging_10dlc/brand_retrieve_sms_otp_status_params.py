# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BrandRetrieveSMSOtpStatusParams"]


class BrandRetrieveSMSOtpStatusParams(TypedDict, total=False):
    brand_id: Annotated[str, PropertyInfo(alias="brandId")]
    """Filter by Brand ID for easier lookup in portal applications"""
