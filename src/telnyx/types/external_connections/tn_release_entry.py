# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TnReleaseEntry"]


class TnReleaseEntry(BaseModel):
    number_id: Optional[str] = None
    """Phone number ID from the Telnyx API."""

    phone_number: Optional[str] = None
    """Phone number in E164 format."""
