# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PortabilityCheckRunResponse", "Data"]


class Data(BaseModel):
    fast_portable: Optional[bool] = None
    """Indicates whether this phone number is FastPort eligible"""

    not_portable_reason: Optional[str] = None
    """If this phone number is not portable, explains why.

    Empty string if the number is portable.
    """

    phone_number: Optional[str] = None
    """The +E.164 formatted phone number this result is about"""

    portable: Optional[bool] = None
    """Indicates whether this phone number is portable"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class PortabilityCheckRunResponse(BaseModel):
    data: Optional[List[Data]] = None
