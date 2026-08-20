# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["BrandAddress"]


class BrandAddress(BaseModel):
    administrative_area: str

    city: str

    country_code: str
    """The two-letter ISO 3166-1 country code."""

    line_1: str

    postal_code: str

    line_2: Optional[str] = None
