# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AgentConsentConfiguration", "OptInMethod"]


class OptInMethod(BaseModel):
    method_type: Literal["SMS", "WEBSITE", "MOBILE_APP", "QR_CODE", "SALE_POINT", "OTHER"]

    description: Optional[str] = None
    """Required when method_type is `OTHER`."""


class AgentConsentConfiguration(BaseModel):
    call_to_action: str

    double_opt_in: bool

    help_response: str

    opt_in_message: str

    opt_in_methods: List[OptInMethod]

    opt_out_response: str

    call_to_action_media_url: Optional[str] = None
    """Required when an opt-in method is `WEBSITE` or `MOBILE_APP`."""

    call_to_action_url: Optional[str] = None
    """Required when an opt-in method is `WEBSITE`."""

    double_opt_in_message: Optional[str] = None
    """Required when double_opt_in is true."""
