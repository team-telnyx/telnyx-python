# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UserAddress"]


class UserAddress(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the user address."""

    administrative_area: Optional[str] = None
    """The locality of the user address.

    For US addresses, this corresponds to the state of the address.
    """

    borough: Optional[str] = None
    """The borough of the user address.

    This field is not used for addresses in the US but is used for some
    international addresses.
    """

    business_name: Optional[str] = None
    """The business name associated with the user address."""

    country_code: Optional[str] = None
    """The two-character (ISO 3166-1 alpha-2) country code of the user address."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    customer_reference: Optional[str] = None
    """A customer reference string for customer look ups."""

    extended_address: Optional[str] = None
    """
    Additional street address information about the user address such as, but not
    limited to, unit number or apartment number.
    """

    first_name: Optional[str] = None
    """The first name associated with the user address."""

    last_name: Optional[str] = None
    """The last name associated with the user address."""

    locality: Optional[str] = None
    """The locality of the user address.

    For US addresses, this corresponds to the city of the address.
    """

    neighborhood: Optional[str] = None
    """The neighborhood of the user address.

    This field is not used for addresses in the US but is used for some
    international addresses.
    """

    phone_number: Optional[str] = None
    """The phone number associated with the user address."""

    postal_code: Optional[str] = None
    """The postal code of the user address."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    street_address: Optional[str] = None
    """The primary street address information about the user address."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""
