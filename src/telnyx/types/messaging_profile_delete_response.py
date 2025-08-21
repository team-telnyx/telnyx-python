# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .messaging_profile import MessagingProfile

__all__ = ["MessagingProfileDeleteResponse"]


class MessagingProfileDeleteResponse(BaseModel):
    data: Optional[MessagingProfile] = None
