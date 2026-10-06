# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BillingContactParam"]


class BillingContactParam(TypedDict, total=False):
    email: Required[str]
    """
    The email address of the person Telnyx should contact about billing for this
    account.
    """

    first_name: Required[str]
    """
    The first name of the person Telnyx should contact about billing for this
    account.
    """

    last_name: Required[str]
    """
    The last name of the person Telnyx should contact about billing for this
    account.
    """

    phone_number: Required[str]
    """
    The phone number of the billing contact, in E.164 format, for example
    +12125551234.
    """
