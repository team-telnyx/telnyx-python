# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["PhysicalAddress"]


class PhysicalAddress(BaseModel):
    administrative_area: str
    """State or province code (e.g. `IL`, `ON`)."""

    city: str

    country: str
    """ISO 3166-1 alpha-2 code (currently `US` or `CA`)."""

    postal_code: str

    street_address: str

    extended_address: Optional[str] = None
