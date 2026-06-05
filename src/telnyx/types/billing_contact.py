# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BillingContact"]


class BillingContact(BaseModel):
    email: str

    first_name: str

    last_name: str

    phone_number: str
    """E.164 format with leading `+`."""
