# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .country_coverage import CountryCoverage

__all__ = ["CountryCoverageRetrieveResponse"]


class CountryCoverageRetrieveResponse(BaseModel):
    data: Optional[Dict[str, CountryCoverage]] = None
