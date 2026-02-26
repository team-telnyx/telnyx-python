# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["QueueRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str
    """Uniquely identifies the queue"""

    average_wait_time_secs: int
    """
    The average time that the calls currently in the queue have spent waiting, given
    in seconds.
    """

    created_at: str
    """ISO 8601 formatted date of when the queue was created"""

    current_size: int
    """The number of calls currently in the queue"""

    max_size: int
    """The maximum number of calls allowed in the queue"""

    name: str
    """Name of the queue"""

    record_type: Literal["queue"]

    updated_at: str
    """ISO 8601 formatted date of when the queue was last updated"""


class QueueRetrieveResponse(BaseModel):
    data: Optional[Data] = None
