# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PortingOrderEndUserLocation"]


class PortingOrderEndUserLocation(BaseModel):
    administrative_area: Optional[str] = None
    """State, province, or similar of billing address"""

    country_code: Optional[str] = None
    """ISO3166-1 alpha-2 country code of billing address"""

    extended_address: Optional[str] = None
    """Second line of billing address"""

    locality: Optional[str] = None
    """City or municipality of billing address"""

    postal_code: Optional[str] = None
    """Postal Code of billing address"""

    street_address: Optional[str] = None
    """First line of billing address"""
