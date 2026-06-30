# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..porting_order import PortingOrder

__all__ = ["ActionConfirmResponse", "Meta"]


class Meta(BaseModel):
    phone_numbers_url: Optional[str] = None
    """Link to list all phone numbers"""


class ActionConfirmResponse(BaseModel):
    data: Optional[PortingOrder] = None

    meta: Optional[Meta] = None
