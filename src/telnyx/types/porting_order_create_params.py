# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PortingOrderCreateParams"]


class PortingOrderCreateParams(TypedDict, total=False):
    phone_numbers: Required[SequenceNotStr[str]]
    """The list of +E.164 formatted phone numbers"""

    customer_reference: str
    """A customer-specified reference number for customer bookkeeping purposes"""
