# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PortingOrderRetrieveParams"]


class PortingOrderRetrieveParams(TypedDict, total=False):
    include_phone_numbers: bool
    """Include the first 50 phone number objects in the results"""
