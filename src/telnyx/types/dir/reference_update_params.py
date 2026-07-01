# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReferenceUpdateParams"]


class ReferenceUpdateParams(TypedDict, total=False):
    dir_id: Required[str]

    ref_type: Required[Literal["business", "financial"]]

    email: str
    """Reference contact email address."""

    full_name: str
    """Full name of the reference contact."""

    job_title: Optional[str]
    """Job title of the reference contact."""

    organization: Optional[str]
    """Organization the reference contact belongs to."""

    phone_e164: str
    """Reference phone number in E.164 format."""

    relationship_to_registrant: Optional[str]
    """How the reference contact is related to the registering business."""

    timezone: str
    """IANA timezone id for the reference."""
