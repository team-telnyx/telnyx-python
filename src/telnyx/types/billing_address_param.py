# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BillingAddressParam"]


class BillingAddressParam(TypedDict, total=False):
    administrative_area: Required[str]
    """State or province code (e.g. `IL`, `ON`)."""

    city: Required[str]

    country: Required[str]
    """ISO 3166-1 alpha-2 code (currently `US` or `CA`)."""

    postal_code: Required[str]

    street_address: Required[str]

    extended_address: Optional[str]
