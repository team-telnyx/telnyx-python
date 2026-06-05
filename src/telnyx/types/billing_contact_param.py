# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BillingContactParam"]


class BillingContactParam(TypedDict, total=False):
    email: Required[str]

    first_name: Required[str]

    last_name: Required[str]

    phone_number: Required[str]
    """E.164 format with leading `+`."""
