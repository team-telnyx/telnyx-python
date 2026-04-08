# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrganizationContactParam"]


class OrganizationContactParam(TypedDict, total=False):
    """Organization contact information.

    Note: the response returns this object with the phone field as 'phone' (not 'phone_number').
    """

    email: Required[str]
    """Contact's email address"""

    first_name: Required[str]
    """Contact's first name"""

    job_title: Required[str]
    """Contact's job title (required)"""

    last_name: Required[str]
    """Contact's last name"""

    phone: Required[str]
    """Contact's phone number in E.164 format"""
