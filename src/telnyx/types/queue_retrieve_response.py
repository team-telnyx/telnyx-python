# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .queue import Queue
from .._models import BaseModel

__all__ = ["QueueRetrieveResponse"]


class QueueRetrieveResponse(BaseModel):
    data: Optional[Queue] = None
