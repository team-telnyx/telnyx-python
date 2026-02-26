# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .queue import Queue
from .._models import BaseModel

__all__ = ["QueueUpdateResponse"]


class QueueUpdateResponse(BaseModel):
    data: Optional[Queue] = None
