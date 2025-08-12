# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RegionIn"]


class RegionIn(BaseModel):
    region_code: Optional[str] = None
    """The region the interface should be deployed to."""
