# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BillingAddressParam"]


class BillingAddressParam(TypedDict, total=False):
    administrative_area: Required[str]
    """State or province"""

    city: Required[str]
    """City name"""

    country: Required[str]
    """Country name (e.g., United States)"""

    postal_code: Required[str]
    """ZIP or postal code"""

    street_address: Required[str]
    """Street address"""

    extended_address: Optional[str]
    """Additional address line (suite, apt, etc.)"""
