# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SimCardOrderPreviewPreviewResponse", "Data", "DataShippingCost", "DataSimCardsCost", "DataTotalCost"]


class DataShippingCost(BaseModel):
    amount: Optional[str] = None
    """A string representing the cost amount."""

    currency: Optional[str] = None
    """ISO 4217 currency string."""


class DataSimCardsCost(BaseModel):
    amount: Optional[str] = None
    """A string representing the cost amount."""

    currency: Optional[str] = None
    """ISO 4217 currency string."""


class DataTotalCost(BaseModel):
    amount: Optional[str] = None
    """A string representing the cost amount."""

    currency: Optional[str] = None
    """ISO 4217 currency string."""


class Data(BaseModel):
    quantity: Optional[int] = None
    """The amount of SIM cards requested in the SIM card order."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    shipping_cost: Optional[DataShippingCost] = None

    sim_cards_cost: Optional[DataSimCardsCost] = None

    total_cost: Optional[DataTotalCost] = None


class SimCardOrderPreviewPreviewResponse(BaseModel):
    data: Optional[Data] = None
