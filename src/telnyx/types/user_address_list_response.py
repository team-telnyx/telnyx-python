# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["UserAddressListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the user address."""

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


class UserAddressListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
