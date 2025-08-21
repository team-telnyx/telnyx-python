# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .record import Record
from .._models import BaseModel

__all__ = ["NetworkCreateResponse", "Data"]


class Data(Record):
    name: Optional[str] = None
    """A user specified name for the network."""

    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""


class NetworkCreateResponse(BaseModel):
    data: Optional[Data] = None
