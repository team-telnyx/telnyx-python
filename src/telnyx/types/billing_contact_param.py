# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BillingContactParam"]


class BillingContactParam(TypedDict, total=False):
    email: Required[str]
    """Contact's email address"""

    first_name: Required[str]
    """Contact's first name"""

    last_name: Required[str]
    """Contact's last name"""

    phone_number: Required[str]
    """Contact's phone number (10-15 digits)"""
