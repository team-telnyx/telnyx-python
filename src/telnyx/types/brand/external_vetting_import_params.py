# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExternalVettingImportParams"]


class ExternalVettingImportParams(TypedDict, total=False):
    evp_id: Required[Annotated[str, PropertyInfo(alias="evpId")]]
    """External vetting provider ID for the brand."""

    vetting_id: Required[Annotated[str, PropertyInfo(alias="vettingId")]]
    """Unique ID that identifies a vetting transaction performed by a vetting provider.

    This ID is provided by the vetting provider at time of vetting.
    """

    vetting_token: Annotated[str, PropertyInfo(alias="vettingToken")]
    """Required by some providers for vetting record confirmation."""
