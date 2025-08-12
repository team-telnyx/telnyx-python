# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NumberLookupRetrieveParams"]


class NumberLookupRetrieveParams(TypedDict, total=False):
    type: Literal["carrier", "caller-name"]
    """Specifies the type of number lookup to be performed"""
