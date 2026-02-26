# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CostInformation"]


class CostInformation(BaseModel):
    currency: Optional[str] = None
    """The ISO 4217 code for the currency."""

    monthly_cost: Optional[str] = None

    upfront_cost: Optional[str] = None
