# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["PhysicalAddress"]


class PhysicalAddress(BaseModel):
    administrative_area: str
    """State or province code (e.g. `IL`, `ON`)."""

    city: str
    """The city of your registered business address."""

    country: str
    """ISO 3166-1 alpha-2 code (currently `US` or `CA`)."""

    postal_code: str
    """The postal or ZIP code of your registered business address."""

    street_address: str
    """
    The street address of your registered business, including the building number
    and street name.
    """

    extended_address: Optional[str] = None
    """An optional second address line, such as a suite, unit, or floor.

    Leave blank if it does not apply.
    """
