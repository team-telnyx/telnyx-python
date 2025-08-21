# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .shared_params.sim_card_status import SimCardStatus

__all__ = ["SimCardUpdateParams", "DataLimit"]


class SimCardUpdateParams(TypedDict, total=False):
    authorized_imeis: List[str]
    """List of IMEIs authorized to use a given SIM card."""

    data_limit: DataLimit
    """The SIM card individual data limit configuration."""

    sim_card_group_id: str
    """The group SIMCardGroup identification.

    This attribute can be <code>null</code> when it's present in an associated
    resource.
    """

    status: SimCardStatus

    tags: List[str]
    """Searchable tags associated with the SIM card"""


class DataLimit(TypedDict, total=False):
    amount: str

    unit: Literal["MB", "GB"]
