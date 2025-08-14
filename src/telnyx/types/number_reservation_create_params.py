# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["NumberReservationCreateParams", "PhoneNumber"]


class NumberReservationCreateParams(TypedDict, total=False):
    customer_reference: str
    """A customer reference string for customer look ups."""

    phone_numbers: Iterable[PhoneNumber]


class PhoneNumber(TypedDict, total=False):
    phone_number: str
