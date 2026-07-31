# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Reference"]


class Reference(BaseModel):
    """A reference (business or financial) on a DIR, in the customer-facing shape.

    No internal identifiers are exposed.
    """

    full_name: str
    """Full name of the reference contact."""

    phone_e164: str
    """Reference phone number in E.164 format."""

    record_type: Literal["dir_reference"]
    """Always `dir_reference`."""

    ref_type: Literal["business", "financial"]
    """Whether this is a business reference or the financial reference."""

    slot: int
    """Position within the reference type, counting from 1.

    Business references occupy slots 1 and 2, in the order they were sent in the
    `business_references` array; the financial reference occupies slot 1. Use this
    value together with `ref_type` to address the reference when updating it.
    """

    timezone: str
    """IANA timezone id for the reference.

    Calls are only placed within the reference's local 8am-9pm window.
    """

    email: Optional[str] = None
    """Reference contact email address."""

    job_title: Optional[str] = None
    """Job title of the reference contact."""

    organization: Optional[str] = None
    """Organization the reference contact belongs to."""

    relationship_to_registrant: Optional[str] = None
    """How the reference contact is related to the registering business."""
