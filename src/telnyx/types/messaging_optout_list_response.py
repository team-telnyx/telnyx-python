# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["MessagingOptoutListResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[datetime] = None
    """The timestamp when the opt-out was created"""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """
    Sending address (+E.164 formatted phone number, alphanumeric sender ID, or short
    code).
    """

    keyword: Optional[str] = None
    """The keyword that triggered the opt-out."""

    messaging_profile_id: Optional[str] = None
    """Unique identifier for a messaging profile."""

    to: Optional[str] = None
    """Receiving address (+E.164 formatted phone number or short code)."""


class MessagingOptoutListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
