# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AssociatedPhoneNumberCreateParams", "PhoneNumberRange"]


class AssociatedPhoneNumberCreateParams(TypedDict, total=False):
    action: Required[Literal["keep", "disconnect"]]
    """Specifies the action to take with this phone number during partial porting."""

    phone_number_range: Required[PhoneNumberRange]


class PhoneNumberRange(TypedDict, total=False):
    end_at: str
    """Specifies the end of the phone number range for this associated phone number."""

    start_at: str
    """Specifies the start of the phone number range for this associated phone number."""
