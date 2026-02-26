# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RegionInformation"]


class RegionInformation(BaseModel):
    region_name: Optional[str] = None

    region_type: Optional[Literal["country_code", "rate_center", "state", "location"]] = None
