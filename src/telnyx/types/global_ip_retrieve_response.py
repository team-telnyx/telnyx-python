# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .record import Record
from .._models import BaseModel

__all__ = ["GlobalIPRetrieveResponse", "Data"]


class Data(Record):
    description: Optional[str] = None
    """A user specified description for the address."""

    ip_address: Optional[str] = None
    """The Global IP address."""

    name: Optional[str] = None
    """A user specified name for the address."""

    ports: Optional[Dict[str, object]] = None
    """A Global IP ports grouped by protocol code."""


class GlobalIPRetrieveResponse(BaseModel):
    data: Optional[Data] = None
