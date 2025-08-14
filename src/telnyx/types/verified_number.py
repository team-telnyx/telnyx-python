# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerifiedNumber"]


class VerifiedNumber(BaseModel):
    phone_number: Optional[str] = None

    record_type: Optional[Literal["verified_number"]] = None
    """The possible verified numbers record types."""

    verified_at: Optional[str] = None
