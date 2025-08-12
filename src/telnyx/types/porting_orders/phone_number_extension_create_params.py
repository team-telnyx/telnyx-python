# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PhoneNumberExtensionCreateParams", "ActivationRange", "ExtensionRange"]


class PhoneNumberExtensionCreateParams(TypedDict, total=False):
    activation_ranges: Required[Iterable[ActivationRange]]
    """Specifies the activation ranges for this porting phone number extension.

    The activation range must be within the extension range and should not overlap
    with other activation ranges.
    """

    extension_range: Required[ExtensionRange]

    porting_phone_number_id: Required[str]
    """
    Identifies the porting phone number associated with this porting phone number
    extension.
    """


class ActivationRange(TypedDict, total=False):
    end_at: Required[int]
    """Specifies the end of the activation range.

    It must be no more than the end of the extension range.
    """

    start_at: Required[int]
    """Specifies the start of the activation range.

    Must be greater or equal the start of the extension range.
    """


class ExtensionRange(TypedDict, total=False):
    end_at: Required[int]
    """
    Specifies the end of the extension range for this porting phone number
    extension.
    """

    start_at: Required[int]
    """
    Specifies the start of the extension range for this porting phone number
    extension.
    """
