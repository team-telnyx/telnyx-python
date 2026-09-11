# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .messaging_messaging_profile import MessagingMessagingProfile

__all__ = ["MessagingProfileUpdateResponse"]


class MessagingProfileUpdateResponse(BaseModel):
    data: Optional[MessagingMessagingProfile] = None
