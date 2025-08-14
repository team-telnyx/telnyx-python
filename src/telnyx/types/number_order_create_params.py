# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["NumberOrderCreateParams", "PhoneNumber"]


class NumberOrderCreateParams(TypedDict, total=False):
    billing_group_id: str
    """Identifies the billing group associated with the phone number."""

    connection_id: str
    """Identifies the connection associated with this phone number."""

    customer_reference: str
    """A customer reference string for customer look ups."""

    messaging_profile_id: str
    """Identifies the messaging profile associated with the phone number."""

    phone_numbers: Iterable[PhoneNumber]


class PhoneNumber(TypedDict, total=False):
    phone_number: Required[str]
    """e164_phone_number"""

    bundle_id: str
    """ID of bundle to associate the number to"""

    requirement_group_id: str
    """ID of requirement group to use to satisfy number requirements"""
