# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .porting_associated_phone_number import PortingAssociatedPhoneNumber

__all__ = ["AssociatedPhoneNumberCreateResponse"]


class AssociatedPhoneNumberCreateResponse(BaseModel):
    data: Optional[PortingAssociatedPhoneNumber] = None
