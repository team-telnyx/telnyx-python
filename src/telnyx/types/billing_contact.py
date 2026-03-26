# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BillingContact"]


class BillingContact(BaseModel):
    email: str
    """Contact's email address"""

    first_name: str
    """Contact's first name"""

    last_name: str
    """Contact's last name"""

    phone_number: str
    """Contact's phone number (10-15 digits)"""
