# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BillingAddress"]


class BillingAddress(BaseModel):
    administrative_area: str
    """State or province"""

    city: str
    """City name"""

    country: str
    """Country name (e.g., United States)"""

    postal_code: str
    """ZIP or postal code"""

    street_address: str
    """Street address"""

    extended_address: Optional[str] = None
    """Additional address line (suite, apt, etc.)"""
