# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .country_coverage import CountryCoverage

__all__ = ["CountryCoverageRetrieveCountryResponse"]


class CountryCoverageRetrieveCountryResponse(BaseModel):
    data: Optional[CountryCoverage] = None
