# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReferenceInputParam"]


class ReferenceInputParam(TypedDict, total=False):
    """One reference supplied at submit.

    The reference type is implied by the field that carries it (business_references vs financial_reference).
    """

    email: Required[str]
    """Reference contact email address.

    Required: the reference is emailed scheduling and dial-in notices.
    """

    full_name: Required[str]
    """Full name of the reference contact."""

    phone_e164: Required[str]
    """Reference phone number in E.164 format, e.g. +14155550123."""

    timezone: Required[str]
    """IANA timezone id for the reference (e.g.

    America/New_York). Required: calls are only placed within the reference's local
    8am-9pm window.
    """

    job_title: Optional[str]
    """Job title of the reference contact."""

    organization: Optional[str]
    """Organization the reference contact belongs to."""

    relationship_to_registrant: Optional[str]
    """How the reference contact is related to the registering business."""
