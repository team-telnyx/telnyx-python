# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["BillingContact"]


class BillingContact(BaseModel):
    email: str
    """
    The email address of the person Telnyx should contact about billing for this
    account.
    """

    first_name: str
    """
    The first name of the person Telnyx should contact about billing for this
    account.
    """

    last_name: str
    """
    The last name of the person Telnyx should contact about billing for this
    account.
    """

    phone_number: str
    """
    The phone number of the billing contact, in E.164 format, for example
    +12125551234.
    """
