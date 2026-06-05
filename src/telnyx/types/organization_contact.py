# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["OrganizationContact"]


class OrganizationContact(BaseModel):
    email: str

    first_name: str

    job_title: str

    last_name: str

    phone_number: str
    """E.164 format with leading `+`."""
