# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CampaignSubmitAppealParams"]


class CampaignSubmitAppealParams(TypedDict, total=False):
    appeal_reason: Required[str]
    """
    Detailed explanation of why the campaign should be reconsidered and what changes
    have been made to address the rejection reason.
    """
