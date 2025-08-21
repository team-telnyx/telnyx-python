# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExternalVettingOrderParams"]


class ExternalVettingOrderParams(TypedDict, total=False):
    evp_id: Required[Annotated[str, PropertyInfo(alias="evpId")]]
    """External vetting provider ID for the brand."""

    vetting_class: Required[Annotated[str, PropertyInfo(alias="vettingClass")]]
    """Identifies the vetting classification."""
