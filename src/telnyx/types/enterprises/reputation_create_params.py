# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReputationCreateParams"]


class ReputationCreateParams(TypedDict, total=False):
    loa_document_id: Required[str]
    """
    ID of the signed Letter of Authorization (LOA) document uploaded to the document
    service
    """

    check_frequency: Literal["business_daily", "daily", "weekly", "biweekly", "monthly", "never"]
    """Frequency for automatically refreshing reputation data"""
