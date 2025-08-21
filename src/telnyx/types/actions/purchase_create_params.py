# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PurchaseCreateParams"]


class PurchaseCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The amount of eSIMs to be purchased."""

    product: str
    """Type of product to be purchased, specify "whitelabel" to use a custom SPN"""

    sim_card_group_id: str
    """The group SIMCardGroup identification.

    This attribute can be <code>null</code> when it's present in an associated
    resource.
    """

    status: Literal["enabled", "disabled", "standby"]
    """Status on which the SIM cards will be set after being successfully registered."""

    tags: List[str]
    """Searchable tags associated with the SIM cards"""

    whitelabel_name: str
    """Service Provider Name (SPN) for the Whitelabel eSIM product.

    It will be displayed as the mobile service name by operating systems of
    smartphones. This parameter must only contain letters, numbers and whitespaces.
    """
