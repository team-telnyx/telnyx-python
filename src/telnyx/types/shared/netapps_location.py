# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["NetappsLocation"]


class NetappsLocation(BaseModel):
    code: Optional[str] = None
    """Location code."""

    name: Optional[str] = None
    """Human readable name of location."""

    pop: Optional[str] = None
    """Point of presence of location."""

    region: Optional[str] = None
    """Identifies the geographical region of location."""

    site: Optional[str] = None
    """Site of location."""
