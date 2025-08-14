# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SimCardGroupCreateParams", "DataLimit"]


class SimCardGroupCreateParams(TypedDict, total=False):
    name: Required[str]
    """A user friendly name for the SIM card group."""

    data_limit: DataLimit
    """Upper limit on the amount of data the SIM cards, within the group, can use."""


class DataLimit(TypedDict, total=False):
    amount: str

    unit: str
