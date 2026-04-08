# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["OrganizationContact"]


class OrganizationContact(BaseModel):
    """Organization contact information.

    Note: the response returns this object with the phone field as 'phone' (not 'phone_number').
    """

    email: str
    """Contact's email address"""

    first_name: str
    """Contact's first name"""

    job_title: str
    """Contact's job title (required)"""

    last_name: str
    """Contact's last name"""

    phone: str
    """Contact's phone number in E.164 format"""
