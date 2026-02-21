# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AlphanumericSenderIDRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the alphanumeric sender ID resource."""

    alphanumeric_sender_id: Optional[str] = None
    """The alphanumeric sender ID string."""

    messaging_profile_id: Optional[str] = None
    """The messaging profile this sender ID belongs to."""

    organization_id: Optional[str] = None
    """The organization that owns this sender ID."""

    record_type: Optional[Literal["alphanumeric_sender_id"]] = None

    us_long_code_fallback: Optional[str] = None
    """A US long code number to use as fallback when sending to US destinations."""


class AlphanumericSenderIDRetrieveResponse(BaseModel):
    data: Optional[Data] = None
