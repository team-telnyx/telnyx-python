# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PortingOrderEndUserLocationParam"]


class PortingOrderEndUserLocationParam(TypedDict, total=False):
    administrative_area: Optional[str]
    """State, province, or similar of billing address"""

    country_code: Optional[str]
    """ISO3166-1 alpha-2 country code of billing address"""

    extended_address: Optional[str]
    """Second line of billing address"""

    locality: Optional[str]
    """City or municipality of billing address"""

    postal_code: Optional[str]
    """Postal Code of billing address"""

    street_address: Optional[str]
    """First line of billing address"""
