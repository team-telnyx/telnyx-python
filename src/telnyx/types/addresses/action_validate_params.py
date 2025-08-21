# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionValidateParams"]


class ActionValidateParams(TypedDict, total=False):
    country_code: Required[str]
    """The two-character (ISO 3166-1 alpha-2) country code of the address."""

    postal_code: Required[str]
    """The postal code of the address."""

    street_address: Required[str]
    """The primary street address information about the address."""

    administrative_area: str
    """The locality of the address.

    For US addresses, this corresponds to the state of the address.
    """

    extended_address: str
    """
    Additional street address information about the address such as, but not limited
    to, unit number or apartment number.
    """

    locality: str
    """The locality of the address.

    For US addresses, this corresponds to the city of the address.
    """
