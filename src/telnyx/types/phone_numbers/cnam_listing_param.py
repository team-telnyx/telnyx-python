# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CnamListingParam"]


class CnamListingParam(TypedDict, total=False):
    cnam_listing_details: str
    """The CNAM listing details for this number.

    Must be alphanumeric characters or spaces with a maximum length of 15. Requires
    cnam_listing_enabled to also be set to true.
    """

    cnam_listing_enabled: bool
    """Enables CNAM listings for this number.

    Requires cnam_listing_details to also be set.
    """
