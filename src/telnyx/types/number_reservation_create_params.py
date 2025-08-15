# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .reserved_phone_number_param import ReservedPhoneNumberParam

__all__ = ["NumberReservationCreateParams"]


class NumberReservationCreateParams(TypedDict, total=False):
    customer_reference: str
    """A customer reference string for customer look ups."""

    phone_numbers: Iterable[ReservedPhoneNumberParam]
