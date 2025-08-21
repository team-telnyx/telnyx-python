# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SimCardOrderPreviewPreviewParams"]


class SimCardOrderPreviewPreviewParams(TypedDict, total=False):
    address_id: Required[str]
    """Uniquely identifies the address for the order."""

    quantity: Required[int]
    """
    The amount of SIM cards that the user would like to purchase in the SIM card
    order.
    """
