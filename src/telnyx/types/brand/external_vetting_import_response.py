# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalVettingImportResponse"]


class ExternalVettingImportResponse(BaseModel):
    create_date: Optional[str] = FieldInfo(alias="createDate", default=None)
    """Vetting submission date.

    This is the date when the vetting request is generated in ISO 8601 format.
    """

    evp_id: Optional[str] = FieldInfo(alias="evpId", default=None)
    """External vetting provider ID for the brand."""

    vetted_date: Optional[str] = FieldInfo(alias="vettedDate", default=None)
    """Vetting effective date.

    This is the date when vetting was completed, or the starting effective date in
    ISO 8601 format. If this date is missing, then the vetting was not complete or
    not valid.
    """

    vetting_class: Optional[str] = FieldInfo(alias="vettingClass", default=None)
    """Identifies the vetting classification."""

    vetting_id: Optional[str] = FieldInfo(alias="vettingId", default=None)
    """Unique ID that identifies a vetting transaction performed by a vetting provider.

    This ID is provided by the vetting provider at time of vetting.
    """

    vetting_score: Optional[int] = FieldInfo(alias="vettingScore", default=None)
    """Vetting score ranging from 0-100."""

    vetting_token: Optional[str] = FieldInfo(alias="vettingToken", default=None)
    """Required by some providers for vetting record confirmation."""
