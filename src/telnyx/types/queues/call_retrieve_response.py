# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .queue_call import QueueCall

__all__ = ["CallRetrieveResponse"]


class CallRetrieveResponse(BaseModel):
    data: Optional[QueueCall] = None
