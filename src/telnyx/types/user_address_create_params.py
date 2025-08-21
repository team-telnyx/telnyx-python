# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserAddressCreateParams"]


class UserAddressCreateParams(TypedDict, total=False):
    business_name: Required[str]
    """The business name associated with the user address."""

    country_code: Required[str]
    """The two-character (ISO 3166-1 alpha-2) country code of the user address."""

    first_name: Required[str]
    """The first name associated with the user address."""

    last_name: Required[str]
    """The last name associated with the user address."""

    locality: Required[str]
    """The locality of the user address.

    For US addresses, this corresponds to the city of the address.
    """

    street_address: Required[str]
    """The primary street address information about the user address."""

    administrative_area: str
    """The locality of the user address.

    For US addresses, this corresponds to the state of the address.
    """

    borough: str
    """The borough of the user address.

    This field is not used for addresses in the US but is used for some
    international addresses.
    """

    customer_reference: str
    """A customer reference string for customer look ups."""

    extended_address: str
    """
    Additional street address information about the user address such as, but not
    limited to, unit number or apartment number.
    """

    neighborhood: str
    """The neighborhood of the user address.

    This field is not used for addresses in the US but is used for some
    international addresses.
    """

    phone_number: str
    """The phone number associated with the user address."""

    postal_code: str
    """The postal code of the user address."""

    skip_address_verification: str
    """
    An optional boolean value specifying if verification of the address should be
    skipped or not. UserAddresses are generally used for shipping addresses, and
    failure to validate your shipping address will likely result in a failure to
    deliver SIM cards or other items ordered from Telnyx. Do not use this parameter
    unless you are sure that the address is correct even though it cannot be
    validated. If this is set to any value other than true, verification of the
    address will be attempted, and the user address will not be allowed if
    verification fails. If verification fails but suggested values are available
    that might make the address correct, they will be present in the response as
    well. If this value is set to true, then the verification will not be attempted.
    Defaults to false (verification will be performed).
    """
