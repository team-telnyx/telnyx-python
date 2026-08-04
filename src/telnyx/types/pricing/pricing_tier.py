# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional

from ..._models import BaseModel

__all__ = ["PricingTier"]


class PricingTier(BaseModel):
    max: Optional[int] = None
    """Upper bound of the tier (exclusive). Null means no upper limit."""

    min: int
    """Lower bound of the tier (inclusive)."""

    rate: Union[float, str]
    """Rate for this tier.

    Numeric for standard products, string for inference products.
    """
