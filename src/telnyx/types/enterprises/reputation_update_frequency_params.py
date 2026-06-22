# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .reputation_check_frequency import ReputationCheckFrequency

__all__ = ["ReputationUpdateFrequencyParams"]


class ReputationUpdateFrequencyParams(TypedDict, total=False):
    check_frequency: Required[ReputationCheckFrequency]
    """
    How often Telnyx refreshes the stored reputation data for this enterprise's
    registered numbers.
    """
