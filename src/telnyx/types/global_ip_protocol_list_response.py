# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["GlobalIPProtocolListResponse", "Data"]


class Data(BaseModel):
    code: Optional[str] = None
    """The Global IP Protocol code."""

    name: Optional[str] = None
    """A name for Global IP Protocol."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class GlobalIPProtocolListResponse(BaseModel):
    data: Optional[List[Data]] = None
