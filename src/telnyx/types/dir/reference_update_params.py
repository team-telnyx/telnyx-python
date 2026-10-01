# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReferenceUpdateParams"]


class ReferenceUpdateParams(TypedDict, total=False):
    dir_id: Required[str]

    ref_type: Required[Literal["business", "financial"]]

    email: str
    """The reference's email address.

    We email them scheduling and dial-in instructions before we call, so use an
    address they check.
    """

    full_name: str
    """The full name of the person we should contact as your reference."""

    job_title: Optional[str]
    """The reference contact's job title, for example CFO or Owner."""

    organization: Optional[str]
    """The name of the organization the reference contact works for."""

    phone_e164: str
    """The reference's phone number in E.164 format, for example +14155550123.

    We call this number during their local business hours.
    """

    relationship_to_registrant: Optional[str]
    """How the reference contact is related to the registering business."""

    timezone: str
    """The reference's IANA time zone, for example America/New_York.

    We only call during their local 8am to 9pm hours, which is why we need it.
    """
