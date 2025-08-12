# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BillingBundleRetrieveResponse", "Data", "DataBundleLimit"]


class DataBundleLimit(BaseModel):
    id: str

    created_at: date

    metric: str

    service: str

    updated_at: date

    billing_service: Optional[str] = None

    country: Optional[str] = None
    """Use country_iso instead"""

    country_code: Optional[int] = None

    country_iso: Optional[str] = None

    direction: Optional[Literal["inbound", "outbound"]] = None
    """An enumeration."""

    limit: Optional[int] = None

    rate: Optional[str] = None

    types: Optional[List[str]] = None


class Data(BaseModel):
    id: str
    """Bundle's ID, this is used to identify the bundle in the API."""

    active: bool
    """If that bundle is active or not."""

    bundle_limits: List[DataBundleLimit]

    cost_code: str
    """Bundle's cost code, this is used to identify the bundle in the billing system."""

    created_at: date
    """Date the bundle was created."""

    is_public: bool
    """Available to all customers or only to specific customers."""

    name: str
    """Bundle's name, this is used to identify the bundle in the UI."""

    slug: Optional[str] = None
    """Slugified version of the bundle's name."""


class BillingBundleRetrieveResponse(BaseModel):
    data: Data
