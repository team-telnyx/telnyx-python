# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ConsumedData"]


class ConsumedData(BaseModel):
    amount: Optional[str] = None

    unit: Optional[str] = None
