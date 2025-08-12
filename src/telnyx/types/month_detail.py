# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MonthDetail"]


class MonthDetail(BaseModel):
    mrc: str
    """Monthly recurring charge amount as decimal string"""

    quantity: int
    """Number of items"""

    otc: Optional[str] = None
    """One-time charge amount as decimal string"""
