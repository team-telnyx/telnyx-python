# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .spend_limit import SpendLimit

__all__ = ["SpendLimitResponse"]


class SpendLimitResponse(BaseModel):
    data: SpendLimit
    """The spend limit, spend and block state of one product and period."""
