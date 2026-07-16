# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PayToolParamsParam"]


class PayToolParamsParam(TypedDict, total=False):
    connector_name: Required[str]
    """The name of the pay connector configured in the Telnyx API.

    Must reference an existing pay connector for this organization.
    """

    currency: str
    """Default currency for payments processed by this tool."""

    description: Optional[str]
    """Optional description of the pay tool that will be passed to the assistant."""

    payment_method: str
    """Default payment method for payments processed by this tool."""
