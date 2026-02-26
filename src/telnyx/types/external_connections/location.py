# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Location"]


class Location(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the resource."""

    additional_info: Optional[str] = None

    description: Optional[str] = None

    is_default: Optional[bool] = None
    """Represents whether the location is the default or not."""
