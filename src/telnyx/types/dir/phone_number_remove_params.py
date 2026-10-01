# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["PhoneNumberRemoveParams"]


class PhoneNumberRemoveParams(TypedDict, total=False):
    phone_numbers: Required[SequenceNotStr[str]]
    """
    The phone numbers to remove from this brand, in E.164 format, up to 100 per
    request. They must currently be attached to this brand.
    """
