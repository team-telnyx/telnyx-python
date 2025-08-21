# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InvoiceRetrieveParams"]


class InvoiceRetrieveParams(TypedDict, total=False):
    action: Literal["json", "link"]
    """Invoice action"""
