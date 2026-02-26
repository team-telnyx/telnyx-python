# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RcsToItem"]


class RcsToItem(BaseModel):
    carrier: Optional[str] = None

    line_type: Optional[str] = None

    phone_number: Optional[str] = None

    status: Optional[str] = None
