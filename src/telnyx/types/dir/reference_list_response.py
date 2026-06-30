# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ReferenceListResponse", "Data"]


class Data(BaseModel):
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
    """Position within the reference type.

    Business references occupy slots 0 and 1; the financial reference occupies
    slot 0.
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


class ReferenceListResponse(BaseModel):
    data: List[Data]
