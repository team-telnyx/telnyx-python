# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SimCardOrder", "Cost", "OrderAddress"]


class Cost(BaseModel):
    amount: Optional[str] = None
    """A string representing the cost amount."""

    currency: Optional[str] = None
    """Filter by ISO 4217 currency string."""


class OrderAddress(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the address for the order."""

    administrative_area: Optional[str] = None
    """State or province where the address is located."""

    business_name: Optional[str] = None
    """The name of the business where the address is located."""

    country_code: Optional[str] = None
    """The mobile operator two-character (ISO 3166-1 alpha-2) origin country code."""

    extended_address: Optional[str] = None
    """Supplemental field for address information."""

    first_name: Optional[str] = None
    """The first name of the shipping recipient."""

    last_name: Optional[str] = None
    """The last name of the shipping recipient."""

    locality: Optional[str] = None
    """The name of the city where the address is located."""

    postal_code: Optional[str] = None
    """Postal code for the address."""

    street_address: Optional[str] = None
    """The name of the street where the address is located."""


class SimCardOrder(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    cost: Optional[Cost] = None
    """An object representing the total cost of the order."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was last created."""

    order_address: Optional[OrderAddress] = None
    """
    An object representing the address information from when the order was
    submitted.
    """

    quantity: Optional[int] = None
    """The amount of SIM cards requested in the SIM card order."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    status: Optional[Literal["pending", "processing", "ready_to_ship", "shipped", "delivered", "canceled"]] = None
    """
    The current status of the SIM Card order.<ul> <li><code>pending</code> - the
    order is waiting to be processed.</li> <li><code>processing</code> - the order
    is currently being processed.</li> <li><code>ready_to_ship</code> - the order is
    ready to be shipped to the specified <b>address</b>.</li>
    <li><code>shipped</code> - the order was shipped and is on its way to be
    delivered to the specified <b>address</b>.</li> <li><code>delivered</code> - the
    order was delivered to the specified <b>address</b>.</li>
    <li><code>canceled</code> - the order was canceled.</li> </ul>
    """

    tracking_url: Optional[str] = None
    """The URL used to get tracking information about the order."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was last updated."""
