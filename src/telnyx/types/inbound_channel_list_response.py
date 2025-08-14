# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["InboundChannelListResponse", "Data"]


class Data(BaseModel):
    channels: Optional[int] = None
    """The current number of concurrent channels set for the account"""

    record_type: Optional[str] = None
    """Identifies the type of the response"""


class InboundChannelListResponse(BaseModel):
    data: Optional[Data] = None
