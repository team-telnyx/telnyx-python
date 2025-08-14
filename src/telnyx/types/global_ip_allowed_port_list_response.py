# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["GlobalIPAllowedPortListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    first_port: Optional[int] = None
    """First port of a range."""

    last_port: Optional[int] = None
    """Last port of a range."""

    name: Optional[str] = None
    """A name for the Global IP ports range."""

    protocol_code: Optional[str] = None
    """The Global IP Protocol code."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class GlobalIPAllowedPortListResponse(BaseModel):
    data: Optional[List[Data]] = None
