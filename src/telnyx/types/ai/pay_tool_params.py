# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PayToolParams"]


class PayToolParams(BaseModel):
    connector_name: str
    """The name of the pay connector configured in the Telnyx API.

    Must reference an existing pay connector for this organization.
    """

    connector_parameters: Optional[Dict[str, object]] = None
    """
    Custom key/value parameters forwarded to the pay connector as `parameters` in
    the processor request. String values may use `{{dynamic_variable}}` templating,
    resolved per call.
    """

    currency: Optional[str] = None
    """Default currency for payments processed by this tool."""

    description: Optional[str] = None
    """
    Description of the pay tool shown to the assistant so it knows when to call the
    tool. Not sent to the payment connector — the per-call `description` argument
    the assistant passes is what reaches the processor.
    """

    payment_method: Optional[str] = None
    """Default payment method for payments processed by this tool."""

    valid_card_types: Optional[
        List[Literal["visa", "mastercard", "amex", "maestro", "discover", "optima", "jcb", "diners-club", "enroute"]]
    ] = None
    """Restricts accepted card numbers to the listed card types.

    When the caller enters a card number that does not match one of the listed
    types, Pay treats the input as invalid and re-prompts for the card number.
    """
