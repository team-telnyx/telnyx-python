# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AddressCreateParams"]


class AddressCreateParams(TypedDict, total=False):
    business_name: Required[str]
    """The business name associated with the address.

    An address must have either a first last name or a business name.
    """

    country_code: Required[str]
    """The two-character (ISO 3166-1 alpha-2) country code of the address."""

    first_name: Required[str]
    """The first name associated with the address.

    An address must have either a first last name or a business name.
    """

    last_name: Required[str]
    """The last name associated with the address.

    An address must have either a first last name or a business name.
    """

    locality: Required[str]
    """The locality of the address.

    For US addresses, this corresponds to the city of the address.
    """

    street_address: Required[str]
    """The primary street address information about the address."""

    address_book: bool
    """
    Indicates whether or not the address should be considered part of your list of
    addresses that appear for regular use.
    """

    administrative_area: str
    """The locality of the address.

    For US addresses, this corresponds to the state of the address.
    """

    borough: str
    """The borough of the address.

    This field is not used for addresses in the US but is used for some
    international addresses.
    """

    customer_reference: str
    """A customer reference string for customer look ups."""

    extended_address: str
    """
    Additional street address information about the address such as, but not limited
    to, unit number or apartment number.
    """

    neighborhood: str
    """The neighborhood of the address.

    This field is not used for addresses in the US but is used for some
    international addresses.
    """

    phone_number: str
    """The phone number associated with the address."""

    postal_code: str
    """The postal code of the address."""

    validate_address: bool
    """
    Indicates whether or not the address should be validated for emergency use upon
    creation or not. This should be left with the default value of `true` unless you
    have used the `/addresses/actions/validate` endpoint to validate the address
    separately prior to creation. If an address is not validated for emergency use
    upon creation and it is not valid, it will not be able to be used for emergency
    services.
    """
