# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentGatewayRetrieveModelsResponse", "Data", "DataPricing"]


class DataPricing(BaseModel):
    """A model's price in USD per million tokens."""

    cached_input: Optional[float] = None
    """USD per million cached input tokens."""

    currency: str
    """Always `USD`."""

    input: float
    """USD per million input tokens."""

    output: float
    """USD per million output tokens."""

    unit: str
    """Always `1M_tokens`."""


class Data(BaseModel):
    """A model an instance serves."""

    id: str
    """The model's ID on the instance."""

    model: str
    """The Telnyx Inference model behind it, such as `zai-org/GLM-5.3-Flash`."""

    name: str
    """The name a request uses, such as `GLM-5.3-Flash`."""

    priced_at: Optional[datetime] = None
    """When the price was last set."""

    pricing: DataPricing
    """A model's price in USD per million tokens."""


class AgentGatewayRetrieveModelsResponse(BaseModel):
    data: List[Data]
