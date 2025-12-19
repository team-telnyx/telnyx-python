# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .record import Record
from .._models import BaseModel

__all__ = ["NetworkDeleteResponse", "Data"]


class Data(Record):
    name: Optional[str] = None
    """A user specified name for the network."""


class NetworkDeleteResponse(BaseModel):
    data: Optional[Data] = None
