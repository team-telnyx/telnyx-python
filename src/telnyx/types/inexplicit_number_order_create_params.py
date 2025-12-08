# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["InexplicitNumberOrderCreateParams", "OrderingGroup", "OrderingGroupPhoneNumber"]


class InexplicitNumberOrderCreateParams(TypedDict, total=False):
    ordering_groups: Required[Iterable[OrderingGroup]]
    """Group(s) of numbers to order.

    You can have multiple ordering_groups objects added to a single request.
    """

    billing_group_id: str
    """Billing group id to apply to phone numbers that are purchased"""

    connection_id: str
    """Connection id to apply to phone numbers that are purchased"""

    customer_reference: str
    """Reference label for the customer"""

    messaging_profile_id: str
    """Messaging profile id to apply to phone numbers that are purchased"""


class OrderingGroupPhoneNumber(TypedDict, total=False):
    """Phone number search criteria"""

    contains: str
    """Filter for phone numbers that contain the digits specified"""

    ends_with: str
    """Filter by the ending digits of the phone number"""

    starts_with: str
    """Filter by the starting digits of the phone number"""


class OrderingGroup(TypedDict, total=False):
    count_requested: Required[str]
    """Quantity of phone numbers to order"""

    country_iso: Required[Literal["US", "CA"]]
    """Country where you would like to purchase phone numbers.

    Allowable values: US, CA
    """

    phone_number_type: Required[str]
    """Number type (local, toll-free, etc.)"""

    administrative_area: str
    """Filter for phone numbers in a given state / province"""

    exclude_held_numbers: bool
    """
    Filter to exclude phone numbers that are currently on hold/reserved for your
    account.
    """

    features: SequenceNotStr[str]
    """
    Filter for phone numbers that have the features to satisfy your use case (e.g.,
    ["voice"])
    """

    locality: str
    """Filter for phone numbers in a given city / region / rate center"""

    national_destination_code: str
    """Filter by area code"""

    phone_number: OrderingGroupPhoneNumber
    """Phone number search criteria"""

    quickship: bool
    """
    Filter to exclude phone numbers that need additional time after to purchase to
    activate. Only applicable for +1 toll_free numbers.
    """

    strategy: Literal["always", "never"]
    """Ordering strategy.

    Define what action should be taken if we don't have enough phone numbers to
    fulfill your request. Allowable values are: always = proceed with ordering phone
    numbers, regardless of current inventory levels; never = do not place any orders
    unless there are enough phone numbers to satisfy the request. If not specified,
    the always strategy will be enforced.
    """
