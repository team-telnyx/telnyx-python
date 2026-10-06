# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrganizationContactParam"]


class OrganizationContactParam(TypedDict, total=False):
    email: Required[str]
    """The email address of the main person Telnyx should contact about this account.

    For a call center (BPO) account this is the email you will verify later, so use
    a mailbox you can access.
    """

    first_name: Required[str]
    """The first name of the main person Telnyx should contact about this account."""

    job_title: Required[str]
    """The job title of the main person Telnyx should contact about this account."""

    last_name: Required[str]
    """The last name of the main person Telnyx should contact about this account."""

    phone_number: Required[str]
    """
    The phone number of the main contact, in E.164 format, for example +12125551234.
    """
