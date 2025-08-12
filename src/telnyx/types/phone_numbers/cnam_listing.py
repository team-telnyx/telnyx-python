# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CnamListing"]


class CnamListing(BaseModel):
    cnam_listing_details: Optional[str] = None
    """The CNAM listing details for this number.

    Must be alphanumeric characters or spaces with a maximum length of 15. Requires
    cnam_listing_enabled to also be set to true.
    """

    cnam_listing_enabled: Optional[bool] = None
    """Enables CNAM listings for this number.

    Requires cnam_listing_details to also be set.
    """
