# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PortingOrderEndUserLocationParam"]


class PortingOrderEndUserLocationParam(TypedDict, total=False):
    administrative_area: str
    """State, province, or similar of billing address"""

    country_code: str
    """ISO3166-1 alpha-2 country code of billing address"""

    extended_address: str
    """Second line of billing address"""

    locality: str
    """City or municipality of billing address"""

    postal_code: str
    """Postal Code of billing address"""

    street_address: str
    """First line of billing address"""
