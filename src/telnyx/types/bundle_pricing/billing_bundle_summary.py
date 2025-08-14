# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["BillingBundleSummary"]


class BillingBundleSummary(BaseModel):
    id: str
    """Bundle's ID, this is used to identify the bundle in the API."""

    cost_code: str
    """Bundle's cost code, this is used to identify the bundle in the billing system."""

    created_at: date
    """Date the bundle was created."""

    is_public: bool
    """Available to all customers or only to specific customers."""

    name: str
    """Bundle's name, this is used to identify the bundle in the UI."""

    currency: Optional[str] = None
    """Bundle's currency code."""

    mrc_price: Optional[float] = None
    """Monthly recurring charge price."""

    slug: Optional[str] = None
    """Slugified version of the bundle's name."""

    specs: Optional[List[str]] = None
