# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PhoneNumberBlockCreateParams", "ActivationRange", "PhoneNumberRange"]


class PhoneNumberBlockCreateParams(TypedDict, total=False):
    activation_ranges: Required[Iterable[ActivationRange]]
    """Specifies the activation ranges for this porting phone number block.

    The activation range must be within the block range and should not overlap with
    other activation ranges.
    """

    phone_number_range: Required[PhoneNumberRange]


class ActivationRange(TypedDict, total=False):
    end_at: Required[str]
    """Specifies the end of the activation range.

    It must be no more than the end of the extension range.
    """

    start_at: Required[str]
    """Specifies the start of the activation range.

    Must be greater or equal the start of the extension range.
    """


class PhoneNumberRange(TypedDict, total=False):
    end_at: Required[str]
    """
    Specifies the end of the phone number range for this porting phone number block.
    """

    start_at: Required[str]
    """
    Specifies the start of the phone number range for this porting phone number
    block.
    """
