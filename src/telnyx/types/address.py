# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the address."""

    address_book: Optional[bool] = None
    """
    Indicates whether or not the address should be considered part of your list of
    addresses that appear for regular use.
    """

    administrative_area: Optional[str] = None
    """The locality of the address.

    For US addresses, this corresponds to the state of the address.
    """

    borough: Optional[str] = None
    """The borough of the address.

    This field is not used for addresses in the US but is used for some
    international addresses.
    """

    business_name: Optional[str] = None
    """The business name associated with the address.

    An address must have either a first last name or a business name.
    """

    country_code: Optional[str] = None
    """The two-character (ISO 3166-1 alpha-2) country code of the address."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    customer_reference: Optional[str] = None
    """A customer reference string for customer look ups."""

    extended_address: Optional[str] = None
    """
    Additional street address information about the address such as, but not limited
    to, unit number or apartment number.
    """

    first_name: Optional[str] = None
    """The first name associated with the address.

    An address must have either a first last name or a business name.
    """

    last_name: Optional[str] = None
    """The last name associated with the address.

    An address must have either a first last name or a business name.
    """

    locality: Optional[str] = None
    """The locality of the address.

    For US addresses, this corresponds to the city of the address.
    """

    neighborhood: Optional[str] = None
    """The neighborhood of the address.

    This field is not used for addresses in the US but is used for some
    international addresses.
    """

    phone_number: Optional[str] = None
    """The phone number associated with the address."""

    postal_code: Optional[str] = None
    """The postal code of the address."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    street_address: Optional[str] = None
    """The primary street address information about the address."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

    validate_address: Optional[bool] = None
    """
    Indicates whether or not the address should be validated for emergency use upon
    creation or not. This should be left with the default value of `true` unless you
    have used the `/addresses/actions/validate` endpoint to validate the address
    separately prior to creation. If an address is not validated for emergency use
    upon creation and it is not valid, it will not be able to be used for emergency
    services.
    """
