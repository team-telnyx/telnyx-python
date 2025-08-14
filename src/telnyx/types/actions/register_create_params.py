# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RegisterCreateParams"]


class RegisterCreateParams(TypedDict, total=False):
    registration_codes: Required[List[str]]

    sim_card_group_id: str
    """The group SIMCardGroup identification.

    This attribute can be <code>null</code> when it's present in an associated
    resource.
    """

    status: Literal["enabled", "disabled", "standby"]
    """Status on which the SIM card will be set after being successful registered."""

    tags: List[str]
    """Searchable tags associated with the SIM card"""
