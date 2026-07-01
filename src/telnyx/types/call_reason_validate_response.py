# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["CallReasonValidateResponse", "Data"]


class Data(BaseModel):
    all_pre_approved: bool
    """
    `true` when every supplied reason matches a pre-vetted entry in the call-reason
    library. When `true`, the DIR will sail through the call-reasons portion of
    vetting.
    """

    non_approved_reasons: List[str]
    """Subset of the input that does NOT match the pre-vetted library.

    The DIR can still be submitted with these - they will go through manual review.
    """

    requires_manual_vetting: bool
    """`true` when at least one supplied reason is in `non_approved_reasons`.

    Equivalent to `non_approved_reasons.length > 0` and the inverse of
    `all_pre_approved`.
    """


class CallReasonValidateResponse(BaseModel):
    data: Data
