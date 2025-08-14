# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SimCardGroupUpdateParams", "DataLimit"]


class SimCardGroupUpdateParams(TypedDict, total=False):
    data_limit: DataLimit
    """Upper limit on the amount of data the SIM cards, within the group, can use."""

    name: str
    """A user friendly name for the SIM card group."""


class DataLimit(TypedDict, total=False):
    amount: str

    unit: str
