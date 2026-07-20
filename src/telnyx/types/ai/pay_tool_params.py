# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["PayToolParams"]


class PayToolParams(BaseModel):
    connector_name: str
    """The name of the pay connector configured in the Telnyx API.

    Must reference an existing pay connector for this organization.
    """

    currency: Optional[str] = None
    """Default currency for payments processed by this tool."""

    description: Optional[str] = None
    """Optional description of the pay tool that will be passed to the assistant."""

    payment_method: Optional[str] = None
    """Default payment method for payments processed by this tool."""
