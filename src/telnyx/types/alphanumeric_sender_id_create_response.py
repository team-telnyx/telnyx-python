# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .alphanumeric_sender_id import AlphanumericSenderID

__all__ = ["AlphanumericSenderIDCreateResponse"]


class AlphanumericSenderIDCreateResponse(BaseModel):
    data: Optional[AlphanumericSenderID] = None
